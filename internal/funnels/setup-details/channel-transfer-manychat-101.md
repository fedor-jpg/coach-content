# Go to WhatsApp: captured button only adds a tag

Setup 1.1.0 | channel-transfer-manychat-101 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Help interested people continue the conversation on WhatsApp.
Businesses with an existing WhatsApp destination and clear ownership of replies.
Source entry: Keyword direct message
Source outcome: A tag, not a confirmed channel transfer
Source requirements: Press the button; Add contactedbywhatsapp
Source timing: No exact timer captured.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Offer a verified business WhatsApp URL in an actual DM reply; do not claim a transfer or tag success.
Retained/replaced: Offer a verified business WhatsApp URL in an actual DM reply; do not claim a transfer or tag success.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: No imported deterministic graph or source folder/tag tracking.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
- Missing source behavior: No WhatsApp navigation action was captured; the button title conflicts with its action.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; continuation only from actual replies in this conversation.
Entry change: DM entry retained. Navigation is an authored addition; the captured button action only tags the contact.
Output: Offer a verified business WhatsApp URL in an actual DM reply; do not claim a transfer or tag success.
Target: dm_base
Ask only for missing business facts:
- whatsapp_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: We'd love to help you on WhatsApp. Open our verified business link: {whatsapp_url}
refusal: Understood. I will stop this request.
placement: DM {keyword}.
On the actual DM request, offer {whatsapp_url}. Before preparation approve a verified business wa.me URL or owner-approved WhatsApp destination. This navigation link is authored, not present in the captured button action. Do not apply contactedbywhatsapp, infer a click, claim successful transfer, or send a WhatsApp message.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; continuation only from actual replies in this conversation.
  - If Selected entry received -> first
- first: Send the requested response.
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; continuation only from actual replies in this conversation.. First message: We'd love to help you on WhatsApp. Open our verified business link: {whatsapp_url}\nOn the actual DM request, offer {whatsapp_url}. Before preparation approve a verified business wa.me URL or owner-approved WhatsApp destination. This navigation link is authored, not present in the captured button action. Do not apply contactedbywhatsapp, infer a click, claim successful transfer, or send a WhatsApp message.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request."
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-101: Go from Instagram to WhatsApp
Full captured settings/provenance: [selected source JSON](../source-records/manychat-101.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"whatsapp","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-1: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
We'd love to help you! We're available on WhatsApp. ❤️ 
 Tap the button below to start a conversation with us there 👇
```
Captured buttons: ["Connect on Whatsapp📱"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"We'd love to help you! We're available on WhatsApp. ❤️ \n Tap the button below to start a conversation with us there 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Connect on Whatsapp📱","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: "Connect on Whatsapp📱"
#### node-1 (actions)
Preserve every actual action. A tag alone is not a URL navigation, purchase or channel transfer.
Business input: required tag/field action
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":"Tag picker","type":null,"value":"contactedbywhatsapp","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-101 / Finish the WhatsApp destination
A proposed destination change, not a captured channel transfer.
```text
Help me prepare: Finish the WhatsApp destination.
Selected source: manychat-101 - Go from Instagram to WhatsApp.
Goal: Help interested people continue the conversation on WhatsApp.
Variant: Go to WhatsApp: captured button only adds a tag
Scope: A proposed destination change, not a captured channel transfer.
Source entry: Keyword direct message
Source requirements: Press the button; Add contactedbywhatsapp
Source timing: No exact timer captured.
Source outcome: A tag, not a confirmed channel transfer
Captured text (node-0, not approved campaign copy):
We'd love to help you! We're available on WhatsApp. ❤️ 
 Tap the button below to start a conversation with us there 👇
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Offer a verified business WhatsApp URL in an actual DM reply; do not claim a transfer or tag success.
Use the owner's existing WhatsApp contact or business account.
Ask me for: Approved WhatsApp number or contact link; Destination owner; Consent and approved opening text.
1. The captured source button only adds a contact tag; it has no verified WhatsApp URL action. Request the actual destination and authorization.
2. Prepare the contact link and opening text as an explicit proposed change. Obtain approval before replacing the tag-only source step. Distinguish opening WhatsApp from a sent message or conversation. Do not assume contacts or context transfer across channels. Return the draft link and success check; do not send a message.
3. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
4. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
5. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](channel-transfer-manychat-101.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
