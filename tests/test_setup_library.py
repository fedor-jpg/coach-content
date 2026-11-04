import copy
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin/scripts"))
import coach
import funnel_library
import scenario_library
import setup_library as setup

REFS = funnel_library.REFERENCES


class SetupLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = funnel_library.outputs()
        cls.packets = {Path(name).stem: json.loads(text) for name, text in cls.outputs.items() if name.startswith("setup-details/") and name.endswith(".json")}
        cls.observation = json.loads((REFS / "capability-observation.json").read_text())
        cls.data = json.loads((REFS / "scenarios.json").read_text())

    def test_all_57_variants_and_60_sources_are_accounted_once(self):
        self.assertEqual(len(self.packets), 57)
        sources = [source for packet in self.packets.values() for source in packet["sources"]]
        self.assertEqual(len(sources), 60)
        self.assertEqual(len({s["source_id"] for s in sources}), 60)
        self.assertEqual(sum(len(s["nodes"]) for s in sources), 517)
        self.assertEqual(sum(len(s["transitions"]) for s in sources), 475)
        self.assertEqual(Counter(bool(p["plans"]) for p in self.packets.values()), {True: 30, False: 27})
        self.assertEqual(Counter(p["preparation_status"] for p in self.packets.values()), {"adaptation_draft_requires_consent": 30, "waiting_for_chatfuel": 25, "source_incomplete_reference_only": 2})
        self.assertTrue(all(not p["runtime_accepted"] for p in self.packets.values()))
        self.assertEqual(json.loads((REFS / "catalog.json").read_text())["recipes"], [])

    def test_all_authored_steps_are_reachable_without_turning_global_rules_into_branches(self):
        for packet in self.packets.values():
            for plan in packet["plans"]:
                graph = plan["intended_branches"]
                if not graph:
                    continue
                reached = {graph["steps"][0]["id"]}
                for _ in graph["steps"]:
                    reached |= {edge["to"] for edge in graph["transitions"] if edge["from"] in reached}
                self.assertEqual(reached, {step["id"] for step in graph["steps"]}, packet["variant"]["id"])
        plan = self.packets["channel-transfer-manychat-101"]["plans"][0]
        self.assertEqual([step["id"] for step in plan["intended_branches"]["steps"]], ["entry", "first"])
        prompt = next(op["settings"]["incomingMessages"]["messagePrompt"] for op in plan["operations"] if "incomingMessages" in op["settings"])
        self.assertIn("Handle refusal before keyword matching", prompt)
        self.assertIn("Do not send after silence", prompt)
        binding = copy.deepcopy(plan["selection"])
        binding["draft"]["branches"]["steps"].append({"id": "orphan", "message_ids": []})
        with self.assertRaisesRegex(ValueError, "unreachable draft steps"):
            setup.draft_plan(None, binding["draft"], self.observation, binding)

    def test_exact_nodes_edges_known_fields_and_all_raw_settings_values(self):
        for packet in self.packets.values():
            for audit in packet["sources"]:
                with self.subTest(source=audit["source_id"]):
                    original = json.loads((REFS / audit["source_file"]).read_text())
                    self.assertEqual(audit["transitions"], original["graph"]["transitions"])
                    self.assertEqual(audit["setup_screens"], original["setup"])
                    self.assertEqual(audit["global_fields"], setup.field_values(original["source"]["document"]))
                    self.assertEqual(len(audit["nodes"]), len(original["graph"]["steps"]))
                    for node, step in zip(audit["nodes"], original["graph"]["steps"]):
                        self.assertEqual((node["id"], node["content"]), (step["id"], step["content"]))
                        self.assertEqual(node["known_fields"], setup.field_values(step["settings"]))
                        linked = original
                        for part in node["settings_pointer"].strip("/").split("/"):
                            linked = linked[int(part)] if isinstance(linked, list) else linked[part]
                        self.assertEqual(list(setup.leaves(linked)), list(setup.leaves(step["settings"])))
                        self.assertEqual(node["settings_sha256"], setup.sha(linked))
                        self.assertTrue(node["reason"] and node["business_inputs"])

    def test_help_waits_for_actual_details_then_answers_without_an_unsolicited_loop(self):
        count = 0
        for packet in self.packets.values():
            for plan in packet["plans"]:
                graph = plan["intended_branches"]
                if not graph or not any(step["id"] == "help" for step in graph["steps"]):
                    continue
                count += 1
                self.assertEqual([edge for edge in graph["transitions"] if edge["from"] == "help"], [{"from": "help", "to": "answer", "condition": "Actual question or problem details in a new reply"}])
                self.assertTrue(any(edge["to"] == "answer" and edge["condition"] == "Actual concrete question" for edge in graph["transitions"]))
                self.assertFalse(any(edge["from"] == "answer" and edge["to"] == "help" for edge in graph["transitions"]))
                answer = next(step for step in graph["steps"] if step["id"] == "answer")
                self.assertIn("approved facts", answer["action"])
                self.assertIn("Do not repeat the help invitation or claim an unconfigured transfer", answer["action"])
                self.assertIn("For a concrete question answer only approved knowledge", plan["instruction"])
        self.assertEqual(count, 11)

    def test_every_plan_binds_reviewed_entry_outputs_and_mandatory_conditions(self):
        for packet in self.packets.values():
            variant = packet["variant"]
            for plan in packet["plans"]:
                with self.subTest(variant=variant["id"], entry=plan["target"]):
                    binding = plan["selection"]
                    self.assertEqual(binding["source_requirements"], variant["mandatory_conditions"])
                    self.assertTrue(binding["approval_required"] and binding["entry_change"])
                    payload = setup.stable([plan["operations"], plan["list_additions"]])
                    for name in binding["output_bindings"]:
                        self.assertIn("{" + name + "}", payload)
                    self.assertEqual(plan["write_permission"], "none")
                    for operation in plan["operations"]:
                        setup.validate_operation(operation, self.observation, plan["target"])
                    names = {i["name"] for i in plan["business_inputs"]}
                    self.assertLessEqual(set(re.findall(r"\{([a-z_]+)\}", payload)), names)
                    if plan["target"] == "dm_base":
                        self.assertFalse(any(set(op["settings"]) & {"publicReply", "privateReply"} for op in plan["operations"]))

    def test_111_has_three_offers_six_urls_and_help_in_dm_payload(self):
        packet = self.packets["courses-manychat-111"]
        self.assertEqual(len(packet["plans"]), 1)
        plan = packet["plans"][0]
        self.assertEqual(plan["target"], "dm_base")
        prompt = plan["operations"][0]["settings"]["incomingMessages"]["messagePrompt"]
        for number in ("one", "two", "three"):
            for field in ("title", "terms", "card_url", "purchase_url"):
                self.assertIn("{course_" + number + "_" + field + "}", prompt)
        self.assertIn("If you have any questions, I'm here to help 💛", prompt)
        self.assertNotIn("{course_name}", prompt)
        text = self.outputs["setup-details/courses-manychat-111.md"]
        for title in ("Marketing Master Plan", "Ideal Client Roadmap", "Create a Freebie Your Followers Love!"):
            self.assertIn(title, text)
        self.assertIn("purchase", text.lower())

    def test_dual_entries_are_separate_selectable_plans_not_both_enabled(self):
        for identifier in ("content-inro-6045", "content-inro-6046", "courses-inro-6080"):
            plans = self.packets[identifier]["plans"]
            self.assertEqual({p["target"] for p in plans}, {"dm_base", "owned_comment"})
            self.assertTrue(all(p["selection"]["approval_required"] for p in plans))
        for identifier in ("community-inro-6051", "webinar-inro-6049"):
            self.assertFalse(self.packets[identifier]["plans"])
        for packet in self.packets.values():
            if "direct message" in packet["variant"]["entry"].lower() and "comment" not in packet["variant"]["entry"].lower():
                self.assertTrue(all(p["target"] == "dm_base" for p in packet["plans"]))

    def test_coupon_and_help_outputs_are_not_nearest_analogue_aliases(self):
        for identifier in ("offers-manychat-72",):
            plan = self.packets[identifier]["plans"][0]
            payload = setup.stable(plan["operations"])
            self.assertIn("{coupon_code}", payload)
            self.assertIn("{store_url}", payload)
            self.assertNotIn("{resource_url}", payload)
        payload = setup.stable(self.packets["content-manychat-112"]["plans"][0]["operations"])
        self.assertIn("HELP", payload)
        self.assertIn("Did you have any trouble subscribing?", payload)
        for identifier in ("offers-manychat-63", "offers-manychat-73"):
            self.assertFalse(self.packets[identifier]["plans"])

    def test_contact_gates_and_alternative_branches_are_explicit(self):
        self.assertIn("Optional", self.packets["contact-material-inro-6022"]["plans"][0]["contact_requirement"])
        self.assertIn("required before delivery", self.packets["contact-material-inro-6026"]["plans"][0]["contact_requirement"])
        self.assertIn("Allow SKIP", str(self.packets["contact-material-inro-6022"]["variant"]["mandatory_conditions"]))
        self.assertIn("valid email before delivery", str(self.packets["contact-material-inro-6026"]["variant"]["mandatory_conditions"]))
        self.assertIn("required before delivery", self.packets["contact-material-manychat-20"]["plans"][0]["contact_requirement"])
        self.assertFalse(self.packets["offers-inro-4484"]["plans"])
        self.assertIn("live", self.packets["offers-inro-4484"]["function_review"]["blocking_dependencies"])
        follower = self.packets["follower-material-manychat-107"]
        self.assertIn("follower", follower["mandatory_dependencies"])
        self.assertIn("false", str(follower["variant"]["mandatory_conditions"]))
        self.assertTrue(any("follower" in node["unsupported"] for node in follower["sources"][0]["nodes"]))
        whatsapp = self.outputs["setup-details/channel-transfer-manychat-101.md"]
        self.assertIn("contactedbywhatsapp", whatsapp)
        self.assertIn("{whatsapp_url}", setup.stable(self.packets["channel-transfer-manychat-101"]["plans"][0]["operations"]))
        self.assertIn("without hiding", self.packets["moderation-inro-6111"]["variant"]["assessment"]["replacement"]["result"])

    def test_business_facts_are_separate_from_assistant_copy_and_identifiers(self):
        for packet in self.packets.values():
            for plan in packet["plans"]:
                for item in plan["business_inputs"]:
                    if item["name"] in {"campaign", "language", "keyword"} or item["name"].endswith(("_text", "_prompt")):
                        self.assertEqual(item["provided_by"], "drafted_by_assistant_for_approval")
                self.assertFalse(any(i["type"] == "ids" for i in plan["business_inputs"]))

    def test_all_operations_rehearse_with_local_values_without_tool_calls(self):
        for packet in self.packets.values():
            for plan in packet["plans"]:
                for operation in plan["operations"]:
                    candidate = copy.deepcopy(operation)
                    name, values = next(iter(candidate["settings"].items()))
                    for key, value in list(values.items()):
                        if value == "$resolved.safe_captures":
                            values[key] = [{"attribute": "fixture_owned", "description": "Only new consented data for this fixture."}]
                        elif value == "$resolved.safe_handoff_rules":
                            values[key] = [{"switchingConditions": "Fixture person request", "messagePrompt": "The team can help."}]
                        elif isinstance(value, str):
                            values[key] = re.sub(r"\{[a-z_]+\}", "approved fixture value", value)
                    setup.validate_operation(candidate, self.observation, plan["target"], resolved=True)

    def test_invalid_or_unresolved_settings_fail_closed(self):
        invalid = [
            ("dm_base", {"incomingMessages": {"howToReply": "DontReply"}}),
            ("owned_comment", {"privateReply": {"privateReplyHowToReply": "ExactText", "exactText": "wrong field"}}),
            ("owned_comment", {"privateReply": {"privateReplyHowToReply": "ExactText"}}),
            ("owned_comment", {"publicReply": {"publicReplyHowToReply": "ExactText", "exactTextReply": "x" * 1001}}),
            ("dm_base", {"collectContactInfo": {"howToCollect": "CollectInfo", "captures": [{"name": "wrong", "description": "purpose"}]}}),
            ("dm_base", {"followUps": {"howToSend": "invented"}}),
        ]
        for scope, settings in invalid:
            with self.assertRaises(ValueError):
                setup.validate_operation({"tool": "update_automation_setting", "settings": settings}, self.observation, scope)
        with self.assertRaisesRegex(ValueError, "unresolved"):
            setup.validate_operation({"tool": "update_automation_setting", "settings": {"collectContactInfo": {"howToCollect": "CollectInfo", "captures": "$resolved.safe_captures"}}}, self.observation, "dm_base", resolved=True)

    def test_binding_expiry_capability_change_and_stale_generation(self):
        packet = next(iter(self.packets.values()))
        setup.verify_binding(packet, REFS, as_of=date(2026, 11, 2))
        with self.assertRaisesRegex(ValueError, "expired"):
            setup.verify_binding(packet, REFS, as_of=date(2026, 11, 10))
        with tempfile.TemporaryDirectory() as directory:
            refs = Path(directory) / "references"
            shutil.copytree(REFS, refs)
            (refs / "capability-observation.json").write_text((refs / "capability-observation.json").read_text() + " ")
            with self.assertRaisesRegex(ValueError, "stale binding"):
                setup.verify_binding(packet, refs, as_of=date(2026, 11, 2))
            shutil.copy2(REFS / "capability-observation.json", refs / "capability-observation.json")
            file = refs / "setup-details/courses-manychat-111.md"
            file.write_text(file.read_text() + "stale")
            with self.assertRaisesRegex(ValueError, "stale generated reference"):
                funnel_library.generate(refs, check=True)

    def test_refusal_repeat_edit_return_stop_and_external_boundaries(self):
        policy = (REFS / "setup-policy.md").read_text()
        for text in ("always enables", "no create-OFF", "one update_automation_setting", "Refusal", "repeated same-run", "An edit", "Return requires", "repeat-safe", "dormant Send", "last20", "external", "optional later outcomes", "not permission to replace the existing prompt", "complete merged value", "hold the write"):
            self.assertIn(text, policy)
        for packet in self.packets.values():
            for plan in packet["plans"]:
                self.assertEqual(plan["stop"]["tool"], "set_automation_enabled")
                self.assertFalse(plan["stop"]["enabled"])
                incoming = next(op["settings"]["incomingMessages"] for op in plan["operations"] if "incomingMessages" in op["settings"])
                if incoming["howToReply"] == "UsingAI":
                    self.assertIn("refusal before keyword", incoming["messagePrompt"])
                    self.assertIn("Same-run repeats", incoming["messagePrompt"])
                else:
                    self.assertEqual(plan["target"], "owned_comment")
            prompts = scenario_library.continuation_prompts(self.data)
            for source, continuation in packet["continuations"].items():
                self.assertEqual(continuation, prompts.get(source, []))

    def test_package_contains_portable_setup_and_source_provenance(self):
        paths = set(coach.RELEASE_FILES)
        for packet in self.packets.values():
            identifier = packet["variant"]["id"]
            self.assertIn(f"internal/funnels/setup-details/{identifier}.md", paths)
            for source in packet["sources"]:
                self.assertIn("internal/funnels/" + source["source_file"], paths)
        self.assertIn("internal/funnels/setup-policy.md", paths)

    def test_package_rejects_stale_selected_setup_before_copying(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "relocated"
            coach.source_snapshot(source)
            detail = source / "internal/funnels/setup-details/courses-manychat-111.md"
            detail.write_text(detail.read_text() + "\nStale course entry.\n")
            destination = Path(directory) / "rejected"
            result = subprocess.run([sys.executable, str(source / "plugin/scripts/coach.py"), "release", str(destination)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing/stale generated reference: setup-details/courses-manychat-111.md", result.stderr)
            self.assertFalse(destination.exists())

    def test_dm_drafts_preserve_base_schedule_and_followups_by_default(self):
        plans = [plan for packet in self.packets.values() for plan in packet["plans"] if plan["target"] == "dm_base"]
        self.assertEqual(len(plans), 14)
        baseline = {"whenAIReplies": {"option": "OutsideOfWorkingHours"}, "followUps": {"howToSend": "Send", "messagePrompt": "Existing approved follow-up."}}
        for plan in plans:
            self.assertEqual(plan["preserve_settings"], ["whenAIReplies", "followUps"])
            prepared = copy.deepcopy(baseline)
            for operation in plan["operations"]:
                self.assertFalse(set(operation["settings"]) & set(baseline))
                prepared.update(operation["settings"])
            for name in baseline:
                self.assertEqual(prepared[name], baseline[name])
            self.assertIn("separate approval", " ".join(plan["preparation_gates"]))
            self.assertIn("hold affected configuration", " ".join(plan["preparation_gates"]))
        for packet in self.packets.values():
            for plan in packet["plans"]:
                if plan["target"] == "owned_comment":
                    self.assertTrue(any(op["settings"].get("followUps", {}).get("howToSend") == "DontSend" for op in plan["operations"]))

    def test_owned_off_scope_must_match_posts_keywords_and_mode_before_staging(self):
        approved = {"post_ids": ["post-one", "post-two"], "keywords": ["GUIDE"], "match_mode": "exact"}
        readback = {**copy.deepcopy(approved), "enabled": False, "readback_complete": True}
        self.assertTrue(setup.validate_comment_staging(approved, readback))
        reordered = {**readback, "post_ids": ["post-two", "post-one"]}
        self.assertTrue(setup.validate_comment_staging(approved, reordered))
        for name, wrong in (("post_ids", ["other-post"]), ("keywords", ["OTHER"]), ("match_mode", "contains")):
            with self.subTest(field=name), self.assertRaisesRegex(ValueError, "scope mismatch: " + name):
                setup.validate_comment_staging(approved, {**readback, name: wrong})
        for wrong in ({**readback, "enabled": True}, {**readback, "readback_complete": False}):
            with self.assertRaisesRegex(ValueError, "complete OFF readback"):
                setup.validate_comment_staging(approved, wrong)
        for packet in self.packets.values():
            for plan in packet["plans"]:
                if plan["target"] == "owned_comment":
                    self.assertEqual(plan["entry_readback_fields"], list(approved))
                    self.assertIn("mismatch blocks staging", " ".join(plan["preparation_gates"]))
        policy = (REFS / "setup-policy.md").read_text()
        self.assertIn("Reply-setting updates cannot alter filters", policy)
        self.assertIn("separate immediate-enabled setup_comment_replies approval", policy)

    def test_capture_configuration_never_proves_saved_contact_values(self):
        boundary = self.observation["normal_tool_contract"]["readback_boundaries"]["contact_attribute_values"]
        self.assertFalse(boundary["available"])
        packet = self.packets["community-inro-6081"]
        self.assertEqual(packet["preparation_status"], "adaptation_draft_requires_consent")
        plan = packet["plans"][0]
        self.assertEqual(plan["missing_readback"], ["contact_attribute_values"])
        self.assertIn("Never say joined, on the list, saved or withdrawn as a completed outcome", plan["instruction"])
        self.assertNotIn("switchToHuman", plan["list_additions"])
        self.assertIn("BLOCKED pending actual persistence proof", plan["contact_requirement"])
        for value in plan["messages"].values():
            self.assertNotRegex(value, r"(?i)saved|persistence|unverified|you're on the list")
        for item in self.packets.values():
            for draft in item["plans"]:
                if "collectContactInfo" in draft["list_additions"]:
                    self.assertIn(boundary["claim"], draft["preparation_gates"])
                    self.assertEqual(draft["missing_readback"], ["contact_attribute_values"])
        for word in ("joined", "withdrawn", "membership_attribute"):
            self.assertIn(word, self.outputs["setup-details/community-inro-6081.md"])

    def test_shared_settings_approval_requires_separate_exact_diff(self):
        policy = (REFS / "setup-policy.md").read_text()
        rule = next(line for line in policy.splitlines() if line.startswith("- Never bundle copy approval"))
        for instruction in (
            "Never bundle copy approval with shared-base settings approval",
            "If current readback or an exact proposed settings diff is missing, hold configuration",
            "Ask only the specific unresolved business choice",
            'Do not ask blanket approval for "shared DM base changes"',
            "independent of copy approval",
            "current old value from readback, proposed new value, affected scope, inheritance change and effects",
            "Unknown old values cannot be invented",
            "Copy approval never authorizes settings changes, activation or sends",
        ):
            self.assertIn(instruction, rule)

    def test_function_decisions_gate_all_machine_plans_and_historical_fallback(self):
        waiting_sources = {"inro-6028", "manychat-107", "inro-6024", "manychat-17", "manychat-73", "inro-6051", "inro-6018", "inro-4530", "manychat-57", "manychat-105", "manychat-108", "inro-6111", "inro-6086", "manychat-434", "inro-6023", "manychat-13", "manychat-66", "manychat-69", "manychat-60", "inro-4393", "inro-4484", "manychat-63", "inro-6019", "inro-6222", "inro-6049"}
        reference_sources = {"manychat-3", "inro-comment-moderation"}
        for packet in self.packets.values():
            variant, review = packet["variant"], packet["function_review"]
            source = variant["source_ids"][0]
            expected = "waiting_for_chatfuel" if source in waiting_sources else "source_incomplete_reference_only" if source in reference_sources else "adaptation_draft_requires_consent"
            self.assertEqual(review["status"], expected, source)
            self.assertEqual(review, variant["setup"]["function_review"])
            if expected != "adaptation_draft_requires_consent":
                self.assertEqual(packet["plans"], [])
                self.assertEqual(variant["setup"]["bindings"], [])
                prepared = self.outputs[f"setup-details/{variant['id']}.md"].split("## Complete Captured Topology")[0]
                self.assertIn("SETUP DISABLED", prepared)
                self.assertNotIn("#### Exact Setting Drafts", prepared)
                bad = copy.deepcopy(variant)
                bad["setup"]["bindings"] = [{"draft": "historical fallback"}]
                with self.assertRaisesRegex(ValueError, "blocked variant"):
                    setup.function_review(bad, self.observation)
        for source in ("giveaway-manychat-105", "games-manychat-108", "reminder-manychat-434"):
            self.assertTrue(self.packets[source]["variant"]["assessment"]["missing_source_behavior"])
        self.assertIn("do not generate configuration payloads", (REFS / "setup-policy.md").read_text())

    def test_source_scenario_facts_are_unchanged_from_approved_baseline(self):
        facts = [{key: variant[key] for key in ("id", "source_ids", "entry", "outcome", "mandatory_conditions", "timing")} for family in self.data["families"] for variant in family["variants"]]
        self.assertEqual(setup.sha(facts), "f29b20061168431ad689f400fa9e7fe7351b273b4d6da965f45f823173cdd32b")

    def test_required_contacts_gate_delivery_and_81_captures_both_fields(self):
        for identifier, fields in (("contact-material-inro-6026", ["email"]), ("contact-material-inro-6027", ["phone"]), ("contact-material-manychat-20", ["email"]), ("webinar-manychat-81", ["email", "phone"])):
            plan = self.packets[identifier]["plans"][0]
            captures = plan["list_additions"]["collectContactInfo"]
            self.assertEqual([item["attribute"] for item in captures], ["$resolved.verified_" + field + "_attribute" for field in fields])
            self.assertTrue(all("{contact_purpose}" in item["description"] for item in captures))
            self.assertIn("never overwrite", plan["instruction"])
            self.assertIn("NOT deterministic validation", plan["instruction"])
            self.assertIn("Do not release the link on SKIP, refusal, partial answers or malformed contact", plan["instruction"])
            self.assertNotRegex(plan["messages"]["initial"], r"\{(?:resource|ebook|webinar)_url\}")
            self.assertNotRegex(plan["messages"]["refusal"] + plan["messages"]["invalid"], r"_url\}")
            routes = plan["intended_branches"]["transitions"]
            deliveries = [edge for edge in routes if edge["to"] == "delivery"]
            self.assertEqual(len(deliveries), 1)
            self.assertIn(fields[-1], deliveries[0]["condition"])
            if len(fields) == 2:
                self.assertEqual(deliveries[0]["from"], "phone")
                self.assertIn("prior required contact", deliveries[0]["condition"])
        for identifier in ("contact-material-inro-6022", "webinar-inro-6054"):
            plan = self.packets[identifier]["plans"][0]
            self.assertTrue(any(e["to"] == "delivery" and e["condition"] == "Actual SKIP reply" for e in plan["intended_branches"]["transitions"]))

    def test_confirmed_additional_copy_is_merged_not_a_second_or_timed_send(self):
        for identifier, source, node in (("link-delivery-manychat-90", "manychat-90", "node-1"), ("link-delivery-manychat-113", "manychat-113", "node-1"), ("offers-manychat-72", "manychat-72", "node-3")):
            plan = self.packets[identifier]["plans"][0]
            captured = json.loads((REFS / f"source-records/{source}.json").read_text())
            message = next(step["content"]["text"] for step in captured["graph"]["steps"] if step["id"] == node)
            self.assertIn(message, plan["messages"]["delivery"])
            self.assertIn(message, setup.stable(plan["operations"]).replace("\\n", "\n"))
            self.assertEqual(sum(step["id"] == "delivery" for step in plan["intended_branches"]["steps"]), 1)
            self.assertTrue(any(e["to"] == "delivery" and "Actual affirmative" in e["condition"] for e in plan["intended_branches"]["transitions"]))
            self.assertFalse(any("delay" in step["id"] or "timer" in step["id"] for step in plan["intended_branches"]["steps"]))
            self.assertNotIn("{resource_url}", plan["messages"]["initial"])
        self.assertIn("waits for their actual reply", (REFS / "setup-policy.md").read_text())
        self.assertTrue(self.observation["messaging_limits"]["source_url"].endswith("#messaging-limits"))

    def test_help_does_not_loop_and_examples_are_exact_and_unique(self):
        for packet in self.packets.values():
            examples = packet["function_review"]["examples"]
            self.assertEqual(len(examples), len({setup.stable([e["source_id"], e["node_id"], e["adapted_text"]]) for e in examples}))
            for plan in packet["plans"]:
                if plan["messages"].get("help"):
                    self.assertIn("bare HELP", plan["instruction"])
                    self.assertIn("concrete question", plan["instruction"])
                    for edge in plan["intended_branches"]["transitions"]:
                        if edge["to"] == "help":
                            self.assertEqual(edge["condition"], "Actual bare HELP reply")


if __name__ == "__main__":
    unittest.main()
