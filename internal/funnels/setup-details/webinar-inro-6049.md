# Webinar access after a completed survey

Setup 1.1.0 | webinar-inro-6049 | waiting_for_chatfuel | runtime not tested

## Business Result
Turn Instagram interest into event sign-ups and access.
Hosts promoting a webinar, workshop or event.
Source entry: webinar comment or DM
Source outcome: Webinar access after survey completion
Source requirements: Press the opening button; Complete the survey before access; Remind after the link click
Source timing: After click: 6 days; no click or survey: 3 days; opening button: 2 hours.

## Functional Availability
waiting_for_chatfuel
Webinar access requires verified completion of an external survey. Two AI questions cannot prove that completion; a verified completion integration is missing.
Primary result: Webinar access after survey completion
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- external: No external survey, webinar, Calendly, payment, mailing/SMS subscription or cross-channel completion event. Native booking status applies only to native bookings.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6049: Get Webinar Sign-Ups
Full captured settings/provenance: [selected source JSON](../source-records/inro-6049.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment, dm-ai
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
All posts
FILTER THE COMMENTS
Comments with keyword(s)
webinar
When
Someone sends you a DM
FILTER MESSAGES
Contains keyword(s)
webinar
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Hey! So happy to see you here 🔥 Do you want to join my webinar?
Sign me up 🙌🏻
```
Captured buttons: ["Sign me up 🙌🏻"]
- Edge e001: n001 -> n002 | condition/label: ""
- Edge e014: n001 -> n015 | condition/label: ""
#### n002 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Sign me up 🙌🏻
```
- Edge e002: n002 -> n003 | condition/label: "WHEN BUTTON IS CLICKED\nSign me up 🙌🏻"
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
webinar leads
```
- Edge e003: n003 -> n004 | condition/label: ""
#### n004 (survey)
A link does not prove external form completion. Keep access-after-completion as an unresolved mandatory dependency.
Business input: survey destination and completion evidence
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, external
Captured text (not approved outbound copy):
```text
Webinar 10.10 💫
Fill this survey to access the webinar
Fill it
```
Captured buttons: ["Fill it"]
- Edge e004: n004 -> n005 | condition/label: ""
- Edge e012: n004 -> n013 | condition/label: ""
#### n005 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN SURVEY IS FILLED
```
- Edge e005: n005 -> n006 | condition/label: "WHEN SURVEY IS FILLED"
#### n006 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
webinar attendee
```
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Amazing! Here it comes...
```
- Edge e007: n007 -> n008 | condition/label: ""
#### n008 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Watch my Webinar here ✨
Learn how to grow your IG.
Watch it now 🔗
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBOGo5TUE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--dcef1ec4a311a010f271d289a5505ae5c9d0cc8b/Instagram%20post%20-%202.png"]
- Edge e008: n008 -> n009 | condition/label: ""
- Edge e011: n008 -> n012 | condition/label: ""
#### n009 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e009: n009 -> n010 | condition/label: "WHEN LINK IS CLICKED"
#### n010 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
Wait 6 days
```
- Edge e010: n010 -> n011 | condition/label: ""
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hey! The webinar is happening soon. You can access through the link above
```
- No captured outgoing edge; do not infer completion.
#### n012 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 days
```
- No captured outgoing edge; do not infer completion.
#### n013 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF SURVEY HASN'T BEEN FILLED AFTER
3 days
```
- Edge e013: n013 -> n014 | condition/label: "IF SURVEY HASN'T BEEN FILLED AFTER\n3 days"
#### n014 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hey! The webinar is happening soon! Don't forget to sign up
```
- No captured outgoing edge; do not infer completion.
#### n015 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
2 hours
```
- Edge e015: n015 -> n016 | condition/label: "IF BUTTON HAS NOT BEEN CLICKED AFTER\n2 hours"
#### n016 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hey! Don't forget to click on the button to access my webinar! It's only available for 3 more days.
```
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6049 / Finish event registration
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
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](webinar-inro-6049.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
