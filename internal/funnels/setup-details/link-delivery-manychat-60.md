# Live comment to one private link

Setup 1.1.0 | link-delivery-manychat-60 | waiting_for_chatfuel | runtime not tested

## Business Result
Put the requested guide, resource or destination in the conversation.
Creators and businesses offering a useful next step without a required contact or follow.
Source entry: Keyword comment during a Live
Source outcome: One private message with a link
Source requirements: Enter through the Live-comment trigger
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: One private message with a link
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- live: Post/comment configuration does not establish a Live-comment entry tool.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-60: Trigger DMs during IG Live
Full captured settings/provenance: [selected source JSON](../source-records/manychat-60.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: comment, live
Captured text (not approved outbound copy):
```text

```
- Edge edge-0: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
You made it to the Live!

Wanna grab that free ebook? It’s yours 👇👇
```
Captured buttons: ["CLICK HERE 🔥"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"You made it to the Live!\n\nWanna grab that free ebook? It’s yours 👇👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"CLICK HERE 🔥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"https://www.youtube.com/watch?v=hNIAaQ8dZC0&ab_channel=Manychat","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](link-delivery-manychat-60.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
