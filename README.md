# Coach Content

Prepare an Instagram funnel from the audited library through existing Chatfuel MCP.
Version 0.3.0 adds the [setup skill](plugin/skills/funnels/SKILL.md): 30 adaptation drafts, 25 variants waiting for capabilities and two incomplete source references.
The 57 variants retain 60 captured originals. 35 entry plans preserve only their stated primary result and disclose changed or omitted behavior.
GitHub availability does not install the plugin, connect an account or verify a campaign. The accepted runtime registry remains empty.

The plugin also retains its existing permitted-video editing, practical exercise and approval workflows. This release does not change those three existing skills.

## Try Funnels in ChatGPT

**Start here:** [Download funnels.skill](https://github.com/fedor-jpg/coach-content/releases/download/funnels-setup-1.1.0/funnels.skill).
This is the complete template setup skill, including its library and supporting files. It does not include the separate video skills. Do not upload only `SKILL.md` or the whole repository ZIP.

You need a ChatGPT workspace with Skills and skill uploads enabled, plus access to the Chatfuel app. Availability depends on your plan and workspace. You do not need Git, a terminal or an API key for this path.

1. Download `funnels.skill` from the link above. No GitHub account is required.
2. In ChatGPT, open **Plugins > Skills > Create > Upload from your computer**. Select the file. Wait for the scan and confirm the skill appears under **Installed**. If ChatGPT requests a review, read it before proceeding. A blocked upload is not an installation.
3. Open a new chat. Select **Chatfuel** through **+**. If it is not connected, find Chatfuel in Plugins and complete its account authorization. Each user connects their own account; this download contains no account access.
4. Send this message:

   > Use the Funnels skill. Open "Auto-DM links from comments" from its library. Show the connected Instagram account, explain this template and its Chatfuel adaptation, then guide me through setup. Ask for missing business details. Do not change settings or launch anything without my confirmation.

5. Confirm the account, choose your post and supply the resource link. If Instagram is not connected, ask the assistant for a connection link and complete the platform authorization yourself. Review the proposed text, branches and changes before approving configuration.
6. Approve activation separately when the saved settings are correct. Test from another Instagram account. Check the received message and link, then ask the assistant to pause only this test automation and confirm its saved state.

The first response should use the named library template and explain any changed or unavailable behavior. It should not invent a replacement funnel or ask you to copy technical IDs. This skill configures a selected template; it is not the separate Instagram-analysis and funnel-selection skill.

The archive matches the published skill source. **ChatGPT import and a complete live campaign are not yet verified.** Installation does not authorize account changes or messages. The skill checks current MCP tools before setup; it must explain any missing capability or wider account effect before requesting approval.

If the Skills or Upload option is absent, this upload path is unavailable in your workspace. Pasting the repository URL into a chat does not install the skill. See [OpenAI's Skills instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) and the [release contents](https://github.com/fedor-jpg/coach-content/releases/tag/funnels-setup-1.1.0).

## Install the Full Plugin in Claude Cowork

Install from [fedor-jpg/coach-content](https://github.com/fedor-jpg/coach-content):

1. Open Customize > Plugins > Add plugin > Add marketplace > Add from a repository.
2. Enter `https://github.com/fedor-jpg/coach-content`.
3. Select Sync.
4. Install Coach Content.
5. Select the native Project or folder for the campaign.
6. Run `/coach-content:start` with a business goal or named funnel. For video work, explicitly request video production or resume a video campaign.

The assistant reads the compact setup index and only the selected detail. You supply business facts, not technical IDs or local commands.
Supported drafts remain preparation until separate readback and approval. Missing follower checks, unsupported entries and other mandatory capabilities keep setup blocked.
External email/SMS continuations are instructions, not installed integrations. No automated sending is authorized by reading or installing this repository.
See the [per-variant audit](docs/funnel-setup-audit.md) for preserved functions and exact limitations.

## Existing Video Evidence

Native 0.2.2 rendered a supplied licensed short clip and recovered it in a fresh session for revision; source/audio preservation and direct MP4 playback/download were verified.
Native private MP4/JSON/TXT readback also passed. These are component checks, not content-quality or full-flow acceptance.
Version 0.2.3 addresses matching revision assets, unsupported subtitle timing and one-snapshot persistence; updated native behavior remains unverified.
Supply permitted media and a transcript. Arbitrary large-source ingestion remains unverified.
YouTube-link-only intake is unsupported in the verified path. The native source download returned HTTP 403; do not bypass it.
Publication and subscriber delivery remain separate, unverified steps. Nothing sends automatically.

[Maintainer requirements and evidence](docs/maintainer-notes.md)
