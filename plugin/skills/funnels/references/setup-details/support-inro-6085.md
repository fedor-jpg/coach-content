# AI support: team backup after 24 hours

Setup 1.1.0 | support-inro-6085 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Help people find an answer and involve the team when needed.
Businesses receiving product, website or service questions in DMs.
Source entry: Direct message asking a question or requesting help
Source outcome: A resolved question or a team notification
Source requirements: AI answers; If unresolved after 24 hours, email the team
Source timing: AI handover expiration: 24 hours.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Answer from approved facts and hand unresolved questions or explicit requests to the Chatfuel team.
Retained/replaced: Answer from approved facts and hand unresolved questions or explicit requests to the Chatfuel team.
Not retained: Exact source timing is not retained: AI handover expiration: 24 hours.. No timed unsolicited message is configured.
Not retained: No imported deterministic graph or source folder/tag tracking.
Not retained: No outbound escalation email or external booking-completion check.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- email-send: No arbitrary outbound email action; handoff does not reproduce source email notifications.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Direct-message entry
Choose this entry only; do not configure all alternatives. Actual incoming support question. Preserve unrelated support.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Answer from approved facts and hand unresolved questions or explicit requests to the Chatfuel team.
Target: dm_base
Ask only for missing business facts:
- service_name: Supply the business value and approve its use in this selected draft. (required)
- known_facts: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text, handoff_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Thanks for your message. How can we help with {service_name}?
refusal: Understood. I will stop this request.
handoff: {handoff_text}
answer: {known_facts}
placement: DM {keyword}.
Answer only from {known_facts}. On an unresolved question, inability to finish or explicit team request, use switchToHuman and {handoff_text}. This is an actual Chatfuel team handoff draft, not outbound email. No automatic 24-hour escalation, resolution tag or promised response deadline.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: Actual incoming support question. Preserve unrelated support.
  - If Actual question or help request -> first
- first: Answer the actual question from approved facts.
  - If Unresolved question, inability to finish, or explicit team request -> handoff
  - If Actual refusal -> refusal
  - If No new reply -> silence
- handoff: Transfer an unresolved question or explicit team request.
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: Actual incoming support question. Preserve unrelated support.. First message: Thanks for your message. How can we help with {service_name}?\nAnswer only from {known_facts}. On an unresolved question, inability to finish or explicit team request, use switchToHuman and {handoff_text}. This is an actual Chatfuel team handoff draft, not outbound email. No automatic 24-hour escalation, resolution tag or promised response deadline.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\nhandoff: {handoff_text}\nanswer: {known_facts}"
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
### inro-6085: Answer every DM with AI, team as backup
Full captured settings/provenance: [selected source JSON](../source-records/inro-6085.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
When
Someone sends you a DM
FILTER MESSAGES
AI-detected intent
Asks a question or for help in their ...
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (agent_handover)
The Inro agent is an AI agent in this capture. Do not relabel it as human handoff.
Business input: approved knowledge and team fallback
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Hand over to AI Agent
Hand over all incoming messages to the AI Agent until the conversation ends
```
- Field (captured): {"label":null,"type":"textarea","value":"Goal: answer the person's question from the knowledge base in one or two short messages, with one question back at most.\nDone only when they have their answer or the link they need.\nIf the answer is not in the knowledge base, or they ask for a person, say the team will reply here. That does not complete the task.","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"button","value":false,"value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"Goal: answer the person's question from the knowledge base in one or two short messages, with one question back at most.\nDone only when they have their answer or the link they need.\nIf the answer is not in the knowledge base, or they ask for a person, say the team will reply here. That does not complete the task.","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"switch","value":true,"value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"select-one","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e001: n001 -> n002 | condition/label: ""
- Edge e003: n001 -> n004 | condition/label: ""
#### n002 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
TASK COMPLETED
```
- Edge e002: n002 -> n003 | condition/label: "TASK COMPLETED"
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Front desk: resolv…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
#### n004 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
HANDOVER EXPIRED
24 hours
```
- Field (captured): {"label":null,"type":"number","value":"24","value_state":"observed_value","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"hours","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":false,"text":"minutes","value":"minutes"},{"selected":true,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":null}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e004: n004 -> n005 | condition/label: "HANDOVER EXPIRED\n24 hours"
#### n005 (send_email)
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
Needs a human: @{{contact.username}} | @{{organization.username}}
The AI couldn't finish with @{{contact.username}}. First message: "{{trigger.message}}" Latest message: "{{conversation.last_message_received}}" Reply in the Inrō inbox or on Instagram. If Instagram blocks the reply, the 24-hour window has closed: answer when they next write. Next step: answer, then remove them from "Needs a human".
```
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":[{"selected":true,"text":"contact@inroapp.com (Default email)","value":""}],"validation":null}
- Field (captured): {"value":""}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":null}
- Field (captured): {"label":null,"type":"text","value":"<redacted>","value_state":"unknown","options":null,"validation":null}
- Field (captured): {"label":null,"type":"textarea","value":"<redacted>","value_state":"unknown","options":null,"validation":null}
- Field (captured): {"label":"Select a file","type":"file","value":"","value_state":"observed_unset","options":null,"validation":null}
- Field (captured): {"label":null,"type":"select-one","value":"","value_state":"observed_unset","options":[{"selected":true,"text":"contact@inroapp.com (Default email)","value":""}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"<redacted>","value_state":"unknown","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"textarea","value":"<redacted>","value_state":"unknown","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":"Select a file","type":"file","value":"","value_state":"observed_unset","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Edge e005: n005 -> n006 | condition/label: ""
#### n006 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Needs a human
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6085 / Retain the source team-email notification
Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
```text
Help me prepare: Retain the source team-email notification.
Selected source: inro-6085 - Answer every DM with AI, team as backup.
Goal: Help people find an answer and involve the team when needed.
Variant: AI support: team backup after 24 hours
Scope: Optional: retain the captured external email notification instead of replacing it with Chatfuel handoff.
Source entry: Direct message asking a question or requesting help
Source requirements: AI answers; If unresolved after 24 hours, email the team
Source timing: AI handover expiration: 24 hours.
Source outcome: A resolved question or a team notification
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Answer from approved facts and hand unresolved questions or explicit requests to the Chatfuel team.
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
Structured audit: [setup record](support-inro-6085.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
