# Sell products during a Live

Setup 1.1.0 | offers-inro-4393 | waiting_for_chatfuel | runtime not tested

## Business Result
Deliver a relevant product offer or coupon while interest is high.
Shops and creators using comments, Stories or Lives to promote an offer.
Source entry: Comment during a Live
Source outcome: A product offer
Source requirements: Press the opening button; Click the product link
Source timing: No link click: 2 hours; opening button: 6 hours.

## Functional Availability
waiting_for_chatfuel
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: A product offer
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- live: Post/comment configuration does not establish a Live-comment entry tool.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-4393: Sell your products during a live
Full captured settings/provenance: [selected source JSON](../source-records/inro-4393.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: comment, live
Captured text (not approved outbound copy):
```text
When
Someone comments on your Live
```
- Field (captured): {"label":null,"type":"text","value":"keywords","value_state":"observed_value","options":[{"selected":false,"text":"Any comment","value":"any"},{"selected":true,"text":"Comments that include a keyword","value":"keywords"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"any"}
- Field (captured): {"value":"keywords"}
- Field (captured): {"label":null,"type":"text","value":"PICKS","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Thanks for joining the live! Want the product picks? Tap below.
Yes, send it
```
Captured buttons: ["Yes, send it"]
- Field (captured): {"label":null,"type":"textarea","value":"Thanks for joining the live! Want the product picks? Tap below.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Yes, send it","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"url","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e001: n001 -> n002 | condition/label: ""
- Edge e007: n001 -> n008 | condition/label: ""
#### n002 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Yes, send it
```
- Edge e002: n002 -> n003 | condition/label: "WHEN BUTTON IS CLICKED\nYes, send it"
#### n003 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Product picks
Open it
```
- Edge e003: n003 -> n004 | condition/label: ""
- Edge e005: n003 -> n006 | condition/label: ""
#### n004 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e004: n004 -> n005 | condition/label: "WHEN LINK IS CLICKED"
#### n005 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Product picks: cli…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
#### n006 (branch_expiration)
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
- Edge e006: n006 -> n007 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n2 hours"
#### n007 (message)
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
#### n008 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
6 hours
```
- Field (captured): {"label":null,"type":"number","value":"6","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-4393 / Finish the offer destination
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: inro-4393 - Sell your products during a live.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Sell products during a Live
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Comment during a Live
Source requirements: Press the opening button; Click the product link
Source timing: No link click: 2 hours; opening button: 6 hours.
Source outcome: A product offer
Captured text (n001, not approved campaign copy):
Thanks for joining the live! Want the product picks? Tap below.
Yes, send it
Current setup decision: waiting_for_chatfuel. This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary Chatfuel result: A product offer
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](offers-inro-4393.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
