# Recognize a website question and reply

Setup 1.1.0 | support-manychat-46 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Help people find an answer and involve the team when needed.
Businesses receiving product, website or service questions in DMs.
Source entry: Direct message with AI-recognized website intent
Source outcome: An answer about the website
Source requirements: Recognize intent; Return fixed website copy and a link
Source timing: No exact timer captured.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Answer website-interest DMs with the approved website URL.
Retained/replaced: Answer website-interest DMs with the approved website URL.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
### Direct-message entry
Choose this entry only; do not configure all alternatives. Actual incoming DM asking about the website. Answer only that intent from approved website facts and its verified URL; preserve unrelated support.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Answer website-interest DMs with the approved website URL.
Target: dm_base
Ask only for missing business facts:
- website_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Thanks for your interest! Here is our website: {website_url}
refusal: Understood. I will stop this request.
placement: DM {keyword}.
On a new message expressing website interest, offer the approved website URL. Do not invent website facts, subscription or visit proof.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: Actual incoming DM asking about the website. Answer only that intent from approved website facts and its verified URL; preserve unrelated support.
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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: Actual incoming DM asking about the website. Answer only that intent from approved website facts and its verified URL; preserve unrelated support.. First message: Thanks for your interest! Here is our website: {website_url}\nOn a new message expressing website interest, offer the approved website URL. Do not invent website facts, subscription or visit proof.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request."
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-46: Recognize questions in DM with AI
Full captured settings/provenance: [selected source JSON](../source-records/manychat-46.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":"Person wants to...","type":null,"value":"Person asks for the website","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-0: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Thanks for your interest! 🌟 Here's our website: https://manychat.com/
```
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Thanks for your interest! 🌟 Here's our website: https://manychat.com/","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](support-manychat-46.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
