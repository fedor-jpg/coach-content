# Keyword DM: button and 60-second follow-up

Setup 1.1.0 | link-delivery-manychat-113 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Put the requested guide, resource or destination in the conversation.
Creators and businesses offering a useful next step without a required contact or follow.
Source entry: Keyword in a direct message
Source outcome: A link and an additional message
Source requirements: Press a button before receiving the link; Receive an unconditional follow-up
Source timing: Inline delay: 60 seconds.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Send the video-system link and captured help copy together after confirmation.
Retained/replaced: Send the video-system link and captured help copy together after confirmation.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Not retained: Exact source timing is not retained: Inline delay: 60 seconds.. No timed unsolicited message is configured.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the video-system link and captured help copy together after confirmation.
Target: dm_base
Ask only for missing business facts:
- resource_title: Supply the business value and approve its use in this selected draft. (required)
- resource_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Want {resource_title}? Reply YES and I will send it.
refusal: Understood. I will stop this request.
delivery: Here you go! Check out the link 👇

Did you have any questions about the video system? I'm here to help! ❤️
{resource_url}
help: Did you have any questions about the video system? I'm here to help! ❤️
placement: DM {keyword}.
Wait for an actual affirmative reply before delivering: Here you go! Check out the link 👇

Did you have any questions about the video system? I'm here to help! ❤️
{resource_url} On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. Keep the additional help copy in the SAME delivery response, not a delayed second message. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.

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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Want {resource_title}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here you go! Check out the link 👇\n\nDid you have any questions about the video system? I'm here to help! ❤️\n{resource_url} On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener. Keep the additional help copy in the SAME delivery response, not a delayed second message. On bare HELP ask for details only. For a concrete question answer only approved knowledge; if unavailable, state that human review is needed without claiming an unconfigured transfer. Never repeat a help invitation instead of answering a concrete question. Pending contact gates still apply.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here you go! Check out the link 👇\n\nDid you have any questions about the video system? I'm here to help! ❤️\n{resource_url}\nhelp: Did you have any questions about the video system? I'm here to help! ❤️"
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-113: Auto-send links in DM
Full captured settings/provenance: [selected source JSON](../source-records/manychat-113.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"viral","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"video","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":null,"value":"viral video","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"viral","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"video","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"viral video","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":null,"label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (inspection_variant): {"name":"","label":null,"type":null,"value":"viral","value_state":"observed","checked":null,"options_exact":null,"validation_exact":{}}
- Field (inspection_variant): {"name":"","label":null,"type":null,"value":"video","value_state":"observed","checked":null,"options_exact":null,"validation_exact":{}}
- Field (inspection_variant): {"name":"","label":null,"type":null,"value":"viral video","value_state":"observed","checked":null,"options_exact":null,"validation_exact":{}}
- Field (inspection_variant): {"name":"","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":null,"options_exact":null,"validation_exact":{}}
- Edge edge-0: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Hey! 👋

Here's a link to the viral video system that will help you crack the code on your next IG Reel or TikTok video!

Want to check it out?
```
Captured buttons: ["Yes, please! 🔥"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hey! 👋\n\nHere's a link to the viral video system that will help you crack the code on your next IG Reel or TikTok video!\n\nWant to check it out?","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Yes, please! 🔥","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-1: node-0 -> node-1 | condition/label: "Yes, please! 🔥"
#### node-1 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Here you go! Check out the link 👇

Did you have any questions about the video system? I'm here to help! ❤️
```
Captured buttons: ["Get it here!"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Here you go! Check out the link 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Did you have any questions about the video system? I'm here to help! ❤️","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Get it here!","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"www.manychat.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":null,"label":null,"type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"time","label":null,"type":"text","value":"60","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":"true","disabled":false,"inputmode":"numeric","max":"60","maxlength":null,"min":"1","minlength":null,"pattern":"[0-9]*","required":false,"step":"1"}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](link-delivery-manychat-113.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
