# KonnectzIT Access-Completion Packet

Verification timestamp: 2026-05-08T09:36:47Z
Operator: Browser Operations Lead
Related issues: DIG-43, DIG-62

## Purpose

This packet is the exact operator handoff required before agents resume KonnectzIT browser or API verification. It exists because DIG-43 verified the public browser entry path and SPA API base but also proved that the current local secure sources do not contain credential material that establishes access.

KonnectzIT remains high-value for this repo because it is a browser-first automation/integration layer that could expand Hermes/Paperclip workflow operations. Do not convert assumptions into account facts. Resume only after the missing credential/session values below are provided through an approved secure channel.

## Current classification

Status: `browser_url_verified_credentials_invalid`

Already known from DIG-43 and this DIG-62 packet pass:

- Public marketing/root URL: `https://konnectzit.com/`
- Correct browser app entry path: `https://app.konnectzit.com/`
- Correct browser login path: `https://app.konnectzit.com/login`
- `https://app.konnectzit.com/` and `/login` currently return the KonnectzIT single-page app over HTTP 200.
- SPA API base identified during DIG-43: `https://api.konnectzit.com`
- Login route identified during DIG-43: `POST /api/v1/auth/login`
- Safe runtime-only login probes against `https://api.konnectzit.com/api/v1/auth/login` using the available generic credential-pool pairs returned HTTP 401.
- Secure source inspection during DIG-43 found no `KONNECTZIT_*` env/API key material and no tool-specific KonnectzIT username/password entry in the inspected credential file.
- No authenticated browser session, bearer token, workspace/account ID, workflow inventory, webhook surface, or connected-app surface was reached.
- `www.konnectzit.com`, `panel.konnectzit.com`, and `dashboard.konnectzit.com` did not resolve during DIG-43. Do not retry those as primary entry paths unless the operator supplies evidence that they changed.

Important classification nuance: the blocker is valid credential/session material, not a missing URL. It is not yet an MFA-only or session-only classification because no valid first-factor credential was observed.

## Missing values the operator must provide

Provide these through the approved secure credential/session channel. Do not paste passwords, tokens, cookies, webhook URLs, workflow payloads, connected-app credentials, or AppSumo license codes into Git, Paperclip comments, screenshots, chat, or terminal output.

| Required input | Exact value needed | Why it is required | Acceptable evidence format |
|---|---|---|---|
| Browser login/session path | Either a human-established persisted ops browser profile/session already logged into `https://app.konnectzit.com/`, or a dedicated username/password entered by a human into the browser at runtime. | Current secure sources do not authenticate; browser verification cannot proceed without an approved account/session. | Preferred: persisted Chrome/Playwright profile path plus account label. Alternative: operator joins a live session and types credentials without exposing them. |
| Account/workspace label | Human-readable label for the KonnectzIT account/workspace: internal ops, demo/test, AppSumo LTD account, client account, inactive legacy account, etc. | Lets agents choose the lowest-risk read-only target and avoid confusing client/private automation data with internal operator data. | Non-secret label and one-line scope summary. |
| MFA/session prerequisite | Whether MFA, CAPTCHA, device approval, email OTP/magic link, IP allowlisting, password reset, or account lockout policy applies. | Prevents repeated failed login attempts, lockouts, or broken session handling. | Plain-language note only; no OTPs, recovery codes, or magic-link URLs in repo/Paperclip. |
| Approved first-read target | The first screen or endpoint agents may inspect after access is established. | Keeps verification narrow and reversible. | Example: `Open dashboard only and record title/navigation labels`, or `Map workflow list count only; do not open workflow steps`. |
| API/token availability | Whether the account exposes a user API token, developer key, webhook/API trigger credentials, or documented auth token after login. | DIG-43 found the SPA API base but no reusable API credential; future API verification needs an operator-approved token source if it exists. | Store token/key only in secure runtime source; repo may record variable names and high-level scope. |
| Connected-app sensitivity note | Which connected apps/integrations may be visible and whether any are client/private, finance, email, CRM, or production-critical. | KonnectzIT workflows can expose third-party account names, webhook URLs, mapped fields, and automation history. | Non-secret category summary such as `contains production CRM/email integrations; inventory only`. |
| Write-safety boundary | Explicit confirmation that this pass is read-only and which actions remain forbidden. | KonnectzIT is an automation tool where opening/running/editing flows can trigger downstream effects. | Plain-language approval scope; default is no creates, edits, toggles, tests, runs, reconnects, or webhook changes. |

## Recommended secure variable/session shape

Use the operator's normal secure store. Names below are examples only; do not commit values:

```text
KONNECTZIT_ACCOUNT_LABEL=
KONNECTZIT_LOGIN_EMAIL=
KONNECTZIT_LOGIN_PASSWORD=
KONNECTZIT_BROWSER_PROFILE_PATH=
KONNECTZIT_MFA_NOTE=
KONNECTZIT_API_BASE=https://api.konnectzit.com
KONNECTZIT_API_TOKEN=
KONNECTZIT_SCOPE_NOTE=
KONNECTZIT_FIRST_READ_TARGET=
```

If a persisted browser profile is used, prefer storing only `KONNECTZIT_BROWSER_PROFILE_PATH` and `KONNECTZIT_ACCOUNT_LABEL` for agents. Keep credentials, cookies, local storage, and session artifacts outside the repo and out of Paperclip comments.

## Safe first-read verification plan

### Guardrails for both paths

- Read-only only.
- Use the lowest-risk internal/demo account first.
- Do not create, edit, enable, disable, duplicate, delete, test-run, manually run, publish, connect, reconnect, import, export, rotate, or change settings.
- Do not reveal or store webhook URLs, API keys, OAuth tokens, connected-app credentials, mapped payloads, automation run payloads, customer records, email/message bodies, phone numbers, or private lead/contact data.
- Do not click controls that can trigger automations, send test requests, refresh tokens, reconnect apps, or change workflow state.
- Summarize metadata only: reachable/unreachable, page title, account/workspace label, top-level navigation labels, counts where safe, and high-level surface names.
- Stop immediately on MFA/CAPTCHA, account warnings, credential reset prompts, disconnected-app repair prompts, billing/payment prompts, unexpected private-data exposure, or any UI that cannot be inspected without risk of mutation.

### Browser path

Prerequisite: human-approved session/credential path for `https://app.konnectzit.com/`.

1. Open `https://app.konnectzit.com/` or `https://app.konnectzit.com/login` in the approved ops browser profile.
2. If already authenticated, record only the page title, account/workspace label, and whether the account appears to be internal/demo/client-facing.
3. If not authenticated, have the human enter credentials at runtime; do not paste credentials into terminal, repo docs, Paperclip comments, or screenshots.
4. If MFA, CAPTCHA, device approval, email OTP/magic link, password reset, or account lockout appears, stop and ask the operator to complete it or provide a persistent approved session.
5. After login, inspect top-level navigation labels only before opening any workflow or app connection.
6. If the operator approved a first-read target, inspect only that screen and record a metadata-only summary.
7. Update this packet or the AppSumo access ledger with the result: account label, access status, top-level read-only surfaces visible, and any remaining blockers.

Minimum browser success definition:

- An authenticated KonnectzIT page loads.
- Account/workspace label is identified at a high level.
- No secrets, workflow payloads, webhook URLs, connected-app credentials, or private run data are copied.
- At least the top-level navigation/surface map can be described.

### API path

Prerequisite: operator confirms an API token/auth source or approves runtime-only reuse of browser-session auth for a documented low-risk read.

1. Load credentials only from the secure runtime source.
2. Use `https://api.konnectzit.com` as the API base unless official app evidence says otherwise.
3. First confirm auth with the lowest-risk account/profile endpoint available from the authenticated app, preferably a `GET` route that returns only the current user/account metadata.
4. If the API still requires `POST /api/v1/auth/login`, use it only with human-approved credentials loaded at runtime; never print the response token or store it in repo docs.
5. After auth, run one metadata-only read against the approved first-read target, for example workflow/app inventory count, not workflow detail payloads.
6. Summarize only HTTP status, endpoint family, object type, count/field-name metadata, and redacted blockers.
7. If 401/403 occurs, classify precisely: invalid credentials, expired/locked account, wrong account, missing API permission, session-only browser auth, MFA/CAPTCHA required, or endpoint/auth-shape drift.

Minimum API success definition:

- A live operator-approved credential/session returns an authenticated response on a low-risk read endpoint.
- Account/workspace label and credential scope are known.
- Output is redacted and data-minimized.

## Read-only surface map to prioritize after access is restored

Prioritize surfaces that prove KonnectzIT can support safe operator automation without exposing sensitive downstream system data.

| Priority | Surface | Why it matters | First-read approach | Write risk |
|---:|---|---|---|---|
| 1 | Dashboard / account overview | Confirms authenticated account, plan state, workspace identity, and top-level app readiness. | Page title + navigation labels + high-level account label only. | Low if read-only; avoid upgrade/billing prompts. |
| 2 | Workflow / zap inventory | Core proof of automation value and existing operating coverage. | Count/status/name-category summary only; do not open steps unless approved. | Very high; editing/toggling/running workflows can mutate downstream systems. |
| 3 | App connection catalog | Shows which apps are connected and what operator integrations may be possible. | App names/categories only; do not reveal account emails, tokens, OAuth details, or reconnect prompts. | Very high; reconnect/refresh can break or expose credentials. |
| 4 | Webhook / API trigger settings | Important for future Paperclip/Hermes event integration. | Existence/count and endpoint family only; do not copy webhook URLs or secrets. | Very high; webhook changes can break live automations. |
| 5 | Task/history/logs | Helps estimate reliability and activity without touching workflows. | Count/status/error category summary only; avoid payload/body/detail exports. | Medium-high; logs may contain PII/secrets. |
| 6 | App-event catalog / available triggers/actions | Useful for designing future integrations without live credentials. | Static catalog labels only if visible; prefer public docs if possible. | Low-medium; avoid adding apps or selecting connected accounts. |
| 7 | Account plan / limits / billing overview | Determines capacity and AppSumo LTD status. | Plan/limit labels only if safe; no billing details/screenshots. | High; billing/payment controls must remain untouched. |
| 8 | Team/users/settings | Governance context, not first-read. | Defer unless specifically authorized; count/role labels only. | Very high; invites/permissions/settings changes are forbidden. |

## What remains blocked vs known

### Known

- The browser app and login entry paths are known: `https://app.konnectzit.com/` and `https://app.konnectzit.com/login`.
- The SPA API base identified by DIG-43 is `https://api.konnectzit.com`.
- DIG-43 identified the login route as `POST /api/v1/auth/login`.
- The available secure sources inspected during DIG-43 did not include tool-specific KonnectzIT credentials or API key material.
- Generic credential-pool login probes returned HTTP 401.
- The current issue is credential/session material, not URL discovery.

### Blocked

- Authenticated browser verification of any KonnectzIT account/workspace.
- Live API reads against a real KonnectzIT account.
- Workspace/account identity and plan/limit confirmation.
- Workflow inventory, app connections, webhook/API trigger surfaces, and task/history mapping.
- Determining whether the account has MFA/CAPTCHA/session prerequisites.
- Determining whether any API token or stable non-browser auth path is available after login.

### Not allowed without a future explicit write issue

- Creating, editing, deleting, duplicating, enabling, disabling, testing, publishing, or running workflows.
- Adding/removing/reconnecting connected apps or OAuth accounts.
- Creating/changing webhooks, API triggers, schedules, filters, mappings, paths, or transformations.
- Rotating, exposing, copying, exporting, or storing webhook URLs, tokens, API keys, cookies, or OAuth details.
- Exporting workflow payloads, task logs, customer records, lead/contact data, message/email bodies, or private connected-app data.
- Changing team, billing, plan, account, or security settings.

## Operator checklist

Before assigning another KonnectzIT verification issue, complete this checklist:

- [ ] Approved browser access path provided: persisted session/profile or human-assisted login plan.
- [ ] Account/workspace label and sensitivity scope documented.
- [ ] MFA/CAPTCHA/device/session prerequisites documented.
- [ ] Approved first-read target selected.
- [ ] If API work is expected, token/session/auth source and allowed endpoint family provided securely.
- [ ] Connected-app sensitivity note provided.
- [ ] Agent instructed to keep output redacted, data-minimized, and read-only.

## Recommended next issue after completion

Once the operator provides the missing secure inputs, create a narrow read-only verification issue with this scope:

- Verify one approved KonnectzIT account in browser first; do not attempt all possible accounts or generic credential guesses.
- First browser read: authenticated page title, account/workspace label, and top-level navigation labels only.
- First approved surface read: workflow inventory count/status summary or app connection category summary, not workflow payloads or webhook details.
- If an API token/auth source is supplied, run one low-risk metadata endpoint and summarize HTTP status/counts only.
- Update `01-market-research/appsumo/2026-05-08-priority-access-ledger.md` with the final classification.
- Do not perform writes, test-runs, exports, webhook/app-connection changes, or settings changes.
