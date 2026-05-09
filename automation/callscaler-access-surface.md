# CallScaler access and reusable operator surface

Date: 2026-05-08
Issue: DIG-57
Operator: Browser Operations Lead

## Classification

Status: viable public surface, but the currently available secure dotenv keys did not authenticate read-only API probes.

CallScaler is reachable and has a documented API plus a browser dashboard. DIG-57 proved the base path exists without credentials; DIG-64 rechecked with runtime-only secure dotenv loading and found CallScaler-style key names, but both available key values still returned HTTP 401 `unauthorized` on the smallest safe reads. The blocker is now narrowed from missing key binding to `api_base_verified_credentials_invalid_or_unscoped`.

Precise blocker:
- DIG-64 found `CALLSCALER_API_KEY` and `CALLSCALER_API_KEY_1` in the secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env`; no raw key values were printed, copied, or committed.
- `tools/.env` and `tools/.env.example` still do not contain CallScaler-specific credential names, which is acceptable because live probes should load the secure dotenv explicitly.
- Safe GET probes using each secure key against `GET /calls?limit=1`, `GET /dashboard/stats`, and `GET /numbers?limit=1` all returned HTTP 401 JSON `{"error":"unauthorized"}`.
- Additional default-key probes against `GET /analytics/calls` and `GET /call-flows` also returned HTTP 401 `unauthorized`.
- The secure key values are non-placeholder shaped, so the likely next distinction is expired/revoked key, wrong account/tenant, non-API token, missing account entitlement, or a required key generated from `https://v3.callscaler.com/app/settings?tab=api-keys`.
- The safe browser path from DIG-57 could not use an existing session in that run: the browser MCP bridge reported an already-running profile conflict, and the fallback Playwright browser could not launch because its Chromium dependency `libnspr4.so` is missing.

## Confirmed entry paths

Dashboard/login:
- `https://callscaler.com/login` redirects to `https://v3.callscaler.com/login`
- Login supports email/password and Google sign-in.
- Public config endpoint: `https://v3.callscaler.com/api/v1/public/config`
- API key creation path from docs: `https://v3.callscaler.com/app/settings?tab=api-keys`

API:
- Base URL: `https://callscaler.com/api/v1/`
- Auth: `Authorization: Bearer API_KEY`
- Docs path: `https://callscaler.com/docs/api-reference`

## Highest-value read-only surfaces after authentication

1. Calls and recordings metadata
   - `GET /api/v1/calls`
   - `GET /api/v1/calls/:id`
   - `GET /api/v1/calls/:id/transcription`
   - `GET /api/v1/calls/:id/recording` only when recording access is explicitly needed and privacy policy allows it.
   - `GET /api/v1/calls/export`

2. Analytics and attribution
   - `GET /api/v1/analytics/calls`
   - Useful groupings documented publicly include date, source, UTM campaign, hour of day, and day of week with metrics such as count, answered/missed count, qualified count/percentage, total value, unique callers, average duration, and AI score.

3. Numbers and number inventory
   - `GET /api/v1/numbers`
   - `GET /api/v1/numbers/export`
   - `GET /api/v1/numbers/bulk-stats`
   - `GET /api/v1/numbers/{id}/stats`
   - Docs explicitly note there is no `GET /api/v1/numbers/:id`; list numbers and look up IDs client-side.

4. Call flows and routing readback
   - `GET /api/v1/call-flows`
   - `GET /api/v1/call-flows/{id}`
   - `GET /api/v1/call-flows/{id}/numbers`
   - `GET /api/v1/call-flows/{id}/versions`

5. Forms, voicemails, SMS/conversations
   - `GET /api/v1/forms`
   - `GET /api/v1/forms/{id}`
   - `GET /api/v1/voicemails`
   - `GET /api/v1/voicemails/{id}`
   - `GET /api/v1/sms`
   - `GET /api/v1/conversations`

6. Dashboard/account observability
   - `GET /api/v1/dashboard/stats`
   - Docs expose browser pages for Overview, Call Log, Voicemails, Numbers, Call Flows, Addons, Billing, Logs, and Settings.

7. Webhook/integration visibility
   - Docs describe post-call webhooks and integrations with Zapier, Slack, CRM endpoints, Google Sheets, and ads connectors.
   - Treat webhook configuration changes as mutating and out of scope unless separately approved.

8. Billing and account logs
   - Browser: `https://v3.callscaler.com/app/settings?tab=billing`
   - Browser: `https://v3.callscaler.com/app/logs`
   - API docs state admin/owner roles are required for billing and API key management.
   - Read-only billing checks should avoid payment-card changes, auto top-up changes, plan changes, or API key rotation.

## First safe non-mutating workflows once a credential/session is available

1. API health check
   - `GET https://callscaler.com/api/v1/calls?limit=1`
   - Success criterion: 200 JSON with call-list shape; do not store private call data in repo.

2. Inventory summary
   - Query numbers, call flows, and dashboard stats.
   - Persist only aggregate counts and endpoint viability, not raw phone numbers or call records.

3. Attribution/readiness report
   - Query `GET /api/v1/analytics/calls` grouped by source and UTM campaign for a narrow date range.
   - Persist only aggregate metrics needed for launch/operations decisions.

4. Export capability check
   - Open Call Log export UI or call `GET /api/v1/calls/export` only with minimal filters.
   - Do not commit CSV exports, recordings, transcripts, phone numbers, caller names, or lead/call content.

5. Integration map
   - Read addons/integration pages and webhook-delivery metadata, if exposed by the authenticated account.
   - Do not create, delete, or rotate webhooks/API keys without an explicit mutation task.

## Safety notes

Do not provision numbers, buy numbers, alter call routing/call flows, create campaigns, modify integrations, rotate keys, alter billing, export private lead/call data into the repo, or persist raw cookies/credentials/phone numbers/recordings/transcripts.

## Recommended unblock

Ask the operator to verify or rotate a real CallScaler API key from `https://v3.callscaler.com/app/settings?tab=api-keys`, confirm which account/tenant the two secure dotenv keys belong to, and approve one first read-only resource. After that, re-run only summary/redacted probes, starting with `GET /api/v1/calls?limit=1` or `GET /api/v1/dashboard/stats`. If API keys cannot be corrected, use a human-approved authenticated browser session to inspect Settings > API Keys and account/plan status without copying key values.

Do not add CallScaler to n8n or scheduled probes yet. Do not fetch recordings/transcripts, export calls, store phone numbers/caller identities, provision numbers, alter call flows, change billing, create webhooks, or mutate integrations without a separate write/privacy contract.
