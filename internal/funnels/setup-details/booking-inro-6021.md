# Qualify DM leads with AI

Setup 1.1.0 | booking-inro-6021 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Understand what a person needs and help them take the next step toward a call.
Coaches, consultants and service businesses offering an appointment.
Source entry: COACHME direct message
Source outcome: A booking link or starter resource
Source requirements: Answer a question about the request; AI distinguishes readiness from browsing
Source timing: Reply: 20 hours; link click: 2 hours.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Retained/replaced: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Not retained: Exact source timing is not retained: Reply: 20 hours; link click: 2 hours.. No timed unsolicited message is configured.
Not retained: No click tracking, click-dependent branch or no-click reminder.
Not retained: No imported deterministic graph or source folder/tag tracking.
Not retained: No outbound escalation email or external booking-completion check.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- email-send: No arbitrary outbound email action; handoff does not reproduce source email notifications.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Use the actual reply to route suitable consultation interest to booking and browsing/later replies to a starter guide.
Target: dm_base
Ask only for missing business facts:
- program_name: Supply the business value and approve its use in this selected draft. (required)
- known_facts: Supply the business value and approve its use in this selected draft. (required)
- booking_url: Supply the business value and approve its use in this selected draft. (required)
- starter_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text, handoff_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Thanks for your message! What would you like help with?
refusal: Understood. I will stop this request.
handoff: {handoff_text}
question: Thanks for your message! What would you like help with?
qualified: Book a call: {booking_url}
starter: Free starter guide: {starter_url}
help: What would you like to know about {program_name}?
placement: DM {keyword}.
Use {program_name} and {known_facts}. Ask what they need; evaluate only their actual answer using the captured ready-soon versus browsing/later criteria. Ready soon -> {booking_url}; not yet -> {starter_url}. These are mutually exclusive alternatives, never both links in sequence. No booking, payment or external completion confirmation. Unresolved questions or a team request use {handoff_text}; no outbound email. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
  - If Selected entry received -> first
- first: Wait for the actual reply.
  - If Actual reply indicates starting soon, price, availability, a call or a relevant problem -> qualified
  - If Actual reply indicates browsing, later, off-topic or no budget -> starter
  - If Actual refusal or STOP -> refusal
  - If No actual reply -> silence
- qualified: Offer only the booking destination.
- starter: Offer only the starter resource.
- refusal: End this request without delivering gated content.
- silence: No message after silence.
#### Exact Setting Drafts
Not tool calls. Add resolved botID/automationID and privacy-safe context only after all gates; one setting per call.
```json
[
  {
    "tool": "update_automation_setting",
    "target": "dm_base",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Thanks for your message! What would you like help with?\nUse {program_name} and {known_facts}. Ask what they need; evaluate only their actual answer using the captured ready-soon versus browsing/later criteria. Ready soon -> {booking_url}; not yet -> {starter_url}. These are mutually exclusive alternatives, never both links in sequence. No booking, payment or external completion confirmation. Unresolved questions or a team request use {handoff_text}; no outbound email. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\nhandoff: {handoff_text}\nquestion: Thanks for your message! What would you like help with?\nqualified: Book a call: {booking_url}\nstarter: Free starter guide: {starter_url}\nhelp: What would you like to know about {program_name}?"
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "dm_base",
    "settings": {
      "switchToHuman": {
        "howToSwitch": "SwitchToTeammates",
        "rules": "$resolved.safe_handoff_rules"
      }
    }
  }
]
```
Candidate additions; never send as a replacement for an unread existing list:
```json
{
  "switchToHuman": {
    "switchingConditions": "Campaign {campaign}: the person requests the team or facts are unresolved.",
    "messagePrompt": "{handoff_text}"
  }
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6021: Qualify DM leads with AI and book calls
Full captured settings/provenance: [selected source JSON](../source-records/inro-6021.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
When
Someone sends you a DM
FILTER MESSAGES
Contains keyword(s)
COACHME
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Thanks for your message! What would you like help with?
```
- Field (captured): {"label":null,"type":"text","value":"Thanks for your message! What would you like help with?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (wait_for_reply)
AI instructions can wait for a real reply. Exact flow state and timeout semantics are not imported.
Business input: approved question and refusal behavior
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, graph
Captured text (not approved outbound copy):
```text
Wait for reply
The scenario will pause and wait until the contact replies to proceed.
```
- Edge e002: n002 -> n003 | condition/label: ""
- Edge e016: n002 -> n017 | condition/label: ""
#### n003 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN CONTACT REPLIES
```
- Edge e003: n003 -> n004 | condition/label: "WHEN CONTACT REPLIES"
#### n004 (ai_condition)
AI judgment may be an explicit adaptation; it does not reproduce an imported deterministic gate.
Business input: qualification policy and exact questions
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, graph
Captured text (not approved outbound copy):
```text
AI-detected condition
Use AI to evaluate if a custom condition is true or false
True when they want to start soon, ask about the price, availability or a call, or describe a problem the program solves. False when they are only browsing, off topic, or say later or no budget.
```
- Field (captured): {"label":null,"type":"textarea","value":"True when they want to start soon, ask about the price, availability or a call, or describe a problem the program solves. False when they are only browsing, off topic, or say later or no budget.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e004: n004 -> n005 | condition/label: ""
- Edge e011: n004 -> n012 | condition/label: ""
#### n005 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
IF CONDITION IS TRUE
```
- Edge e005: n005 -> n006 | condition/label: "IF CONDITION IS TRUE"
#### n006 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Coaching program:…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (send_email)
External notification remains a separate continuation; switchToHuman is not an email send.
Business input: recipient, purpose and existing authorized provider
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: email-send
Captured text (not approved outbound copy):
```text
Send email
Send an email to a specified email address.
From	contact@inroapp.com
To	
New lead: @{{contact.username}} | @{{organization.username}}
@{{contact.username}} asked about the coaching program, and the AI judged them a fit. Their answer: "{{conversation.last_message_received}}". Your booking link is on its way to them. Reply in the Inrō inbox or on Instagram. Instagram only lets you reply within 24 hours of their last message. Next step: check whether they booked, and follow up if not.
```
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":[{"selected":true,"text":"contact@inroapp.com (Default email)","value":""}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":""}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"<redacted>","value_state":"unknown","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"<redacted>","value_state":"unknown","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":"Select a file","type":"file","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"","value_state":"observed_unset","options":[{"selected":true,"text":"contact@inroapp.com (Default email)","value":""}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e007: n007 -> n008 | condition/label: ""
#### n008 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Book a call
Pick a time
```
- Edge e008: n008 -> n009 | condition/label: ""
- Edge e009: n008 -> n010 | condition/label: ""
#### n009 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- No captured outgoing edge; do not infer completion.
#### n010 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
2 hours
```
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e010: n010 -> n011 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n2 hours"
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you checked the link yet?
```
- Field (captured): {"label":null,"type":"text","value":"Have you checked the link yet?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- No captured outgoing edge; do not infer completion.
#### n012 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
IF CONDITION IS FALSE
```
- Edge e012: n012 -> n013 | condition/label: "IF CONDITION IS FALSE"
#### n013 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Coaching program:…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e013: n013 -> n014 | condition/label: ""
#### n014 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Free starter guide
Open it
```
- Edge e014: n014 -> n015 | condition/label: ""
- Edge e015: n014 -> n016 | condition/label: ""
#### n015 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- No captured outgoing edge; do not infer completion.
#### n016 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
2 hours
```
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n017 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T REPLIED AFTER
20 hours
```
- Field (captured): {"label":null,"type":"number","value":"20","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6021 / Finish booking setup
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
## External Continuation: inro-6021 / Retain the source team-email notification
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
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](booking-inro-6021.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
