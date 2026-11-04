# Keyword DM to link: shared setup wizard

Setup 1.1.0 | link-delivery-manychat-8 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Put the requested guide, resource or destination in the conversation.
Creators and businesses offering a useful next step without a required contact or follow.
Source entry: Keyword in a direct message
Source outcome: A resource link
Source requirements: Match a specified keyword, not every incoming message
Source timing: No exact timer captured.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Send the requested resource URL in response to the DM keyword.
Retained/replaced: Send the requested resource URL in response to the DM keyword.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Direct-message entry
Choose this entry only; do not configure all alternatives. New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Send the requested resource URL in response to the DM keyword.
Target: dm_base
Ask only for missing business facts:
- resource_title: Supply the business value and approve its use in this selected draft. (required)
- resource_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation.
#### Copy and Conversation Instructions
initial: Here is {resource_title}: {resource_url}
refusal: Understood. I will stop this request.
placement: DM {keyword}.
On the actual entry, send the approved resource URL once. Do not claim a visit or send after silence.

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
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New ordinary DM matching {keyword}; subsequent messages must belong to this campaign in the current conversation.. First message: Here is {resource_title}: {resource_url}\nOn the actual entry, send the approved resource URL once. Do not claim a visit or send after silence.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request."
      }
    }
  }
]
```

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### manychat-8: Respond to all your DMs
Full captured settings/provenance: [selected source JSON](../source-records/manychat-8.json). Start: no captured graph.
No runtime graph captured. Setup fields are evidence, not invented messages:
- captured_default: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"Price","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"contents.content20250424093659_147100.1047869889.blocks.f51c211f-1c86-42c9-8423-c1f5966c1337.text","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"contents.content20250424093659_147100.1047869889.blocks.f51c211f-1c86-42c9-8423-c1f5966c1337.text","label":null,"type":null,"value":"Inspection placeholder; not customer copy.","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.follow_up.enable","label":"Follow up to re-engage and build trust","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.ask_for_follow.enable","label":"Automatically ask for a follow to build your audience","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.collect_email.enable","label":"Ask for emails in DMs to keep in touch beyond social","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":"true","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":null,"label":"Button label","type":null,"value":"","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":null,"label":"Link","type":null,"value":"","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
### manychat-286: Respond to all your DMs
Full captured settings/provenance: [selected source JSON](../source-records/manychat-286.json). Start: no captured graph.
No runtime graph captured. Setup fields are evidence, not invented messages:
- resumed_instance: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- resumed_instance: {"name":"contents.content20250424093659_147100.1047869889.blocks.f51c211f-1c86-42c9-8423-c1f5966c1337.text","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- resumed_instance: {"name":"use_cases.follow_up.enable","label":"Follow up to re-engage and build trust","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- resumed_instance: {"name":"use_cases.ask_for_follow.enable","label":"Automatically ask for a follow to build your audience","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- resumed_instance: {"name":"use_cases.collect_email.enable","label":"Ask for emails in DMs to keep in touch beyond social","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":"true","disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_variant: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"sol-inspection-only-286","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_variant: {"name":"contents.content20250424093659_147100.1047869889.blocks.f51c211f-1c86-42c9-8423-c1f5966c1337.text","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":"false","disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_variant: {"name":"contents.content20250424093659_147100.1047869889.blocks.f51c211f-1c86-42c9-8423-c1f5966c1337.text","label":null,"type":null,"value":"Inspection only.","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":"false","disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_variant: {"name":"use_cases.follow_up.enable","label":"Follow up to re-engage and build trust","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_variant: {"name":"use_cases.ask_for_follow.enable","label":"Automatically ask for a follow to build your audience","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- inspection_variant: {"name":"use_cases.collect_email.enable","label":"Ask for emails in DMs to keep in touch beyond social","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- restoration_check: {"name":"triggers.keyword_rules.32080745.keyword_rules_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- restoration_check: {"name":"contents.content20250424093659_147100.1047869889.blocks.f51c211f-1c86-42c9-8423-c1f5966c1337.text","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":"false","disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- restoration_check: {"name":"use_cases.follow_up.enable","label":"Follow up to re-engage and build trust","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- restoration_check: {"name":"use_cases.ask_for_follow.enable","label":"Automatically ask for a follow to build your audience","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- restoration_check: {"name":"use_cases.collect_email.enable","label":"Ask for emails in DMs to keep in touch beyond social","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_invalid":null,"disabled":false,"max":null,"maxlength":null,"min":null,"pattern":null,"required":false,"step":null}}
- captured: {"value":""}
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](link-delivery-manychat-8.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
