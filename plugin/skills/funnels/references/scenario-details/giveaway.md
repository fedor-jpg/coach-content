# Grow reach with a giveaway
Invite participation and apply the giveaway rules before confirming an entry.
Businesses running a campaign with clear eligibility and prize rules.

No launch or full-path test. Before any change, verify current host tools, account state, overlapping rules and owner approval.
setup_comment_replies creates and enables a rule and may change Main/base; it is not draft creation.
Ordinary tools expose no create-OFF, exact inheritance restoration or continuing comment preview.
test_reply previews DM only. Pausing an automation does not disable Main.
Do not transfer user settings or cross-chat state. catalog.json remains the separate accepted registry.

Profile: ordinary Chatfuel MCP. Documentation observation: 2026-11-02. Not an account test.

## Giveaway entry: tag, follow and email
waiting_for_chatfuel
Entry: Comment tagging another person
Outcome: An eligible entrant, not a selected winner
Requirements: Verify the tag; Verify a follow; Require email
Timing: Email: 20 hours; follow: 24 hours.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary result: An eligible entrant, not a selected winner
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- follower: not_exposed; inference_from_tool_inputs; setup_comment_replies, update_automation_setting; . No Instagram follower condition or follow/check/retry gate in normal tool inputs.
- contact: documented; tool_schema_and_playbook; update_automation_setting; collectContactInfo. Collect and save contact attributes. Not external mailing/SMS subscription or deterministic field-gated branching.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6018: Eligibility verification and selecting a winner require separate confirmation. [Described analogue inro-6018](../native-recipes/inro-6018.md)

## Giveaway: captured 95/5 random split
waiting_for_chatfuel
Entry: Comment tagging another person
Outcome: One of two giveaway outcomes
Requirements: Check started_giveaway; Choose between random outcomes with 95% and 5% weights
Timing: No separate exact timer captured.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The selected outcome requires random selection or allocation. Ordinary MCP cannot implement that selection; giving everyone the same reward is a different result.
Primary result: One of two giveaway outcomes
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: Resolve the gate/notes and 95%/5% outcome conflict without correcting the original record.
Client inputs: post, keywords, eligibility policy, tag, prizes, destinations
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- random: not_exposed; inference_from_tool_inputs; update_automation_setting; . No weighted random prize distribution in normal tool inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- manychat-105: Captured 95% and 5% weights conflict with the notes. Values remain unchanged. No authored analogue; this does not establish tool availability.
