# Comment enquiry triage

inro-comment-moderation | v1.0.0 | described, not accepted.

Read setup-policy.md and the selected setup-details/<variant>.md via setup-index.md before configuration. The historical native-policy modes below cannot bypass current variant gates. Recheck actual host tools/account before writes.

### inro-comment-moderation | Comment enquiry triage
Inputs: resolution_policy, issue_prompt.
Messages: public "I have sent you a private reply about your request." DM: "{issue_prompt}" After the actual reply, resolve from resolution_policy or hand off; never repeat private details publicly.
Native: C+D+H.
End/stop: Keyword-requested issue receives private resolution or team handoff; S.
Difference: Opt-in comment triage, not hiding or deleting comments. Comments remain visible. Do not promise automatic removal.

## Applicability
- People request help through an explicit keyword on selected posts and can discuss the issue privately.

## Prerequisites
- Approve the private issue question and resolution policy; have a team route for unresolved facts.

## Exclusions
- Do not choose when comments must be hidden/deleted or unwanted comments must be detected semantically. Comments remain visible.
- Do not configure when required lifecycle operations are unavailable on the actual host.

## Inputs
- `campaign` (text; required): Unique ASCII campaign name, at most 48 characters. Journal belongs to this conversation only.
- `language` (text; required): Language for the exact approved messages.
- `initial_text` (text; required): Exact approved first message; promised value must be in that message.
- `refusal_text` (text; required): Exact approved refusal reply. Ends this campaign before keyword matching.
- `handoff_text` (text; required): Exact approved team reply; native handoff needs separate readback.
- `post_ids` (ids; required): Actual owned Instagram posts; inspect overlap before preparation.
- `keyword` (text; required): Approved entry word; read actual host matching rules.
- `public_text` (text; required): Exact approved public copy, or nonempty inactive copy when public replies are disabled.
- `resolution_policy` (text; required): Approved facts and resolution boundaries. Unknown facts go to the team.
- `issue_prompt` (text; required): Exact approved private invitation to explain the issue.

## Available Templates And Instructions
### public (template; available_template)
I have sent you a private reply about your request.
### initial (template; available_template)
{issue_prompt}
### placement (template; not_required)
No outgoing message supplied.
### continuation (instruction; instruction_not_sent_text)
public "I have sent you a private reply about your request." DM: "{issue_prompt}" After the actual reply, resolve from resolution_policy or hand off; never repeat private details publicly.
### refusal (template; available_template)
Understood. I will not continue this campaign.
### handoff (template; available_template)
Our team will handle your request.

## Intended Branches
Derived from native instructions, not captured competitor graph or imported deterministic Flow.
### entry
Actual matching keyword comment on the selected post.
- If New matching source event; current account, permission and delivery window verified. -> first
### first
Send the exact approved first message. Deliver any promised value now.
- If Actual contact reply within the current window. No silent continuation. -> reply
- If Actual refusal. -> refusal
- If No inbound reply, or only an external click. -> silence
- If Same-run repeated word. -> repeat
- If Person request, unknown facts or unresolved issue; never silently invent an answer. -> handoff
### end
Stated outcome only. No inferred booking, registration, purchase, verified follow or verified share.
### reply
public "I have sent you a private reply about your request." DM: "{issue_prompt}" After the actual reply, resolve from resolution_policy or hand off; never repeat private details publicly.
- If Approved factual resolution or appropriate contextual thanks. -> end
- If Actual refusal. -> refusal
- If Person request, unknown facts or unresolved issue; never silently invent an answer. -> handoff
### refusal
End this campaign on refusal. Do not restart from a keyword in the refusal.
- If Refusal completed. No permanent cross-source suppression claimed. -> end
### silence
Send nothing for silence or external clicks; enforce current delivery windows.
### repeat
Same-run repeat does not restart intake, resend a bonus or duplicate capture. Ambiguous late replies need clarification.
### handoff
Use native team handoff on person request, unresolved facts or approved handoff criteria. Text alone is not handoff proof.
- If Actual native team control readback. -> end

## Settings And Operations
- Read actual host tools and get_playbook for this recipe.
- Create/bind only an approved owned OFF rule. Normal setup_comment_replies is not draft preparation.
- Read/stage general InstagramDirectMessages only under explicit OFF/ON shared-state branches.
- Apply native policy mode C; inspect actual inputs before writes.
- Apply native policy mode D; inspect actual inputs before writes.
- Apply native policy mode H; inspect actual inputs before writes.
- Read back each exact setting and inheritance before continuing.
Required OFF creation, exact inheritance restoration or continuing comment preview may be unavailable. Stop before writes; a documented GraphQL alternative is not an available normal tool.

## Legacy Reconciliation
Keep the older literal-source contract and its unavailable/unverified status unchanged. This described outcome replaces its mechanism and does not inherit its evidence.
Original goal: Hide unwanted comments automatically.
Legacy status: unavailable. Legacy digest: dbcee8552b24c198a1ec9e79b1df509263eb11c67d9947db6998dd8a86fee6cf.
Legacy lists are audit evidence, not additional requirements for this analogue.

## Lifecycle
Use this conversation journal and fresh native readback. No cross-chat state or user settings transfer. If the journal is missing, read-only reconciliation only.
Apply S from native-policy.md: safe owned disable; exact campaign additions only; preserve concurrent changes and inheritance. Restore dormant Send only after original OFF DM is OFF. Read back every stop; live silence is separate.
Fresh source and consent, same verified ownership. Waitlist membership stays joined/withdrawn; no old consent reuse.
- Required check: content
- Required check: return
- Required check: stop
- Required check: refusal
- Required check: repeat
- Required check: unknown_action
- Required check: wrong_account
- Required check: two_campaigns
- Required check: source_attribution
- Required check: unavailable_removal_declined
- Required check: normal_host_capabilities
- Required check: fresh_account_state
- Required check: exact_restoration
- Required check: live_suppression

## Evidence
- source_capture: {"observed_at": "2026-10-30", "status": "captured_research_not_runtime"}
- canonical_version: {"status": "described_not_runtime_tested"}
- capability: {"observed_at": "2026-11-01", "status": "dated_document_and_tool_observation_not_account_check"}
- preview: {"status": "not_tested_for_canonical_version", "note": "Older previews do not establish unchanged behavior after prompt changes."}
- live: {"status": "historical_partial_not_accepted", "observed_at": "2026-10-31", "note": "Earlier core delivery/handoff reported separately; full lifecycle and exact current recipe revision not accepted.", "reference": "inro-business-analogues-live.json; checked_at=2026-10-31T06:52:44Z"}
- acceptance: {"status": "not_accepted", "registry": "catalog.json", "note": "Zero versions qualify. Local checks, previews and partial live paths are not acceptance."}

## Selected Native Setting Instructions
### Mode C
Owned OFF `InstagramPostComments` custom. Set `listOfPosts.update.postIDs`; `keywords.update` to `CommentThatExactlyMatches` and the approved word; `publicReply.update` to `ExactText`, approved `public_text`, nonempty `messagePrompt`, `likeContactComment:false`; `privateReply.update` to `ExactText`, approved `initial_text`, nonempty `messagePrompt`. First DM includes any promised value. No second message until a real inbound reply.
### Mode D
General `InstagramDirectMessages` base, not an invented DM custom. Append one marked block to existing `incomingMessages.messagePrompt`; use `howToReply:UsingAI`. The block starts only on the exact DM word or a verified linked comment reply. Exception 6085 answers ordinary inbound support without a word. Preserve ordinary support outside the campaign. Clarify ambiguous late YES before routing.
### Mode H
`switchToHuman.update` uses `howToSwitch:SwitchToTeammates` and campaign-owned rules with `switchingConditions` and approved `messagePrompt`. With original `DontSwitch`, save dormant rules only in the journal; stage owned rules only. Never merge dormant rules into an activated list. Use assignee userIDs only if requested and read; otherwise use the existing team route. Handoff on person request or unresolved facts. Q+handoff also hands off after both new answers. Q+booking_link must not hand off on qualification alone. Unknown price/availability/refund facts require native handoff, not an empty answer plus a link.

## Related Sources
These are mappings or losses, not runtime equivalence.
- inro-comment-moderation (business_replacement): Original: Comment moderation. Business analogue: Comment enquiry triage.
  - Opt-in comment triage, not hiding or deleting comments. Comments remain visible. Do not promise automatic removal.
