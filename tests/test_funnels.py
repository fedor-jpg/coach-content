"""Synthetic offline fixtures only. No native account, conversational eval or E2E run."""

import argparse
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("funnels", ROOT / "plugin/scripts/funnels.py")
funnels = importlib.util.module_from_spec(spec)
spec.loader.exec_module(funnels)
ENV = {"host": "synthetic-cowork-fixture", "model": "synthetic-model", "connector_contract": "schema-fixture-2026-10-30"}
IDS = {"inro-" + suffix for suffix in (
    "comment-moderation", "6085", "4530", "6111", "6018", "6082", "6086", "6025", "6220", "6028",
    "6223", "6023", "6081", "4484", "6024", "6049", "6051", "6026", "6022", "6027", "6054",
    "6021", "6080", "4393", "6053", "6222", "6047", "6046", "6045", "6019")}


def now():
    return datetime.now(timezone.utc).isoformat()


def business(value):
    parameters = {}
    for key in value["required_inputs"]:
        field = value["allowed_parameters"][key]
        parameters[key] = (["fixture-post"] if field["type"] == "post_ids" else
                           "https://example.org/" + key if field["type"] == "url" else
                           "Approved fixture " + key)
    parameters.update({key: val for key, val in {"keyword": "GUIDE", "language": "English", "next_step": "handoff"}.items() if key in parameters})
    if value["family"] == "waitlist":
        parameters.update({"membership_attribute": "coach_fixture_campaign_launch", "consent_text": "Reply YES to join this launch. Reply STOP to withdraw."})
    if value["id"] == "inro-6019":
        parameters["profile_url"] = "https://www.instagram.com/fixture_coach/"
    for key in ("public", "initial", "refusal", "handoff"):
        field = key + "_text"
        if field in parameters:
            parameters[field] = value["messages"][key].format_map(parameters)
    initial = parameters.get("initial_text", "")
    for key in value["initial_required_parameters"]:
        if key in parameters and str(parameters[key]) not in initial:
            initial += " " + str(parameters[key])
    if "initial_text" in parameters:
        parameters["initial_text"] = initial
    return {"campaign_id": "fixture-campaign", "parameters": parameters, "accepted_changes": value["design_changes"]}


def rule(identifier, scope, base, enabled, inherited=None):
    settings = {
        "incomingMessages": {"howToReply": "UsingAI", "messagePrompt": "Keep ordinary support and another campaign unchanged."},
        "followUps": {"howToSend": "DontSend", "messagePrompt": "No follow-ups."},
        "switchToHuman": {"howToSwitch": "SwitchToTeammates", "rules": [{"switchingConditions": "Existing support escalation.", "messagePrompt": "Existing team reply."}]},
        "collectContactInfo": {"howToCollect": "CollectInfo", "captures": [{"name": "existing_support_email", "description": "Existing support capture."}]},
        "whenAIReplies": {"option": "Always"},
    }
    if scope == "InstagramPostComments":
        settings.update({"listOfPosts": {"postIDs": []}, "keywords": {"reactTo": "AnyComment", "keywords": []},
                         "publicReply": {"publicReplyHowToReply": "ExactText", "exactTextReply": "Existing public reply.", "messagePrompt": "Existing public prompt.", "likeContactComment": False},
                         "privateReply": {"privateReplyHowToReply": "ExactText", "exactTextReply": "Existing private reply.", "messagePrompt": "Existing private prompt."}})
    for config in settings.values():
        config["inheritsFrom"] = inherited
    return {"id": identifier, "scope": scope, "isBase": base, "enabled": enabled, "settings": settings}


def state(value, owned=True):
    rules = [rule("fixture-main", "All", True, True), rule("fixture-comment-base", "InstagramPostComments", True, True),
             rule("fixture-dm", "InstagramDirectMessages", True, True)]
    result = {"schema_version": 1, "read_complete": True, "observed_at": now(), "account_id": "fixture-account",
              "bot_id": "fixture-bot", "platform": "Instagram", "connected": True, "ai_compatible": True,
              "posts": ["fixture-post"], "rules": rules, "environment": ENV, "actions": [], "instagram_username": "fixture_coach",
              "known_attribute_names": ["existing_support_email"], "attribute_namespace_complete": True}
    if value["entry"] in {"comment", "public"} and owned:
        own = rule("fixture-owned", "InstagramPostComments", False, False, "fixture-comment-base")
        rules.append(own)
        result["ownership"] = {"campaign_id": "fixture-campaign", "recipe_id": value["id"], "account_id": result["account_id"],
                               "rule_id": own["id"], "rule_sha256": funnels.fingerprint(own)}
    return result


def apply_commands(original, operations):
    result = copy.deepcopy(original)
    result["observed_at"] = now()
    rules = {item["id"]: item for item in result["rules"]}
    for operation in operations:
        variables = operation["variables"]
        if operation["operation"] == "fuelyAutomationSetEnabled":
            rules[variables["id"]]["enabled"] = variables["enabled"]
            continue
        for name, wrapper in variables["update"].items():
            if "setInheritFrom" in wrapper:
                parent = wrapper["setInheritFrom"]
                config = funnels.setting(rules[parent], name)
                rules[variables["id"]]["settings"][name] = {**config, "inheritsFrom": parent}
            else:
                rules[variables["id"]]["settings"][name] = {**copy.deepcopy(wrapper["update"]), "inheritsFrom": None}
    return result


def readback(plan, original, phase="configure"):
    operations = plan["commands"] + (plan["activation"] if phase in {"activation", "enabled"} else [])
    if phase == "enabled":
        operations += plan["enable"]
    return apply_commands(original, operations)


def native_shaped_state(value, dm_enabled=False, active=False):
    current = state(value)
    for item in current["rules"]:
        item["settings"]["switchToHuman"]["howToSwitch"] = "SwitchToTeammates" if active else "DontSwitch"
        item["settings"]["collectContactInfo"]["howToCollect"] = "CollectInfo" if active else "DoNotCollectInfo"
    current["rules"][2]["enabled"] = dm_enabled
    for item in current["rules"][1:]:
        for name in ("incomingMessages", "followUps", "switchToHuman", "collectContactInfo", "whenAIReplies"):
            item["settings"][name] = {**copy.deepcopy(current["rules"][0]["settings"][name]), "inheritsFrom": "fixture-main"}
    if "ownership" in current:
        current["ownership"]["rule_sha256"] = funnels.fingerprint(current["rules"][-1])
    return current


def export_qa(baseline=None, cases=None, owned_rule_id=None, refresh_observed_at=False):
    if cases is None:
        cases = [{"id": identifier, "fixture": True, "business": business(funnels.recipe(identifier))}
                 for identifier in sorted(IDS) if not funnels.recipe(identifier)["blockers"]
                 and funnels.recipe(identifier)["status"] not in {"unavailable", "unverified"}]
    funnels.require(isinstance(cases, list) and len({row["id"] for row in cases}) == len(cases), "QA cases must have unique IDs")
    rows = []
    for case in cases:
        value = funnels.recipe(case["id"])
        current = copy.deepcopy(baseline) if baseline else native_shaped_state(value)
        data = copy.deepcopy(case["business"])
        if refresh_observed_at:
            current["observed_at"] = now()
        if value["entry"] in {"comment", "public"}:
            identifier = owned_rule_id if baseline else "fixture-owned"
            own = next((item for item in current["rules"] if item["id"] == identifier), None)
            funnels.require(own is not None and not own["isBase"] and not own["enabled"] and own["scope"] == "InstagramPostComments", "Provide the actual approved OFF QA custom ID")
            current["ownership"] = {"campaign_id": data["campaign_id"], "recipe_id": value["id"], "account_id": current["account_id"],
                                    "rule_id": identifier, "rule_sha256": funnels.fingerprint(own)}
        else:
            current.pop("ownership", None)
        try:
            plan = funnels.prepare(value, data, current, developer_qa=True)
        except (ValueError, KeyError, TypeError) as error:
            rows.append({"id": value["id"], "business_fixture": case.get("fixture", True), "business": data,
                         "snapshot": current, "blocking_error": str(error)})
            continue
        rows.append({"id": value["id"], "business_fixture": case.get("fixture", True), "business": data,
                     "snapshot": current, "plan": plan})
    return {"schema_version": 1, "purpose": "offline-rendered QA plans; never runtime receipts or acceptance",
            "snapshot_source": "provided-native-normalized" if baseline else "synthetic-offline",
            "timestamp_refreshed_by_request": refresh_observed_at, "runtime_accepted": False,
            "plan_count": sum("plan" in row for row in rows), "blocked_count": sum("blocking_error" in row for row in rows), "cases": rows}


def export_qa_cli(arguments):
    parser = argparse.ArgumentParser(description="Render actual prepare() plans only; never execute native commands")
    parser.add_argument("--state", type=Path)
    parser.add_argument("--inputs", type=Path)
    parser.add_argument("--owned-rule-id")
    parser.add_argument("--refresh-observed-at", action="store_true", help="Use only when the supplied native baseline remains unchanged")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(arguments)
    result = export_qa(funnels.load(args.state) if args.state else None, funnels.load(args.inputs) if args.inputs else None,
                       args.owned_rule_id, args.refresh_observed_at)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps({"path": str(args.output.resolve()), "plan_count": result["plan_count"], "blocked_count": result["blocked_count"], "runtime_accepted": False}))


def save_fixture(root, name, content):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(content, sort_keys=True), encoding="utf-8")
    return {"path": name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def synthetic_acceptance(root, value, next_steps=None, material=False):
    """Accepted-shaped records to exercise validation, NOT actual live receipts."""
    runs = []
    digest = funnels.recipe_digest(value)
    for number in range(3):
        current = state(value)
        account = f"synthetic-account-{number % 2}"
        current["account_id"] = account
        if "ownership" in current:
            current["ownership"]["account_id"] = account
        data = business(value)
        if "keyword" in data["parameters"]:
            data["parameters"]["keyword"] = "GUIDE" + str(number)
        else:
            data["parameters"]["known_facts"] += " " + str(number)
        if next_steps:
            data["parameters"]["next_step"] = next_steps[number]
            if next_steps[number] == "booking_link":
                data["parameters"]["booking_url"] = "https://example.org/book"
        if material:
            data["parameters"].update({"resource_title": "Decision exercise", "resource_url": "https://example.org/exercise",
                                       "initial_text": "Decision exercise: https://example.org/exercise. Reply YES to continue."})
        prepared = funnels.prepare(value, data, current, True)
        source = {"kind": value["entry"], "entry_event_id": f"synthetic-entry-{number}", "post_id": "fixture-post"}
        source.update({"ordinary_inbound": True} if value.get("entry_match") == "any_inbound" else {"keyword": data["parameters"]["keyword"]})
        run = {"id": f"synthetic-run-{number}", "mode": "live" if number < 2 else "preview", "platform": "Instagram",
               "compatible": True, "account_id": account, "bot_id": current["bot_id"], "recipient_id": f"synthetic-recipient-{number}",
               "author_account": number == 0, "input_sha256": funnels.fingerprint(data), "source": source,
               "inputs": save_fixture(root, f"{number}/inputs.json", data), "prepared_plan": save_fixture(root, f"{number}/plan.json", prepared), "checks": {}}
        bindings = {"recipe_id": value["id"], "recipe_digest": digest, "run_id": run["id"], "account_id": account,
                    "bot_id": run["bot_id"], "recipient_id": run["recipient_id"], "input_sha256": run["input_sha256"],
                    "mode": run["mode"], "platform": run["platform"], "source": source}
        outcomes = funnels.business_checks(value, data["parameters"])
        for check in set(value["runtime_checks"]) | set(outcomes):
            outcome = outcomes.get(check)
            record = {"schema_version": 1, "fixture": False, "passed": True, "origin": outcome["origin"] if outcome else "human-review", "observed_at": now(),
                      "observation": "Synthetic validator exercise, never actual runtime proof: " + check, "bindings": {**bindings, "check": check}}
            if outcome:
                record["native_refs"] = [f"synthetic-{number}-{check}-{i}" for i in range(outcome["min_native_refs"])]
                if "parameter" in outcome:
                    record["destination"] = data["parameters"][outcome["parameter"]]
                if check == "two_actual_answers":
                    record["answers"] = [{"event_id": record["native_refs"][i], "recipient_id": run["recipient_id"],
                                          "question": data["parameters"][key], "answer": "Synthetic fixture answer " + str(i)}
                                         for i, key in enumerate(("question_one", "question_two"))]
            run["checks"][check] = save_fixture(root, f"{number}/{check}.json", record)
        runs.append(run)
    acceptance = {"status": "accepted", "independent_reviewer": "synthetic-reviewer", "runs_sha256": funnels.fingerprint(runs),
                  "fresh_install_and_private_recovery": True,
                  "variants": sorted(set(next_steps[:2])) if next_steps else ["handoff"] if value["family"] == "qualification" else ["default"],
                  "material_delivery": material,
                  "target_users": [{"id": f"synthetic-user-{i}", "unassisted": True, "business_clarifications": 1} for i in range(3)]}
    acceptance["receipt"] = save_fixture(root, "acceptance.json", {"schema_version": 1, "fixture": False, "passed": True,
        "origin": "human-review", "observed_at": now(), "observation": "Synthetic acceptance-shaped fixture; not E2E.",
        "bindings": {"recipe_id": value["id"], "recipe_digest": digest, "runs_sha256": acceptance["runs_sha256"],
                     "variants": acceptance["variants"], "material_delivery": material, "check": "independent_acceptance"}})
    manifest = {"schema_version": 1, "fixture": False, "recipe_id": value["id"], "recipe_digest": digest,
                "environment": ENV, "runs": runs, "acceptance": acceptance}
    save_fixture(root, value["id"] + ".json", manifest)
    return manifest


class ContractPinTests(unittest.TestCase):
    def bundle(self):
        return {"schema_version": 1, "source": "chatfuel-public-api.get_type", "observed_at": now(),
                "definition_set": "coach-funnel-native-v1", "records": [
                    {"tool": "get_type", "arguments": copy.deepcopy(arguments),
                     "text": "# Synthetic offline fixture, not native schema or evidence.\n" +
                     "\n\n".join("type " + name + " {\n  fixtureOnly: String\n}" for name in arguments.get("names", [arguments.get("name")])) +
                     ('\nshown 1-1 of 1 matching "fuelyAutomation" (1 total)' if "filter" in arguments else "")}
                    for arguments in funnels.CONTRACT_REQUESTS]}

    def test_contract_pin_is_stable_across_read_times_and_record_order(self):
        bundle = self.bundle()
        pin = funnels.contract_pin(bundle, complete=True)
        later = copy.deepcopy(bundle)
        later["observed_at"] = (datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat()
        later["records"].reverse()
        self.assertEqual(funnels.contract_pin(later, True)["connector_contract"], pin["connector_contract"])
        self.assertIn("not native provenance", pin["limit"])
        later["records"][0]["text"] += "\nChanged exact source text."
        self.assertNotEqual(funnels.contract_pin(later, True)["connector_contract"], pin["connector_contract"])

    def test_contract_pin_rejects_incomplete_stale_and_wrong_source_bundles(self):
        with self.assertRaisesRegex(ValueError, "Attest complete"):
            funnels.contract_pin(self.bundle())
        for mutation in ("missing", "duplicate", "source", "definition-set", "stale", "future", "empty", "arguments", "tool"):
            bundle = self.bundle()
            if mutation == "missing":
                bundle["records"].pop()
            elif mutation == "duplicate":
                bundle["records"][0] = copy.deepcopy(bundle["records"][1])
            elif mutation == "source":
                bundle["source"] = "invented-provider-version"
            elif mutation == "definition-set":
                bundle["definition_set"] = "partial"
            elif mutation in {"stale", "future"}:
                bundle["observed_at"] = (datetime.now(timezone.utc) + timedelta(seconds=-901 if mutation == "stale" else 61)).isoformat()
            elif mutation == "empty":
                bundle["records"][0]["text"] = " "
            elif mutation == "arguments":
                bundle["records"][0]["arguments"]["limit"] = 1
            else:
                bundle["records"][0]["tool"] = "execute_query"
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.contract_pin(bundle, True)

    def test_contract_pin_cli_uses_the_same_exact_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic-schema.json"
            bundle = self.bundle()
            path.write_text(json.dumps(bundle), encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "plugin/scripts/funnels.py"), "contract-pin", "--bundle", str(path), "--complete"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["connector_contract"], funnels.contract_pin(bundle, True)["connector_contract"])

    def test_contract_pin_rejects_wrong_definitions_errors_and_partial_pages(self):
        for mutation in ("tool-error", "wrong-name", "comment-name", "missing-brace", "partial-page", "later-page", "no-footer", "truncated", "duplicate-definition"):
            bundle = self.bundle()
            record = bundle["records"][0]
            if mutation == "tool-error":
                for item in bundle["records"]:
                    item["text"] = "tool error"
            elif mutation == "wrong-name":
                record["text"] = record["text"].replace("type Mutation", "type WrongMutation")
            elif mutation == "comment-name":
                record["text"] = record["text"].replace("type Mutation", "# type Mutation")
            elif mutation == "missing-brace":
                record["text"] = record["text"].replace("}", "")
            elif mutation == "partial-page":
                record["text"] = record["text"].replace("shown 1-1 of 1", "shown 1-1 of 2")
            elif mutation == "later-page":
                record["text"] = record["text"].replace("shown 1-1 of 1", "shown 2-2 of 2")
            elif mutation == "no-footer":
                record["text"] = record["text"].split("\nshown")[0]
            elif mutation == "truncated":
                record["text"] += "\nOutput truncated"
            else:
                record["text"] += "\ntype Mutation {\n duplicate: String\n}"
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.contract_pin(bundle, True)


class WaitlistRestartTests(unittest.TestCase):
    def stopped(self, dm_enabled=False, active=False, unrelated=False):
        value = funnels.recipe("inro-6081")
        data = business(value)
        baseline = native_shaped_state(value, dm_enabled, active)
        if unrelated:
            baseline["rules"].append(rule("foreign-off", "All", False, False))
        baseline["synthetic_contact_memberships"] = {"fixture-a": "joined", "fixture-b": "withdrawn"}
        original = funnels.prepare(value, data, baseline, True)
        running = readback(original, baseline, "enabled")
        running["known_attribute_names"].append(data["parameters"]["membership_attribute"])
        stop = funnels.stop_plan(original, running)
        stopped = apply_commands(running, stop["commands"])
        verification = funnels.verify_stop(stop, stopped)
        return data, original, stop, verification, stopped

    def test_start_stop_restart_stop_off_on_and_active_dormant(self):
        for dm_enabled in (False, True):
            for active in (False, True):
                with self.subTest(dm_enabled=dm_enabled, active=active):
                    data, original, stop, verification, current = self.stopped(dm_enabled, active)
                    before = copy.deepcopy(current)
                    restarted = funnels.restart_plan(original, stop, verification, data, current, True)
                    self.assertEqual(current, before)
                    self.assertEqual(restarted["campaign_id"], original["campaign_id"])
                    self.assertEqual(restarted["shared_additions"]["capture_names"], original["shared_additions"]["capture_names"])
                    self.assertEqual(restarted, funnels.restart_plan(original, stop, verification, data, current, True))
                    configured = readback(restarted, current)
                    self.assertTrue(funnels.verify(restarted, configured)["configuration_verified"])
                    activated = apply_commands(configured, funnels.activation_plan(restarted, configured)["commands"])
                    enabled = apply_commands(activated, funnels.enable_plan(restarted, activated)["commands"])
                    self.assertTrue(funnels.verify(restarted, enabled, "enabled")["enable_verified"])
                    for identifier, settings in restarted["expected"].items():
                        self.assertIn("restart alone never reenrolls", settings["incomingMessages"]["messagePrompt"])
                        self.assertIn("Never reuse old consent or answers", settings["collectContactInfo"]["captures"][-1]["description"])
                    again_stop = funnels.stop_plan(restarted, enabled)
                    stopped_again = apply_commands(enabled, again_stop["commands"])
                    again_verified = funnels.verify_stop(again_stop, stopped_again)
                    self.assertTrue(again_verified["settings_stopped"])
                    self.assertFalse(again_verified["live_stop_verified"])
                    self.assertEqual(stopped_again["rules"], current["rules"])
                    self.assertEqual(stopped_again["synthetic_contact_memberships"], {"fixture-a": "joined", "fixture-b": "withdrawn"})
                    self.assertEqual(funnels.stop_plan(restarted, stopped_again)["commands"], [])
                    self.assertEqual(funnels.restart_plan(original, again_stop, again_verified, data, stopped_again, True)["campaign_id"], original["campaign_id"])
                    with self.assertRaisesRegex(ValueError, "Affected settings changed"):
                        funnels.restart_plan(original, stop, verification, data, configured, True)

    def test_restart_preserves_concurrent_unrelated_rules_and_settings(self):
        data, original, stop, verification, current = self.stopped()
        current["rules"].append(rule("foreign-off", "All", False, False))
        current["rules"][2]["settings"]["whenAIReplies"] = {"option": "Always", "inheritsFrom": None}
        plan = funnels.restart_plan(original, stop, verification, data, current, True)
        staged = readback(plan, current)
        self.assertEqual(staged["rules"][-1], current["rules"][-1])
        self.assertEqual(staged["rules"][2]["settings"]["whenAIReplies"], current["rules"][2]["settings"]["whenAIReplies"])
        self.assertEqual(plan["original_enabled"]["fixture-dm"], False)

    def test_late_return_refresh_preserves_ownership_and_unrelated_off_changes(self):
        for dm_enabled in (False, True):
            for mutation in ("addition", "edit"):
                with self.subTest(dm_enabled=dm_enabled, mutation=mutation):
                    data, original, stop, verification, current = self.stopped(dm_enabled, unrelated=mutation == "edit")
                    saved_stop = copy.deepcopy(stop)
                    if mutation == "addition":
                        current["rules"].append(rule("foreign-off", "All", False, False))
                    else:
                        current["rules"][-1]["settings"]["incomingMessages"]["messagePrompt"] = "Updated unrelated support."
                    current["rules"][2]["settings"]["whenAIReplies"]["inheritsFrom"] = None
                    later = datetime.now(timezone.utc) + timedelta(minutes=20)
                    current["observed_at"] = later.isoformat()
                    with patch.object(funnels, "datetime", wraps=datetime) as clock:
                        clock.now.return_value = later
                        with self.assertRaisesRegex(ValueError, "Stale stop verification"):
                            funnels.restart_plan(original, stop, verification, data, current, True)
                        with self.assertRaisesRegex(ValueError, "not stopped"):
                            funnels.verify_stop(stop, current)
                        refreshed = funnels.verify_stop(stop, current, original)
                        self.assertEqual(refreshed, funnels.verify_stop(stop, current, original))
                        self.assertEqual(refreshed["verification_scope"], "unchanged-affected-settings")
                        self.assertNotEqual(refreshed["rules_sha256"], refreshed["stop_rules_sha256"])
                        self.assertFalse(refreshed["live_stop_verified"])
                        self.assertEqual(stop, saved_stop)
                        restarted = funnels.restart_plan(original, stop, refreshed, data, current, True)
                        staged = readback(restarted, current, "activation")
                        staged["observed_at"] = later.isoformat()
                        self.assertEqual(staged["rules"][-1], current["rules"][-1])
                        self.assertEqual(staged["synthetic_contact_memberships"], current["synthetic_contact_memberships"])
                        next_stop = funnels.stop_plan(restarted, staged)
                        stopped_again = apply_commands(staged, next_stop["commands"])
                        stopped_again["observed_at"] = later.isoformat()
                        self.assertTrue(funnels.verify_stop(next_stop, stopped_again)["settings_stopped"])
                        self.assertEqual(stopped_again["rules"], current["rules"])

    def test_refresh_rejects_stale_capture_ownership(self):
        for mutation in ("foreign-dormant", "owned-capture", "changed-proof", "zero-command-stop"):
            data, original, stop, verification, current = self.stopped()
            saved_original = copy.deepcopy(original)
            name = data["parameters"]["membership_attribute"]
            if mutation == "foreign-dormant":
                foreign = rule("foreign-off", "All", False, False)
                foreign["settings"]["collectContactInfo"].update({"howToCollect": "DoNotCollectInfo", "captures": [{"name": name, "description": "Foreign ownership."}]})
                current["rules"].append(foreign)
            elif mutation == "owned-capture":
                current["rules"][3]["settings"]["collectContactInfo"] = {**copy.deepcopy(original["expected"]["fixture-owned"]["collectContactInfo"]), "inheritsFrom": None}
            elif mutation == "changed-proof":
                stop["membership_ownership"]["captures"]["fixture-owned"][0]["description"] += " Changed purpose."
                stop.pop("plan_sha256")
                funnels.seal(stop)
            else:
                stop = funnels.stop_plan(original, current)
                self.assertEqual(stop["commands"], [])
                self.assertIsNone(stop["membership_ownership"])
            self.assertEqual(original, saved_original)
            reason = "Stop lacks exact original campaign capture ownership proof" if mutation == "changed-proof" else ".+"
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, reason):
                funnels.verify_stop(stop, current, original)

    def test_refresh_rejects_affected_changes_and_invalid_current_state(self):
        for mutation in ("prompt", "capture", "switch", "scope", "namespace", "unknown-action", "stale-state"):
            data, original, stop, verification, current = self.stopped()
            if mutation in {"prompt", "capture"}:
                key = "incomingMessages" if mutation == "prompt" else "collectContactInfo"
                config = current["rules"][2]["settings"][key]
                config["inheritsFrom"] = None
                if mutation == "prompt":
                    config["messagePrompt"] = "Changed affected support."
                else:
                    config["captures"].append({"name": "unrelated_new_capture", "description": "Still an affected setting."})
            elif mutation == "switch":
                current["rules"][3]["enabled"] = True
            elif mutation == "scope":
                current["rules"][3]["scope"] = "InstagramDirectMessages"
            elif mutation == "namespace":
                current["attribute_namespace_complete"] = False
            elif mutation == "unknown-action":
                current["actions"] = [{"status": "unknown"}]
            else:
                current["observed_at"] = (datetime.now(timezone.utc) - timedelta(minutes=20)).isoformat()
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.verify_stop(stop, current, original)

    def test_refreshed_receipt_rejects_tampering_and_wrong_bindings(self):
        data, original, stop, verification, current = self.stopped()
        current["rules"].append(rule("foreign-off", "All", False, False))
        refreshed = funnels.verify_stop(stop, current, original)
        for field in ("observed_at", "plan_sha256", "source_plan_sha256", "stop_rules_sha256", "original_plan_sha256", "verification_scope"):
            changed = copy.deepcopy(refreshed)
            changed[field] = "forged"
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "changed stop receipt"):
                funnels.restart_plan(original, stop, changed, data, current, True)
            if field != "observed_at":
                changed.pop("verification_sha256")
                changed["verification_sha256"] = funnels.fingerprint(changed)
                with self.subTest(rehashed_field=field), self.assertRaisesRegex(ValueError, "does not verify"):
                    funnels.restart_plan(original, stop, changed, data, current, True)

    def test_restart_keeps_same_name_when_empty_native_definition_disappears(self):
        data, original, stop, verification, current = self.stopped()
        current["synthetic_contact_memberships"] = {}
        name = data["parameters"]["membership_attribute"]
        current["known_attribute_names"].remove(name)
        plan = funnels.restart_plan(original, stop, verification, data, current, True)
        self.assertEqual(plan["shared_additions"]["capture_names"], [name])
        self.assertEqual(plan["campaign_id"], original["campaign_id"])
        staged = readback(plan, current)
        staged["known_attribute_names"].append(name)
        self.assertTrue(funnels.verify(plan, staged)["configuration_verified"])
        self.assertEqual(staged["synthetic_contact_memberships"], {})

    def test_restart_rejects_changed_business_identity(self):
        data, original, stop, verification, current = self.stopped()
        for field in ("campaign_id", "membership_attribute", "launch_name", "launch_purpose", "consent_text"):
            changed = copy.deepcopy(data)
            if field == "campaign_id":
                changed[field] = "different-campaign"
            else:
                changed["parameters"][field] += " changed"
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "cannot change"):
                funnels.restart_plan(original, stop, verification, changed, current, True)

    def test_restart_rejects_missing_stale_foreign_or_changed_proof(self):
        for mutation in ("receipt", "stale", "stop-source", "no-capture-proof", "foreign-capture", "incomplete-namespace", "unknown-action", "affected-setting", "enabled", "old-origin"):
            data, original, stop, verification, current = self.stopped()
            if mutation == "receipt":
                verification.pop("verification_sha256")
            elif mutation == "stale":
                verification["observed_at"] = (datetime.now(timezone.utc) - timedelta(seconds=901)).isoformat()
                verification.pop("verification_sha256")
                verification["verification_sha256"] = funnels.fingerprint(verification)
            elif mutation in {"stop-source", "no-capture-proof"}:
                stop["campaign_root_sha256" if mutation == "stop-source" else "membership_ownership"] = None
                stop.pop("plan_sha256")
                funnels.seal(stop)
                verification = funnels.verify_stop(stop, current)
            elif mutation == "foreign-capture":
                foreign = rule("foreign-launch", "All", False, False)
                foreign["settings"]["collectContactInfo"] = {"howToCollect": "DoNotCollectInfo", "captures": [{"name": data["parameters"]["membership_attribute"], "description": "Foreign meaning."}], "inheritsFrom": None}
                current["rules"].append(foreign)
            elif mutation == "incomplete-namespace":
                current["attribute_namespace_complete"] = False
            elif mutation == "unknown-action":
                current["actions"] = [{"kind": "setting", "status": "unknown"}]
            elif mutation == "affected-setting":
                current["rules"][2]["settings"]["incomingMessages"] = {"howToReply": "UsingAI", "messagePrompt": "Changed after stop.", "inheritsFrom": None}
            elif mutation == "enabled":
                current["rules"][3]["enabled"] = True
            else:
                original["recipe_digest"] = "old-code"
                original.pop("plan_sha256")
                funnels.seal(original)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.restart_plan(original, stop, verification, data, current, True)

    def test_restart_never_bypasses_customer_acceptance_or_normal_collision_gate(self):
        data, original, stop, verification, current = self.stopped()
        with self.assertRaisesRegex(ValueError, "already exists"):
            funnels.prepare(funnels.recipe("inro-6081"), data, current, True)
        with self.assertRaisesRegex(ValueError, "cannot be prepared"):
            funnels.restart_plan(original, stop, verification, data, current)

    def test_restart_cli_uses_saved_plans_and_verification_without_writes(self):
        data, original, stop, verification, current = self.stopped()
        current["rules"].append(rule("foreign-off", "All", False, False))
        verification = funnels.verify_stop(stop, current, original)
        with tempfile.TemporaryDirectory() as directory:
            values = {"inputs": data, "original-plan": original, "stop-plan": stop,
                      "stop-verification": verification, "state": current}
            command = [sys.executable, str(ROOT / "plugin/scripts/funnels.py"), "restart-plan", "--developer-qa"]
            for flag, value in values.items():
                path = Path(directory) / (flag + ".json")
                path.write_text(json.dumps(value), encoding="utf-8")
                command.extend(["--" + flag, str(path)])
            refresh_command = [sys.executable, str(ROOT / "plugin/scripts/funnels.py"), "verify-stop",
                               "--original-plan", str(Path(directory) / "original-plan.json"),
                               "--plan", str(Path(directory) / "stop-plan.json"), "--state", str(Path(directory) / "state.json")]
            refreshed = subprocess.run(refresh_command, capture_output=True, text=True)
            self.assertEqual(refreshed.returncode, 0, refreshed.stderr)
            self.assertEqual(json.loads(refreshed.stdout), verification)
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), funnels.restart_plan(original, stop, verification, data, current, True))
            for flag, value in values.items():
                self.assertEqual(funnels.load(Path(directory) / (flag + ".json")), value)


class DesignTests(unittest.TestCase):
    def test_thirty_individual_sources_and_schema(self):
        result = funnels.validate()
        self.assertEqual(result["sources"], 30)
        self.assertEqual({row["id"] for row in funnels.load(funnels.REFERENCES / "research.json")["sources"]}, IDS)
        outcomes = [funnels.recipe(identifier)["outcome"] for identifier in IDS]
        self.assertEqual(len(set(outcomes)), 30)

    def test_customer_catalogue_empty_and_candidates_not_released(self):
        self.assertEqual(funnels.load(funnels.REFERENCES / "catalog.json")["recipes"], [])
        for identifier in IDS:
            with self.subTest(identifier=identifier):
                self.assertFalse(funnels.selection(funnels.recipe(identifier), [], env=ENV)["eligible"])

    def test_required_function_not_replaced_by_different_goal(self):
        for identifier, required in [("inro-6028", "follower-gate"), ("inro-6026", "required-email-paywall"),
                                     ("inro-6222", "ad-click-trigger"), ("inro-6025", "confirmed-booking"),
                                     ("inro-6054", "confirmed-registration"), ("inro-6086", "automatic-story-mention-acknowledgment")]:
            with self.subTest(identifier=identifier):
                self.assertFalse(funnels.selection(funnels.recipe(identifier), [required], True)["eligible"])
        self.assertFalse(funnels.selection(funnels.recipe("inro-6220"), ["unknown-mandatory-function"], True)["eligible"])
        self.assertTrue(funnels.selection(funnels.recipe("inro-6220"), ["instagram", "link-delivery"], True)["eligible"])

    def test_unavailable_and_unverified_designs_do_not_prepare(self):
        for identifier in ("inro-comment-moderation", "inro-6111", "inro-6086"):
            value = funnels.recipe(identifier)
            with self.subTest(identifier=identifier), self.assertRaises(ValueError):
                funnels.prepare(value, business(value), state(value), True)

    def test_story_mention_thanks_remains_unverified_not_reaction_only(self):
        value = funnels.recipe("inro-6086")
        self.assertEqual(value["status"], "unverified")
        self.assertEqual(value["goal"], "Automatically thank people who mention the coach in their story.")
        self.assertEqual(value["native_operations"], [])
        self.assertIn("actual mention trigger and automatic reply", value["blockers"][0])
        self.assertIn("does not prove that automatic text acknowledgment is impossible", value["messages"]["continuation"])
        self.assertFalse(funnels.selection(value, [], developer_qa=True)["eligible"])
        fixture = next(row for row in funnels.load(ROOT / "tests/funnel-prompts.json")["recipes"] if row["recipe_id"] == value["id"])
        self.assertEqual(fixture["expected"]["required_outcome"], value["goal"])
        self.assertFalse(fixture["expected"]["developer_preparable"])

    def test_changed_conditions_need_explicit_acceptance(self):
        value = funnels.recipe("inro-6028")
        data = business(value)
        data["accepted_changes"] = []
        with self.assertRaisesRegex(ValueError, "changed conditions"):
            funnels.prepare(value, data, state(value), True)

    def test_prompt_fixtures_cover_each_recipe_and_negative_routes(self):
        suite = funnels.load(ROOT / "tests/funnel-prompts.json")
        self.assertEqual({case["recipe_id"] for case in suite["recipes"]}, IDS)
        for case in suite["recipes"]:
            self.assertEqual(len(set(case["prompts"])), 3)
            value = funnels.recipe(case["recipe_id"])
            self.assertFalse(funnels.selection(value, case["requirements"], False, env=ENV)["eligible"])
            self.assertEqual(funnels.selection(value, case["requirements"], True)["eligible"], case["expected"]["developer_selectable"])
        self.assertGreaterEqual(len(suite["unsupported"]), 5)
        self.assertEqual({case["route"] for case in suite["routing_controls"]}, {"video", "waiting", "video-resume"})


class LifecycleTests(unittest.TestCase):
    def test_capture_never_promises_an_external_delivery_service(self):
        for identifier in ("inro-6018", "inro-6024", "inro-6026", "inro-6022", "inro-6027", "inro-6054"):
            value = funnels.recipe(identifier)
            plan = funnels.prepare(value, business(value), native_shaped_state(value), True)
            for settings in plan["expected"].values():
                prompt = settings["incomingMessages"]["messagePrompt"]
                self.assertIn("Never promise email delivery, a phone call", prompt)
                self.assertIn("Capturing a field does not send anything", prompt)
                capture = settings["collectContactInfo"]["captures"][-1]
                self.assertIn("for the team", capture["description"])
                self.assertIn("capture sends nothing", capture["description"])

    def test_substantive_text_facts_are_not_dropped_as_copy_overrides(self):
        for identifier, key in (("inro-4530", "bonus_text"), ("inro-6223", "thanks_text")):
            value = funnels.recipe(identifier)
            data = business(value)
            data["parameters"][key] = "Exact substantive business content, not a generic replacement."
            if key == "thanks_text":
                data["parameters"]["initial_text"] = data["parameters"][key]
            plan = funnels.prepare(value, data, native_shaped_state(value), True)
            for settings in plan["expected"].values():
                self.assertIn(f"{key}: {data['parameters'][key]}", settings["incomingMessages"]["messagePrompt"])

    def test_unknown_facts_escalate_in_both_paths_without_repeated_greeting(self):
        for recipe_id in ("inro-4393", "inro-6025"):
            value = funnels.recipe(recipe_id)
            plan = funnels.prepare(value, business(value), native_shaped_state(value), True)
            for settings in plan["expected"].values():
                prompt = settings["incomingMessages"]["messagePrompt"]
                self.assertIn("initiate native team handoff", prompt)
                self.assertIn("without repeating a greeting", prompt)
                self.assertIn("marked not provided or unknown is absent", prompt)
                condition = settings["switchToHuman"]["rules"][-1]["switchingConditions"]
                self.assertIn("switch to teammates when asked price, availability, refunds", condition)
                self.assertIn("Do not merely say no price was provided", condition)

    def test_qr_uses_existing_encoder_and_independent_decode(self):
        import cv2
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "profile.png"
            url = "https://www.instagram.com/fixture_coach/"
            result = funnels.create_qr(url, "fixture_coach", output)
            decoded, points, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(str(output)))
            self.assertEqual(decoded, url)
            self.assertIsNotNone(points)
            self.assertEqual(result["sha256"], hashlib.sha256(output.read_bytes()).hexdigest())
            self.assertFalse(result["runtime_accepted"])
            with self.assertRaisesRegex(ValueError, "do not overwrite"):
                funnels.create_qr(url, "fixture_coach", output)

    def test_qr_rejects_nonprofile_or_unverified_account_destinations(self):
        for url in ("http://www.instagram.com/fixture_coach/", "https://example.org/fixture_coach/",
                    "https://instagram.com.evil.example/fixture_coach/", "https://www.instagram.com/direct/",
                    "https://www.instagram.com/p/123/", "https://www.instagram.com/other_account/",
                    "https://www.instagram.com/fixture_coach/?next=other", "https://www.instagram.com/fixture_coach/#other",
                    "https://user@www.instagram.com/fixture_coach/", "https://www.instagram.com:443/fixture_coach/"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                funnels.profile_destination(url, "fixture_coach")
        value = funnels.recipe("inro-6019")
        current = native_shaped_state(value)
        current.pop("instagram_username")
        with self.assertRaisesRegex(ValueError, "actual Instagram username"):
            funnels.prepare(value, business(value), current, True)

    def test_waitlist_capture_scope_values_and_withdrawal_order(self):
        value = funnels.recipe("inro-6081")
        data = business(value)
        plan = funnels.prepare(value, data, native_shaped_state(value), True)
        for identifier in ("fixture-dm", "fixture-owned"):
            settings = plan["expected"][identifier]
            capture = settings["collectContactInfo"]["captures"][-1]
            self.assertEqual(capture["name"], data["parameters"]["membership_attribute"])
            for text in (f"Campaign {data['campaign_id']} only", "Fresh source and explicit new YES: joined", "STOP: withdrawn before handoff", "preserve state, including unset", "Never reuse old consent or answers"):
                self.assertIn(text, capture["description"])
            for key in ("launch_name", "launch_purpose", "consent_text"):
                self.assertIn(data["parameters"][key], settings["incomingMessages"]["messagePrompt"])
            condition = settings["switchToHuman"]["rules"][-1]["switchingConditions"]
            self.assertIn("= withdrawn before any handoff", condition)
            self.assertIn("Do not hand off for YES or STOP alone", condition)
            self.assertNotIn("on current-run refusal", condition)

    def test_waitlist_capture_description_stays_short_with_long_business_inputs(self):
        value = funnels.recipe("inro-6081")
        descriptions = []
        for long_inputs in (False, True):
            data = business(value)
            data["campaign_id"] = "c" * 48
            if long_inputs:
                data["parameters"]["launch_name"] = "Interview preparation " * 3
                data["parameters"]["launch_purpose"] = "Practice concrete interview answers with the coach. " * 3
                data["parameters"]["initial_text"] = value["messages"]["initial"].format_map(data["parameters"]) + " " + data["parameters"]["launch_purpose"]
            current = native_shaped_state(value)
            current["ownership"]["campaign_id"] = data["campaign_id"]
            plan = funnels.prepare(value, data, current, True)
            for identifier in ("fixture-dm", "fixture-owned"):
                settings = plan["expected"][identifier]
                description = settings["collectContactInfo"]["captures"][-1]["description"]
                self.assertLessEqual(len(description.encode("utf-8")), 240, "Internal size budget, not an asserted provider limit")
                descriptions.append(description)
                for key in ("launch_name", "launch_purpose", "consent_text"):
                    self.assertIn(data["parameters"][key], settings["incomingMessages"]["messagePrompt"])
            emitted = []
            for operation in plan["commands"] + plan["activation"]:
                update = operation["variables"].get("update", {}).get("collectContactInfo")
                if update:
                    emitted.extend(entry["description"] for entry in update["update"]["captures"]
                                   if entry["name"] == data["parameters"]["membership_attribute"])
            self.assertEqual(emitted, [descriptions[-1], descriptions[-1]])
        self.assertEqual(len(set(descriptions)), 1)

    def test_waitlist_requires_real_attribute_readback_and_unique_capture(self):
        value = funnels.recipe("inro-6081")
        data = business(value)
        for check, state_value in (("launch_membership_readback", "joined"), ("launch_withdrawal_confirmed", "withdrawn")):
            record = {"origin": "native-readback", "native_refs": ["synthetic-unit-test-not-live"],
                      "attribute_name": data["parameters"]["membership_attribute"], "attribute_value": state_value,
                      "launch_name": data["parameters"]["launch_name"]}
            funnels.verify_business_receipt(record, check, value["business_outcomes"][check], data["parameters"], "synthetic-recipient")
            record.pop("attribute_value")
            record["observation"] = "Bot prose claims membership."
            with self.assertRaisesRegex(ValueError, "not bot prose"):
                funnels.verify_business_receipt(record, check, value["business_outcomes"][check], data["parameters"], "synthetic-recipient")
        current = native_shaped_state(value)
        current["rules"][2]["settings"]["collectContactInfo"] = {"howToCollect": "CollectInfo", "inheritsFrom": None,
            "captures": [{"name": data["parameters"]["membership_attribute"], "description": "Existing launch; do not adopt."}]}
        with self.assertRaisesRegex(ValueError, "already exists"):
            funnels.prepare(value, data, current, True)

    def test_waitlist_rejects_global_native_and_known_attribute_collisions(self):
        value = funnels.recipe("inro-6081")
        data = business(value)
        name = data["parameters"]["membership_attribute"]
        for enabled in (False, True):
            for active in (False, True):
                for scope in ("InstagramPostComments", "All"):
                    with self.subTest(enabled=enabled, active=active, scope=scope):
                        current = native_shaped_state(value)
                        foreign = rule("foreign-launch", scope, False, enabled)
                        foreign["settings"]["collectContactInfo"] = {
                            "howToCollect": "CollectInfo" if active else "DoNotCollectInfo", "inheritsFrom": None,
                            "captures": [{"name": name, "description": "Another launch membership."}]}
                        current["rules"].append(foreign)
                        before = copy.deepcopy(current)
                        with self.assertRaisesRegex(ValueError, "already exists in native rule foreign-launch"):
                            funnels.prepare(value, data, current, True)
                        self.assertEqual(current, before)
        current = native_shaped_state(value)
        current["known_attribute_names"].append(name)
        with self.assertRaisesRegex(ValueError, "already exists in known account attributes"):
            funnels.prepare(value, data, current, True)
        current.pop("known_attribute_names")
        with self.assertRaisesRegex(ValueError, "Read account-wide"):
            funnels.prepare(value, data, current, True)
        current = state(value, owned=False)
        current["known_attribute_names"].append(name)
        with self.assertRaisesRegex(ValueError, "already exists"):
            funnels.prepare(value, data, current, True)
        for attestation in (None, False):
            current = native_shaped_state(value)
            current["known_attribute_names"] = []
            current["attribute_namespace_complete"] = attestation
            with self.subTest(attestation=attestation), self.assertRaisesRegex(ValueError, "namespace attestation"):
                funnels.prepare(value, data, current, True)

    def test_waitlist_rechecks_namespace_before_activation_and_enable(self):
        value = funnels.recipe("inro-6081")
        current = native_shaped_state(value)
        plan = funnels.prepare(value, business(value), current, True)
        configured = readback(plan, current)
        self.assertTrue(funnels.enable_plan(plan, configured)["commands"])
        current["known_attribute_names"].append(business(value)["parameters"]["membership_attribute"])
        for operation in (funnels.activation_plan, funnels.enable_plan):
            with self.subTest(operation=operation.__name__), self.assertRaisesRegex(ValueError, "known account attributes"):
                operation(plan, current)
        configured["attribute_namespace_complete"] = False
        with self.assertRaisesRegex(ValueError, "namespace attestation"):
            funnels.enable_plan(plan, configured)

    def test_waitlist_configuration_can_register_its_own_new_global_attribute(self):
        value = funnels.recipe("inro-6081")
        data = business(value)
        name = data["parameters"]["membership_attribute"]
        for dm_enabled in (False, True):
            for active in (False, True):
                with self.subTest(dm_enabled=dm_enabled, active=active):
                    current = native_shaped_state(value, dm_enabled, active)
                    plan = funnels.prepare(value, data, current, True)
                    original_namespace = plan["ownership_before_write"]["attribute_namespace"]
                    self.assertTrue(original_namespace["complete"])
                    self.assertNotIn(name, original_namespace["names"])
                    configured = readback(plan, current)
                    configured["known_attribute_names"].append(name)
                    self.assertEqual(funnels.activation_plan(plan, configured)["commands"], plan["activation"])
                    activated = apply_commands(configured, plan["activation"])
                    self.assertEqual(funnels.enable_plan(plan, activated)["commands"], plan["enable"])
                    running = apply_commands(activated, plan["enable"])
                    self.assertTrue(funnels.verify(plan, running, "enabled")["enable_verified"])
                    stop = funnels.stop_plan(plan, running)
                    stopped = apply_commands(running, stop["commands"])
                    self.assertTrue(funnels.verify_stop(stop, stopped)["restoration_complete"])
                    self.assertEqual(stopped["rules"], current["rules"])
                    self.assertIn(name, stopped["known_attribute_names"])
                    self.assertEqual(funnels.stop_plan(plan, stopped)["commands"], [])
                    with self.assertRaisesRegex(ValueError, "known account attributes"):
                        funnels.prepare(value, data, stopped, True)

    def test_waitlist_registered_name_requires_exact_owned_capture_and_original_absence(self):
        value = funnels.recipe("inro-6081")
        data = business(value)
        name = data["parameters"]["membership_attribute"]
        current = native_shaped_state(value)
        plan = funnels.prepare(value, data, current, True)
        configured = readback(plan, current)
        configured["known_attribute_names"].append(name)
        for mutation in ("foreign-dormant", "owned-edited", "owned-duplicated", "missing-original-namespace", "original-name-present"):
            changed = copy.deepcopy(configured)
            changed_plan = copy.deepcopy(plan)
            if mutation == "foreign-dormant":
                foreign = rule("foreign-launch", "All", False, False)
                foreign["settings"]["collectContactInfo"] = {"howToCollect": "DoNotCollectInfo", "inheritsFrom": None,
                    "captures": [{"name": name, "description": "Foreign launch."}]}
                changed["rules"].append(foreign)
            elif mutation == "owned-edited":
                changed["rules"][-1]["settings"]["collectContactInfo"]["captures"][-1]["description"] = "Changed membership meaning."
            elif mutation == "owned-duplicated":
                captures = changed["rules"][-1]["settings"]["collectContactInfo"]["captures"]
                captures.append(copy.deepcopy(captures[-1]))
            elif mutation == "missing-original-namespace":
                changed_plan["ownership_before_write"].pop("attribute_namespace")
            else:
                changed_plan["ownership_before_write"]["attribute_namespace"]["names"].append(name)
            changed_plan.pop("plan_sha256")
            funnels.seal(changed_plan)
            for operation in (funnels.activation_plan, funnels.enable_plan):
                with self.subTest(mutation=mutation, operation=operation.__name__), self.assertRaisesRegex(ValueError, "already exists|original membership-name absence"):
                    operation(changed_plan, changed)

    def test_stopped_waitlist_new_campaign_preserves_old_namespace(self):
        value = funnels.recipe("inro-6081")
        data = business(value)
        current = native_shaped_state(value)
        plan = funnels.prepare(value, data, current, True)
        running = readback(plan, current, "enabled")
        old_name = data["parameters"]["membership_attribute"]
        running["known_attribute_names"].append(old_name)
        stopped = apply_commands(running, funnels.stop_plan(plan, running)["commands"])
        with self.assertRaisesRegex(ValueError, "known account attributes"):
            funnels.prepare(value, data, stopped, True)
        new_data = copy.deepcopy(data)
        new_data["campaign_id"] = "fixture-new-campaign"
        new_data["parameters"]["membership_attribute"] = "coach_fixture_new_launch"
        new_rule = rule("fixture-new-owned", "InstagramPostComments", False, False)
        stopped["rules"].append(new_rule)
        stopped["ownership"] = {"campaign_id": new_data["campaign_id"], "recipe_id": value["id"],
                                "account_id": stopped["account_id"], "rule_id": new_rule["id"],
                                "rule_sha256": funnels.fingerprint(new_rule)}
        before = copy.deepcopy(stopped)
        new_plan = funnels.prepare(value, new_data, stopped, True)
        self.assertEqual(stopped, before)
        self.assertIn(old_name, new_plan["ownership_before_write"]["attribute_namespace"]["names"])
        self.assertIn("fixture-owned", new_plan["preserved_rules"])
        self.assertEqual(new_plan["shared_additions"]["capture_names"], ["coach_fixture_new_launch"])

    def test_qa_export_preserves_exact_supplied_business_and_actual_off_state(self):
        value = funnels.recipe("inro-6025")
        data = business(value)
        data["parameters"]["question_one"] = "What decision do you face now?"
        original = copy.deepcopy(data)
        baseline = native_shaped_state(value)
        exported = export_qa(baseline, [{"id": value["id"], "fixture": True, "business": data}], "fixture-owned")
        self.assertEqual(exported["plan_count"], 1)
        row = exported["cases"][0]
        self.assertEqual(row["business"], original)
        self.assertFalse(row["snapshot"]["rules"][2]["enabled"])
        self.assertEqual(row["snapshot"]["rules"], baseline["rules"])
        self.assertEqual(row["plan"], funnels.prepare(value, original, baseline, True))
        self.assertFalse(exported["runtime_accepted"])

    def test_qa_export_does_not_invent_missing_inputs(self):
        value = funnels.recipe("inro-4530")
        data = business(value)
        data["parameters"].pop("bonus_text")
        result = export_qa(cases=[{"id": value["id"], "fixture": True, "business": data}])
        self.assertEqual(result["plan_count"], 0)
        self.assertEqual(result["blocked_count"], 1)
        self.assertNotIn("plan", result["cases"][0])
        self.assertEqual(result["cases"][0]["business"], data)

    def test_all_preparable_lifecycles_off_on_dormant_active_exact_stop(self):
        prepared = set()
        for identifier in sorted(IDS):
            value = funnels.recipe(identifier)
            if value["status"] in {"unavailable", "unverified"} or value["blockers"]:
                continue
            prepared.add(identifier)
            for dm_enabled in (False, True):
                for active in (False, True):
                    with self.subTest(recipe=identifier, dm_enabled=dm_enabled, active=active):
                        current = native_shaped_state(value, dm_enabled, active)
                        plan = funnels.prepare(value, business(value), current, True)
                        self.assertFalse(plan["runtime_accepted"])
                        self.assertTrue(all("execute_mutation" in item["executor"] for item in plan["commands"] + plan["activation"] + plan["enable"]))
                        self.assertTrue(all(item["operation"] != "fuelyAutomationSetEnabled" for item in plan["commands"] + plan["activation"]))
                        configured = readback(plan, current)
                        self.assertTrue(funnels.verify(plan, configured)["configuration_verified"])
                        self.assertTrue(configured["rules"][0]["enabled"])
                        self.assertEqual(configured["rules"][2]["enabled"], dm_enabled)
                        if "fixture-dm" in plan["expected"]:
                            self.assertEqual(bool(plan["activation"]), dm_enabled)
                            switches = plan["expected"]["fixture-dm"]["switchToHuman"]["rules"]
                            self.assertEqual(len(switches), 2 if active else 1)
                        activated = readback(plan, current, "activation")
                        enable = funnels.enable_plan(plan, activated)
                        enabled_ids = {item["variables"]["id"] for item in enable["commands"]}
                        self.assertFalse(enabled_ids & {"fixture-main", "fixture-comment-base"})
                        self.assertEqual("fixture-dm" in enabled_ids, not dm_enabled and "fixture-dm" in plan["expected"])
                        running = readback(plan, current, "enabled")
                        self.assertTrue(funnels.verify(plan, running, "enabled")["enable_verified"])
                        stop = funnels.stop_plan(plan, running)
                        self.assertTrue(stop["restoration_complete"])
                        stopped = apply_commands(running, stop["commands"])
                        self.assertTrue(funnels.verify_stop(stop, stopped)["settings_stopped"])
                        self.assertEqual(stopped["rules"], current["rules"])
                        self.assertEqual(funnels.stop_plan(plan, stopped)["commands"], [])
        self.assertEqual(prepared, {identifier for identifier in IDS if not funnels.recipe(identifier)["blockers"]
                                  and funnels.recipe(identifier)["status"] not in {"unavailable", "unverified"}})

    def test_dm_off_can_stage_dontreply_and_disable_dormant_followups(self):
        value = funnels.recipe("inro-6025")
        current = native_shaped_state(value)
        dm = current["rules"][2]
        dm["settings"]["incomingMessages"]["howToReply"] = "DontReply"
        dm["settings"]["incomingMessages"]["inheritsFrom"] = None
        dm["settings"]["followUps"]["howToSend"] = "Send"
        dm["settings"]["followUps"]["inheritsFrom"] = None
        plan = funnels.prepare(value, business(value), current, True)
        self.assertEqual(plan["shared_mode"], "off-staging")
        self.assertEqual(plan["expected"][dm["id"]]["followUps"]["howToSend"], "DontSend")
        running = readback(plan, current, "enabled")
        stop = funnels.stop_plan(plan, running)
        self.assertEqual(apply_commands(running, stop["commands"])["rules"], current["rules"])

    def test_main_off_never_becomes_implicit_enable(self):
        value = funnels.recipe("inro-6025")
        current = native_shaped_state(value)
        current["rules"][0]["enabled"] = False
        with self.assertRaisesRegex(ValueError, "separate global approval"):
            funnels.prepare(value, business(value), current, True)

    def test_qualification_requires_current_run_source_consent_and_two_new_answers(self):
        for identifier in ("inro-6025", "inro-6021", "inro-6222"):
            value = funnels.recipe(identifier)
            data = business(value)
            plan = funnels.prepare(value, data, native_shaped_state(value), True)
            for settings in plan["expected"].values():
                prompt = settings["incomingMessages"]["messagePrompt"]
                for requirement in ("Current-run source", "new explicit consent", "Never reuse previous-run consent or answers",
                                    "distinct new actual inbound answer", "exactly two qualification questions", "Never add a third",
                                    "ignore unrelated knowledge-base", data["parameters"]["question_one"], data["parameters"]["question_two"]):
                    self.assertIn(requirement, prompt)
                self.assertIn("never use old consent or answers", settings["switchToHuman"]["rules"][-1]["switchingConditions"].lower())

    def test_qualification_consent_matches_localized_opt_in_without_fixed_token(self):
        for identifier in ("inro-6025", "inro-6021", "inro-6222"):
            value = funnels.recipe(identifier)
            self.assertNotIn("consent_text", value["required_inputs"])
            self.assertNotIn("{question_one}", value["messages"]["initial"])
            self.assertNotIn("After YES", json.dumps(value["transitions"]))
            for language, initial in (("Russian", "Ответьте ДА, если хотите ответить на два вопроса."),
                                      ("Portuguese", "Responda SIM se quiser responder a duas perguntas.")):
                for next_step in ("handoff", "booking_link"):
                    with self.subTest(recipe=identifier, language=language, next_step=next_step):
                        data = business(value)
                        data["parameters"].update({"language": language, "initial_text": initial, "next_step": next_step})
                        if next_step == "booking_link":
                            data["parameters"]["booking_url"] = "https://example.org/booking"
                        plan = funnels.prepare(value, data, native_shaped_state(value), True)
                        self.assertEqual(plan["preview"]["initial"], initial)
                        self.assertIn("explicit affirmative consent matching the presented opt-in", plan["preview"]["continuation"])
                        self.assertNotIn("After YES", plan["preview"]["continuation"])
                        for settings in plan["expected"].values():
                            prompt = settings["incomingMessages"]["messagePrompt"]
                            for text in ("approved language; do not require a fixed English token", "exactly two qualification questions",
                                         "The entry word and consent are not answers", "Never reuse previous-run consent or answers",
                                         data["parameters"]["question_one"], data["parameters"]["question_two"]):
                                self.assertIn(text, prompt)
                            self.assertNotIn("After YES", prompt)

    def test_stop_preserves_concurrent_shared_text_and_active_lists(self):
        value = funnels.recipe("inro-6022")
        current = native_shaped_state(value, dm_enabled=True, active=False)
        plan = funnels.prepare(value, business(value), current, True)
        running = readback(plan, current, "enabled")
        dm = running["rules"][2]
        dm["settings"]["incomingMessages"]["messagePrompt"] += "\nNew ordinary support instruction."
        foreign_handoff = {"switchingConditions": "New foreign escalation.", "messagePrompt": "New team message."}
        foreign_capture = {"name": "new_support_email", "description": "New support capture."}
        dm["settings"]["switchToHuman"]["rules"].append(foreign_handoff)
        dm["settings"]["collectContactInfo"]["captures"].append(foreign_capture)
        stop = funnels.stop_plan(plan, running)
        stopped = apply_commands(running, stop["commands"])
        self.assertTrue(funnels.verify_stop(stop, stopped)["settings_stopped"])
        self.assertFalse(stop["restoration_complete"])
        settings = stopped["rules"][2]["settings"]
        self.assertEqual(settings["switchToHuman"]["rules"], [foreign_handoff])
        self.assertEqual(settings["collectContactInfo"]["captures"], [foreign_capture])
        self.assertIn("New ordinary support instruction.", settings["incomingMessages"]["messagePrompt"])
        self.assertNotIn("[coach-funnel:", settings["incomingMessages"]["messagePrompt"])
        self.assertIsNone(settings["incomingMessages"]["inheritsFrom"])
        self.assertEqual(funnels.stop_plan(plan, stopped)["commands"], [])

    def test_stop_refuses_ambiguous_modified_or_duplicate_campaign_additions(self):
        value = funnels.recipe("inro-6022")
        current = native_shaped_state(value, dm_enabled=True)
        plan = funnels.prepare(value, business(value), current, True)
        for mutation in ("prompt-edit", "prompt-duplicate", "handoff-edit", "handoff-duplicate", "capture-edit"):
            running = readback(plan, current, "enabled")
            settings = running["rules"][2]["settings"]
            if mutation == "prompt-edit":
                settings["incomingMessages"]["messagePrompt"] = settings["incomingMessages"]["messagePrompt"].replace("Initial value:", "Edited value:")
            elif mutation == "prompt-duplicate":
                settings["incomingMessages"]["messagePrompt"] += plan["shared_additions"]["prompt_block"]
            elif mutation == "handoff-edit":
                settings["switchToHuman"]["rules"][-1]["messagePrompt"] = "Changed campaign handoff."
            elif mutation == "handoff-duplicate":
                settings["switchToHuman"]["rules"].append(copy.deepcopy(settings["switchToHuman"]["rules"][-1]))
            else:
                settings["collectContactInfo"]["captures"][-1]["description"] = "Changed campaign capture."
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, "ambiguous"):
                funnels.stop_plan(plan, running)

    def test_stop_defers_shared_disable_but_removes_campaign_with_concurrent_work(self):
        value = funnels.recipe("inro-6025")
        current = native_shaped_state(value)
        plan = funnels.prepare(value, business(value), current, True)
        for mutation in ("prompt", "new-rule", "main"):
            running = readback(plan, current, "enabled")
            if mutation == "prompt":
                running["rules"][2]["settings"]["incomingMessages"]["messagePrompt"] += "\nConcurrent campaign."
            elif mutation == "new-rule":
                running["rules"].append(rule("concurrent-rule", "InstagramPostComments", False, True))
            else:
                running["rules"][0]["settings"]["incomingMessages"]["messagePrompt"] += "\nNew main instruction."
                running["rules"][1]["settings"]["incomingMessages"]["messagePrompt"] = running["rules"][0]["settings"]["incomingMessages"]["messagePrompt"]
            with self.subTest(mutation=mutation):
                stop = funnels.stop_plan(plan, running)
                stopped = apply_commands(running, stop["commands"])
                verified = funnels.verify_stop(stop, stopped)
                self.assertTrue(verified["settings_stopped"])
                self.assertFalse(verified["restoration_complete"])
                self.assertFalse(verified["live_stop_verified"])
                self.assertTrue(stopped["rules"][2]["enabled"])
                self.assertFalse(next(item for item in stopped["rules"] if item["id"] == "fixture-owned")["enabled"])
                self.assertIn({"rule_id": "fixture-dm", "setting": "enabled"},
                              [{key: item[key] for key in ("rule_id", "setting")} for item in stop["deferred_restorations"]])
                self.assertNotIn("[coach-funnel:", stopped["rules"][2]["settings"]["incomingMessages"]["messagePrompt"])
                self.assertEqual(stopped["rules"][2]["settings"]["switchToHuman"]["rules"], [])
                for item in running["rules"]:
                    if item["id"] not in plan["expected"]:
                        self.assertEqual(stop["expected_rules"][item["id"]], item)
                if mutation == "prompt":
                    self.assertIn("Concurrent campaign.", stopped["rules"][2]["settings"]["incomingMessages"]["messagePrompt"])
                self.assertEqual(funnels.stop_plan(plan, stopped)["commands"], [])

    def test_deferred_dm_stop_preserves_support_and_does_not_wake_followups(self):
        value = funnels.recipe("inro-6022")
        current = native_shaped_state(value)
        dm = current["rules"][2]
        dm["settings"]["incomingMessages"] = {"howToReply": "DontReply", "messagePrompt": "Original support.", "inheritsFrom": None}
        dm["settings"]["followUps"] = {"howToSend": "Send", "messagePrompt": "Dormant follow-up.", "inheritsFrom": None}
        plan = funnels.prepare(value, business(value), current, True)
        running = readback(plan, current, "enabled")
        settings = running["rules"][2]["settings"]
        settings["incomingMessages"]["messagePrompt"] += "\nConcurrent support."
        foreign_handoff = {"switchingConditions": "New support.", "messagePrompt": "New team response."}
        foreign_capture = {"name": "new_support_detail", "description": "New support detail."}
        settings["switchToHuman"]["rules"].append(foreign_handoff)
        settings["collectContactInfo"]["captures"].append(foreign_capture)
        stop = funnels.stop_plan(plan, running)
        stopped = apply_commands(running, stop["commands"])
        settings = stopped["rules"][2]["settings"]
        self.assertTrue(funnels.verify_stop(stop, stopped)["settings_stopped"])
        self.assertFalse(stop["restoration_complete"])
        self.assertTrue(stopped["rules"][2]["enabled"])
        self.assertFalse(stopped["rules"][-1]["enabled"])
        self.assertEqual(settings["incomingMessages"]["howToReply"], "UsingAI")
        self.assertEqual(settings["incomingMessages"]["messagePrompt"], "Original support.\nConcurrent support.")
        self.assertEqual(settings["followUps"]["howToSend"], "DontSend")
        self.assertEqual(settings["switchToHuman"]["rules"], [foreign_handoff])
        self.assertEqual(settings["collectContactInfo"]["captures"], [foreign_capture])
        self.assertEqual(funnels.stop_plan(plan, stopped)["commands"], [])

    def test_stop_accepts_native_empty_capture_validation_arrays(self):
        value = funnels.recipe("inro-6022")
        current = native_shaped_state(value)
        plan = funnels.prepare(value, business(value), current, True)
        running = readback(plan, current, "enabled")
        for item in running["rules"]:
            if item["id"] in plan["expected"]:
                for capture in item["settings"]["collectContactInfo"]["captures"]:
                    capture["validationErrors"] = []
        stop = funnels.stop_plan(plan, running)
        stopped = apply_commands(running, stop["commands"])
        self.assertTrue(funnels.verify_stop(stop, stopped)["settings_stopped"])
        self.assertTrue(stop["restoration_complete"])

    def test_stop_does_not_disable_shared_dm_after_concurrent_owned_custom_edit(self):
        value = funnels.recipe("inro-6025")
        current = native_shaped_state(value)
        plan = funnels.prepare(value, business(value), current, True)
        running = readback(plan, current, "enabled")
        running["rules"][-1]["settings"]["whenAIReplies"] = {"option": "OutsideOfWorkingHours", "inheritsFrom": None}
        stop = funnels.stop_plan(plan, running)
        stopped = apply_commands(running, stop["commands"])
        self.assertTrue(funnels.verify_stop(stop, stopped)["settings_stopped"])
        self.assertFalse(stop["restoration_complete"])
        self.assertTrue(stopped["rules"][2]["enabled"])
        self.assertFalse(stopped["rules"][-1]["enabled"])
        self.assertEqual(stopped["rules"][-1]["settings"]["whenAIReplies"], running["rules"][-1]["settings"]["whenAIReplies"])

    def test_stop_keeps_explicit_settings_when_inheritance_parent_changed(self):
        value = funnels.recipe("inro-6025")
        current = native_shaped_state(value, dm_enabled=True)
        plan = funnels.prepare(value, business(value), current, True)
        running = readback(plan, current, "enabled")
        running["rules"][0]["settings"]["switchToHuman"]["rules"].append({"switchingConditions": "New dormant foreign rule.", "messagePrompt": "New dormant reply."})
        running["rules"][1]["settings"]["switchToHuman"]["rules"] = copy.deepcopy(running["rules"][0]["settings"]["switchToHuman"]["rules"])
        stop = funnels.stop_plan(plan, running)
        stopped = apply_commands(running, stop["commands"])
        self.assertFalse(stop["restoration_complete"])
        self.assertEqual(stopped["rules"][0], running["rules"][0])
        for identifier in ("fixture-dm", "fixture-owned"):
            setting = stop["expected_rules"][identifier]["settings"]["switchToHuman"]
            self.assertIsNone(setting["inheritsFrom"])
            self.assertEqual(setting["howToSwitch"], "DontSwitch")

    def test_partial_configuration_and_stop_readback_are_not_live_proof(self):
        value = funnels.recipe("inro-6025")
        current = native_shaped_state(value)
        plan = funnels.prepare(value, business(value), current, True)
        partial = apply_commands(current, plan["commands"][:2])
        stop = funnels.stop_plan(plan, partial)
        stopped = apply_commands(partial, stop["commands"])
        self.assertEqual(stopped["rules"], current["rules"])
        self.assertFalse(funnels.verify_stop(stop, stopped)["live_stop_verified"])
        running = readback(plan, current, "enabled")
        stop = funnels.stop_plan(plan, running)
        with self.assertRaisesRegex(ValueError, "not stopped"):
            funnels.verify_stop(stop, running)
        stopped = apply_commands(running, stop["commands"])
        stopped["rules"][1]["enabled"] = False
        with self.assertRaisesRegex(ValueError, "not stopped"):
            funnels.verify_stop(stop, stopped)


class PreparationTests(unittest.TestCase):
    def test_reply_readiness_blocks_dm_off_on_and_inherited_restrictions(self):
        for identifier in ("inro-6019", "inro-6023", "inro-6025"):
            value = funnels.recipe(identifier)
            for enabled in (False, True):
                for inherited in (False, True):
                    for option in ("OutsideOfWorkingHours", None):
                        with self.subTest(recipe=identifier, enabled=enabled, inherited=inherited, option=option):
                            current = native_shaped_state(value, dm_enabled=enabled)
                            if inherited:
                                for item in current["rules"]:
                                    item["settings"]["whenAIReplies"]["option"] = option
                            else:
                                current["rules"][2]["settings"]["whenAIReplies"] = {"option": option, "inheritsFrom": None}
                            before = copy.deepcopy(current)
                            with self.assertRaisesRegex(ValueError, "Reply readiness for fixture-dm"):
                                funnels.prepare(value, business(value), current, True)
                            self.assertEqual(current, before)

    def test_reply_readiness_rechecked_at_activation_enable_and_readback(self):
        for identifier in ("inro-6019", "inro-6023", "inro-6025"):
            value = funnels.recipe(identifier)
            current = native_shaped_state(value)
            plan = funnels.prepare(value, business(value), current, True)
            configured = readback(plan, current)
            self.assertTrue(funnels.enable_plan(plan, configured)["commands"])
            self.assertTrue(all("whenAIReplies" not in item["variables"].get("update", {})
                                for item in plan["commands"] + plan["activation"]))
            configured["rules"][2]["settings"]["whenAIReplies"] = {"option": "OutsideOfWorkingHours", "inheritsFrom": None}
            for operation in (funnels.activation_plan, funnels.enable_plan):
                with self.subTest(recipe=identifier, operation=operation.__name__), self.assertRaisesRegex(ValueError, "Reply readiness"):
                    operation(plan, configured)
            with self.assertRaisesRegex(ValueError, "Reply readiness"):
                funnels.verify(plan, configured, "enabled")

    def test_actual_payloads_for_all_preparable_designs_match_schema_fixture(self):
        contract = funnels.load(ROOT / "tests/fixtures/funnel-contract.json")
        for identifier in IDS:
            value = funnels.recipe(identifier)
            if value["status"] in {"unavailable", "unverified"} or value["blockers"]:
                continue
            with self.subTest(identifier=identifier):
                current = state(value)
                plan = funnels.prepare(value, business(value), current, True)
                self.assertEqual(plan["stage"], "configuration-prepared")
                self.assertFalse(plan["runtime_accepted"])
                for operation in plan["commands"] + plan["activation"]:
                    self.assertEqual(operation["operation"], contract["operation"])
                    variables = operation["variables"]
                    self.assertEqual(set(variables), {"botID", "id", "update"})
                    self.assertEqual(len(variables["update"]), 1)
                    name, wrapped = next(iter(variables["update"].items()))
                    self.assertEqual(set(wrapped), {contract["wrapper"]})
                    config = wrapped["update"]
                    schema = contract["settings"][name]
                    self.assertEqual(set(config), set(schema["required"]))
                    for key, allowed in schema["enums"].items():
                        self.assertIn(config[key], allowed)
                    self.assertTrue(all(not isinstance(item, str) or item.strip() for item in config.values()))
                    if name == "switchToHuman":
                        self.assertTrue(all(set(item) == set(contract["handoff_rule_required"]) for item in config["rules"]))
                    if name == "collectContactInfo":
                        self.assertTrue(all(set(item) == set(contract["capture_required"]) for item in config["captures"]))
                self.assertTrue(funnels.verify(plan, readback(plan, current))["configuration_verified"])
                self.assertTrue(funnels.verify(plan, readback(plan, current, "activation"), "activation")["shared_activation_verified"])

    def test_first_stage_create_is_off_and_has_no_guessed_rule_id(self):
        value = funnels.recipe("inro-6025")
        plan = funnels.prepare(value, business(value), state(value, False), True)
        self.assertEqual(plan["stage"], "create-required")
        self.assertEqual(len(plan["commands"]), 1)
        self.assertEqual(plan["commands"][0]["operation"], "fuelyAutomationCreate")
        self.assertEqual(set(plan["commands"][0]["variables"]), {"botID", "scope", "name"})
        self.assertEqual(plan["enable"], [])

    def test_material_then_two_questions_and_handoff_without_booking(self):
        value = funnels.recipe("inro-6025")
        data = business(value)
        data["parameters"].update({"resource_title": "Decision exercise", "resource_url": "https://example.org/exercise.pdf",
                                   "initial_text": "Decision exercise: https://example.org/exercise.pdf. Reply YES to discuss it.",
                                   "question_one": "Which decision do you face?", "question_two": "What have you tried?"})
        plan = funnels.prepare(value, data, state(value), True)
        self.assertNotIn("booking_url", data["parameters"])
        prompt = plan["expected"]["fixture-owned"]["incomingMessages"]["messagePrompt"]
        self.assertIn("Which decision do you face?", prompt)
        self.assertIn("What have you tried?", prompt)
        self.assertIn("handoff only", prompt)
        self.assertEqual(plan["expected"]["fixture-owned"]["privateReply"]["exactTextReply"], data["parameters"]["initial_text"])
        self.assertIn("after completing", plan["expected"]["fixture-owned"]["switchToHuman"]["rules"][-1]["switchingConditions"])
        self.assertEqual(plan["expected"]["fixture-owned"]["followUps"]["howToSend"], "DontSend")

    def test_shared_writes_require_a_separate_live_activation_phase(self):
        for identifier in ("inro-6025", "inro-6021"):
            value = funnels.recipe(identifier)
            current = state(value)
            plan = funnels.prepare(value, business(value), current, True)
            self.assertTrue(plan["activation"])
            self.assertTrue(all(operation["variables"]["id"] != "fixture-dm" for operation in plan["commands"]))
            self.assertTrue(all(operation["phase"] == "shared-activation" and operation["requires_native_approval"] and operation["readback_after"] for operation in plan["activation"]))
            if plan["commands"]:
                with self.assertRaises(ValueError):
                    funnels.activation_plan(plan, current)
            configured = readback(plan, current)
            gate = funnels.activation_plan(plan, configured)
            self.assertTrue(gate["requires_separate_native_approval_before_first_shared_write"])
            self.assertEqual(gate["commands"], plan["activation"])
            with self.assertRaisesRegex(ValueError, "before activation approval"):
                funnels.verify(plan, readback(plan, current, "activation"))
            self.assertTrue(funnels.verify(plan, readback(plan, current, "activation"), "activation")["shared_activation_verified"])

    def test_inactive_inherited_owned_lists_are_saved_but_not_activated(self):
        for identifier, setting, field, inactive in (("inro-6025", "switchToHuman", "howToSwitch", "DontSwitch"),
                                                    ("inro-6022", "collectContactInfo", "howToCollect", "DoNotCollectInfo")):
            value = funnels.recipe(identifier)
            current = state(value)
            current["rules"][-1]["settings"][setting][field] = inactive
            current["rules"][-1]["settings"][setting]["inheritsFrom"] = None
            current["ownership"]["rule_sha256"] = funnels.fingerprint(current["rules"][-1])
            with self.subTest(identifier=identifier):
                plan = funnels.prepare(value, business(value), current, True)
                entries = plan["expected"]["fixture-owned"][setting]["rules" if setting == "switchToHuman" else "captures"]
                self.assertEqual(len(entries), 1)
                self.assertEqual(plan["ownership_before_write"]["rules"]["fixture-owned"], current["rules"][-1])

    def test_booking_link_mode_does_not_handoff_just_for_two_answers(self):
        value = funnels.recipe("inro-6025")
        data = business(value)
        data["parameters"].update({"next_step": "booking_link", "booking_url": "https://example.org/book"})
        plan = funnels.prepare(value, data, state(value), True)
        native = plan["expected"]["fixture-owned"]
        condition = native["switchToHuman"]["rules"][-1]["switchingConditions"]
        self.assertNotIn("after completing", condition)
        self.assertIn("do not hand off a successful booking-link", condition)
        self.assertIn("A link is not a confirmed booking", native["incomingMessages"]["messagePrompt"])

    def test_support_preserves_ordinary_inbound_without_keyword(self):
        value = funnels.recipe("inro-6085")
        data = business(value)
        self.assertNotIn("keyword", data["parameters"])
        self.assertEqual(value["design_changes"], [])
        plan = funnels.prepare(value, data, state(value), True)
        self.assertEqual(plan["commands"], [])
        self.assertTrue(plan["activation"])
        prompt = plan["expected"]["fixture-dm"]["incomingMessages"]["messagePrompt"]
        self.assertIn("No campaign keyword is required", prompt)
        self.assertNotIn("Campaign word:", prompt)
        brief = (funnels.REFERENCES / "chatfuel-execution.md").read_text(encoding="utf-8")
        self.assertIn(f"recipe `{value['id']}` uses `entry_match: {value['entry_match']}`; no keyword is required.", brief)

    def test_exact_coach_language_and_semantic_material_requirement(self):
        value = funnels.recipe("inro-6025")
        data = business(value)
        data["parameters"].update({"language": "Russian", "public_text": "Материал в личных сообщениях и запросах.",
                                   "initial_text": "Вот Упражнение: https://example.org/guide. Ответь ДА для двух вопросов.",
                                   "resource_title": "Упражнение", "resource_url": "https://example.org/guide"})
        plan = funnels.prepare(value, data, state(value), True)
        self.assertEqual(plan["preview"]["public"], data["parameters"]["public_text"])
        data["parameters"]["initial_text"] = "Reply first to get the material."
        with self.assertRaisesRegex(ValueError, "omits promised"):
            funnels.prepare(value, data, state(value), True)

    def test_booking_mode_and_material_pair_validation(self):
        value = funnels.recipe("inro-6025")
        data = business(value)
        data["parameters"]["next_step"] = "booking_link"
        with self.assertRaisesRegex(ValueError, "booking_url"):
            funnels.prepare(value, data, state(value), True)
        data["parameters"].update({"next_step": "handoff", "resource_title": "An exercise"})
        with self.assertRaisesRegex(ValueError, "together"):
            funnels.prepare(value, data, state(value), True)

    def test_copy_override_does_not_eagerly_format_optional_example(self):
        value = copy.deepcopy(funnels.recipe("inro-6025"))
        data = business(value)
        value["messages"]["initial"] = "Optional material: {resource_title} {resource_url}"
        plan = funnels.prepare(value, data, state(value), True)
        self.assertEqual(plan["preview"]["initial"], data["parameters"]["initial_text"])

    def test_disabled_foreign_rule_preserved_and_dm_off_allows_off_create(self):
        value = funnels.recipe("inro-6025")
        current = state(value)
        current["rules"].append(rule("disabled-foreign", "InstagramPostComments", False, False))
        plan = funnels.prepare(value, business(value), current, True)
        self.assertEqual(plan["preserved_rules"]["disabled-foreign"], funnels.fingerprint(current["rules"][-1]))
        current = state(value, False)
        current["rules"][2]["enabled"] = False
        plan = funnels.prepare(value, business(value), current, True)
        self.assertEqual(plan["stage"], "create-required")
        self.assertEqual(plan["activation"], [])
        self.assertEqual(plan["enable"], [])

    def test_shared_disabled_lists_preserved_and_duplicate_dm_word_blocks(self):
        value = funnels.recipe("inro-6022")
        for mutation in ("handoff", "capture", "word"):
            current = state(value)
            settings = current["rules"][2]["settings"]
            if mutation == "handoff":
                settings["switchToHuman"]["howToSwitch"] = "DontSwitch"
            elif mutation == "capture":
                settings["collectContactInfo"]["howToCollect"] = "DoNotCollectInfo"
            else:
                settings["incomingMessages"]["messagePrompt"] += "\n[coach-funnel:other]\nCampaign word: GUIDE.\n[/coach-funnel:other]"
            with self.subTest(mutation=mutation):
                if mutation == "word":
                    with self.assertRaises(ValueError):
                        funnels.prepare(value, business(value), current, True)
                else:
                    plan = funnels.prepare(value, business(value), current, True)
                    setting = "switchToHuman" if mutation == "handoff" else "collectContactInfo"
                    self.assertEqual(len(plan["expected"]["fixture-dm"][setting]["rules" if mutation == "handoff" else "captures"]), 1)

    def test_public_only_private_reply_disabled_before_separate_enable(self):
        value = funnels.recipe("inro-6082")
        plan = funnels.prepare(value, business(value), state(value), True)
        self.assertEqual(plan["expected"]["fixture-owned"]["privateReply"]["privateReplyHowToReply"], "DontReply")
        self.assertTrue(all(item["phase"] == "configure" for item in plan["commands"]))
        self.assertEqual(plan["enable"][0]["phase"], "after-verified-readback-and-separate-approval")
        self.assertNotIn("fixture-dm", plan["expected"])

    def test_preserve_shared_prompt_handoff_and_capture_lists(self):
        value = funnels.recipe("inro-6022")
        current = state(value)
        dm = current["rules"][2]
        plan = funnels.prepare(value, business(value), current, True)
        expected = plan["expected"][dm["id"]]
        self.assertTrue(expected["incomingMessages"]["messagePrompt"].startswith(dm["settings"]["incomingMessages"]["messagePrompt"]))
        self.assertEqual(expected["switchToHuman"]["rules"][:-1], dm["settings"]["switchToHuman"]["rules"])
        self.assertEqual(expected["collectContactInfo"]["captures"][:-1], dm["settings"]["collectContactInfo"]["captures"])
        self.assertTrue(expected["collectContactInfo"]["captures"][-1]["name"].endswith("_email"))
        self.assertNotIn("attribute", expected["collectContactInfo"]["captures"][-1])

    def test_shared_followup_and_capture_validation_errors_block(self):
        value = funnels.recipe("inro-6022")
        for mutation in ("followUps", "collectContactInfo"):
            current = state(value)
            if mutation == "followUps":
                current["rules"][2]["settings"][mutation]["howToSend"] = "Send"
            else:
                current["rules"][2]["settings"][mutation]["captures"][0]["validationErrors"] = ["Invalid name"]
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.prepare(value, business(value), current, True)

    def test_ownership_must_not_adopt_shared_rule_or_changed_custom(self):
        value = funnels.recipe("inro-6025")
        for mutation in ("base", "changed", "wrong-account", "enabled"):
            current = state(value)
            if mutation == "base":
                current["ownership"]["rule_id"] = "fixture-comment-base"
            elif mutation == "changed":
                current["rules"][-1]["settings"]["privateReply"]["exactTextReply"] = "Changed elsewhere."
            elif mutation == "wrong-account":
                current["ownership"]["account_id"] = "other-account"
            else:
                current["rules"][-1]["enabled"] = True
                current["ownership"]["rule_sha256"] = funnels.fingerprint(current["rules"][-1])
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.prepare(value, business(value), current, True)

    def test_overlap_and_wrong_posts_block_without_foreign_mutation(self):
        value = funnels.recipe("inro-6025")
        current = state(value)
        current["rules"].append(rule("foreign-custom", "InstagramPostComments", False, True))
        with self.assertRaisesRegex(ValueError, "overlap"):
            funnels.prepare(value, business(value), current, True)
        data = business(value)
        data["parameters"]["post_ids"] = ["foreign-account-post"]
        with self.assertRaisesRegex(ValueError, "source mixing"):
            funnels.prepare(value, data, state(value), True)

    def test_unknown_create_or_send_never_becomes_retry(self):
        value = funnels.recipe("inro-6025")
        for kind in ("create", "send"):
            current = state(value)
            current["actions"] = [{"kind": kind, "status": "unknown"}]
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "do not retry"):
                funnels.prepare(value, business(value), current, True)

    def test_stale_incomplete_wrong_channel_state_blocks(self):
        value = funnels.recipe("inro-6220")
        for changed in ({"observed_at": (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()},
                        {"read_complete": False}, {"connected": False}, {"platform": "WebWidget"}):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                funnels.prepare(value, business(value), {**state(value), **changed}, True)

    def test_readback_rejects_shared_side_effects_early_enable_and_inheritance(self):
        value = funnels.recipe("inro-6025")
        current = state(value)
        plan = funnels.prepare(value, business(value), current, True)
        for mutation in ("base-disabled", "private-inherited", "early-enable", "other-setting", "new-rule"):
            actual = readback(plan, current)
            if mutation == "base-disabled":
                actual["rules"][1]["enabled"] = False
            elif mutation == "private-inherited":
                actual["rules"][-1]["settings"]["privateReply"]["inheritsFrom"] = "fixture-comment-base"
            elif mutation == "early-enable":
                actual["rules"][-1]["enabled"] = True
            elif mutation == "other-setting":
                actual["rules"][2]["settings"]["whenAIReplies"]["option"] = "OutsideOfWorkingHours"
            else:
                actual["rules"].append(rule("new-rule", "InstagramPostComments", False, False))
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                funnels.verify(plan, actual)

    def test_capture_readback_validation_error_and_changed_plan_block(self):
        value = funnels.recipe("inro-6022")
        current = state(value)
        plan = funnels.prepare(value, business(value), current, True)
        actual = readback(plan, current, "activation")
        actual["rules"][2]["settings"]["collectContactInfo"]["captures"][-1]["validationErrors"] = ["Invalid capture"]
        with self.assertRaisesRegex(ValueError, "validationErrors"):
            funnels.verify(plan, actual, "activation")
        plan["preview"]["initial"] = "Unapproved revision."
        with self.assertRaisesRegex(ValueError, "plan changed"):
            funnels.verify(plan, readback(plan, current))


class EvidenceTests(unittest.TestCase):
    def test_business_outcome_receipts_are_mandatory_for_material_and_next_step(self):
        value = funnels.recipe("inro-6025")
        for missing in ("two_actual_answers", "material_received", "material_opened_on_phone", "handoff_confirmed", "booking_link_received", "no_false_booking_confirmation"):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = synthetic_acceptance(root, value, ("handoff", "booking_link", "handoff"), True)
                self.assertTrue(funnels.evidence_check(value, root, ENV)["eligible"])
                run = manifest["runs"][1 if missing in {"booking_link_received", "no_false_booking_confirmation"} else 0]
                del run["checks"][missing]
                save_fixture(root, value["id"] + ".json", manifest)
                self.assertFalse(funnels.evidence_check(value, root, ENV)["eligible"])

    def test_actual_answers_destination_and_native_origin_are_checked(self):
        value = funnels.recipe("inro-6025")
        for mutation in ("answers", "recipient", "destination", "origin", "refs"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = synthetic_acceptance(root, value, material=True)
                run = manifest["runs"][0]
                check = "two_actual_answers" if mutation in {"answers", "recipient"} else "material_received"
                reference = run["checks"][check]
                receipt = funnels.load(root / reference["path"])
                if mutation == "answers":
                    receipt["answers"] = []
                elif mutation == "recipient":
                    receipt["answers"][0]["recipient_id"] = "another-person"
                elif mutation == "destination":
                    receipt["destination"] = "https://example.org/different-material"
                elif mutation == "origin":
                    receipt["origin"] = "human-review"
                else:
                    receipt["native_refs"] = []
                run["checks"][check] = save_fixture(root, reference["path"], receipt)
                save_fixture(root, value["id"] + ".json", manifest)
                self.assertFalse(funnels.evidence_check(value, root, ENV)["eligible"])

    def test_unproven_booking_variant_cannot_enter_sanitized_metadata(self):
        value = funnels.recipe("inro-6025")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = synthetic_acceptance(root, value)
            entry = funnels.evidence_check(value, root, ENV)["catalog_metadata"]
            real_load = funnels.load
            def with_catalog(path):
                if Path(path) == funnels.REFERENCES / "catalog.json":
                    return {"schema_version": 1, "recipes": [entry]}
                return real_load(path)
            with patch.object(funnels, "load", side_effect=with_catalog):
                data = business(value)
                self.assertTrue(funnels.prepare(value, data, state(value))["runtime_accepted"])
                data["parameters"].update({"next_step": "booking_link", "booking_url": "https://example.org/book"})
                with self.assertRaisesRegex(ValueError, "variant has no runtime acceptance"):
                    funnels.prepare(value, data, state(value))
                data["parameters"].update({"next_step": "handoff", "resource_title": "Decision exercise", "resource_url": "https://example.org/exercise",
                                           "initial_text": "Decision exercise: https://example.org/exercise. Reply YES."})
                with self.assertRaisesRegex(ValueError, "material delivery has no runtime acceptance"):
                    funnels.prepare(value, data, state(value))
            manifest["acceptance"]["variants"].append("booking_link")
            save_fixture(root, value["id"] + ".json", manifest)
            self.assertFalse(funnels.evidence_check(value, root, ENV)["eligible"])

    def test_no_receipts_or_fixture_claims_cannot_release(self):
        value = funnels.recipe("inro-6220")
        self.assertFalse(funnels.evidence_check(value, None, ENV)["eligible"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = synthetic_acceptance(root, value)
            manifest["fixture"] = True
            save_fixture(root, value["id"] + ".json", manifest)
            self.assertFalse(funnels.evidence_check(value, root, ENV)["eligible"])

    def test_structurally_complete_synthetic_records_exercise_integrity_not_e2e(self):
        value = funnels.recipe("inro-6220")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            synthetic_acceptance(root, value)
            self.assertTrue(funnels.evidence_check(value, root, ENV)["eligible"])
            self.assertFalse(funnels.selection(value, [], False, ENV)["eligible"])

    def test_false_release_variants_block(self):
        value = funnels.recipe("inro-6220")
        for mutation in ("one-live", "same-account", "missing-branch", "missing-stop", "fixture-receipt", "recipient-mix", "source-mix", "changed-receipt", "changed-input", "changed-plan", "no-review", "assisted-user", "no-private-recovery"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                manifest = synthetic_acceptance(root, value)
                run = manifest["runs"][1]
                if mutation == "one-live":
                    run["mode"] = "preview"
                elif mutation == "same-account":
                    run["account_id"] = manifest["runs"][0]["account_id"]
                elif mutation in {"missing-branch", "missing-stop"}:
                    del run["checks"]["non_follower" if mutation == "missing-branch" else "stop"]
                elif mutation in {"fixture-receipt", "recipient-mix", "source-mix", "changed-receipt"}:
                    ref = run["checks"]["content"]
                    receipt = funnels.load(root / ref["path"])
                    if mutation == "fixture-receipt":
                        receipt["fixture"] = True
                    elif mutation == "recipient-mix":
                        receipt["bindings"]["recipient_id"] = "another-person"
                    elif mutation == "source-mix":
                        receipt["bindings"]["source"]["post_id"] = "another-post"
                    else:
                        receipt["observation"] = "Changed bytes without updated hash."
                    fresh = save_fixture(root, ref["path"], receipt)
                    if mutation != "changed-receipt":
                        run["checks"]["content"] = fresh
                elif mutation in {"changed-input", "changed-plan"}:
                    ref = run["inputs" if mutation == "changed-input" else "prepared_plan"]
                    content = funnels.load(root / ref["path"])
                    if mutation == "changed-input":
                        content["parameters"]["resource_title"] = "Another material"
                    else:
                        content["account_id"] = "another-account"
                    run["inputs" if mutation == "changed-input" else "prepared_plan"] = save_fixture(root, ref["path"], content)
                elif mutation == "no-review":
                    manifest["acceptance"]["status"] = "pending"
                elif mutation == "assisted-user":
                    manifest["acceptance"]["target_users"][0]["unassisted"] = False
                else:
                    manifest["acceptance"]["fresh_install_and_private_recovery"] = False
                save_fixture(root, value["id"] + ".json", manifest)
                self.assertFalse(funnels.evidence_check(value, root, ENV)["eligible"])

    def test_changed_recipe_and_environment_invalidate_acceptance(self):
        value = funnels.recipe("inro-6220")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            synthetic_acceptance(root, value)
            altered = copy.deepcopy(value)
            altered["messages"]["initial"] += " Changed promise."
            self.assertFalse(funnels.evidence_check(altered, root, ENV)["eligible"])
            self.assertFalse(funnels.evidence_check(value, root, {**ENV, "model": "new-model"})["eligible"])

    def test_catalogue_requires_exact_version_digest_environment_and_evidence(self):
        value = funnels.recipe("inro-6220")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            synthetic_acceptance(root, value)
            real_load = funnels.load
            entry = funnels.evidence_check(value, root, ENV)["catalog_metadata"]
            def with_catalog(path):
                if Path(path) == funnels.REFERENCES / "catalog.json":
                    return {"schema_version": 1, "recipes": [entry]}
                return real_load(path)
            with patch.object(funnels, "load", side_effect=with_catalog):
                self.assertTrue(funnels.selection(value, [], False, ENV)["eligible"])
                self.assertEqual(len(funnels.catalog_entries()), 1)
                entry["version"] = "wrong-version"
                self.assertFalse(funnels.selection(value, [], False, ENV)["eligible"])

    def test_relocated_runtime_discovers_accepted_metadata_without_private_receipts(self):
        value = funnels.recipe("inro-6220")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            proof = root / "private-proof"
            proof.mkdir()
            synthetic_acceptance(proof, value)
            entry = funnels.evidence_check(value, proof, ENV)["catalog_metadata"]
            self.assertIsNotNone(entry)
            self.assertNotIn("synthetic-account", json.dumps(entry))
            self.assertNotIn("runs", entry)
            installed = root / "installed plugin"
            shutil.copytree(ROOT / "plugin", installed)
            shutil.copytree(ROOT / "internal/funnels", root / "internal/funnels")
            save_fixture(root, "internal/funnels/catalog.json", {"schema_version": 1, "recipes": [entry]})
            shutil.rmtree(proof)
            environment_path = root / "environment.json"
            save_fixture(root, environment_path.name, ENV)
            for command in (["catalog"], ["catalog", "--environment", str(environment_path)],
                            ["select", value["id"], "--environment", str(environment_path)]):
                result = subprocess.run([sys.executable, str(installed / "scripts/funnels.py"), *command], capture_output=True, text=True, cwd=directory)
                self.assertEqual(result.returncode, 0, result.stderr)
                response = json.loads(result.stdout)
                if command[0] == "catalog":
                    self.assertEqual([item["id"] for item in response["recipes"]], [value["id"]])
                else:
                    self.assertTrue(response["eligible"])
            save_fixture(root, environment_path.name, {**ENV, "model": "changed-runtime-model"})
            result = subprocess.run([sys.executable, str(installed / "scripts/funnels.py"), "catalog", "--environment", str(environment_path)], capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["recipes"], [])


class AttributionAndPackagingTests(unittest.TestCase):
    def test_attribution_rejects_recipient_source_and_campaign_mixing(self):
        value = funnels.recipe("inro-6025")
        card = {"recipe_id": value["id"], "recipe_digest": funnels.recipe_digest(value), "account_id": "fixture-account", "bot_id": "fixture-bot",
                "campaign_id": "fixture-campaign", "post_ids": ["fixture-post"], "keyword": "GUIDE"}
        event = {"id": "fixture-entry", "recipe_id": value["id"], "account_id": card["account_id"], "bot_id": card["bot_id"],
                 "campaign_id": card["campaign_id"], "recipient_id": "fixture-person", "chain": [
                     {"id": "comment", "recipient_id": "fixture-person", "media_id": "fixture-post", "comment_id": "c1", "text": "GUIDE", "private_reply_id": "dm1"},
                     {"id": "dm1", "recipient_id": "fixture-person"}]}
        complete = funnels.attribute(value, card, {"events": [event], "pagination_complete": True})
        self.assertEqual(complete["confirmed_event_ids"], [event["id"]])
        self.assertFalse(complete["lead_outcome_verified"])
        for mutation in ("recipient", "media", "keyword", "linked-dm", "campaign"):
            changed = copy.deepcopy(event)
            if mutation == "recipient":
                changed["chain"][1]["recipient_id"] = "another-person"
            elif mutation == "media":
                changed["chain"][0]["media_id"] = "another-post"
            elif mutation == "keyword":
                changed["chain"][0]["text"] = "OTHER-CAMPAIGN"
            elif mutation == "linked-dm":
                changed["chain"][0]["private_reply_id"] = "missing-dm"
            else:
                changed["campaign_id"] = "another-campaign"
            with self.subTest(mutation=mutation):
                result = funnels.attribute(value, card, {"events": [changed], "pagination_complete": True})
                self.assertEqual(result["confirmed_event_ids"], [])
                self.assertFalse(result["empty_claim_allowed"])
        self.assertFalse(funnels.attribute(value, card, {"events": [], "pagination_complete": False})["empty_claim_allowed"])
        self.assertTrue(funnels.attribute(value, card, {"events": [], "pagination_complete": True})["empty_claim_allowed"])

    def test_relocated_plugin_cli_preserves_recipe_paths_without_environment(self):
        with tempfile.TemporaryDirectory() as directory:
            relocated = Path(directory) / "plugin with spaces"
            shutil.copytree(ROOT / "plugin", relocated)
            shutil.copytree(ROOT / "internal/funnels", Path(directory) / "internal/funnels")
            for command in (["validate"], ["catalog"], ["select", "inro-6025", "--developer-qa"]):
                result = subprocess.run([sys.executable, str(relocated / "scripts/funnels.py"), *command], capture_output=True, text=True, cwd=directory)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIsInstance(json.loads(result.stdout), dict)

    def test_no_dependency_on_external_docs_for_runtime_skill(self):
        skill = (ROOT / "plugin/skills/funnels/SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("../../../docs", skill)
        self.assertNotIn("ffmpeg", skill.lower())


if __name__ == "__main__":
    if sys.argv[1:2] == ["export-qa"]:
        export_qa_cli(sys.argv[2:])
    else:
        unittest.main()
