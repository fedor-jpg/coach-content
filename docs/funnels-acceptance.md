# Funnels: Acceptance

## Result

One setup skill. The owner selects a ready funnel, supplies missing business facts, approves the messages and saves a paused campaign. Activation needs separate approval. The assistant verifies delivery, supports edits and pauses only the owned campaign.

Customer files contain no competitor audit, unready variants or fallback recipes. The complete internal library lives in `internal/funnels`. Its captured texts, branches, settings and source hashes remain intact.

## Acceptance Criteria

1. **Package:** A clean installation can read the short entrypoint, index, selected funnel and operation instructions. No local paths, terminal commands, external private files or unsupported variants are needed.
2. **Conversation:** The first response shows the actual subscriber path and concrete messages. It asks only for missing business facts. No adaptation table, technical IDs, unsupported promise or claimed conversion guarantee appears.
3. **Safety:** Saving stays paused. Activation requires separate explicit approval. Current targeting, messages, switches and overlapping rules are checked. Unrelated automations remain unchanged.
4. **Result:** An authorized subscriber enters through the exact trigger, receives the approved message and opens the correct material. Every advertised alternative and negative branch is tested. A preview does not pass this criterion.
5. **Lifecycle:** A repeated setup command creates no duplicate. Return reconciles the existing campaign. An approved edit changes only the intended text. A stop leaves the owned rule OFF and a fresh entry receives no campaign response. Unknown write results are reconciled, not retried.
6. **Release:** The accepted catalogue binds the exact instructions, customer funnel, helper, version and tested host/model/connector. Changed instructions invalidate acceptance. Empty, stale or incomplete acceptance blocks publication. Fedor's acceptance precedes publication.

## First Candidate

**Send a resource from a comment.** The owner chooses a post and provides the material link. The assistant writes the public reply and first DM. A matching comment delivers the link. The campaign sends no confirmation question or follow-up.

Starter: "Use Funnels. Set up sending my resource when someone comments on my post. Prepare the messages and ask only for what is missing. Keep the campaign paused until I approve activation."

The candidate is a reviewable instruction, not an accepted campaign. The production registry currently contains no runtime-accepted recipe. No customer archive is released until the live criteria pass. Test fixtures cannot change that registry.

## Maintainer Checks

Run `python3 plugin/scripts/funnel_library.py --check` to validate all original references. Run the focused Python tests, including `tests/test_customer_funnels.py`, to validate export boundaries and lifecycle logic.

After real acceptance is recorded in `internal/funnels/catalog.json`, `python3 plugin/scripts/funnel_library.py --customer-package <new-path>.skill` exports only accepted customer instructions. `python3 plugin/scripts/coach.py release <new-path>` applies the same gate to the full plugin. Neither command publishes or grants account permissions.

Storage/upload remains a separate task. An attachment in an AI chat is not a durable public URL. Do not add hosting, payments, email or SMS to this change.

## Verification: 2026-11-03

- All 301 pre-existing reference files have unchanged SHA-256 checksums after relocation. The generator validates all 60 sources and 57 variants.
- Nine customer-export tests pass, including the complete evidence-validator-to-export path using explicitly synthetic records. No synthetic record entered the real catalogue.
- The complete Python suite ran 174 tests: 166 passed. Eight existing video/render checks failed because the installed FFmpeg lacks the required subtitle/drawtext, H.264 or AAC capabilities. No video environment changes were made.
- Four setup/snapshot checks and 16 snapshot/description checks pass after regenerating the local library snapshot. The viewer builds with unchanged donor-source hashes. No site was deployed. Browser/UI inspection was not performed.
- Independent static review found two release defects. Both were corrected and regression-tested. The reviewer found no unresolved issue in the two corrections.
- The real catalogue remains empty. The real packaging command rejects an empty release before creating a file. Clean native installation, real delivery, edit, return and live stop are not accepted. Account settings and messages were not changed.
- The prior published archive remains unchanged. No Git commit, push or new release was made. Hosting is tracked separately in [FED-70](https://linear.app/chatfuelteam/issue/FED-70).
