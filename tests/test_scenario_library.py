import copy
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
import scenario_library


class ScenarioLibraryTests(unittest.TestCase):
    def setUp(self):
        self.refs = funnel_library.REFERENCES
        self.recipes, self.coverage, self.observation = funnel_library.read_library()
        self.data = scenario_library.read_scenarios(self.refs, self.coverage, self.observation)
        self.variants = [variant for family in self.data["families"] for variant in family["variants"]]

    def source(self, identifier):
        return next(variant for variant in self.variants if identifier in variant["source_ids"])

    def test_complete_primary_coverage_and_all_thirty_analogue_links(self):
        sources = [source for variant in self.variants for source in variant["source_ids"]]
        self.assertEqual(len(sources), 60)
        self.assertEqual(len(set(sources)), 60)
        self.assertEqual({row["recipe_id"] for row in self.coverage["records"] if row["recipe_id"]}, {recipe["id"] for recipe in self.recipes})
        self.assertEqual(len(self.data["families"]), 20)
        self.assertEqual(len(self.variants), 57)
        self.assertEqual(self.source("manychat-8"), self.source("manychat-286"))
        self.assertEqual(self.source("manychat-69"), self.source("manychat-251"))
        self.assertEqual(self.source("inro-6045"), self.source("inro-6047"))
        self.assertNotEqual(self.source("inro-6045"), self.source("inro-6046"))

    def test_material_distinctions_and_no_invented_sequential_route(self):
        ids = ["inro-6022", "inro-6026", "inro-6027", "inro-6024", "manychat-81", "manychat-20", "manychat-84"]
        self.assertEqual(len({self.source(identifier)["id"] for identifier in ids}), len(ids))
        for variant in self.variants:
            self.assertNotIn("route", variant)
            self.assertTrue(variant["mandatory_conditions"])
        for source, fact in (("manychat-107", "false offers another check"), ("inro-6022", "SKIP"), ("manychat-81", "Phone is required"), ("inro-4530", "50/50"), ("manychat-57", "34%"), ("manychat-108", "score thresholds")):
            self.assertIn(fact, " ".join(self.source(source)["mandatory_conditions"]))
        self.assertIn("6 days", " ".join(self.source("inro-6049")["timing"]))
        self.assertIn("60 seconds", " ".join(self.source("manychat-90")["timing"]))
        self.assertIn("23 hours", " ".join(self.source("manychat-20")["timing"]))
        self.assertIn("2 minutes", " ".join(self.source("manychat-72")["timing"]))
        self.assertNotEqual(self.source("manychat-90"), self.source("manychat-113"))

    def test_classification_is_grounded_and_separate_from_runtime_and_client_inputs(self):
        self.assertEqual(self.observation["observed_at"], "2026-11-02")
        self.assertEqual(self.observation["profile"], "normal-mcp")
        self.assertEqual(self.observation["capabilities"]["comment"]["state"], "documented")
        self.assertEqual(self.observation["capabilities"]["story"]["state"], "dashboard_only")
        self.assertIn("listOfStories", self.observation["public_api_note"]["additional_fields"])
        self.assertFalse(self.observation["public_api_note"]["runtime_tested"])
        self.assertEqual(self.source("manychat-183")["assessment"]["status"], "replacement")
        self.assertEqual(self.source("manychat-12")["assessment"]["status"], "replacement")
        for variant in self.variants:
            assessment = variant["assessment"]
            self.assertEqual(variant["runtime_status"], "not_tested")
            self.assertTrue(assessment["reason"])
            if assessment["replacement"]:
                self.assertTrue(assessment["replacement"]["requires_consent"])
            for capability in variant["requirements"]:
                self.assertTrue(self.observation["capabilities"][capability]["basis"])
        self.assertEqual(json.loads((self.refs / "catalog.json").read_text())["recipes"], [])

    def test_6022_replacement_delivers_before_optional_email_like_existing_analogue(self):
        recipe = next(recipe for recipe in self.recipes if recipe["id"] == "inro-6022")
        initial = next(message["text"] for message in recipe["messages"] if message["id"] == "initial")
        self.assertEqual(initial, "Here is {resource_title}: {resource_url}. Reply MORE to continue.")
        self.assertIn("After MORE, explain purpose and offer optional email capture.", recipe["native"]["messages_text"])
        assessment = self.source("inro-6022")["assessment"]
        self.assertEqual(assessment["replacement"]["result"], "The resource arrives in the first DM. After MORE, AI explains the purpose and offers optional email.")
        self.assertEqual(assessment["reason"], assessment["replacement"]["changes"])
        self.assertNotIn("after an answer", assessment["replacement"]["result"])

    def test_duplicate_source_missing_ground_and_false_green_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            refs = Path(directory)
            for mutate, message in (
                (lambda data: data["families"][0]["variants"][0]["source_ids"].append("manychat-8"), "exactly one"),
                (lambda data: data["families"][0]["variants"][0]["assessment"].update(status="supported"), "cannot be green"),
                (lambda data: data["families"][0]["variants"][0]["requirements"].append("invented-tool"), "unknown capability"),
                (lambda data: data["families"][0]["variants"][0].update(route=["entry", "click", "link"]), "sequential route"),
            ):
                data = copy.deepcopy(self.data)
                mutate(data)
                (refs / "scenarios.json").write_text(json.dumps(data))
                with self.assertRaisesRegex(ValueError, message):
                    scenario_library.read_scenarios(refs, self.coverage, self.observation)

    def test_shared_continuations_are_contextual_drafts_not_automatic_integrations(self):
        outputs = scenario_library.scenario_outputs(self.refs, self.coverage, self.observation)
        index = json.loads(outputs["scenario-index.json"])
        prompts = scenario_library.continuation_prompts(self.data)
        self.assertEqual(index["continuation_prompts"], prompts)
        for source, items in prompts.items():
            family = next(family for family in self.data["families"] if any(source in variant["source_ids"] for variant in family["variants"]))
            for item in items:
                self.assertIn(item["prompt"], outputs[f"scenario-details/{family['id']}.md"])
                self.assertIn(source, item["prompt"])
                self.assertIn("draft only", item["prompt"])
                self.assertIn("Never request secret API keys in chat", item["prompt"])
                self.assertIn("owner approval", item["prompt"])
        email = prompts["inro-6022"][0]["prompt"]
        self.assertIn("optional email, then deliver the checklist on a valid answer or SKIP", email)
        self.assertIn("hosted signup form", email)
        self.assertIn("ongoing bridge unverified", email)
        self.assertIn("membership in the intended list; this can complete", email)
        self.assertIn("Only if the owner requests a welcome email", email)
        self.assertIn("sender, reply-to and unsubscribe", email)
        self.assertIn("Optional:", prompts["inro-6024"][0]["scope"])
        sms = prompts["manychat-84"][0]["prompt"]
        self.assertIn("SMS-specific consent", sms)
        self.assertIn("SMS delivery is a separate optional later check", sms)
        self.assertIn("phone country code", sms)
        self.assertNotIn("inro-6220", prompts)
        for template in ("booking", "event", "checkout", "community", "whatsapp", "team-email"):
            self.assertNotIn("Brevo", json.dumps(self.data["continuations"]["templates"][template]))
        for capability in self.observation["capabilities"].values():
            self.assertIn("summary", capability)
            self.assertNotIn("summary_ru", capability)

    def test_generated_scenarios_packaged_relocated_and_freshness_gated(self):
        outputs = scenario_library.scenario_outputs(self.refs, self.coverage, self.observation)
        self.assertLess(len(outputs["scenario-index.md"].encode()), 20000)
        self.assertNotIn("Link click check →", outputs["scenario-details/link-delivery.md"])
        self.assertIn("Entry:", outputs["scenario-details/link-delivery.md"])
        self.assertIn("Outcome:", outputs["scenario-details/link-delivery.md"])
        for name in outputs:
            self.assertIn(f"internal/funnels/{name}", coach.RELEASE_FILES)
        with tempfile.TemporaryDirectory() as directory:
            relocated = Path(directory) / "relocated"
            for name in coach.RELEASE_FILES:
                target = relocated / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, target)
            command = [sys.executable, str(relocated / "plugin/scripts/funnel_library.py"), "--check"]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            (relocated / "internal/funnels/scenario-index.md").write_text("stale")
            output = Path(directory) / "not-created"
            result = subprocess.run([sys.executable, str(relocated / "plugin/scripts/coach.py"), "release", str(output)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("stale generated reference", result.stderr + result.stdout)
            self.assertFalse(output.exists())
