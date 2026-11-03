"""Static handoff checks and offline parity only, not ChatGPT or native acceptance."""

import copy
import json
import re
import unittest
from pathlib import Path

from test_funnels import apply_commands, business, funnels, native_shaped_state, readback


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugin/skills/funnels"
GUIDE = (SKILL / "references/chatgpt-funnels.md").read_text(encoding="utf-8")
SECTIONS = dict(re.findall(r"^### (inro-[\w-]+) \| [^\n]+\n(.*?)(?=^### inro-|\Z)", GUIDE, re.M | re.S))


class NativeHandoffTests(unittest.TestCase):
    def test_funnel_is_the_default_plugin_entry_without_media_or_local_execution(self):
        start = (ROOT / "plugin/commands/start.md").read_text(encoding="utf-8")
        default, video = start.split("## Optional Video Work", 1)
        self.assertIn("skills/funnels/SKILL.md", default)
        self.assertIn("business goal", default)
        self.assertIn("Existing material is optional", default)
        self.assertIn("edit, retest and stop", default)
        self.assertNotIn("scripts/coach.py resources", default)
        self.assertNotIn("skills/campaign/SKILL.md", default)
        self.assertIn("Only if the user explicitly requests video production", video)
        self.assertIn("skills/campaign/SKILL.md", video)
        manifest = json.loads((ROOT / "plugin/.claude-plugin/plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], marketplace["plugins"][0]["version"])
        for description in (manifest["description"], marketplace["metadata"]["description"],
                            marketplace["plugins"][0]["description"]):
            self.assertIn("funnel", description.lower())
            self.assertNotIn("Reel", description)

    def test_required_native_capabilities_are_checked_before_writes(self):
        for instruction in ("exact value/inheritance restoration", "and record pagination",
                            "not a universal tool-name requirement",
                            "stop before writes; do not add a connector or invent an operation"):
            self.assertIn(instruction, GUIDE)
        entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("before the first write", entry)
        self.assertIn("Do not add a connection or switch tools after a rejection", entry)

    def test_high_level_tools_are_mapped_without_inventing_lifecycle_actions(self):
        for instruction in ("Existing explicit settings can use `update_automation_setting`",
                            "switches use `set_automation_enabled`", "without GraphQL `update` wrappers",
                            "captures use `attribute`, not GraphQL `name`", "It cannot restore inheritance",
                            "`setup_comment_replies` activates immediately",
                            "`test_reply` tests one message, not a continuing thread",
                            "Never substitute these for missing lifecycle actions"):
            self.assertIn(instruction, GUIDE)

    def test_all_thirty_source_ids_have_concrete_variant_contracts(self):
        research = json.loads((SKILL / "references/research.json").read_text(encoding="utf-8"))
        self.assertEqual(set(SECTIONS), {row["id"] for row in research["sources"]})
        self.assertEqual(len(SECTIONS), 30)
        self.assertEqual(len(re.findall(r"^### inro-", GUIDE, re.M)), 30)
        for identifier, section in SECTIONS.items():
            with self.subTest(recipe=identifier):
                for label in ("Inputs", "Messages", "Native", "End/stop"):
                    self.assertRegex(section, rf"(?m)^{label}: .+")
                modes = re.search(r"^Native: ([A-Z+]+)\.", section, re.M).group(1).split("+")
                self.assertTrue(set(modes) <= set("CNPDQHETW"))
                self.assertEqual(len(set(modes) & set("CNPD")) >= 1, True)
                self.assertIn("S", section.split("End/stop:", 1)[1])
                self.assertNotIn("blockers:", section.lower())

    def test_recipe_message_parameters_are_declared(self):
        common = {"campaign", "language", "keyword", "post_ids", "public_text", "initial_text", "refusal_text", "handoff_text"}
        for identifier, section in SECTIONS.items():
            inputs = re.search(r"^Inputs: (.+)", section, re.M).group(1)
            for parameter in re.findall(r"\{([a-z_]+)\}", section):
                with self.subTest(recipe=identifier, parameter=parameter):
                    self.assertTrue(parameter in common or re.search(rf"\b{parameter}\b", inputs))

    def test_single_file_has_no_local_runtime_or_relative_reference_dependency(self):
        self.assertLess(len(GUIDE.encode("utf-8")), 32768)
        for dependency in ("/Users/", "/private/tmp/", "python3 ", "pip install", "scripts/funnels.py", "select --environment"):
            self.assertNotIn(dependency, GUIDE)
        self.assertEqual(re.findall(r"\]\((?!https?://)[^)]+\)", GUIDE), [])
        for operation in ("get_type", "get_playbook", "execute_query", "execute_mutation", "fuelyAutomationCreate",
                          "fuelyAutomationUpdateSetting", "fuelyAutomationSetEnabled"):
            self.assertIn(operation, GUIDE)
        entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/chatgpt-funnels.md", entry)
        self.assertNotIn("return before `select`", entry)

    def test_changed_outcomes_do_not_relabel_literal_source_evidence(self):
        for identifier in ("inro-comment-moderation", "inro-6111"):
            self.assertIn("Comments remain visible", SECTIONS[identifier])
            self.assertIn("Difference:", SECTIONS[identifier])
            self.assertEqual(funnels.recipe(identifier)["status"], "unavailable")
        self.assertIn("not automatic Story-mention detection", SECTIONS["inro-6086"])
        self.assertEqual(funnels.recipe("inro-6086")["status"], "unverified")
        self.assertEqual(funnels.load(SKILL / "references/catalog.json")["recipes"], [])
        self.assertIn("30 predefined business analogues", GUIDE)
        self.assertIn("not exact copies", GUIDE)
        self.assertIn("do not ask the coach to design a workaround", GUIDE)
        self.assertIn("Accept each against its stated outcome", GUIDE)
        self.assertIn("self-reported shares, never verified mentions", GUIDE)
        self.assertIn("not `error=null` as success", GUIDE)

    def test_lifecycle_and_permission_boundaries_are_explicit(self):
        for safeguard in ("verify AI control before inviting a fresh test entry", "do not count it as campaign delivery",
                          "re-read within 60 seconds", "never leave a failed test ON",
                          "Never merge dormant rules into an activated list",
                          "inspect source/ref and the matching comment custom",
                          "do not infer DM-only readiness",
                          "Never change system source/ref",
                          "exact refusal_text; cover refusal before keyword matching"):
            self.assertIn(safeguard, GUIDE)
        for safeguard in ("existing matching custom with working scoped handoff", "do not rewrite shared handoff",
                          "D fallback is a separate path", "Never retry a blocked write"):
            self.assertIn(safeguard, GUIDE)
        for safeguard in ("If general DM was OFF", "If general DM was ON", "separate enable approval",
                          "never wake foreign dormant records", "Preserve concurrent text", "stays ON",
                          "safe owned disable", "exact owned capture proof", "zero-command stop",
                          "Never silently use `return_chat_to_ai`", "Originally OFF test"):
            with self.subTest(safeguard=safeguard):
                self.assertIn(safeguard.casefold(), GUIDE.casefold())
        self.assertIn("A read-only request permits a proposal, not writes", GUIDE)
        self.assertIn("Qualification without capture needs no global attribute inventory", GUIDE)

    def test_off_dm_followups_staged_before_enable_for_comment_and_dm_only(self):
        for instruction in ("For ANY D recipe", "C+D 6025 and D-only 6021", "exact inheritance and parent readback",
                            "base still OFF BEFORE enable", "custom alone is insufficient",
                            "originally ON base with `Send` remains a shared conflict requiring separate approval"):
            self.assertIn(instruction, GUIDE)
        for identifier in ("inro-6025", "inro-6021"):
            with self.subTest(recipe=identifier):
                value = funnels.recipe(identifier)
                current = native_shaped_state(value)
                for rule in current["rules"]:
                    rule["settings"]["followUps"].update({"howToSend": "Send", "messagePrompt": "Original dormant follow-up."})
                if "ownership" in current:
                    current["ownership"]["rule_sha256"] = funnels.fingerprint(current["rules"][-1])
                before = copy.deepcopy(current["rules"][2]["settings"]["followUps"])
                plan = funnels.prepare(value, business(value), current, True)
                self.assertEqual(plan["ownership_before_write"]["rules"]["fixture-dm"]["settings"]["followUps"], before)
                configured = readback(plan, current)
                dm = configured["rules"][2]
                self.assertFalse(dm["enabled"])
                self.assertEqual(dm["settings"]["followUps"]["howToSend"], "DontSend")
                self.assertIsNone(dm["settings"]["followUps"]["inheritsFrom"])
                self.assertTrue(funnels.verify(plan, configured)["configuration_verified"])
                running = readback(plan, current, "enabled")
                stop = funnels.stop_plan(plan, running)
                operations = stop["commands"]
                disabled = next(index for index, operation in enumerate(operations)
                                if operation["operation"] == "fuelyAutomationSetEnabled"
                                and operation["variables"] == {"botID": plan["bot_id"], "id": "fixture-dm", "enabled": False})
                restored = next(index for index, operation in enumerate(operations)
                                if operation["variables"]["id"] == "fixture-dm"
                                and "followUps" in operation["variables"].get("update", {}))
                self.assertLess(disabled, restored)
                stopped = apply_commands(running, operations)
                self.assertFalse(stopped["rules"][2]["enabled"])
                self.assertEqual(stopped["rules"][2]["settings"]["followUps"], before)

    def test_concurrent_shared_dm_retained_on_never_restores_dormant_send(self):
        self.assertIn("only AFTER the general DM base is read back OFF", GUIDE)
        self.assertIn("base to remain ON, retain `DontSend`; never restore `Send`", GUIDE)
        for identifier in ("inro-6025", "inro-6021"):
            with self.subTest(recipe=identifier):
                value = funnels.recipe(identifier)
                current = native_shaped_state(value)
                current["rules"][2]["settings"]["followUps"] = {
                    "howToSend": "Send", "messagePrompt": "Original dormant follow-up.", "inheritsFrom": None}
                plan = funnels.prepare(value, business(value), current, True)
                running = readback(plan, current, "enabled")
                running["rules"][2]["settings"]["incomingMessages"]["messagePrompt"] += "\nConcurrent support instruction."
                stop = funnels.stop_plan(plan, running)
                stopped = apply_commands(running, stop["commands"])
                self.assertTrue(stopped["rules"][2]["enabled"])
                self.assertEqual(stopped["rules"][2]["settings"]["followUps"]["howToSend"], "DontSend")
                self.assertIn("Concurrent support instruction.", stopped["rules"][2]["settings"]["incomingMessages"]["messagePrompt"])
                self.assertFalse(stop["restoration_complete"])
                self.assertTrue(funnels.verify_stop(stop, stopped)["settings_stopped"])

    def test_journal_adoption_and_short_coach_reply_are_not_hidden_work(self):
        for instruction in ("5-7 short lines and one approval question", "not a dump of technical IDs",
                            "never transports files manually", "must specifically authorize the exact existing rule ID",
                            "restoration baseline BEFORE writes", "Never create a replacement",
                            "do not invent hidden storage", "Do not promise cross-account recovery"):
            self.assertIn(instruction, GUIDE)
        self.assertIn("An address in configuration is not proof of availability", GUIDE)
        self.assertIn("recipient access, not just owner access", GUIDE)

    def test_waitlist_description_matches_helper_and_measured_budget(self):
        template = re.search(r'\*\*W\*\*.*?Description: "([^"]+)"', GUIDE).group(1)
        value = funnels.recipe("inro-6081")
        data = business(value)
        data["campaign_id"] = "c" * 48
        current = native_shaped_state(value)
        current["ownership"]["campaign_id"] = data["campaign_id"]
        plan = funnels.prepare(value, data, current, True)
        description = template.format(campaign=data["campaign_id"])
        self.assertEqual(len(description.encode("ascii")), 217)
        for settings in plan["expected"].values():
            self.assertEqual(settings["collectContactInfo"]["captures"][-1]["description"], description)
        self.assertIn("not a provider limit", GUIDE)

    def test_native_comment_preview_uses_session_conversation_and_actual_readback(self):
        for procedure in (
            "previewResponsesStartForFuelyAutomation(botID, fuelyAutomationID)",
            "returned `conversationID`, NOT session `id`",
            "previewResponsesInstagramPostCommentSend(botID, conversationID, comment: {text, postCaption})",
            "both text fields are required",
            "previewResponsesInstagramTextSend(botID, conversationID, message: {text})",
            "optional `clientId`",
            "Read actual preview conversation messages after EVERY send",
            "`test_reply`: it is a DM shortcut, not comment-dispatch proof",
            "do not prove Instagram post/keyword routing, actual delivery or delivery-window behavior",
            "a real path is still required",
        ):
            with self.subTest(procedure=procedure):
                self.assertIn(procedure, GUIDE)


if __name__ == "__main__":
    unittest.main()
