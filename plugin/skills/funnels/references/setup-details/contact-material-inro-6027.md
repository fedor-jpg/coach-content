# Grow your phone list: required phone before the freebie

Setup 1.1.0 | contact-material-inro-6027 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Use a useful resource to start a direct relationship with interested people.
Creators and businesses building an owned audience; choose required or optional contact capture.
Source entry: Freebie comment
Source outcome: A resource after phone capture
Source requirements: Press the opening button; Provide a valid phone number before delivery; Repeat the request
Source timing: Link click: 3 hours; phone and opening button: 3 days.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Ask for phone before sending the guide; refuse delivery if the phone is missing or obviously malformed.
Retained/replaced: Ask for phone before sending the guide; refuse delivery if the phone is missing or obviously malformed.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Link click: 3 hours; phone and opening button: 3 days.. No timed unsolicited message is configured.
Not retained: No click tracking, click-dependent branch or no-click reminder.
Not retained: No imported deterministic graph or source folder/tag tracking.
Limitation: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.
Limitation: Every requested contact is required before delivery: phone. Refusal does not release the gated link.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Ask for phone before sending the guide; refuse delivery if the phone is missing or obviously malformed.
Target: owned_comment
Ask only for missing business facts:
- resource_title: Supply the business value and approve its use in this selected draft. (required)
- resource_url: Supply the business value and approve its use in this selected draft. (required)
- contact_purpose: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
- Normal MCP has no contact-attribute-value reader. Capture configuration readback and chat text do not prove saved email/phone, joined membership or withdrawal. Keep value-dependent confirmation or handoff unresolved; simple preparation remains available.
#### Copy and Conversation Instructions
initial: Want {resource_title}? Reply YES to continue.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Here is {resource_title}: {resource_url}
invalid: That looks incomplete or incorrectly formatted. Please try again.
phone: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact.
Every requested contact is required before delivery: phone. Refusal does not release the gated link. Explain {contact_purpose} before collection; use only new answers after this purpose is clear. Ask: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact. Check email conversationally for a nonempty name, @ and a plausible domain; check phone for country code and plausible digits. Reject missing or obviously malformed answers and ask correction without showing the resource URL. These are AI conversational checks, NOT deterministic validation. Do not release the link on SKIP, refusal, partial answers or malformed contact. Require all phone answers before delivery. Deliver: Here is {resource_title}: {resource_url} Preserve refusal and silence. HELP asks for the problem; do not bypass any pending contact gate. Configure separate capture additions for phone with the explicit purpose; merge them into the complete existing captures list, never overwrite it. Contact persistence is unverified: do not claim saved data or external subscription. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: Every requested contact is required before delivery: phone. Refusal does not release the gated link.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Selected entry received -> first
- first: Wait for actual confirmation.
  - If Actual affirmative reply -> phone
  - If Actual refusal -> refusal
  - If No actual reply -> silence
- phone: Request phone; wait for an actual answer.
  - If New consented phone passes AI conversational check -> delivery
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
        "exactTextReply": "Want {resource_title}? Reply YES to continue."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {resource_title}? Reply YES to continue.\nEvery requested contact is required before delivery: phone. Refusal does not release the gated link. Explain {contact_purpose} before collection; use only new answers after this purpose is clear. Ask: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact. Check email conversationally for a nonempty name, @ and a plausible domain; check phone for country code and plausible digits. Reject missing or obviously malformed answers and ask correction without showing the resource URL. These are AI conversational checks, NOT deterministic validation. Do not release the link on SKIP, refusal, partial answers or malformed contact. Require all phone answers before delivery. Deliver: Here is {resource_title}: {resource_url} Preserve refusal and silence. HELP asks for the problem; do not bypass any pending contact gate. Configure separate capture additions for phone with the explicit purpose; merge them into the complete existing captures list, never overwrite it. Contact persistence is unverified: do not claim saved data or external subscription. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {resource_title}: {resource_url}\ninvalid: That looks incomplete or incorrectly formatted. Please try again.\nphone: For {contact_purpose}, please send your phone number with country code. You can refuse; the link requires this contact. The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
      "attribute": "$resolved.verified_phone_attribute",
      "description": "Campaign {campaign}; phone for {contact_purpose}: Every requested contact is required before delivery: phone. Refusal does not release the gated link."
    }
  ]
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6027: Grow Your Phone List
Full captured settings/provenance: [selected source JSON](../source-records/inro-6027.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
All posts
FILTER THE COMMENTS
Comments with keyword(s)
Freebie
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (comment)
A fixed public reply is a documented primitive, not proof of captured random text choice or downstream routing.
Business input: approved public reply
Setting candidate: update_automation_setting: publicReply
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text
Thanks for your comment 💛
Check your DMs 🔥
```
- Field (captured): {"label":null,"type":"text","value":"Thanks for your comment 💛","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Check your DMs 🔥","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"checkbox","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":"","required":null}}
- Field (captured): {"label":null,"type":"checkbox","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":"","required":null}}
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Freebie lead
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e002: n002 -> n003 | condition/label: ""
#### n003 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Hey {{contact.name}}! Do you want our guide?
Yes ✨
```
Captured buttons: ["Yes ✨"]
- Field (captured): {"label":null,"type":"textarea","value":"Hey {{contact.name}}! Do you want our guide?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Yes ✨","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"url","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e003: n003 -> n004 | condition/label: ""
- Edge e012: n003 -> n013 | condition/label: ""
#### n004 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Yes ✨
```
- Edge e004: n004 -> n005 | condition/label: "WHEN BUTTON IS CLICKED\nYes ✨"
#### n005 (collect_property)
Contact storage is documented. Exact validation gates, retries and external subscriptions are separate dependencies.
Business input: purpose, required versus optional contact, channel consent
Setting candidate: update_automation_setting: collectContactInfo
Disposition: requires_change_or_external_dependency; dependencies: contact, graph
Captured text (not approved outbound copy):
```text
Ask for information
Collect email, phone or any contact property and save it automatically.
Please send your phone number to receive it.
Message without the information
We couldn't detect a valid number. Please try again.
Phone
```
- Field (captured): {"label":null,"type":"textarea","value":"Please send your phone number to receive it.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"button","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect a valid number. Please try again.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":"0","minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"continue"}
- Field (captured): {"value":"expire"}
- Field (captured): {"label":null,"type":"button","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Field (captured): {"label":null,"type":"textarea","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e005: n005 -> n006 | condition/label: ""
- Edge e011: n005 -> n012 | condition/label: ""
#### n006 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN INFORMATION IS COLLECTED
```
- Edge e006: n006 -> n007 | condition/label: "WHEN INFORMATION IS COLLECTED"
#### n007 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Phone collected
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e007: n007 -> n008 | condition/label: ""
#### n008 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Here's your guide 🔥
Get it now
```
- Edge e008: n008 -> n009 | condition/label: ""
- Edge e009: n008 -> n010 | condition/label: ""
#### n009 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- No captured outgoing edge; do not infer completion.
#### n010 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 hours
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e010: n010 -> n011 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 hours"
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you received the link?
```
- Field (captured): {"label":null,"type":"text","value":"Have you received the link?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- No captured outgoing edge; do not infer completion.
#### n012 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF INFORMATION HAS NOT BEEN RECEIVED AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n013 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e013: n013 -> n014 | condition/label: "IF BUTTON HAS NOT BEEN CLICKED AFTER\n3 days"
#### n014 (collect_property)
Contact storage is documented. Exact validation gates, retries and external subscriptions are separate dependencies.
Business input: purpose, required versus optional contact, channel consent
Setting candidate: update_automation_setting: collectContactInfo
Disposition: requires_change_or_external_dependency; dependencies: contact, graph
Captured text (not approved outbound copy):
```text
Ask for information
Collect email, phone or any contact property and save it automatically.
Hey there! Still want your guide? Leave your phone below 👇🏻
Message without the information
We couldn't detect a valid date. Please try again.
Phone
```
- Field (captured): {"label":null,"type":"textarea","value":"Hey there! Still want your guide? Leave your phone below 👇🏻","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"button","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"We couldn't detect a valid date. Please try again.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":"0","minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"continue"}
- Field (captured): {"value":"expire"}
- Field (captured): {"label":null,"type":"button","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"expire","value_state":"observed_value","options":[{"selected":false,"text":"Go to next automation step","value":"continue"},{"selected":true,"text":"Mark step as expired","value":"expire"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Field (captured): {"label":null,"type":"textarea","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e014: n014 -> n015 | condition/label: ""
- Edge e020: n014 -> n021 | condition/label: ""
#### n015 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN INFORMATION IS COLLECTED
```
- Edge e015: n015 -> n016 | condition/label: "WHEN INFORMATION IS COLLECTED"
#### n016 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Phone collected
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e016: n016 -> n017 | condition/label: ""
#### n017 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Here's your guide 🔥
Get it now
```
- Edge e017: n017 -> n018 | condition/label: ""
- Edge e018: n017 -> n019 | condition/label: ""
#### n018 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- No captured outgoing edge; do not infer completion.
#### n019 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 hours
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e019: n019 -> n020 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 hours"
#### n020 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you received the link?
```
- Field (captured): {"label":null,"type":"text","value":"Have you received the link?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- No captured outgoing edge; do not infer completion.
#### n021 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF INFORMATION HAS NOT BEEN RECEIVED AFTER
3 days
```
- Field (captured): {"label":null,"type":"number","value":"3","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"days","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":true,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](contact-material-inro-6027.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
