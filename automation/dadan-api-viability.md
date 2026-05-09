# Dadan API Viability — DIG-56

Verification date: 2026-05-08
Owner: Automation Engineer
Related issue: DIG-56

## Safety contract

- Credentials were inspected only from runtime/secure dotenv sources; no raw API keys, cookies, passwords, request codes, private video metadata, or viewer analytics are stored here.
- Only unauthenticated/public page inspection, static app bundle inspection, and data-minimized `GET`/credential-shape probes were used.
- No Dadan recording requests were created, no demos/videos were uploaded, no videos were shared, no users were invited, no webhooks were changed, and no browser session/cookie material was persisted.
- `POST https://app.dadan.io/api/v1/usedadan/requestrecording` is documented by Dadan but is a create action. It remains unauthorized for the current read-only connector scope.

## Current classification

`api_verified_limited_readonly`

The prior `https://api.dadan.io` result was a wrong/obsolete guessed API host for this integration path. The active browser app and embedded developer docs point to `https://app.dadan.io/api/v1/usedadan`.

Dadan is viable only for a narrow manual-first read-only check against an already-known recording request code created by the same API key. It is not yet useful as a general account inventory API because the public/developer docs found in the app expose only recording-request create and recording-request detail endpoints.

## Evidence

### Public/browser surfaces

| Surface | Result | Notes |
|---|---|---|
| `https://app.dadan.io` | HTTP 200 | Current React SPA entry point. Sets normal anti-forgery cookies for the app. |
| `https://api.dadan.io` | HTTP 525 | Cloudflare/TLS origin error. Treat as a wrong or inactive guessed API host for this use case. |
| `https://dadan.com` / `https://www.dadan.com` | TLS hostname mismatch in curl | Not a reliable API/docs base for connector work. |
| `docs.dadan.com`, `help.dadan.com`, `support.dadan.com` | DNS did not resolve in this runtime | Public API docs were instead found embedded in the Dadan app bundle under the Developers settings page. |

### Auth and endpoint shape from app-bundle developer docs

The Dadan app bundle contains embedded developer documentation for two endpoints:

| Purpose | Method | Endpoint | Auth |
|---|---|---|---|
| Create recording request | `POST` | `https://app.dadan.io/api/v1/usedadan/requestrecording` | `X-Dadan-API-Key` header |
| Get recording request details | `GET` | `https://app.dadan.io/api/v1/usedadan/requestrecording/{RequestCode}` | `X-Dadan-API-Key` header |

The create endpoint accepts fields such as `title`, `instructions`, `externalSystemName`, `expireAfterDays`, `singleSubmission`, `allowanonymoussubmission`, `requestPassword`, `recordingModeCode`, `extraData`, and `targetFolder`, then returns a request code and public recording URL. This is a mutation and must not be automated without a separate write contract.

The detail endpoint returns request metadata and submission video references for a specific request code. This can expose private recording/video metadata, so future use must be limited to known operator-approved request codes and summary-only reporting.

### Runtime credential-shape probe

Secure source inspection found `DADAN_API_KEY` in `/mnt/c/Users/ohu00/Documents/.env`; `tools/.env` does not include it. The raw key was not printed or copied.

Data-minimized probes against the detail endpoint with a zero UUID request code produced:

| Probe | Result | Interpretation |
|---|---|---|
| No `X-Dadan-API-Key` | HTTP 401, message says `X-Dadan-Api-Key Is missing` | Header is required. |
| Invalid dummy key | HTTP 401, message says `X-Dadan-Api-Key Invalid value provided` | Server distinguishes invalid keys. |
| Runtime `DADAN_API_KEY` | HTTP 401, message says `You are not authorized to view this request` and `Request not found or not created by API key` | The runtime key is syntactically accepted by the Dadan API, but the test request code is not accessible. This is enough to validate base/auth shape without exposing real request/video data. |
| Same path on `https://api.dadan.io` | HTTP 525 | Confirms the prior guessed API host remains unusable. |

## Tooling update

`tools/appsumo_readonly_probe.py` now includes a guarded Dadan GET-only resource:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate
python appsumo_readonly_probe.py dadan --list-resources
python appsumo_readonly_probe.py dadan recording-request \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --request-code <operator-approved-request-code> \
  --summary-only --json
```

The tool uses `X-Dadan-API-Key` and requires `--request-code` before making the GET request. It intentionally does not implement the recording-request `POST` create endpoint.

## Smallest safe future workflow

Only after an operator supplies an approved request code created by the same Dadan API key:

1. Run the local probe manually with `--summary-only --json`.
2. Confirm the output does not include private video titles, requester names, webhook `extraData`, or viewer/submission details that should remain private.
3. If useful, create a disabled/manual-first n8n health workflow that accepts a single request code as input and emits only:
   - HTTP status;
   - success flag;
   - whether the request exists and is accessible;
   - submission count, if safe to reveal;
   - no raw submission video URLs/titles unless separately approved.

## Explicit non-goals / forbidden actions

- Do not call `POST /api/v1/usedadan/requestrecording` from automation without a separate write/mutation issue.
- Do not upload recordings, create demos, change webhook settings, share videos, invite users, or modify account/developer settings.
- Do not store recording request codes, video GUIDs, video URLs, viewer analytics, webhook payloads, `extraData`, cookies, or API keys in repo docs or Paperclip comments.
- Do not use `https://api.dadan.io` for current connector work unless official docs later reintroduce it and the TLS/origin issue is resolved.

## Operator asks before n8n promotion

- A dedicated automation-owned Dadan API key, preferably separate from any human/browser session key.
- One approved non-sensitive recording request code created by that key for a manual detail check.
- Written approval for exactly which fields may appear in n8n/Paperclip summaries.
- Separate write contract if the business ever wants automation to create request links or process webhook submissions.
