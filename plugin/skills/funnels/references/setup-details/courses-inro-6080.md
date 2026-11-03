# Sell one course from comments or DMs

Setup 1.1.0 | courses-inro-6080 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Present the right course and help interested learners reach the offer.
Educators selling one course or a small course catalogue.
Source entry: Course comment or direct message
Source outcome: A link to one course
Source requirements: Press a button before the offer; Remind when the link is not clicked
Source timing: No link click or opening-button click: 3 days.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Send the course URL after confirmation and retain help.
Retained/replaced: Send the course URL after confirmation and retain help.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: No link click or opening-button click: 3 days.. No timed unsolicited message is configured.
Not retained: No click tracking, click-dependent branch or no-click reminder.
Not retained: No imported deterministic graph or source folder/tag tracking.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the course URL after confirmation and retain help.
Target: owned_comment
Ask only for missing business facts:
- course_name: Supply the business value and approve its use in this selected draft. (required)
- course_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Want {course_name}? Reply YES and I will send it.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Here is {course_name}: {course_url}
Let me know if you have any questions!
help: Let me know if you have any questions!
Wait for an actual affirmative reply before delivering: Here is {course_name}: {course_url}
Let me know if you have any questions! On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

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
        "exactTextReply": "Want {course_name}? Reply YES and I will send it."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {course_name}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {course_name}: {course_url}\nLet me know if you have any questions! On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {course_name}: {course_url}\nLet me know if you have any questions!\nhelp: Let me know if you have any questions! The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the course URL after confirmation and retain help.
Target: dm_base
Ask only for missing business facts:
- course_name: Supply the business value and approve its use in this selected draft. (required)
- course_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Want {course_name}? Reply YES and I will send it.
refusal: Understood. I will stop this request.
delivery: Here is {course_name}: {course_url}
Let me know if you have any questions!
help: Let me know if you have any questions!
placement: DM {keyword}.
Wait for an actual affirmative reply before delivering: Here is {course_name}: {course_url}
Let me know if you have any questions! On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
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
    "target": "dm_base",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Want {course_name}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {course_name}: {course_url}\nLet me know if you have any questions! On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {course_name}: {course_url}\nLet me know if you have any questions!\nhelp: Let me know if you have any questions!"
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6080: Sell Your Courses
Full captured settings/provenance: [selected source JSON](../source-records/inro-6080.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment, dm-ai
Captured text (not approved outbound copy):
```text
When
Someone sends you a DM
FILTER MESSAGES
Contains keyword(s)
Course
When
Someone comments on your post
SELECT THE POSTS
All posts
FILTER THE COMMENTS
Comments with keyword(s)
Course
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Comment leads
```
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Hey! Thanks for being here 🙌🏻  Do you want to join my course?
Yes 👀
```
Captured buttons: ["Yes 👀"]
- Edge e002: n002 -> n003 | condition/label: ""
- Edge e009: n002 -> n010 | condition/label: ""
#### n003 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Yes 👀
```
- Edge e003: n003 -> n004 | condition/label: "WHEN BUTTON IS CLICKED\nYes 👀"
#### n004 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Full Course [Topic] | Only $19.90
Learn how to grow your IG.
Check it out 🔗
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBNUVxUWc9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--17d424c03dcec242d292c95638789e306a90f7f2/Join%20Now%20(9).png"]
- Edge e004: n004 -> n005 | condition/label: ""
- Edge e007: n004 -> n008 | condition/label: ""
#### n005 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e005: n005 -> n006 | condition/label: "WHEN LINK IS CLICKED"
#### n006 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Course lead
```
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Let me know if you have any questions!
```
- No captured outgoing edge; do not infer completion.
#### n008 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 days
```
- Edge e008: n008 -> n009 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 days"
#### n009 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
We're running a limited offer for the next 7 days!
```
- No captured outgoing edge; do not infer completion.
#### n010 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
3 days
```
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6080 / Finish the offer destination
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: inro-6080 - Sell Your Courses.
Goal: Present the right course and help interested learners reach the offer.
Variant: Sell one course from comments or DMs
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Course comment or direct message
Source requirements: Press a button before the offer; Remind when the link is not clicked
Source timing: No link click or opening-button click: 3 days.
Source outcome: A link to one course
Captured text (n002, not approved campaign copy):
Hey! Thanks for being here 🙌🏻  Do you want to join my course?
Yes 👀
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Send the course URL after confirmation and retain help.
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
Structured audit: [setup record](courses-inro-6080.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
