# Brands campaign: one DM with a link

Setup 1.1.0 | link-delivery-manychat-432 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Put the requested guide, resource or destination in the conversation.
Creators and businesses offering a useful next step without a required contact or follow.
Source entry: Comment in a Brands campaign
Source outcome: The requested link
Source requirements: Receive one private message with a URL button
Source timing: No exact timer captured.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Send the requested link in the one initial private reply.
Retained/replaced: Send the requested link in the one initial private reply.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the requested link in the one initial private reply.
Target: owned_comment
Ask only for missing business facts:
- resource_title: Supply the business value and approve its use in this selected draft. (required)
- resource_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Here is {resource_title}: {resource_url}
public: {public_text}
refusal: Understood. I will stop this request.
On the actual entry, send the approved resource URL once. Do not claim a visit or send after silence.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Selected entry received -> first
- first: Send the requested response.
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
        "exactTextReply": "Here is {resource_title}: {resource_url}"
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Here is {resource_title}: {resource_url}\nOn the actual entry, send the approved resource URL once. Do not claim a visit or send after silence.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request. The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-432: * Solo DM (Manychat for Brands)
Full captured settings/provenance: [selected source JSON](../source-records/manychat-432.json). Start: trigger.
#### trigger (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment
Captured text (not approved outbound copy):
```text

```
- Field (captured_default): {"name":"replies.0.reply","label":null,"type":null,"value":"Message sent, check your inbox 🚀","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.1.reply","label":null,"type":null,"value":"Done! Look at messages 📩","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"replies.2.reply","label":null,"type":null,"value":"Sent the link! Check your messages 📝","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Edge edge-0: trigger -> node-0 | condition/label: "Starting Step"
#### node-0 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: buttons, dm-ai
Captured text (not approved outbound copy):
```text
Hey! Here's the link you asked for 👇
```
Captured buttons: ["Get the link"]
- Field (captured_default): {"name":"text","label":null,"type":null,"value":"Hey! Here's the link you asked for 👇","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false}}
- Field (captured_default): {"name":"caption","label":null,"type":null,"value":"Get the link","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":"url","label":null,"type":null,"value":"yourlink.com","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- Field (captured_default): {"name":null,"label":"Additional actions","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](link-delivery-manychat-432.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
