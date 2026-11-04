# Live leads: product or course by interest

Setup 1.1.0 | offers-inro-4484 | waiting_for_chatfuel | runtime not tested

## Business Result
Deliver a relevant product offer or coupon while interest is high.
Shops and creators using comments, Stories or Lives to promote an offer.
Source entry: Comment during a Live
Source outcome: An offer matching the chosen interest
Source requirements: Choose an interest: products or course; Receive the matching offer
Source timing: Link clicks: 3 hours and 3 days; no reply: 3 days.

## Functional Availability
waiting_for_chatfuel
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: An offer matching the chosen interest
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
### inro-4484: Get Leads From IG Lives
Full captured settings/provenance: [selected source JSON](../source-records/inro-4484.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, live
Captured text (not approved outbound copy):
```text
When
Someone comments on your Live
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
IG lives leads
```
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Thanks for joining my live! Glad to have you here ❤️
```
- Edge e002: n002 -> n003 | condition/label: ""
#### n003 (ask_question)
AI can ask and wait for an actual answer. Exact graph branches are not guaranteed.
Business input: approved question and answer requirements
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, graph
Captured text (not approved outbound copy):
```text
What did you enjoy the most?
Products I showed
Course I am running
```
- Edge e003: n003 -> n004 | condition/label: ""
- Edge e011: n003 -> n012 | condition/label: ""
- Edge e019: n003 -> n020 | condition/label: ""
- Edge e022: n003 -> n023 | condition/label: ""
#### n004 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
CONTACT REPLIES
Products I showed
```
- Edge e004: n004 -> n005 | condition/label: "CONTACT REPLIES\nProducts I showed"
#### n005 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
IG live - product
```
- Edge e005: n005 -> n006 | condition/label: ""
#### n006 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Amazing! Here's my products ❤️
```
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
$15 facial cream 🤩
The shopify link to the product you want
Shop now
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBM2l5S0E9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--de1b493ae1e6a38937cf9624d4a6f005b42b7c00/Untitled%20design%20-%202025-06-25T141331.210.png"]
- Edge e007: n007 -> n008 | condition/label: ""
- Edge e009: n007 -> n010 | condition/label: ""
#### n008 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e008: n008 -> n009 | condition/label: "WHEN LINK IS CLICKED"
#### n009 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
See you in my next live🔥  
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
3 hours
```
- Edge e010: n010 -> n011 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 hours"
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you checked the link yet? 
```
- No captured outgoing edge; do not infer completion.
#### n012 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
CONTACT REPLIES
Course I am running
```
- Edge e012: n012 -> n013 | condition/label: "CONTACT REPLIES\nCourse I am running"
#### n013 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
IG live - course
```
- Edge e013: n013 -> n014 | condition/label: ""
#### n014 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Amazing! See you in my next live ❤️
```
- Edge e014: n014 -> n015 | condition/label: ""
#### n015 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Check my course here 🔥
Check what my course is about
Visit website 🔗
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBMjhjUFE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--01309da4202f5e07ce93b7b1599ff0ae2db2ca84/download.jpeg"]
- Edge e015: n015 -> n016 | condition/label: ""
- Edge e017: n015 -> n018 | condition/label: ""
#### n016 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e016: n016 -> n017 | condition/label: "WHEN LINK IS CLICKED"
#### n017 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
See you in my next live🔥  
```
- No captured outgoing edge; do not infer completion.
#### n018 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 days
```
- Edge e018: n018 -> n019 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 days"
#### n019 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you checked the link yet? 
```
- No captured outgoing edge; do not infer completion.
#### n020 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
ANY OTHER REPLY
```
- Edge e020: n020 -> n021 | condition/label: "ANY OTHER REPLY"
#### n021 (agent_reply)
Grounded AI replies are instructions, not deterministic output or unknown facts.
Business input: approved facts and reply constraints
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
AI Agent auto-DM
Let your AI Agent reply once to the last message or comment
Normal message (~25 words)
```
- Edge e021: n021 -> n022 | condition/label: ""
#### n022 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
IG Live - Unique R…
```
- No captured outgoing edge; do not infer completion.
#### n023 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T REPLIED AFTER
3 days
```
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](offers-inro-4484.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
