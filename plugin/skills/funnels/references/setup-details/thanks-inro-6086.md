# Thank a verified Story mention with a Like

Setup 1.1.0 | thanks-inro-6086 | waiting_for_chatfuel | runtime not tested

## Business Result
Acknowledge kind comments, messages and shared Stories.
Creators and teams who want to respond to audience appreciation.
Source entry: Verified mention of the account in a Story
Source outcome: A Like reaction to the mention
Source requirements: Wait 1 minute; Like the message
Source timing: Delay: 1 minute.

## Functional Availability
waiting_for_chatfuel
The entry requires a verified Story mention and the result is an Instagram Like reaction. Neither is configured by ordinary MCP; a self-reported mention is not equivalent.
Primary result: A Like reaction to the mention
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- story: Story-specific configuration is dashboard-only for normal MCP. Ordinary DM does not verify a Story reply or mention.
- ig-like: Documented Like applies to Facebook, not Instagram.
- timers: messageDelays is dashboard-only for the normal profile; exact per-step delays and expiration branches are not exposed. Generic followUps is not an exact timer.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6086: Thank people who share you in their story
Full captured settings/provenance: [selected source JSON](../source-records/inro-6086.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: story
Captured text (not approved outbound copy):
```text
When
Someone mentions you in a story
FILTER STORIES
Any story that mentions you
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (delay)
Retain the exact captured delay; no numeric per-step timer in ordinary MCP.
Business input: approved timing change
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: timers
Captured text (not approved outbound copy):
```text
Wait 1 minutes
```
- Field (captured): {"label":null,"type":"number","value":"1","value_state":"observed_value","options":null,"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"label":null,"type":"text","value":"minutes","value_state":"observed_value","options":[{"selected":false,"text":"seconds","value":"seconds"},{"selected":true,"text":"minutes","value":"minutes"},{"selected":false,"text":"hours","value":"hours"},{"selected":false,"text":"days","value":"days"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"seconds"}
- Field (captured): {"value":"minutes"}
- Field (captured): {"value":"hours"}
- Field (captured): {"value":"days"}
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (like)
Instagram likes are not configured by likeContactComment; that field is Facebook-only.
Business input: whether omitting the reaction is acceptable
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: ig-like
Captured text (not approved outbound copy):
```text
❤️
Like message
```
- Edge e002: n002 -> n003 | condition/label: ""
#### n003 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Thanks: mentioned…
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":{"disabled":null,"inputmode":null,"max":null,"maxlength":null,"min":null,"minlength":null,"pattern":null,"readonly":null,"required":null}}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](thanks-inro-6086.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
