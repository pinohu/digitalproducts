# Lunacal API Viability Pass

Related issue: DIG-49
Verification timestamp: 2026-05-08T07:32:32Z
Owner: Automation Engineer
Source access ledger: `01-market-research/appsumo/2026-05-08-priority-access-ledger.md`

## Verdict

Lunacal is not ready for a read-only API connector yet.

Current classification: `browser_url_verified_api_not_public`

The useful, evidence-backed conclusion is narrower than the earlier `api_base_unknown` state:

- The public marketing/docs surface is reachable at `https://lunacal.ai/` and `https://help.lunacal.ai/`.
- The authenticated app surface is reachable at `https://app.lunacal.ai/` and redirects anonymous users to `/auth/login`.
- The previously guessed `api.lunacal.ai` hostname still does not resolve.
- Public help docs expose product workflows, webhooks, Zapier, calendars, CRM, payments, and team booking features, but they do not expose a public REST/OpenAPI developer API for API-key reads.
- The app bundle exposes a Next.js/tRPC browser application and internal `/api/*` routes, not a stable documented external API contract.
- The secure runtime contains `LUNACAL_API_KEY`, but safe GET probes did not prove that this key can authenticate to a read-only account API.

Do not treat the current key as invalid. Treat it as `api_key_signal_unmapped`: a key-like value exists, but its issuer, expected header/query shape, and external API base are not documented or verified.

## Evidence checked

### Public DNS and entry points

| Host | Result | Interpretation |
|---|---|---|
| `lunacal.ai` | Resolves and returns HTTP 200 | Current public/booking/marketing surface. |
| `www.lunacal.ai` | Resolves and redirects to `https://lunacal.ai/` | Canonical public host is non-www. |
| `app.lunacal.ai` | Resolves and redirects `/` to `/auth/login` | Current browser app/admin entry path. |
| `api.lunacal.ai` | DNS resolution failed | The prior guessed API host is still not a valid current base. |
| `lunacal.com`, `www.lunacal.com` | Resolve to unrelated/parked-style hosts | Not useful for API discovery. |
| `app.lunacal.com`, `api.lunacal.com` | DNS resolution failed | Not current app/API hosts. |

### Public docs checked

`https://help.lunacal.ai/` is a Mintlify documentation site and publishes `llms.txt` / `llms-full.txt`. The docs list these integration-relevant topics:

- Webhooks
- Zapier integration
- HubSpot integration
- Pipedrive integration
- Stripe and PayPal integrations
- Google Tag Manager / UTM tracking
- calendar, conferencing, messaging, payment, and team settings

No public REST API, OpenAPI document, Swagger document, or API-key authentication guide was found in the reachable docs during this pass.

### API-like routes checked safely

The following were checked with only safe `GET` requests and without printing the raw key:

| Base | Route family | Result |
|---|---|---|
| `https://app.lunacal.ai` and `https://lunacal.ai` | `/api/v1/*`, `/api/v2/*` for `me`, `event-types`, `bookings` | HTTP 404 HTML responses; no public v1/v2 REST API surfaced there. |
| `https://app.lunacal.ai` and `https://lunacal.ai` | `/api/me` | HTTP 409 JSON `Unauthorized` across tested key header shapes; appears session/auth protected, not key-auth verified. |
| `https://app.lunacal.ai` and `https://lunacal.ai` | `/api/auth/session` | HTTP 200 `{}` for anonymous requests; useful only as NextAuth session signal, not account data. |
| `https://app.lunacal.ai` and `https://lunacal.ai` | guessed tRPC route `/api/trpc/viewer.me` | HTTP 404; the app uses browser/tRPC internals but this guess is not a verified public endpoint. |

Tested non-mutating auth shapes: `Authorization: Bearer`, `X-API-KEY`, `api-key`, and raw `Authorization`. None turned the current `LUNACAL_API_KEY` into a verified read-only API credential.

## Safety constraints retained

- No booking, scheduling, calendar, webhook, integration, payment, or team-setting mutations were attempted.
- No raw API key, cookie, password, session token, booking data, or account data was printed or committed.
- No browser login was attempted because no Lunacal browser username/password/session was established in this pass.
- Do not automate internal Next.js/tRPC routes as a production connector unless Lunacal documents them or an authenticated browser-session runbook is explicitly approved.

## Smallest safe next step

Do not add Lunacal to `tools/appsumo_readonly_probe.py` yet. A runnable probe would either hit anonymous/session-only routes or encode undocumented guesses, which would create false confidence.

The next useful handoff is an operator access-completion packet with one of these:

1. official Lunacal developer/API documentation showing base URL, auth header/query shape, and at least one safe account-level read endpoint;
2. confirmation from Lunacal support that `LUNACAL_API_KEY` is for a specific integration and which endpoint consumes it;
3. a human-approved browser login or persisted ops browser session for `https://app.lunacal.ai/auth/login`, plus an explicit read-only scope to inspect account settings/integrations/API-key pages.

If a browser session is supplied, map these read-only surfaces first:

- Bookings: upcoming/past/cancelled/unconfirmed counts only.
- Event types: names/statuses/counts only.
- Integrations/apps: installed app names and connection status only.
- Webhooks/Zapier settings: existence/counts and event types only; do not create/test/delete webhooks.
- Team/workspace settings: workspace/member counts only.
- API key/settings page: whether a documented key/base exists, never the raw key.

## Recommended repo status

- Ledger status: `browser_url_verified_api_not_public`.
- Integration value: medium for scheduling/booking workflows, but currently browser-session or documented-webhook-first rather than API-first.
- n8n readiness: not ready. Prefer Zapier/webhook docs or browser-session runbook after operator access; no disabled n8n workflow should be created until a stable read-only surface is verified.
