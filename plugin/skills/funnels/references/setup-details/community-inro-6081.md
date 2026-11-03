# Launch waitlist: optional email

Setup 1.1.0 | community-inro-6081 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Invite interested people into your next launch or a shared community.
Creators launching an offer or welcoming members.
Source entry: WAITLIST comment or Story reply
Source outcome: Waitlist participation without requiring email
Source requirements: Confirm joining; Ask for optional email after joining
Source timing: Email: 20 hours; opening button: 6 hours.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Collect consented waitlist join or STOP intent and optional email; saved membership remains unverified.
Retained/replaced: Collect consented waitlist join or STOP intent and optional email; saved membership remains unverified.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Email: 20 hours; opening button: 6 hours.. No timed unsolicited message is configured.
Not retained: No imported deterministic graph or source folder/tag tracking.
Not retained: Only comment entry is prepared; Story-specific entry remains unavailable through ordinary MCP.
Limitation: Contact-value persistence is unverified. Capture configuration and chat text do not prove a saved value or external list membership.
Limitation: Join/STOP intent and optional email can be drafted. Saved membership/withdrawal confirmation is BLOCKED pending actual persistence proof.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- story: Story-specific configuration is dashboard-only for normal MCP. Ordinary DM does not verify a Story reply or mention.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Only the comment entry is prepared. Story replies remain dashboard-only; owner must approve the narrowed entry.
Output: Collect consented waitlist join or STOP intent and optional email; saved membership remains unverified.
Target: owned_comment
Ask only for missing business facts:
- launch_name: Supply the business value and approve its use in this selected draft. (required)
- launch_purpose: Supply the business value and approve its use in this selected draft. (required)
- contact_purpose: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, consent_text, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
- Normal MCP has no contact-attribute-value reader. Capture configuration readback and chat text do not prove saved email/phone, joined membership or withdrawal. Keep value-dependent confirmation or handoff unresolved; simple preparation remains available.
#### Copy and Conversation Instructions
initial: Want to join the waitlist for {launch_name}? {consent_text} Reply YES to request joining, or STOP.
public: {public_text}
refusal: Understood. I will stop this request.
joined: Thanks, I received your request. You may also share an email for {contact_purpose}, or reply SKIP.
withdrawn: Understood. I will stop this conversation.
email: Thanks for your reply.
Collect only current consented join intent for {launch_purpose}. YES requests joined; STOP requests withdrawn and stops this conversation. Configure membership and optional email captures for {contact_purpose}, preserving all existing captures. Never say joined, on the list, saved or withdrawn as a completed outcome without actual saved-value readback. Normal MCP cannot read contact attribute values. Chat text and capture configuration are not proof. Optional email or SKIP never controls join intent. No external list, launch alert or saved-state-dependent handoff is configured. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

Contact rule: Join/STOP intent and optional email can be drafted. Saved membership/withdrawal confirmation is BLOCKED pending actual persistence proof.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Matching comment -> first
- first: Ask for actual join intent.
  - If Actual YES reply -> joined
  - If Actual STOP reply -> withdrawn
  - If No actual reply -> silence
- joined: Record a join request; do not confirm saved membership.
  - If Actual STOP reply -> withdrawn
  - If New optional consented email or SKIP -> email
- withdrawn: Record STOP intent; do not confirm saved withdrawal.
- email: Optional email or SKIP; persistence remains unverified.
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
        "exactTextReply": "Want to join the waitlist for {launch_name}? {consent_text} Reply YES to request joining, or STOP."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want to join the waitlist for {launch_name}? {consent_text} Reply YES to request joining, or STOP.\nCollect only current consented join intent for {launch_purpose}. YES requests joined; STOP requests withdrawn and stops this conversation. Configure membership and optional email captures for {contact_purpose}, preserving all existing captures. Never say joined, on the list, saved or withdrawn as a completed outcome without actual saved-value readback. Normal MCP cannot read contact attribute values. Chat text and capture configuration are not proof. Optional email or SKIP never controls join intent. No external list, launch alert or saved-state-dependent handoff is configured. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\njoined: Thanks, I received your request. You may also share an email for {contact_purpose}, or reply SKIP.\nwithdrawn: Understood. I will stop this conversation.\nemail: Thanks for your reply. The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
      "attribute": "$resolved.verified_membership_attribute",
      "description": "Campaign {campaign}; membership for {contact_purpose}: Join/STOP intent and optional email can be drafted. Saved membership/withdrawal confirmation is BLOCKED pending actual persistence proof."
    },
    {
      "attribute": "$resolved.verified_email_attribute",
      "description": "Campaign {campaign}; email for {contact_purpose}: Join/STOP intent and optional email can be drafted. Saved membership/withdrawal confirmation is BLOCKED pending actual persistence proof."
    }
  ]
}
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6081: Build a waitlist for your next launch
Full captured settings/provenance: [selected source JSON](../source-records/inro-6081.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: comment, dm-ai, story
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
Next post only
FILTER THE COMMENTS
Comments with keyword(s)
WAITLIST
When
Someone replies to your story
FILTER REPLIES
Contains a keyword
WAITLIST
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (comment)
A fixed public reply is a documented primitive, not proof of captured random text choice or downstream routing.
Business input: approved public reply
Setting candidate: update_automation_setting: publicReply
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text
Check your DMs to join the list
Sent you a DM 🙂
Just sent you the details
```
- Field (captured): {"label":null,"type":"text","value":"Check your DMs to join the list","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Sent you a DM 🙂","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Just sent you the details","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
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
Want to join the waitlist for the spring drop? Tap below.
Join the list
```
Captured buttons: ["Join the list"]
- Field (captured): {"label":null,"type":"textarea","value":"Want to join the waitlist for the spring drop? Tap below.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"Join the list","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"url","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":false,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e002: n002 -> n003 | condition/label: ""
- Edge e008: n002 -> n009 | condition/label: ""
#### n003 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Join the list
```
- Edge e003: n003 -> n004 | condition/label: "WHEN BUTTON IS CLICKED\nJoin the list"
#### n004 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Spring drop waitli…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- Edge e004: n004 -> n005 | condition/label: ""
#### n005 (collect_property)
Contact storage is documented. Exact validation gates, retries and external subscriptions are separate dependencies.
Business input: purpose, required versus optional contact, channel consent
Setting candidate: update_automation_setting: collectContactInfo
Disposition: requires_change_or_external_dependency; dependencies: contact, graph
Captured text (not approved outbound copy):
```text
Ask for information
Collect email, phone or any contact property and save it automatically.
You're on the list. Want to leave your email too?
Message without the information
You're on the list either way. If you meant to send an email, check it and send it again.
Email
```
- Field (captured): {"label":null,"type":"textarea","value":"You're on the list. Want to leave your email too?","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"button","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"You're on the list either way. If you meant to send an email, check it and send it again.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
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
- Edge e007: n005 -> n008 | condition/label: ""
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
#### n007 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Thanks, got it. You're all set.
```
- Field (captured): {"label":null,"type":"text","value":"Thanks, got it. You're all set.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- No captured outgoing edge; do not infer completion.
#### n008 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF INFORMATION HAS NOT BEEN RECEIVED AFTER
20 hours
```
- Field (captured): {"label":null,"type":"number","value":"20","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- No captured outgoing edge; do not infer completion.
#### n009 (branch_expiration)
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
## External Continuation: inro-6081 / Finish email-list signup
Optional: only if the owner also wants email marketing signup. Resource delivery or waitlist participation alone does not require it.
```text
Help me prepare: Finish email-list signup.
Selected source: inro-6081 - Build a waitlist for your next launch.
Goal: Invite interested people into your next launch or a shared community.
Variant: Launch waitlist: optional email
Scope: Optional: only if the owner also wants email marketing signup. Resource delivery or waitlist participation alone does not require it.
Source entry: WAITLIST comment or Story reply
Source requirements: Confirm joining; Ask for optional email after joining
Source timing: Email: 20 hours; opening button: 6 hours.
Source outcome: Waitlist participation without requiring email
Captured text (n001, not approved campaign copy):
Check your DMs to join the list
Sent you a DM 🙂
Just sent you the details
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Collect consented waitlist join or STOP intent and optional email; saved membership remains unverified.
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
Structured audit: [setup record](community-inro-6081.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
