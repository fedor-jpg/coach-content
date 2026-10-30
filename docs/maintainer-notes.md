# Maintainer Notes

Git marketplace package, version 0.2.3. One start command and three skills.
This package creates and revises actual MP4 files when the host provides its required media tools.
It does not install tools, publish Reels, send messages, or create services.

## Coach entry

Installation repository: https://github.com/fedor-jpg/coach-content

1. Open Customize > Plugins > Add plugin > Add marketplace > Add from a repository.
2. Enter `https://github.com/fedor-jpg/coach-content`.
3. Select Sync.
4. Install Coach Content from that marketplace.
5. Run `/coach-content:start` with a permitted recording and programme context.

The main task installed through version0.2.2 in Claude web and exercised real provided-file rendering and fresh-session revision.
Public plugin-code distribution was authorized on 2026-10-30. Reviewed version0.2.3 is approved for publication; full product acceptance remains open.
Do not use the private development repository as the coach's distribution.
Distribute only the allowlisted marketplace, plugin, documentation and tests.
Exclude `docs/artifacts`, `_system`, runtime caches and private campaign media from distribution.
The marketplace uses `./plugin`; retain the directory structure at the Git repository root.

## Runtime

The assistant, not the coach, executes the included Python helper in the host's native environment.
Python 3.10+, FFmpeg with libx264/AAC and either libass subtitles or drawtext, and ffprobe must already be available on PATH.
`doctor` reports missing capabilities without installing anything. No API keys, LLM endpoints or third-party Python modules are required.
The default FFmpeg on the development Mac lacks libass. A separate already-installed full FFmpeg build is used for media tests.
That local build does not establish availability in Cowork. The main task separately verified installed helper doctor exit0 with native Python3.13.18 and FFmpeg6.1.1.
Version0.2.0 initially failed because CLAUDE_PLUGIN_ROOT was unset. Claude recovered using its actual installed plugin path.
Version0.2.1 discovers host-exposed locations first and accepts a nonempty environment path only as a fallback candidate.
The main task verified actual installed0.2.1 resource discovery with the root variable empty and a hash-identical native brief write/read.
The helper's resources command verifies the adjacent manifest and required files, then returns absolute paths without environment dependence.
This is resource validation, not a filesystem search or proof of binary input/output support.

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
Use the existing authorized native folder or document-backed Project. Do not silently use /tmp as durable storage.
Document-backed Projects require actual native read/write operations and a separate execution working copy.
Prefer one complete private native Artifact snapshot and one Project locator, not separate writes for each stage.
Verify every file and the dependency chain before advancing the locator; retain the previous snapshot on failure.
The tested present_to_user=false still produced internal cards. One locator write may show one card; hiding is not guaranteed.
If no workspace exists, make one native location selection an explicit setup step. Do not broaden file permissions.
Native JSON write/read was byte-identical and helper show passed. A second session recovered the same empty ledger without initialization or replacement.
Version0.2.1 also saves a minimal brief.json before media arrives, independently of source approval. Resume reads it before asking for missing facts.
The brief contains supplied audience, programme, source reference, rights statement, language, intent and limits; no complete chat or customer records.
It grants no authorization and supplies no verified media evidence. Native0.2.2 brief/state recovery passed; the new0.2.3 snapshot-plus-locator route remains unverified.
On resume, read the Project locator and restore the complete snapshot with exact relative paths and JSON bytes. Missing media remains a blocker.
Local files do not imply upload or cross-device access. Do not serialize binaries into text documents to bypass transfer limits.
The tested Project writer accepts text only; binary Project uploads are read-only to those tools. A separate native private Artifact binary branch is available as described below.
Missing referenced media blocks affected approvals and pending external actions even when the text ledger restores successfully.
Sources: https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
and https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps .

No third-party skill code or video is bundled in the plugin. Editorial examples are original.
FFmpeg is an external host dependency, not a redistributed binary. Rights to each source remain separate from plugin code.
The package does not claim that an instruction rubric improves quality until the planned blind comparisons run.

## Acceptance boundaries

Local mechanical media and state tests are separate from native installation, coach usability, real-source editorial acceptance and live delivery.
The local brief test round-trips actual JSON/text and checks unchanged empty approvals. It is not a native Project or conversational acceptance test.
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
The provided-file branch rendered a licensed short source, recovered it in a fresh session and revised the hook while preserving source and decoded audio.
Direct MP4 playback and a downloaded H264/AAC720x1280,30fps,12.921-second file were verified. Artifact HTML preview failure does not block direct MP4 use.
Timing, layout and overall quality remain pending. Broad file-URL upload permission was restored off.

## Private Artifact persistence

The native Artifact files scope saved a private synthetic two-second MP4 and read it in an independent session.
Hash and byte count matched; ffprobe identified H264,720x1280,7361bytes,no audio. This is mechanical evidence, not real coach content or delivery.
The assets scope failed and must not be used. The observed schema permits standard web files up to15MB; inspect current schema before use.
Native multi-file readback also preserved JSON and TXT bytes and nested paths, with one Artifact card and no independent JSON/TXT cards.
Version0.2.3 prefers a complete private snapshot with snapshot.json listing all payload paths, hashes and sizes, including original source and stage dependencies.
One Project locator stores Artifact URL/version and index path/hash; it is advanced only after complete readback verification.
The new snapshot retains the previous locator, and the old Artifact is not modified. Current session scratch paths are not durable locations.
Receipts and stage JSON remain byte-identical during recovery; their relative references must resolve in the recreated working tree.
If a version selector is absent, do not claim historical version selection. Require saved bytes/hash equality before use.
Missing source bytes still block approvals/actions even when the finished Reel is restored. Private links are not recipient-accessible delivery URLs.
No binary-as-text encoding, splitting oversized files, public-share requirement, new connector or network-policy workaround is allowed.
Arbitrary large-source ingestion, the new snapshot-plus-locator route and full-flow acceptance remain unverified.

## Explicit video-later branch

When the coach says the video will arrive later without asking for source selection, save and verify the brief, then stop.
Reuse verified environment evidence or make one necessary check. Do not start captions, ASR, network searches or technical draft cards.
Internal working text uses native execution if the file-writing tool auto-presents cards. Do not rely on a hidden-write flag to prevent native cards.
Respond with known inputs and the one next action, not repeated questions or a technical intake screen.
Preserve already-supplied demo/test-only status. Do not select or request approval of CTA/DM copy before source selection.
Main tests this conversational behavior in the native host; local file tests do not establish that acceptance.

## Revision quality

A hook revision regenerates the matching cover and refreshes the post caption by default, preserving the previous complete version.
No extra question is needed for these dependent assets. Unchanged source/audio requests retain ranges/settings and compare decoded audio.
Energy, silence, syllable and word-count heuristics do not verify subtitle timing. Without a proven capability or verified cues, render an uncaptioned preview and keep acceptance pending.
Check phone-size safe zones. Report unrepairable layout collisions honestly; do not remove required credit or claim platform readiness.
