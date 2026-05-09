# SMS-iT CRM Access Classification

Verification timestamp: 2026-05-08T08:39:47Z
Related issue: DIG-55
Operator: Browser Operations Lead

## Security handling

- Runtime-only secure sources were inspected without copying raw API keys, passwords, license codes, cookies, session IDs, private contact records, message history, or campaign data into this document.
- Sources checked:
  - `C:\Users\ohu00\Documents\.env`
  - `C:\Users\ohu00\Documents\SOFTWARE TOOLS LOGIN CREDENTIALS.txt`
  - `C:\Users\ohu00\Downloads\tigertail-product-list-07-05-2026.csv`
- No messages were sent, no campaigns were created, no contacts were imported/exported, no automations were changed, and no billing/account settings were modified.

## Classification

Current classification: `api_docs_and_login_verified_credentials_invalid_or_unmapped`

SMS-iT CRM is not yet a reusable live operator surface for Hermes/Paperclip. The blocker is precise: the correct public/API documentation and browser-login paths are now known, and secure runtime sources contain SMS-iT-shaped API key material, but the available key material did not authenticate a safe account read and the approved browser credential pool did not establish a session.

This should not be treated as a missing-host problem. It should also not yet be treated as MFA-only, because no valid first-factor login was observed before the session attempts were rejected/limited.

## Verified entry paths

- Public marketing/product root: `https://www.smsit.ai/`
- Browser login path: `https://aicpanel.smsit.ai/login`
  - Page title observed: `SMS-iT™`
  - Form shape: `POST https://aicpanel.smsit.ai/login` with `_token`, `email`, `password`, and optional `remember` fields.
- Public registration path signal: `https://aicpanel.smsit.ai/register`
  - The marketing site links to this path, but direct unauthenticated requests may be Cloudflare-challenged.
- Legacy/empty app host: `https://app.smsit.ai/`
  - Returned an Apache-style `Index of /`; do not use this as the current CRM login/dashboard entry.
- API documentation host: `https://api.smsit.ai/`
  - Redirects to `https://smsit.stoplight.io/`.
  - Stoplight workspace home is reachable and identifies `SMS-iT Integration APIs`.
  - The visible docs homepage describes authentication plus endpoints for contacts, campaigns, and related CRM/marketing integration capabilities, but the current public page did not expose a directly downloadable OpenAPI spec during this pass.

## Credential-source result

- Secure operator dotenv contains `SMS_IT_API_KEY` and `SMS_IT_API_KEY_1`-shaped material. Values were handled runtime-only and are not copied here.
- The generic secure browser-login pool contains four username labels and four password labels, but no SMS-iT-specific username/password mapping was found.
- The AppSumo inventory contains one activated `SMS-iT CRM` License Tier 4 row. License/redemption values were treated as secret-like material and were not copied here.

## Runtime checks performed

### API/key checks

Safe account-read probes were attempted against the verified SMS-iT/AICPanel API surface only in read-only mode.

- `GET https://aicpanel.smsit.ai/api/user` with no auth returned `401 {"message":"Unauthenticated."}`.
- `GET https://aicpanel.smsit.ai/api/user` with each SMS-iT key using these auth shapes all returned `401 {"message":"Unauthenticated."}`:
  - `Authorization: Bearer [runtime key]`
  - `X-API-KEY: [runtime key]`
  - `api-key: [runtime key]`
  - raw `Authorization: [runtime key]`
- Additional safe guessed GET routes across `https://api.smsit.ai`, `https://api.smsit.ai/api`, `https://api.smsit.ai/api/v1`, `https://api.smsit.ai/v1`, `https://aicpanel.smsit.ai/api`, and `https://aicpanel.smsit.ai/api/v1` did not produce an authenticated read-only account/contacts/campaigns response.

Interpretation: the current key material is either invalid for this app surface, mapped to a different SMS-iT API/auth mechanism, stale/expired, or requires a companion account/workspace identifier not present in the inspected sources.

### Browser-login checks

- Runtime-only login probes used the approved generic credential labels from the secure credential file; no raw values were printed or stored.
- The first available generic pairs redirected back to the login page and did not establish an authenticated dashboard session.
- Later generic probes encountered HTTP 403/429 responses consistent with Cloudflare/rate limiting after repeated failed attempts.
- No authenticated dashboard, workspace, contacts, campaigns, pipelines, automations, messaging, calendars, sites, billing, or API/settings surface was reached.

Interpretation: available generic browser credentials are invalid/non-matching for SMS-iT, and further automated retries should stop until a human supplies a verified SMS-iT credential/session or confirms the API-key issuing context.

## Highest-value surfaces after access is completed

If a human-approved session or working API auth is supplied, the first read-only surfaces to map are:

1. Account/workspace dashboard and plan/license status.
2. Contacts/leads/lists/tags/custom fields, summarized by counts and schema only.
3. Campaign inventory and campaign status metadata, without opening/sending message bodies beyond minimal titles/counts.
4. Messaging channels/numbers/sender IDs/templates, summarized without exposing phone numbers or message history.
5. Pipelines/deals/stages if enabled.
6. Automations/sequences/workflows/triggers, read-only names/statuses only.
7. Calendar/booking/task surfaces if present.
8. Sites/forms/landing-page surfaces if present.
9. Integrations/API-key/settings pages for auth-shape completion and rate-limit documentation.
10. Billing/team/security settings, strictly read-only.

## First safe non-mutating workflows

Only after valid access is established:

- Account readiness summary: dashboard reachable, workspace/plan/license state, connected channel counts, and API/settings availability.
- CRM schema summary: contact/list/tag/custom-field counts and field names only; no exports or full contact records.
- Campaign/automation inventory summary: campaign/workflow names, statuses, counts, and last-updated timestamps only.
- Messaging capability check: connected number/sender/template counts only; do not open or copy message history.
- API documentation completion: capture confirmed base URL, auth header/body/query shape, and safe GET endpoints with HTTP status/count-only summaries.

## Guardrails

Do not send SMS/WhatsApp/email messages, create campaigns, import contacts, change automations, alter billing/team/security settings, rotate keys, redeem license material, export contact lists, or store raw credentials/cookies/private message/contact data without a separate write-authorized issue.

## Next action required

Ask the operator for one of:

1. a human-approved SMS-iT browser credential/session for `https://aicpanel.smsit.ai/login`, or
2. confirmation of what the `SMS_IT_API_KEY*` values are issued for, including any required workspace/account ID, base URL, auth header/body shape, and a safe read-only endpoint.

Until then, keep SMS-iT CRM out of automated n8n/Paperclip connector work and classify it as access-blocked rather than API-verified.
