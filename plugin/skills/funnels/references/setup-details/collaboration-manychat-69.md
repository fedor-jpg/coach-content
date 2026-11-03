# Collaboration enquiry: collect email only if missing

Setup 1.1.0 | collaboration-manychat-69 | waiting_for_chatfuel | runtime not tested

## Business Result
Make it easy for a potential partner to reach the right contact.
Creators and brands considering co-branded partnerships.
Source entry: Keyword reply to a Story
Source outcome: A mailto link for collaboration
Source requirements: Existing email: show the team contact; Missing email: collect it, then show the contact
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
This scenario starts from a Story reply. Ordinary MCP cannot configure the Story-specific entry. An ordinary DM keyword would be a different entry, not this setup.
Primary result: A mailto link for collaboration
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- story: Story-specific configuration is dashboard-only for normal MCP. Ordinary DM does not verify a Story reply or mention.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-69: Answer FAQs from story replies
Full captured settings/provenance: [selected source JSON](../source-records/manychat-69.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, story
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"collab","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"partnership","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-3: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Field (inspection_variant): {"name":"","value":""}
- Field (inspection_variant): {"name":"","checked":true}
- Edge edge-1: node-0 -> node-1 | condition/label: "Yes, the contact matches"
- Edge edge-2: node-0 -> node-2 | condition/label: "If not"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Yes! I accept select co-branded partnership opportunities, so tap the button below to reach out to me (and my team) to see if you're a good fit! 👇  
```
Captured buttons: ["Email Me📥 "]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Yes! I accept select co-branded partnership opportunities, so tap the button below to reach out to me (and my team) to see if you're a good fit! 👇  ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Email Me📥 ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"mailto:yourname@yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
I'm so excited you'd like to collab with me!

I only discuss co-branded partnership opportunities via email, so my team can help with the outreach.

So we can contact you, enter your email address below. 👇

Thanks, I've got your email! 
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"I'm so excited you'd like to collab with me!\n\nI only discuss co-branded partnership opportunities via email, so my team can help with the outreach.\n\nSo we can contact you, enter your email address below. 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Thanks, I've got your email! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"saveEmailToSystemField","label":"Save Email to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"setEmailOptIn","label":"Set Email Opt-In ","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Please enter a correct email address, e.g. me@mail.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"value":"23"}
- Field (captured_default): {"value":"hours","options":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}]}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Edge edge-0: node-2 -> node-3 | condition/label: "Next Step"
#### node-3 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Feel free to reach out to my team to outline your co-branded partnership opportunity via the button below! 👇
```
Captured buttons: ["Email Me📥 "]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Feel free to reach out to my team to outline your co-branded partnership opportunity via the button below! 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Email Me📥 ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"mailto:yourname@yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
### manychat-251: Get more collabs from Story replies
Full captured settings/provenance: [selected source JSON](../source-records/manychat-251.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, story
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"collab","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"partnership","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-3: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Edge edge-1: node-0 -> node-1 | condition/label: "Yes, the contact matches"
- Edge edge-2: node-0 -> node-2 | condition/label: "If not"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Yes! I accept select co-branded partnership opportunities, so tap the button below to reach out to me (and my team) to see if you're a good fit! 👇  
```
Captured buttons: ["Email Me📥 "]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Yes! I accept select co-branded partnership opportunities, so tap the button below to reach out to me (and my team) to see if you're a good fit! 👇  ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Email Me📥 ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"mailto:yourname@yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
I'm so excited you'd like to collab with me!

I only discuss co-branded partnership opportunities via email, so my team can help with the outreach.

So we can contact you, enter your email address below. 👇

Thanks, I've got your email! 
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"I'm so excited you'd like to collab with me!\n\nI only discuss co-branded partnership opportunities via email, so my team can help with the outreach.\n\nSo we can contact you, enter your email address below. 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Thanks, I've got your email! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"saveEmailToSystemField","label":"Save Email to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"setEmailOptIn","label":"Set Email Opt-In ","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Please enter a correct email address, e.g. me@mail.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"value":"23"}
- Field (captured_default): {"value":"hours","options":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}]}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Edge edge-0: node-2 -> node-3 | condition/label: "Next Step"
#### node-3 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Feel free to reach out to my team to outline your co-branded partnership opportunity via the button below! 👇
```
Captured buttons: ["Email Me📥 "]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Feel free to reach out to my team to outline your co-branded partnership opportunity via the button below! 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Email Me📥 ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"mailto:yourname@yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](collaboration-manychat-69.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
