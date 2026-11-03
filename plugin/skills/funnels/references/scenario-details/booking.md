# Qualify consultation leads
Understand what a person needs and help them take the next step toward a call.
Coaches, consultants and service businesses offering an appointment.

No launch or full-path test. Before any change, verify current host tools, account state, overlapping rules and owner approval.
setup_comment_replies creates and enables a rule and may change Main/base; it is not draft creation.
Ordinary tools expose no create-OFF, exact inheritance restoration or continuing comment preview.
test_reply previews DM only. Pausing an automation does not disable Main.
Do not transfer user settings or cross-chat state. catalog.json remains the separate accepted registry.

Profile: ordinary Chatfuel MCP. Documentation observation: 2026-11-02. Not an account test.

## Book calls from comments: readiness question
adaptation_draft_requires_consent
Entry: APPLY comment
Outcome: A consultation link or starter resource
Requirements: Agree to a question; Ready now leads to booking; not yet leads to starter material
Timing: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Retained: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.; URL buttons become readable URLs; confirmation and help controls become actual user replies.
Omitted: Exact source timing is not retained: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.. No timed unsolicited message is configured.; No click tracking, click-dependent branch or no-click reminder.; No imported deterministic graph or source folder/tag tracking.; No outbound escalation email or external booking-completion check.
Limitations: 
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- human: documented; tool_schema_and_playbook; update_automation_setting; switchToHuman. Configure AI-to-human handoff; not an arbitrary email notification action.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- email-send: not_exposed; inference_from_tool_inputs; update_automation_setting; switchToHuman. No arbitrary outbound email action; handoff does not reproduce source email notifications.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6025: Sending a booking link does not confirm an appointment. [Described analogue inro-6025](../native-recipes/inro-6025.md)
### Finish booking setup - inro-6025
Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
```text
Help me prepare: Finish booking setup.
Selected source: inro-6025 - Book more calls from your comments.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Book calls from comments: readiness question
Scope: Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
Source entry: APPLY comment
Source requirements: Agree to a question; Ready now leads to booking; not yet leads to starter material
Source timing: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.
Source outcome: A consultation link or starter resource
Captured text (n001, not approved campaign copy):
Sent, check your DMs
Just sent it to your DMs
It's in your DMs now 🙂
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Use the booking service already named by the owner or source. Do not replace it silently with native Chatfuel booking.
Ask me for: Booking service and URL; Service, availability and time zone; Qualification criteria; Existing authorized access.
1. Confirm the destination service and authorized access. Draft its booking page and required fields using approved availability and time zone. Keep the captured qualification and refusal branches explicit.
2. Verify the page and define confirmation evidence in that service. A link click is not a booking. Native Chatfuel booking statuses do not prove completion in Calendly or another external service. If an automated status bridge is needed, identify a verified existing connection or leave it unresolved.
3. Return draft settings, field mapping, access gaps and separate checks for link delivery and confirmed booking. Do not create a live booking.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
### Retain the source team-email notification - inro-6025
Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
```text
Help me prepare: Retain the source team-email notification.
Selected source: inro-6025 - Book more calls from your comments.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Book calls from comments: readiness question
Scope: Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
Source entry: APPLY comment
Source requirements: Agree to a question; Ready now leads to booking; not yet leads to starter material
Source timing: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.
Source outcome: A consultation link or starter resource
Captured text (n001, not approved campaign copy):
Sent, check your DMs
Just sent it to your DMs
It's in your DMs now 🙂
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Use the existing authorized team mailbox or notification service.
Ask me for: Team recipient and service; Permitted lead fields; Notification condition and approved text; Existing authorized connection.
1. This step is optional if the owner chooses Chatfuel team handoff instead. If the original email notification must remain, verify an existing authorized connection and draft recipient, field mapping and trigger conditions.
2. Do not invent an email-sending bridge. If none is verified, list the missing access and exact next action. Preserve consent and data minimization; prevent duplicate notifications. Verify the recipient and delivery separately from the Chatfuel handoff. Return draft settings only.
3. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
4. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
5. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Qualify DM leads with AI
adaptation_draft_requires_consent
Entry: COACHME direct message
Outcome: A booking link or starter resource
Requirements: Answer a question about the request; AI distinguishes readiness from browsing
Timing: Reply: 20 hours; link click: 2 hours.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Retained: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Omitted: Exact source timing is not retained: Reply: 20 hours; link click: 2 hours.. No timed unsolicited message is configured.; No click tracking, click-dependent branch or no-click reminder.; No imported deterministic graph or source folder/tag tracking.; No outbound escalation email or external booking-completion check.
Limitations: 
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- human: documented; tool_schema_and_playbook; update_automation_setting; switchToHuman. Configure AI-to-human handoff; not an arbitrary email notification action.
- email-send: not_exposed; inference_from_tool_inputs; update_automation_setting; switchToHuman. No arbitrary outbound email action; handoff does not reproduce source email notifications.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6021: AI replies do not establish exact execution of every source condition. [Described analogue inro-6021](../native-recipes/inro-6021.md)
### Finish booking setup - inro-6021
Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
```text
Help me prepare: Finish booking setup.
Selected source: inro-6021 - Qualify DM leads with AI and book calls.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Qualify DM leads with AI
Scope: Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
Source entry: COACHME direct message
Source requirements: Answer a question about the request; AI distinguishes readiness from browsing
Source timing: Reply: 20 hours; link click: 2 hours.
Source outcome: A booking link or starter resource
Captured text (n001, not approved campaign copy):
Thanks for your message! What would you like help with?
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Use the booking service already named by the owner or source. Do not replace it silently with native Chatfuel booking.
Ask me for: Booking service and URL; Service, availability and time zone; Qualification criteria; Existing authorized access.
1. Confirm the destination service and authorized access. Draft its booking page and required fields using approved availability and time zone. Keep the captured qualification and refusal branches explicit.
2. Verify the page and define confirmation evidence in that service. A link click is not a booking. Native Chatfuel booking statuses do not prove completion in Calendly or another external service. If an automated status bridge is needed, identify a verified existing connection or leave it unresolved.
3. Return draft settings, field mapping, access gaps and separate checks for link delivery and confirmed booking. Do not create a live booking.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
### Retain the source team-email notification - inro-6021
Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
```text
Help me prepare: Retain the source team-email notification.
Selected source: inro-6021 - Qualify DM leads with AI and book calls.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Qualify DM leads with AI
Scope: Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
Source entry: COACHME direct message
Source requirements: Answer a question about the request; AI distinguishes readiness from browsing
Source timing: Reply: 20 hours; link click: 2 hours.
Source outcome: A booking link or starter resource
Captured text (n001, not approved campaign copy):
Thanks for your message! What would you like help with?
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Use the existing authorized team mailbox or notification service.
Ask me for: Team recipient and service; Permitted lead fields; Notification condition and approved text; Existing authorized connection.
1. This step is optional if the owner chooses Chatfuel team handoff instead. If the original email notification must remain, verify an existing authorized connection and draft recipient, field mapping and trigger conditions.
2. Do not invent an email-sending bridge. If none is verified, list the missing access and exact next action. Preserve consent and data minimization; prevent duplicate notifications. Verify the recipient and delivery separately from the Chatfuel handoff. Return draft settings only.
3. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
4. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
5. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Ad enquiry: readiness and optional email
waiting_for_chatfuel
Entry: Reply to a specific ad
Outcome: A booking link or resource
Requirements: Ask about readiness; Ready: ask for email with SKIP; Not ready: offer a resource
Timing: Reply: 20 hours; email and link click: 2 hours.
Consent: Email can be skipped; marketing consent is separate.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
This scenario starts from a specific ad reply. Ordinary MCP cannot configure that entry. An ordinary DM conversation would not preserve the selected entry.
Primary result: A booking link or resource
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- ad: dashboard_only; automation-settings_playbook; update_automation_setting; listOfAds. Ad-specific configuration is dashboard-only for normal MCP; ordinary DM loses ad attribution.
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- contact: documented; tool_schema_and_playbook; update_automation_setting; collectContactInfo. Collect and save contact attributes. Not external mailing/SMS subscription or deterministic field-gated branching.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6222: Replacing the ad-specific entry with an ordinary DM changes the behavior. [Described analogue inro-6222](../native-recipes/inro-6222.md)
### Finish booking setup - inro-6222
Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
```text
Help me prepare: Finish booking setup.
Selected source: inro-6222 - Turn ad clicks into booked calls.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Ad enquiry: readiness and optional email
Scope: Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
Source entry: Reply to a specific ad
Source requirements: Ask about readiness; Ready: ask for email with SKIP; Not ready: offer a resource
Source timing: Reply: 20 hours; email and link click: 2 hours.
Source outcome: A booking link or resource
Captured text (n001, not approved campaign copy):
Thanks for your message about the starter plan! Are you looking to start soon?
Yes, soon
Just looking
Current setup decision: waiting_for_chatfuel. This scenario starts from a specific ad reply. Ordinary MCP cannot configure that entry. An ordinary DM conversation would not preserve the selected entry.
Primary Chatfuel result: A booking link or resource
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the booking service already named by the owner or source. Do not replace it silently with native Chatfuel booking.
Ask me for: Booking service and URL; Service, availability and time zone; Qualification criteria; Existing authorized access.
1. Confirm the destination service and authorized access. Draft its booking page and required fields using approved availability and time zone. Keep the captured qualification and refusal branches explicit.
2. Verify the page and define confirmation evidence in that service. A link click is not a booking. Native Chatfuel booking statuses do not prove completion in Calendly or another external service. If an automated status bridge is needed, identify a verified existing connection or leave it unresolved.
3. Return draft settings, field mapping, access gaps and separate checks for link delivery and confirmed booking. Do not create a live booking.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
