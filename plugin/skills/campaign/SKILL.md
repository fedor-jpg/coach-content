---
name: campaign
description: Guides a coach content campaign from source selection through edits, approvals, resumption and test shutdown.
---

# Campaign

Deliver one selected Reel and one matching next step. An MP4 is a content milestone, not a launched funnel.

## Start or resume

1. Locate this installed plugin from actual paths in the host's skill/plugin catalogue or native file tools. If unavailable, use a nonempty CLAUDE_PLUGIN_ROOT as a candidate, not an assumption. Inspect `.claude-plugin/plugin.json` for name `coach-content` and agreement with the installed version. Run the located helper's `resources` command by its actual absolute path; use the verified returned paths for skills and subsequent commands. Missing or mismatched resources stop helper execution; do not search unrelated folders or invent a path.
2. Use the existing authorized native Project or Work in a folder location. If absent, ask once to select it. A Project may be document storage, not a filesystem directory. Use its locator to restore the verified private snapshot, or read legacy campaign documents when no locator exists. Read brief.json and campaign.json before `init` or questions. Report known context and next step without internal file cards. Missing read permission is not evidence that a campaign is absent.
3. Immediately preserve the supplied context in brief.json, independently of media availability and source approval. Merge only explicitly supplied new facts into the existing brief; retain other known facts, including supplied demo/test-only status in intent or limits. When the video will arrive later, take the waiting branch below before further questions or checks. Otherwise ask once for only genuinely missing audience, programme, source reference/rights statement, language, intent or limits. Never re-ask known facts merely because media has not arrived. Accept an existing material URL as a delivery branch; do not force a PDF.
4. Run `doctor` with the resolved absolute helper path in native execution. Missing Python, FFmpeg, ffprobe, H.264/AAC encoding or both libass and drawtext is an explicit rendering limit. Do not install software or use a paid API without permission. Continue editorial work independently.
5. Check that the environment can read actual media bytes and return generated files in chat. A video webpage is not a downloaded video. Do not claim installation or transfer from a developer-local test.
6. Use the video skill for source selection and edits. Use the delivery skill after the promise and content are coherent.

The assistant runs all helper commands as `python3` followed by the verified absolute helper path and arguments. Do not rely on shell variables surviving between tool calls. Never use a developer home directory. JSON media paths resolve relative to the edit specification, not the shell directory.

### When the video will come later

If the user explicitly says they will provide the recording later and has not requested source selection, take this branch immediately after reading/saving the brief. Verify its persisted readback; run at most one necessary environment check, reusing an unchanged verified result. Do not start caption, ASR, browser/network discovery, downloads, rehosting or media-storage attempts. Do not create source-check documents, promise drafts, clip candidates or other technical output cards. Do not select a CTA/keyword/DM or ask for their approval before selecting the source clip. Do not ask known programme/audience/language questions again or make a full intake questionnaire a prerequisite for waiting. Retain an explicitly supplied educational/demo label and test-only limits without asking whether to apply them again. Reply in two or three short sentences: known inputs and one next required action, provide the recording when ready. Omit filenames, ledger revisions, hashes, tool counts and character budgets unless requested. State only a necessary blocker; do not promise background work. Stop the turn. Continue the normal content-first branch only when media arrives or the user explicitly requests source selection. This does not remove candidate, hook, quality or delivery criteria from that later branch.

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

For a document-backed Project, prefer one complete private native Artifact snapshot plus one Project locator. The verified native files scope preserves MP4, JSON and TXT bytes and relative paths together. Discover current schemas; do not invent tool names, parameters or filesystem access. The Project is document storage, not the execution directory. Read its locator and restore the snapshot before questions or init. For an older campaign, read its existing Project documents/media pointers without deleting or rewriting them; migrate only after complete snapshot verification.

Keep internal working files in native execution, not auto-presenting WriteFile cards. Do not write each stage to the Project. present_to_user=false did not prevent cards in the tested host; it is not a hiding guarantee. The preferred branch makes at most one Project locator write per completed checkpoint, which may still show one card. Return the actual Reel/cover/caption as coach-facing outputs; do not require an Artifact HTML preview to load.

## Private campaign snapshot

1. Check the actual native files schema supports every required file type, private/Only you visibility, and current per-file/total limits. The observed per-file limit is15MB; use15000000bytes conservatively if no exact byte value is supplied. The assets scope is unavailable. No public sharing, splitting, binary-as-text encoding, new connector or policy bypass is allowed. Unsupported or missing dependencies block a complete snapshot; do not silently fall back to many stage-document writes or coach file shuttling.
2. Freeze a working-copy checkpoint. Include brief, ledger, stage JSON, edit specs, receipts, source/transcript, matching Reel/cover/caption and other referenced files that exist for this campaign. Preserve original source bytes and previous versions. Before media arrives, brief plus an empty ledger is valid; do not invent source evidence. Keep exact JSON bytes and relative directory structure. Do not rewrite hashed records, insert host URLs into them or flatten paths. Omit full chats, unrelated files and secrets.
3. Create snapshot.json listing each payload path, byte count and SHA-256; exclude the index itself. Retain the previous Project locator in its previous_locator field. Store this metadata outside the stage approval graph. Use the following shape with real complete values, not null placeholders:

```json
{
  "files": [{"path": "campaign.json", "sha256": null, "bytes": null}],
  "previous_locator": null
}
```

4. Write a new private Artifact containing that index and all payload files. Do not modify the currently pointed-to snapshot: version labels alone do not prove old-version reads work. Retain the previous Artifact and locator on any failure. Read every new file back through native operations, compare size/hash, verify private visibility and completeness against the ledger's recursive file dependencies, including original source. A link, preview or successful write is insufficient. Changed working files require a fresh checkpoint; do not advance a locator over mixed versions.
5. Only after complete verification, update the single campaign locator in the authorized Project. It contains artifact_url, artifact_version, index_path and index_sha256, not a session-local path. Re-read the current locator before overwrite and stop on concurrent changes. Use only local_path values demonstrably accessible to the actual writer, or inline text if its schema allows; an execution-directory path is not proof of access by another tool. On a failed path, stop and inspect the actual boundary instead of guessing home directories. Read the locator back and verify it. If outcome is unknown or differs, report persistence incomplete and inspect current state; do not retry blindly. This is not an atomic transaction or send lock.

On resume, verify the index hash from the Project locator, then every payload hash/size before using its records. Use recorded host URL/path/version only through actual native read operations. If historical version selection is unsupported, require exact saved bytes and do not claim version pinning. Recover under a fresh working root; reject absolute index paths, parent traversal, duplicate paths and symlink escapes. Relative references resolve from their owning JSON, not always campaign.json. Choose a root that contains all referenced files; legacy external paths require explicit revalidation, not silent rewriting. Run show for inspection, but it is not dependency verification. Missing or changed source/output bytes block affected approvals/actions even if the finished Reel or text ledger is readable.

Private snapshots are not subscriber delivery URLs. Native multi-file storage, real short-source rendering/revision and playback are component evidence; the complete snapshot-plus-locator route and content quality still need native acceptance. An arbitrary large source, a hidden locator card and live publication/delivery are not established. Preserve previous snapshots and do not add a cleanup service.

## State and approvals

The helper's CLI is documented by `--help` and subcommand `--help`. Use `set --stage STAGE --file FILE` to record a JSON artifact, its file hash and current prerequisite tokens. The acyclic order is source -> promise -> edit -> delivery -> review. Select source and excerpts first; draft the actual benefit and CTA before rendering the edit that embeds them. Promise depends on source, not on edit. This avoids a dependency cycle.

Store source media SHA-256 and rights evidence in source. Declare actual input files as `files: [{"path": "source.mp4", "sha256": "..."}]`, relative to that artifact. Set source_sha256 in source. Put the promise artifact's actual file SHA-256 in the edit specification as promise_sha256 before rendering. Edit receipts bind that promise, source bytes, specification and rendered media. Store exact account, post, recipient and message in delivery/review, not generic consent. Relative paths resolve from campaign.json or its artifact, never from a developer directory.

Run `approve --stage STAGE --by COACH` only after explicit coach approval. The helper rechecks prerequisite artifacts, dependency snapshots, artifact file hashes and referenced files. Approve prerequisites in DAG order. Pending external actions require approval of the entire current dependency chain, not just delivery. A file mutation outside the ledger blocks both approval and pending actions. Source changes invalidate all approvals. Promise changes invalidate edit, delivery and review because the Reel embeds its CTA. Edit changes preserve promise but invalidate delivery/review. A new subscriber answer changes review.

After a change, regenerate or explicitly revalidate dependent artifacts in DAG order with `set`, then obtain fresh approvals. An unchanged artifact can be explicitly rebound only when its prerequisites are current; rendered receipts must also match source and promise hashes. Version-1 ledgers cannot authorize actions; retain them as history and start a version-2 ledger. The helper remains a local ledger, not an atomic remote send lock. Never claim it prevents concurrent remote changes.

Translate a natural-language revision into a changed edit specification. Example: "Keep the qualification and make captions larger" means extend the selected range to include the qualification and increase caption_size, but only for independently verified cues. Without verified timing, follow video's uncaptioned-preview rule rather than inventing it. A changed hook also requires a regenerated matching cover and refreshed post caption by default, without asking another permission question. Preserve the previous complete version, then record the new edit and matching delivery files with `set`; report which approvals changed. Do not merely rename the old video or pair it with an old cover. After two ordinary revision rounds recommend one version; unresolved errors still block approval.

## Stop and recovery

After two attempts with no new evidence, stop that approach and record the exact missing transition. Continue independent useful work. Never silently replace native transfer with coach downloads/uploads.

Before a permitted external action, record its scoped action key as `pending` with `action`. Unknown outcomes become `unknown`; inspect remote history before reconciling to confirmed or failed. Never retry pending, unknown or confirmed keys. A confirmed action is not proof of subscriber receipt.

On "stop", first run `stop` to block new local actions. Then, only within authorized scope, disable this campaign's remote test rule and read back its status. Stop any separately authorized native schedule and verify it separately. Test that a control comment produces no new reply. Record remaining remote cleanup if tools or permissions are missing. Local `stopped` does not mean remote rules are disabled or messages recalled. `resume` requires a new explicit coach request and does not restore approvals.

End each update with the current artifact, verified result and next decision. Do not promise background work, booking or publication without the corresponding tested host capability.
