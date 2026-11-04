# Turn comments into RSVPs: email and phone required

Setup 1.1.0 | webinar-manychat-81 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Turn Instagram interest into event sign-ups and access.
Hosts promoting a webinar, workshop or event.
Source entry: Keyword comment
Source outcome: A webinar link after both contacts
Source requirements: Press the opening button; Email is required; Phone is required after email
Source timing: Two unset no-response exits: 23 hours each.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.
Retained/replaced: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Two unset no-response exits: 23 hours each.. No timed unsolicited message is configured.
Not retained: No imported deterministic graph or source folder/tag tracking.
Limitation: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.
Limitation: Every requested contact is required before delivery: email and phone. Refusal does not release the gated link.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.
Target: owned_comment
Ask only for missing business facts:
- webinar_title: Supply the business value and approve its use in this selected draft. (required)
- webinar_url: Supply the business value and approve its use in this selected draft. (required)
- contact_purpose: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
- Normal MCP has no contact-attribute-value reader. Capture configuration readback and chat text do not prove saved email/phone, joined membership or withdrawal. Keep value-dependent confirmation or handoff unresolved; simple preparation remains available.
#### Copy and Conversation Instructions
initial: Want {webinar_title}? Reply YES to continue.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Here is {webinar_title}: {webinar_url}
invalid: That looks incomplete or incorrectly formatted. Please try again.
email: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact.
phone: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact.
Every requested contact is required before delivery: email and phone. Refusal does not release the gated link. Explain {contact_purpose} before collection; use only new answers after this purpose is clear. Ask: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact. Then, after a valid answer, Ask: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact. Check email conversationally for a nonempty name, @ and a plausible domain; check phone for country code and plausible digits. Reject missing or obviously malformed answers and ask correction without showing the resource URL. These are AI conversational checks, NOT deterministic validation. Do not release the link on SKIP, refusal, partial answers or malformed contact. Require all email and phone answers before delivery. Deliver: Here is {webinar_title}: {webinar_url} Preserve refusal and silence. HELP asks for the problem; do not bypass any pending contact gate. Configure separate capture additions for email and phone with the explicit purpose; merge them into the complete existing captures list, never overwrite it. Contact persistence is unverified: do not claim saved data or external subscription. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: Every requested contact is required before delivery: email and phone. Refusal does not release the gated link.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Selected entry received -> first
- first: Wait for actual confirmation.
  - If Actual affirmative reply -> email
  - If Actual refusal -> refusal
  - If No actual reply -> silence
- email: Request email; wait for an actual answer.
  - If New consented email passes AI conversational check -> phone
  - If Missing or obviously malformed email -> invalid-email
  - If Actual refusal or STOP -> refusal
  - If No actual reply -> silence
- invalid-email: Ask for email correction without a resource URL.
  - If Actual new correction reply -> email
- phone: Request phone; wait for an actual answer.
  - If New consented phone passes AI conversational check and prior required contact remains present in this run -> delivery
  - If Missing or obviously malformed phone -> invalid-phone
  - If Actual refusal or STOP -> refusal
  - If No actual reply -> silence
- invalid-phone: Ask for phone correction without a resource URL.
  - If Actual new correction reply -> phone
- delivery: Deliver only after the required contact answers, or explicit SKIP when optional.
- refusal: End this request without delivering gated content.
- silence: No message after silence.
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
        "exactTextReply": "Want {webinar_title}? Reply YES to continue."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {webinar_title}? Reply YES to continue.\nEvery requested contact is required before delivery: email and phone. Refusal does not release the gated link. Explain {contact_purpose} before collection; use only new answers after this purpose is clear. Ask: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact. Then, after a valid answer, Ask: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact. Check email conversationally for a nonempty name, @ and a plausible domain; check phone for country code and plausible digits. Reject missing or obviously malformed answers and ask correction without showing the resource URL. These are AI conversational checks, NOT deterministic validation. Do not release the link on SKIP, refusal, partial answers or malformed contact. Require all email and phone answers before delivery. Deliver: Here is {webinar_title}: {webinar_url} Preserve refusal and silence. HELP asks for the problem; do not bypass any pending contact gate. Configure separate capture additions for email and phone with the explicit purpose; merge them into the complete existing captures list, never overwrite it. Contact persistence is unverified: do not claim saved data or external subscription. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {webinar_title}: {webinar_url}\ninvalid: That looks incomplete or incorrectly formatted. Please try again.\nemail: For {contact_purpose}, please send your email address. You can refuse; the link requires this contact.\nphone: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact. The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
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
      "description": "Campaign {campaign}; email for {contact_purpose}: Every requested contact is required before delivery: email and phone. Refusal does not release the gated link."
    },
    {
      "attribute": "$resolved.verified_phone_attribute",
      "description": "Campaign {campaign}; phone for {contact_purpose}: Every requested contact is required before delivery: email and phone. Refusal does not release the gated link."
    }
  ]
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-81: Turn comments into RSVPs
Full captured settings/provenance: [selected source JSON](../source-records/manychat-81.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"replies.0.reply","label":null,"type":null,"value":"Sent the secret link to your DMs 🔐","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.1.reply","label":null,"type":null,"value":"Details sent, see your inbox 📬","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.2.reply","label":null,"type":null,"value":"Done! Check your inbox for info 📫","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-3: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Hey! I'm so happy you'd like to join my free webinar "How to make real money from social media". 💅

Tap below to get access! 
```
Captured buttons: ["Sign Me Up! 🔥"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hey! I'm so happy you'd like to join my free webinar \"How to make real money from social media\". 💅\n\nTap below to get access! ","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Sign Me Up! 🔥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-0: node-0 -> node-1 | condition/label: "Sign Me Up! 🔥"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Oh yeah! To reserve your spot, please gimme your email below 👇

Thanks! I've got it. 😉 I promise to only send you the good stuff (no spam, ever!) Just one more thing...
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Oh yeah! To reserve your spot, please gimme your email below 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Thanks! I've got it. 😉 I promise to only send you the good stuff (no spam, ever!) Just one more thing...","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
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
- Edge edge-1: node-1 -> node-2 | condition/label: "Next Step"
#### node-2 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
I'd love your phone number! Gimme it below so you're in the loop for all of my masterclasses 👇

You're the best. Thank you! ❤️
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"I'd love your phone number! Gimme it below so you're in the loop for all of my masterclasses 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"You're the best. Thank you! ❤️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
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
- Field (inspection_variant): {"name":"savePhoneToWhatsAppIdSystemField","label":"Save Phone as WhatsApp ID","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"savePhoneToSystemField","label":"Save Phone to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"customFieldId","label":"Add Response to a Custom Field","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Your phone number must contain the country and city code and be in the following format: +15417543010","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (inspection_variant): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"savePhoneToWhatsAppIdSystemField","label":"Save Phone as WhatsApp ID","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"savePhoneToSystemField","label":"Save Phone to System Field","type":"checkbox","value":"<redacted>","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"setSmsOptIn","label":"Set SMS Opt-In ","type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"validationErrorMessage","label":"No retry message","type":null,"value":"Your phone number must contain the country and city code and be in the following format: +15417543010","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (restoration_check): {"name":"skipButtonCaption","label":"\"Skip\" button text","type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Edge edge-2: node-2 -> node-3 | condition/label: "Next Step"
#### node-3 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
You're IN! 

Grab your pen and paper (and your fave energy drink!) and settle in to watch my "How to make real money from social media" webinar now! 👇
```
Captured buttons: ["Watch Webinar 📺"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"You're IN! \n\nGrab your pen and paper (and your fave energy drink!) and settle in to watch my \"How to make real money from social media\" webinar now! 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Watch Webinar 📺","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourwebinarpage.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: manychat-81 / Finish event registration
Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
```text
Help me prepare: Finish event registration.
Selected source: manychat-81 - Turn comments into RSVPs.
Goal: Turn Instagram interest into event sign-ups and access.
Variant: Turn comments into RSVPs: email and phone required
Scope: Use to finish registration in the existing event service. Do not add a marketing subscription unless separately requested.
Source entry: Keyword comment
Source requirements: Press the opening button; Email is required; Phone is required after email
Source timing: Two unset no-response exits: 23 hours each.
Source outcome: A webinar link after both contacts
Captured text (node-0, not approved campaign copy):
Hey! I'm so happy you'd like to join my free webinar "How to make real money from social media". 💅

Tap below to get access! 
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Ask for email and then phone; deliver the webinar URL only after both answers pass conversational checks.
Use the existing form or webinar service and the selected event.
Ask me for: Event service, form and URL; Event date and time zone; Required registration fields and consent; Existing authorized access.
1. Confirm the event and authorized access. Draft the registration form and map only its required fields. Event registration consent does not imply email or SMS marketing consent.
2. Retain required versus optional email/phone distinctions. If the Chatfuel variant delivers the link before optional email, disclose that change; do not claim the original contact gate remains.
3. Define success as a registration record in the event service, separately from delivery or clicks. If reminders depend on external completion or exact timing, identify a verified existing connection and its semantics or leave that dependency unresolved. Return draft settings and next access steps; do not register attendees or send reminders.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](webinar-manychat-81.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
