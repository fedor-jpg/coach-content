# Giveaway: captured 95/5 random split

Setup 1.1.0 | giveaway-manychat-105 | waiting_for_chatfuel | runtime not tested

## Business Result
Invite participation and apply the giveaway rules before confirming an entry.
Businesses running a campaign with clear eligibility and prize rules.
Source entry: Comment tagging another person
Source outcome: One of two giveaway outcomes
Source requirements: Check started_giveaway; Choose between random outcomes with 95% and 5% weights
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
The selected outcome requires random selection or allocation. Ordinary MCP cannot implement that selection; giving everyone the same reward is a different result.
Primary result: One of two giveaway outcomes
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- random: No weighted random prize distribution in normal tool inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- Missing source behavior: Resolve the gate/notes and 95%/5% outcome conflict without correcting the original record.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-105: Run a giveaway
Full captured settings/provenance: [selected source JSON](../source-records/manychat-105.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"replies.0.reply","label":null,"type":null,"value":"Link in your DMs, check it out! 🚀","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.1.reply","label":null,"type":null,"value":"Done! Details in your inbox 📩","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.2.reply","label":null,"type":null,"value":"Sent the info, check DMs! 📂","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-1: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Edge edge-2: node-0 -> node-1 | condition/label: "Yes, the contact matches"
- Edge edge-3: node-0 -> node-6 | condition/label: "If not"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Hey! Are you ready to see if you're one of our winners for our Pilates Pack giveaway? 

Hit the button below to test your luck 👇
```
Captured buttons: ["LET'S GOOOO! 🔥"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hey! Are you ready to see if you're one of our winners for our Pilates Pack giveaway? \n\nHit the button below to test your luck 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"LET'S GOOOO! 🔥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-1 -> node-2 | condition/label: "LET'S GOOOO! 🔥"
#### node-2 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":"Tag picker","type":null,"value":"started_giveaway","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-4: node-2 -> node-3 | condition/label: "Next Step"
#### node-3 (randomizer)
No weighted random outcomes in ordinary MCP. Do not substitute a deterministic message without consent.
Business input: approved changed outcome, if desired
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: random
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"randomized","label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"range","value":"95","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":null,"min":"0","pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":"Value","type":"text","value":"95","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":"3","min":"0","pattern":"[0-9]*","required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"range","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":null,"min":"0","pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":"Value","type":"text","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":"3","min":"0","pattern":"[0-9]*","required":false}}
- Field (captured_default): {"name":"randomized","label":"Pick a random path every time ","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":null,"type":"range","value":"95","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":"100","maxlength":null,"min":"0","minlength":null,"pattern":null,"required":false,"step":"1"}}
- Field (captured_default): {"name":null,"label":"Value","type":"text","value":"95","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":"numeric","max":"100","maxlength":"3","min":"0","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Field (captured_default): {"name":null,"label":null,"type":"range","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":"100","maxlength":null,"min":"0","minlength":null,"pattern":null,"required":false,"step":"1"}}
- Field (captured_default): {"name":null,"label":"Value","type":"text","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":"numeric","max":"100","maxlength":"3","min":"0","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Field (inspection_variant): {"name":"randomized","label":null,"type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":"range","value":"95","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":null,"min":"0","pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":"Value","type":"text","value":"95","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":"3","min":"0","pattern":"[0-9]*","required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":"range","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":null,"min":"0","pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":"Value","type":"text","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":"3","min":"0","pattern":"[0-9]*","required":false}}
- Edge edge-5: node-3 -> node-4 | condition/label: "95% A"
- Edge edge-6: node-3 -> node-5 | condition/label: "5% B"
#### node-4 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Congrats! You're one of our lucky winners! 🥳

Click the button below to enter your details so we can send your prize  👇
```
Captured buttons: ["Claim My Prize 🎁"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Congrats! You're one of our lucky winners! 🥳\n\nClick the button below to enter your details so we can send your prize  👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Claim My Prize 🎁","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-5 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
We're sorry! You're not a lucky winner... This time. 

Yeah, we're bummed, too. 😭

But don't worry — we'll announce an new giveaway soon! Stay tuned. ❤️️
```
Captured buttons: ["Visit Website🌐"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"We're sorry! You're not a lucky winner... This time. \n\nYeah, we're bummed, too. 😭\n\nBut don't worry — we'll announce an new giveaway soon! Stay tuned. ❤️️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Visit Website🌐","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-6 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Oops! You've already entered. It's only one entry per person.  ✨
But we have some other cool Pilates stuff on our website. Check it out 👇
```
Captured buttons: ["Visit website 🌐"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Oops! You've already entered. It's only one entry per person.  ✨\nBut we have some other cool Pilates stuff on our website. Check it out 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Visit website 🌐","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](giveaway-manychat-105.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
