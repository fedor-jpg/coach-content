# Live offer: reveal one coupon

Setup 1.1.0 | offers-manychat-63 | waiting_for_chatfuel | runtime not tested

## Business Result
Deliver a relevant product offer or coupon while interest is high.
Shops and creators using comments, Stories or Lives to promote an offer.
Source entry: Keyword comment during a Live
Source outcome: The SECRET10 coupon
Source requirements: Press the coupon-reveal button
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: The SECRET10 coupon
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- live: Post/comment configuration does not establish a Live-comment entry tool.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-63: Send offers in DMs during Live
Full captured settings/provenance: [selected source JSON](../source-records/manychat-63.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: comment, live
Captured text (not approved outbound copy):
```text

```
- Edge edge-1: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
I'm so excited you want my VIP-only secret coupon code. 🤫

Tap below to get it 👇
```
Captured buttons: ["Gimme the code! 🤫"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"I'm so excited you want my VIP-only secret coupon code. 🤫\n\nTap below to get it 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Gimme the code! 🤫","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: "Gimme the code! 🤫"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Oh yeah! Here's your special code:

SECRET10

Use it at checkout for 10% off sitewide. Hurry - it expires in 24 hours! ⏳
```
Captured buttons: ["Shop Now 🛍️"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Oh yeah! Here's your special code:\n\nSECRET10\n\nUse it at checkout for 10% off sitewide. Hurry - it expires in 24 hours! ⏳","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Shop Now 🛍️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebiste.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-63 / Finish the offer destination
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-63 - Send offers in DMs during Live.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Live offer: reveal one coupon
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Keyword comment during a Live
Source requirements: Press the coupon-reveal button
Source timing: No exact timer captured.
Source outcome: The SECRET10 coupon
Captured text (node-0, not approved campaign copy):
I'm so excited you want my VIP-only secret coupon code. 🤫

Tap below to get it 👇
Current setup decision: waiting_for_chatfuel. This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary Chatfuel result: The SECRET10 coupon
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
Structured audit: [setup record](offers-manychat-63.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
