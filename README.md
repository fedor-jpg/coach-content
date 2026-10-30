# Coach Content

Create and revise a Reel from a permitted video and transcript.
The plugin also prepares a matching practical exercise and tracks approvals.

Install from [fedor-jpg/coach-content](https://github.com/fedor-jpg/coach-content):

1. Open Customize > Plugins > Add plugin > Add marketplace > Add from a repository.
2. Enter `https://github.com/fedor-jpg/coach-content`.
3. Select Sync.
4. Install Coach Content.
5. Select the native Project or folder for the campaign.
6. Run `/coach-content:start` with your video, transcript and programme context.

Native 0.2.2 rendered a supplied licensed short clip and recovered it in a fresh session for revision; source/audio preservation and direct MP4 playback/download were verified.
Native private MP4/JSON/TXT readback also passed. These are component checks, not content-quality or full-flow acceptance.
Version 0.2.3 addresses matching revision assets, unsupported subtitle timing and one-snapshot persistence; updated native behavior remains unverified.
Supply permitted media and a transcript. Arbitrary large-source ingestion remains unverified.
YouTube-link-only intake is unsupported in the verified path. The native source download returned HTTP 403; do not bypass it.
Publication and subscriber delivery remain separate, unverified steps. Nothing sends automatically.

[Maintainer requirements and evidence](docs/maintainer-notes.md)
