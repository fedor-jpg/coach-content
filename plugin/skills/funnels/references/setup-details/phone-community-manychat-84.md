# Grow an SMS list: phone and 23-hour reminder

Setup 1.1.0 | phone-community-manychat-84 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Give your Instagram audience a direct line to your business through an opt-in SMS list.
Creators and businesses building a private VIP audience beyond Instagram.
Source entry: Direct message matching a VIP keyword
Source outcome: A stored phone number toward an opt-in SMS audience
Source requirements: Collect the phone number; Remind after silence without a second collection block
Source timing: No reply: 23 hours; the reminder does not contain another collection block.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Request a consented phone number; keep SMS-provider signup and sending as separate unimplemented continuation.
Retained/replaced: Request a consented phone number; keep SMS-provider signup and sending as separate unimplemented continuation.
Not retained: Exact source timing is not retained: No reply: 23 hours; the reminder does not contain another collection block.. No timed unsolicited message is configured.
Not retained: No external SMS subscription, SMS send or delivery confirmation.
Limitation: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.
Limitation: Phone and SMS-specific consent are required for the requested signup; actual provider membership and delivery remain unimplemented.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- external: No external survey, webinar, Calendly, payment, mailing/SMS subscription or cross-channel completion event. Native booking status applies only to native bookings.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Request a consented phone number; keep SMS-provider signup and sending as separate unimplemented continuation.
Target: dm_base
Ask only for missing business facts:
- sms_purpose: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
- Normal MCP has no contact-attribute-value reader. Capture configuration readback and chat text do not prove saved email/phone, joined membership or withdrawal. Keep value-dependent confirmation or handoff unresolved; simple preparation remains available.
#### Copy and Conversation Instructions
initial: Would you like to share your phone for {sms_purpose}? Please include the country code. You can say NO.
refusal: Understood. I will stop this request.
received: Thanks, I received your reply.
placement: DM {keyword}.
Explain {sms_purpose} and obtain channel-specific consent. Request a new phone with country code, reject missing or obviously malformed answers conversationally, then draft capture only. This is not deterministic validation or persistence proof. Never say added, subscribed or I will text you. External provider list membership and any later approved send remain separate continuation; no reminder after silence. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: Phone and SMS-specific consent are required for the requested signup; actual provider membership and delivery remain unimplemented.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
  - If Actual VIP keyword DM -> first
- first: Explain purpose and request consented phone.
  - If New consented phone passes AI conversational check -> received
  - If Actual missing or malformed answer: request correction -> first
  - If Actual refusal -> refusal
  - If No actual reply -> silence
- received: Acknowledge the reply, not saved membership.
- refusal: End this request without delivering gated content.
- silence: No message after silence.
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Would you like to share your phone for {sms_purpose}? Please include the country code. You can say NO.\nExplain {sms_purpose} and obtain channel-specific consent. Request a new phone with country code, reject missing or obviously malformed answers conversationally, then draft capture only. This is not deterministic validation or persistence proof. Never say added, subscribed or I will text you. External provider list membership and any later approved send remain separate continuation; no reminder after silence. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\nreceived: Thanks, I received your reply."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "dm_base",
    "settings": {
      "collectContactInfo": {
        "howToCollect": "CollectInfo",
        "captures": "$resolved.safe_captures"
      }
    }
  }
]
```
Candidate additions; never send as a replacement for an unread existing list:
```json
{
  "collectContactInfo": [
    {
      "attribute": "$resolved.verified_phone_attribute",
      "description": "Campaign {campaign}; phone for {sms_purpose}: Phone and SMS-specific consent are required for the requested signup; actual provider membership and delivery remain unimplemented."
    }
  ]
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-84: Grow an SMS list
Full captured settings/provenance: [selected source JSON](../source-records/manychat-84.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"VIP","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"VIP list","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-1: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
OMG! I'm so excited you'd like to join my VIP-only hotline (aka my Text Besties community)! 🤭

I drop the best content, tools, tricks and more via text, so gimme your phone number so I can add you 👇

Yes! Got it. You’re added to my Text Besties community! 😉
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"OMG! I'm so excited you'd like to join my VIP-only hotline (aka my Text Besties community)! 🤭\n\nI drop the best content, tools, tricks and more via text, so gimme your phone number so I can add you 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Yes! Got it. You’re added to my Text Besties community! 😉","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"savePhoneToWhatsAppIdSystemField","label":"Save Phone as WhatsApp ID","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"savePhoneToSystemField","label":"Save Phone to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"setSmsOptIn","label":"Set SMS Opt-In ","type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Your phone number must contain the country and city code and be in the following format: +15417543010","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"value":"23"}
- Field (captured_default): {"value":"hours","options":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}]}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Edge edge-0: node-0 -> node-1 | condition/label: "Next Step"
- Edge edge-2: node-0 -> node-2 | condition/label: "no response expiration"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Stay tuned! I'll text you soon. Make sure you save the number so you don't miss a thing from me! ❤️
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Stay tuned! I'll text you soon. Make sure you save the number so you don't miss a thing from me! ❤️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Whoops! Looks like you got busy and forgot to leave your number. Got a moment to give it to me? 😉
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Whoops! Looks like you got busy and forgot to leave your number. Got a moment to give it to me? 😉","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-84 / Finish SMS-list signup
For the SMS-list goal. Captured phone collection does not send SMS.
```text
Help me prepare: Finish SMS-list signup.
Selected source: manychat-84 - Grow an SMS list.
Goal: Give your Instagram audience a direct line to your business through an opt-in SMS list.
Variant: Grow an SMS list: phone and 23-hour reminder
Scope: For the SMS-list goal. Captured phone collection does not send SMS.
Source entry: Direct message matching a VIP keyword
Source requirements: Collect the phone number; Remind after silence without a second collection block
Source timing: No reply: 23 hours; the reminder does not contain another collection block.
Source outcome: A stored phone number toward an opt-in SMS audience
Captured text (node-0, not approved campaign copy):
OMG! I'm so excited you'd like to join my VIP-only hotline (aka my Text Besties community)! 🤭

I drop the best content, tools, tricks and more via text, so gimme your phone number so I can add you 👇

Yes! Got it. You’re added to my Text Besties community! 😉
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Request a consented phone number; keep SMS-provider signup and sending as separate unimplemented continuation.
Use the existing SMS provider. If none exists, propose Brevo for approval; it is not connected.
Ask me for: Provider and target list; SMS-specific consent and opt-out wording; Phone country and country code; Only for a later owner-requested send: sender approval, credits and SMS text; Existing authorized access or connection.
1. Inspect existing authorized connections. A phone saved in Chatfuel is not an SMS subscription. Use an existing sync only after verifying authorization, field mapping and readback.
2. If no sync is verified, propose a native hosted SMS signup form linked from the DM. Brevo forms can collect SMS and add the contact to a selected list. Disclose the extra form step and obtain approval. If DM phone collection must remain, leave the bridge unverified and prepare the exact mapping and next access action only.
3. Normalize the phone country code and retain SMS-specific consent proof and opt-outs. Prevent duplicate list entries. Only if the owner separately requests SMS delivery, draft a list-added automation with plain-text SMS and reentry protection, then check sender approval and credits, including US/Canada toll-free prerequisites. Do not register a sender or spend credits.
4. Verify list membership; this can complete the SMS-list goal. SMS delivery is a separate optional later check, never an assumed source action. The captured 23-hour DM reminder is not an SMS action or a verified timer in ordinary MCP. Return draft form/list settings, unresolved access and the next authorized action.
5. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
6. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
7. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
Official guidance checked 2026-11-02:
Brevo signup forms: https://help.brevo.com/hc/en-us/articles/208771869-Create-a-sign-up-form-in-Brevo
SMS automation and reentry: https://help.brevo.com/hc/en-us/articles/4424283046418-Send-SMS-messages-through-an-automation
Sender and country prerequisites: https://help.brevo.com/hc/en-us/articles/28255350696466-Register-a-Sender-ID-to-send-SMS-messages
Consent records: https://help.brevo.com/hc/en-us/articles/213405965-Build-a-legitimate-contacts-database-for-optimal-deliverability-and-compliance
Authorized contact and list mapping: https://developers.brevo.com/docs/synchronise-contact-lists
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](phone-community-manychat-84.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
