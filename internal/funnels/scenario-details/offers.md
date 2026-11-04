# Send product offers and coupons
Deliver a relevant product offer or coupon while interest is high.
Shops and creators using comments, Stories or Lives to promote an offer.

No launch or full-path test. Before any change, verify current host tools, account state, overlapping rules and owner approval.
setup_comment_replies creates and enables a rule and may change Main/base; it is not draft creation.
Ordinary tools expose no create-OFF, exact inheritance restoration or continuing comment preview.
test_reply previews DM only. Pausing an automation does not disable Main.
Do not transfer user settings or cross-chat state. catalog.json remains the separate accepted registry.

Profile: ordinary Chatfuel MCP. Documentation observation: 2026-11-02. Not an account test.

## Sell products during a Live
waiting_for_chatfuel
Entry: Comment during a Live
Outcome: A product offer
Requirements: Press the opening button; Click the product link
Timing: No link click: 2 hours; opening button: 6 hours.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: A product offer
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- live: not_exposed; inference_from_tool_inputs; setup_comment_replies; . Post/comment configuration does not establish a Live-comment entry tool.
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-4393: Sending an offer does not confirm a purchase. [Described analogue inro-4393](../native-recipes/inro-4393.md)
### Finish the offer destination - inro-4393
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: inro-4393 - Sell your products during a live.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Sell products during a Live
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Comment during a Live
Source requirements: Press the opening button; Click the product link
Source timing: No link click: 2 hours; opening button: 6 hours.
Source outcome: A product offer
Captured text (n001, not approved campaign copy):
Thanks for joining the live! Want the product picks? Tap below.
Yes, send it
Current setup decision: waiting_for_chatfuel. This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary Chatfuel result: A product offer
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Live leads: product or course by interest
waiting_for_chatfuel
Entry: Comment during a Live
Outcome: An offer matching the chosen interest
Requirements: Choose an interest: products or course; Receive the matching offer
Timing: Link clicks: 3 hours and 3 days; no reply: 3 days.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: An offer matching the chosen interest
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- live: not_exposed; inference_from_tool_inputs; setup_comment_replies; . Post/comment configuration does not establish a Live-comment entry tool.
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: not_exposed; inference_from_tool_inputs; update_automation_setting; . No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-4484: Choosing an offer does not confirm a purchase. [Described analogue inro-4484](../native-recipes/inro-4484.md)

## Live offer: reveal one coupon
waiting_for_chatfuel
Entry: Keyword comment during a Live
Outcome: The SECRET10 coupon
Requirements: Press the coupon-reveal button
Timing: No separate exact timer captured.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary result: The SECRET10 coupon
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: Live keyword, coupon, destination, validity policy
### Capability evidence
- live: not_exposed; inference_from_tool_inputs; setup_comment_replies; . Post/comment configuration does not establish a Live-comment entry tool.
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- manychat-63: The 24 hours in copy do not establish an expiration timer. [Described analogue inro-4393](../native-recipes/inro-4393.md)
### Finish the offer destination - manychat-63
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-63 - Send offers in DMs during Live.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Live offer: reveal one coupon
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Keyword comment during a Live
Source requirements: Press the coupon-reveal button
Source timing: No exact timer captured.
Source outcome: The SECRET10 coupon
Captured text (node-0, not approved campaign copy):
I'm so excited you want my VIP-only secret coupon code. 🤫

Tap below to get it 👇
Current setup decision: waiting_for_chatfuel. This scenario starts from a Live comment. Ordinary MCP cannot configure that Live-specific entry. An ordinary post comment or DM would be a different scenario.
Primary Chatfuel result: The SECRET10 coupon
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Story offer: reveal a coupon
waiting_for_chatfuel
Entry: Keyword reply to a Story
Outcome: The MYBDAYGIFT coupon
Requirements: Press the coupon-reveal button
Timing: No separate exact timer captured.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
This scenario starts from a Story reply. Ordinary MCP cannot configure the Story-specific entry. An ordinary DM keyword would be a different entry, not this setup.
Primary result: The MYBDAYGIFT coupon
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: story, keyword, coupon, validity policy, destination
### Capability evidence
- story: dashboard_only; automation-settings_playbook; update_automation_setting; listOfStories. Story-specific configuration is dashboard-only for normal MCP. Ordinary DM does not verify a Story reply or mention.
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- manychat-66: No specific Story was selected. All Stories was restored; a date in copy is not an expiration timer. No authored analogue; this does not establish tool availability.
### Finish the offer destination - manychat-66
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-66 - Give coupons in stories.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Story offer: reveal a coupon
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Keyword reply to a Story
Source requirements: Press the coupon-reveal button
Source timing: No exact timer captured.
Source outcome: The MYBDAYGIFT coupon
Captured text (node-0, not approved campaign copy):
Guess what?! Until February 28th, you get 25% OFF storewide, plus FREE shipping! 🎁

Tap below to review your code!
Current setup decision: waiting_for_chatfuel. This scenario starts from a Story reply. Ordinary MCP cannot configure the Story-specific entry. An ordinary DM keyword would be a different entry, not this setup.
Primary Chatfuel result: The MYBDAYGIFT coupon
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Reel coupon: help after 2 minutes
adaptation_draft_requires_consent
Entry: Comment on a Reel
Outcome: The HAPPY10 coupon and a help message
Requirements: Press the opening button; Receive unconditional help after 2 minutes
Timing: Unconditional delay: 2 minutes. The 48-hour validity appears only in copy.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary result: Send the coupon, store URL and captured help copy together after confirmation.
Retained: Send the coupon, store URL and captured help copy together after confirmation.; URL buttons become readable URLs; confirmation and help controls become actual user replies.
Omitted: Exact source timing is not retained: Unconditional delay: 2 minutes. The 48-hour validity appears only in copy.. No timed unsolicited message is configured.
Limitations: 
Missing source facts: None blocking this assessment.
Client inputs: post, keywords, coupon, destination, validity policy
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- manychat-72: The 48 hours in copy do not establish an expiration timer. No authored analogue; this does not establish tool availability.
### Finish the offer destination - manychat-72
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-72 - Sell from Reel comments.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Reel coupon: help after 2 minutes
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Comment on a Reel
Source requirements: Press the opening button; Receive unconditional help after 2 minutes
Source timing: Unconditional delay: 2 minutes. The 48-hour validity appears only in copy.
Source outcome: The HAPPY10 coupon and a help message
Captured text (node-0, not approved campaign copy):
Hey! Tap below to get your coupon code for 10% off your first purchase of Happy Beans Vitamins 👇 
Current setup decision: adaptation_draft_requires_consent. The primary job can be prepared with the explicit reply/text substitutions below; this is not a full reproduction or a runtime test.
Primary Chatfuel result: Send the coupon, store URL and captured help copy together after confirmation.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Follower-only coupon: check and retry
waiting_for_chatfuel
Entry: Keyword comment
Outcome: A coupon only for a follower
Requirements: Check follower status; Offer another check after a negative result
Timing: No separate exact timer captured.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary result: A coupon only for a follower
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: post, keywords, coupon, destination
### Capability evidence
- comment: documented; tool_schema_and_playbook; setup_comment_replies, update_automation_setting; publicReply.publicReplyHowToReply, publicReply.exactTextReply, privateReply.privateReplyHowToReply, privateReply.exactTextReply. Scoped post/keyword comments with fixed public and private text; inline URLs can be text. setup_comment_replies enables rules, not drafts.
- follower: not_exposed; inference_from_tool_inputs; setup_comment_replies, update_automation_setting; . No Instagram follower condition or follow/check/retry gate in normal tool inputs.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- manychat-73: A follow request does not replace follower verification. Coupon redemption is not confirmed. [Described analogue inro-6028](../native-recipes/inro-6028.md)
### Finish the offer destination - manychat-73
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: manychat-73 - Grow followers from comments.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Follower-only coupon: check and retry
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Keyword comment
Source requirements: Check follower status; Offer another check after a negative result
Source timing: No exact timer captured.
Source outcome: A coupon only for a follower
Captured text (node-0, not approved campaign copy):
I can't wait to share this special code with you! 
Tap below to get it (but make sure you're following me first!) 💛
Current setup decision: waiting_for_chatfuel. The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary Chatfuel result: A coupon only for a follower
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```

## Welcome offer from a QR or referral link
waiting_for_chatfuel
Entry: Referral-link click or QR entry
Outcome: A welcome coupon
Requirements: Press the confirmation button
Timing: Opening button: 6 hours.
Consent: Consent to an external mailing list or service is not established by this capture.
Sending a link or collecting a contact does not confirm registration, subscription, payment or attendance in an external service.
The referral-link or QR entry is not configurable through ordinary MCP. A manually configured scope or an ordinary DM keyword is not a new-account setup for this scenario.
Primary result: A welcome coupon
Retained: 
Omitted: 
Limitations: 
Setup disabled. Source and older analogue links below are references only, not fallback setup instructions.
Missing source facts: None blocking this assessment.
Client inputs: 
### Capability evidence
- ref-link: dashboard_only; automation-settings_playbook; update_automation_setting; refLinks. Referral-link configuration is dashboard-only for normal MCP; ordinary DM loses the referral/QR entry.
- dm-ai: documented; tool_schema_and_playbook; update_automation_setting; incomingMessages, whenAIReplies. AI replies to incoming messages with instructions; not a deterministic imported graph or an exact-text guarantee for every AI response.
- buttons: not_exposed; inference_from_tool_inputs; update_automation_setting; publicReply, privateReply. Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: dashboard_only; automation-settings_playbook; update_automation_setting; messageDelays. messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: dashboard_only; playbook_and_tool_inputs; update_automation_setting; . Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.
### Sources and described analogues
A distinct variant because its entry, required conditions, timing or outcome differs.
- inro-6019: QR scanning and coupon redemption need separate confirmation. [Described analogue inro-6019](../native-recipes/inro-6019.md)
### Finish the offer destination - inro-6019
Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
```text
Help me prepare: Finish the offer destination.
Selected source: inro-6019 - Welcome new customers from a QR code.
Goal: Deliver a relevant product offer or coupon while interest is high.
Variant: Welcome offer from a QR or referral link
Scope: Optional destination setup. Skip this step when sharing an existing approved offer link without changing checkout or fulfillment.
Source entry: Referral-link click or QR entry
Source requirements: Press the confirmation button
Source timing: Opening button: 6 hours.
Source outcome: A welcome coupon
Captured text (n001, not approved campaign copy):
Welcome! Want 10% off? Tap below for your code.
Get my code
Current setup decision: waiting_for_chatfuel. The referral-link or QR entry is not configurable through ordinary MCP. A manually configured scope or an ordinary DM keyword is not a new-account setup for this scenario.
Primary Chatfuel result: A welcome coupon
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing store, course platform or checkout named by the owner.
Ask me for: Offer and destination URL; Price or coupon terms; Access or fulfillment rules; Existing authorized access.
1. Confirm the existing destination and approved offer. Draft the product, coupon or course-access configuration only where it is needed; merely sharing an existing link needs no new integration.
2. Check the page and define separate evidence for payment, coupon redemption and access delivery. Neither a DM link nor a source message promising expiry proves these outcomes. Keep unverified expiry or completion callbacks unresolved.
3. Return draft settings, authorization gaps and exact success checks. Do not publish an offer, create a purchase, charge money or grant access.
4. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
5. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
6. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
