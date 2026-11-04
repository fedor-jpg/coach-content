# Coach Content: 30 Native Funnel Analogues

## Start Here

Historical reference. setup-policy.md and selected setup-details/<variant>.md take precedence for normal MCP. GraphQL procedures below are not normal tools. Main ON is unnecessary for drafts; OFF staging needs an approved existing OFF rule.

Use existing Chatfuel MCP; no new connector, runtime or settings transfer.

Draft in the coach's language. Show exact messages, destination, scope and next step before approval. Use existing material; no video required. Comment -> material -> two answers -> team selects 6025. Accept localized affirmative consent.

These are 30 predefined business analogues, not exact copies or 30 field-accepted recipes. Select the result; do not ask the coach to design a workaround. Comment-moderation resolves enquiries; 6111 resolves complaints privately; 6086 rewards self-reported sharing. Accept each against its stated outcome, not unavailable mechanics. Show the actual journey before approval. Never claim removal, verified sharing or completed booking from link delivery. Explicit removal/detection requests require scope clarification. Separate literal-source evidence, analogue previews and current live results.

### Coach-Facing Reply

Use 5-7 short lines and one approval question. Keep technical details in the journal unless asked. Example:

> Result: Comment -> worksheet -> two answers -> coach.
> First DM: "Here is your worksheet: [verified link]. Would you like to answer two questions?"
> Questions: "[complete question one]", then "[complete question two]", each after the actual reply.
> Scope: Prepare the owned test rule and DM continuation OFF. No new rules, sends or notifications.
> Approve preparation only?

Preparation never authorizes enable, sends or conversation control. A read-only request permits a proposal, not writes.

## Native Readiness

1. Read actual tools and the relevant `get_playbook` first. Choose the documented tools for the selected recipe before writes, not a universal tool-name requirement. Existing explicit settings can use `update_automation_setting`; switches use `set_automation_enabled`. Read their actual inputs. The GraphQL path below uses `get_type`, `execute_query` and `execute_mutation`, with `get_operation` when exposed. Verify required OFF creation, exact value/inheritance restoration and record pagination. If a required action is absent, stop before writes; do not add a connector or invent an operation.
2. Read the connected Instagram identity, bot, plan/credits, posts, complete automation list and effective settings with inheritance. A bot name is not proof of account connection. Resolve actual IDs; never execute placeholders. Read Main, the general DM base and each relevant comment rule. Inspect overlapping posts/keywords and existing campaign blocks before proposing writes.
3. Main must already be ON. Every AI continuation scope must have effective `whenAIReplies.option: Always`. Do not change Main, schedules, other channels or timezone. A restricted schedule requires separate readiness resolution, not a silent edit. An ON general DM base with active shared follow-ups requires explicit conflict resolution before this flow.
4. For a returning test contact, read control state. Open/waiting-for-human is not an AI failure. Never silently use `return_chat_to_ai`; get native approval for that conversation. Complete approvals and verify AI control before inviting a fresh test entry. Return can send a greeting; do not count it as campaign delivery. If real DM fails but explicit preview works, inspect source/ref and the matching comment custom. An owned comment continuation may still handle the contact; do not infer DM-only readiness. Never change system source/ref or activate foreign rules to force a pass. Do not add this ceremony for every new lead.
5. Only for a recipe with capture (E/T/W), read all native capture names, including dormant lists, and page `Bot.botAttributes` across all platforms and system/custom attributes without name filters. Collect `edges.node.botAttribute.name` until `pageInfo.hasNextPage` is false, following `endCursor`. Missing pages are not an empty namespace. Do not collect contact values for this inventory. Qualification without capture needs no global attribute inventory.
6. Before enable, open the destination and verify recipient access, not just owner access. An address in configuration is not proof of availability. For Drive, verify file and sharing; never change sharing silently. If access is unverified, keep delivery OFF. Never invent hosting or ask the coach to transport settings.

## Save Before Writing

Keep a campaign journal in this same conversation before mutations, with native readback and approvals. Use a host-supported conversation-bound artifact; verify journal and original results remain accessible; do not invent hidden storage. The coach sees a compact summary, not a dump of technical IDs, and never transports files manually. Save `campaign` (unique ASCII slug, at most 48 characters), recipe, account/bot IDs, posts/word, approved inputs/messages, owned rule ID, original switches/settings, inheritance parents, exact additions, expected readback and pending/completed operations. Save full dormant lists. For waitlists retain the original complete namespace and exact owned capture proof before removal.

Name an owned custom `Coach {campaign}` and mark its prompt and the shared DM block with `[coach-funnel:{campaign}]` and `[/coach-funnel:{campaign}]`. Names/markers help discovery but never prove ownership alone. Save the actual created ID and OFF readback before updates. An existing rule is owned only if the saved journal and current account, ID, scope and contents agree.

Explicit adoption is the only exception to requiring an older journal: the user must specifically authorize the exact existing rule ID for this campaign/test. Read its actual connected account, ID, scope, OFF switch and full settings/inheritance; record them as the restoration baseline BEFORE writes. Record adoption and its authorization in the new journal. Never infer adoption from a name, keyword or another campaign's marker. Adoption does not authorize enable, sends, conversation control or other rules. If the user prohibits new rules, use only that authorized existing OFF rule; otherwise the normal path is create-OFF after approval. Never create a replacement to evade a no-new-rules constraint.

Return means this conversation plus current native readback. Do not promise cross-account recovery, private storage or another chat's access. If the journal is unavailable, offer read-only reconciliation; never invent original values or create a duplicate. Native markers alone cannot reconstruct overwritten inheritance. No notifications, background jobs or automatic follow-ups.

## Native Operations

Read the actual types before using these checked mutation shapes. Send variables through the tool's documented interface; one setting per update. `validateOnly` is not backend execution or readback proof.

```graphql
mutation($botID: BotID!, $scope: FuelyAutomationScope!, $name: String!) {
  fuelyAutomationCreate(botID: $botID, scope: $scope, name: $name) { id enabled }
}
mutation($botID: BotID!, $id: FuelyAutomationID!, $update: FuelySettingUpdateInput!) {
  fuelyAutomationUpdateSetting(botID: $botID, id: $id, update: $update) { id enabled }
}
mutation($botID: BotID!, $id: FuelyAutomationID!, $enabled: Boolean!) {
  fuelyAutomationSetEnabled(botID: $botID, id: $id, enabled: $enabled) { id enabled }
}
```

High-level `update_automation_setting` takes one setting without GraphQL `update` wrappers; captures use `attribute`, not GraphQL `name`. It cannot restore inheritance. `setup_comment_replies` activates immediately and changes shared switches; it is not OFF preparation. `test_reply` tests one message, not a continuing thread. Never substitute these for missing lifecycle actions or switch executors after rejection.

Recipe modes:

- **C**: Owned OFF `InstagramPostComments` custom. Set `listOfPosts.update.postIDs`; `keywords.update` to `CommentThatExactlyMatches` and the approved word; `publicReply.update` to `ExactText`, approved `public_text`, nonempty `messagePrompt`, `likeContactComment:false`; `privateReply.update` to `ExactText`, approved `initial_text`, nonempty `messagePrompt`. First DM includes any promised value. No second message until a real inbound reply.
- **N**: Like C, but `publicReplyHowToReply:DontReply`, nonempty inactive text and no likes. Select `CommentThatContains` with the coach's explicit feedback terms. No semantic hate detection is promised. The first private message invites resolution; do not quote abusive content.
- **P**: Like C, but `privateReplyHowToReply:DontReply` and nonempty inactive text. Public-only thanks. No DM continuation or shared DM change.
- **D**: General `InstagramDirectMessages` base, not an invented DM custom. Append one marked block to existing `incomingMessages.messagePrompt`; use `howToReply:UsingAI`. The block starts only on the exact DM word or a verified linked comment reply. Exception 6085 answers ordinary inbound support without a word. Preserve ordinary support outside the campaign. Clarify ambiguous late YES before routing.
- **Q**: In the incoming prompt, require new affirmative consent after this run's first message. Ask exactly `question_one`, then wait for its actual answer; ask exactly `question_two`, then wait for a distinct actual answer. Entry word and consent are not answers. Apply `qualification_policy`. `next_step=handoff` needs no calendar URL; `next_step=booking_link` needs the existing `booking_url`. Do not add a third intake question.
- **H**: `switchToHuman.update` uses `howToSwitch:SwitchToTeammates` and campaign-owned rules with `switchingConditions` and approved `messagePrompt`. With original `DontSwitch`, save dormant rules only in the journal; stage owned rules only. Never merge dormant rules into an activated list. Use assignee userIDs only if requested and read; otherwise use the existing team route. Handoff on person request or unresolved facts. Q+handoff also hands off after both new answers. Q+booking_link must not hand off on qualification alone. Unknown price/availability/refund facts require native handoff, not an empty answer plus a link.
- **E/T**: `collectContactInfo.update` uses `howToCollect:CollectInfo` and `captures:[{name,description}]` for optional email/phone. Use a unique campaign-specific name. Keep descriptions short: "Campaign {campaign}: after new explicit consent, save optional email for the stated purpose. Never reuse old data." Substitute phone for T. Full purpose belongs in the incoming prompt. Read actual `validationErrors` and saved attributes. Save details for the team; never promise email delivery, calls or mailing-list subscription.
- **W**: Same capture operation, with the supplied unique `membership_attribute`. Description: "Campaign {campaign} only. Fresh source and explicit new YES: joined. STOP: withdrawn before handoff. Otherwise preserve state, including unset. Never reuse old consent or answers." This stays at most 217 ASCII characters, an internal choice, not a provider limit. Put full launch name, purpose and consent in the incoming prompt. Persist actual `joined`/`withdrawn`; bot prose is not proof. STOP must write withdrawal before any handoff. Never change another launch or reenroll from old YES.

For new C/N continuation, configure the owned custom. D fallback is a separate path: configure it only if required, approved and verified. For an existing matching custom with working scoped handoff, reuse its settings; do not rewrite shared handoff merely to test activation. Verify live routing before claiming general-DM fallback works. Never retry a blocked write through another tool or obscured payload. For C without continuation or P, use owned `incomingMessages.howToReply:DontReply`; leave general DM unchanged. Owned follow-ups use `DontSend`. Preserve active foreign handoff/capture records. Save inactive inherited lists exactly; never wake foreign dormant records. Update wrappers are `{"incomingMessages":{"update":{"howToReply":"UsingAI","messagePrompt":"APPROVED PROMPT"}}}`. Restore inheritance with `{"settingName":{"setInheritFrom":"ACTUAL_PARENT_ID"}}` only with saved proof.

For ANY D recipe, including C+D 6025 and D-only 6021, save the original general DM `followUps` mode, text, exact inheritance and parent readback before writes. If the base is originally OFF with dormant `Send`, stage `{"followUps":{"update":{"howToSend":"DontSend","messagePrompt":"No follow-ups for silence or clicks."}}}` on that base while OFF. Read back explicit `DontSend` with inheritance removed and the base still OFF BEFORE enable. An already effective `DontSend` needs readback too. Disabling follow-ups on the owned custom alone is insufficient. An originally ON base with `Send` remains a shared conflict requiring separate approval; never silently disable it.

Build the incoming prompt from current-run source, campaign identity, approved facts, first message, continuation and refusal/handoff messages. Verify the saved prompt contains the approved bonus, consent and exact refusal_text; cover refusal before keyword matching. Never import unrelated KB context, including in refusal replies. Never reuse old answers, consent or contact fields. Same-run repeats must not restart intake or duplicate capture. Refusal ends this campaign. No permanent cross-source suppression is promised. Keep native text within observed constraints; never truncate approved facts.

## Approve, Configure, Test

1. Show the account, selected posts/word, complete first messages, exact staged writes, shared effects and stop steps. Obtain native tool approval. A batch approval is valid only for those exact actions; obey further tool yes/no prompts. Never treat setup approval as enable, send or conversation-control approval.
2. Create or bind only the owned OFF custom. Avoid `setup_comment_replies`: it can activate a rule and change the base immediately. If general DM was OFF, stage its complete settings while OFF. If general DM was ON, leave it unchanged during custom preparation; its writes need a separate live-shared-change approval. DM-only recipes use this same OFF/ON branch.
3. Save intent, execute one setting, read it back, then continue. Capture configuration may register a global attribute before any user message. Allow that name only with original absence and exact unchanged owned capture proof; any foreign dormant capture still collides. A failed/unknown create or write requires reconciliation, not a blind retry. Stop partial configuration using saved originals.
4. Verify full expected settings, inheritance resolution, capture validation, switches and absence of unrelated side effects. Apply approved ON-DM shared changes only now, with each readback. Then request separate enable approval for general DM if originally OFF and the owned custom. Never enable Main, comment base or another channel. A human-controlled test chat remains human-controlled unless separately approved.
5. For approved OFF previews, read current mutation/input definitions. Start `previewResponsesStartForFuelyAutomation(botID, fuelyAutomationID)` and use its returned `conversationID`, NOT session `id`. Send the comment with `previewResponsesInstagramPostCommentSend(botID, conversationID, comment: {text, postCaption})`; both text fields are required. Send subsequent replies with `previewResponsesInstagramTextSend(botID, conversationID, message: {text})`. Both input objects allow optional `clientId`; use only its documented type. Read actual preview conversation messages after EVERY send, plus relevant attributes/handoff, using the returned conversationID. Do not infer absent comment simulation from `test_reply`: it is a DM shortcut, not comment-dispatch proof. Preview checks do not prove Instagram post/keyword routing, actual delivery or delivery-window behavior; a real path is still required. Real triggers/sends need exact test-recipient/text approval, never unsolicited customer tests. Check current windows from the playbook and last inbound event; clicks/outbound activity do not reopen them.
6. Test delivery, silence, both new qualification answers, ambiguous answers, repeats, refusal, expired window, return and stop as relevant. Preserve unrelated support and campaigns. Record behavior and revision, not `error=null` as success. Old previews support unchanged behavior only; changed prompts need affected checks. An absent asynchronous reply/handoff is pending: re-read within 60 seconds. On timeout, stop and restore; never leave a failed test ON. Do not relabel old evidence or rerun unchanged checks.
7. After testing, stop the campaign and read back OFF for every originally OFF test scope. Preserve pre-existing ON scopes. Report `settings stopped`, restoration completeness and any unverified live silence separately. Never claim all thirty field-accepted from this guide or a successful preview.

## S: Stop, Return And Leads

Every recipe below uses S. Restore the saved journal and fresh complete native state. Disable the owned custom first. Remove only the exact single marked DM block and exact campaign handoff/capture additions. Preserve concurrent text and active foreign records. Modified or duplicate additions are ambiguous: perform safe owned disable, then report the unresolved removal instead of overwriting it.

Restore original values/inheritance only when current affected values equal the prepared values and saved inheritance parents are unchanged. Otherwise keep safe explicit settings and report deferred restoration. An originally ON DM base stays ON. Disable an originally OFF DM base only when unchanged shared state proves that doing so cannot disable concurrent work; otherwise leave it ON, remove only campaign additions and report that deferred switch. Never restore dormant follow-ups into active shared behavior. Read back every stop write. Repeated stop must produce no duplicate operations. Stop removes settings, not sent messages or stored contact data. New comments and late replies after stop need an actual live suppression check; settings restoration alone does not prove silence.

Restore original dormant `Send` and its exact inheritance only AFTER the general DM base is read back OFF, and only with unchanged-value/parent proof. If concurrent work requires the base to remain ON, retain `DontSend`; never restore `Send`. Report deferred follow-up restoration without blocking safe campaign removal. This ordering also applies to D-only recipes with no custom to disable.

Waitlist restart keeps the same campaign, purpose and attribute. Require saved original absence, exact owned capture proof observed before its removal, saved stop/readback and fresh affected-state equality. Keep joined/withdrawn values whether an empty attribute definition remains or disappears. Re-read complete namespace and reject foreign captures. A late return may refresh stopped-state verification after unrelated edits, but cannot replace historical ownership with a new zero-command stop or altered receipt. Stage OFF again, obtain approvals again, require fresh source/consent again. No re-enrollment by restart.

For leads, read only this campaign's verified recipient chains. Page conversation history completely for the requested period. Match comment ID/media/linked private reply or actual inbound campaign word, then actual answers and handoff for the same recipient. 6085 uses the actual inbound support event. `get_chat`'s last messages alone do not prove full history; use current query pagination. Keep ambiguous attribution separate; do not call it zero leads. Show actual results when asked, never notifications. Use chat links only when returned by the current tools.

## Recipes

Common inputs: `campaign`, `language`, approved `initial_text` for private replies; D needs `refusal_text`, H needs `handoff_text`. C/N/P need actual `post_ids`, `keyword`, `public_text` (inactive for N). D needs `keyword` except 6085. The coach approves final copy. Defaults: public "Check DMs and message requests."; D refusal "Understood. I will not continue this campaign."; H handoff "Our team will handle your request." Without D, keep DontReply: no refusal, clarification or continuation. Link-only recipes need no consent question or capture. Native letters and S refer to the procedures above.

### inro-4393 | Product-code enquiry from a Live invitation
Inputs: product_code, product_name, availability, offer_terms, product_url.
Messages: Live CTA gives the exact DM keyword/product code. DM: "{product_name}: {availability}. {offer_terms}. {product_url}" Clarify wrong codes; missing price or facts trigger native handoff.
Native: D+H.
End/stop: Matching offer or actual team handoff; S.
Difference: No Live-comment automation, purchase confirmation or invented price.

### inro-4484 | Live invitation and preference routing
Inputs: preference_question, option_one, option_one_url, option_two, option_two_url.
Messages: Live CTA: "DM {keyword}." DM: "{preference_question}" After an actual answer give its matching URL; clarify an unknown choice.
Native: D+H.
End/stop: Correct choice-specific destination; S.
Difference: Ordinary DM, not a Live-comment trigger. Coach places the invitation.

### inro-4530 | DM quiz with the same bonus
Inputs: quiz_question, quiz_answer, bonus_text.
Messages: Live CTA: "DM {keyword} for the quiz." DM: "{quiz_question}" After either answer explain quiz_answer and give the exact bonus_text, including after a wrong answer.
Native: D+H.
End/stop: Actual answer, approved explanation and identical bonus; S.
Difference: No Live-comment trigger, random prize or winner selection.

### inro-6018 | Giveaway enquiry for team review
Inputs: giveaway_name, entry_terms, contact_purpose.
Messages: "Rules for {giveaway_name}: {entry_terms}. Reply ENTER to submit an enquiry." After ENTER offer optional email for the stated purpose.
Native: C+D+E+H.
End/stop: Actual enquiry and optional contact for review; S.
Difference: No follow/tag verification, certified entry, random draw or winner claim.

### inro-6019 | Profile or QR invitation with a coupon
Inputs: profile_url, coupon_code, coupon_terms.
Messages: Placement: "Open this Instagram profile and DM {keyword}." DM: "Your code is {coupon_code}. {coupon_terms}"
Native: D+H.
End/stop: Inbound word receives the exact code; S.
Difference: Native entry is the DM word, not a QR scan. Verify profile_url belongs to the connected account. Use an existing QR or the host's available QR/file tool with a proven encoder; decode it to that exact URL before delivering a printable file. Do not generate QR modules as an illustration. Without a verified image tool, deliver the profile invitation and state that a printable QR is not supplied. No scan attribution or redemption claim.

### inro-6021 | Two-question DM qualification
Inputs: question_one, question_two, qualification_policy, next_step; booking_url only for booking_link.
Messages: "Would you like to answer two questions about your situation?" Ask Q only after new consent.
Native: D+Q+H.
End/stop: Actual answers and the agreed next step; S. No fabricated booking.

### inro-6022 | Resource and optional email
Inputs: resource_title, resource_url, contact_purpose.
Messages: "Here is {resource_title}: {resource_url}. Reply MORE to continue." After MORE, explain purpose and offer optional email capture.
Native: C+D+E+H.
End/stop: Delivered resource plus consented saved email, or refusal without withholding; S. Capture is not an external list subscription.

### inro-6023 | Story invitation to a resource DM
Inputs: resource_title, resource_url.
Messages: Story CTA: "DM {keyword} for {resource_title}." DM: "Here is {resource_title}: {resource_url}."
Native: D+H.
End/stop: Actual inbound word receives the matching link; S.
Difference: Coach places CTA in the existing Story; no automatic Story-reply filter or click claim.

### inro-6024 | Equal-access freebie and email
Inputs: resource_title, resource_url, contact_purpose.
Messages: "Here is {resource_title}: {resource_url}. Reply MORE to discuss it." Offer optional email after MORE.
Native: C+D+E+H.
End/stop: Same freebie for followers/non-followers; actual optional email; S.
Difference: No follower gate or asymmetric reward.

### inro-6025 | Material, two answers, team next step
Inputs: question_one, question_two, qualification_policy, next_step; resource_title/resource_url together if material; booking_url only for booking_link.
Messages: "Here is {resource_title}: {resource_url}. Would you like to answer two questions for the coach?" Omit the material sentence when absent. After new localized affirmative consent, ask the two approved questions separately.
Native: C+D+Q+H.
End/stop: Both actual answers and confirmed team handoff or approved booking destination; S. A link is not a booked call.

### inro-6026 | Voluntary email after delivery
Inputs: resource_title, resource_url, contact_purpose.
Messages: "Here is {resource_title}: {resource_url}. Reply EMAIL to leave an address." After EMAIL explain purpose, then request the address.
Native: C+D+E+H.
End/stop: Saved valid voluntary email or retained access after refusal; S.
Difference: No email paywall or automatic mailing subscription.

### inro-6027 | Voluntary phone for the team
Inputs: resource_title, resource_url, contact_purpose.
Messages: "Here is {resource_title}: {resource_url}. Reply PHONE if you want our team to have your number." Explain purpose before collecting it.
Native: C+D+T+H.
End/stop: Actual consented phone attribute or refusal; S.
Difference: No phone gate, automatic call or promised call completion.

### inro-6028 | Freebie with optional follow invitation
Inputs: resource_title, resource_url, profile_url.
Messages: "Here is {resource_title}: {resource_url}. You can also follow {profile_url} if useful."
Native: C.
End/stop: Non-follower receives the material; S.
Difference: Voluntary follow request, not follower verification or gating.

### inro-6045 | YouTube video delivery
Inputs: video_title, video_url.
Messages: "Watch {video_title} here: {video_url}."
Native: C.
End/stop: Correct video delivered and opened by recipient; S. No verified watch or subscription claim.

### inro-6046 | TikTok destination from Instagram
Inputs: tiktok_title, tiktok_url.
Messages: "Here is {tiktok_title}: {tiktok_url}."
Native: C.
End/stop: Correct TikTok destination delivered in Instagram; S. No TikTok automation or follow claim.

### inro-6047 | Podcast episode delivery
Inputs: episode_title, episode_url.
Messages: "Listen to {episode_title} here: {episode_url}."
Native: C.
End/stop: Correct episode opens; S. Silence and clicks cause no second DM.

### inro-6049 | Webinar interest and registration link
Inputs: event_name, event_date, question_one, question_two, registration_url.
Messages: "Interested in {event_name} on {event_date}? Reply YES for details." Ask both questions one at a time after YES and actual answers, then share registration_url.
Native: C+D+H.
End/stop: Actual answers and current registration destination; S.
Difference: Conversation and link, not completed web-form registration.

### inro-6051 | Existing community invitation
Inputs: community_name, community_url.
Messages: "You can join {community_name} here: {community_url}."
Native: C.
End/stop: Correct invitation opens; S.
Difference: No follower gate or verified community membership.

### inro-6053 | Disclosed affiliate recommendation
Inputs: recommendation, affiliate_disclosure, affiliate_url.
Messages: "{recommendation}. {affiliate_disclosure}. {affiliate_url}"
Native: C.
End/stop: Correct disclosed recommendation delivered; S. No invented benefit, purchase or commission.

### inro-6054 | Event link and optional email
Inputs: event_name, event_date, registration_url, contact_purpose.
Messages: "Register for {event_name} on {event_date}: {registration_url}. Reply MORE for a question." Offer optional email after MORE and purpose disclosure.
Native: C+D+E+H.
End/stop: Registration link delivered and optional actual email; S. Neither proves registration.

### inro-6080 | Course enquiry and offer
Inputs: course_name, offer_terms, course_url.
Messages: "Here is {course_name}: {offer_terms}. Reply COURSE to ask a question." After COURSE answer approved facts and provide course_url; unknown facts go to the team.
Native: C+D+H.
End/stop: Correct course offer/destination or confirmed handoff; S. No payment or access claim.

### inro-6081 | Named-launch waitlist with withdrawal
Inputs: launch_name, launch_purpose, consent_text containing YES and STOP, membership_attribute.
Messages: "Join the waitlist for {launch_name}, for {launch_purpose}? {consent_text}" Persist joined after this run's YES; STOP persists withdrawn before any handoff. Before YES keep unset; on restart preserve existing state.
Native: C+D+W+H.
End/stop: Actual attribute readback joined/withdrawn, isolated to this launch; S retains membership. No automatic mailings or external list claim.

### inro-6082 | Public thanks only
Inputs: thanks_text.
Messages: public_text equals thanks_text. No private message.
Native: P.
End/stop: Matching positive keyword receives approved public thanks only; S. No semantic sentiment promise.

### inro-6085 | Grounded support with team backup
Inputs: known_facts, handoff_conditions. No keyword.
Messages: Answer the actual question from known_facts; ask one clarification if needed. Unknown facts or a person request use handoff_text, without repeating a greeting.
Native: D+H.
End/stop: Grounded answer or native team handoff; S preserves unrelated support.

### inro-6086 | Share-report gratitude and bonus
Inputs: thanks_text, bonus_text.
Messages: Coach's Story CTA: "Share this in your Story, tag me, then DM {keyword} for the bonus." Default keyword is SHARED, localized to the coach's language. DM: "{thanks_text} {bonus_text}" Give the bonus once after the actual inbound word. Do not say you saw a mention or verified a share. Unknown questions use the team route; refusal ends this campaign.
Native: D+H.
End/stop: Actual campaign-word DM receives gratitude and the approved bonus once; the coach can retrieve people who reported sharing through campaign history; S. Report these as self-reported shares, never verified mentions.
Difference: Explicit keyword acknowledgement, not automatic Story-mention detection, reaction or verified sharing.

### inro-6111 | Private resolution for flagged feedback
Inputs: feedback_terms, resolution_policy, issue_prompt. Use feedback_terms for N's approved contains-list.
Messages: No public response or like. DM: "{issue_prompt}" After an actual reply, answer from resolution_policy or use team handoff. No argument, abuse quotation or repeated outreach.
Native: N+D+H.
End/stop: Flagged feedback receives a private invitation and, after reply, resolution/handoff; S.
Difference: No-amplification response and triage, not hate removal or semantic hate detection. Comments remain visible.

### inro-6220 | Requested resource from a comment
Inputs: resource_title, resource_url.
Messages: "Here is {resource_title}: {resource_url}."
Native: C.
End/stop: Recipient receives and can open the actual destination; S. No click tracking or follow-up.

### inro-6222 | Ad-invited DM qualification
Inputs: question_one, question_two, qualification_policy, next_step; booking_url only for booking_link.
Messages: Existing ad CTA: "DM {keyword}." DM: "Would you like to answer two questions about your situation?" Then Q.
Native: D+Q+H.
End/stop: Actual answers and link or handoff; S.
Difference: Coach changes the existing CTA; no ad-click trigger, ad attribution or confirmed booking.

### inro-6223 | Contextual DM thanks
Inputs: thanks_text, acknowledgment_policy.
Messages: "{thanks_text}" once for genuine kind feedback after the campaign word. Use acknowledgment_policy; treat complaints as complaints and clarify sarcasm.
Native: D+H.
End/stop: One appropriate text thank-you or team resolution; S. No reaction operation is required.

### inro-comment-moderation | Comment enquiry triage
Inputs: resolution_policy, issue_prompt.
Messages: public "I have sent you a private reply about your request." DM: "{issue_prompt}" After the actual reply, resolve from resolution_policy or hand off; never repeat private details publicly.
Native: C+D+H.
End/stop: Keyword-requested issue receives private resolution or team handoff; S.
Difference: Opt-in comment triage, not hiding or deleting comments. Comments remain visible. Do not promise automatic removal.
