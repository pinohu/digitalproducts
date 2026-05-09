# Plerdy access classification

Verification timestamp: 2026-05-08T08:01:03Z
Operator: Browser Operations Lead
Related issue: DIG-51

## Security handling

- Runtime-only credential sources were inspected without copying raw passwords, cookies, session IDs, API keys, or AppSumo redemption codes into this document.
- Sources checked:
  - `C:\Users\ohu00\Downloads\tigertail-product-list-07-05-2026.csv`
  - `C:\Users\ohu00\Documents\SOFTWARE TOOLS LOGIN CREDENTIALS.txt`
  - `C:\Users\ohu00\Documents\.env`
- No Plerdy-specific username/password/API-key material was found in the secure dotenv or credential-file sources.
- Generic credential-pool login probes were performed at runtime only; none authenticated. Raw usernames/passwords and cookies were not stored.
- Browser-cookie/session inspection was not performed, because the shared ChromeOps profile was locked by another running browser process and the fallback Playwright Chromium runtime is missing `libnspr4.so` in this WSL environment.

## Entry path verification

- Public marketing/product path: `https://www.plerdy.com/` returns HTTP 200 and is the canonical host for the public site.
- App login path: `https://a.plerdy.com/login` returns HTTP 200 and renders `Plerdy | Login Form`.
- Canonical login form action: `POST https://a.plerdy.com/auth/login` with form fields `email`, `password`, `_token`, and optional `remember`.
- Public site login link also points to `https://a.plerdy.com/auth/login`.
- `https://app.plerdy.com/` does not resolve in DNS during this pass and should not be treated as the dashboard host.

## Authentication result

Classification: `browser_url_verified_credentials_invalid`

Reasoning:

- Inventory confirms ten redeemed Plerdy code-based AppSumo rows, but redemption/license-code inventory is not a login credential and was not persisted here.
- Secure source inspection found no `PLERDY_*` env/API-key material and no Plerdy-specific credential entry.
- Four available generic credential-pool pairs each posted successfully to the login endpoint at a transport/form level, but each redirected back to `/auth/login`, followed by a login page with no logout/dashboard/authenticated markers.
- No MFA or reCAPTCHA blocker was observed in these HTTP-level probes; the blocker is currently absent/non-matching credentials or absent verified persisted browser session, not a wrong login URL.
- Live tenant/site instrumentation was not verified. Plerdy is therefore not yet a reusable operator surface for this company.

## Highest-value read-only surfaces after access is established

Plerdy is most valuable only after a real owned site is connected and the tracking script is installed by an approved human/site-owner workflow. Once access exists, initial read-only browser workflows should inspect only summary/count/configuration metadata for:

1. Site/project inventory and installed-domain status.
2. Tracking-code/instrumentation health and last-seen activity.
3. Heatmaps and click/scroll depth summaries.
4. User session recordings list and filters, without exporting raw visitor sessions.
5. Conversion funnel configuration and aggregate drop-off reports.
6. Event/goal tracking configuration and aggregate counts.
7. SEO checker/audit alerts and page-level issue counts.
8. Smart forms, popups, NPS, or feedback widgets inventory and status.
9. E-commerce analytics / sales-performance dashboards if an owned store is connected.
10. Integrations, team/account, billing/plan, and data-retention settings in read-only mode.

## Safe first workflows

- Account access readiness check: confirm login, tenant/account identity, plan/license status, and available modules without changing settings.
- Site instrumentation readiness check: list connected site domains, tracking-code status, and whether any site is actively collecting data.
- CRO/UX summary check: collect high-level counts/status for heatmaps, session recordings, funnels, events, forms/popups, and SEO alerts without exporting visitor-level data.

## Do not do without a separate write contract

- Do not install Plerdy scripts on any site or edit site code.
- Do not create/edit popups, forms, surveys, funnels, events, goals, integrations, users, billing, or analytics settings.
- Do not export raw visitor recordings, heatmap datasets, form submissions, personal data, API keys, cookies, or site secrets.
- Do not redeem/change license material or alter account ownership/team access.

## Current unblock requirement

Need either a human-approved Plerdy account credential/session for the correct account or a human-established persisted ops browser session. If the intended value is CRO for the current `digitalproducts` product, also confirm the exact owned site/domain that should be instrumented before any future write/install work is proposed.
