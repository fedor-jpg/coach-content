# Book calls from comments: readiness question

Setup 1.1.0 | booking-inro-6025 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Understand what a person needs and help them take the next step toward a call.
Coaches, consultants and service businesses offering an appointment.
Source entry: APPLY comment
Source outcome: A consultation link or starter resource
Source requirements: Agree to a question; Ready now leads to booking; not yet leads to starter material
Source timing: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Retained/replaced: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.. No timed unsolicited message is configured.
Not retained: No click tracking, click-dependent branch or no-click reminder.
Not retained: No imported deterministic graph or source folder/tag tracking.
Not retained: No outbound escalation email or external booking-completion check.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- email-send: No arbitrary outbound email action; handoff does not reproduce source email notifications.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Target: owned_comment
Ask only for missing business facts:
- program_name: Supply the business value and approve its use in this selected draft. (required)
- known_facts: Supply the business value and approve its use in this selected draft. (required)
- booking_url: Supply the business value and approve its use in this selected draft. (required)
- starter_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text, handoff_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Want to talk about {program_name}? Reply YES for one quick question.
public: {public_text}
refusal: Understood. I will stop this request.
handoff: {handoff_text}
question: Are you looking to start soon? Reply YES SOON or NOT YET.
qualified: Book a call: {booking_url}
starter: Free starter guide: {starter_url}
help: What would you like to know about {program_name}?
Use {program_name} and {known_facts}. After actual confirmation ask: Are you looking to start soon? Reply YES SOON or NOT YET. Ready soon -> {booking_url}; not yet -> {starter_url}. These are mutually exclusive alternatives, never both links in sequence. No booking, payment or external completion confirmation. Unresolved questions or a team request use {handoff_text}; no outbound email. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Selected entry received -> first
- first: Wait for the actual reply.
  - If Actual affirmative reply -> question
- question: Ask the readiness question and wait.
  - If Actual YES SOON reply -> qualified
  - If Actual NOT YET reply -> starter
  - If Actual refusal or STOP -> refusal
  - If No actual reply -> silence
- qualified: Offer only the booking destination.
- starter: Offer only the starter resource.
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
        "exactTextReply": "Want to talk about {program_name}? Reply YES for one quick question."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want to talk about {program_name}? Reply YES for one quick question.\nUse {program_name} and {known_facts}. After actual confirmation ask: Are you looking to start soon? Reply YES SOON or NOT YET. Ready soon -> {booking_url}; not yet -> {starter_url}. These are mutually exclusive alternatives, never both links in sequence. No booking, payment or external completion confirmation. Unresolved questions or a team request use {handoff_text}; no outbound email. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\nhandoff: {handoff_text}\nquestion: Are you looking to start soon? Reply YES SOON or NOT YET.\nqualified: Book a call: {booking_url}\nstarter: Free starter guide: {starter_url}\nhelp: What would you like to know about {program_name}? The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
### inro-6025: Book more calls from your comments
Full captured settings/provenance: [selected source JSON](../source-records/inro-6025.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment, dm-ai
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
Next post only
FILTER THE COMMENTS
Comments with keyword(s)
APPLY
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (comment)
A fixed public reply is a documented primitive, not proof of captured random text choice or downstream routing.
Business input: approved public reply
Setting candidate: update_automation_setting: publicReply
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text
Sent, check your DMs
Just sent it to your DMs
It's in your DMs now 🙂
```
- Field (captured): {"label":null,"type":"text","value":"Sent, check your DMs","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Just sent it to your DMs","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"It's in your DMs now 🙂","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"checkbox","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":"","required":null}}
- Field (captured): {"label":null,"type":"checkbox","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":"","required":null}}
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Want to talk about the mentoring program? One quick question first.
Sure, ask me
```
Captured buttons: ["Sure, ask me"]
- Field (captured): {"label":null,"type":"textarea","value":"Want to talk about the mentoring program? One quick question first.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Sure, ask me","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"url","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e002: n002 -> n003 | condition/label: ""
- Edge e017: n002 -> n018 | condition/label: ""
#### n003 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Sure, ask me
```
- Edge e003: n003 -> n004 | condition/label: "WHEN BUTTON IS CLICKED\nSure, ask me"
#### n004 (ask_question)
AI can ask and wait for an actual answer. Exact graph branches are not guaranteed.
Business input: approved question and answer requirements
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, graph
Captured text (not approved outbound copy):
```text
Are you looking to start soon?
Yes, soon
Not yet
```
- Field (captured): {"label":null,"type":"textarea","value":"Are you looking to start soon?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Yes, soon","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Not yet","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"button","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"button","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"Just tap one of the two options below.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Field (captured): {"label":null,"type":"textarea","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e004: n004 -> n005 | condition/label: ""
- Edge e011: n004 -> n012 | condition/label: ""
- Edge e016: n004 -> n017 | condition/label: ""
#### n005 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
CONTACT REPLIES
Yes, soon
```
- Edge e005: n005 -> n006 | condition/label: "CONTACT REPLIES\nYes, soon"
#### n006 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Mentoring program:…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (send_email)
External notification remains a separate continuation; switchToHuman is not an email send.
Business input: recipient, purpose and existing authorized provider
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: email-send
Captured text (not approved outbound copy):
```text
Send email
Send an email to a specified email address.
From	contact@inroapp.com
To	
New lead: @{{contact.username}} | @{{organization.username}}
@{{contact.username}} commented "{{trigger.comment}}" and answered "{{conversation.last_message_received}}" to your question. Your booking link is on its way to them. Reply in the Inrō inbox or on Instagram. Instagram only lets you reply within 24 hours of their last message. Next step: check whether they booked, and follow up if not.
```
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":[{"selected":true,"text":"contact@inroapp.com (Default email)","value":""}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":""}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"<redacted>","value_state":"unknown","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"<redacted>","value_state":"unknown","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":"Select a file","type":"file","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"","value_state":"observed_unset","options":[{"selected":true,"text":"contact@inroapp.com (Default email)","value":""}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e007: n007 -> n008 | condition/label: ""
#### n008 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Book a call
Pick a time
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
2 hours
```
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e010: n010 -> n011 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n2 hours"
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you checked the link yet?
```
- Field (captured): {"label":null,"type":"text","value":"Have you checked the link yet?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- No captured outgoing edge; do not infer completion.
#### n012 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
CONTACT REPLIES
Not yet
```
- Edge e012: n012 -> n013 | condition/label: "CONTACT REPLIES\nNot yet"
#### n013 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Mentoring program:…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e013: n013 -> n014 | condition/label: ""
#### n014 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: click, external
Captured text (not approved outbound copy):
```text
Free starter guide
Open it
```
- Edge e014: n014 -> n015 | condition/label: ""
- Edge e015: n014 -> n016 | condition/label: ""
#### n015 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- No captured outgoing edge; do not infer completion.
#### n016 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
2 hours
```
- Field (captured): {"label":null,"type":"number","value":"2","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n017 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T REPLIED AFTER
20 hours
```
- Field (captured): {"label":null,"type":"number","value":"20","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n018 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
6 hours
```
- Field (captured): {"label":null,"type":"number","value":"6","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6025 / Finish booking setup
Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
```text
Help me prepare: Finish booking setup.
Selected source: inro-6025 - Book more calls from your comments.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Book calls from comments: readiness question
Scope: Use when the booking page or external confirmation needs setup. An already configured booking link needs no new integration.
Source entry: APPLY comment
Source requirements: Agree to a question; Ready now leads to booking; not yet leads to starter material
Source timing: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.
Source outcome: A consultation link or starter resource
Captured text (n001, not approved campaign copy):
Sent, check your DMs
Just sent it to your DMs
It's in your DMs now 🙂
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Use the booking service already named by the owner or source. Do not replace it silently with native Chatfuel booking.
Ask me for: Booking service and URL; Service, availability and time zone; Qualification criteria; Existing authorized access.
1. Confirm the destination service and authorized access. Draft its booking page and required fields using approved availability and time zone. Keep the captured qualification and refusal branches explicit.
2. Verify the page and define confirmation evidence in that service. A link click is not a booking. Native Chatfuel booking statuses do not prove completion in Calendly or another external service. If an automated status bridge is needed, identify a verified existing connection or leave it unresolved.
3. Return draft settings, field mapping, access gaps and separate checks for link delivery and confirmed booking. Do not create a live booking.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
## External Continuation: inro-6025 / Retain the source team-email notification
Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
```text
Help me prepare: Retain the source team-email notification.
Selected source: inro-6025 - Book more calls from your comments.
Goal: Understand what a person needs and help them take the next step toward a call.
Variant: Book calls from comments: readiness question
Scope: Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
Source entry: APPLY comment
Source requirements: Agree to a question; Ready now leads to booking; not yet leads to starter material
Source timing: Link click: 2 hours; reply: 20 hours; opening button: 6 hours.
Source outcome: A consultation link or starter resource
Captured text (n001, not approved campaign copy):
Sent, check your DMs
Just sent it to your DMs
It's in your DMs now 🙂
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: After confirmation, route ready-soon replies to booking and not-yet replies to the starter guide.
Use the existing authorized team mailbox or notification service.
Ask me for: Team recipient and service; Permitted lead fields; Notification condition and approved text; Existing authorized connection.
1. This step is optional if the owner chooses Chatfuel team handoff instead. If the original email notification must remain, verify an existing authorized connection and draft recipient, field mapping and trigger conditions.
2. Do not invent an email-sending bridge. If none is verified, list the missing access and exact next action. Preserve consent and data minimization; prevent duplicate notifications. Verify the recipient and delivery separately from the Chatfuel handoff. Return draft settings only.
3. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
4. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
5. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](booking-inro-6025.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
