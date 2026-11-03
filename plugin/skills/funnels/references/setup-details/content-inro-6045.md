# Grow YouTube or podcast visits: help after a click

Setup 1.1.0 | content-inro-6045 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Bring Instagram interest to your video, podcast or another channel.
Creators distributing existing YouTube, TikTok or podcast content.
Source entry: Keyword comment or direct message
Source outcome: A content link and a help branch
Source requirements: Press the opening button; Wait 3 seconds; Offer help after the click
Source timing: Before link: 3 seconds; no click or opening button: 3 days.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Deliver the selected video or podcast link after confirmation; retain help through actual replies.
Retained/replaced: Deliver the selected video or podcast link after confirmation; retain help through actual replies.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Before link: 3 seconds; no click or opening button: 3 days.. No timed unsolicited message is configured.
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
### Selected-post comment entry / Video
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the video link after an actual YES reply and retain help.
Target: owned_comment
Ask only for missing business facts:
- video_title: Supply the business value and approve its use in this selected draft. (required)
- video_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Want {video_title}? Reply YES and I will send it.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Here is {video_title}: {video_url}
Let me know if you have any questions!
help: Let me know if you have any questions!
Wait for an actual affirmative reply before delivering: Here is {video_title}: {video_url}
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
        "exactTextReply": "Want {video_title}? Reply YES and I will send it."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {video_title}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {video_title}: {video_url}\nLet me know if you have any questions! On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {video_title}: {video_url}\nLet me know if you have any questions!\nhelp: Let me know if you have any questions! The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
### Direct-message entry / Video
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the video link after an actual YES reply and retain help.
Target: dm_base
Ask only for missing business facts:
- video_title: Supply the business value and approve its use in this selected draft. (required)
- video_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Want {video_title}? Reply YES and I will send it.
refusal: Understood. I will stop this request.
delivery: Here is {video_title}: {video_url}
Let me know if you have any questions!
help: Let me know if you have any questions!
placement: DM {keyword}.
Wait for an actual affirmative reply before delivering: Here is {video_title}: {video_url}
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Want {video_title}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {video_title}: {video_url}\nLet me know if you have any questions! On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {video_title}: {video_url}\nLet me know if you have any questions!\nhelp: Let me know if you have any questions!"
      }
    }
  }
]
```
### Selected-post comment entry / Podcast
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the podcast link after an actual YES reply and retain help.
Target: owned_comment
Ask only for missing business facts:
- episode_title: Supply the business value and approve its use in this selected draft. (required)
- episode_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Want {episode_title}? Reply YES and I will send it.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Here is {episode_title}: {episode_url}
Let me know if you have any questions! 
help: Let me know if you have any questions! 
Wait for an actual affirmative reply before delivering: Here is {episode_title}: {episode_url}
Let me know if you have any questions!  On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

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
        "exactTextReply": "Want {episode_title}? Reply YES and I will send it."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {episode_title}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {episode_title}: {episode_url}\nLet me know if you have any questions!  On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {episode_title}: {episode_url}\nLet me know if you have any questions! \nhelp: Let me know if you have any questions!  The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
### Direct-message entry / Podcast
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the podcast link after an actual YES reply and retain help.
Target: dm_base
Ask only for missing business facts:
- episode_title: Supply the business value and approve its use in this selected draft. (required)
- episode_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Want {episode_title}? Reply YES and I will send it.
refusal: Understood. I will stop this request.
delivery: Here is {episode_title}: {episode_url}
Let me know if you have any questions! 
help: Let me know if you have any questions! 
placement: DM {keyword}.
Wait for an actual affirmative reply before delivering: Here is {episode_title}: {episode_url}
Let me know if you have any questions!  On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Want {episode_title}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {episode_title}: {episode_url}\nLet me know if you have any questions!  On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {episode_title}: {episode_url}\nLet me know if you have any questions! \nhelp: Let me know if you have any questions! "
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6045: Grow Your YouTube
Full captured settings/provenance: [selected source JSON](../source-records/inro-6045.json). Start: n000.
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
All posts
FILTER THE COMMENTS
Comments with keyword(s)
Tutorial
When
Someone sends you a DM
FILTER MESSAGES
Contains keyword(s)
Tutorial
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Hi {{contact.name}}! ❤️
Do you want the full video?
Yesss 👀
```
Captured buttons: ["Yesss 👀"]
- Edge e001: n001 -> n002 | condition/label: ""
- Edge e009: n001 -> n010 | condition/label: ""
#### n002 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Yesss 👀
```
- Edge e002: n002 -> n003 | condition/label: "WHEN BUTTON IS CLICKED\nYesss 👀"
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
youtube leads
```
- Edge e003: n003 -> n004 | condition/label: ""
#### n004 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
Wait 3 seconds
```
- Edge e004: n004 -> n005 | condition/label: ""
#### n005 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Check the full video!
Explore how to grow your IG.
Check it out 🔗
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBMkRBUEE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--33264cdf0859918a926931e848a8df49cfe0da84/Join%20Now%20(3).png"]
- Edge e005: n005 -> n006 | condition/label: ""
- Edge e007: n005 -> n008 | condition/label: ""
#### n006 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e006: n006 -> n007 | condition/label: "WHEN LINK IS CLICKED"
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
Have you checked it out yet?
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
### inro-6047: Grow Your Podcast
Full captured settings/provenance: [selected source JSON](../source-records/inro-6047.json). Start: n000.
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
All posts
FILTER THE COMMENTS
Comments with keyword(s)
podcast
When
Someone sends you a DM
FILTER MESSAGES
Contains keyword(s)
podcast
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Hi {{contact.name}}! ❤️ Do you want to see the full video?
Yes 👀
```
Captured buttons: ["Yes 👀"]
- Edge e001: n001 -> n002 | condition/label: ""
- Edge e009: n001 -> n010 | condition/label: ""
#### n002 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Yes 👀
```
- Edge e002: n002 -> n003 | condition/label: "WHEN BUTTON IS CLICKED\nYes 👀"
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
podcast leads
```
- Edge e003: n003 -> n004 | condition/label: ""
#### n004 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
Wait 3 seconds
```
- Edge e004: n004 -> n005 | condition/label: ""
#### n005 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Check the full podcast here!
Explore how to grow your IG.
Check it out 🎵
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBeHpBUEE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--9bbd9b1834d21693977e74ffd2699642b77811a5/Untitled%20design%20-%202025-10-16T105356.308.png"]
- Edge e005: n005 -> n006 | condition/label: ""
- Edge e007: n005 -> n008 | condition/label: ""
#### n006 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e006: n006 -> n007 | condition/label: "WHEN LINK IS CLICKED"
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
Have you checked it out yet?
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
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](content-inro-6045.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
