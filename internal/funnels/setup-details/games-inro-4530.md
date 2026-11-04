# Live quiz: correct answer and a 50% chance

Setup 1.1.0 | games-inro-4530 | waiting_for_chatfuel | runtime not tested

## Business Result
Use a quiz or prize reveal to make participation rewarding.
Creators choosing between knowledge-based results and chance-based rewards.
Source entry: Comment during a Live
Source outcome: A prize for some correct answers
Source requirements: Answer a question; Correct answer: random 50/50 outcome; wrong answer: no prize
Source timing: Opening button: 1 hour; reply: 2 hours; link click: 3 days.

## Functional Availability
waiting_for_chatfuel
The selected outcome requires random selection or allocation. Ordinary MCP cannot implement that selection; giving everyone the same reward is a different result.
Primary result: A prize for some correct answers
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- live: Post/comment configuration does not establish a Live-comment entry tool.
- random: No weighted random prize distribution in normal tool inputs.
- buttons: Normal reply inputs expose text modes, not rich buttons, callbacks, quick replies or galleries.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- click: No URL-click/no-click conditions or click-triggered actions in normal inputs.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-4530: Gamify IG Lives
Full captured settings/provenance: [selected source JSON](../source-records/inro-4530.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: live
Captured text (not approved outbound copy):
```text
When
Someone comments on your Live
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
IG Live Game Parti…
```
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (button_template)
Rich buttons/callbacks are not normal MCP fields. A text-choice adaptation needs approval; never treat it as the captured button event.
Business input: approved alternative text or choice words
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text
Are you ready? Win and get a chance to get an exclusive prize 
Let's go!!!🔥
```
Captured buttons: ["Let's go!!!🔥"]
- Edge e002: n002 -> n003 | condition/label: ""
- Edge e020: n002 -> n021 | condition/label: ""
#### n003 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN BUTTON IS CLICKED
Let's go!!!🔥
```
- Edge e003: n003 -> n004 | condition/label: "WHEN BUTTON IS CLICKED\nLet's go!!!🔥"
#### n004 (media_message)
Media/gallery delivery is not a normal reply setting. Do not silently turn required media into text.
Business input: approved destination or image requirement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons
Captured text (not approved outbound copy):
```text

```
Captured media: ["https://app.inro.social/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBM0g5TUE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--1da0e2b77e78f3b4d84036cdacdfea006b518ba2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCam9VY21WemFYcGxYM1J2WDJ4cGJXbDBXd2RwQWVBdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--77580adcb47c9209a9fc05070e60d13ba9bc109e/clap-clapping.mp4"]
- Edge e004: n004 -> n005 | condition/label: ""
#### n005 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Here are the rules:

Watch for my next question in your DMs.
Reply with your best answer.

✅ Got it right? Nice one! But heads-up: only 50 % of the correct answers will actually win, so luck still plays a part.

🔴 Missed it? No stress! Just catch my next live and have another go.
```
- Edge e005: n005 -> n006 | condition/label: ""
#### n006 (survey)
A link does not prove external form completion. Keep access-after-completion as an unresolved mandatory dependency.
Business input: survey destination and completion evidence
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, external
Captured text (not approved outbound copy):
```text
Quiz
Which of these animals is physically incapable of jumping?
Kangaroo
Elephant
Goat
Rabbit
```
Captured buttons: ["Kangaroo","Elephant","Goat","Rabbit"]
- Edge e006: n006 -> n007 | condition/label: ""
#### n007 (wait_for_reply)
AI instructions can wait for a real reply. Exact flow state and timeout semantics are not imported.
Business input: approved question and refusal behavior
Setting candidate: update_automation_setting: incomingMessages
Disposition: requires_change_or_external_dependency; dependencies: dm-ai, graph
Captured text (not approved outbound copy):
```text
Wait for reply
The scenario will pause and wait until the contact replies to proceed.
```
- Edge e007: n007 -> n008 | condition/label: ""
- Edge e016: n007 -> n017 | condition/label: ""
- Edge e018: n007 -> n019 | condition/label: ""
#### n008 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
IF MESSAGE CONTAINS
Elephant
```
- Edge e008: n008 -> n009 | condition/label: "IF MESSAGE CONTAINS\nElephant"
#### n009 (ab_testing)
Preserve exact source weights and outcomes. Ordinary MCP has no random allocation primitive.
Business input: approved changed outcome, if desired
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: random
Captured text (not approved outbound copy):
```text
A/B testing
Test different flows randomly to see which one performs better.
Option A: 50% - Option B: 50%
```
- Edge e009: n009 -> n010 | condition/label: ""
- Edge e014: n009 -> n015 | condition/label: ""
#### n010 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
50%
```
- Edge e010: n010 -> n011 | condition/label: "50%"
#### n011 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Congratulations, you won!
Luck was on your part after all 😃
```
- Edge e011: n011 -> n012 | condition/label: ""
#### n012 (conversion_link)
Delivering a text URL is possible; click/no-click events and external completion are not established.
Business input: approved URL and recipient access
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: buttons, click, external
Captured text (not approved outbound copy):
```text
Your prize!
Enjoy
Get it now 🥰
```
Captured media: ["https://app.inro.social/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBMk9YS0E9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b4f3d77b21751e3d6dd475c245ff3115e970eb9f/Screen%20Shot%202025-06-24%20at%204.38.11%20PM.png"]
- Edge e012: n012 -> n013 | condition/label: ""
- Edge e013: n012 -> n014 | condition/label: ""
#### n013 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
WHEN LINK IS CLICKED
```
- No captured outgoing edge; do not infer completion.
#### n014 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF LINK HASN'T BEEN CLICKED AFTER
3 days
```
- No captured outgoing edge; do not infer completion.
#### n015 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
50%
```
- Edge e015: n015 -> n016 | condition/label: "50%"
#### n016 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Your answer was correct, however you're not part of the winners! Join my next live to try again ❤️
```
- No captured outgoing edge; do not infer completion.
#### n017 (branch_option)
Preserve this outgoing branch and its actual target. AI intent is not a deterministic button callback or stored-field condition.
Business input: approved interpretation if replacing the branch
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
ELSE
```
- Edge e017: n017 -> n018 | condition/label: "ELSE"
#### n018 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Sorry... wrong answer!
Join my next live to try again ❤️
```
- No captured outgoing edge; do not infer completion.
#### n019 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF CONTACT HASN'T REPLIED AFTER
2 hours
```
- Edge e019: n019 -> n020 | condition/label: "IF CONTACT HASN'T REPLIED AFTER\n2 hours"
#### n020 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Thank you for joining my live. The game is expired, but you will be able to play next time! 
```
- No captured outgoing edge; do not infer completion.
#### n021 (branch_expiration)
No exact timeout/expiration branch in ordinary MCP. Do not replace this with generic followUps or send after silence.
Business input: approved changed timing, if any
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
IF BUTTON HAS NOT BEEN CLICKED AFTER
1 hours
```
- Edge e021: n021 -> n022 | condition/label: "IF BUTTON HAS NOT BEEN CLICKED AFTER\n1 hours"
#### n022 (message)
AI may use approved copy as instructions. Exact branch delivery and callback conditions are not imported. A first comment DM can use privateReply instead.
Business input: approved message and destination
Setting candidate: update_automation_setting: incomingMessages
Disposition: documented_primitive_not_graph_equivalence; dependencies: dm-ai
Captured text (not approved outbound copy):
```text
Thank you for joining my live. Even if you missed the game, you will be able to play next time! 
```
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](games-inro-4530.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
