"""Local media editing and an approval ledger. No network operations."""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap


STAGES = ("source", "promise", "edit", "delivery", "review")
DEPENDENCIES = {
    "source": (),
    "promise": ("source",),
    "edit": ("source", "promise"),
    "delivery": ("source", "promise", "edit"),
    "review": ("delivery",),
}
RELEASE_FILES = (
    ".claude-plugin/marketplace.json", ".gitignore", "README.md", "docs/maintainer-notes.md",
    "plugin/.claude-plugin/plugin.json", "plugin/commands/start.md", "plugin/scripts/coach.py",
    "plugin/skills/campaign/SKILL.md", "plugin/skills/video/SKILL.md",
    "plugin/skills/video/references/criteria.md", "plugin/skills/delivery/SKILL.md", "tests/test_coach.py",
)


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, value):
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def run(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(f"{command[0]} failed: {result.stderr[-1800:]}")
    return result.stdout


def doctor():
    for executable in ("ffmpeg", "ffprobe"):
        if not shutil.which(executable):
            raise ValueError(f"Missing {executable}; rendering unavailable in this environment")
    filters = run(["ffmpeg", "-hide_banner", "-filters"])
    encoders = run(["ffmpeg", "-hide_banner", "-encoders"])
    backends = [name for name in ("subtitles", "drawtext") if f" {name} " in filters]
    if not backends or "libx264" not in encoders or " aac " not in encoders:
        raise ValueError("FFmpeg needs subtitles/libass or drawtext, libx264 and AAC support")
    return {"python": sys.version.split()[0], "ffmpeg": run(["ffmpeg", "-version"]).splitlines()[0],
            "caption_backends": backends,
            "status": "local runtime ready; native Cowork execution not established by this check"}


def resources():
    root = Path(__file__).resolve().parents[1]
    names = {"manifest": ".claude-plugin/plugin.json", "helper": "scripts/coach.py",
             "campaign": "skills/campaign/SKILL.md", "video": "skills/video/SKILL.md",
             "delivery": "skills/delivery/SKILL.md", "criteria": "skills/video/references/criteria.md"}
    paths = {key: (root / name).resolve() for key, name in names.items()}
    for path in paths.values():
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("Installed plugin resource is missing or outside its root")
    manifest = load(paths["manifest"])
    if manifest.get("name") != "coach-content" or not isinstance(manifest.get("version"), str) or not manifest["version"]:
        raise ValueError("Installed manifest must identify coach-content and its version")
    return {"name": manifest["name"], "version": manifest["version"], "root": str(root),
            **{key: str(path) for key, path in paths.items()}}


def probe(path):
    return json.loads(run(["ffprobe", "-v", "error", "-protocol_whitelist", "file,pipe", "-show_streams", "-show_format",
                           "-of", "json", str(path)]))


def number(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    if not low <= value <= high:
        raise ValueError(f"{name} must be between {low} and {high}")
    return value


def ass_time(seconds):
    ticks = round(seconds * 100)
    return f"{ticks // 360000}:{ticks // 6000 % 60:02}:{ticks // 100 % 60:02}.{ticks % 100:02}"


def ass_text(value):
    if not isinstance(value, str) or any(ord(c) < 32 and c != "\n" for c in value):
        raise ValueError("Text must be a string without control characters")
    return value.replace("\\", "\\\ufeff").replace("{", "\\{").replace("}", "\\}").replace("\n", "\\N")


def subtitles(spec, duration):
    size = number(spec.get("caption_size", 42), "caption_size", 24, 64)
    hook = spec.get("hook", "")
    if not isinstance(hook, str) or len(hook) > 90:
        raise ValueError("hook must contain at most 90 characters")
    lines = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 720", "PlayResY: 1280",
             "WrapStyle: 0", "[V4+ Styles]",
             "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
             f"Style: Caption,Arial,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,3,1,2,55,55,190,1",
             "Style: Hook,Arial,48,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,8,55,55,60,1",
             "Style: Credit,Arial,28,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,1,0,2,40,40,80,1",
             "Style: Notice,Arial,26,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,1,0,2,40,40,15,1",
             "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    cues = spec.get("captions", [])
    if not isinstance(cues, list):
        raise ValueError("captions must be a list")
    previous_end = 0
    for cue in cues:
        start = number(cue["start"], "caption start", 0, duration)
        end = number(cue["end"], "caption end", 0, duration)
        text = cue["text"]
        if end <= start or start < previous_end:
            raise ValueError("Caption cues must be ordered, non-overlapping and positive")
        if not isinstance(text, str) or not text.strip() or len(text.splitlines()) > 2 or any(len(line) > 32 for line in text.splitlines()):
            raise ValueError("Caption needs 1-2 nonempty lines of at most 32 characters")
        previous_end = end
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Caption,,0,0,0,,{ass_text(text)}")
    if hook:
        end = number(spec.get("hook_seconds", 3), "hook_seconds", 0.1, duration)
        lines.append(f"Dialogue: 1,0:00:00.00,{ass_time(end)},Hook,,0,0,0,,{ass_text(hook)}")
    cta = spec.get("cta", "")
    if not isinstance(cta, str) or len(cta) > 90:
        raise ValueError("cta must contain at most 90 characters")
    if cta:
        length = number(spec.get("cta_seconds", 3), "cta_seconds", 0.1, duration)
        if hook and duration - length < spec.get("hook_seconds", 3):
            raise ValueError("Hook and CTA must not overlap; shorten their durations")
        lines.append(f"Dialogue: 1,{ass_time(duration-length)},{ass_time(duration)},Hook,,0,0,0,,{ass_text(cta)}")
    credit = spec.get("credit", "")
    if not isinstance(credit, str) or len(credit) > 240 or len(credit.splitlines()) > 4:
        raise ValueError("credit must contain at most 240 characters and four lines")
    if credit:
        lines.append(f"Dialogue: 2,0:00:00.00,{ass_time(duration)},Credit,,0,0,0,,{ass_text(credit)}")
    notice = spec.get("notice", "")
    if not isinstance(notice, str) or len(notice) > 45 or "\n" in notice:
        raise ValueError("notice must be one line of at most 45 characters")
    if notice:
        lines.append(f"Dialogue: 2,0:00:00.00,{ass_time(duration)},Notice,,0,0,0,,{ass_text(notice)}")
    return "\n".join(lines) + "\n"


def frame_filter(spec, metadata):
    framing = spec.get("framing", "contain")
    if framing == "portrait":
        video = next(stream for stream in metadata["streams"] if stream["codec_type"] == "video")
        crop = spec["crop"]
        x, y, width, height = (crop[key] for key in ("x", "y", "width", "height"))
        if any(type(value) is not int or value < 0 or value % 2 for value in (x, y, width, height)):
            raise ValueError("Crop values must be nonnegative even integers")
        if width != height or width < 2 or x + width > video["width"] or y + height > video["height"]:
            raise ValueError("Portrait panel requires a square crop within the source frame")
        return f"crop={width}:{height}:{x}:{y},scale=720:720,pad=720:1280:0:230"
    if framing == "contain":
        return "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2"
    if framing == "cover":
        return "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
    raise ValueError("framing must be contain, cover or an explicitly inspected portrait crop")


def drawtext_overlay(cues, temporary):
    filters = []
    for index, (text, start, end, size, y) in enumerate(cues):
        text_lines = text.splitlines()
        spacing = round(size * 1.25)
        for line_index, line in enumerate(text_lines):
            filename = f"text-{index}-{line_index}.txt"
            (temporary / filename).write_text(line, encoding="utf-8")
            position = f"{y}-{len(text_lines)*spacing}+{line_index*spacing}" if y.startswith("h-") else f"{y}+{line_index*spacing}"
            filters.append(f"drawtext=textfile={filename}:expansion=none:font=Sans:fontsize={size}:"
                           f"fontcolor=white:borderw=2:bordercolor=black:x=(w-text_w)/2:y={position}:"
                           f"enable='gte(t,{start})*lt(t,{end})'")
    return ",".join(filters) or "null"


def cover(spec_path, output):
    runtime = doctor()
    if "drawtext" not in runtime["caption_backends"]:
        raise ValueError("Standalone cover requires FFmpeg drawtext")
    spec_path, output = Path(spec_path).resolve(), Path(output).resolve()
    if output.exists():
        raise ValueError("Cover exists; choose a new output")
    spec = load(spec_path)
    subtitles(spec, round(sum(clip["end"] - clip["start"] for clip in spec["clips"]), 9))
    source = (spec_path.parent / spec["source"]).resolve()
    title, subtitle = spec["cover_title"], spec["cover_subtitle"]
    if any(not isinstance(text, str) or len(text) > 90 for text in (title, subtitle)):
        raise ValueError("Cover title and subtitle must contain at most 90 characters")
    with tempfile.TemporaryDirectory(prefix="coach-cover-", dir=output.parent) as directory:
        temporary = Path(directory)
        cues = [("\n".join(textwrap.wrap(title, 24)), 0, 1, 52, "60"),
                ("\n".join(textwrap.wrap(subtitle, 30)), 0, 1, 34, "980"),
                (spec.get("credit", ""), 0, 1, 28, "h-80"),
                (spec.get("notice", ""), 0, 1, 26, "h-10")]
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-protocol_whitelist", "file,pipe",
             "-ss", str(spec.get("cover_time", spec["clips"][0]["start"])), "-i", str(source),
             "-vf", frame_filter(spec, probe(source)) + "," + drawtext_overlay(cues, temporary),
             "-frames:v", "1", "-q:v", "2", str(temporary / "cover.jpg")], cwd=temporary)
        with output.open("xb") as destination:
            destination.write((temporary / "cover.jpg").read_bytes())
    return {"output": str(output), "sha256": digest(output), "type": "standalone cover; not a subtitle screenshot"}


def release(output):
    root = Path(__file__).resolve().parents[2]
    output = Path(output).resolve()
    if output.exists():
        raise ValueError("Release destination exists; retain/review it before creating another snapshot")
    for name in RELEASE_FILES:
        if not (root / name).is_file() or (root / name).is_symlink():
            raise ValueError(f"Missing or unsafe release file: {name}")
    output.mkdir(parents=True)
    files = []
    for name in RELEASE_FILES:
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / name, destination)
        files.append({"path": name, "sha256": digest(destination), "bytes": destination.stat().st_size})
    manifest = {"version": load(root / "plugin/.claude-plugin/plugin.json")["version"],
                "status": "Allowlisted snapshot; staging does not perform publication or installation",
                "files": files, "excluded": ["source media", "transcripts", "model weights", "campaign records", "_system", "runtime caches"],
                "license_status": "Original plugin code; no additional license grant specified. No third-party skill code or binaries bundled."}
    save(output / "docs/release-manifest.json", manifest)
    return {"output": str(output), "files": len(files), "manifest": str(output / "docs/release-manifest.json")}


def render(spec_path, output):
    runtime = doctor()
    spec_path, output = Path(spec_path).resolve(), Path(output).resolve()
    receipt_path = output.with_suffix(".receipt.json")
    if output.exists() or receipt_path.exists():
        raise ValueError("Output or receipt already exists; choose a new revision filename")
    spec = load(spec_path)
    if not isinstance(spec.get("rights"), str) or not spec["rights"].strip():
        raise ValueError("Record permission evidence in rights before rendering")
    if type(spec.get("test_media")) is not bool:
        raise ValueError("Explicit test_media boolean required")
    source = (spec_path.parent / spec["source"]).resolve()
    if not source.is_file():
        raise ValueError("Source must be an accessible local media file")
    source_hash = digest(source)
    spec_hash = digest(spec_path)
    metadata = probe(source)
    if not any(s["codec_type"] == "video" for s in metadata["streams"]):
        raise ValueError("Source has no video stream")
    source_duration = float(metadata["format"]["duration"])
    clips = spec["clips"]
    if not isinstance(clips, list) or not 1 <= len(clips) <= 10:
        raise ValueError("Use 1-10 clips")
    duration = 0
    for clip in clips:
        start = number(clip["start"], "clip start", 0, source_duration)
        end = number(clip["end"], "clip end", 0, source_duration)
        if end <= start:
            raise ValueError("Clip end must follow start")
        duration += end - start
    duration = round(duration, 9)
    number(duration, "total duration", 1, 180)
    ass = subtitles(spec, duration)
    engine = spec.get("caption_engine", "auto")
    if engine == "auto":
        engine = runtime["caption_backends"][0]
    if engine not in runtime["caption_backends"]:
        raise ValueError("Requested caption engine is unavailable")
    resize = frame_filter(spec, metadata)
    audio = any(s["codec_type"] == "audio" for s in metadata["streams"])
    with tempfile.TemporaryDirectory(prefix="coach-render-", dir=output.parent) as directory:
        temporary = Path(directory)
        (temporary / "captions.ass").write_text(ass, encoding="utf-8")
        overlay = "subtitles=captions.ass"
        if engine == "drawtext":
            cues = [(cue["text"], cue["start"], cue["end"], spec.get("caption_size", 42), "h-190")
                    for cue in spec.get("captions", [])]
            if spec.get("hook"):
                wrapped = "\n".join(textwrap.wrap(spec["hook"], width=25))
                cues.append((wrapped, 0, spec.get("hook_seconds", 3), 48, "60"))
            if spec.get("cta"):
                wrapped = "\n".join(textwrap.wrap(spec["cta"], width=25))
                cues.append((wrapped, duration - spec.get("cta_seconds", 3), duration, 48, "60"))
            if spec.get("credit"):
                cues.append((spec["credit"], 0, duration, 28, "h-80"))
            if spec.get("notice"):
                cues.append((spec["notice"], 0, duration, 26, "h-10"))
            overlay = drawtext_overlay(cues, temporary)
        segments = []
        for index, clip in enumerate(clips):
            segment = temporary / f"clip-{index}.mp4"
            command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-protocol_whitelist", "file,pipe",
                       "-ss", str(clip["start"]), "-i", str(source), "-t", str(clip["end"] - clip["start"]),
                       "-map", "0:v:0", "-vf", resize + ",setsar=1,fps=30", "-c:v", "libx264",
                       "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p"]
            if audio:
                command += ["-map", "0:a:0", "-af", "aresample=48000,apad", "-c:a", "aac", "-b:a", "128k", "-ac", "2", "-shortest"]
            else:
                command += ["-an"]
            run(command + [str(segment)])
            segments.append(f"file '{segment.name}'")
        (temporary / "clips.txt").write_text("\n".join(segments), encoding="utf-8")
        rendered = temporary / "rendered.mp4"
        command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-f", "concat", "-safe", "1",
                   "-i", "clips.txt", "-vf", overlay, "-c:v", "libx264", "-preset", "veryfast",
                   "-crf", "21", "-pix_fmt", "yuv420p"]
        if audio:
            command += ["-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "128k"]
        run(command + ["-movflags", "+faststart", str(rendered)], cwd=temporary)
        if digest(source) != source_hash or digest(spec_path) != spec_hash:
            raise ValueError("Source or edit changed during render; retry from a stable input")
        result = probe(rendered)
        video = next(s for s in result["streams"] if s["codec_type"] == "video")
        if video["width"] != 720 or video["height"] != 1280 or abs(float(result["format"]["duration"]) - duration) > 0.25:
            raise ValueError("Rendered dimensions or duration failed verification")
        receipt = {"source_sha256": source_hash, "spec_sha256": spec_hash,
                   "output_sha256": digest(rendered), "duration": float(result["format"]["duration"]),
                   "width": 720, "height": 1280, "audio": audio, "test_media": spec["test_media"],
                   "rights": spec["rights"], "spec": spec,
                   "promise_sha256": spec.get("promise_sha256"),
                   "files": [{"path": os.path.relpath(source, output.parent), "sha256": source_hash},
                             {"path": os.path.relpath(spec_path, output.parent), "sha256": spec_hash},
                             {"path": output.name, "sha256": digest(rendered)}],
                   "caption_engine": engine,
                   "audio_processing": "loudnorm I=-16 TP=-1.5 LRA=11; AAC 48kHz stereo" if audio else "no source audio",
                   "verification": "encoding only; human playback and editorial acceptance required"}
        # Exclusive creation prevents an accidental overwrite of a competing revision.
        with output.open("xb") as destination, rendered.open("rb") as incoming:
            shutil.copyfileobj(incoming, destination)
        save(receipt_path, receipt)
    return {"output": str(output), "receipt": str(receipt_path),
            **{key: value for key, value in receipt.items() if key not in ("spec", "rights")}}


def transcribe(args):
    source, model, output = Path(args.source).resolve(), Path(args.model).resolve(), Path(args.output).resolve()
    if not shutil.which("whisper-cli") or not shutil.which("ffmpeg"):
        raise ValueError("Local transcription requires whisper-cli and FFmpeg on PATH; no API fallback or automatic install")
    if not source.is_file() or not model.is_file():
        raise ValueError("Source and an actual whisper.cpp GGML model file must exist")
    if model.stat().st_size < 10_000_000:
        raise ValueError("Model is too small for usable Whisper weights; test stubs are not transcription models")
    if output.exists():
        raise ValueError("Transcript already exists; choose a new output filename")
    start = number(args.start, "transcription start", 0, 86400)
    duration = number(args.duration, "transcription duration", 1, 600)
    source_hash = digest(source)
    model_hash = digest(model)
    with tempfile.TemporaryDirectory(prefix="coach-transcribe-", dir=output.parent) as directory:
        temporary = Path(directory)
        audio = temporary / "audio.wav"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-protocol_whitelist", "file,pipe",
             "-ss", str(start), "-i", str(source), "-t", str(duration), "-map", "0:a:0", "-ar", "16000",
             "-ac", "1", "-c:a", "pcm_s16le", str(audio)])
        run(["whisper-cli", "-m", str(model), "-f", str(audio), "-l", args.language, "-oj",
             "-of", str(temporary / "transcript"), "-ml", "64", "-sow", "-np"])
        raw = load(temporary / "transcript.json")
        segments = []
        for segment in raw["transcription"]:
            begin = number(segment["offsets"]["from"] / 1000, "segment start", 0, duration + 30)
            end = number(segment["offsets"]["to"] / 1000, "segment end", begin, duration + 30)
            begin, end = min(begin, duration), min(end, duration)
            text = segment["text"].strip()
            if text and end > begin:
                segments.append({"start": round(start + begin, 3), "end": round(start + end, 3), "text": text})
        if not segments:
            raise ValueError("No recognized speech; do not invent captions")
        if digest(source) != source_hash or digest(model) != model_hash:
            raise ValueError("Source or model changed during transcription")
        result = {"source_sha256": source_hash, "model_sha256": model_hash, "engine": "whisper.cpp whisper-cli",
                  "language": args.language, "offset": start, "requested_duration": duration,
                  "status": "machine transcript; words and timing require listening verification",
                  "segments": segments}
        with output.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    return {"output": str(output), "segments": len(segments), "status": result["status"]}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def validate_resources(content, directory):
    for resource in content.get("files", []):
        path = directory / resource["path"]
        if digest(path) != resource["sha256"]:
            raise ValueError(f"Referenced file changed: {resource['path']}")


def current_artifact(state, stage, directory, approved=False):
    artifact = state["artifacts"].get(stage)
    if not artifact or artifact.get("stale"):
        raise ValueError(f"Missing or stale prerequisite: {stage}")
    artifact_path = directory / artifact["path"]
    if digest(artifact_path) != artifact["file_sha256"]:
        raise ValueError(f"Artifact file changed outside the ledger: {stage}; set and reapprove it")
    validate_resources(load(artifact_path), artifact_path.parent)
    dependencies = {name: current_artifact(state, name, directory, approved)["token"]
                    for name in DEPENDENCIES[stage]}
    if dependencies != artifact["dependencies"]:
        raise ValueError(f"Dependency snapshot changed: {stage}")
    expected = fingerprint({"file_sha256": artifact["file_sha256"], "dependencies": dependencies})
    if expected != artifact["token"]:
        raise ValueError(f"Invalid artifact snapshot: {stage}")
    if approved and state["approvals"].get(stage, {}).get("token") != expected:
        raise ValueError(f"Current prerequisite approval required: {stage}")
    return artifact


def descendants(stage):
    found = {stage}
    for candidate in STAGES:
        if any(dependency in found for dependency in DEPENDENCIES[candidate]):
            found.add(candidate)
    return found


def state_command(args):
    path = Path(args.state)
    if args.command == "init":
        if path.exists():
            raise ValueError("Campaign already exists; resume it")
        state = {"version": 2, "revision": 0, "status": "active", "artifacts": {}, "approvals": {}, "actions": {}, "history": []}
    else:
        state = load(path)
        if state["version"] != 2 and args.command != "show":
            raise ValueError("Legacy ledger cannot authorize actions; retain it and initialize a version-2 ledger")
    if args.command == "set":
        if state["status"] != "active":
            raise ValueError("Campaign stopped; explicit resume required")
        artifact_path = Path(args.file).resolve()
        artifact = load(artifact_path)
        validate_resources(artifact, artifact_path.parent)
        dependencies = {name: current_artifact(state, name, path.parent)["token"]
                        for name in DEPENDENCIES[args.stage]}
        if args.stage == "edit" and "output_sha256" in artifact:
            if artifact.get("source_sha256") != state["artifacts"]["source"]["content"].get("source_sha256"):
                raise ValueError("Rendered media does not match the current source artifact")
            if artifact.get("promise_sha256") != state["artifacts"]["promise"]["file_sha256"]:
                raise ValueError("Render receipt must bind the current promise file hash")
        file_hash = digest(artifact_path)
        token = fingerprint({"file_sha256": file_hash, "dependencies": dependencies})
        if state["artifacts"].get(args.stage, {}).get("token") != token or state["artifacts"].get(args.stage, {}).get("stale"):
            state["revision"] += 1
            state["artifacts"][args.stage] = {"sha256": fingerprint(artifact), "content": artifact, "stale": False,
                                             "path": os.path.relpath(artifact_path, path.parent.resolve()),
                                             "file_sha256": file_hash, "dependencies": dependencies, "token": token}
            for dependent in descendants(args.stage):
                state["approvals"].pop(dependent, None)
                if dependent != args.stage and dependent in state["artifacts"]:
                    state["artifacts"][dependent]["stale"] = True
            state["history"].append({"revision": state["revision"], "changed": args.stage})
    elif args.command == "approve":
        if state["status"] != "active" or args.stage not in state["artifacts"] or not args.by.strip():
            raise ValueError("Approval requires an active campaign, existing artifact and coach name")
        artifact = current_artifact(state, args.stage, path.parent)
        for dependency in DEPENDENCIES[args.stage]:
            current_artifact(state, dependency, path.parent, approved=True)
        state["approvals"][args.stage] = {"sha256": artifact["sha256"], "by": args.by,
                                         "token": artifact["token"], "dependencies": artifact["dependencies"]}
    elif args.command == "action":
        if args.stage not in ("delivery", "review"):
            raise ValueError("External actions require delivery or review approval, not source/edit approval")
        prior = state["actions"].get(args.key)
        if args.result == "pending":
            if state["status"] != "active" or prior:
                raise ValueError("Stopped campaign or previously recorded action; reconcile, do not retry")
            artifact = current_artifact(state, args.stage, path.parent, approved=True)
            state["actions"][args.key] = {"status": "pending", "stage": args.stage,
                                         "token": artifact["token"], "dependencies": artifact["dependencies"]}
        else:
            if not prior or prior["status"] not in ("pending", "unknown") or not args.evidence.strip():
                raise ValueError("Reconciliation needs pending/unknown action and evidence")
            prior.update(status=args.result, evidence=args.evidence)
    elif args.command == "stop":
        state["status"] = "stopped"
        state["approvals"] = {}
    elif args.command == "resume":
        state["status"] = "active"
    if args.command != "show":
        save(path, state)
    return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor")
    commands.add_parser("resources", help="Verify and resolve resources beside this installed helper; no environment variable required")
    edit = commands.add_parser("render")
    edit.add_argument("spec")
    edit.add_argument("output")
    poster = commands.add_parser("cover", help="Create a standalone cover without transient subtitles")
    poster.add_argument("spec")
    poster.add_argument("output")
    bundle = commands.add_parser("release", help="Stage only allowlisted Git marketplace files; no Git/network operations")
    bundle.add_argument("output")
    speech = commands.add_parser("transcribe", help="Optional local Whisper adapter; requires existing model weights")
    speech.add_argument("source")
    speech.add_argument("output")
    speech.add_argument("--model", required=True)
    speech.add_argument("--start", type=float, default=0)
    speech.add_argument("--duration", type=float, default=180)
    speech.add_argument("--language", default="en")
    for name in ("init", "show", "set", "approve", "stop", "resume", "action"):
        command = commands.add_parser(name)
        command.add_argument("state")
        if name in ("set", "approve", "action"):
            command.add_argument("--stage", choices=STAGES, required=True)
        if name == "set":
            command.add_argument("--file", required=True)
        if name == "approve":
            command.add_argument("--by", required=True)
        if name == "action":
            command.add_argument("--key", required=True)
            command.add_argument("--result", choices=("pending", "unknown", "confirmed", "failed"), required=True)
            command.add_argument("--evidence", default="")
    args = parser.parse_args()
    try:
        if args.command == "doctor":
            result = doctor()
        elif args.command == "resources":
            result = resources()
        elif args.command == "render":
            result = render(args.spec, args.output)
        elif args.command == "transcribe":
            result = transcribe(args)
        elif args.command == "cover":
            result = cover(args.spec, args.output)
        elif args.command == "release":
            result = release(args.output)
        else:
            result = state_command(args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"Coach Content: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
