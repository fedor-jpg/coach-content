# Maintainer Notes

Local Git marketplace package, version 0.2.0. One start command and three skills.
This package creates and revises actual MP4 files when the host provides its required media tools.
It does not install tools, publish Reels, send messages, or create services.

## Coach entry

Installation repository: https://github.com/fedor-jpg/coach-content

1. Open Customize > Plugins > Add plugin > Add marketplace > Add from a repository.
2. Enter `https://github.com/fedor-jpg/coach-content`.
3. Select Sync.
4. Install Coach Content from that marketplace.
5. Run `/coach-content:start` with a permitted recording and programme context.

The UI route was inspected by the main task. This package has not been installed on an independent account.
Public plugin-code distribution was authorized on 2026-10-30. This does not establish native installation or product acceptance.
Do not use the private development repository as the coach's distribution.
Distribute only the allowlisted marketplace, plugin, documentation and tests.
Exclude `docs/artifacts`, `_system`, runtime caches and private campaign media from distribution.
The marketplace uses `./plugin`; copy the directory contents intact to the future Git repository root.

## Runtime

The assistant, not the coach, executes the included Python helper in the host's native environment.
Python 3.10+, FFmpeg with libx264/AAC and either libass subtitles or drawtext, and ffprobe must already be available on PATH.
`doctor` reports missing capabilities without installing anything. No API keys, LLM endpoints or third-party Python modules are required.
The default FFmpeg on the development Mac lacks libass. A separate already-installed full FFmpeg build is used for media tests.
That local build does not establish availability in Cowork. Native execution and native artifact return remain integration gates.

Optional `transcribe` uses an existing whisper-cli executable and an explicitly supplied real GGML model.
It extracts a bounded audio window and writes source-aligned machine transcript segments without a network API.
It never downloads weights or treats transcript text as verified subtitles. Caption endpoint failure does not block video editing.
The main task's native Claude probe found Ubuntu 24.04, Python 3.13.18 and FFmpeg 6.1.1 with drawtext.
It found no speech-recognition runtime, and model hosts were unavailable behind the host proxy.
Do not bypass those restrictions or disguise model files. Supply an allowed transcript or supported native understanding instead.
Developer-local transcription is component evidence only. It does not establish fresh-account speech support.
The demonstrated branch uses actual video plus a supplied transcript.
Native Claude opened the YouTube page and license, but its transcript panel remained loading for more than 40 seconds.
That route is stopped. The main task's successful ordinary Chrome export is assisted setup, not autonomous native-Claude proof.
YouTube-link-only input remains unsupported in the verified path. Do not retry the same stalled route or use a bypass.

## Maintainer checks

Run `python3 tests/test_coach.py -v` with a compatible FFmpeg on PATH.
Run `python3 tests/test_coach.py --demo-output docs/artifacts/generated-mechanical-test` to produce clearly labeled generated fixtures.
Use a new empty output folder. Render refuses existing output filenames.
The test fixture includes an actual encode, two-excerpt join, burned captions, audible tone, changed edit, changed hash and approval invalidation.
Its recorded natural-language request maps to an explicit changed specification; it is not a model-mediated conversation test.

Use `python3 plugin/scripts/coach.py release OUTPUT_FOLDER` to stage an allowlisted Git marketplace tree.
This copies code, skills, the two manifests, concise coach instructions, maintainer notes and focused tests.
It writes docs/release-manifest.json with sizes and SHA-256 values. It excludes source media, transcripts, weights and campaign data.
It performs no Git operation, network call or installation. The destination must not exist.
This release's public repository creation and push are authorized. Main/Astra owns native installation and acceptance separately.

Ledger version 2 uses the DAG source -> promise -> edit -> delivery -> review.
Artifact and referenced file hashes are checked at approval and before pending external actions.
Promise changes invalidate an edit that embeds its CTA. A fresh delivery cannot hide stale prerequisites.
Old ledgers are readable history only; they cannot authorize actions. Rebuild their artifacts in DAG order.
Keep campaign files in the existing authorized native Project/Work in a folder location, not /tmp.
If no workspace exists, make one native location selection an explicit setup step. Do not broaden file permissions.
Native persistence and resumption remain unverified. Local files do not imply upload or cross-device access.
Sources: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
and https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps .

No third-party skill code or video is bundled in the plugin. Editorial examples are original.
FFmpeg is an external host dependency, not a redistributed binary. Rights to each source remain separate from plugin code.
The package does not claim that an instruction rubric improves quality until the planned blind comparisons run.

## Acceptance boundaries

Local mechanical media and state tests are separate from native installation, coach usability, real-source editorial acceptance and live delivery.
The current checked Chatfuel catalogue lacks a Reel publisher. New-file transfer into Chatfuel remains unverified.
The delivery skill prepares a useful text benefit and defines approval, readback, recipient testing and shutdown.
It does not fabricate missing connector operations. Full G0-G5 acceptance remains open.
Booking and closed-client background review are separately unimplemented branches.

Architecture follows Anthropic's [plugin authoring guidance](https://code.claude.com/docs/en/plugins) and
[Git marketplace guidance](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).
Documentation support does not prove installation of this package.

## Current preview and native boundary

Clean preview assets retain source credit. Adjacent review.txt and campaign state retain timing, listening and approval limits.
Clean appearance does not imply publication approval. Caption and handoff retain synthetic-programme disclosure.
The native Commons download failed at the gateway with CONNECT403; no source downloaded. That route is stopped.
A separate native synthetic two-second H264/AAC file appeared in the file viewer, readyState4 and duration2.
That proves mechanical generation/viewing only, not source intake, this helper, installation or independent download verification.
Provided-file input remains a separate untested branch. Broad file-URL upload permission remains off.
