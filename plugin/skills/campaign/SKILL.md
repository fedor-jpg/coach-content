---
name: campaign
description: Guides a coach content campaign from source selection through edits, approvals, resumption and test shutdown.
---

# Campaign

Deliver one selected Reel and one matching next step. An MP4 is a content milestone, not a launched funnel.

## Start or resume

1. Locate this installed plugin from actual paths in the host's skill/plugin catalogue or native file tools. If unavailable, use a nonempty CLAUDE_PLUGIN_ROOT as a candidate, not an assumption. Inspect `.claude-plugin/plugin.json` for name `coach-content` and agreement with the installed version. Run the located helper's `resources` command by its actual absolute path; use the verified returned paths for skills and subsequent commands. Missing or mismatched resources stop helper execution; do not search unrelated folders or invent a path.
2. Use the existing authorized native Project or Work in a folder location. If absent, ask once to select it. A Project may be document storage, not a filesystem directory. Use the matching persistence branch below. Read existing brief.json and campaign.json before `init` or questions. Report known context, files, approvals, unresolved actions and next step. Missing read permission is not evidence that either document is absent.
3. Immediately preserve the supplied context in brief.json, independently of media availability and source approval. Merge only explicitly supplied new facts into the existing brief; retain other known facts, including supplied demo/test-only status in intent or limits. When the video will arrive later, take the waiting branch below before further questions or checks. Otherwise ask once for only genuinely missing audience, programme, source reference/rights statement, language, intent or limits. Never re-ask known facts merely because media has not arrived. Accept an existing material URL as a delivery branch; do not force a PDF.
4. Run `doctor` with the resolved absolute helper path in native execution. Missing Python, FFmpeg, ffprobe, H.264/AAC encoding or both libass and drawtext is an explicit rendering limit. Do not install software or use a paid API without permission. Continue editorial work independently.
5. Check that the environment can read actual media bytes and return generated files in chat. A video webpage is not a downloaded video. Do not claim installation or transfer from a developer-local test.
6. Use the video skill for source selection and edits. Use the delivery skill after the promise and content are coherent.

The assistant runs all helper commands as `python3` followed by the verified absolute helper path and arguments. Do not rely on shell variables surviving between tool calls. Never use a developer home directory. JSON media paths resolve relative to the edit specification, not the shell directory.

### When the video will come later

If the user explicitly says they will provide the recording later and has not requested source selection, take this branch immediately after reading/saving the brief. Verify its hidden native readback; run at most one necessary environment check, reusing an unchanged verified result. Do not start caption, ASR, browser/network discovery, downloads, rehosting or media-persistence attempts. Do not create source-check documents, promise drafts, clip candidates or other technical output cards. Do not select a CTA/keyword/DM or ask for their approval before selecting the source clip. Do not ask known programme/audience/language questions again or make a full intake questionnaire a prerequisite for waiting. Retain an explicitly supplied educational/demo label and test-only limits without asking whether to apply them again. Reply in two or three short sentences: known inputs and one next required action, provide the recording when ready. Omit filenames, ledger revisions, hashes, tool counts and character budgets unless requested. State only a necessary blocker; do not promise background work. Stop the turn. Continue the normal content-first branch only when media arrives or the user explicitly requests source selection. This does not remove candidate, hook, quality or delivery criteria from that later branch.

## Native persistence

Keep one small brief.json alongside the ledger. Use this shape with supplied values instead of null; null means unknown, not permission:

```json
{
  "audience": null,
  "programme": null,
  "source_reference": null,
  "rights_statement": null,
  "language": null,
  "intent": null,
  "limits": null
}
```

The brief records user-supplied context, not verified rights, media bytes, source approval or authorization to publish/send. Do not put full chats, private customer records or credentials in it. Save and verify brief.json as soon as facts arrive, even with an empty ledger. Do not force it into the source stage or invent a media hash. On resume, restore it before questions; distinguish known brief facts from unavailable source/transcript bytes. If a changed brief affects an existing approved source, promise or delivery, stop local actions and revalidate affected stages before new approval. The brief never overrides the ledger.

For an authorized filesystem folder, verify read/write access and keep campaign.json, supporting artifacts and renders together outside the plugin. Do not silently use /tmp as durable storage.

For a document-backed Project, discover its actual available native read/write operations and schemas; do not invent tool names. Read existing JSON/text documents into a working directory accessible to native execution, preserving exact UTF-8 bytes and relative paths. This directory is a working copy, not the durable Project. Run `show` on the recovered campaign and verify referenced artifacts/media before approvals or actions. `show` alone does not validate dependencies. Initialize only after confirming no existing campaign.

The tested Project writer creates or replaces text documents only. Briefs, ledgers, specifications, receipts and media pointers can use that branch. Binary Project items are user uploads and are read-only to the tested Project tools. A separate native private Artifact branch is permitted below when the host exposes it; text storage alone proves no binary capability. If required source/output bytes cannot be read and their hashes revalidated, stop affected approvals and external actions explicitly. Do not present coach downloads/uploads as a frictionless substitute, or encode media into text to bypass this boundary.

After a change, write changed JSON/text dependencies first and campaign.json last through the authorized Project operation. Read each document back and compare its UTF-8 SHA-256 with the working file. Preserve the previous state if readback differs or any write fails; report persistence incomplete and block external actions. Before overwriting an existing document, compare its current content with the version read earlier; stop on concurrent changes. This is not an atomic transaction or send lock. Do not store secrets or binary/base64 media as text documents.

Keep briefs, ledgers, source checks, specifications, receipts and internal text out of coach-facing file outputs. Use the native execution tool for working-copy JSON/text if a file-writing tool auto-presents cards. For durable Project writes, use present_to_user=false only when the actual schema exposes it; never invent a visibility parameter. If no hidden supported write exists, report that limit rather than flooding the conversation with internal files. Present the Reel, cover, caption and useful benefit when available, with a short status summary; do not show raw ledgers unless requested.

On resume, reconstruct the working copy from Project documents, not remembered local paths. Verify referenced file hashes and actual binary availability. JSON readback does not prove media transfer or cross-device access. If source/output bytes are unavailable, preserve state and report the media gap; do not rebind approvals to missing files. Use only the host's already-authorized transfer capabilities, never another connector or hidden API. Local desktop files are not automatically uploaded. Native tests verified text-ledger recovery and a separate small synthetic MP4 private Artifact recovery in a second session. Neither proves a complete campaign or arbitrary source-video recovery.

## Private native media

Use only an already-available native Artifact tool whose actual schema supports private binary files of the current type and size. Verify private/Only you visibility; never force public sharing. The tested files scope works; assets scope is unavailable and must not be used. The observed schema allows standard web file types up to 15 MB. Check the current schema and exact byte limit before writing; use 15000000 bytes conservatively if only 15 MB is stated. Do not split oversized files, encode binaries into text, add storage/connectors, or bypass network policy. An oversized or inaccessible source remains an explicit gap.

For each permitted file, record its byte count and SHA-256, write through the real native operation, then read its binary bytes back and compare both. A link, preview or successful write alone is insufficient. Only after equality and private visibility are verified, save a pointer in media-locations.json through the Project text branch, with readback verification. Keep this sidecar separate from hashed stage JSON and the current session's absolute scratch path. A pointer is a locator, not approval or a substitute for source bytes. Use this shape with verified host-returned values; null fields are incomplete and cannot authorize recovery:

```json
{
  "items": [
    {
      "workspace_path": "media/reel.mp4",
      "artifact_url": null,
      "artifact_path": null,
      "artifact_version": null,
      "sha256": null,
      "bytes": null,
      "visibility": "private"
    }
  ]
}
```

On resume, read the pointer from the authorized Project, then use native Artifact read with its recorded URL/path and version when supported. Do not assume a version selector exists: if only current-file read is available, require saved hash/size equality and disclose that historical version selection was not verified. If a listed version changes, do not silently replace the pointer or expected hash. Never treat a private Artifact URL as a subscriber-accessible link.

Recover into a fresh execution working copy under the recorded workspace-relative path, not the old absolute session directory. Reject absolute paths, parent traversal and symlink escapes in workspace_path. Confirm the path agrees with the stage's file references. Preserve the directory structure: source/spec paths resolve relative to their owning JSON file, not necessarily campaign.json. Restore exact JSON bytes without formatting, rewriting paths or inserting Artifact URLs into edit specs/receipts. New campaigns must place accessible media, specs and outputs inside their working root before hashing. If legacy paths leave that root, stop automatic recovery and explain the required revalidation; do not rewrite approved records silently.

Revalidate all referenced source and output bytes, not only the finished Reel, before approvals or external actions. A restored output with a missing source is still incomplete. Failed reads, wrong versions with unmatched bytes, size/hash mismatch or missing files keep those operations blocked and preserve prior evidence. Native persistence is separate from coach-facing file return, publication and subscriber delivery. The observed proof is only a private synthetic two-second, no-audio MP4 recovered across sessions; real-source intake/render and arbitrary large-video persistence remain unproven.

## State and approvals

The helper's CLI is documented by `--help` and subcommand `--help`. Use `set --stage STAGE --file FILE` to record a JSON artifact, its file hash and current prerequisite tokens. The acyclic order is source -> promise -> edit -> delivery -> review. Select source and excerpts first; draft the actual benefit and CTA before rendering the edit that embeds them. Promise depends on source, not on edit. This avoids a dependency cycle.

Store source media SHA-256 and rights evidence in source. Declare actual input files as `files: [{"path": "source.mp4", "sha256": "..."}]`, relative to that artifact. Set source_sha256 in source. Put the promise artifact's actual file SHA-256 in the edit specification as promise_sha256 before rendering. Edit receipts bind that promise, source bytes, specification and rendered media. Store exact account, post, recipient and message in delivery/review, not generic consent. Relative paths resolve from campaign.json or its artifact, never from a developer directory.

Run `approve --stage STAGE --by COACH` only after explicit coach approval. The helper rechecks prerequisite artifacts, dependency snapshots, artifact file hashes and referenced files. Approve prerequisites in DAG order. Pending external actions require approval of the entire current dependency chain, not just delivery. A file mutation outside the ledger blocks both approval and pending actions. Source changes invalidate all approvals. Promise changes invalidate edit, delivery and review because the Reel embeds its CTA. Edit changes preserve promise but invalidate delivery/review. A new subscriber answer changes review.

After a change, regenerate or explicitly revalidate dependent artifacts in DAG order with `set`, then obtain fresh approvals. An unchanged artifact can be explicitly rebound only when its prerequisites are current; rendered receipts must also match source and promise hashes. Version-1 ledgers cannot authorize actions; retain them as history and start a version-2 ledger. The helper remains a local ledger, not an atomic remote send lock. Never claim it prevents concurrent remote changes.

Translate a natural-language revision into a changed edit specification. Example: "Keep the qualification and make captions larger" means extend the selected range to include the qualification and increase caption_size. Render a new file, show it, record it with `set`, and state which approvals changed. Do not merely rename the old video. After two ordinary revision rounds recommend one version; unresolved errors still block approval.

## Stop and recovery

After two attempts with no new evidence, stop that approach and record the exact missing transition. Continue independent useful work. Never silently replace native transfer with coach downloads/uploads.

Before a permitted external action, record its scoped action key as `pending` with `action`. Unknown outcomes become `unknown`; inspect remote history before reconciling to confirmed or failed. Never retry pending, unknown or confirmed keys. A confirmed action is not proof of subscriber receipt.

On "stop", first run `stop` to block new local actions. Then, only within authorized scope, disable this campaign's remote test rule and read back its status. Stop any separately authorized native schedule and verify it separately. Test that a control comment produces no new reply. Record remaining remote cleanup if tools or permissions are missing. Local `stopped` does not mean remote rules are disabled or messages recalled. `resume` requires a new explicit coach request and does not restore approvals.

End each update with the current artifact, verified result and next decision. Do not promise background work, booking or publication without the corresponding tested host capability.
