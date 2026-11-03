# Hide spam and hateful comments

Setup 1.1.0 | moderation-inro-6111 | waiting_for_chatfuel | runtime not tested

## Business Result
Handle unwanted comments and make space for genuine questions.
Teams with a defined moderation policy or a private complaint process.
Source entry: Any post: hate/spam filter
Source outcome: A hidden comment and a tagged contact
Source requirements: Recognize an unwanted comment; Hide the comment
Source timing: No exact timer captured.

## Functional Availability
waiting_for_chatfuel
Hiding a hate/spam comment and applying the source moderation actions are unavailable through ordinary MCP. A complaint DM is not moderation.
Primary result: A hidden comment and a tagged contact
Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.

## Shared Setup Procedure
Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.

## Selected Preparation
SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency.
- moderation: No Instagram hide/delete comment action or dedicated hate/spam detection input. Replying to named words is not moderation.
- graph: Full deterministic flow-builder graphs and arbitrary folder/tag/field branches are dashboard-only, not graph import through normal MCP.

## Complete Captured Topology
Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state.
### inro-6111: Keep hate out of your comments
Full captured settings/provenance: [selected source JSON](../source-records/inro-6111.json). Start: n000.
#### n000 (trigger)
Read the actual captured entry. Post/comment configuration is not Story, Live, ad or referral configuration.
Business input: entry word and selected post or invitation placement
Setting candidate: No direct normal-MCP setting
Disposition: documented_primitive_not_graph_equivalence; dependencies: 
Captured text (not approved outbound copy):
```text
When
Someone comments on your post
SELECT THE POSTS
All posts
FILTER THE COMMENTS
automation.scenarios.steps.select_comments.hate_spam
```
- Edge e000: n000 -> n001 | condition/label: ""
#### n001 (hide_comment)
No hide/delete operation. Private complaint handling is a different outcome, not moderation equivalence.
Business input: whether a different complaint-response goal is acceptable
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: moderation
Captured text (not approved outbound copy):
```text
Hide comment
Hide the comment from your post. You will still be able to see it in the hidden comments section.
```
- Edge e001: n001 -> n002 | condition/label: ""
#### n002 (folder)
Arbitrary folder/tag membership is not imported. Contact capture does not prove the original folder action.
Business input: business meaning of the membership/tag
Setting candidate: No direct normal-MCP setting
Disposition: requires_change_or_external_dependency; dependencies: graph
Captured text (not approved outbound copy):
```text
Add contact to folder(s)
Moderation: hidden
```
- Field (captured): {"label":null,"type":"text","value":"add","value_state":"observed_value","options":[{"selected":true,"text":"Add contact to folder(s)","value":"add"},{"selected":false,"text":"Remove contact from folder(s)","value":"remove"}],"validation":null}
- Field (captured): {"value":"add"}
- Field (captured): {"value":"remove"}
- No captured outgoing edge; do not infer completion.
All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation.
## Binding And Evidence
Profile: normal-mcp; observation 2026-11-02, revision 2026-11-02.3. Recheck after 2026-11-09 and before every write.
This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.
Structured audit: [setup record](moderation-inro-6111.json). Source changes and capability changes invalidate generated references; they never change live campaigns.
