# Fill your event or webinar
Turn Instagram interest into event sign-ups and access.
Hosts promoting a webinar, workshop or event.

No launch or full-path test. Before any change, verify current host tools, account state, overlapping rules and owner approval.
setup_comment_replies creates and enables a rule and may change Main/base; it is not draft creation.
Ordinary tools expose no create-OFF, exact inheritance restoration or continuing comment preview.
test_reply previews DM only. Pausing an automation does not disable Main.
Do not transfer user settings or cross-chat state. catalog.json remains the separate accepted registry.

Profile: ordinary Chatfuel MCP. Documentation observation: 2026-11-02. Not an account test.

## Webinar access after a completed survey
waiting_for_chatfuel
Entry: webinar comment or DM
Outcome: Webinar access after survey completion
Requirements: Press the opening button; Complete the survey before access; Remind after the link click
Timing: After click: 6 days; no click or survey: 3 days; opening button: 2 hours.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
Webinar access requires verified completion of an external survey. Two AI questions cannot prove that completion; a verified completion integration is missing.
Primary result: Webinar access after survey completion
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- external: not_exposed; tool_schema_and_playbook; setup_booking, list_bookings, update_automation_setting; collectContactInfo, bookingRules. No external survey, webinar, Calendly, payment, mailing/SMS subscription or cross-channel completion event. Native booking status applies only to native bookings.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6049: A registration link does not establish survey completion. [Described analogue inro-6049](../native-recipes/inro-6049.md)
### Finish event registration - inro-6049
Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
```text
Help me prepare: Finish event registration.
Selected source: inro-6049 - Get Webinar Sign-Ups.
Goal: Turn Instagram interest into event sign-ups and access.
Variant: Webinar access after a completed survey
Scope: Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
Source entry: webinar comment or DM
Source requirements: Press the opening button; Complete the survey before access; Remind after the link click
Source timing: After click: 6 days; no click or survey: 3 days; opening button: 2 hours.
Source outcome: Webinar access after survey completion
Captured text (n001, not approved campaign copy):
Hey! So happy to see you here 🔥 Do you want to join my webinar?
Sign me up 🙌🏻
Current setup decision: waiting_for_chatfuel. Webinar access requires verified completion of an external survey. Two AI questions cannot prove that completion; a verified completion integration is missing.
Primary Chatfuel result: Webinar access after survey completion
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing form or webinar service and the selected event.
Ask me for: Event service, form and URL; Event date and time zone; Required registration fields and consent; Existing authorized access.
1. Confirm the event and authorized access. Draft the registration form and map only its required fields. Event registration consent does not imply email or SMS marketing consent.
2. Retain required versus optional email/phone distinctions. If the Chatfuel variant delivers the link before optional email, disclose that change; do not claim the original contact gate remains.
3. Define success as a registration record in the event service, separately from delivery or clicks. If reminders depend on external completion or exact timing, identify a verified existing connection and its semantics or leave that dependency unresolved. Return draft settings and next access steps; do not register attendees or send reminders.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Event sign-up link: optional email
adaptation_draft_requires_consent
Entry: WEBINAR comment
Outcome: A registration link, not a confirmed registration
Requirements: Ask for email; Allow SKIP before the link
Timing: No email and no click: 2 hours; opening button: 6 hours.
Consent: Email can be skipped. External consent and registration are not confirmed.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Ask for optional email, then give the registration URL on a valid answer or SKIP.
Retained: Ask for optional email, then give the registration URL on a valid answer or SKIP.; URL buttons become readable URLs; confirmation and help controls become actual user replies.
Omitted: Exact source timing is not retained: No email and no click: 2 hours; opening button: 6 hours.. No timed unsolicited message is configured.; No click tracking, click-dependent branch or no-click reminder.; No imported deterministic graph or source folder/tag tracking.
Limitations: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.; Optional contact before delivery: a new consented contact or explicit SKIP both lead to the link.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- contact: documented; tool_schema_and_playbook; update_automation_setting; collectContactInfo. Collect and save contact attributes. Not external mailing/SMS subscription or deterministic field-gated branching.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6054: Registration in the external event system is not confirmed. [Described analogue inro-6054](../native-recipes/inro-6054.md)
### Finish event registration - inro-6054
Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
```text
Help me prepare: Finish event registration.
Selected source: inro-6054 - Get sign-ups for your event or webinar.
Goal: Turn Instagram interest into event sign-ups and access.
Variant: Event sign-up link: optional email
Scope: Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
Source entry: WEBINAR comment
Source requirements: Ask for email; Allow SKIP before the link
Source timing: No email and no click: 2 hours; opening button: 6 hours.
Source outcome: A registration link, not a confirmed registration
Captured text (n001, not approved campaign copy):
Sent you the details by DM
Check your DMs for the link
Just sent it to your DMs 🙂
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Ask for optional email, then give the registration URL on a valid answer or SKIP.
Use the existing form or webinar service and the selected event.
Ask me for: Event service, form and URL; Event date and time zone; Required registration fields and consent; Existing authorized access.
1. Confirm the event and authorized access. Draft the registration form and map only its required fields. Event registration consent does not imply email or SMS marketing consent.
2. Retain required versus optional email/phone distinctions. If the Chatfuel variant delivers the link before optional email, disclose that change; do not claim the original contact gate remains.
3. Define success as a registration record in the event service, separately from delivery or clicks. If reminders depend on external completion or exact timing, identify a verified existing connection and its semantics or leave that dependency unresolved. Return draft settings and next access steps; do not register attendees or send reminders.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Turn comments into RSVPs: email and phone required
adaptation_draft_requires_consent
Entry: Keyword comment
Outcome: A webinar link after both contacts
Requirements: Press the opening button; Email is required; Phone is required after email
Timing: Two unset no-response exits: 23 hours each.
Consent: State the purposes of email and phone collection. The invitation does not prove external subscription consent.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.
Retained: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.; URL buttons become readable URLs; confirmation and help controls become actual user replies.
Omitted: Exact source timing is not retained: Two unset no-response exits: 23 hours each.. No timed unsolicited message is configured.; No imported deterministic graph or source folder/tag tracking.
Limitations: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.; Every requested contact is required before delivery: email and phone. Refusal does not release the gated link.
Missing source facts: None blocking this assessment.
Client inputs: post, keywords, webinar URL, email purpose, phone purpose, consent basis
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- contact: documented; tool_schema_and_playbook; update_automation_setting; collectContactInfo. Collect and save contact attributes. Not external mailing/SMS subscription or deterministic field-gated branching.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- manychat-81: Two 23-hour exits are unset. Webinar registration is not confirmed. [Described analogue inro-6054](../native-recipes/inro-6054.md)
### Finish event registration - manychat-81
Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
```text
Help me prepare: Finish event registration.
Selected source: manychat-81 - Turn comments into RSVPs.
Goal: Turn Instagram interest into event sign-ups and access.
Variant: Turn comments into RSVPs: email and phone required
Scope: Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
Source entry: Keyword comment
Source requirements: Press the opening button; Email is required; Phone is required after email
Source timing: Two unset no-response exits: 23 hours each.
Source outcome: A webinar link after both contacts
Captured text (node-0, not approved campaign copy):
Hey! I'm so happy you'd like to join my free webinar "How to make real money from social media". 💅

Tap below to get access! 
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.
Use the existing form or webinar service and the selected event.
Ask me for: Event service, form and URL; Event date and time zone; Required registration fields and consent; Existing authorized access.
1. Confirm the event and authorized access. Draft the registration form and map only its required fields. Event registration consent does not imply email or SMS marketing consent.
2. Retain required versus optional email/phone distinctions. If the Chatfuel variant delivers the link before optional email, disclose that change; do not claim the original contact gate remains.
3. Define success as a registration record in the event service, separately from delivery or clicks. If reminders depend on external completion or exact timing, identify a verified existing connection and its semantics or leave that dependency unresolved. Return draft settings and next access steps; do not register attendees or send reminders.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
