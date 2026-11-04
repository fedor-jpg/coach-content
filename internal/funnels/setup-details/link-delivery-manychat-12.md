# Auto-DM links from comments

Setup 1.1.0 | link-delivery-manychat-12 | adaptation_draft_requires_consent | runtime not tested

## Business Result
Put the requested guide, resource or destination in the conversation.
Creators and businesses offering a useful next step without a required contact or follow.
Source entry: Keyword comment
Source outcome: A link after confirmation
Source requirements: Opening DM and confirmation button before the link
Source timing: No exact timer captured.

## Functional Availability
adaptation_draft_requires_consent
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Ask for confirmation, then send the requested link.
Retained/replaced: Ask for confirmation, then send the requested link.
Retained/replaced: URL buttons become readable URLs; confirmation and help controls become actual user replies.
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Selected-post comment entry
Choose this entry only; do not configure all alternatives. New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
Entry change: Source entry retained. UI controls use actual replies or plain URLs; no source-specific entry is silently substituted.
Output: Ask for confirmation, then send the requested link.
Target: owned_comment
Ask only for missing business facts:
- resource_title: Supply the business value and approve its use in this selected draft. (required)
- resource_url: Supply the business value and approve its use in this selected draft. (required)
Assistant-derived, not questionnaire fields: campaign, language, keyword, public_text. Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft.
#### Preparation Gates
- Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval.
#### Copy and Conversation Instructions
initial: Want {resource_title}? Reply YES and I will send it.
public: {public_text}
refusal: Understood. I will stop this request.
delivery: Here is {resource_title}: {resource_url}
Wait for an actual affirmative reply before delivering: Here is {resource_title}: {resource_url} On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener.

Contact rule: No contact capture in this plan.
#### Intended Alternative Branches (Instructions, Not Imported Flow)
- entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.
  - If Selected entry received -> first
- first: Ask for an actual affirmative reply; no link yet.
  - If Actual affirmative reply in this conversation -> delivery
  - If Actual refusal -> refusal
  - If No actual reply -> silence
- delivery: Deliver the approved destination and included help together.
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
        "exactTextReply": "Want {resource_title}? Reply YES and I will send it."
      }
    }
  },
  {
    "tool": "update_automation_setting",
    "target": "owned_comment",
    "settings": {
      "incomingMessages": {
        "howToReply": "UsingAI",
        "messagePrompt": "Campaign {campaign}. Language: {language}. Entry: New matching {keyword} comment on the selected post; continuation only after a verified linked actual reply.. First message: Want {resource_title}? Reply YES and I will send it.\nWait for an actual affirmative reply before delivering: Here is {resource_title}: {resource_url} On bare HELP ask what assistance is needed. For an actual question, answer only approved facts; otherwise state that human review is needed without promising an unconfigured handoff. Do not repeat the help invitation. Do not infer confirmation from a comment, silence, button click or URL visit. Do not resend the opener.\n\nHandle refusal before keyword matching. On refusal: Understood. I will stop this request. End this campaign. Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support.\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\nrefusal: Understood. I will stop this request.\ndelivery: Here is {resource_title}: {resource_url} The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
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
### manychat-12: Auto-DM links from comments
Full captured settings/provenance: [selected source JSON](../source-records/manychat-12.json). Start: no captured graph.
No runtime graph captured. Setup fields are evidence, not invented messages:
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"a specific post or reel","type":"radio","value":"specific_post","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"any post or reel","type":"radio","value":"all_posts","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"next post or reel","type":"radio","value":"next_post","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"a specific word or words","type":"radio","value":"specific_words","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.include_keywords_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"any word","type":"radio","value":"any_words","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.publicly_reply_to_comment.enable","label":"reply to their comments under the post","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"a specific post or reel","type":"radio","value":"specific_post","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"any post or reel","type":"radio","value":"all_posts","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"next post or reel","type":"radio","value":"next_post","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"a specific word or words","type":"radio","value":"specific_words","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.widgets.37456583.feed_comment_settings.include_keywords_input","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":"true","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"any word","type":"radio","value":"any_words","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- inspection_observation: {"name":"use_cases.publicly_reply_to_comment.enable","label":"reply to their comments under the post","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"a specific word or words","type":"radio","value":"specific_words","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"any word","type":"radio","value":"any_words","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":null,"label":"an opening DM","type":"checkbox","value":"on","value_state":"observed","checked":true,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"contents.content20240829181834_361233.1021777883.blocks.cc0d6fa1-d597-43d6-96ad-754bb1d6f4e6.text","label":null,"type":null,"value":"Hey there! I’m so happy you’re here, thanks so much for your interest 😊 \n\nClick below and I’ll send you the link in just a sec ✨","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"contents.content20240829181834_361233.1021777883.blocks.1e137234-7aef-4ff6-bddc-64c757d7f901.caption","label":null,"type":null,"value":"Send me the link","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.ask_for_follow.enable","label":"a DM asking to follow you before they get the link","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.collect_email.enable","label":"a DM asking for their email","type":"checkbox","value":"<redacted>","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"contents.content20240829181834_361233.1021777908.blocks.0f737649-51ed-4cc6-8360-d7e68b7bf11a.text","label":null,"type":null,"value":"","value_state":"unset_client_input_required","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured_default: {"name":"use_cases.follow_up.enable","label":"a follow up DM if they don't click the link","type":"checkbox","value":"on","value_state":"observed","checked":false,"options_exact":null,"validation_exact":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"a specific post or reel","type":"radio","value":"specific_post","checked":true,"options":null,"validation":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"any post or reel","type":"radio","value":"all_posts","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.post_covered_area","label":"next post or reel","type":"radio","value":"next_post","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"a specific word or words","type":"radio","value":"specific_words","checked":true,"options":null,"validation":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.include_keywords_input","label":null,"type":null,"value":"","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"any word","type":"radio","value":"any_words","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"use_cases.publicly_reply_to_comment.enable","label":"reply to their comments under the post","type":"checkbox","value":"on","checked":true,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_welcome.public_reply_messages.0","label":null,"type":null,"value":"Thanks! Please see DMs.","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_welcome.public_reply_messages.1","label":null,"type":null,"value":"Sent you a message! Check it out!","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_welcome.public_reply_messages.2","label":null,"type":null,"value":"Nice! Check your DMs!","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"a specific word or words","type":"radio","value":"specific_words","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"triggers.widgets.37456583.feed_comment_settings.comment_contains","label":"any word","type":"radio","value":"any_words","checked":true,"options":null,"validation":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"use_cases.publicly_reply_to_comment.enable","label":"reply to their comments under the post","type":"checkbox","value":"on","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":null,"label":"an opening DM","type":"checkbox","value":"on","checked":true,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"contents.content20240829181834_361233.1021777883.blocks.cc0d6fa1-d597-43d6-96ad-754bb1d6f4e6.text","label":null,"type":null,"value":"Hey there! I’m so happy you’re here, thanks so much for your interest 😊 \n\nClick below and I’ll send you the link in just a sec ✨","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":"false","aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"contents.content20240829181834_361233.1021777883.blocks.1e137234-7aef-4ff6-bddc-64c757d7f901.caption","label":null,"type":null,"value":"Send me the link","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"use_cases.ask_for_follow.enable","label":"a DM asking to follow you before they get the link","type":"checkbox","value":"on","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":"use_cases.collect_email.enable","label":"a DM asking for their email","type":"checkbox","value":"<redacted>","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":null,"label":"an opening DM","type":"checkbox","value":"on","checked":false,"options":null,"validation":{"aria_disabled":"false","aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":null,"label":"Button label","type":null,"value":"","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
- captured: {"name":null,"label":"Link","type":null,"value":"","checked":false,"options":null,"validation":{"aria_disabled":null,"aria_invalid":null,"aria_required":null,"disabled":false,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"required":false,"step":null}}
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](link-delivery-manychat-12.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
