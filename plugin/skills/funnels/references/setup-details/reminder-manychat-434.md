# Brands campaign: no click after 23 hours

Setup 1.1.0 | reminder-manychat-434 | waiting_for_chatfuel | runtime not tested

## Business Result
Follow up with interested people who have not opened the offer.
Brands adding a conditional reminder to an existing campaign.
Source entry: Comment in a Brands campaign
Source outcome: A reminder only if the link was not clicked
Source requirements: Opening button and link; Tag the link click; Check the tag after 23 hours
Source timing: Delay: 23 hours.

## Functional Availability
waiting_for_chatfuel
The primary result is a reminder only after a verified non-click and exact delay. Ordinary MCP cannot observe that condition or configure that timer. Generic silence follow-ups are not a substitute.
Primary result: A reminder only if the link was not clicked
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
- Missing source behavior: The click tag and positive condition exit are unset.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-434: *Follow-up (Manychat for Brands)
Full captured settings/provenance: [selected source JSON](../source-records/manychat-434.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"replies.0.reply","label":null,"type":null,"value":"Done! Details in your inbox 📩","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.1.reply","label":null,"type":null,"value":"Info sent! Check your DMs 📬","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.2.reply","label":null,"type":null,"value":"Done! Your DMs have the details 📌","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-2: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Thanks for your comment! Want the link? Tap below and I'll send it 
```
Captured buttons: [" Send me the link"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Thanks for your comment! Want the link? Tap below and I'll send it ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":" Send me the link","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: " Send me the link"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Here you go! 👇
```
Captured buttons: ["Get the link"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Here you go! 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Get the link","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourlink.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-3: node-1 -> node-5 | condition/label: "button-0.additional-actions"
- Edge edge-4: node-1 -> node-2 | condition/label: "Next Step"
#### node-2 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"23","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"delayUnits","label":null,"type":null,"value":"hours","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Field (captured_default): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"23","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"delayUnits","label":null,"type":null,"value":"hours","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"value":"seconds"}
- Field (inspection_variant): {"value":"minutes"}
- Field (inspection_variant): {"value":"hours"}
- Field (inspection_variant): {"value":"days"}
- Field (inspection_variant): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"from","label":null,"type":null,"value":"8","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"0:00","value":"0"},{"selected":false,"text":"1:00","value":"1"},{"selected":false,"text":"2:00","value":"2"},{"selected":false,"text":"3:00","value":"3"},{"selected":false,"text":"4:00","value":"4"},{"selected":false,"text":"5:00","value":"5"},{"selected":false,"text":"6:00","value":"6"},{"selected":false,"text":"7:00","value":"7"},{"selected":true,"text":"8:00","value":"8"},{"selected":false,"text":"9:00","value":"9"},{"selected":false,"text":"10:00","value":"10"},{"selected":false,"text":"11:00","value":"11"},{"selected":false,"text":"12:00","value":"12"},{"selected":false,"text":"13:00","value":"13"},{"selected":false,"text":"14:00","value":"14"},{"selected":false,"text":"15:00","value":"15"},{"selected":false,"text":"16:00","value":"16"},{"selected":false,"text":"17:00","value":"17"},{"selected":false,"text":"18:00","value":"18"},{"selected":false,"text":"19:00","value":"19"},{"selected":false,"text":"20:00","value":"20"},{"selected":false,"text":"21:00","value":"21"},{"selected":false,"text":"22:00","value":"22"},{"selected":false,"text":"23:00","value":"23"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"value":"0"}
- Field (inspection_variant): {"value":"1"}
- Field (inspection_variant): {"value":"2"}
- Field (inspection_variant): {"value":"3"}
- Field (inspection_variant): {"value":"4"}
- Field (inspection_variant): {"value":"5"}
- Field (inspection_variant): {"value":"6"}
- Field (inspection_variant): {"value":"7"}
- Field (inspection_variant): {"value":"8"}
- Field (inspection_variant): {"value":"9"}
- Field (inspection_variant): {"value":"10"}
- Field (inspection_variant): {"value":"11"}
- Field (inspection_variant): {"value":"12"}
- Field (inspection_variant): {"value":"13"}
- Field (inspection_variant): {"value":"14"}
- Field (inspection_variant): {"value":"15"}
- Field (inspection_variant): {"value":"16"}
- Field (inspection_variant): {"value":"17"}
- Field (inspection_variant): {"value":"18"}
- Field (inspection_variant): {"value":"19"}
- Field (inspection_variant): {"value":"20"}
- Field (inspection_variant): {"value":"21"}
- Field (inspection_variant): {"value":"22"}
- Field (inspection_variant): {"value":"23"}
- Field (inspection_variant): {"name":"to","label":null,"type":null,"value":"22","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"1:00","value":"1"},{"selected":false,"text":"2:00","value":"2"},{"selected":false,"text":"3:00","value":"3"},{"selected":false,"text":"4:00","value":"4"},{"selected":false,"text":"5:00","value":"5"},{"selected":false,"text":"6:00","value":"6"},{"selected":false,"text":"7:00","value":"7"},{"selected":false,"text":"8:00","value":"8"},{"selected":false,"text":"9:00","value":"9"},{"selected":false,"text":"10:00","value":"10"},{"selected":false,"text":"11:00","value":"11"},{"selected":false,"text":"12:00","value":"12"},{"selected":false,"text":"13:00","value":"13"},{"selected":false,"text":"14:00","value":"14"},{"selected":false,"text":"15:00","value":"15"},{"selected":false,"text":"16:00","value":"16"},{"selected":false,"text":"17:00","value":"17"},{"selected":false,"text":"18:00","value":"18"},{"selected":false,"text":"19:00","value":"19"},{"selected":false,"text":"20:00","value":"20"},{"selected":false,"text":"21:00","value":"21"},{"selected":true,"text":"22:00","value":"22"},{"selected":false,"text":"23:00","value":"23"},{"selected":false,"text":"0:00","value":"0"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"SET_TO_SPECIFIC_DATE","value_state":"observed","checked":false,"options_exact":[{"selected":true,"text":"Specific date","value":"SET_TO_SPECIFIC_DATE"},{"selected":false,"text":"Dynamic date","value":"SET_TO_CUF"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"value":"SET_TO_SPECIFIC_DATE"}
- Field (inspection_variant): {"value":"SET_TO_CUF"}
- Field (inspection_variant): {"name":"waitUntil","label":null,"type":"text","value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"Smart Delay","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"SET_TO_CUF","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"Specific date","value":"SET_TO_SPECIFIC_DATE"},{"selected":true,"text":"Dynamic date","value":"SET_TO_CUF"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"waitUntil","label":"Date time picker","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"value","label":"Delay time","type":"text","value":"1","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"99999","maxlength":null,"min":"0","pattern":"[0-9]*","required":false}}
- Field (inspection_variant): {"name":"unit","label":null,"type":null,"value":"days","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"Minutes","value":"minutes"},{"selected":false,"text":"Hours","value":"hours"},{"selected":true,"text":"Days","value":"days"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (restoration_check): {"name":null,"label":null,"type":null,"value":"23","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (restoration_check): {"name":"delayUnits","label":null,"type":null,"value":"hours","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (restoration_check): {"value":"seconds"}
- Field (restoration_check): {"value":"minutes"}
- Field (restoration_check): {"value":"hours"}
- Field (restoration_check): {"value":"days"}
- Field (restoration_check): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-5: node-2 -> node-3 | condition/label: "Next Step"
#### node-3 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Edge edge-1: node-3 -> node-4 | condition/label: "If not"
#### node-4 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Still thinking about it? Your link is right here 👇
```
Captured buttons: ["Get the link"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Still thinking about it? Your link is right here 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Get the link","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourlink.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-5 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":"Tag picker","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](reminder-manychat-434.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
