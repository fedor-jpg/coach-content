# Acknowledge a kind DM with a Like

Setup 1.1.0 | thanks-inro-6223 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Acknowledge kind comments, messages and shared Stories.
Creators and teams who want to respond to audience appreciation.
Source entry: Direct message: AI recognizes appreciation
Source outcome: A Like reaction to a kind message
Source requirements: Wait 1 minute; Like the message
Source timing: Delay: 1 minute.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Reply to appreciation with a short text thank-you instead of an Instagram Like.
Retained/replaced: Reply to appreciation with a short text thank-you instead of an Instagram Like.
Not retained: Exact source timing is not retained: Delay: 1 minute.. No timed unsolicited message is configured.
Not retained: No imported deterministic graph or source folder/tag tracking.
Not retained: No Instagram Like reaction.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- ig-like: Documented Like applies to Facebook, not Instagram.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Reply to appreciation with a short text thank-you instead of an Instagram Like.
Target: dm_base
Ask only for missing business facts:
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Thanks for the kind words!
refusal: Understood. I will stop this request.
placement: DM {keyword}.
On an actual appreciative DM, send a short text thank-you. This is not an Instagram Like; do not claim a reaction or send a timed extra message.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Thanks for the kind words!\nOn an actual appreciative DM, send a short text thank-you. This is not an Instagram Like; do not claim a reaction or send a timed extra message.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request."
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6223: Show love to kind messages
Full captured settings/provenance: [selected source JSON](../source-records/inro-6223.json). Start: n000.
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
A kind message in their own words, su...
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
Wait 1 minutes
```
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"minutes","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":true,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (like)
Instagram likes are not configured by likeContactComment; that field is Facebook-only.
Business input: whether omitting the reaction is acceptable
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: ig-like
Captured text (not approved outbound copy):
```text
❤️
Like message
```
- Edge e002: n002 -> n003 | condition/label: ""
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Thanks: praised us
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](thanks-inro-6223.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
