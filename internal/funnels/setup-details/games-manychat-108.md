# Qualify with a three-question scored quiz

Setup 1.1.0 | games-manychat-108 | waiting_for_chatfuel | runtime not tested

## Business Result
Use a quiz or prize reveal to make participation rewarding.
Creators choosing between knowledge-based results and chance-based rewards.
Source entry: Keyword direct message
Source outcome: A score-based result and coupon
Source requirements: Check whether the quiz was already taken; Ask three questions; Use score thresholds for different results
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
The quiz requires persistent scoring and score-dependent outcomes. Ordinary MCP has no score updates or score conditions.
Primary result: A score-based result and coupon
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- score: No deterministic score arithmetic, thresholds or quiz-attempt guard in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- Missing source behavior: Score fields, initial value, increments and thresholds are unknown. The inspected points is unknown condition is not the original rule.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-108: Qualify with a quiz
Full captured settings/provenance: [selected source JSON](../source-records/manychat-108.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"quiz","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-28: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Edge edge-9: node-0 -> node-1 | condition/label: "Yes, the contact matches"
- Edge edge-10: node-0 -> node-21 | condition/label: "If not"
#### node-1 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":"Tag picker","type":null,"value":"quiz_started","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"","value":""}
- Edge edge-15: node-1 -> node-2 | condition/label: "Next Step"
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Let the games begin! Answer these 3 questions to check your IG mastery level. (Answer 2 of 3 correctly to get a special gift! 👀)

#1: What's the worst way to grow on Instagram? 
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Let the games begin! Answer these 3 questions to check your IG mastery level. (Answer 2 of 3 correctly to get a special gift! 👀)\n\n#1: What's the worst way to grow on Instagram? ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"0afee189-abee-42bf-9a50-56ad94bfec3c","label":null,"type":null,"value":"Buying followers","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"94b8637c-637f-4d46-85aa-71abb60aa899","label":null,"type":null,"value":"DM automation","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"04328247-8ec8-4bb0-a2c5-00cdda86a6fb","label":null,"type":null,"value":"Daily stories/posts","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-0: node-2 -> node-3 | condition/label: "Buying followers"
- Edge edge-1: node-2 -> node-20 | condition/label: "DM automation"
- Edge edge-2: node-2 -> node-20 | condition/label: "Daily stories/posts"
#### node-3 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"","value":""}
- Edge edge-16: node-3 -> node-4 | condition/label: "Next Step"
#### node-4 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Let's GO! Posting frequently and combining it with Manychat's DM automation can SKYROCKET your account!  Buying followers? Not so much. 😎
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Let's GO! Posting frequently and combining it with Manychat's DM automation can SKYROCKET your account!  Buying followers? Not so much. 😎","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-17: node-4 -> node-5 | condition/label: "Next Step"
#### node-5 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
#2: What's the NEW ratio for Instagram's grid photos? 👀
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"#2: What's the NEW ratio for Instagram's grid photos? 👀","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"15a85c4d-1fd7-4c71-8c7f-fd6e7dc9f0e9","label":null,"type":null,"value":"16:9","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"19559032-f32c-4d61-bc96-c7eb54dc75e8","label":null,"type":null,"value":"4:5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"73cda9a2-fc12-4d9d-a3f5-384c599812af","label":null,"type":null,"value":"1:1","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-3: node-5 -> node-6 | condition/label: "16:9"
- Edge edge-4: node-5 -> node-17 | condition/label: "4:5"
- Edge edge-5: node-5 -> node-19 | condition/label: "1:1"
#### node-6 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
No, sorry! 😔

Tricky tricky. We got you! That's a HDTV ratio! 🎥

Correct answer is 4:5. 
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"No, sorry! 😔","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Tricky tricky. We got you! That's a HDTV ratio! 🎥\n\nCorrect answer is 4:5. ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-18: node-6 -> node-7 | condition/label: "Next Step"
#### node-7 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Edge edge-11: node-7 -> node-8 | condition/label: "Yes, the contact matches"
- Edge edge-12: node-7 -> node-9 | condition/label: "If not"
#### node-8 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Don't worry! One more question left! 😊
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Don't worry! One more question left! 😊","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"5","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-19: node-8 -> node-9 | condition/label: "Next Step"
#### node-9 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Last question. Our toughest yet.

Who is the current CEO of Instagram?
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Last question. Our toughest yet.\n\nWho is the current CEO of Instagram?","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"dc689da4-edf8-4eeb-b777-793fb8ab9daf","label":null,"type":null,"value":"Mark Zuckerberg","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"4e1883a0-aba3-4dca-9fb5-ca9040be9ade","label":null,"type":null,"value":"Sheryl Sandberg","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"6cfba9b8-e483-4e34-bcf5-ece37d77efde","label":null,"type":null,"value":"Adam Mosseri","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-6: node-9 -> node-10 | condition/label: "Mark Zuckerberg"
- Edge edge-7: node-9 -> node-14 | condition/label: "Sheryl Sandberg"
- Edge edge-8: node-9 -> node-15 | condition/label: "Adam Mosseri"
#### node-10 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Nope! Mr. Zuckerberg is the CEO of Meta, not Instagram! 

(You can be forgiven for mistaking that one!) 😏
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Nope! Mr. Zuckerberg is the CEO of Meta, not Instagram! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"(You can be forgiven for mistaking that one!) 😏","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-20: node-10 -> node-11 | condition/label: "Next Step"
#### node-11 (condition)
Preserve true/false exits, field values and retry loops. No deterministic condition import.
Business input: mandatory business condition
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Edge edge-13: node-11 -> node-12 | condition/label: "Yes, the contact matches"
- Edge edge-14: node-11 -> node-13 | condition/label: "If not"
#### node-12 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Congratulations, you got {No field selected} points out of 60 ❤️ and we're so proud of you!

And we think you deserve a 10% off to enjoy our expert Instagram course. 👀

Code: 

#quizguru 

Now don't tell anyone... 🤫

Check out the course details and redeem your discount here. 👇
```
Captured buttons: ["Try our course!"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Congratulations, you got {No field selected} points out of 60 ❤️ and we're so proud of you!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"And we think you deserve a 10% off to enjoy our expert Instagram course. 👀\n\nCode: \n\n#quizguru ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Now don't tell anyone... 🤫","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Check out the course details and redeem your discount here. 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Try our course!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"www.manychat.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-13 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
{First Name}, so you got {No field selected} points out of 60, but we're proud of you anyway. 🥲

Learning new things is filled with challenges and we're happy to have been alongside you for this ride! 

Because you're such a great sport, we  wanna to share a special 15% off promo code to enjoy our amazing course for fans of Instagram! 🥳

Use code this code at checkout:

quizrocket

Check out the course details and redeem the discount here !👇
```
Captured buttons: ["Try our course!"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"{First Name}, so you got {No field selected} points out of 60, but we're proud of you anyway. 🥲","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Learning new things is filled with challenges and we're happy to have been alongside you for this ride! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Because you're such a great sport, we  wanna to share a special 15% off promo code to enjoy our amazing course for fans of Instagram! 🥳","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Use code this code at checkout:\n\nquizrocket\n\nCheck out the course details and redeem the discount here !👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Try our course!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"www.manychat.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-14 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
No, sorry! Ms. Sandberg, famous for her book "Lean In," was COO of Meta until 2022!

It's okay. We were extra tricky. 😇
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"No, sorry! Ms. Sandberg, famous for her book \"Lean In,\" was COO of Meta until 2022!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"It's okay. We were extra tricky. 😇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-21: node-14 -> node-11 | condition/label: "Next Step"
#### node-15 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"","value":""}
- Edge edge-22: node-15 -> node-16 | condition/label: "Next Step"
#### node-16 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
You're correct! 👏👏👏
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"You're correct! 👏👏👏","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-23: node-16 -> node-11 | condition/label: "Next Step"
#### node-17 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph, score
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"","value":""}
- Edge edge-24: node-17 -> node-18 | condition/label: "Next Step"
#### node-18 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Heck yes! 😍 Are you a genius? (Don't answer that, we KNOW you are.)
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Heck yes! 😍 Are you a genius? (Don't answer that, we KNOW you are.)","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-25: node-18 -> node-9 | condition/label: "Next Step"
#### node-19 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Not anymore! 

1:1 used to be the grid's famed square. But things have changed (you should probably go check).

Correct answer is 4:5. 💌
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Not anymore! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"1:1 used to be the grid's famed square. But things have changed (you should probably go check).\n\nCorrect answer is 4:5. 💌","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"3","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- Edge edge-26: node-19 -> node-7 | condition/label: "Next Step"
#### node-20 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Oops! 🫣

Posting frequently and combining it with  DM automation with Manychat will actually do the OPPOSITE, you silly goose. 😉

We were looking for "Buying followers." 💅
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Oops! 🫣","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Posting frequently and combining it with  DM automation with Manychat will actually do the OPPOSITE, you silly goose. 😉","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"We were looking for \"Buying followers.\" 💅","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-27: node-20 -> node-5 | condition/label: "Next Step"
#### node-21 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Looks like you have already taken the quiz! Sorry, friend! 
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Looks like you have already taken the quiz! Sorry, friend! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](games-manychat-108.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
