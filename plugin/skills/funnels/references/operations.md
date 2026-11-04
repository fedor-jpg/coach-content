# Account Operations

Use the existing Chatfuel connection. These instructions are for the assistant; do not print them as an audit.

## Read

Read `get_playbook` for `setup` and `channels`. Check the actual tool declarations, then use `list_bots`, `get_bot`, `get_automation` and paginated `list_posts`. Confirm the Instagram account, exact selected posts, automation ownership, effective settings, inheritance, enabled flags and overlapping rules. Read the exported compatibility record for the selected funnel. A different host, model or connector contract is not covered by that acceptance; prepare copy but hold writes until verified.

Keep a compact record in this conversation: campaign, account, owned automation ID, baseline, approved changes and readbacks. Never put credentials in that record. This is not cross-chat storage. In a new chat, missing ownership or baseline means read-only reconciliation, not a new duplicate campaign.

## Save While Paused

Show the exact texts, selected posts, keywords, match mode and settings to change. Ask a yes/no question before the requested account changes. Follow tool-specific confirmations; do not combine copy approval with activation.

Use `create_comment_automation` to create one disabled Instagram custom. It starts with broad targeting and inherited replies. Configure it while OFF with `configure_comment_targeting`: explicit selected post IDs, keyword list and match mode. Empty post IDs mean all posts and are forbidden for a selected-post campaign. Creating a paused rule is still an account write.

Use `update_automation_setting` with one setting per call. Fixed messages use `publicReplyHowToReply` or `privateReplyHowToReply` set to `ExactText` and `exactTextReply`. Read back each change. Preserve omitted inactive values. Do not use `setup_comment_replies` for staging: it activates and can change Main and the comment base.

Reuse an existing rule only after verified ownership and explicit adoption approval. Pause before targeting or copy edits. Never change a shared base, Main, schedules, contact collection, handoff, booking or unrelated prompts as an implicit dependency. If the selected path requires a wider change, show the exact old/new values and affected campaigns, then obtain separate approval. A rejection ends that approach.

A created custom can inherit unsafe continuation or follow-up settings. Set the selected funnel's explicit behavior on that custom only, then verify it. Do not assume disabled means correctly configured. Do not silently replace inherited settings on an existing shared rule. Restoration requires supported `set_automation_inheritance` and exact readback, not copying a parent's values.

An unknown write result requires fresh readback and reconciliation. Do not retry creation or sending blindly. A repeated setup request first checks the existing campaign. Never make a second rule because the first response was unclear.

## Activate And Verify

Before activation, read back the complete targeting, message settings, inheritance and flags. Resolve overlapping active rules. Diagnose plan, channel, Main, working-hours and handoff constraints without enabling anything. A Main change needs its own approval covering other enabled automations; do not use it merely to unlock a test.

Ask whether to turn on the named campaign. Use `set_automation_enabled`, then read back its state. An ON flag alone is not proof of delivery.

Use an explicitly authorized test account and selected post. Check the actual entry event, exact received text and recipient-side destination access. Do not infer an external signup, download completion, booking or payment from a sent link. Do not substitute a manual DM for automation delivery. `test_reply` is a sandbox action, not recipient delivery; check its own side effects and approval requirements.

For new commenters, allow only the first private reply until they actually respond. A click is not a reply. Respect current platform messaging rules and per-contact eligibility. Never promise exact-once delivery across repeat comments unless separately verified. A failed test must end with the owned test rule OFF under the agreed stop permission; report any unresolved stop rather than claiming it succeeded.

## Edit, Return, Stop

For edits, read the current settings and compare them with the last verified state. Preserve concurrent changes. Show the changed text, pause with approval, save, read back and request reactivation separately. A new subscriber answer invalidates any draft based on older answers; re-review the final text and recipient before a manual send.

For return, use the conversation record and fresh account state. Never claim a campaign was recovered from a previous chat without evidence. If the owner cannot be established, do not overwrite or recreate it.

For stop, obtain the required approval and call `set_automation_enabled(enabled:false)` only for the owned custom. Read back OFF. If already OFF, do not repeat the mutation. Keep the settings for later use; resuming re-enables them. Leave unrelated campaigns and shared bases unchanged. A stop does not retract sent messages or delete collected data. Verify a new test entry stays silent before claiming live stop passed.
