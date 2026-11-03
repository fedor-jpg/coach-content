# Grow your community: follow-gated invitation

Setup 1.1.0 | community-inro-6051 | waiting_for_chatfuel | runtime not tested

## Business Result
Invite interested people into your next launch or a shared community.
Creators launching an offer or welcoming members.
Source entry: Community comment or DM
Source outcome: An invitation to an external community
Source requirements: Press the opening button; Verify a follow before the invitation
Source timing: Link click: 3 days; follow and opening button: 2 days.

## Functional Availability
waiting_for_chatfuel
The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary result: An invitation to an external community
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- follower: No Instagram follower condition or follow/check/retry gate in normal tool inputs.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6051: Grow Your Community
Full captured settings/provenance: [selected source JSON](../source-records/inro-6051.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: comment, dm-ai
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
All posts
FILTER THE COMMENTS
Comments with keyword(s)
Community
When
Someone sends you a DM
FILTER MESSAGES
Contains keyword(s)
Community
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Hey {{contact.name}} ❤️ Do you want to join my community?
Yesss 👀
```
Captured buttons: ["Yesss 👀"]
- Edge e001: n001 -> n002 | condition/label: ""
- Edge e013: n001 -> n014 | condition/label: ""
#### n002 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Yesss 👀
```
- Edge e002: n002 -> n003 | condition/label: "WHEN BUTTON IS CLICKED\nYesss 👀"
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Community leads
```
- Edge e003: n003 -> n004 | condition/label: ""
#### n004 (ask_for_follow)
A follow request is not a verified follow gate. Keep true delivery/false retry in the original only.
Business input: whether unconditional delivery is acceptable
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, follower
Captured text (not approved outbound copy):
```text
First, make sure to follow my page to be on top of all new trends and tips 💫
I have followed you
```
Captured buttons: ["I have followed you"]
- Edge e004: n004 -> n005 | condition/label: ""
- Edge e011: n004 -> n012 | condition/label: ""
#### n005 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN CONTACT CLICKS AND FOLLOWS YOU
```
- Edge e005: n005 -> n006 | condition/label: "WHEN CONTACT CLICKS AND FOLLOWS YOU"
#### n006 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
thanks for your follow❤️  
```
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Here's the access to my community
Join creators, automation experts and more!
Join now 🤝
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBei9BUEE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--98318ba47c94561b7eef793d7a5221729dde6f78/Join%20Now.png"]
- Edge e007: n007 -> n008 | condition/label: ""
- Edge e009: n007 -> n010 | condition/label: ""
#### n008 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- Edge e008: n008 -> n009 | condition/label: "WHEN LINK IS CLICKED"
#### n009 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Community joiner
```
- No captured outgoing edge; do not infer completion.
#### n010 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 days
```
- Edge e010: n010 -> n011 | condition/label: "IF LINK HASN'T BEEN CLICKED AFTER\n3 days"
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Have you received the link?
```
- No captured outgoing edge; do not infer completion.
#### n012 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T CLICKED AND FOLLOWED YOU AFTER
2 days
```
- Edge e012: n012 -> n013 | condition/label: "IF CONTACT HASN'T CLICKED AND FOLLOWED YOU AFTER\n2 days"
#### n013 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Make sure to follow me if you want access to exclusive perks and a community of like-minded individuals 🔥
```
- No captured outgoing edge; do not infer completion.
#### n014 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
2 days
```
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## External Continuation: inro-6051 / Finish community access
Optional destination setup. The Chatfuel variant delivers an invitation, not verified membership.
```text
Help me prepare: Finish community access.
Selected source: inro-6051 - Grow Your Community.
Goal: Invite interested people into your next launch or a shared community.
Variant: Grow your community: follow-gated invitation
Scope: Optional destination setup. The Chatfuel variant delivers an invitation, not verified membership.
Source entry: Community comment or DM
Source requirements: Press the opening button; Verify a follow before the invitation
Source timing: Link click: 3 days; follow and opening button: 2 days.
Source outcome: An invitation to an external community
Captured text (n001, not approved campaign copy):
Hey {{contact.name}} ❤️ Do you want to join my community?
Yesss 👀
Current setup decision: waiting_for_chatfuel. The promised resource, coupon or eligibility depends on a verified Instagram follow. Ordinary MCP cannot check follower status; unconditional delivery would remove the gate.
Primary Chatfuel result: An invitation to an external community
Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence.
Use the existing community and invitation service.
Ask me for: Community and invitation URL; Membership or access rules; Existing authorized access.
1. Confirm the destination and owner authorization. Draft invitation settings and check the intended membership rules without issuing invitations.
2. Distinguish link delivery, link clicks and actual membership. Do not claim automatic admission, membership verification or expiry without evidence from the service. Return the destination check, draft settings and unresolved access.
3. Prepare a draft only. Do not create accounts, spend, register senders, activate automations, send messages or change live settings without separate approval.
4. Use existing authorized access available in this host. Never request secret API keys in chat. Do not assume background persistence or an installed connection; claim connected only after readback.
5. Keep the selected source gates, delays and optional inputs explicit. Any changed journey needs owner approval. Do not silently introduce exports, manual transfers, Zapier, a new MCP or backend.
```
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](community-inro-6051.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
