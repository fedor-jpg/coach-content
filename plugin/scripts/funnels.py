#!/usr/bin/env python3
"""Offline funnel preparation and evidence checks. No network or native execution."""

import argparse
import copy
import hashlib
import json
import re
import string
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT.parent / "internal/funnels"
CUSTOMER_SKILL = ROOT / "skills/funnels"
ENVIRONMENT_KEYS = {"host", "model", "connector_contract"}
CONTRACT_REQUESTS = [
    {"name": "Mutation", "filter": "fuelyAutomation"},
    {"name": "FuelyAutomation"},
    {"name": "FuelySettingUpdateInput"},
    {"names": ["FuelySettingIncomingMessagesInput", "FuelySettingSwitchToHumanInput", "FuelySettingFollowUpsInput", "FuelySettingCollectContactInfoInput", "FuelySettingWhenAIRepliesInput"]},
    {"names": ["FuelySettingKeywordsInput", "FuelySettingListOfPostsInput", "FuelySettingPublicReplyInput", "FuelySettingPrivateReplyInput"]},
    {"names": ["FuelySettingIncomingMessagesUpdateInput", "FuelySettingSwitchToHumanUpdateInput", "FuelySettingFollowUpsUpdateInput", "FuelySettingCollectContactInfoUpdateInput", "FuelySettingWhenAIRepliesUpdateInput"]},
    {"names": ["FuelySettingKeywordsUpdateInput", "FuelySettingListOfPostsUpdateInput", "FuelySettingPublicReplyUpdateInput", "FuelySettingPrivateReplyUpdateInput", "FuelyAutomationScope"]},
    {"names": ["FuelySettingIncomingMessagesHowToReply", "FuelySettingSwitchToHumanHowToSwitch", "FuelySettingFollowUpsHowToSend", "FuelySettingCollectContactInfoHowToCollect", "FuelySettingWhenAIRepliesOptions"]},
    {"names": ["FuelySettingKeywordsReactTo", "FuelySettingPublicReplyHowToReply", "FuelySettingPrivateReplyHowToReply", "FuelySettingSwitchToHumanRuleInput", "FuelySettingCollectContactInfoEntryInput"]},
    {"name": "FuelySettingSwitchToHumanRuleAssigneeInput"},
]
CREATE = "mutation($botID: BotID!, $scope: FuelyAutomationScope!, $name: String!) { fuelyAutomationCreate(botID: $botID, scope: $scope, name: $name) { id enabled } }"
UPDATE = "mutation($botID: BotID!, $id: FuelyAutomationID!, $update: FuelySettingUpdateInput!) { fuelyAutomationUpdateSetting(botID: $botID, id: $id, update: $update) { id enabled } }"
ENABLE = "mutation($botID: BotID!, $id: FuelyAutomationID!, $enabled: Boolean!) { fuelyAutomationSetEnabled(botID: $botID, id: $id, enabled: $enabled) { id enabled } }"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode()).hexdigest()


def inside(root, relative):
    path = Path(relative)
    require(not path.is_absolute() and ".." not in path.parts, "Unsafe relative path")
    resolved = (root / path).resolve()
    require(resolved.is_relative_to(root.resolve()) and resolved.is_file(), "Missing or escaping reference")
    require(not any(part.is_symlink() for part in [root / path, *(root / path).parents] if part != root.parent), "Symlink reference")
    return resolved


def recipe(identifier):
    require(re.fullmatch(r"inro-(?:[0-9]{4}|comment-moderation)", identifier) is not None, "Invalid recipe ID")
    value = load(inside(REFERENCES, f"recipes/{identifier}.json"))
    require(value["id"] == identifier and value["schema_version"] == 1, "Recipe identity/schema mismatch")
    return value


def recipe_digest(value):
    return fingerprint({"recipe": value, "execution": (REFERENCES / "chatfuel-execution.md").read_text(encoding="utf-8"),
                        "skill": (CUSTOMER_SKILL / "SKILL.md").read_text(encoding="utf-8"),
                        "operations": (CUSTOMER_SKILL / "references/operations.md").read_text(encoding="utf-8"),
                        "customer_recipe": load(REFERENCES / "customer-recipes" / f"{value['id']}.json")
                        if (REFERENCES / "customer-recipes" / f"{value['id']}.json").is_file() else None,
                        "helper": Path(__file__).read_text(encoding="utf-8")})


def environment(value):
    require(isinstance(value, dict) and set(value) == ENVIRONMENT_KEYS, "Environment must pin host, model and connector_contract")
    require(all(isinstance(item, str) and item.strip() for item in value.values()), "Empty environment pin")
    return value


def contract_pin(bundle, complete=False):
    require(complete is True, "Attest complete successful tool responses, including every pagination footer")
    require(set(bundle) == {"schema_version", "source", "observed_at", "definition_set", "records"}, "Unexpected schema bundle fields")
    require(bundle["schema_version"] == 1 and bundle["source"] == "chatfuel-public-api.get_type"
            and bundle["definition_set"] == "coach-funnel-native-v1", "Wrong schema source or definition set")
    age = (datetime.now(timezone.utc) - timestamp(bundle["observed_at"])).total_seconds()
    require(-60 <= age <= 900, "Stale schema bundle; repeat actual get_type reads")
    records = bundle["records"]
    require(isinstance(records, list) and len(records) == len(CONTRACT_REQUESTS), "Incomplete definition set")
    expected = {fingerprint(arguments) for arguments in CONTRACT_REQUESTS}
    seen = set()
    for record in records:
        require(set(record) == {"tool", "arguments", "text"} and record["tool"] == "get_type", "Expected verbatim get_type source records")
        key = fingerprint(record["arguments"])
        require(key in expected and key not in seen, "Missing, duplicate or unexpected definition request")
        require(isinstance(record["text"], str) and record["text"].strip(), "Missing definition text")
        text = record["text"]
        require(not re.search(r"\b(?:truncated|truncation)\b|^\s*(?:error|tool error|failed|not found)\b|\.\.\.", text, re.I | re.M),
                "Schema response contains an error or truncation marker")
        names = record["arguments"].get("names", [record["arguments"].get("name")])
        declarations = re.findall(r"^(?:type|input|enum)\s+([A-Za-z_][A-Za-z0-9_]*)\b[^\r\n{]*\{", text, re.M)
        require(len(declarations) == len(names) and set(declarations) == set(names)
                and text.count("{") == text.count("}") == len(names), "Missing, wrong or incomplete named definitions")
        footers = re.findall(r'^\s*shown (\d+)-(\d+) of (\d+) matching\b[^\n]*$', text, re.M)
        require(len(footers) == len(re.findall(r'^\s*shown\b', text, re.M)), "Unrecognized schema pagination footer")
        require(all(int(start) == 1 and int(end) == int(total) and int(total) > 0 for start, end, total in footers)
                and ("filter" not in record["arguments"] or bool(footers)), "Incomplete schema pagination")
        seen.add(key)
    payload = {key: value for key, value in bundle.items() if key != "observed_at"}
    payload["records"] = sorted(records, key=lambda record: fingerprint(record["arguments"]))
    return {"connector_contract": "chatfuel-funnel-input-sha256:" + fingerprint(payload),
            "definition_set": bundle["definition_set"], "observed_at": bundle["observed_at"], "records": len(records),
            "scope": "Exact named mutation/input contract reads, not a whole API version or readback schema",
            "limit": "Checks supplied bundle integrity and completeness attestation, not native provenance or runtime acceptance. Actual current tool reads and native readback remain required."}


def validate():
    index = load(REFERENCES / "research.json")
    rows = index["sources"]
    require(index["schema_version"] == 1 and index["source_count"] == len(rows) == 30, "Expected 30 sources")
    ids = [row["id"] for row in rows]
    require(len(set(ids)) == 30, "Duplicate source")
    require({path.stem for path in (REFERENCES / "recipes").glob("*.json")} == set(ids), "Recipe coverage mismatch")
    counts = {}
    for row in rows:
        value = recipe(row["id"])
        require(inside(REFERENCES, row["recipe"]) == REFERENCES / "recipes" / f"{value['id']}.json", "Wrong recipe reference")
        require(value["source"]["id"] == row["id"] and value["source"]["title"] == row["title"], "Source mixing")
        require(value["family"] == row["family"] and value["status"] == row["status"], "Index disagreement")
        require(value["status"] in {"candidate", "changed", "unverified", "unavailable"}, "Invalid design status")
        require(value["entry"] in {"comment", "dm", "public", "none"} and value["platforms"] == ["Instagram"], "Unsupported platform/entry")
        require(isinstance(value["supported_requirements"], list) and not (set(value["supported_requirements"]) & set(value["unsupported_requirements"])), "Conflicting requirement declarations")
        require(bool(value["design_changes"]) == (value["status"] == "changed"), "Changed-condition declaration missing")
        require(set(value["required_inputs"]) <= set(value["allowed_parameters"]), "Parameter schema mismatch")
        require(all(p["type"] in {"text", "url", "post_ids"} and p["description"] for p in value["allowed_parameters"].values()), "Invalid parameter schema")
        for template in value["messages"].values():
            names = {name for _, name, _, _ in string.Formatter().parse(template) if name}
            require(names <= set(value["allowed_parameters"]), "Undeclared message parameter")
        require(all(value.get(key) for key in ("goal", "outcome", "business_outcomes", "negative_cases", "runtime_checks", "transitions", "resume", "stop")), "Incomplete recipe")
        require(set(value["business_outcomes"]) <= set(value["runtime_checks"]), "Business outcome checks missing from runtime requirements")
        for outcome in value["business_outcomes"].values():
            require(outcome["origin"] in {"native-readback", "recipient-observation", "human-review"} and outcome["description"] and outcome["min_native_refs"] >= 1, "Invalid business outcome evidence contract")
        require(all(set(step) == {"event", "actor", "action", "evidence"} and all(step.values()) for step in value["transitions"]), "Incomplete transition")
        require((REFERENCES / "recipes" / value["execution_reference"]).resolve() == (REFERENCES / "chatfuel-execution.md").resolve(), "Invalid execution reference")
        if value["status"] in {"unverified", "unavailable"}:
            require(bool(value["blockers"]), "Missing blocker")
        counts[value["status"]] = counts.get(value["status"], 0) + 1
    require(sum(counts.values()) == 30, "Source matrix coverage drift")
    catalog = load(REFERENCES / "catalog.json")
    require(catalog["schema_version"] == 1 and isinstance(catalog["recipes"], list), "Invalid catalogue")
    published = [entry["id"] for entry in catalog["recipes"]]
    require(len(set(published)) == len(published) and set(published) <= set(ids), "Invalid catalogue IDs")
    for entry in catalog["recipes"]:
        value = recipe(entry["id"])
        accepted_entry(value, entry)
    return {"sources": 30, "designs": counts, "catalog_entries": len(published), "runtime_claim": "none from validation"}


def timestamp(text):
    value = datetime.fromisoformat(text.replace("Z", "+00:00"))
    require(value.tzinfo is not None, "Timestamp must include timezone")
    return value


def snapshot(value):
    require(value.get("schema_version") == 1 and value.get("read_complete") is True, "Incomplete normalized state read")
    require(value.get("connected") is True and value.get("platform") == "Instagram", "Connected Instagram required")
    require(all(isinstance(value.get(key), str) and value[key].strip() for key in ("bot_id", "account_id")), "Account/bot IDs required")
    age = (datetime.now(timezone.utc) - timestamp(value["observed_at"])).total_seconds()
    require(-60 <= age <= 900, "Stale current-state snapshot; read native state again")
    environment(value["environment"])
    require(isinstance(value.get("rules"), list) and isinstance(value.get("posts"), list), "Rules/posts must be complete lists")
    rules = value["rules"]
    require(len({rule["id"] for rule in rules}) == len(rules), "Duplicate rule IDs")
    require(all(isinstance(rule.get("enabled"), bool) and isinstance(rule.get("isBase"), bool) and isinstance(rule.get("settings"), dict) for rule in rules), "Invalid normalized rule")
    rule_map = {rule["id"]: rule for rule in rules}
    for rule in rules:
        for name, config in rule["settings"].items():
            parent = config.get("inheritsFrom")
            if parent is not None:
                inheritance_proof(rule, name, rule_map)
                require(setting(rule, name) == setting(rule_map[parent], name), "Inherited effective value differs from parent; normalize actual readback")
    require(not any(action.get("status") in {"unknown", "pending"} for action in value.get("actions", [])), "Unknown/pending action: reconcile native state, do not retry")
    return value


def setting(rule, name):
    require(name in rule["settings"], f"Read {name} including inherited effective value first")
    result = copy.deepcopy(rule["settings"][name])
    result.pop("inheritsFrom", None)
    return result


def require_reply_readiness(rule):
    require(setting(rule, "whenAIReplies").get("option") == "Always",
            f"Reply readiness for {rule['id']} requires Always; working-hours restrictions or unknown availability need separate verification and approval, never an implicit schedule change")


def require_membership_available(name, current, plan=None, reserved=False):
    known = current.get("known_attribute_names")
    require(current.get("attribute_namespace_complete") is True,
            "Complete account-wide attribute namespace attestation required; finish native pagination")
    require(isinstance(known, list) and all(isinstance(item, str) and item.strip() for item in known),
            "Read account-wide known_attribute_names before waitlist preparation or activation")
    if plan is not None:
        origin = plan.get("restart_origin", plan)
        original = origin["ownership_before_write"].get("attribute_namespace", {})
        require(original.get("complete") is True and isinstance(original.get("names"), list)
                and name not in original["names"], "Saved complete namespace must prove original membership-name absence")
        require(all(name not in {entry["name"] for entry in setting(rule, "collectContactInfo")["captures"]}
                    for rule in origin["ownership_before_write"]["rules"].values()),
                "Saved original captures must not already own the membership name")
    registered_by_campaign = False
    for rule in current["rules"]:
        captures = setting(rule, "collectContactInfo").get("captures")
        require(isinstance(captures, list), "Read capture names for every native rule, including inactive rules")
        if name in {entry["name"] for entry in captures}:
            expected = plan["expected"].get(rule["id"], {}).get("collectContactInfo") if plan else None
            require(expected is not None and comparable_setting("collectContactInfo", rule["settings"]["collectContactInfo"])
                    == {**comparable_setting("collectContactInfo", expected), "inheritsFrom": None},
                    f"Membership attribute already exists in native rule {rule['id']}; choose a new launch-specific name")
            registered_by_campaign = True
    require(name not in known or registered_by_campaign or (reserved and plan is not None),
            "Membership attribute already exists in known account attributes without exact campaign-owned capture proof")


def command(operation, variables, phase="configure"):
    document = {"fuelyAutomationCreate": CREATE, "fuelyAutomationUpdateSetting": UPDATE,
                "fuelyAutomationSetEnabled": ENABLE}[operation]
    return {"executor": "Claude through current Chatfuel MCP execute_mutation", "operation": operation,
            "phase": phase, "requires_native_approval": True, "document": document, "variables": variables}


def update(bot_id, rule_id, name, value):
    return command("fuelyAutomationUpdateSetting", {"botID": bot_id, "id": rule_id, "update": {name: {"update": value}}})


def active_entries(rule, name, mode, inactive, field):
    config = setting(rule, name)
    require(isinstance(config.get(field), list), f"Read existing {name}/{field}")
    if config[mode] == inactive:
        return []
    entries = copy.deepcopy(config[field])
    if name == "collectContactInfo":
        require(all(not entry.get("validationErrors") for entry in entries), "Existing captures have validation errors")
        entries = [{key: entry[key] for key in ("name", "description")} for entry in entries]
    return entries


def seal(value):
    value["plan_sha256"] = fingerprint(value)
    return value


def comparable_setting(name, config):
    result = copy.deepcopy(config)
    if name == "collectContactInfo":
        for capture in result["captures"]:
            if not capture.get("validationErrors"):
                capture.pop("validationErrors", None)
    return result


def comparable_rule(rule):
    result = copy.deepcopy(rule)
    result["settings"] = {name: comparable_setting(name, config) for name, config in result["settings"].items()}
    return result


def within_owned_values(before, expected, actual):
    if actual is None:
        return False
    before, actual = comparable_rule(before), comparable_rule(actual)
    applied = copy.deepcopy(before)
    for name, config in expected.items():
        applied["settings"][name] = {**comparable_setting(name, config), "inheritsFrom": None}
    return (all(actual.get(key) == item for key, item in before.items() if key not in {"settings", "enabled"})
            and set(actual["settings"]) == set(before["settings"])
            and all(actual["settings"][name] in (config, applied["settings"][name]) for name, config in before["settings"].items()))


def check_plan(plan, current, stage, check_recipe=True):
    snapshot(current)
    require(plan.get("stage") == stage, "Configuration is not prepared" if stage == "configuration-prepared" else "Stop is not prepared")
    require(plan.get("plan_sha256") == fingerprint({key: item for key, item in plan.items() if key != "plan_sha256"}), "Prepared plan changed")
    if check_recipe:
        require(plan["recipe_digest"] == recipe_digest(recipe(plan["recipe_id"])), "Recipe changed; approvals are stale")
    require(all(plan[key] == current[key] for key in ("account_id", "bot_id", "environment")), "Readback account/environment mismatch")


def inheritance_proof(rule, name, rules):
    proof = {}
    parent = rule["settings"][name].get("inheritsFrom")
    while parent is not None:
        require(parent in rules and parent not in proof and parent != rule["id"], "Unresolved or cyclic inheritance")
        proof[parent] = copy.deepcopy(rules[parent])
        parent = proof[parent]["settings"][name].get("inheritsFrom")
    return proof


def inputs_for(value, data):
    require(set(data) <= {"campaign_id", "parameters", "accepted_changes"}, "Unknown business input field")
    require(re.fullmatch(r"[a-z0-9][a-z0-9-]{0,47}", data.get("campaign_id", "")) is not None, "Invalid campaign ID")
    require(set(data.get("accepted_changes", [])) == set(value["design_changes"]), "Explicit acceptance of this design's changed conditions required")
    supplied = data.get("parameters", {})
    require(set(value["required_inputs"]) <= set(supplied) <= set(value["allowed_parameters"]), "Missing required or unknown recipe parameters")
    for key, spec in value["allowed_parameters"].items():
        if key not in supplied:
            continue
        item = supplied[key]
        if spec["type"] == "post_ids":
            require(isinstance(item, list) and 1 <= len(item) <= 50 and len(set(item)) == len(item) and all(isinstance(p, str) and p for p in item), "Expected 1-50 unique real post IDs")
        else:
            require(isinstance(item, str) and item.strip() and len(item) <= 1000, f"Invalid text: {key}")
            require("[coach-funnel:" not in item and "[/coach-funnel:" not in item, "Reserved campaign marker in input")
            if "values" in spec:
                require(item in spec["values"], f"Unsupported parameter value: {key}")
            if spec["type"] == "url":
                parsed = urlsplit(item)
                require(parsed.scheme == "https" and parsed.hostname and not parsed.username and not parsed.password, f"Public HTTPS destination required: {key}")
    if "keyword" in supplied:
        require(len(supplied["keyword"]) <= 50, "Keyword exceeds 50 characters")
    if value["family"] == "qualification":
        require(supplied["next_step"] != "booking_link" or "booking_url" in supplied, "Booking-link mode needs an existing booking_url")
    if value["id"] == "inro-6025":
        require(("resource_title" in supplied) == ("resource_url" in supplied), "Supply material title and URL together")
    if value["family"] == "waitlist":
        require(re.fullmatch(r"[a-z][a-z0-9_]{0,99}", supplied["membership_attribute"]) is not None, "Use a launch-specific lowercase native capture name")
        require("YES" in supplied["consent_text"] and "STOP" in supplied["consent_text"], "Waitlist consent must state YES and STOP")
    return supplied


def profile_destination(url, username):
    parsed = urlsplit(url)
    require(isinstance(username, str) and re.fullmatch(r"[A-Za-z0-9._]{1,30}", username) is not None, "Read the actual Instagram username first")
    require(username.casefold() not in {"p", "reel", "reels", "stories", "direct", "accounts", "explore", "about", ".", ".."}, "Expected a profile, not an Instagram route")
    require(parsed.scheme == "https" and parsed.netloc.lower() in {"instagram.com", "www.instagram.com"}
            and not parsed.query and not parsed.fragment and parsed.path.strip("/").casefold() == username.casefold()
            and parsed.path in {"/" + username, "/" + username + "/"}, "QR URL must be the verified account's HTTPS Instagram profile")
    return url


def create_qr(url, username, output):
    profile_destination(url, username)
    require(output.suffix.lower() == ".png" and not output.exists(), "Use a new PNG output path; do not overwrite an existing artifact")
    try:
        import qrcode
    except ImportError as error:
        raise ValueError("QR needs qrcode[pil] in this host. Check/import it, then use an approved local dependency install if missing.") from error
    output.parent.mkdir(parents=True, exist_ok=True)
    image = qrcode.make(url, box_size=10, border=4)
    image.save(output, format="PNG")
    return {"path": str(output.resolve()), "profile_url": url, "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            "runtime_accepted": False, "scan_attribution": False}


def accepted_entry(value, entry, env=None):
    require(set(entry) <= {"id", "version", "digest", "environment", "acceptance", "goal", "recipe"}, "Private QA data must not enter the customer catalogue")
    require(entry.get("id") == value["id"] and entry.get("digest") == recipe_digest(value) and entry.get("version") == value["version"], "Stale catalogue version")
    require(value["status"] not in {"unavailable", "unverified"} and not value["blockers"], "Blocked catalogue recipe")
    environment(entry["environment"])
    accepted = entry["acceptance"]
    require(set(accepted) <= {"status", "accepted_at", "variants", "material_delivery"}, "Private acceptance details must remain outside the installed catalogue")
    require(accepted.get("status") == "runtime-accepted", "Missing maintainer runtime acceptance")
    timestamp(accepted["accepted_at"])
    variants = {"handoff", "booking_link"} if value["family"] == "qualification" else {"default"}
    require(isinstance(accepted.get("variants"), list) and bool(accepted["variants"]) and set(accepted["variants"]) <= variants, "Invalid accepted outcome variants")
    require(env is None or entry["environment"] == environment(env), "Runtime environment differs from accepted metadata")
    return {"id": value["id"], "version": value["version"], "digest": entry["digest"], "environment": entry["environment"],
            "acceptance": accepted, "goal": value["goal"], "recipe": f"recipes/{value['id']}.json"}


def catalog_entries(env=None):
    entries = []
    for entry in load(REFERENCES / "catalog.json")["recipes"]:
        try:
            entries.append(accepted_entry(recipe(entry["id"]), entry, env))
        except (ValueError, KeyError, TypeError):
            continue
    return entries


def selection(value, requirements, developer_qa=False, env=None):
    require(isinstance(requirements, list) and all(isinstance(item, str) for item in requirements), "Requirements must be a string list")
    conflicts = sorted(set(requirements) - set(value["supported_requirements"]))
    if conflicts or value["status"] in {"unavailable", "unverified"}:
        return {"eligible": False, "reason": conflicts or value["blockers"]}
    if developer_qa:
        return {"eligible": True, "mode": "developer-qa-only", "runtime_accepted": False}
    entry = next((item for item in catalog_entries(env) if item["id"] == value["id"]), None) if env is not None else None
    if not entry:
        return {"eligible": False, "reason": ["No accepted catalogue version for this environment"]}
    return {"eligible": True, "mode": "customer", "accepted_variants": entry["acceptance"]["variants"],
            "material_delivery": entry["acceptance"].get("material_delivery", False)}


def prepare(value, data, current, developer_qa=False):
    return _prepare(value, data, current, developer_qa)


def _prepare(value, data, current, developer_qa=False, restart_origin=None):
    parameters = inputs_for(value, data)
    current = snapshot(current)
    eligibility = selection(value, [], developer_qa, current["environment"])
    require(eligibility["eligible"], f"Recipe cannot be prepared: {eligibility.get('reason')}")
    if not developer_qa:
        variant = parameters["next_step"] if value["family"] == "qualification" else "default"
        require(variant in eligibility["accepted_variants"], "This outcome variant has no runtime acceptance")
        require(value["id"] != "inro-6025" or "resource_url" not in parameters or eligibility["material_delivery"], "Optional material delivery has no runtime acceptance")
    require(not value["blockers"], "; ".join(value["blockers"]))
    if value["id"] == "inro-6019":
        profile_destination(parameters["profile_url"], current.get("instagram_username"))
    if value["family"] == "waitlist":
        require_membership_available(parameters["membership_attribute"], current, restart_origin, reserved=restart_origin is not None)
    bot = current["bot_id"]
    campaign = data["campaign_id"]
    rendered = {key: parameters[key + "_text"] if key + "_text" in parameters else text.format_map(parameters)
                for key, text in value["messages"].items()}
    require(all(str(parameters[key]) in rendered["initial"] for key in value["initial_required_parameters"] if key in parameters), "Initial message omits promised material, destination, terms or disclosure")
    if value["entry"] == "public":
        require(rendered["public"] == parameters["thanks_text"], "Public-only copy must match the approved thanks_text")
    require(len(rendered["public"]) <= 1000 and len(rendered["initial"]) <= 1000, "Rendered reply exceeds native limit")
    rules = current["rules"]
    mains = [rule for rule in rules if rule["scope"] == "All" and rule["isBase"]]
    require(len(mains) == 1 and mains[0]["enabled"], "Main bot is off or unknown; separate global approval is required")
    if value["conversation"]:
        require(current.get("ai_compatible") is True, "AI plan/credits and channel readiness are not established")
    dm = None
    if value["entry"] == "dm" or value["conversation"]:
        bases = [rule for rule in rules if rule["scope"] == "InstagramDirectMessages" and rule["isBase"]]
        require(len(bases) == 1, "Read exactly one general Instagram DM base")
        dm = bases[0]
        require_reply_readiness(dm)
        require(not dm["enabled"] or setting(dm, "followUps")["howToSend"] == "DontSend", "Shared DM follow-ups conflict; do not disable them silently")
        require(not dm["enabled"] or setting(dm, "incomingMessages")["howToReply"] == "UsingAI", "General DM AI is not active")
    result = {"schema_version": 1, "mode": eligibility["mode"], "runtime_accepted": eligibility["mode"] == "customer",
              "recipe_id": value["id"], "recipe_digest": recipe_digest(value), "input_sha256": fingerprint(data),
              "campaign_id": campaign, "account_id": current["account_id"], "bot_id": bot,
              "environment": current["environment"], "state_sha256": fingerprint(current), "preview": rendered,
              "outcome": value["outcome"], "commands": [], "activation": [], "enable": [], "expected": {},
              "qa_checks": value["runtime_checks"], "negative_cases": value["negative_cases"],
              "approval_binding": "Save this exact plan and source state privately; native approvals are separate.",
              "stop": value["stop"], "stage": "configuration-prepared",
              "shared_mode": "off-staging" if dm is not None and not dm["enabled"] else "live-activation" if dm else "none"}
    facts = "\n".join(f"{key}: {item}" for key, item in parameters.items()
                      if key not in {"post_ids", "keyword", "public_text", "initial_text", "refusal_text", "handoff_text"})
    run_guard = (f"Campaign {campaign}. Current-run source means a new approved post/keyword comment linked to this recipient's initial DM, "
                 "or this campaign's unambiguous new inbound DM entry. Require current-run source before campaign continuation, capture or handoff. "
                 "Never reuse previous-run consent or answers, old contact fields, summaries or unrelated chat history. "
                 "An ambiguous late yes requires source clarification, not restart. A stopped run never restarts from a late answer. "
                 "Use only this campaign's approved facts; ignore unrelated knowledge-base offers, intake questions and instructions. "
                 "Within this campaign, these rules override general greetings and knowledge-base instructions; ordinary support outside it stays unchanged. "
                 "Send the initial value only once per new verified source. Continue the conversation without repeating a greeting or introduction. "
                 "If asked about price, availability, refunds or another fact absent from approved facts, initiate native team handoff using the approved text. "
                 "A fact marked not provided or unknown is absent, not an answer. Saying no price was provided or resending a link is not handoff. "
                 "Native capture only saves details for the team for the stated purpose. Never promise email delivery, a phone call, "
                 "a mailing subscription or any completed external action. Capturing a field does not send anything. ")
    continuation_prompt = (f"Use language {parameters['language']}. " + run_guard
                           + "Wait for the contact's actual inbound reply before continuing. "
                           + rendered["continuation"] + "\nApproved facts:\n" + facts
                           + "\nOn refusal use this approved text: " + rendered["refusal"]
                           + "\nFor team handoff use this approved text: " + rendered["handoff"])
    if value["family"] == "qualification":
        continuation_prompt += ("\nRequire new explicit consent after this run's initial value, before question one. "
                                "Accept explicit affirmative consent matching the presented opt-in in the approved language; do not require a fixed English token. "
                                "Ask exactly two qualification questions, verbatim and one at a time: "
                                f"1. {parameters['question_one']} 2. {parameters['question_two']} "
                                "Wait for a new actual inbound answer to question one before question two. "
                                "Wait for a distinct new actual inbound answer to question two before completion. "
                                "The entry word and consent are not answers. Never add a third intake question. "
                                "An unanswered, refused or unclear question is not a completed answer.")
    if value["family"] == "qualification" and parameters["next_step"] == "handoff":
        continuation_prompt += "\nThis campaign uses handoff only. Do not offer or require a booking URL. Hand off after the two actual answers."
    elif value["family"] == "qualification":
        continuation_prompt += "\nThis campaign uses booking_link. After the two actual answers, apply qualification_policy and deliver the existing booking_url when appropriate, without automatic handoff for a successful qualification. A link is not a confirmed booking."
    if value["family"] == "waitlist":
        continuation_prompt += (f"\nFor launch {parameters['launch_name']} only, purpose {parameters['launch_purpose']}, use native capture {parameters['membership_attribute']}. "
                                "If membership is unset, leave it unset before explicit YES. After this run's YES, persist joined. After STOP, persist withdrawn before any handoff. "
                                "Preserve existing joined/withdrawn values on restart; restart alone never reenrolls anyone or reuses old YES. "
                                "Bot prose is not membership proof. Confirm joined or withdrawn only from the actual saved attribute state. "
                                "Never change another launch, subscribe an existing email list or send automatic follow-ups. "
                                "STOP is withdrawal, not an immediate handoff. If the launch is ambiguous, ask which launch without changing attributes.")
    require(len(continuation_prompt) <= 5000, "Continuation prompt exceeds native limit")
    target = None
    ownership = current.get("ownership")
    if value["entry"] in {"comment", "public"}:
        require(set(parameters["post_ids"]) <= set(current["posts"]), "Post/account source mixing")
        if ownership:
            require(ownership.get("campaign_id") == campaign and ownership.get("recipe_id") == value["id"] and ownership.get("account_id") == current["account_id"], "Ownership card mismatch")
            target = next((rule for rule in rules if rule["id"] == ownership.get("rule_id")), None)
            require(target is not None and not target["isBase"] and target["scope"] == "InstagramPostComments", "Cannot own a shared/base/wrong-scope rule")
            require(ownership.get("rule_sha256") == fingerprint(target), "Owned rule changed; reconcile instead of overwriting")
            require(not target["enabled"], "Configure only an owned OFF custom; pause needs separate approval")
        for other in rules:
            if other["scope"] != "InstagramPostComments" or other["isBase"] or not other["enabled"] or other is target:
                continue
            posts = setting(other, "listOfPosts").get("postIDs", [])
            words = setting(other, "keywords")
            overlap = not posts or bool(set(posts) & set(parameters["post_ids"]))
            exact_disjoint = words.get("reactTo") == "CommentThatExactlyMatches" and parameters["keyword"].casefold() not in {word.casefold() for word in words.get("keywords", [])}
            require(not overlap or exact_disjoint, "Foreign custom may overlap; resolve conflict without taking ownership")
        if target is None:
            result["stage"] = "create-required"
            result["commands"] = [command("fuelyAutomationCreate", {"botID": bot, "scope": "InstagramPostComments", "name": f"Coach {campaign}"}, "create-off")]
            result["next"] = "After scoped approval, read the returned OFF custom and save its actual ID/ownership fingerprint. Rerun prepare; no settings or enable with guessed IDs."
            result["preserved_rules"] = {rule["id"]: fingerprint(rule) for rule in rules}
            return result
        rule_id = target["id"]
        updates = {"listOfPosts": {"postIDs": parameters["post_ids"]},
                   "keywords": {"reactTo": "CommentThatExactlyMatches", "keywords": [parameters["keyword"]]},
                   "publicReply": {"publicReplyHowToReply": "ExactText", "exactTextReply": rendered["public"], "messagePrompt": "Use the approved public text only.", "likeContactComment": False},
                   "privateReply": {"privateReplyHowToReply": "DontReply" if value["entry"] == "public" else "ExactText", "exactTextReply": rendered["initial"] or "No private campaign reply.", "messagePrompt": "Use the approved first message only."},
                   "followUps": {"howToSend": "DontSend", "messagePrompt": "Do not follow up for silence or clicks."},
                   "incomingMessages": {"howToReply": "UsingAI" if value["conversation"] else "DontReply", "messagePrompt": continuation_prompt}}
        updates["collectContactInfo"] = setting(target, "collectContactInfo")
        updates["collectContactInfo"]["captures"] = [{key: entry[key] for key in ("name", "description")}
                                                   for entry in updates["collectContactInfo"]["captures"]]
        if value["conversation"]:
            require_reply_readiness(target)
        for name, config in updates.items():
            result["commands"].append(update(bot, rule_id, name, config))
        result["expected"][rule_id] = updates
        result["enable"] = [command("fuelyAutomationSetEnabled", {"botID": bot, "id": rule_id, "enabled": True}, "after-verified-readback-and-separate-approval")]
        result["owned_rule_id"] = rule_id
    if value["entry"] == "dm" or value["conversation"]:
        previous = setting(dm, "incomingMessages")
        marker = f"[coach-funnel:{campaign}]"
        require(marker not in previous["messagePrompt"], "Campaign block already exists; reconcile return/revision instead of appending a duplicate")
        if value.get("entry_match") == "any_inbound":
            route = "Support route: ordinary inbound DM. No campaign keyword is required. Answer the actual support question from approved facts."
            require(route not in previous["messagePrompt"], "Another ordinary support route already exists; resolve the shared conflict")
        else:
            require(f"campaign word: {parameters['keyword']}.".casefold() not in previous["messagePrompt"].casefold(), "Another campaign uses this DM word; resolve ambiguous routing")
            route = f"Campaign word: {parameters['keyword']}. Only an unambiguous inbound word or linked comment reply starts this campaign. Ask which campaign for a late ambiguous yes."
        block = (f"{marker}\n{route} Initial value: {rendered['initial']}\n"
                 f"{continuation_prompt}\n"
                 "Ask questions one at a time only after an inbound answer. Never invent an answer. "
                 "No follow-ups for silence or clicks. On refusal, stop this campaign and hand off if needed; do not promise permanent opt-out. "
                 f"[/coach-funnel:{campaign}]")
        merged = previous["messagePrompt"] + "\n\n" + block
        require(len(merged) <= 5000, "Merged shared DM prompt exceeds 5000 characters")
        dm_updates = {"incomingMessages": {"howToReply": "UsingAI", "messagePrompt": merged}}
        if not dm["enabled"] and setting(dm, "followUps")["howToSend"] != "DontSend":
            dm_updates["followUps"] = {"howToSend": "DontSend", "messagePrompt": "Do not follow up for silence or clicks."}
        switches = setting(dm, "switchToHuman")
        require(isinstance(switches.get("rules"), list), "Read existing handoff rules")
        completion = ("after completing its two approved questions with actual answers" if value["family"] == "qualification" and parameters["next_step"] == "handoff" else
                      "only when a person is requested or an enquiry cannot be resolved; do not hand off a successful booking-link qualification merely because its two answers are complete" if value["family"] == "qualification" else
                      "when these approved handoff conditions apply: " + parameters["handoff_conditions"] if value["family"] == "support" else
                      "on an unresolved request requiring the team")
        condition = f"For campaign {campaign}, only with verified current-run source: {completion}, on current-run refusal or request for a person. Also switch to teammates when asked price, availability, refunds or any fact absent from this campaign's approved facts, including facts marked unknown or not provided. Do not merely say no price was provided, resend a link or repeat a greeting. Never use old consent or answers; qualification completion requires this run's new consent and two distinct subsequent inbound answers to the exact approved questions."
        if value["family"] == "waitlist":
            condition = f"For campaign {campaign}, only with verified current-run source, hand off only on an unresolved request or request for a person. STOP requires native {parameters['membership_attribute']} = withdrawn before any handoff. Do not hand off for YES or STOP alone. Never infer a saved attribute from bot prose."
        handoff = {"switchingConditions": condition, "messagePrompt": rendered["handoff"]}
        dm_updates["switchToHuman"] = {"howToSwitch": "SwitchToTeammates", "rules": active_entries(dm, "switchToHuman", "howToSwitch", "DontSwitch", "rules") + [handoff]}
        if target is not None:
            target_switches = setting(target, "switchToHuman")
            target_handoff = {"howToSwitch": "SwitchToTeammates", "rules": active_entries(target, "switchToHuman", "howToSwitch", "DontSwitch", "rules") + [handoff]}
            result["commands"].append(update(bot, target["id"], "switchToHuman", target_handoff))
            result["expected"][target["id"]]["switchToHuman"] = target_handoff
        if value["family"] == "waitlist" or value["id"] in {"inro-6018", "inro-6024", "inro-6026", "inro-6022", "inro-6027", "inro-6054"}:
            captures = setting(dm, "collectContactInfo")
            existing = active_entries(dm, "collectContactInfo", "howToCollect", "DoNotCollectInfo", "captures")
            field = "phone" if value["id"] == "inro-6027" else "email"
            name = "coach_" + campaign.replace("-", "_") + "_" + field
            if value["family"] == "waitlist":
                name = parameters["membership_attribute"]
            require(name not in {entry["name"] for entry in captures["captures"]}, "Capture attribute already exists; reconcile instead of duplicating")
            if value["family"] == "waitlist":
                capture = {"name": name, "description": f"Campaign {campaign} only. Fresh source and explicit new YES: joined. STOP: withdrawn before handoff. Otherwise preserve state, including unset. Never reuse old consent or answers."}
            else:
                capture = {"name": name, "description": f"Only after campaign {campaign}'s verified current-run source, new inbound reply and explicit agreement, save optional {field} for the team for {parameters['contact_purpose']}. Never reuse old contact fields or consent. Refusal preserves access. Confirm only actual saved details. Never promise email delivery, a phone call, mailing subscription or completed external action; capture sends nothing."}
            dm_updates["collectContactInfo"] = {"howToCollect": "CollectInfo", "captures": existing + [capture]}
            if target is not None:
                target_captures = setting(target, "collectContactInfo")
                target_entries = active_entries(target, "collectContactInfo", "howToCollect", "DoNotCollectInfo", "captures")
                require(name not in {entry["name"] for entry in target_captures["captures"]}, "Owned capture already exists; reconcile")
                target_capture = {"howToCollect": "CollectInfo", "captures": target_entries + [capture]}
                result["commands"].append(update(bot, target["id"], "collectContactInfo", target_capture))
                result["expected"][target["id"]]["collectContactInfo"] = target_capture
        for name, config in dm_updates.items():
            operation = update(bot, dm["id"], name, config)
            operation.update({"phase": "shared-activation" if dm["enabled"] else "shared-staging", "readback_after": True,
                              "warning": "This shared write changes live behavior immediately; it is not inactive staging or an atomic transaction." if dm["enabled"] else "Keep general DM OFF during staging. Enabling it requires separate approval for all shared effects."})
            result["activation" if dm["enabled"] else "commands"].append(operation)
        result["expected"][dm["id"]] = dm_updates
        result["shared_additions"] = {"rule_id": dm["id"], "prompt_block": block, "handoff_rule": handoff,
                                      "capture_names": [capture["name"]] if "collectContactInfo" in dm_updates else []}
        if not dm["enabled"]:
            result["enable"].insert(0, command("fuelyAutomationSetEnabled", {"botID": bot, "id": dm["id"], "enabled": True}, "separate-general-dm-enable-approval"))
    for settings in result["expected"].values():
        for config in settings.values():
            for key, text in config.items():
                if isinstance(text, str):
                    require(text.strip() and len(text) <= (5000 if "howToReply" in config else 3000), f"Invalid native text: {key}")
    changed = set(result["expected"])
    result["preserved_rules"] = {rule["id"]: fingerprint(rule) for rule in rules if rule["id"] not in changed}
    result["preserved_settings"] = {rule["id"]: {key: fingerprint(item) for key, item in rule["settings"].items() if key not in result["expected"].get(rule["id"], {})} for rule in rules if rule["id"] in changed}
    result["original_enabled"] = {rule["id"]: rule["enabled"] for rule in rules}
    result["activation_before"] = {rule["id"]: fingerprint(rule) for rule in rules if rule["isBase"] and rule["id"] in result["expected"] and rule["enabled"]}
    result["shared_effects"] = [{"rule_id": rule["id"], "setting": name, "before": setting(rule, name), "after": config,
                                 "requires_separate_scope_approval": True}
                                for rule in rules if rule["isBase"] for name, config in result["expected"].get(rule["id"], {}).items()]
    rule_map = {rule["id"]: rule for rule in rules}
    result["ownership_before_write"] = {
        "rules": {rule["id"]: copy.deepcopy(rule) for rule in rules if rule["id"] in changed},
        "inheritance": {rule["id"]: {name: inheritance_proof(rule, name, rule_map) for name in result["expected"][rule["id"]]}
                        for rule in rules if rule["id"] in changed},
        "must_save_and_read_back_before_first_write": True}
    if value["family"] == "waitlist":
        result["ownership_before_write"]["attribute_namespace"] = {
            "names": copy.deepcopy(current["known_attribute_names"]), "complete": current["attribute_namespace_complete"]}
    if restart_origin is not None:
        result["restart_origin"] = copy.deepcopy(restart_origin)
    return seal(result)


def verify(plan, current, phase="configure"):
    require(phase in {"configure", "activation", "enabled"}, "Unknown verification phase")
    check_plan(plan, current, "configuration-prepared")
    rules = {rule["id"]: rule for rule in current["rules"]}
    for identifier, expected in plan["expected"].items():
        if expected.get("incomingMessages", {}).get("howToReply") == "UsingAI":
            require(identifier in rules, "Campaign rule missing; reconcile before enable")
            require_reply_readiness(rules[identifier])
    if phase != "enabled" and recipe(plan["recipe_id"])["family"] == "waitlist":
        require_membership_available(plan["shared_additions"]["capture_names"][0], current, plan)
    require(set(rules) == set(plan["original_enabled"]), "Rule set changed; reconcile before enable")
    for identifier, digest in plan["preserved_rules"].items():
        require(fingerprint(rules[identifier]) == digest, "Shared/unowned rule side effect")
    for identifier, expected in plan["expected"].items():
        rule = rules[identifier]
        wanted_enabled = plan["original_enabled"][identifier]
        if phase == "enabled" and any(item["variables"]["id"] == identifier for item in plan["enable"]):
            wanted_enabled = True
        require(rule["enabled"] == wanted_enabled, "Unexpected activation before readback")
        if phase == "configure" and identifier in plan["activation_before"]:
            require(fingerprint(rule) == plan["activation_before"][identifier], "Shared rule changed before activation approval")
            continue
        for name, wanted in expected.items():
            require(rule["settings"].get(name, {}).get("inheritsFrom") is None, "Setting still inherits")
            actual = setting(rule, name)
            if name == "collectContactInfo":
                require(all(not entry.get("validationErrors") for entry in actual["captures"]), "Capture validationErrors block success")
                actual["captures"] = [{key: entry[key] for key in ("name", "description")} for entry in actual["captures"]]
            require(actual == wanted, f"Readback differs: {identifier}/{name}")
        for name, digest in plan["preserved_settings"][identifier].items():
            require(fingerprint(rule["settings"].get(name)) == digest, "Unrelated setting changed")
    return {"configuration_verified": True, "verified_phase": phase, "shared_activation_verified": phase in {"activation", "enabled"},
            "live_delivery_verified": False, "enable_verified": phase == "enabled", "enable_requires_separate_native_approval": True,
            "plan_sha256": plan["plan_sha256"]}


def activation_plan(plan, current):
    verified = verify(plan, current, "configure")
    return {"plan_sha256": verified["plan_sha256"], "current_state_sha256": fingerprint(current),
            "requires_separate_native_approval_before_first_shared_write": True,
            "shared_mode": plan["shared_mode"],
            "warning": "Shared writes affect live behavior immediately; read each back." if plan["activation"] else "Shared settings are staged with DM OFF. Separate approved enable is still required.",
            "commands": plan["activation"]}


def enable_plan(plan, current):
    verify(plan, current, "activation")
    return {"plan_sha256": plan["plan_sha256"], "current_state_sha256": fingerprint(current),
            "requires_separate_native_approval": True, "shared_effects": plan["shared_effects"],
            "commands": plan["enable"], "live_delivery_verified": False}


def without_addition(plan, identifier, name, actual):
    additions = plan.get("shared_additions", {})
    config = comparable_setting(name, actual)
    if name == "incomingMessages":
        block = additions.get("prompt_block", "")
        marker = f"[coach-funnel:{plan['campaign_id']}]"
        if marker not in config["messagePrompt"]:
            require(f"[/coach-funnel:{plan['campaign_id']}]" not in config["messagePrompt"], "Ambiguous partial campaign block")
            return config
        require(block and config["messagePrompt"].count(block) == 1 and config["messagePrompt"].count(marker) == 1,
                "Campaign prompt changed or duplicated; ambiguous removal")
        config["messagePrompt"] = config["messagePrompt"].replace("\n\n" + block, "", 1) if "\n\n" + block in config["messagePrompt"] else config["messagePrompt"].replace(block, "", 1)
        require(config["messagePrompt"].strip(), "Removing campaign would leave an empty native prompt")
    elif name in {"switchToHuman", "collectContactInfo"}:
        field = "rules" if name == "switchToHuman" else "captures"
        wanted = ([additions["handoff_rule"]] if name == "switchToHuman" else
                  [entry for entry in plan["expected"][identifier][name][field] if entry["name"] in additions.get("capture_names", [])])
        for entry in wanted:
            matches = [item for item in config[field] if item == entry]
            identity = [item for item in config[field] if (f"For campaign {plan['campaign_id']}," in item["switchingConditions"] if field == "rules" else item["name"] == entry["name"])]
            require(len(matches) <= 1 and len(identity) == len(matches), "Campaign list entry changed or duplicated; ambiguous removal")
            if matches:
                config[field].remove(entry)
    return config


def stop_plan(plan, current):
    check_plan(plan, current, "configuration-prepared", check_recipe=False)
    saved = plan["ownership_before_write"]
    rules = {rule["id"]: rule for rule in current["rules"]}
    result = {key: plan[key] for key in ("recipe_id", "recipe_digest", "campaign_id", "account_id", "bot_id", "environment")}
    result.update({"schema_version": 1, "stage": "stop-prepared", "source_plan_sha256": plan["plan_sha256"],
                   "commands": [], "expected_rules": copy.deepcopy(rules), "deferred_restorations": [],
                   "requires_native_approval": True, "must_save_and_read_back_before_first_write": True,
                   "live_stop_verified": False})
    origin = plan.get("restart_origin", plan)
    result["campaign_root_sha256"] = origin["plan_sha256"]
    if plan["recipe_id"] == "inro-6081":
        name = plan["shared_additions"]["capture_names"][0]
        try:
            require_membership_available(name, current, plan)
            captures = {}
            for identifier, expected in plan["expected"].items():
                wanted = expected.get("collectContactInfo")
                if wanted is None:
                    continue
                require(comparable_setting("collectContactInfo", rules[identifier]["settings"]["collectContactInfo"])
                        == {**comparable_setting("collectContactInfo", wanted), "inheritsFrom": None},
                        "Restart needs exact capture readback before stop")
                captures[identifier] = [copy.deepcopy(entry) for entry in wanted["captures"] if entry["name"] == name]
                require(len(captures[identifier]) == 1, "Ambiguous membership capture")
            require(name in current["known_attribute_names"] and captures, "Read the reserved global attribute before stop")
            result["membership_ownership"] = {"name": name, "captures": captures,
                                              "original_plan_sha256": origin["plan_sha256"]}
        except (ValueError, KeyError, TypeError):
            result["membership_ownership"] = None
    owned = plan.get("owned_rule_id")
    for identifier, before in saved["rules"].items():
        require(identifier in rules, "Campaign rule missing; reconcile deletion before stop")
        actual = rules[identifier]
        require(all(actual[key] == before[key] for key in ("id", "scope", "isBase")), "Ownership scope changed")
        exact = within_owned_values(before, plan["expected"][identifier], actual)
        shared_enable_deferred = False
        if identifier == owned and actual["enabled"]:
            result["commands"].append(command("fuelyAutomationSetEnabled", {"botID": plan["bot_id"], "id": identifier, "enabled": False}, "stop-disable-owned"))
            result["expected_rules"][identifier]["enabled"] = False
        elif before["isBase"] and not before["enabled"] and actual["enabled"]:
            untouched = set(rules) == set(plan["original_enabled"])
            untouched = untouched and all(fingerprint(rules[key]) == digest for key, digest in plan["preserved_rules"].items())
            untouched = untouched and all(within_owned_values(source, plan["expected"][key], rules.get(key)) for key, source in saved["rules"].items())
            if exact and untouched:
                result["commands"].append(command("fuelyAutomationSetEnabled", {"botID": plan["bot_id"], "id": identifier, "enabled": False}, "stop-restore-approved-dm-enable"))
                result["expected_rules"][identifier]["enabled"] = False
            else:
                shared_enable_deferred = True
                result["deferred_restorations"].append({"rule_id": identifier, "setting": "enabled", "reason": "Concurrent shared changes; cannot prove ownership of general DM enable. Preserve ON and remove only campaign additions."})
        for name, wanted in plan["expected"][identifier].items():
            original = comparable_setting(name, before["settings"][name])
            now = actual["settings"].get(name)
            require(now is not None, "Changed setting missing; reconcile before stop")
            now = comparable_setting(name, now)
            if now == original:
                continue
            applied_setting = {**comparable_setting(name, wanted), "inheritsFrom": None}
            proof = saved["inheritance"][identifier][name]
            parent_unchanged = all(key in rules and comparable_rule(rules[key]) == comparable_rule(parent) for key, parent in proof.items())
            if now == applied_setting and not shared_enable_deferred:
                restored = copy.deepcopy(original)
            else:
                require(now.get("inheritsFrom") is None, "Concurrent inheritance change; ambiguous restoration")
                restored = {**without_addition(plan, identifier, name, setting(actual, name)), "inheritsFrom": None}
                result["deferred_restorations"].append({"rule_id": identifier, "setting": name, "reason": "Shared enable restoration deferred; preserve current behavior and remove only campaign additions" if shared_enable_deferred else "Concurrent content preserved instead of original snapshot"})
                if restored == now:
                    continue
            can_inherit = exact and parent_unchanged
            if restored.get("inheritsFrom") is not None and not can_inherit:
                restored["inheritsFrom"] = None
                result["deferred_restorations"].append({"rule_id": identifier, "setting": name, "reason": "Concurrent change prevents exact inheritance restoration"})
            if restored == now:
                continue
            if restored.get("inheritsFrom") is not None:
                operation = command("fuelyAutomationUpdateSetting", {"botID": plan["bot_id"], "id": identifier,
                                    "update": {name: {"setInheritFrom": restored["inheritsFrom"]}}}, "stop-restore-inheritance")
            else:
                operation = update(plan["bot_id"], identifier, name, {key: item for key, item in restored.items() if key != "inheritsFrom"})
                operation["phase"] = "stop-remove-owned-additions"
            operation["readback_after"] = True
            result["commands"].append(operation)
            result["expected_rules"][identifier]["settings"][name] = restored
    result["restoration_complete"] = not result["deferred_restorations"]
    return seal(result)


def verify_stop(plan, current, original=None):
    check_plan(plan, current, "stop-prepared", check_recipe=False)
    rules = {rule["id"]: rule for rule in current["rules"]}
    expected = {key: comparable_rule(rule) for key, rule in plan["expected_rules"].items()}
    if original is None:
        require({key: comparable_rule(rule) for key, rule in rules.items()} == expected,
                "Stop readback differs; stopping/result unknown, not stopped")
    else:
        check_stopped_waitlist(original, plan, current)
    result = {"schema_version": 1, "verification_kind": "normalized-stop-readback",
            "verification_scope": "complete-readback" if original is None else "unchanged-affected-settings",
            "original_plan_sha256": None if original is None else original["plan_sha256"],
            "observed_at": current["observed_at"], "source_plan_sha256": plan["source_plan_sha256"],
            "rules_sha256": fingerprint({key: comparable_rule(rule) for key, rule in rules.items()}),
            "stop_rules_sha256": fingerprint(expected),
            "settings_stopped": True, "restoration_complete": plan["restoration_complete"],
            "deferred_restorations": plan["deferred_restorations"], "live_stop_verified": False,
            "plan_sha256": plan["plan_sha256"]}
    result["verification_sha256"] = fingerprint(result)
    return result


def check_stopped_waitlist(original, stopped, current):
    check_plan(original, current, "configuration-prepared")
    check_plan(stopped, current, "stop-prepared")
    require(original["recipe_id"] == "inro-6081" and "restart_origin" not in original,
            "Restart requires the original waitlist preparation, not a later restart")
    require(all(stopped[key] == original[key] for key in ("recipe_id", "recipe_digest", "campaign_id"))
            and stopped.get("campaign_root_sha256") == original["plan_sha256"], "Stop belongs to another campaign preparation")
    name = original["shared_additions"]["capture_names"][0]
    proof = stopped.get("membership_ownership")
    expected_captures = {identifier: [entry for entry in settings["collectContactInfo"]["captures"] if entry["name"] == name]
                         for identifier, settings in original["expected"].items() if "collectContactInfo" in settings}
    require(proof == {"name": name, "captures": expected_captures, "original_plan_sha256": original["plan_sha256"]},
            "Stop lacks exact original campaign capture ownership proof")
    rules = {rule["id"]: rule for rule in current["rules"]}
    for identifier, settings in original["expected"].items():
        require(identifier in rules and identifier in stopped["expected_rules"], "Restart rule missing")
        actual, expected = rules[identifier], stopped["expected_rules"][identifier]
        require(all(actual[key] == expected[key] for key in ("id", "scope", "isBase", "enabled")), "Stopped rule scope or switch changed")
        require(all(comparable_setting(key, actual["settings"].get(key, {}))
                    == comparable_setting(key, expected["settings"][key]) for key in settings),
                "Affected settings changed after verified stop; reconcile before restart")
    owned = original["owned_rule_id"]
    require(not rules[owned]["enabled"], "Restage only the owned OFF custom")
    require_membership_available(name, current, original, reserved=True)
    require(all(name not in {entry["name"] for entry in setting(rule, "collectContactInfo")["captures"]} for rule in current["rules"]),
            "Stopped membership capture still exists; reconcile instead of duplicating")


def restart_plan(original, stopped, verification, data, current, developer_qa=False):
    check_stopped_waitlist(original, stopped, current)
    require(fingerprint(data) == original["input_sha256"], "Restart cannot change campaign, launch, purpose, membership name or business inputs")
    require(verification.get("verification_sha256") == fingerprint({key: item for key, item in verification.items() if key != "verification_sha256"}),
            "Unverified or changed stop receipt")
    expected_hash = fingerprint({key: comparable_rule(rule) for key, rule in stopped["expected_rules"].items()})
    require(verification.get("schema_version") == 1 and verification.get("verification_kind") == "normalized-stop-readback"
            and verification.get("settings_stopped") is True and verification.get("plan_sha256") == stopped["plan_sha256"]
            and verification.get("source_plan_sha256") == stopped["source_plan_sha256"]
            and verification.get("stop_rules_sha256") == expected_hash
            and ((verification.get("verification_scope") == "complete-readback" and verification.get("rules_sha256") == expected_hash)
                 or (verification.get("verification_scope") == "unchanged-affected-settings"
                     and verification.get("original_plan_sha256") == original["plan_sha256"])),
            "Stop receipt does not verify this stop plan")
    age = (datetime.now(timezone.utc) - timestamp(verification["observed_at"])).total_seconds()
    require(-60 <= age <= 900, "Stale stop verification; obtain fresh native readback before restart")
    require(timestamp(current["observed_at"]) >= timestamp(verification["observed_at"]), "Current state predates stop verification")
    rules = {rule["id"]: rule for rule in current["rules"]}
    owned = original["owned_rule_id"]
    source = copy.deepcopy(current)
    source["ownership"] = {"campaign_id": original["campaign_id"], "recipe_id": original["recipe_id"],
                           "account_id": original["account_id"], "rule_id": owned, "rule_sha256": fingerprint(rules[owned])}
    result = _prepare(recipe(original["recipe_id"]), data, source, developer_qa, restart_origin=original)
    result.pop("plan_sha256")
    result["restart"] = {"original_plan_sha256": original["plan_sha256"], "stop_plan_sha256": stopped["plan_sha256"],
                         "stop_verification_sha256": verification["verification_sha256"],
                         "membership_values_unchanged": True, "fresh_source_and_consent_required": True}
    return seal(result)


def attribute(value, card, events):
    require(card["recipe_id"] == value["id"] and card["recipe_digest"] == recipe_digest(value), "Stale attribution card")
    confirmed, ambiguous = [], []
    for event in events["events"]:
        require(event["account_id"] == card["account_id"] and event["bot_id"] == card["bot_id"], "Wrong account in campaign history")
        if event.get("recipe_id") != value["id"] or event.get("campaign_id") != card["campaign_id"]:
            ambiguous.append(event["id"])
            continue
        recipient = event.get("recipient_id")
        chain = event.get("chain", [])
        valid = bool(recipient and chain) and all(item.get("recipient_id") == recipient for item in chain)
        entry = chain[0] if chain else {}
        if value["entry"] in {"comment", "public"}:
            valid = (valid and entry.get("media_id") in card["post_ids"] and bool(entry.get("comment_id"))
                     and entry.get("text", "").casefold() == card["keyword"].casefold())
            if value["entry"] == "comment":
                valid = valid and bool(entry.get("private_reply_id")) and any(item.get("id") == entry.get("private_reply_id") for item in chain[1:])
        elif value.get("entry_match") == "any_inbound":
            valid = valid and entry.get("direction") == "inbound" and bool(entry.get("text", "").strip())
        else:
            valid = valid and entry.get("direction") == "inbound" and entry.get("text", "").casefold() == card["keyword"].casefold()
        if valid:
            confirmed.append(event["id"])
        else:
            ambiguous.append(event["id"])
    return {"confirmed_event_ids": confirmed, "ambiguous_event_ids": ambiguous,
            "complete": events.get("pagination_complete") is True and not ambiguous,
            "empty_claim_allowed": events.get("pagination_complete") is True and not ambiguous and not confirmed,
            "lead_outcome_verified": False,
            "proof": "Normalized source-chain check only; native provenance and full history remain required."}


def evidence_file(root, reference):
    path = inside(root, reference["path"])
    require(hashlib.sha256(path.read_bytes()).hexdigest() == reference["sha256"], "Changed evidence receipt")
    return load(path)


def receipt(root, reference, bindings, check):
    record = evidence_file(root, reference)
    require(record.get("schema_version") == 1 and record.get("fixture") is False, "Fixtures cannot be runtime evidence")
    require(record.get("bindings") == {**bindings, "check": check}, "Evidence source/recipient/run mixing")
    require(record.get("passed") is True and record.get("observation", "").strip(), "Missing/failed observation")
    require(record.get("origin") in {"native-readback", "recipient-observation", "human-review"}, "Unknown receipt origin")
    timestamp(record["observed_at"])
    return record


def business_checks(value, parameters):
    checks = dict(value["business_outcomes"])
    if value["id"] == "inro-6220":
        checks["recipient_access"] = {"origin": "recipient-observation", "min_native_refs": 1, "parameter": "resource_url"}
    if value["family"] == "qualification":
        checks.update(value["outcome_variants"][parameters["next_step"]])
    for parameter, conditional in value.get("conditional_business_outcomes", {}).items():
        if parameter in parameters:
            checks.update(conditional)
    return checks


def verify_business_receipt(record, check, specification, parameters, recipient):
    require(record["origin"] == specification["origin"], f"Business outcome needs {specification['origin']}: {check}")
    references = record.get("native_refs", [])
    require(isinstance(references, list) and len(set(references)) >= specification["min_native_refs"] and all(isinstance(item, str) and item.strip() for item in references), f"Missing native business references: {check}")
    if "parameter" in specification:
        require(record.get("destination") == parameters[specification["parameter"]], f"Business destination differs: {check}")
    if check == "two_actual_answers":
        answers = record.get("answers", [])
        require(len(answers) == 2 and {answer.get("question") for answer in answers} == {parameters["question_one"], parameters["question_two"]}, "Evidence must contain the two approved questions and actual answers")
        require(len({answer.get("event_id") for answer in answers}) == 2 and all(answer.get("event_id") in references and answer.get("recipient_id") == recipient and isinstance(answer.get("answer"), str) and answer["answer"].strip() for answer in answers), "Actual answer events/recipient are missing or mixed")
    if check in {"launch_membership_readback", "launch_withdrawal_confirmed"}:
        state = "joined" if check == "launch_membership_readback" else "withdrawn"
        require(record.get("attribute_name") == parameters["membership_attribute"] and record.get("attribute_value") == state
                and record.get("launch_name") == parameters["launch_name"], "Actual launch-specific attribute readback required, not bot prose")


def evidence_check(value, root, env):
    errors = []
    metadata = None
    try:
        require(value["status"] not in {"unverified", "unavailable"} and not value["blockers"], "Recipe has unresolved mechanism blockers")
        require(root is not None, "No runtime evidence directory")
        root = Path(root).resolve()
        record = load(inside(root, f"{value['id']}.json"))
        require(record.get("schema_version") == 1 and record.get("fixture") is False, "Fixture or invalid evidence manifest")
        require(record["recipe_id"] == value["id"] and record["recipe_digest"] == recipe_digest(value), "Changed recipe invalidates evidence")
        require(environment(record["environment"]) == environment(env), "Environment/contract/model changed")
        runs = record["runs"]
        require(len(runs) >= 3 and len({run["id"] for run in runs}) == len(runs), "Three independent runs required")
        require(len({run["input_sha256"] for run in runs}) == len(runs), "Runs must use distinct business inputs")
        live = [run for run in runs if run["mode"] == "live"]
        require(len({run["account_id"] for run in live}) >= 2, "Two live compatible accounts required")
        require(any(run.get("author_account") is False for run in live), "An independent non-author account is required")
        live_variants = set()
        material_live = False
        for run in runs:
            require(run["mode"] in {"live", "preview"} and run.get("compatible") is True, "Unproved account compatibility")
            require(run["platform"] in value["platforms"], "Unaccepted platform branch")
            require(bool(re.fullmatch(r"[0-9a-f]{64}", run["input_sha256"])), "Invalid business input fingerprint")
            require(all(isinstance(run.get(key), str) and run[key].strip() for key in ("account_id", "bot_id", "recipient_id")), "Unbound live identities")
            source = run["source"]
            require(source.get("kind") == value["entry"] and source.get("entry_event_id"), "Missing native entry provenance")
            if value["entry"] in {"comment", "public"}:
                require(source.get("post_id"), "Missing comment media provenance")
            business = evidence_file(root, run["inputs"])
            parameters = inputs_for(value, business)
            require(fingerprint(business) == run["input_sha256"], "Business/source evidence mixing")
            if value.get("entry_match") == "any_inbound":
                require(source.get("ordinary_inbound") is True, "Ordinary support evidence must not require a keyword")
            else:
                require(source.get("keyword") == parameters["keyword"], "Business/source evidence mixing")
            if value["entry"] in {"comment", "public"}:
                require(source["post_id"] in parameters["post_ids"], "Evidence post/account mixing")
            prepared = evidence_file(root, run["prepared_plan"])
            require(prepared.get("stage") == "configuration-prepared" and prepared.get("recipe_digest") == record["recipe_digest"] and prepared.get("input_sha256") == run["input_sha256"], "Evidence must bind a prepared recipe configuration")
            require(prepared.get("account_id") == run["account_id"] and prepared.get("bot_id") == run["bot_id"] and prepared.get("environment") == env, "Prepared plan belongs to another account/environment")
            require(prepared.get("plan_sha256") == fingerprint({key: item for key, item in prepared.items() if key != "plan_sha256"}), "Changed prepared evidence plan")
            bindings = {"recipe_id": value["id"], "recipe_digest": record["recipe_digest"], "run_id": run["id"],
                        "account_id": run["account_id"], "bot_id": run["bot_id"], "recipient_id": run["recipient_id"],
                        "input_sha256": run["input_sha256"], "mode": run["mode"], "platform": run["platform"], "source": source}
            required = set(value["runtime_checks"]) if run["mode"] == "live" else {"content", "return", "stop"}
            outcomes = business_checks(value, parameters) if run["mode"] == "live" else {}
            required.update(outcomes)
            require(required <= set(run["checks"]), "Missing applicable live/return/stop/content checks")
            for check, reference in run["checks"].items():
                observed = receipt(root, reference, bindings, check)
                if check in outcomes:
                    verify_business_receipt(observed, check, outcomes[check], parameters, run["recipient_id"])
            if run["mode"] == "live":
                live_variants.add(parameters["next_step"] if value["family"] == "qualification" else "default")
                material_live = material_live or ("resource_url" in parameters and (
                    value["id"] == "inro-6025" or value["id"] == "inro-6220"
                    and {"promised_link_received", "recipient_access"} <= set(outcomes)))
        accepted = record["acceptance"]
        require(accepted.get("status") == "accepted" and accepted.get("independent_reviewer"), "Independent acceptance required")
        require(accepted.get("runs_sha256") == fingerprint(runs), "Acceptance does not bind current runs")
        users = accepted["target_users"]
        require(len(users) >= 3 and len({user["id"] for user in users}) == len(users), "Three distinct target-user trials required")
        require(all(user.get("unassisted") is True and type(user.get("business_clarifications")) is int and 0 <= user["business_clarifications"] <= 1 for user in users), "Target-user path requires hidden assistance")
        require(accepted.get("fresh_install_and_private_recovery") is True, "New-account private recovery not accepted")
        require(isinstance(accepted.get("variants"), list) and bool(accepted["variants"]) and set(accepted["variants"]) <= live_variants, "Every accepted outcome variant needs live business evidence")
        require(not accepted.get("material_delivery") or material_live, "Material delivery needs live recipient evidence")
        acceptance_bindings = {"recipe_id": value["id"], "recipe_digest": record["recipe_digest"], "runs_sha256": accepted["runs_sha256"],
                               "variants": accepted["variants"], "material_delivery": accepted.get("material_delivery", False)}
        accepted_receipt = receipt(root, accepted["receipt"], acceptance_bindings, "independent_acceptance")
        metadata = accepted_entry(value, {"id": value["id"], "version": value["version"], "digest": recipe_digest(value), "environment": env,
            "acceptance": {"status": "runtime-accepted", "accepted_at": accepted_receipt["observed_at"], "variants": accepted["variants"], "material_delivery": accepted.get("material_delivery", False)}})
    except (ValueError, KeyError, TypeError, OSError) as error:
        errors.append(str(error))
    return {"eligible": not errors, "recipe_id": value["id"], "recipe_digest": recipe_digest(value), "errors": errors, "catalog_metadata": metadata if not errors else None,
            "limit": "Integrity and acceptance-record checks only. Humans verify receipt authenticity; this helper cannot witness a live account."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate", help="Check all 30 designs and local references; not runtime acceptance")
    candidates = commands.add_parser("candidates", help="Internal candidate index, not a customer catalogue")
    candidates.add_argument("--developer-qa", action="store_true", required=True)
    catalog = commands.add_parser("catalog", help="Discover sanitized accepted metadata; optional runtime environment filter, no private QA receipts")
    catalog.add_argument("--environment", type=Path)
    contract = commands.add_parser("contract-pin", help="Fingerprint ten exact public schema reads; no network or provider-version claim")
    contract.add_argument("--bundle", type=Path, required=True)
    contract.add_argument("--complete", action="store_true", required=True, help="Attest all ten tool responses are complete, including pagination metadata")
    qr = commands.add_parser("qr", help="Create a profile QR PNG using qrcode; no scan trigger or native execution")
    qr.add_argument("--profile-url", required=True)
    qr.add_argument("--username", required=True, help="Actual username read from the connected Instagram account")
    qr.add_argument("--output", type=Path, required=True)
    for name in ("select", "prepare", "release-check"):
        sub = commands.add_parser(name)
        sub.add_argument("recipe_id")
        if name == "release-check":
            sub.add_argument("--evidence", type=Path)
        sub.add_argument("--environment", type=Path)
        if name != "release-check":
            sub.add_argument("--developer-qa", action="store_true")
        if name == "select":
            sub.add_argument("--requirements", type=Path)
        if name == "prepare":
            sub.add_argument("--inputs", type=Path, required=True)
            sub.add_argument("--state", type=Path, required=True)
    check = commands.add_parser("verify", help="Check fresh normalized readback against the exact prepared plan")
    check.add_argument("--plan", type=Path, required=True)
    check.add_argument("--state", type=Path, required=True)
    check.add_argument("--phase", choices=["configure", "activation", "enabled"], default="configure")
    activation = commands.add_parser("activation-plan", help="Check OFF configuration and unchanged shared state before separately approved live shared writes")
    activation.add_argument("--plan", type=Path, required=True)
    activation.add_argument("--state", type=Path, required=True)
    for name in ("enable-plan", "stop-plan", "verify-stop"):
        sub = commands.add_parser(name)
        sub.add_argument("--plan", type=Path, required=True)
        sub.add_argument("--state", type=Path, required=True)
        if name == "verify-stop":
            sub.add_argument("--original-plan", type=Path, help="Refresh same-waitlist verification after unrelated changes using saved original ownership")
    restart = commands.add_parser("restart-plan", help="Restage the same stopped waitlist without changing membership values")
    restart.add_argument("--original-plan", type=Path, required=True)
    restart.add_argument("--stop-plan", type=Path, required=True)
    restart.add_argument("--stop-verification", type=Path, required=True)
    restart.add_argument("--inputs", type=Path, required=True)
    restart.add_argument("--state", type=Path, required=True)
    restart.add_argument("--developer-qa", action="store_true")
    attribution = commands.add_parser("attribute", help="Check normalized campaign source chains, never all qualified chats")
    attribution.add_argument("recipe_id")
    attribution.add_argument("--card", type=Path, required=True)
    attribution.add_argument("--events", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate()
        elif args.command == "candidates":
            result = {"mode": "developer-qa-only", "sources": load(REFERENCES / "research.json")["sources"]}
        elif args.command == "catalog":
            result = {"recipes": catalog_entries(load(args.environment) if args.environment else None)}
        elif args.command == "contract-pin":
            result = contract_pin(load(args.bundle), args.complete)
        elif args.command == "qr":
            result = create_qr(args.profile_url, args.username, args.output)
        elif args.command == "select":
            result = selection(recipe(args.recipe_id), load(args.requirements) if args.requirements else [], args.developer_qa, load(args.environment) if args.environment else None)
        elif args.command == "prepare":
            result = prepare(recipe(args.recipe_id), load(args.inputs), load(args.state), args.developer_qa)
        elif args.command == "verify":
            result = verify(load(args.plan), load(args.state), args.phase)
        elif args.command == "activation-plan":
            result = activation_plan(load(args.plan), load(args.state))
        elif args.command == "enable-plan":
            result = enable_plan(load(args.plan), load(args.state))
        elif args.command == "stop-plan":
            result = stop_plan(load(args.plan), load(args.state))
        elif args.command == "verify-stop":
            result = verify_stop(load(args.plan), load(args.state), load(args.original_plan) if args.original_plan else None)
        elif args.command == "restart-plan":
            result = restart_plan(load(args.original_plan), load(args.stop_plan), load(args.stop_verification), load(args.inputs), load(args.state), args.developer_qa)
        elif args.command == "attribute":
            result = attribute(recipe(args.recipe_id), load(args.card), load(args.events))
        else:
            result = evidence_check(recipe(args.recipe_id), args.evidence, load(args.environment) if args.environment else None)
        print(json.dumps(result, indent=2, ensure_ascii=True))
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"funnels: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
