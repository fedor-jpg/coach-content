---
name: campaign
description: Guides a coach content campaign from source selection through edits, approvals, resumption and test shutdown.
---

# Campaign

Deliver one selected Reel and one matching next step. An MP4 is a content milestone, not a launched funnel.

## Start or resume

1. Use the existing authorized native Project or Work in a folder location. Read its campaign.json before asking questions. Report its files, approvals, unresolved actions and next step.
2. If there is no workspace, ask the coach once to select a native Project or Work in a folder location. This is an explicit setup step. Verify that native execution can actually read/write that authorized location. Keep campaign.json, source/transcript references, receipts and renders there, outside the installed plugin. Never silently use /tmp for durable campaign files. Create campaign.json with `init` only after locating the workspace.
3. Gather missing source permission, audience, programme, desired outcome, language and programme limits in one question. Accept an existing material URL as a delivery branch; do not force a PDF.
4. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/coach.py" doctor` in native execution. Missing Python, FFmpeg, ffprobe, H.264/AAC encoding or both libass and drawtext is an explicit rendering limit. Do not install software or use a paid API without permission. Continue editorial work independently.
5. Check that the environment can read actual media bytes and return generated files in chat. A video webpage is not a downloaded video. Do not claim installation or transfer from a developer-local test.
6. Use the video skill for source selection and edits. Use the delivery skill after the promise and content are coherent.

The assistant runs all helper commands. Resolve plugin resources from CLAUDE_PLUGIN_ROOT, never a developer home directory. JSON media paths resolve relative to the edit specification, not the shell directory. Store campaign files together for portability.

Local project files are not automatically uploaded. A Project name or a local desktop path does not prove that the code VM can access its files. Use only actual authorized host file tools; disclose any transfer/persistence gap. On resume, re-read the files in the same workspace and verify referenced inputs. Do not claim cross-device access or arbitrary new-session recovery from a JSON file on the developer Mac. Native persistence/resumption remains unverified until tested.

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
