# Offline checks

The assistant runs these commands using the verified installed helper path. Python 3.10+ and the standard library suffice except for optional QR generation, which needs `qrcode[pil]`. No FFmpeg is needed for funnels. The helper prints JSON; only the explicit `qr` command writes a PNG. It neither calls Chatfuel nor grants approval.

```text
python3 /actual/plugin/scripts/funnels.py validate
python3 /actual/plugin/scripts/funnels.py catalog
python3 /actual/plugin/scripts/funnels.py candidates --developer-qa
python3 /actual/plugin/scripts/funnels.py select inro-6025 --developer-qa
python3 /actual/plugin/scripts/funnels.py prepare inro-6025 --developer-qa --inputs /private/campaign/inputs.json --state /private/campaign/state.json
python3 /actual/plugin/scripts/funnels.py verify --plan /private/campaign/prepared.json --state /private/campaign/readback.json
python3 /actual/plugin/scripts/funnels.py activation-plan --plan /private/campaign/prepared.json --state /private/campaign/readback.json
python3 /actual/plugin/scripts/funnels.py verify --phase activation --plan /private/campaign/prepared.json --state /private/campaign/activated-readback.json
python3 /actual/plugin/scripts/funnels.py enable-plan --plan /private/campaign/prepared.json --state /private/campaign/activated-readback.json
python3 /actual/plugin/scripts/funnels.py verify --phase enabled --plan /private/campaign/prepared.json --state /private/campaign/enabled-readback.json
python3 /actual/plugin/scripts/funnels.py stop-plan --plan /private/campaign/prepared.json --state /private/campaign/current.json
python3 /actual/plugin/scripts/funnels.py verify-stop --plan /private/campaign/stop.json --state /private/campaign/stopped-readback.json
python3 /actual/plugin/scripts/funnels.py verify-stop --plan /private/campaign/stop.json --original-plan /private/campaign/original-prepared.json --state /private/campaign/current.json
python3 /actual/plugin/scripts/funnels.py restart-plan --original-plan /private/campaign/original-prepared.json --stop-plan /private/campaign/stop.json --stop-verification /private/campaign/stop-verification.json --inputs /private/campaign/inputs.json --state /private/campaign/current.json
python3 /actual/plugin/scripts/funnels.py release-check inro-6025 --evidence /private/acceptance --environment /private/campaign/environment.json
```

These are illustrative absolute paths, not host defaults. Use actual authorized native paths. Save printed preparation in the private campaign snapshot, not the plugin. Do not execute an unresolved path or ask the coach to copy JSON.

## Business input

The input object has `campaign_id` (lowercase ASCII slug), `parameters` and `accepted_changes`. Read the selected recipe's `required_inputs` and `allowed_parameters`; optional parameters are not in `required_inputs`. Reject unknown keys. `accepted_changes` must equal that recipe's design change IDs; do not use it to satisfy an original requirement which the design cannot provide. `select --requirements FILE` accepts a JSON string list of mandatory requirement tokens; only the recipe's declared `supported_requirements` qualify. Unknown mandatory requirements fail closed.

For `inro-6025`, supply actual `post_ids`, `keyword`, `language`, exact `public_text`, exact `initial_text`, exact `refusal_text`, exact `handoff_text`, `question_one`, `question_two`, `qualification_policy` and `next_step`. `next_step: handoff` requires no booking link. `next_step: booking_link` requires `booking_url`. Optional `resource_title` and `resource_url` travel together; the exact initial text must include both. The material URL must already work for the recipient. The helper does not host a file. Questions occur only after the recipient's actual reply.

All active recipes accept exact coach-language copy within their fixed outcome. Required facts, destinations and affiliate disclosure must remain in the initial value where the recipe requires them. Copy is not permission to add a gate, change a trigger, invent a result or send extra messages. The recipe's English examples illustrate meaning, not mandatory delivery language.

Recipe 6085 preserves ordinary incoming support: no keyword input or keyword gate is required. Its answer must use the actual question and approved facts. It does not silently change support into a campaign-word funnel.

Recipe 6081 requires a unique `membership_attribute`, `launch_name`, `launch_purpose` and explicit `consent_text` containing YES and STOP. Its initial text must include the launch, purpose and consent wording. Preparation creates native captures on the owned custom and general DM base. The same launch-specific name records `joined` after YES and `withdrawn` after STOP. Before YES it stays unset. The assistant must read `Conversation.contact.attributes` for that exact name before reporting membership or withdrawal. Prose, an email address and a preview are not live membership evidence. Do not hand off a withdrawal before the state write; other launches remain unchanged.

## QR artifact

Recipe 6019 requires the actual `instagram_username` in normalized state and a matching HTTPS `profile_url` under `instagram.com` or `www.instagram.com`. A Reel, post, Direct route, query, fragment or different account is rejected. Read the username from the connected account; helper validation cannot establish native provenance by itself.

In native Claude, check `python3 -c 'import qrcode, PIL'` in the same execution environment. If missing, use an authorized local dependency install: `python3 -m pip install 'qrcode[pil]'`. Do not add an MCP or work around installation restrictions. If installation is unavailable, report the QR dependency blocker. Then run:

```text
python3 /actual/plugin/scripts/funnels.py qr --profile-url https://www.instagram.com/actual_handle/ --username actual_handle --output /actual/project/docs/artifacts/profile-qr.png
```

Use actual verified values, not this example. The output path must be a new PNG. The command uses `qrcode`, not a hand-rolled encoder. Independently decode the image and compare its exact destination before sharing it. The coach's declared placement remains visible work; scanning alone does not trigger a DM. The person opens Direct and sends the campaign word. No scan attribution or coupon redemption is proved by the PNG.

## Normalized current state

Create this local object from the actual native read; it is not an API request:

- `schema_version: 1`, `observed_at` with timezone, `read_complete: true`.
- Actual `bot_id`, `account_id`, `platform: Instagram`, `connected: true` and complete selected account `posts` ID list.
- `environment`: exact nonempty `host`, `model`, `connector_contract` identifiers. A changed pin requires reacceptance.
- `ai_compatible: true` only after plan/credit checks establish AI compatibility. The Main bot must already be ON. General DM may be OFF for staging; its enable remains a separate approved step.
- Effective `whenAIReplies.option: Always` is required for general DM and owned AI continuation rules at preparation, activation and enable. Restricted or unknown availability blocks preparation; the helper never changes schedules or silently sets Always.
- Waitlist requires `known_attribute_names` (a string list) and `attribute_namespace_complete: true`. Read `Bot.botAttributes` across all platforms and system/custom types, without name filters. Collect `edges.node.botAttribute.name` and page with `after: pageInfo.endCursor` until `pageInfo.hasNextPage` is false. Set completeness only after successful full pagination. Do not collect individual contacts or values for this check. Missing inventory is not an empty namespace. Every native rule's active, dormant and inherited capture names are also checked, regardless of its enabled state. Repeat the namespace read before activation and enable.
- Complete `rules`: objects with `id`, `scope`, `isBase`, `enabled`, `settings`. Omit volatile display timestamps from these normalized objects. Include all affected and unrelated rules so preservation can be checked.
- Each `settings` map key uses its API setting name; its value holds the effective input fields plus `inheritsFrom` (`null` for owned settings). Resolve inherited values from the actual parent before preparing. Include every referenced parent and verify that inherited effective values match. Normalize `listOfPosts.posts` to `postIDs`. Normalize captures to `name`, `description`, optional `validationErrors`; handoff rules to their actual input fields without invented assignees.
- `actions`: unresolved scoped intents with `kind` and `status`, if any. `pending` or `unknown` blocks preparation, including an unknown send. Reconcile remotely first.
- Optional `ownership`: `campaign_id`, `recipe_id`, `account_id`, returned `rule_id`, and `rule_sha256` from `fingerprint(normalized_rule)`. This comes from the restored private card, never a matching name. It cannot claim a base/shared rule. An owned custom must be OFF for configuration.

The provider does not expose a contract version here. Derive `connector_contract` from the exact live public definitions below, not a connector label, model name, date or fixture value. Environment equality and acceptance gates remain unchanged. The helper cannot authenticate source provenance; actual current tool reads are mandatory. Clearly labeled synthetic identifiers and schema records remain offline developer QA only.

Without an owned ID, preparation emits only a concrete OFF-create command. After native approval and successful create, read it back and persist the returned ID. If the result is unknown, do not create again. With verified ownership, rerun preparation for the complete validated plan. Save and read back `ownership_before_write` and the exact plan before settings writes. This includes original settings, dormant lists and full inheritance parents. No placeholder IDs are executable. The plan hash binds its exact contents; native approvals and a fresh pre-write read still apply.

For waitlists, `ownership_before_write.attribute_namespace` saves `{names, complete}` from the original inventory. OFF capture configuration can register a new global name before any contact value exists. Fresh post-configuration inventory must include that name. Verification permits it only with saved original absence and exact unchanged campaign capture settings; any foreign native capture remains a collision. Missing original namespace proof requires reconciliation, not an inferred empty list. Native cleanup may remove an empty definition; the helper never deletes contact values or infers membership from namespace presence. `restart-plan` is the same-launch reservation path whether the name remains registered or disappears; normal `prepare` still rejects occupied names. It preserves `campaign_id`, membership name and all original inputs, joined/withdrawn values, and unrelated current settings. It needs the original plan, matching stop ownership proof, a fresh hashed `verify-stop` result, and unchanged affected current settings. This is not permission to reuse another campaign's attribute or old consent.

For `shared_mode: off-staging`, `commands` stage shared settings while general DM stays OFF; `activation` is empty. For `live-activation`, `commands` leave the ON DM base unchanged and `activation-plan` returns separately approved live shared writes. `verify --phase configure` checks the applicable branch. `verify --phase activation` checks final settings before `enable-plan` returns explicit enable commands. An originally OFF DM base requires separate enable approval; Main and other channels never appear there. Read back every write and final enable. Partial/unknown actions remain unresolved. These checks do not send, witness delivery or grant approval.

`stop-plan` consumes the exact saved preparation plus fresh state. It prints approved cleanup commands, complete `expected_rules`, `deferred_restorations` and a bound hash. `verify-stop` requires exact final readback, including preserved concurrent changes. For a late same-waitlist return, add `--original-plan ORIGINAL` to refresh verification against the SAVED stop without replacing its historical ownership proof. That explicit mode allows unrelated changes only; affected settings, switches, identity, complete namespace and foreign-capture checks remain mandatory. A new zero-command stop cannot supply missing historical capture ownership. The receipt binds `stop_rules_sha256` to the saved stop and `rules_sha256` to actual current readback; `verification_scope` identifies the check. Neither receipt is native provenance or live acceptance. Original inheritance returns through `setInheritFrom` only with exact current content and unchanged parents. Concurrent edits prevent snapshot overwrite. Changed/duplicated campaign additions cause refusal, not guessed cleanup. An unprovable shared DM enable instead adds a deferred `enabled` restoration: keep DM ON, disable the owned custom and remove exact campaign additions. Preserve current shared reply and follow-up modes so concurrent support stays available and dormant follow-ups stay inactive. `settings_stopped: true` is not live-stop acceptance; inspect `restoration_complete` separately. Cleanup never erases already captured contact attributes or recalls sent messages.

## Contract pin

Through the current Chatfuel Public API connector, make these ten `get_type` calls. Preserve each exact argument object and returned text. Do not substitute cached fixture definitions, account data or guessed version names. Check every response for successful complete output. The filtered Mutation response must show all matching results; a partial range requires reacquisition. The helper checks the fixed requests, expected named declarations, balanced definition blocks, complete pagination footers and known error/truncation markers. These narrow checks and explicit completeness attestation are not a full SDL parser or native authenticity proof.

```json
[
  {"name":"Mutation","filter":"fuelyAutomation"},
  {"name":"FuelyAutomation"},
  {"name":"FuelySettingUpdateInput"},
  {"names":["FuelySettingIncomingMessagesInput","FuelySettingSwitchToHumanInput","FuelySettingFollowUpsInput","FuelySettingCollectContactInfoInput","FuelySettingWhenAIRepliesInput"]},
  {"names":["FuelySettingKeywordsInput","FuelySettingListOfPostsInput","FuelySettingPublicReplyInput","FuelySettingPrivateReplyInput"]},
  {"names":["FuelySettingIncomingMessagesUpdateInput","FuelySettingSwitchToHumanUpdateInput","FuelySettingFollowUpsUpdateInput","FuelySettingCollectContactInfoUpdateInput","FuelySettingWhenAIRepliesUpdateInput"]},
  {"names":["FuelySettingKeywordsUpdateInput","FuelySettingListOfPostsUpdateInput","FuelySettingPublicReplyUpdateInput","FuelySettingPrivateReplyUpdateInput","FuelyAutomationScope"]},
  {"names":["FuelySettingIncomingMessagesHowToReply","FuelySettingSwitchToHumanHowToSwitch","FuelySettingFollowUpsHowToSend","FuelySettingCollectContactInfoHowToCollect","FuelySettingWhenAIRepliesOptions"]},
  {"names":["FuelySettingKeywordsReactTo","FuelySettingPublicReplyHowToReply","FuelySettingPrivateReplyHowToReply","FuelySettingSwitchToHumanRuleInput","FuelySettingCollectContactInfoEntryInput"]},
  {"name":"FuelySettingSwitchToHumanRuleAssigneeInput"}
]
```

Save a private JSON object with `schema_version: 1`, `source: chatfuel-public-api.get_type`, `definition_set: coach-funnel-native-v1`, timezone-bearing `observed_at`, and `records`. Each record has exactly `tool: get_type`, `arguments` from one call above, and verbatim returned `text`. All ten calls must be from the same current connector. Use the oldest read time for `observed_at`. After checking complete responses, run:

```text
python3 /actual/plugin/scripts/funnels.py contract-pin --bundle /private/campaign/schema-reads.json --complete
```

The bundle must be no older than 15 minutes. `--complete` attests complete successful tool responses, not approval for mutations. The command rejects missing, duplicated or different requests. It hashes canonical JSON, sorts records by request identity, and excludes only the read timestamp. Exact returned text, source, definition set and arguments remain in the hash. Repeating the same reads produces the same `chatfuel-funnel-input-sha256:...` pin. A definition change produces a different pin and invalidates environment compatibility. This is a fingerprint of the used mutation/input contract, not a version of the whole API. Actual automation readback validation and release evidence remain required.

## QA plan export

Maintainers can render every configured candidate with the same production `prepare()` function:

```text
python3 tests/test_funnels.py export-qa --state /private/tmp/native-state.json --inputs /private/tmp/qa-inputs.json --owned-rule-id ACTUAL_OFF_CUSTOM_ID --output /private/tmp/qa-plans.json
```

Inputs are a list of `{id, fixture, business}` objects. `business` is passed unchanged to `prepare`; approved qualification copy needs no edits. The state is a complete actual normalized snapshot. The custom ID must be an approved existing OFF Instagram comment custom. The utility binds its actual fingerprint for each test campaign, never guesses IDs or changes switches. Without supplied state/inputs, it exports clearly labeled synthetic fixtures instead. `--refresh-observed-at` is permitted only after verifying that the native baseline remains unchanged. Each output case contains business input, source snapshot and actual plan, or a blocking input error without commands. Output is not a runtime receipt. Never execute plans sequentially against a changed baseline without fresh readback/restoration.

## Grounded acceptance records

The customer catalogue is intentionally empty. A maintainer alone runs `release-check --evidence DIR --environment FILE` against private proof. A successful result includes sanitized `catalog_metadata`; it never writes or publishes it. Only after independent human acceptance may a maintainer place that metadata in the installed catalogue. It contains id, version, digest, environment, goal, recipe path, and acceptance status/date/variants/material flag. It contains no account IDs, contacts, receipts, runs or QA logs. No signatures or new service are required.

`catalog` without arguments discovers those sanitized accepted entries after installation or relocation. `catalog --environment FILE` filters them to the actual environment. Customer `select --environment FILE` and `prepare` require compatible host/model/contract pins and the accepted outcome variant. They never request private evidence. Recipe/code changes invalidate metadata through the digest. Raw receipts remain private and are checked by maintainers, not installed customers.

The evidence directory contains `<recipe_id>.json` with `schema_version: 1`, `fixture: false`, `recipe_id`, current `recipe_digest`, environment and `runs`. Each run has unique `id`, distinct `input_sha256`, mode `live` or `preview`, compatible true, platform, account/bot/recipient IDs, author-account flag, and a `checks` map. Each check refers to an actual receipt by safe relative `path` and exact file-byte `sha256`. At least three independent runs and two different compatible live accounts are required; one live account must not be the author's. Every live run covers the recipe's full `runtime_checks` and applicable `business_outcomes`, `outcome_variants` and `conditional_business_outcomes`. Preview runs cover content, return and stop. Content and actual business results are not inferred from successful tool calls.

Each run also references its actual business input and prepared configuration by the same path/hash shape. The input must validate against the recipe and match input_sha256. The plan must bind the account, bot, environment, recipe digest and business input, and its plan hash must match. Each run's `source` includes kind (the recipe entry), actual entry_event_id and keyword; comment/public sources also require post_id from the approved inputs. Ordinary support instead has `ordinary_inbound: true` and no keyword requirement.

Each referenced receipt has schema version 1, fixture false, passed true, a specific nonempty observation, timestamp and origin `native-readback`, `recipient-observation` or `human-review`. Its exact `bindings` are recipe ID/digest, run ID, account ID, bot ID, recipient ID, input SHA, mode, platform, the complete source object and check name. Bindings cannot cross runs, contacts, modes or sources. Store only minimal redacted observations and native proof references privately; never publish full chats or account IDs in this plugin.

Business receipts must use their recipe's required origin and include `native_refs` to actual returned events or native observations. Destination checks must bind the exact approved URL. `two_actual_answers` additionally needs two distinct referenced inbound event IDs and two nonempty actual answers matching the approved questions and recipient. Material-enabled 6025 runs need initial material delivery and phone-access observations. Handoff runs need confirmed native handoff. Booking-link runs need actual link receipt and no false booking or automatic handoff claim. Missing outcome receipts block acceptance, even if generic negative cases pass.

Waitlist business receipts additionally require exact `attribute_name`, `launch_name` and `attribute_value` (`joined` or `withdrawn`) from actual native contact-attribute readback. A response saying "joined" is not that evidence. Preview capture proves only that preview's mechanism. Live duplicate handling, two-launch isolation, withdrawal ordering and post-stop behavior remain required.

The evidence manifest's `acceptance` object has status accepted, an independent reviewer, `runs_sha256` from `fingerprint(runs)`, at least three distinct `target_users` (ID, unassisted true, business_clarifications 0 or 1), and `fresh_install_and_private_recovery: true`. It declares accepted `variants` (`handoff`, `booking_link`, or `default`) and optional `material_delivery`. Each advertised variant and material capability requires applicable live business receipts. Its acceptance receipt bindings are recipe ID/digest, runs SHA, variants, material_delivery (false if absent), and check `independent_acceptance`. The reviewer must verify authenticity, content quality, recovery, all distinct user paths and actual stop. The helper checks integrity and completeness, not whether observations truly occurred. Handwritten false receipts remain false evidence.

`recipe_digest` binds the complete recipe, execution brief, entry skill and helper implementation. Changing any invalidates old acceptance; model/host/contract changes also invalidate eligibility. Business values may vary only within accepted parameters and require current campaign approvals. Source contract changes must update the recipe or environment pin. No production version bump or publication is implied.

## Prompt evaluations

Repository maintainers use `tests/funnel-prompts.json` in fresh Claude sessions with no source IDs disclosed. Each recipe has three realistic goal variants, expected recipe/outcome boundaries and grading criteria. Unsupported lookalikes and video/waiting/resume controls are separate. Grade actual assistant output, not the expected ID fed into a function. The automated tests validate deterministic selection eligibility and fixture structure; they do not claim these conversational evaluations ran. No agent starts automatically.
