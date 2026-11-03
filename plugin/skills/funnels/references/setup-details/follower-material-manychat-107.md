# Follow first, then freebie: check and retry

Setup 1.1.0 | follower-material-manychat-107 | waiting_for_chatfuel | runtime not tested

## Business Result
Offer a useful resource in exchange for a verified follow.
Creators who want access to depend on following, not just an invitation to follow.
Source entry: Keyword comment
Source outcome: A guide only after the follower check succeeds
Source requirements: Ask the person to follow; Check: true delivers the guide; false offers another check
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary result: A guide only after the follower check succeeds
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- follower: No Instagram follower condition or follow/check/retry gate in normal tool inputs.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-107: Follow first, then freebie
Full captured settings/provenance: [selected source JSON](../source-records/manychat-107.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"replies.0.reply","label":null,"type":null,"value":"Link's in your DMs 📥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.1.reply","label":null,"type":null,"value":"Sent! The link is with you now 💌","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.2.reply","label":null,"type":null,"value":"Done! Kindly check your DMs 🌟","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"replies.0.reply","label":null,"type":null,"value":"Link's in your DMs 📥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"replies.1.reply","label":null,"type":null,"value":"Sent! The link is with you now 💌","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"replies.2.reply","label":null,"type":null,"value":"Done! Kindly check your DMs 🌟","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"replies.3.reply","label":null,"type":null,"value":"Sent the info! Check messages 📨","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-0: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Hey, I'm so glad you want my Ultimate Luxury Guide to the Amalfi Coast. 

This is exclusive to my followers, so follow my account and I'll DM you the guide! La Dolce Vita ❤️️
```
Captured buttons: ["I'm following you✅"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hey, I'm so glad you want my Ultimate Luxury Guide to the Amalfi Coast. \n\nThis is exclusive to my followers, so follow my account and I'll DM you the guide! La Dolce Vita ❤️️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_observation): {"name":"text","label":null,"type":null,"value":"Hey, I'm so glad you want my Ultimate Luxury Guide to the Amalfi Coast. \n\nThis is exclusive to my followers, so follow my account and I'll DM you the guide! La Dolce Vita ❤️️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"I'm following you✅","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-2: node-0 -> node-1 | condition/label: "I'm following you✅"
#### node-1 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: follower, graph
Captured text (not approved outbound copy):
```text

```
- Edge edge-3: node-1 -> node-2 | condition/label: "Yes, the contact matches"
- Edge edge-4: node-1 -> node-3 | condition/label: "If not"
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Oh yeah! I'm so happy you're following me! 💅

Here's your followers-only access to my guide! 👇 
```
Captured buttons: ["Get Guide📖"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Oh yeah! I'm so happy you're following me! 💅\n\nHere's your followers-only access to my guide! 👇 ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Get Guide📖","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
#### node-3 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Well, this is embarrassing... 😳

It says you're not following me. Would you mind trying again? 

Hit the button below when you're done 👇
```
Captured buttons: ["I'm following! ✅"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Well, this is embarrassing... 😳\n\nIt says you're not following me. Would you mind trying again? \n\nHit the button below when you're done 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"I'm following! ✅","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-1: node-3 -> node-1 | condition/label: "I'm following! ✅"
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](follower-material-manychat-107.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
