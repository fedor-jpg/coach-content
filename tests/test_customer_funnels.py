"""Customer export checks with synthetic metadata, never live acceptance."""

import copy
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin/scripts"))
import coach
import funnel_library
import funnels
from test_funnels import ENV, save_fixture, synthetic_acceptance


class CustomerExportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.refs = self.root / "internal/funnels"
        self.skill = self.root / "plugin/skills/funnels"
        shutil.copytree(funnel_library.REFERENCES, self.refs)
        shutil.copytree(funnel_library.CUSTOMER_SKILL, self.skill)
        for module, name, value in ((funnel_library, "REFERENCES", self.refs), (funnels, "REFERENCES", self.refs),
                                    (funnel_library, "CUSTOMER_SKILL", self.skill), (funnels, "CUSTOMER_SKILL", self.skill)):
            active = patch.object(module, name, value)
            active.start()
            self.addCleanup(active.stop)

    def fixture_entry(self):
        value = funnels.recipe("inro-6220")
        return {"id": value["id"], "version": value["version"], "digest": funnels.recipe_digest(value),
                "environment": {"host": "synthetic-test", "model": "fixture", "connector_contract": "fixture"},
                "acceptance": {"status": "runtime-accepted", "accepted_at": "2026-11-03T00:00:00Z",
                               "variants": ["default"], "material_delivery": True}}

    def catalogue(self, *entries):
        (self.refs / "catalog.json").write_text(json.dumps({"schema_version": 1, "recipes": list(entries)}))

    def test_empty_registry_cannot_create_or_replace_a_package(self):
        output = self.root / "output/funnels.skill"
        with self.assertRaisesRegex(ValueError, "No runtime-accepted"):
            funnel_library.package_customer(output)
        self.assertFalse(output.parent.exists())
        output.parent.mkdir()
        output.write_bytes(b"previous release")
        with self.assertRaises(ValueError):
            funnel_library.package_customer(output)
        self.assertEqual(output.read_bytes(), b"previous release")

    def test_archive_only_contains_ready_customer_instructions(self):
        self.catalogue(self.fixture_entry())
        output = self.root / "funnels.skill"
        result = funnel_library.package_customer(output)
        self.assertEqual(result["files"], 5)
        with zipfile.ZipFile(output) as archive:
            self.assertEqual(set(archive.namelist()), {
                "funnels/SKILL.md", "funnels/references/operations.md", "funnels/references/index.md",
                "funnels/references/compatibility.json", "funnels/references/funnels/comment-to-resource.md"})
            text = "\n".join(archive.read(name).decode() for name in archive.namelist())
            for forbidden in ("inro-6220", "Manychat", "source-records", "setup-details", "adaptation_draft", "/Users/", "GraphQL"):
                self.assertNotIn(forbidden, text)
            archive.extractall(self.root / "clean-host")
        shutil.rmtree(self.refs)
        shutil.rmtree(self.skill)
        installed = self.root / "clean-host/funnels"
        self.assertIn("Send a resource", (installed / "references/index.md").read_text())
        self.assertIn("resource_url", (installed / "references/funnels/comment-to-resource.md").read_text())

    def test_version_environment_and_material_evidence_are_not_invented(self):
        for key in ("version", "digest", "status", "material_delivery", "variants"):
            with self.subTest(key=key):
                entry = self.fixture_entry()
                if key in ("version", "digest"):
                    entry[key] = "changed"
                elif key == "status":
                    entry["acceptance"][key] = "local-fixture-passed"
                elif key == "material_delivery":
                    entry["acceptance"][key] = False
                else:
                    entry["acceptance"][key] = []
                self.catalogue(entry)
                with self.assertRaises(ValueError):
                    funnel_library.customer_outputs()
        entry = self.fixture_entry()
        self.catalogue(entry)
        metadata = json.loads(funnel_library.customer_outputs()["references/compatibility.json"])
        self.assertEqual(metadata["comment-to-resource"]["environment"], entry["environment"])

    def test_changes_to_copy_and_operations_invalidate_previous_acceptance(self):
        for path in (self.skill / "SKILL.md", self.skill / "references/operations.md",
                     self.refs / "customer-recipes/inro-6220.json"):
            with self.subTest(path=path.name):
                original = path.read_text()
                self.catalogue(self.fixture_entry())
                if path.suffix == ".json":
                    card = json.loads(original)
                    card["body"] += "\nChanged promise.\n"
                    path.write_text(json.dumps(card))
                else:
                    path.write_text(original + "\nChanged instruction.\n")
                with self.assertRaisesRegex(ValueError, "Stale catalogue"):
                    funnel_library.customer_outputs()
                path.write_text(original)

    def test_unready_funnel_and_internal_data_cannot_leak_as_fallback(self):
        entry = self.fixture_entry()
        self.catalogue(entry, copy.deepcopy(entry))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            funnel_library.customer_outputs()
        self.catalogue(entry)
        path = self.refs / "customer-recipes/inro-6220.json"
        card = json.loads(path.read_text())
        card["internal_audit"] = "Do not leak this"
        path.write_text(json.dumps(card))
        self.catalogue(self.fixture_entry())
        with self.assertRaisesRegex(ValueError, "Unexpected customer"):
            funnel_library.customer_outputs()

    def test_missing_dependency_and_unsafe_paths_block_export(self):
        path = self.refs / "customer-recipes/inro-6220.json"
        original = json.loads(path.read_text())
        for field, value in (("slug", "../../outside"), ("body", "[Missing](unknown.md)"),
                             ("body", "[Internal](../setup-index.md)")):
            card = {**original, field: value}
            path.write_text(json.dumps(card))
            self.catalogue(self.fixture_entry())
            with self.assertRaises(ValueError):
                funnel_library.customer_outputs()

    def test_customer_release_fails_before_writing_with_empty_catalogue(self):
        with patch.object(funnel_library, "generate"):
            with self.assertRaisesRegex(ValueError, "No runtime-accepted"):
                coach.release(self.root / "release")
        self.assertFalse((self.root / "release").exists())

    def test_full_plugin_release_excludes_internal_base_and_maintainer_tools(self):
        self.catalogue(self.fixture_entry())
        with patch.object(funnel_library, "generate"):
            result = coach.release(self.root / "customer-plugin")
        root = Path(result["output"])
        self.assertFalse((root / "internal").exists())
        self.assertFalse((root / "tests").exists())
        self.assertEqual([path.name for path in (root / "plugin/scripts").iterdir()], ["coach.py"])
        self.assertEqual(len(list((root / "plugin/skills/funnels").rglob("*.*"))), 5)
        for item in json.loads(Path(result["manifest"]).read_text())["files"]:
            self.assertTrue((root / item["path"]).is_file())

    def test_real_validator_can_accept_resource_delivery_shape_but_not_missing_access(self):
        value = funnels.recipe("inro-6220")
        proof = self.root / "synthetic-proof"
        proof.mkdir()
        manifest = synthetic_acceptance(proof, value, material=True)
        checked = funnels.evidence_check(value, proof, ENV)
        self.assertTrue(checked["eligible"], checked["errors"])
        self.catalogue(checked["catalog_metadata"])
        self.assertEqual(len(funnel_library.customer_outputs()), 5)
        del manifest["runs"][0]["checks"]["recipient_access"]
        save_fixture(proof, value["id"] + ".json", manifest)
        self.assertFalse(funnels.evidence_check(value, proof, ENV)["eligible"])


if __name__ == "__main__":
    unittest.main()
