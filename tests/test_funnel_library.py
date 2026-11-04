import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin/scripts"))
import coach
import funnel_library


class FunnelLibraryTests(unittest.TestCase):
    def test_thirty_analogues_and_sixty_sources_have_explicit_provenance(self):
        recipes, coverage, observation = funnel_library.read_library()
        self.assertEqual(len(recipes), 30)
        self.assertEqual(len(coverage["records"]), 60)
        self.assertFalse(observation["runtime_tested"])
        self.assertEqual(json.loads((funnel_library.REFERENCES / "catalog.json").read_text())["recipes"], [])
        self.assertTrue(all(recipe["evidence"]["acceptance"]["status"] == "not_accepted" for recipe in recipes))
        self.assertTrue(all(recipe["applicability"]["prerequisites"] for recipe in recipes))

    def test_generated_references_are_current(self):
        result = funnel_library.generate(check=True)
        self.assertEqual(result["generated_files"], 171)
        self.assertLess((funnel_library.REFERENCES / "described-index.md").stat().st_size, 8192)
        entry = (funnel_library.CUSTOMER_SKILL / "SKILL.md").read_text()
        self.assertIn("only the selected", entry)
        self.assertIn("Do not search the repository for other recipes", entry)

    def test_missing_stale_and_contradictory_inputs_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            refs = Path(directory) / "references"
            shutil.copytree(funnel_library.REFERENCES, refs)
            detail = refs / "native-recipes/inro-6111.md"
            detail.write_text(detail.read_text() + "stale")
            with self.assertRaisesRegex(ValueError, "stale generated reference"):
                funnel_library.generate(refs, check=True)
            funnel_library.generate(refs)
            canonical = refs / "described-recipes/inro-6111.json"
            recipe = json.loads(canonical.read_text())
            recipe["route"]["transitions"][0]["to"] = "missing"
            canonical.write_text(json.dumps(recipe))
            with self.assertRaisesRegex(ValueError, "dangling/empty"):
                funnel_library.read_library(refs)
            canonical.unlink()
            with self.assertRaisesRegex(ValueError, "30 canonical"):
                funnel_library.read_library(refs)

    def test_replacements_and_follow_gate_have_honest_messages_and_branches(self):
        recipes = {recipe["id"]: recipe for recipe in funnel_library.read_library()[0]}
        for identifier in ("inro-comment-moderation", "inro-6111", "inro-6086"):
            recipe = recipes[identifier]
            self.assertEqual(recipe["reconciliation"]["relationship"], "deliberate_business_replacement")
            self.assertEqual(recipe["route"]["origin"], "derived_native_instructions")
            self.assertEqual(recipe["evidence"]["acceptance"]["status"], "not_accepted")
        self.assertEqual(recipes["inro-6111"]["reconciliation"]["legacy_status"], "unavailable")
        self.assertIn("No public response", recipes["inro-6111"]["native"]["messages_text"])
        self.assertIn("not automatic Story-mention detection", recipes["inro-6086"]["source_differences"][0])
        follow = recipes["inro-6028"]
        self.assertIn("not follower verification", follow["source_differences"][0])
        self.assertIn("You can also follow", next(m["text"] for m in follow["messages"] if m["id"] == "initial"))
        self.assertNotIn("keyword", {i["name"] for i in recipes["inro-6085"]["inputs"]})
        waitlist = recipes["inro-6081"]["route"]
        self.assertTrue(any(edge["from"] == "joined" and edge["to"] == "withdrawn" for edge in waitlist["transitions"]))
        quiz = recipes["inro-4530"]
        self.assertEqual(next(m["text"] for m in quiz["messages"] if m["id"] == "quiz_result"), "{quiz_answer} {bonus_text}")

    def test_packaged_and_relocated_native_library_is_complete(self):
        expected = {f"internal/funnels/{name}" for name in funnel_library.outputs()}
        expected |= {str(path.relative_to(ROOT)) for path in (funnel_library.REFERENCES / "described-recipes").glob("*.json")}
        self.assertTrue(expected <= set(coach.RELEASE_FILES))
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "package"
            for name in coach.RELEASE_FILES:
                target = output / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, target)
            result = subprocess.run([sys.executable, str(output / "plugin/scripts/funnel_library.py"), "--check"], cwd=directory, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            relocated = output / "internal/funnels"
            for item in funnel_library.load(relocated / "described-index.json")["recipes"]:
                self.assertTrue((relocated / item["native_file"]).is_file())
                self.assertTrue((relocated / item["file"]).is_file())

    def test_no_dm_continuation_modes_have_only_silent_terminal_branches(self):
        recipes = funnel_library.read_library()[0]
        one_shot = {f"inro-{identifier}" for identifier in (6028, 6045, 6046, 6047, 6051, 6053, 6220)}
        self.assertEqual({recipe["id"] for recipe in recipes if recipe["native"]["modes"] == ["C"]}, one_shot)
        for recipe in recipes:
            modes = recipe["native"]["modes"]
            with self.subTest(recipe=recipe["id"]):
                if "W" not in modes:
                    for edge in recipe["route"]["transitions"]:
                        self.assertNotRegex(edge["condition"].lower(), r"\b(waitlist|withdrawn)\b")
                if "N" not in modes:
                    entry = next(step for step in recipe["route"]["steps"] if step["id"] == "entry")
                    self.assertNotRegex(entry["action"].lower(), r"contains-list|feedback term|for n\b")
                if "D" in modes:
                    continue
                self.assertEqual(recipe["configuration"]["continuation_reply_mode"], "DontReply")
                self.assertNotIn("refusal_text", {item["name"] for item in recipe["inputs"]})
                for message in recipe["messages"]:
                    if message["id"] in {"refusal", "continuation", "handoff"}:
                        self.assertEqual(message["text"], "")
                        self.assertEqual(message["availability"], "not_sent")
                for step in recipe["route"]["steps"]:
                    if step["id"] not in {"entry", "first"}:
                        self.assertEqual(step["response_mode"], "silent")
                        self.assertEqual(step["message_ids"], [])
                        self.assertFalse(any(edge["from"] == step["id"] for edge in recipe["route"]["transitions"]))

    def test_validation_rejects_one_shot_reply_and_unrelated_mode_instructions(self):
        with tempfile.TemporaryDirectory() as directory:
            refs = Path(directory) / "references"
            shutil.copytree(funnel_library.REFERENCES, refs)
            path = refs / "described-recipes/inro-6220.json"
            original = json.loads(path.read_text())
            for case, error in (("refusal", "DontReply cannot send"), ("terminal", "silent terminal"),
                                ("waitlist", "waitlist condition outside W"), ("entry", "N-only entry outside N")):
                with self.subTest(case=case):
                    recipe = json.loads(json.dumps(original))
                    if case == "refusal":
                        next(message for message in recipe["messages"] if message["id"] == "refusal").update(text="I will stop.", availability="available_template")
                    elif case == "terminal":
                        next(step for step in recipe["route"]["steps"] if step["id"] == "repeat")["response_mode"] = "send"
                    elif case == "waitlist":
                        recipe["route"]["transitions"][0]["condition"] = "Waitlist STOP writes withdrawn first."
                    else:
                        recipe["route"]["steps"][0]["action"] = "Use explicit feedback contains-list for N."
                    path.write_text(json.dumps(recipe))
                    with self.assertRaisesRegex(ValueError, error):
                        funnel_library.read_library(refs)

    def test_release_rejects_stale_native_instructions_before_creating_package(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "relocated"
            coach.source_snapshot(source)
            detail = source / "internal/funnels/native-recipes/inro-6220.md"
            detail.write_text(detail.read_text() + "\nStale generated refusal instruction.\n")
            output = Path(directory) / "rejected"
            result = subprocess.run([sys.executable, str(source / "plugin/scripts/coach.py"), "release", str(output)],
                                    cwd=directory, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing/stale generated reference: native-recipes/inro-6220.md", result.stderr)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
