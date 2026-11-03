# Grow your email list: ebook and 23-hour retry

Setup 1.1.0 | contact-material-manychat-20 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Use a useful resource to start a direct relationship with interested people.
Creators and businesses building an owned audience; choose required or optional contact capture.
Source entry: Keyword in a direct message
Source outcome: An ebook after email capture
Source requirements: Email is required; Repeat email collection after no reply
Source timing: No reply: 23 hours; the reminder contains a second email collection step.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Ask for email before delivering the ebook.
Retained/replaced: Ask for email before delivering the ebook.
Not retained: Exact source timing is not retained: No reply: 23 hours; the reminder contains a second email collection step.. No timed unsolicited message is configured.
Not retained: No imported deterministic graph or source folder/tag tracking.
Limitation: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.
Limitation: Every requested contact is required before delivery: email. Refusal does not release the gated link.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Ask for email before delivering the ebook.
Target: dm_base
Ask only for missing business facts:
- ebook_title: Supply the business value and approve its use in this selected draft. (required)
- ebook_url: Supply the business value and approve its use in this selected draft. (required)
- contact_purpose: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
- Normal MCP has no contact-attribute-value reader. Capture configuration readback and chat text do not prove saved email/phone, joined membership or withdrawal. Keep value-dependent confirmation or handoff unresolved; simple preparation remains available.
#### Copy and Conversation Instructions
initial: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact.
refusal: Understood. I will stop this request.
delivery: Here is {ebook_title}: {ebook_url}
invalid: That looks incomplete or incorrectly formatted. Please try again.
email: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact.
placement: DM {keyword}.
Every requested contact is required before delivery: email. Refusal does not release the gated link. Explain {contact_purpose} before collection; use only new answers after this purpose is clear. Ask: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact. Check email conversationally for a nonempty name, @ and a plausible domain; check phone for country code and plausible digits. Reject missing or obviously malformed answers and ask correction without showing the resource URL. These are AI conversational checks, NOT deterministic validation. Do not release the link on SKIP, refusal, partial answers or malformed contact. Require all email answers before delivery. Deliver: Here is {ebook_title}: {ebook_url} Preserve refusal and silence. HELP asks for the problem; do not bypass any pending contact gate. Configure separate capture additions for email with the explicit purpose; merge them into the complete existing captures list, never overwrite it. Contact persistence is unverified: do not claim saved data or external subscription. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: Every requested contact is required before delivery: email. Refusal does not release the gated link.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
  - If Selected entry received -> first
- first: Request the first contact for the stated purpose.
  - If New consented email passes AI conversational check -> delivery
  - If Missing or obviously malformed email -> invalid-email
  - If Actual refusal or STOP -> refusal
  - If No actual reply -> silence
- invalid-email: Ask for email correction without a resource URL.
  - If Actual new correction reply -> first
- delivery: Deliver only after the required contact answers, or explicit SKIP when optional.
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact.\nEvery requested contact is required before delivery: email. Refusal does not release the gated link. Explain {contact_purpose} before collection; use only new answers after this purpose is clear. Ask: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact. Check email conversationally for a nonempty name, @ and a plausible domain; check phone for country code and plausible digits. Reject missing or obviously malformed answers and ask correction without showing the resource URL. These are AI conversational checks, NOT deterministic validation. Do not release the link on SKIP, refusal, partial answers or malformed contact. Require all email answers before delivery. Deliver: Here is {ebook_title}: {ebook_url} Preserve refusal and silence. HELP asks for the problem; do not bypass any pending contact gate. Configure separate capture additions for email with the explicit purpose; merge them into the complete existing captures list, never overwrite it. Contact persistence is unverified: do not claim saved data or external subscription. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {ebook_title}: {ebook_url}\ninvalid: That looks incomplete or incorrectly formatted. Please try again.\nemail: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact."
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
      "attribute": "$resolved.verified_email_attribute",
      "description": "Campaign {campaign}; email for {contact_purpose}: Every requested contact is required before delivery: email. Refusal does not release the gated link."
    }
  ]
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-20: Grow your email list
Full captured settings/provenance: [selected source JSON](../source-records/manychat-20.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"ebook","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-0: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hi! Thanks for reaching out 💌

We are excited you are interested in our content and the ebook, and we would LOVE to send you more!

To get a free ebook, please leave us your email below 👇
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hi! Thanks for reaching out 💌\n\nWe are excited you are interested in our content and the ebook, and we would LOVE to send you more!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"To get a free ebook, please leave us your email below 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"saveEmailToSystemField","label":"Save Email to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"setEmailOptIn","label":"Set Email Opt-In ","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Please enter a correct email address, e.g. me@mail.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"value":"23"}
- Field (captured_default): {"value":"hours","options":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}]}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Field (inspection_variant): {"name":"saveEmailToSystemField","label":"Save Email to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"customFieldId","label":"Add Response to a Custom Field","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Please enter a correct email address, e.g. me@mail.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"saveEmailToSystemField","label":"Save Email to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"setEmailOptIn","label":"Set Email Opt-In ","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Please enter a correct email address, e.g. me@mail.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-1: node-0 -> node-1 | condition/label: "successful input/Next Step"
- Edge edge-2: node-0 -> node-2 | condition/label: "no response expiration"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Awesome!

You are all set.

Click the link to grab your ebook 👇🚀
```
Captured buttons: ["Grab the book! 💌"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Awesome!\n\nYou are all set.\n\nClick the link to grab your ebook 👇🚀","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Grab the book! 💌","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"https://www.youtube.com/watch?v=hNIAaQ8dZC0&ab_channel=Manychat","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hi! Are you still here? 💙

If you are still interested in getting a free ebook, please leave us your email below 👇
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hi! Are you still here? 💙","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"If you are still interested in getting a free ebook, please leave us your email below 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"saveEmailToSystemField","label":"Save Email to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"setEmailOptIn","label":"Set Email Opt-In ","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Please enter a correct email address, e.g. me@mail.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"value":"23"}
- Field (captured_default): {"value":"hours","options":[{"selected":false,"text":"Seconds","value":"seconds"},{"selected":false,"text":"Minutes","value":"minutes"},{"selected":true,"text":"Hours","value":"hours"},{"selected":false,"text":"Days","value":"days"}]}
- Field (captured_default): {"value":"seconds"}
- Field (captured_default): {"value":"minutes"}
- Field (captured_default): {"value":"hours"}
- Field (captured_default): {"value":"days"}
- Edge edge-3: node-2 -> node-1 | condition/label: "successful input/Next Step"
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-20 / Finish email-list signup
For the email-list goal. Contact capture is not external subscription.
```text
Help me prepare: Finish email-list signup.
Selected source: manychat-20 - Grow your email list.
Goal: Use a useful resource to start a direct relationship with interested people.
Variant: Grow your email list: ebook and 23-hour retry
Scope: For the email-list goal. Contact capture is not external subscription.
Source entry: Keyword in a direct message
Source requirements: Email is required; Repeat email collection after no reply
Source timing: No reply: 23 hours; the reminder contains a second email collection step.
Source outcome: An ebook after email capture
Captured text (node-0, not approved campaign copy):
Hi! Thanks for reaching out 💌

We are excited you are interested in our content and the ebook, and we would LOVE to send you more!

To get a free ebook, please leave us your email below 👇
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Ask for email before delivering the ebook.
Use the existing email provider. If none exists, propose Brevo for approval; it is not connected.
Ask me for: Provider and target list; Email consent wording and proof; Resource URL; welcome email only if separately requested; Existing authorized access or connection.
1. Inspect existing authorized connections. Chatfuel contact collection alone does not subscribe anyone to an external list. Use a sync only after verifying its field mapping, authorization and readback.
2. If no sync is verified, propose a hosted signup form link in the DM. A Brevo form can collect EMAIL and add the contact to the selected list. Disclose the extra form step and ask for approval before changing the source journey. If DM collection must remain, leave the ongoing bridge unverified and prepare the exact mapping and next access action only.
3. Draft the email-to-list mapping and channel-specific consent record. Preserve opt-outs; prevent duplicate contacts and repeated welcome sends. Keep optional signup optional and do not withhold a resource that the selected Chatfuel variant delivers first.
4. Verify actual membership in the intended list; this can complete the list-growth goal. A saved Chatfuel email or a link click does not prove membership. Only if the owner requests a welcome email or series, draft sender, reply-to and unsubscribe settings and a separate consented delivery check before any later approved send. Return draft form/list settings, unresolved access and the next authorized action.
5. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
6. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
7. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
Official guidance checked 2026-11-02:
Brevo signup forms: https://help.brevo.com/hc/en-us/articles/208771869-Create-a-sign-up-form-in-Brevo
Authorized contact and list mapping: https://developers.brevo.com/docs/synchronise-contact-lists
Consent records: https://help.brevo.com/hc/en-us/articles/213405965-Build-a-legitimate-contacts-database-for-optimal-deliverability-and-compliance
Email and SMS automation actions: https://help.brevo.com/hc/en-us/articles/15445989568402-Available-triggers-actions-and-rules-in-an-automation
Optional email sender and message settings: https://help.brevo.com/hc/en-us/articles/24257124386066-Send-an-email-from-an-automation
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](contact-material-manychat-20.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
