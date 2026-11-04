# Reel coupon: help after 2 minutes

Setup 1.1.0 | offers-manychat-72 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Deliver a relevant product offer or coupon while interest is high.
Shops and creators using comments, Stories or Lives to promote an offer.
Source entry: Comment on a Reel
Source outcome: The HAPPY10 coupon and a help message
Source requirements: Press the opening button; Receive unconditional help after 2 minutes
Source timing: Unconditional delay: 2 minutes. The 48-hour validity appears only in copy.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Send the coupon, store URL and captured help copy together after confirmation.
Retained/replaced: Send the coupon, store URL and captured help copy together after confirmation.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Unconditional delay: 2 minutes. The 48-hour validity appears only in copy.. No timed unsolicited message is configured.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the coupon, store URL and captured help copy together after confirmation.
Target: owned_comment
Ask only for missing business facts:
- offer_title: Supply the business value and approve its use in this selected draft. (required)
- coupon_code: Supply the business value and approve its use in this selected draft. (required)
- offer_terms: Supply the business value and approve its use in this selected draft. (required)
- store_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Want {offer_title}? Reply YES for the coupon.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Your code is {coupon_code}
{offer_terms}
{store_url}

Is the code working for you? If you have any questions about the Happy Beans range, I'm happy to help ❤️
help: Is the code working for you? If you have any questions about the Happy Beans range, I'm happy to help ❤️
Only after an actual affirmative reply, deliver the coupon, approved terms, store URL and complete help sentence TOGETHER in one response. The captured two-minute separate send is not retained. Do not send a timed second message. Confirm offer terms and brand facts before using the captured help copy. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Selected entry received -> first
- first: Ask for an actual affirmative reply; no link yet.
  - If Actual affirmative reply in this conversation -> delivery
  - If Actual refusal -> refusal
  - If No actual reply -> silence
- delivery: Deliver the approved destination and included help together.
  - If Actual bare HELP reply -> help
  - If Actual concrete question -> answer
- help: Only for bare HELP, ask what assistance is needed.
  - If Actual question or problem details in a new reply -> answer
- refusal: End this request without delivering gated content.
- silence: No message after silence.
- answer: Answer a concrete question only from approved facts; otherwise state that human review is needed. Do not repeat the help invitation or claim an unconfigured transfer.
#### Exact Setting Drafts
Not tool calls. Add resolved botID/automationID and privacy-safe context only after all gates; one setting per call.
```json
[
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "publicReply": {
        "publicReplyHowToReply": "ExactText",
        "exactTextReply": "{public_text}"
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "privateReply": {
        "privateReplyHowToReply": "ExactText",
        "exactTextReply": "Want {offer_title}? Reply YES for the coupon."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {offer_title}? Reply YES for the coupon.\nOnly after an actual affirmative reply, deliver the coupon, approved terms, store URL and complete help sentence TOGETHER in one response. The captured two-minute separate send is not retained. Do not send a timed second message. Confirm offer terms and brand facts before using the captured help copy. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Your code is {coupon_code}\n{offer_terms}\n{store_url}\n\nIs the code working for you? If you have any questions about the Happy Beans range, I'm happy to help ❤️\nhelp: Is the code working for you? If you have any questions about the Happy Beans range, I'm happy to help ❤️ The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "whenAIReplies": {
        "option": "Always"
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "followUps": {
        "howToSend": "DontSend"
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-72: Sell from Reel comments
Full captured settings/provenance: [selected source JSON](../source-records/manychat-72.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"replies.0.reply","label":null,"type":null,"value":"Check your DMs, info is there 🎉","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.1.reply","label":null,"type":null,"value":"Details sent! Peek at your DMs 📧","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.2.reply","label":null,"type":null,"value":"Sent! Look in your messages 📥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-3: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Hey! Tap below to get your coupon code for 10% off your first purchase of Happy Beans Vitamins 👇 
```
Captured buttons: ["Get Code 💊"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hey! Tap below to get your coupon code for 10% off your first purchase of Happy Beans Vitamins 👇 ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Get Code 💊","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: "Get Code 💊"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Your code is HAPPY10

Use it at checkout for 10% off (expires in 48 hours!)
```
Captured buttons: ["Shop Now 🛍️"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Your code is HAPPY10\n\nUse it at checkout for 10% off (expires in 48 hours!)","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Shop Now 🛍️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-1: node-1 -> node-2 | condition/label: "Next Step"
#### node-2 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"2","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"delayUnits","label":null,"type":null,"value":"minutes","value_state":"observed","checked":false,"options_exact":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":true,"text":"Minutes","value":"minutes"},{"selected":false,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}],"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Field (captured_default): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-2: node-2 -> node-3 | condition/label: "Next Step"
#### node-3 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Is the code working for you? If you have any questions about the Happy Beans range, I'm happy to help ❤️
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Is the code working for you? If you have any questions about the Happy Beans range, I'm happy to help ❤️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-72 / Finish the offer destination
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-72 - Sell from Reel comments.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Reel coupon: help after 2 minutes
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Comment on a Reel
Source requirements: Press the opening button; Receive unconditional help after 2 minutes
Source timing: Unconditional delay: 2 minutes. The 48-hour validity appears only in copy.
Source outcome: The HAPPY10 coupon and a help message
Captured text (node-0, not approved campaign copy):
Hey! Tap below to get your coupon code for 10% off your first purchase of Happy Beans Vitamins 👇 
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Send the coupon, store URL and captured help copy together after confirmation.
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
Structured audit: [setup record](offers-manychat-72.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
