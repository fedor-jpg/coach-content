import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = importlib.util.spec_from_file_location("coach", ROOT / "plugin/scripts/coach.py")
coach = importlib.util.module_from_spec(MODULE)
MODULE.loader.exec_module(coach)


def invoke(*arguments):
    result = subprocess.run([shutil.which("python3"), str(ROOT / "plugin/scripts/coach.py"), *map(str, arguments)],
                            capture_output=True, text=True)
    if result.returncode:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


def fixture(folder):
    source = folder / "generated-test-source.mp4"
    coach.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i",
               "testsrc2=size=640x360:rate=30", "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000",
               "-t", "6", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(source)])
    return source


def demo(folder):
    folder.mkdir(parents=True, exist_ok=True)
    fixture(folder)
    spec = {"source": "generated-test-source.mp4", "rights": "Generated test pattern and sine tone; no coach or real speech",
            "test_media": True, "clips": [{"start": 0, "end": 2}, {"start": 3, "end": 5}],
            "framing": "contain", "hook": "GENERATED TEST MEDIA", "hook_seconds": 3,
            "caption_size": 36, "captions": [{"start": 0, "end": 2, "text": "MECHANICAL TEST ONLY"}]}
    coach.save(folder / "source.json", {"source_sha256": coach.digest(folder / spec["source"])})
    coach.save(folder / "promise.json", {"benefit": "Generated mechanical fixture only"})
    spec["promise_sha256"] = coach.digest(folder / "promise.json")
    coach.save(folder / "edit.json", spec)
    first = invoke("render", folder / "edit.json", folder / "reel.mp4")
    invoke("init", folder / "campaign.json")
    invoke("set", folder / "campaign.json", "--stage", "source", "--file", folder / "source.json")
    invoke("set", folder / "campaign.json", "--stage", "promise", "--file", folder / "promise.json")
    invoke("set", folder / "campaign.json", "--stage", "edit", "--file", folder / "reel.receipt.json")
    invoke("approve", folder / "campaign.json", "--stage", "source", "--by", "TEST FIXTURE")
    invoke("approve", folder / "campaign.json", "--stage", "promise", "--by", "TEST FIXTURE")
    invoke("approve", folder / "campaign.json", "--stage", "edit", "--by", "TEST FIXTURE - not a coach approval")
    # This is the deterministic edit produced for the recorded revision request.
    spec["clips"] = [{"start": 1, "end": 4}]
    spec["caption_size"] = 52
    spec["hook_seconds"] = 2
    coach.save(folder / "edit-revision.json", spec)
    second = invoke("render", folder / "edit-revision.json", folder / "reel-revision.mp4")
    state = invoke("set", folder / "campaign.json", "--stage", "edit", "--file", folder / "reel-revision.receipt.json")
    report = {"classification": "Generated mechanical fixture, NOT real coach source or E2E",
              "revision_request": "Remove the first second, use one continuous excerpt, and make captions larger.",
              "interpretation": "start=1,end=4; caption_size 36 -> 52; two clips -> one",
              "first": first, "revision": second, "approval_invalidated": "edit" not in state["approvals"]}
    coach.save(folder / "mechanical-report.json", report)
    return report


class StateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="coach-test-")
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name)
        self.state = self.folder / "campaign.json"
        invoke("init", self.state)

    def artifact(self, stage, value):
        path = self.folder / (stage + ".json")
        coach.save(path, value)
        return invoke("set", self.state, "--stage", stage, "--file", path)

    def approve_all(self):
        for stage in coach.STAGES:
            self.artifact(stage, {"version": 1})
        for stage in coach.STAGES:
            invoke("approve", self.state, "--stage", stage, "--by", "Fixture")

    def test_source_change_invalidates_all_approvals(self):
        self.approve_all()
        state = self.artifact("source", {"version": 2})
        self.assertEqual(state["approvals"], {})
        with self.assertRaises(AssertionError):
            invoke("approve", self.state, "--stage", "delivery", "--by", "Fixture")
        with self.assertRaises(AssertionError):
            self.artifact("delivery", {"version": 1})

    def test_edit_change_preserves_source_and_promise_only(self):
        self.approve_all()
        state = self.artifact("edit", {"version": 2})
        self.assertEqual(set(state["approvals"]), {"source", "promise"})

    def test_source_mutation_cannot_refresh_delivery_over_stale_prerequisites(self):
        self.approve_all()
        self.artifact("source", {"version": 2})
        with self.assertRaises(AssertionError):
            self.artifact("delivery", {"version": 2})
        with self.assertRaises(AssertionError):
            invoke("approve", self.state, "--stage", "delivery", "--by", "Fixture")
        with self.assertRaises(AssertionError):
            invoke("action", self.state, "--stage", "delivery", "--key", "stale", "--result", "pending")
        for stage in coach.STAGES[1:]:
            self.artifact(stage, {"version": 2})
        with self.assertRaises(AssertionError):
            invoke("approve", self.state, "--stage", "delivery", "--by", "Fixture")
        for stage in coach.STAGES:
            invoke("approve", self.state, "--stage", stage, "--by", "Fixture")
        result = invoke("action", self.state, "--stage", "delivery", "--key", "fresh", "--result", "pending")
        self.assertEqual(result["actions"]["fresh"]["status"], "pending")

    def test_promise_change_invalidates_embedded_cta_without_cycle(self):
        self.approve_all()
        result = self.artifact("promise", {"version": 2, "cta": "NEW"})
        self.assertEqual(set(result["approvals"]), {"source"})
        self.assertTrue(result["artifacts"]["edit"]["stale"])
        with self.assertRaises(AssertionError):
            invoke("approve", self.state, "--stage", "edit", "--by", "Fixture")
        invoke("approve", self.state, "--stage", "promise", "--by", "Fixture")
        self.artifact("edit", {"version": 2, "cta": "NEW"})
        invoke("approve", self.state, "--stage", "edit", "--by", "Fixture")
        self.artifact("delivery", {"version": 2, "cta": "NEW"})
        result = invoke("approve", self.state, "--stage", "delivery", "--by", "Fixture")
        self.assertEqual(result["approvals"]["delivery"]["dependencies"], result["artifacts"]["delivery"]["dependencies"])

    def test_out_of_band_artifact_mutation_blocks_approval_and_pending(self):
        for stage in ("source", "promise", "edit", "delivery"):
            with self.subTest(stage=stage):
                self.approve_all()
                coach.save(self.folder / (stage + ".json"), {"version": "changed outside ledger"})
                with self.assertRaises(AssertionError):
                    invoke("approve", self.state, "--stage", "delivery", "--by", "Fixture")
                with self.assertRaises(AssertionError):
                    invoke("action", self.state, "--stage", "delivery", "--key", "mutated-" + stage, "--result", "pending")

    def test_referenced_file_mutation_blocks_pending(self):
        media = self.folder / "media.bin"
        media.write_bytes(b"original fixture")
        self.artifact("source", {"files": [{"path": media.name, "sha256": coach.digest(media)}]})
        for stage in coach.STAGES[1:]:
            self.artifact(stage, {"version": 1})
        for stage in coach.STAGES:
            invoke("approve", self.state, "--stage", stage, "--by", "Fixture")
        media.write_bytes(b"changed fixture")
        with self.assertRaises(AssertionError):
            invoke("action", self.state, "--stage", "delivery", "--key", "mutated-media", "--result", "pending")

    def test_snapshot_relocation_and_render_context_binding(self):
        self.approve_all()
        relocated = self.folder / "relocated"
        relocated.mkdir()
        for path in self.folder.glob("*.json"):
            shutil.copy2(path, relocated / path.name)
        result = invoke("action", relocated / "campaign.json", "--stage", "delivery", "--key", "relocated", "--result", "pending")
        self.assertEqual(result["actions"]["relocated"]["status"], "pending")
        with self.assertRaises(AssertionError):
            self.artifact("edit", {"output_sha256": "fixture", "source_sha256": "wrong", "promise_sha256": "wrong"})

    def test_text_only_restore_blocks_approvals_and_actions_without_media(self):
        media = self.folder / "mechanical-fixture.bin"
        media.write_bytes(b"Test bytes only, not coach video")
        self.artifact("source", {"files": [{"path": media.name, "sha256": coach.digest(media)}]})
        for stage in coach.STAGES[1:]:
            self.artifact(stage, {"version": 1})
        for stage in coach.STAGES:
            invoke("approve", self.state, "--stage", stage, "--by", "Fixture")
        restored = self.folder / "text-only-restore"
        restored.mkdir()
        for path in self.folder.glob("*.json"):
            shutil.copy2(path, restored / path.name)
        state = restored / "campaign.json"
        before = coach.digest(state)
        self.assertTrue(invoke("show", state)["approvals"])
        self.assertFalse((restored / media.name).exists())
        for stage in ("delivery", "review"):
            with self.assertRaises(AssertionError):
                invoke("approve", state, "--stage", stage, "--by", "Fixture")
            with self.assertRaises(AssertionError):
                invoke("action", state, "--stage", stage, "--key", "missing-media-" + stage, "--result", "pending")
        self.assertEqual(coach.digest(state), before)

    def test_legacy_ledger_cannot_authorize(self):
        coach.save(self.state, {"version": 1})
        with self.assertRaises(AssertionError):
            invoke("approve", self.state, "--stage", "delivery", "--by", "Fixture")

    def test_render_receipt_requires_current_promise_hash(self):
        self.artifact("source", {"source_sha256": "unit-source-hash"})
        self.artifact("promise", {"benefit": "unit fixture"})
        receipt = {"output_sha256": "unit-output-hash", "source_sha256": "unit-source-hash", "promise_sha256": "old-promise-hash"}
        with self.assertRaises(AssertionError):
            self.artifact("edit", receipt)
        receipt["promise_sha256"] = coach.digest(self.folder / "promise.json")
        result = self.artifact("edit", receipt)
        self.assertFalse(result["artifacts"]["edit"]["stale"])

    def test_same_data_is_noop_and_subscriber_change_invalidates_review(self):
        self.approve_all()
        state = self.artifact("review", {"version": 1})
        self.assertIn("review", state["approvals"])
        state = self.artifact("review", {"version": 2, "answer": "new answer"})
        self.assertNotIn("review", state["approvals"])
        self.assertIn("delivery", state["approvals"])

    def test_unknown_action_cannot_be_retried_and_can_be_reconciled(self):
        self.approve_all()
        common = ("action", self.state, "--stage", "delivery", "--key", "fixture-post-recipient")
        invoke(*common, "--result", "pending")
        invoke(*common, "--result", "unknown", "--evidence", "fixture timeout")
        with self.assertRaises(AssertionError):
            invoke(*common, "--result", "pending")
        result = invoke(*common, "--result", "confirmed", "--evidence", "fixture readback, no remote call")
        self.assertEqual(result["actions"]["fixture-post-recipient"]["status"], "confirmed")

    def test_stop_blocks_actions_and_clears_approvals(self):
        self.approve_all()
        state = invoke("stop", self.state)
        self.assertEqual(state["approvals"], {})
        with self.assertRaises(AssertionError):
            self.artifact("edit", {"version": 2})
        with self.assertRaises(AssertionError):
            invoke("action", self.state, "--stage", "delivery", "--key", "new", "--result", "pending")
        state = invoke("resume", self.state)
        self.assertEqual(state["approvals"], {})


class RenderTests(unittest.TestCase):
    def test_hook_revision_refreshes_cover_caption_and_preserves_audio(self):
        with tempfile.TemporaryDirectory(prefix="coach-hook-revision-") as directory:
            folder = Path(directory)
            source = fixture(folder)
            spec = {"source": source.name, "rights": "Generated pattern and tone; no verified speech",
                    "test_media": True, "clips": [{"start": 0, "end": 2}], "framing": "contain",
                    "hook": "Check one decision.", "hook_seconds": 0.75, "cta": "TEST EXAMPLE", "cta_seconds": 0.75,
                    "captions": [], "caption_engine": "drawtext", "cover_title": "Check one decision.",
                    "cover_subtitle": "Mechanical fixture only", "cover_time": 1, "credit": "GENERATED TEST MEDIA"}
            coach.save(folder / "edit.json", spec)
            first = invoke("render", folder / "edit.json", folder / "reel.mp4")
            first_cover = invoke("cover", folder / "edit.json", folder / "cover.jpg")
            suffix = "\nTEST EXAMPLE\nGenerated mechanical fixture; no endorsement or send.\n"
            (folder / "caption.txt").write_text(spec["hook"] + suffix, encoding="utf-8")
            preserved = {p: coach.digest(p) for p in folder.iterdir() if p.is_file()}
            spec["hook"] = spec["cover_title"] = "What would change your mind?"
            coach.save(folder / "edit-revision.json", spec)
            second = invoke("render", folder / "edit-revision.json", folder / "reel-revision.mp4")
            second_cover = invoke("cover", folder / "edit-revision.json", folder / "cover-revision.jpg")
            (folder / "caption-revision.txt").write_text(spec["hook"] + suffix, encoding="utf-8")
            self.assertNotEqual(first["output_sha256"], second["output_sha256"])
            self.assertNotEqual(first_cover["sha256"], second_cover["sha256"])
            self.assertEqual((folder / "caption-revision.txt").read_text(encoding="utf-8"), spec["cover_title"] + suffix)
            self.assertNotEqual(coach.digest(folder / "caption.txt"), coach.digest(folder / "caption-revision.txt"))
            for path, digest in preserved.items():
                self.assertEqual(coach.digest(path), digest)
            hashes = []
            for name in ("reel.mp4", "reel-revision.mp4"):
                pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(folder / name), "-map", "0:a:0",
                                      "-c:a", "pcm_s16le", "-f", "s16le", "-"], capture_output=True, check=True).stdout
                self.assertTrue(pcm)
                hashes.append(hashlib.sha256(pcm).hexdigest())
            self.assertEqual(*hashes)
            self.assertEqual(first["source_sha256"], second["source_sha256"])
            receipt = coach.load(folder / "reel-revision.receipt.json")
            self.assertEqual(receipt["spec"]["captions"], [])
            self.assertIn("human playback and editorial acceptance required", receipt["verification"])
            self.assertEqual(coach.probe(folder / "cover-revision.jpg")["streams"][0]["width"], 720)

    def test_complete_snapshot_restores_exact_files_before_locator_advances(self):
        with tempfile.TemporaryDirectory(prefix="coach-rehydrate-") as directory:
            base = Path(directory)
            original, stored, restored = [base / name for name in ("original campaign", "local binary fixture", "new execution")]
            for folder in (original, stored, restored, original / "media", original / "edits", original / "renders"):
                folder.mkdir()
            source = fixture(original / "media")
            coach.save(original / "source.json", {"source_sha256": coach.digest(source),
                       "files": [{"path": "media/" + source.name, "sha256": coach.digest(source)}]})
            coach.save(original / "promise.json", {"benefit": "Mechanical rehydration fixture; not a subscriber send"})
            spec = {"source": "../media/" + source.name, "rights": "Generated test pattern and tone only",
                    "test_media": True, "clips": [{"start": 0, "end": 1}], "framing": "contain",
                    "promise_sha256": coach.digest(original / "promise.json"), "captions": []}
            coach.save(original / "edits/edit.json", spec)
            invoke("render", original / "edits/edit.json", original / "renders/reel.mp4")
            coach.save(original / "delivery.json", {"message": "Mechanical fixture, no external send"})
            state = original / "campaign.json"
            invoke("init", state)
            for stage, name in (("source", "source.json"), ("promise", "promise.json"),
                                ("edit", "renders/reel.receipt.json"), ("delivery", "delivery.json")):
                invoke("set", state, "--stage", stage, "--file", original / name)
                invoke("approve", state, "--stage", stage, "--by", "MECHANICAL FIXTURE")
            (original / "transcript.txt").write_text("Generated pattern and tone; not real coach speech.\n", encoding="utf-8")
            skill = (ROOT / "plugin/skills/campaign/SKILL.md").read_text(encoding="utf-8")
            index = json.loads(skill.split("```json\n")[2].split("```", 1)[0])
            previous = {"artifact_url": "https://example.invalid/artifact/previous-fixture",
                        "artifact_version": "fixture-v1", "index_path": "snapshot.json", "index_sha256": "previous-fixture"}
            locator = base / "project-locator.json"
            coach.save(locator, previous)
            locator_hash = coach.digest(locator)
            index["previous_locator"] = previous
            index["files"] = [{"path": p.relative_to(original).as_posix(), "sha256": coach.digest(p), "bytes": p.stat().st_size}
                              for p in sorted(original.rglob("*")) if p.is_file()]
            for entry in index["files"]:
                target = stored / entry["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(original / entry["path"], target)
            coach.save(stored / "snapshot.json", index)
            candidate = {**previous, "artifact_url": "https://example.invalid/artifact/new-fixture",
                         "artifact_version": "fixture-v2", "index_sha256": coach.digest(stored / "snapshot.json")}
            for entry in index["files"]:
                if not entry["path"].endswith(".mp4"):
                    target = restored / entry["path"]
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(stored / entry["path"], target)
            restored_state = restored / "campaign.json"
            action = ("action", restored_state, "--stage", "delivery", "--key", "fixture-only", "--result", "pending")
            (restored / "renders").mkdir(exist_ok=True)
            shutil.copyfile(stored / "renders/reel.mp4", restored / "renders/reel.mp4")
            partial_index = {"files": [e for e in index["files"] if (restored / e["path"]).exists()]}
            coach.validate_resources(partial_index, restored)
            with self.assertRaises(OSError):
                coach.current_artifact(coach.load(restored_state), "delivery", restored, approved=True)
            with self.assertRaises(AssertionError):
                invoke(*action)
            self.assertEqual(coach.digest(locator), locator_hash)
            restored_source = restored / "media" / source.name
            restored_source.parent.mkdir(parents=True)
            restored_source.write_bytes(b"Wrong readback bytes; mechanical negative fixture")
            with self.assertRaises(ValueError):
                coach.validate_resources(index, restored)
            with self.assertRaises(AssertionError):
                invoke(*action)
            self.assertEqual(coach.digest(locator), locator_hash)
            shutil.copyfile(stored / "media" / source.name, restored_source)
            coach.validate_resources(index, restored)
            coach.current_artifact(coach.load(restored_state), "delivery", restored, approved=True)
            for entry in index["files"]:
                self.assertEqual(coach.digest(restored / entry["path"]), entry["sha256"])
                self.assertEqual((restored / entry["path"]).stat().st_size, entry["bytes"])
                self.assertEqual(coach.digest(original / entry["path"]), entry["sha256"])
            self.assertEqual(coach.load(stored / "snapshot.json")["previous_locator"], previous)
            coach.save(locator, candidate)
            self.assertEqual(coach.load(locator)["index_sha256"], coach.digest(stored / "snapshot.json"))
            receipt = coach.load(restored / "renders/reel.receipt.json")
            coach.validate_resources(receipt, restored / "renders")
            self.assertEqual(coach.probe(restored / "renders/reel.mp4")["streams"][0]["width"], 720)
            self.assertEqual(invoke(*action)["actions"]["fixture-only"]["status"], "pending")

    def test_explicit_portrait_and_standalone_cover(self):
        with tempfile.TemporaryDirectory(prefix="coach-portrait-") as directory:
            folder = Path(directory)
            fixture(folder)
            spec = {"source": "generated-test-source.mp4", "rights": "Generated fixture", "test_media": True,
                    "clips": [{"start": 0.3, "end": 2.32}], "framing": "portrait",
                    "crop": {"x": 140, "y": 0, "width": 360, "height": 360},
                    "caption_engine": "drawtext", "captions": [{"start": 0, "end": 2.02, "text": "TRANSIENT TEST CAPTION"}],
                    "cover_title": "Standalone test title", "cover_subtitle": "Generated test media",
                    "notice": "DRAFT TEST ONLY", "credit": "Generated fixture"}
            coach.save(folder / "edit.json", spec)
            video = invoke("render", folder / "edit.json", folder / "portrait.mp4")
            poster = invoke("cover", folder / "edit.json", folder / "cover.jpg")
            metadata = coach.probe(folder / "cover.jpg")["streams"][0]
            self.assertEqual((metadata["width"], metadata["height"]), (720, 1280))
            self.assertNotEqual(poster["sha256"], video["output_sha256"])
            pixels = subprocess.run(["ffmpeg", "-v", "error", "-i", str(folder / "cover.jpg"),
                                     "-vf", "scale=36:64", "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                    capture_output=True, check=True).stdout
            self.assertEqual(len(pixels), 36 * 64 * 3)
            self.assertGreater(max(pixels) - min(pixels), 100)
            spec["crop"]["x"] = 400
            coach.save(folder / "invalid.json", spec)
            with self.assertRaises(AssertionError):
                invoke("render", folder / "invalid.json", folder / "invalid.mp4")

    def test_drawtext_backend_renders_literal_text(self):
        with tempfile.TemporaryDirectory(prefix="coach-drawtext-") as directory:
            folder = Path(directory)
            fixture(folder)
            spec = {"source": "generated-test-source.mp4", "rights": "Generated test only", "test_media": True,
                    "clips": [{"start": 1, "end": 3}], "hook": "GENERATED TEST", "hook_seconds": 1,
                    "captions": [{"start": 0, "end": 1, "text": "100% {literal} \\ text"}],
                    "caption_engine": "drawtext", "credit": "No coach source", "cta": "TEST CTA", "cta_seconds": 0.5}
            coach.save(folder / "edit.json", spec)
            result = invoke("render", folder / "edit.json", folder / "literal.mp4")
            self.assertEqual(result["caption_engine"], "drawtext")
            self.assertAlmostEqual(result["duration"], 2, delta=0.25)

    def test_silent_cover_encode_and_missing_rights_rejection(self):
        with tempfile.TemporaryDirectory(prefix="coach-silent-") as directory:
            folder = Path(directory)
            coach.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i",
                       "testsrc2=size=320x240:rate=30", "-t", "2", "-an", "-c:v", "libx264", str(folder / "source.mp4")])
            spec = {"source": "source.mp4", "rights": "Generated test", "test_media": True,
                    "clips": [{"start": 0, "end": 1}], "framing": "cover", "credit": "TEST ONLY"}
            coach.save(folder / "edit.json", spec)
            result = invoke("render", folder / "edit.json", folder / "silent.mp4")
            self.assertFalse(result["audio"])
            self.assertAlmostEqual(result["duration"], 1, delta=0.25)
            spec["rights"] = ""
            coach.save(folder / "bad.json", spec)
            with self.assertRaises(AssertionError):
                invoke("render", folder / "bad.json", folder / "bad.mp4")
            self.assertFalse((folder / "bad.mp4").exists())

    def test_transcription_rejects_stub_weights_without_claiming_speech(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "stub.bin").write_bytes(b"stub")
            (folder / "source.mp4").write_bytes(b"not a video")
            with self.assertRaises(AssertionError):
                invoke("transcribe", folder / "source.mp4", folder / "transcript.json", "--model", folder / "stub.bin")
            self.assertFalse((folder / "transcript.json").exists())

    def test_real_encode_revision_and_approval_invalidation(self):
        with tempfile.TemporaryDirectory(prefix="coach-media-") as directory:
            report = demo(Path(directory))
            self.assertNotEqual(report["first"]["output_sha256"], report["revision"]["output_sha256"])
            self.assertAlmostEqual(report["first"]["duration"], 4, delta=0.25)
            self.assertAlmostEqual(report["revision"]["duration"], 3, delta=0.25)
            self.assertTrue(report["approval_invalidated"])
            self.assertTrue(report["revision"]["audio"])
            self.assertEqual((report["revision"]["width"], report["revision"]["height"]), (720, 1280))
            self.assertTrue(report["revision"]["test_media"])
            with self.assertRaises(AssertionError):
                invoke("render", Path(directory) / "edit.json", Path(directory) / "reel.mp4")

    def test_validation_rejects_bad_ranges_nan_and_long_captions(self):
        for value in (float("nan"), float("inf"), True, "1"):
            with self.assertRaises(ValueError):
                coach.number(value, "test", 0, 10)
        with self.assertRaises(ValueError):
            coach.subtitles({"captions": [{"start": 2, "end": 1, "text": "bad"}]}, 3)
        with self.assertRaises(ValueError):
            coach.subtitles({"captions": [{"start": 0, "end": 1, "text": "x" * 33}]}, 3)
        self.assertIn("Dialogue", coach.subtitles({"captions": [{"start": 0, "end": 9.64, "text": "Valid decimal endpoint"}]}, round(335.88 - 326.24, 9)))


class PackageTests(unittest.TestCase):
    def test_brief_text_roundtrip_without_media_does_not_approve_source(self):
        skill = (ROOT / "plugin/skills/campaign/SKILL.md").read_text(encoding="utf-8")
        template = json.loads(skill.split("```json\n", 1)[1].split("```", 1)[0])
        supplied = {"audience": "Adults", "programme": "Four sessions on workplace decisions",
                    "source_reference": "https://example.org/permitted-recording", "rights_statement": "User says reuse is permitted",
                    "language": "English", "intent": "Prepare a Reel and exercise", "limits": None}
        self.assertEqual(set(template), set(supplied))
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first execution"
            second = Path(directory) / "new execution"
            first.mkdir()
            second.mkdir()
            invoke("init", first / "campaign.json")
            coach.save(first / "brief.json", {**template, **supplied})
            before = invoke("show", first / "campaign.json")
            documents = {name: (first / name).read_text(encoding="utf-8") for name in ("brief.json", "campaign.json")}
            for name, text in documents.items():
                (second / name).write_text(text, encoding="utf-8")
                self.assertEqual(coach.digest(second / name), coach.digest(first / name))
            restored = coach.load(second / "brief.json")
            self.assertEqual(restored, supplied)
            self.assertEqual([key for key, value in restored.items() if value is None], ["limits"])
            state = invoke("show", second / "campaign.json")
            self.assertEqual(state, before)
            self.assertFalse(state["artifacts"])
            self.assertFalse(state["approvals"])
            self.assertFalse(state["actions"])

    def test_resources_without_environment_follow_relocated_helper(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "installed plugin with spaces"
            shutil.copytree(ROOT / "plugin", root)
            env = dict(os.environ)
            env.pop("CLAUDE_PLUGIN_ROOT", None)
            result = subprocess.run([shutil.which("python3"), str(root / "scripts/coach.py"), "resources"],
                                    capture_output=True, text=True, cwd=directory, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            paths = json.loads(result.stdout)
            self.assertEqual(Path(paths["root"]), root.resolve())
            self.assertEqual(paths["name"], "coach-content")
            self.assertEqual(paths["version"], coach.load(root / ".claude-plugin/plugin.json")["version"])
            for name in ("manifest", "helper", "campaign", "video", "delivery", "criteria"):
                path = Path(paths[name])
                self.assertTrue(path.is_relative_to(root.resolve()))
                self.assertEqual(path.read_bytes(), (ROOT / "plugin" / path.relative_to(root.resolve())).read_bytes())
            result = subprocess.run([shutil.which("python3"), paths["helper"], "doctor"],
                                    capture_output=True, text=True, cwd=directory, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_resources_ignore_stale_environment_and_reject_wrong_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "installed"
            shutil.copytree(ROOT / "plugin", root)
            env = {**os.environ, "CLAUDE_PLUGIN_ROOT": str(Path(directory) / "not-installed")}
            command = [shutil.which("python3"), str(root / "scripts/coach.py"), "resources"]
            result = subprocess.run(command, capture_output=True, text=True, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(Path(json.loads(result.stdout)["root"]), root.resolve())
            manifest_path = root / ".claude-plugin/plugin.json"
            for manifest in ({"name": "other-plugin", "version": "0.2.1"}, {"name": "coach-content"}):
                coach.save(manifest_path, manifest)
                result = subprocess.run(command, capture_output=True, text=True, env=env)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Installed manifest", result.stderr)

    def test_resources_reject_missing_or_escaping_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "installed"
            shutil.copytree(ROOT / "plugin", root)
            skill = root / "skills/campaign/SKILL.md"
            skill.unlink()
            command = [shutil.which("python3"), str(root / "scripts/coach.py"), "resources"]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("resource is missing", result.stderr)
            outside = Path(directory) / "outside.md"
            outside.write_text("Not part of installed plugin", encoding="utf-8")
            skill.symlink_to(outside)
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("outside its root", result.stderr)

    def test_release_allowlist_and_checksums(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "release"
            result = invoke("release", output)
            manifest = coach.load(result["manifest"])
            paths = {entry["path"] for entry in manifest["files"]}
            self.assertEqual(paths, set(coach.RELEASE_FILES))
            self.assertIn("plugin/skills/funnels/references/chatgpt-funnels.md", paths)
            for entry in manifest["files"]:
                self.assertEqual(coach.digest(output / entry["path"]), entry["sha256"])
            self.assertFalse((output / "docs/artifacts").exists())
            self.assertFalse((output / "_system").exists())
            self.assertFalse(list(output.rglob("*.bin")))
            self.assertFalse(list(output.rglob("*.mp4")))
            with self.assertRaises(AssertionError):
                invoke("release", output)

    def test_marketplace_resolves_self_contained_plugin(self):
        marketplace = coach.load(ROOT / ".claude-plugin/marketplace.json")
        plugin = (ROOT / marketplace["plugins"][0]["source"]).resolve()
        self.assertTrue(plugin.is_relative_to(ROOT))
        self.assertEqual(coach.load(plugin / ".claude-plugin/plugin.json")["name"], "coach-content")
        self.assertEqual(coach.load(plugin / ".claude-plugin/plugin.json")["version"], marketplace["plugins"][0]["version"])
        self.assertEqual(len(list((plugin / "skills").glob("*/SKILL.md"))), 4)
        self.assertTrue((plugin / "commands/start.md").is_file())
        with tempfile.TemporaryDirectory() as directory:
            relocated = Path(directory) / "relocated plugin"
            shutil.copytree(plugin, relocated)
            result = subprocess.run([shutil.which("python3"), str(relocated / "scripts/coach.py"), "doctor"],
                                    capture_output=True, text=True, cwd=directory)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo-output", type=Path)
    args, remaining = parser.parse_known_args()
    if args.demo_output:
        report = demo(args.demo_output.resolve())
        print(json.dumps({"folder": str(args.demo_output), "approval_invalidated": report["approval_invalidated"]}))
    else:
        unittest.main(argv=[__file__, *remaining])
