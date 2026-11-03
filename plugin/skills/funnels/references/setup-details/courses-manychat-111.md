# Sell courses: three cards and help

Setup 1.1.0 | courses-manychat-111 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Present the right course and help interested learners reach the offer.
Educators selling one course or a small course catalogue.
Source entry: Keyword direct message
Source outcome: A choice of three courses
Source requirements: Three-course gallery; Separate card and purchase URLs; A following help message
Source timing: No exact timer captured.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Offer three named courses with all six detail/purchase URLs and a help branch.
Retained/replaced: Offer three named courses with all six detail/purchase URLs and a help branch.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Offer three named courses with all six detail/purchase URLs and a help branch.
Target: dm_base
Ask only for missing business facts:
- course_one_title: Supply the business value and approve its use in this selected draft. (required)
- course_one_terms: Supply the business value and approve its use in this selected draft. (required)
- course_one_card_url: Supply the business value and approve its use in this selected draft. (required)
- course_one_purchase_url: Supply the business value and approve its use in this selected draft. (required)
- course_two_title: Supply the business value and approve its use in this selected draft. (required)
- course_two_terms: Supply the business value and approve its use in this selected draft. (required)
- course_two_card_url: Supply the business value and approve its use in this selected draft. (required)
- course_two_purchase_url: Supply the business value and approve its use in this selected draft. (required)
- course_three_title: Supply the business value and approve its use in this selected draft. (required)
- course_three_terms: Supply the business value and approve its use in this selected draft. (required)
- course_three_card_url: Supply the business value and approve its use in this selected draft. (required)
- course_three_purchase_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, help_text, refusal_text, handoff_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Choose a course: 1. {course_one_title}: {course_one_terms}. Details: {course_one_card_url}. Buy: {course_one_purchase_url}. 2. {course_two_title}: {course_two_terms}. Details: {course_two_card_url}. Buy: {course_two_purchase_url}. 3. {course_three_title}: {course_three_terms}. Details: {course_three_card_url}. Buy: {course_three_purchase_url}. If you have any questions, I'm here to help 💛
refusal: {refusal_text}
handoff: {handoff_text}
help: If you have any questions, I'm here to help 💛
placement: DM {keyword}.
On the actual DM keyword show all three distinct offers and all six destinations in plain text. Preserve each card/details URL separately from its purchase URL, even when the owner intentionally uses the same destination. Include the following help invitation in the same reply: If you have any questions, I'm here to help 💛. After a new question answer only from the selected offer terms; unknown facts use {handoff_text}. No gallery, button callback, separate autonomous second message, purchase or access verification. On refusal send {refusal_text} and stop. HELP is an actual reply, not a button callback. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
  - If Selected entry received -> first
- first: Send the requested response.
  - If Actual bare HELP reply -> help
  - If Actual concrete question -> answer
- help: Only for bare HELP, ask what assistance is needed.
  - If Actual question or problem details in a new reply -> answer
- answer: Answer a concrete question only from approved facts; otherwise state that human review is needed. Do not repeat the help invitation or claim an unconfigured transfer.
#### Exact Setting Drafts
Not tool calls. Add resolved botID/automationID and privacy-safe context only after all gates; one setting per call.
```json
[
  {
    "tool": "update_automation_setting",
    "target": "dm_base",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Choose a course: 1. {course_one_title}: {course_one_terms}. Details: {course_one_card_url}. Buy: {course_one_purchase_url}. 2. {course_two_title}: {course_two_terms}. Details: {course_two_card_url}. Buy: {course_two_purchase_url}. 3. {course_three_title}: {course_three_terms}. Details: {course_three_card_url}. Buy: {course_three_purchase_url}. If you have any questions, I'm here to help 💛\nOn the actual DM keyword show all three distinct offers and all six destinations in plain text. Preserve each card/details URL separately from its purchase URL, even when the owner intentionally uses the same destination. Include the following help invitation in the same reply: If you have any questions, I'm here to help 💛. After a new question answer only from the selected offer terms; unknown facts use {handoff_text}. No gallery, button callback, separate autonomous second message, purchase or access verification. On refusal send {refusal_text} and stop. HELP is an actual reply, not a button callback. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: {refusal_text} End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: {refusal_text}\nhandoff: {handoff_text}\nhelp: If you have any questions, I'm here to help 💛"
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "dm_base",
    "settings": {
      "switchToHuman": {
        "howToSwitch": "SwitchToTeammates",
        "rules": "$resolved.safe_handoff_rules"
      }
    }
  }
]
```
Candidate additions; never send as a replacement for an unread existing list:
```json
{
  "switchToHuman": {
    "switchingConditions": "Campaign {campaign}: the person requests the team or facts are unresolved.",
    "messagePrompt": "{handoff_text}"
  }
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-111: DM your course like a closer
Full captured settings/provenance: [selected source JSON](../source-records/manychat-111.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"new","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-1: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Let me show you my new drop! My courses are designed to help you get more dream clients from Instagram ☁️
```
Captured buttons: ["Buy Now🛍️"]
Captured gallery: [{"background_image":"url(\"https://manychat-storage.s3.eu-central-1.amazonaws.com/manychat/quickcampaign/ca/2025/11/26/818756a64161df38e0315cab60549421/big_ed56a3400119d3e7a59963207bb56d38\")","file_control":[{"multiple":true}],"position":0,"rendered_height":"280px","subtitle":"The #1 easy marketing guide","title":"Marketing Master Plan","image":"https://manychat-storage.s3.eu-central-1.amazonaws.com/manychat/quickcampaign/ca/2025/11/26/818756a64161df38e0315cab60549421/big_ed56a3400119d3e7a59963207bb56d38"},{"background_image":"url(\"https://manychat-storage.s3.eu-central-1.amazonaws.com/manychat/quickcampaign/ca/2025/11/26/c1db65893942fb23b518a61cf18ffd6b/big_1661f57af6dcd96e3c013fd58d158b94\")","file_control":[{"multiple":true}],"position":1,"rendered_height":"280px","subtitle":"The bumper target market guide","title":"Ideal Client Roadmap","image":"https://manychat-storage.s3.eu-central-1.amazonaws.com/manychat/quickcampaign/ca/2025/11/26/c1db65893942fb23b518a61cf18ffd6b/big_1661f57af6dcd96e3c013fd58d158b94"},{"background_image":"url(\"https://manychat-storage.s3.eu-central-1.amazonaws.com/manychat/quickcampaign/ca/2025/11/26/d3bead947a019cb41492cf5eca931de9/big_c182299b4ba66f0aa0fd54c47df1a590\")","file_control":[{"multiple":true}],"position":2,"rendered_height":"280px","subtitle":"The only lead magnet workbook you need!","title":"Create a Freebie Your Followers Love!","image":"https://manychat-storage.s3.eu-central-1.amazonaws.com/manychat/quickcampaign/ca/2025/11/26/d3bead947a019cb41492cf5eca931de9/big_c182299b4ba66f0aa0fd54c47df1a590"}]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Let me show you my new drop! My courses are designed to help you get more dream clients from Instagram ☁️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"file","value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"disabled":true,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"title","label":null,"type":null,"value":"Marketing Master Plan","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"subtitle","label":null,"type":null,"value":"The #1 easy marketing guide","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"title","label":null,"type":null,"value":"Ideal Client Roadmap","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"subtitle","label":null,"type":null,"value":"The bumper target market guide","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"title","label":null,"type":null,"value":"Create a Freebie Your Followers Love!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"subtitle","label":null,"type":null,"value":"The only lead magnet workbook you need!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"","value":""}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Buy Now🛍️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebsite.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: "Next Step"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
If you have any questions, I'm here to help 💛
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"If you have any questions, I'm here to help 💛","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-111 / Finish the offer destination
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-111 - DM your course like a closer.
Goal: Present the right course and help interested learners reach the offer.
Variant: Sell courses: three cards and help
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Keyword direct message
Source requirements: Three-course gallery; Separate card and purchase URLs; A following help message
Source timing: No exact timer captured.
Source outcome: A choice of three courses
Captured text (node-0, not approved campaign copy):
Let me show you my new drop! My courses are designed to help you get more dream clients from Instagram ☁️
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Offer three named courses with all six detail/purchase URLs and a help branch.
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
Structured audit: [setup record](courses-manychat-111.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
