import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugin/scripts"))
import coach


class FunnelPublicationTests(unittest.TestCase):
    def test_metadata_and_release_scope(self):
        plugin = json.loads((ROOT / "plugin/.claude-plugin/plugin.json").read_text())
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(plugin["version"], "0.3.0")
        self.assertEqual(marketplace["plugins"][0]["version"], plugin["version"])
        self.assertEqual(len(coach.RELEASE_FILES), len(set(coach.RELEASE_FILES)))
        for name in coach.RELEASE_FILES:
            path = ROOT / name
            self.assertTrue(path.is_file() and not path.is_symlink(), name)
            self.assertFalse(set(path.relative_to(ROOT).parts) & {"_system", "artifacts", "node_modules", "__pycache__", ".env"}, name)
        index = json.loads((ROOT / "internal/funnels/setup-index.json").read_text())
        self.assertEqual(len(index["variants"]), 57)
        self.assertEqual(sum(v["status"] == "adaptation_draft_requires_consent" for v in index["variants"]), 30)
        self.assertEqual(sum(v["status"] == "waiting_for_chatfuel" for v in index["variants"]), 25)
        self.assertEqual(sum(v["status"] == "source_incomplete_reference_only" for v in index["variants"]), 2)
        self.assertEqual(index["runtime_accepted"], 0)

    def test_native_entry_has_no_machine_specific_dependency(self):
        skill = ROOT / "plugin/skills/funnels"
        entry = (skill / "SKILL.md").read_text()
        self.assertNotIn("Local setup revision", entry)
        self.assertIn("A saved setting or a preview is not delivery", entry)
        for path in [skill / "SKILL.md", skill / "references/operations.md"]:
            text = path.read_text()
            self.assertNotRegex(text, r"/(?:Users|home)/[^/\s]+|/private/tmp/|file://", str(path.relative_to(ROOT)))
        for reference in re.findall(r"\]\((references/[^)]+)\)", entry):
            if reference == "references/index.md":
                self.assertFalse((skill / reference).exists())
                self.assertEqual(json.loads((ROOT / "internal/funnels/catalog.json").read_text())["recipes"], [])
            else:
                self.assertTrue((skill / reference).is_file(), reference)

    def test_release_contains_no_secret_patterns(self):
        secret = re.compile(r"\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,})\b|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
        for name in coach.RELEASE_FILES:
            self.assertIsNone(secret.search((ROOT / name).read_text()), name)

    def test_relocated_source_validates_without_media_tools_or_developer_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "portable source"
            coach.source_snapshot(source)
            plugin = source / "plugin"
            commands = [
                [sys.executable, str(plugin / "scripts/coach.py"), "resources"],
                [sys.executable, str(plugin / "scripts/funnels.py"), "--help"],
                [sys.executable, str(plugin / "scripts/funnel_library.py"), "--check"],
            ]
            for command in commands:
                result = subprocess.run(command, cwd=directory, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr[-1500:])
            resources = json.loads(subprocess.check_output(commands[0], cwd=directory, text=True))
            self.assertIn(str(plugin), json.dumps(resources))


if __name__ == "__main__":
    unittest.main()
