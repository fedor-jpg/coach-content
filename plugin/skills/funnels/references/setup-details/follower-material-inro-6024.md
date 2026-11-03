# Freebie: different gates for existing and new followers

Setup 1.1.0 | follower-material-inro-6024 | waiting_for_chatfuel | runtime not tested

## Business Result
Offer a useful resource in exchange for a verified follow.
Creators who want access to depend on following, not just an invitation to follow.
Source entry: Freebie comment
Source outcome: A resource after the conditions of the matching branch
Source requirements: Check current follower status; Existing followers provide email; new followers verify a follow
Source timing: Clicks: 3 hours and 3 days; email: 3 days; button: 2 days; follow: 1 day and 3 days.

## Functional Availability
waiting_for_chatfuel
The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary result: A resource after the conditions of the matching branch
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- follower: No Instagram follower condition or follow/check/retry gate in normal tool inputs.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6024: Get Leads With Freebies
Full captured settings/provenance: [selected source JSON](../source-records/inro-6024.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
All posts
FILTER THE COMMENTS
Comments with keyword(s)
Freebie
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (comment)
A fixed public reply is a documented primitive, not proof of captured random text choice or downstream routing.
Business input: approved public reply
Setting candidate: update_automation_setting: publicReply
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text
Thanks for your comment 💛
Check your DMs 🔥
```
- Field (captured): {"label":null,"type":"text","value":"Thanks for your comment 💛","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"Check your DMs 🔥","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"checkbox","value":false,"value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"checkbox","value":true,"value_state":"observed_value","options":null,"validation":null}
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Comment leads
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e002: n002 -> n003 | condition/label: ""
#### n003 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hey {{contact.name}}! Happy to see you here 😃
```
- Field (captured): {"label":null,"type":"text","value":"Hey {{contact.name}}! Happy to see you here 😃","value_state":"observed_value","options":null,"validation":null}
- Edge e003: n003 -> n004 | condition/label: ""
#### n004 (contact_filter_condition)
Preserve both condition exits. A prompt is not a verified stored-contact/follower predicate.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: follower, graph
Captured text (not approved outbound copy):
```text
Contact filter
Branch based on whether the contact matches a set of filters.
They follow you
```
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"is_true","value_state":"observed_value","options":[{"selected":true,"text":"They follow you","value":"is_true"},{"selected":false,"text":"They don't follow you","value":"is_false"}],"validation":null}
- Field (captured): {"value":"is_true"}
- Field (captured): {"value":"is_false"}
- Edge e004: n004 -> n005 | condition/label: ""
- Edge e024: n004 -> n025 | condition/label: ""
#### n005 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
MATCHES FILTERS
```
- Edge e005: n005 -> n006 | condition/label: "MATCHES FILTERS"
#### n006 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
To get our free guide, please leave us your email below 👇
Let's go ✨
```
Captured buttons: ["Let's go ✨"]
- Field (captured): {"label":null,"type":"textarea","value":"To get our free guide, please leave us your email below 👇","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"Let's go ✨","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"To get our free guide, please leave us your email below 👇","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Let's go ✨","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"url","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e006: n006 -> n007 | condition/label: ""
- Edge e015: n006 -> n016 | condition/label: ""
#### n007 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Let's go ✨
```
- Edge e007: n007 -> n008 | condition/label: "WHEN BUTTON IS CLICKED\nLet's go ✨"
#### n008 (collect_property)
Contact storage is documented. Exact validation gates, retries and external subscriptions are separate dependencies.
Business input: purpose, required versus optional contact, channel consent
Setting candidate: update_automation_setting: collectContactInfo
Disposition: requires_change_or_external_dependency; dependencies: contact, graph
Captured text (not approved outbound copy):
```text
Ask for information
Collect email, phone or any contact property and save it automatically.
Please send your email address to continue
Message without the information
We couldn't detect your email. Please try again.
Email
```
- Field (captured): {"label":null,"type":"textarea","value":"Please send your email address to continue","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect your email. Please try again.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":"0","minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"continue"}
- Field (captured): {"value":"expire"}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Field (captured): {"label":null,"type":"textarea","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e008: n008 -> n009 | condition/label: ""
- Edge e014: n008 -> n015 | condition/label: ""
#### n009 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN INFORMATION IS COLLECTED
```
- Edge e009: n009 -> n010 | condition/label: "WHEN INFORMATION IS COLLECTED"
#### n010 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Here's your guide 🔥
Get it now
```
- Edge e010: n010 -> n011 | condition/label: ""
- Edge e012: n010 -> n013 | condition/label: ""
#### n011 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e011: n011 -> n012 | condition/label: "WHEN LINK IS CLICKED"
#### n012 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Freebie received
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
#### n013 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 hours
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e013: n013 -> n014 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 hours"
#### n014 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you received the link?
```
- Field (captured): {"label":null,"type":"text","value":"Have you received the link?","value_state":"observed_value","options":null,"validation":null}
- No captured outgoing edge; do not infer completion.
#### n015 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF INFORMATION HAS NOT BEEN RECEIVED AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n016 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
2 days
```
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e016: n016 -> n017 | condition/label: "IF BUTTON HAS NOT BEEN CLICKED AFTER\n2 days"
#### n017 (collect_property)
Contact storage is documented. Exact validation gates, retries and external subscriptions are separate dependencies.
Business input: purpose, required versus optional contact, channel consent
Setting candidate: update_automation_setting: collectContactInfo
Disposition: requires_change_or_external_dependency; dependencies: contact, graph
Captured text (not approved outbound copy):
```text
Ask for information
Collect email, phone or any contact property and save it automatically.
Hey there! Still want your guide? Leave your email below 👇🏻
Message without the information
We couldn't detect your email. Please try again.
Email
```
- Field (captured): {"label":null,"type":"textarea","value":"Hey there! Still want your guide? Leave your email below 👇🏻","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"button","value":true,"value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect your email. Please try again.","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":null}
- Field (captured): {"value":"continue"}
- Field (captured): {"value":"expire"}
- Field (captured): {"label":null,"type":"button","value":false,"value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"Hey there! Still want your guide? Leave your email below 👇🏻","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect your email. Please try again.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":"0","minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Field (captured): {"label":null,"type":"textarea","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e017: n017 -> n018 | condition/label: ""
- Edge e023: n017 -> n024 | condition/label: ""
#### n018 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN INFORMATION IS COLLECTED
```
- Edge e018: n018 -> n019 | condition/label: "WHEN INFORMATION IS COLLECTED"
#### n019 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Here's your guide 🔥
Get it now
```
- Edge e019: n019 -> n020 | condition/label: ""
- Edge e021: n019 -> n022 | condition/label: ""
#### n020 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e020: n020 -> n021 | condition/label: "WHEN LINK IS CLICKED"
#### n021 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Freebie received
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
#### n022 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 hours
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e022: n022 -> n023 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 hours"
#### n023 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you received the link?
```
- Field (captured): {"label":null,"type":"text","value":"Have you received the link?","value_state":"observed_value","options":null,"validation":null}
- No captured outgoing edge; do not infer completion.
#### n024 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF INFORMATION HAS NOT BEEN RECEIVED AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n025 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
DOES NOT MATCH
```
- Edge e025: n025 -> n026 | condition/label: "DOES NOT MATCH"
#### n026 (ask_for_follow)
A follow request is not a verified follow gate. Keep true delivery/false retry in the original only.
Business input: whether unconditional delivery is acceptable
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, follower
Captured text (not approved outbound copy):
```text
To get our free guide, please follow us👇
I have followed you
```
Captured buttons: ["I have followed you"]
- Field (captured): {"label":null,"type":"textarea","value":"To get our free guide, please follow us👇","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"I have followed you","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect your follow. Please try again.","value_state":"observed_value","options":null,"validation":null}
- Edge e026: n026 -> n027 | condition/label: ""
- Edge e032: n026 -> n033 | condition/label: ""
#### n027 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN CONTACT CLICKS AND FOLLOWS YOU
```
- Edge e027: n027 -> n028 | condition/label: "WHEN CONTACT CLICKS AND FOLLOWS YOU"
#### n028 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Here's your guide 🔥
Get it now
```
- Edge e028: n028 -> n029 | condition/label: ""
- Edge e030: n028 -> n031 | condition/label: ""
#### n029 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e029: n029 -> n030 | condition/label: "WHEN LINK IS CLICKED"
#### n030 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Freebie received
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
#### n031 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 hours
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e031: n031 -> n032 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 hours"
#### n032 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you received the link?
```
- Field (captured): {"label":null,"type":"text","value":"Have you received the link?","value_state":"observed_value","options":null,"validation":null}
- No captured outgoing edge; do not infer completion.
#### n033 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T CLICKED AND FOLLOWED YOU AFTER
1 days
```
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e033: n033 -> n034 | condition/label: "IF CONTACT HASN'T CLICKED AND FOLLOWED YOU AFTER\n1 days"
#### n034 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hey there! Still want your guide? Give us a follow and we'll share it with you 👇🏻
```
- Field (captured): {"label":null,"type":"text","value":"Hey there! Still want your guide? Give us a follow and we'll share it with you 👇🏻","value_state":"observed_value","options":null,"validation":null}
- Edge e034: n034 -> n035 | condition/label: ""
#### n035 (ask_for_follow)
A follow request is not a verified follow gate. Keep true delivery/false retry in the original only.
Business input: whether unconditional delivery is acceptable
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, follower
Captured text (not approved outbound copy):
```text
Please follow us to continue
I have followed you
```
Captured buttons: ["I have followed you"]
- Field (captured): {"label":null,"type":"textarea","value":"Please follow us to continue","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"I have followed you","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect your follow. Please try again.","value_state":"observed_value","options":null,"validation":null}
- Edge e035: n035 -> n036 | condition/label: ""
- Edge e040: n035 -> n041 | condition/label: ""
#### n036 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN CONTACT CLICKS AND FOLLOWS YOU
```
- Edge e036: n036 -> n037 | condition/label: "WHEN CONTACT CLICKS AND FOLLOWS YOU"
#### n037 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Here's your guide 🔥
Get it now
```
- Edge e037: n037 -> n038 | condition/label: ""
- Edge e039: n037 -> n040 | condition/label: ""
#### n038 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e038: n038 -> n039 | condition/label: "WHEN LINK IS CLICKED"
#### n039 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Freebie received
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
#### n040 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n041 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T CLICKED AND FOLLOWED YOU AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6024 / Finish email-list signup
Optional: only if the owner also wants email marketing signup. Resource delivery or waitlist participation alone does not require it.
```text
Help me prepare: Finish email-list signup.
Selected source: inro-6024 - Get Leads With Freebies.
Goal: Offer a useful resource in exchange for a verified follow.
Variant: Freebie: different gates for existing and new followers
Scope: Optional: only if the owner also wants email marketing signup. Resource delivery or waitlist participation alone does not require it.
Source entry: Freebie comment
Source requirements: Check current follower status; Existing followers provide email; new followers verify a follow
Source timing: Clicks: 3 hours and 3 days; email: 3 days; button: 2 days; follow: 1 day and 3 days.
Source outcome: A resource after the conditions of the matching branch
Captured text (n001, not approved campaign copy):
Thanks for your comment 💛
Check your DMs 🔥
Current setup decision: waiting_for_chatfuel. The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary Chatfuel result: A resource after the conditions of the matching branch
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing email provider. If none exists, propose Brevo for approval; it is not connected.
Ask me for: Provider and target list; Email consent wording and proof; Resource URL; welcome email only if separately requested; Existing authorized access or connection.
1. Inspect existing authorized connections. Chatfuel contact collection alone does not subscribe anyone to an external list. Use a sync only after verifying its field mapping, authorization and readback.
2. If no sync is verified, propose a hosted signup form link in the DM. A Brevo form can collect EMAIL and add the contact to the selected list. Disclose the extra form step and ask for approval before changing the source journey. If DM collection must remain, leave the ongoing bridge unverified and prepare the exact mapping and next access action only.
3. Draft the email-to-list mapping and channel-specific consent record. Preserve opt-outs; prevent duplicate contacts and repeated welcome sends. Keep optional signup optional and do not withhold a resource that the selected Chatfuel variant delivers first.
4. Verify actual membership in the intended list; this can complete the list-growth goal. A saved Chatfuel email or a link click does not prove membership. Only if the owner requests a welcome email or series, draft sender, reply-to and unsubscribe settings and a separate consented delivery check before any later approved send. Return draft form/list settings, unresolved access and the next authorized action.
5. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
6. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
7. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
Official guidance checked 2026-11-02:
Brevo signup forms: https://help.brevo.com/hc/en-us/articles/208771869-Create-a-sign-up-form-in-Brevo
Authorized contact and list mapping: https://developers.brevo.com/docs/synchronise-contact-lists
Consent records: https://help.brevo.com/hc/en-us/articles/213405965-Build-a-legitimate-contacts-database-for-optimal-deliverability-and-compliance
Email and SMS automation actions: https://help.brevo.com/hc/en-us/articles/15445989568402-Available-triggers-actions-and-rules-in-an-automation
Optional email sender and message settings: https://help.brevo.com/hc/en-us/articles/24257124386066-Send-an-email-from-an-automation
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](follower-material-inro-6024.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
