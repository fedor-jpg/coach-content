# Live game: three coupons at 33/33/34

Setup 1.1.0 | games-manychat-57 | waiting_for_chatfuel | runtime not tested

## Business Result
Use a quiz or prize reveal to make participation rewarding.
Creators choosing between knowledge-based results and chance-based rewards.
Source entry: Keyword comment during a Live
Source outcome: One of three coupons
Source requirements: Press the button; Randomly distribute outcomes at 33%, 33%, 34%
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
The selected outcome requires random selection or allocation. Ordinary MCP cannot implement that selection; giving everyone the same reward is a different result.
Primary result: One of three coupons
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- live: Post/comment configuration does not establish a Live-comment entry tool.
- random: No weighted random prize distribution in normal tool inputs.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-57: Gamify Instagram live
Full captured settings/provenance: [selected source JSON](../source-records/manychat-57.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: live
Captured text (not approved outbound copy):
```text

```
- Edge edge-4: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Oooh are you ready to test your luck and reveal your discount?  Press the magic button👇
```
Captured buttons: ["I'm Lucky! ✨"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Oooh are you ready to test your luck and reveal your discount?  Press the magic button👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"I'm Lucky! ✨","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: "I'm Lucky! ✨"
#### node-1 (randomizer)
No weighted random outcomes in ordinary MCP. Do not substitute a deterministic message without consent.
Business input: approved changed outcome, if desired
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: random
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"randomized","label":null,"type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"range","value":"33","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":null,"min":"0","pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":"Value","type":"text","value":"33","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":"3","min":"0","pattern":"[0-9]*","required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"range","value":"34","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":null,"min":"0","pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":"Value","type":"text","value":"34","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":"100","maxlength":"3","min":"0","pattern":"[0-9]*","required":false}}
- Edge edge-1: node-1 -> node-2 | condition/label: "33% A"
- Edge edge-2: node-1 -> node-3 | condition/label: "33% B"
- Edge edge-3: node-1 -> node-4 | condition/label: "34% C"
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Congrats! You've unlocked 20% off sitewide for the next 24 hours only!

Simply use code LUCKY20 at and the discount will be automatically applied at checkout! 
```
Captured buttons: ["Go! Go! Go! 🔥"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Congrats! You've unlocked 20% off sitewide for the next 24 hours only!\n\nSimply use code LUCKY20 at and the discount will be automatically applied at checkout! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Go! Go! Go! 🔥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-3 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Congrats! You've scored our exclusive BOGO offer! 🎁

Simply buy one item and you'll get the second item (of equal or lesser value) for FREE!

Simply add your two items to your cart, and code BOGOBABE at checkout.
```
Captured buttons: ["Shop Now 🛍️"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Congrats! You've scored our exclusive BOGO offer! 🎁\n\nSimply buy one item and you'll get the second item (of equal or lesser value) for FREE!\n\nSimply add your two items to your cart, and code BOGOBABE at checkout.","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Shop Now 🛍️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-4 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Congrats! You've scored 15% your next purchase!  🎁

Simply use code LUCKY15 at and the discount will be automatically applied at checkout! 
```
Captured buttons: ["Redeem Code 🛍️"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Congrats! You've scored 15% your next purchase!  🎁\n\nSimply use code LUCKY15 at and the discount will be automatically applied at checkout! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Redeem Code 🛍️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-57 / Finish the offer destination
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-57 - Gamify Instagram live.
Goal: Use a quiz or prize reveal to make participation rewarding.
Variant: Live game: three coupons at 33/33/34
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Keyword comment during a Live
Source requirements: Press the button; Randomly distribute outcomes at 33%, 33%, 34%
Source timing: No exact timer captured.
Source outcome: One of three coupons
Captured text (node-0, not approved campaign copy):
Oooh are you ready to test your luck and reveal your discount?  Press the magic button👇
Current setup decision: waiting_for_chatfuel. The selected outcome requires random selection or allocation. Ordinary MCP cannot implement that selection; giving everyone the same reward is a different result.
Primary Chatfuel result: One of three coupons
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
Structured audit: [setup record](games-manychat-57.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
