# AppSumo Priority Access Ledger

Verification timestamp: 2026-05-08T01:37:14Z
Operator: Browser Operations Lead
Related issue: DIG-26

## Security handling

- Runtime-only secret sources were inspected but no raw passwords, API keys, license keys, cookies, or tokens are copied into this repo document.
- Source files used:
  - `C:\Users\ohu00\Downloads\tigertail-product-list-07-05-2026.csv`
  - `C:\Users\ohu00\Documents\SOFTWARE TOOLS LOGIN CREDENTIALS.txt`
  - `C:\Users\ohu00\Documents\.env`
- Browser login-page reachability was checked for Brilliant Directories with ChromeOps during the prior pass; DIG-34 subsequently verified authenticated admin access with runtime-only credential handling. Credential values were not pasted into this ledger.

## Summary

This pass confirms that the AppSumo portfolio has strong coverage for the priority operating tools, but actual integration readiness differs sharply by platform:

- Verified API access now exists for `AITable.ai`, `Agiled`, and `Emailit`; the DIG-35 recheck confirmed the prior AITable 401 was caused by environment/source drift, and DIG-39 confirmed Emailit's current API is v2 with bearer auth.
- `Emailit` is no longer just API-reachable: the correct `https://api.emailit.com/v2` base and `Authorization: Bearer` auth shape returned HTTP 200 for multiple safe read-only resources.
- `Late/Zernio`, `Formaloo`, and `Flotiq` are now guarded read-only API surfaces: DIG-66 verified Late/Zernio bearer GET summaries, DIG-67 verified Formaloo token-mint plus GET summaries, and DIG-68 verified Flotiq `X-AUTH-TOKEN` summaries for content-type and media counts.
- `Brilliant Directories` has activated inventory, an explicit secure credential mapping, verified authenticated admin access for `Immigration Smarts`, and visible reusable admin areas; it is now the strongest browser-operated integration candidate.
- `SuiteDash` now has a verified public browser login path, verified Secure API documentation/base, and a real non-secret tenant portal registry from the secure ENV sheet. Eight of eleven portal auth URLs are live branded SuiteDash login pages; Coadjutant, Dome Law, and NAWA need operator/network/tenant repair. Available local `SUITEDASH_*` material is still not sufficient for live tenant/API access because required Public ID values and browser username/password/session are absent from the inspected secure sources.
- `KonnectzIT` now has a verified browser entry path and API base signal, but the available credential pool did not establish access: no tool-specific credentials were found and generic credential pairs returned HTTP 401.
- `Dadan` is no longer blocked by endpoint/TLS uncertainty: DIG-56 found the current app-embedded developer docs at `https://app.dadan.io`, verified the active API base `https://app.dadan.io/api/v1/usedadan`, and confirmed `X-Dadan-API-Key` auth with the runtime key against the GET-only recording-request detail endpoint. It is limited to operator-approved request-code checks; `https://api.dadan.io` remains a bad/525 host.
- `Boost.space` and `Flowlu` have API-key signals and official API docs now confirm tenant-shaped bases, but the current secure sources still lack the required Boost.space system hostname and Flowlu company subdomain; DIG-42 therefore classifies them as tenant/base missing rather than key-invalid. DIG-44 verified `FuseBase` authenticated browser access via the Nimbus/FuseBase login path, DIG-45 upgraded `Certopus` to `api_verified_readonly` after official Swagger confirmed `X-API-KEY` auth and safe GET probes returned HTTP 200, and DIG-48 reclassified `Brizy Cloud` from deferred to `browser_url_verified_credentials_invalid` after verifying its account/admin entry paths but failing to establish access with the available credential pool. DIG-49 narrowed Lunacal from `api_base_unknown` to `browser_url_verified_api_not_public`: `lunacal.ai`, `app.lunacal.ai`, and `help.lunacal.ai` are reachable, `api.lunacal.ai` still does not resolve, public docs expose webhooks/Zapier but no REST/OpenAPI contract, and the current `LUNACAL_API_KEY` did not authenticate any safe guessed read-only API route. DIG-52 narrowed `WbizTool` from `api_signal_unverified` to `credential_pair_incomplete`: docs/base are known, but the current secure source has only `WBIZTOOL_COM_API_KEY` and lacks the required WbizTool `client_id` / `whatsapp_client` pair. DIG-55 narrowed `SMS-iT CRM` from `api_signal_unverified` to `api_docs_and_login_verified_credentials_invalid_or_unmapped`: current login/docs paths are known, but the available API-key material and generic credential pool did not establish read-only access. DIG-58 narrowed `AgenticFlow` from `api_signal_unverified` to `api_auth_verified_project_scope_mismatch`: official docs/CLI confirm `https://api.agenticflow.ai/` with bearer auth, and the current key authenticates through the CLI, but the documented REST `GET /v1/agents/` read with CLI-returned workspace/project context returns HTTP 403 `API key does not have access to this project`. DIG-60 narrowed `Procesio` from `api_signal_unverified` to `api_base_verified_key_name_missing`: public docs and Swagger confirm `https://webapi.procesio.app` with separate `key` + `value` headers, but the current secure runtime has only the API key value and lacks the matching key name/workspace context.

## Priority access table

| Tool | Inventory signal | Secure credential/API signal | Verification performed | Status | Integration value | Blocker / next action |
|---|---:|---|---|---|---|---|
| Brilliant Directories | 5 activated rows | Explicit admin URL + tool-specific username/password mapping in secure credential file; env key names also present | Authenticated admin session established via runtime-only credential handling; active console title observed as `Immigration Smarts Administration Console`; live site domain observed as `find.immigrationsmarts.com` | `browser_admin_verified` | High: directory/site operations and productized business-site demos | Treat as a strong reusable browser-operated surface. Next: create a dedicated persisted ops browser profile and write read-only runbooks for member, content, lead, email, finance, settings, and developer-hub inspection. |
| SuiteDash | 136 redeemed rows | Eleven local `SUITEDASH_*_API_KEY` values present; no matching `X-Public-ID`, browser username/password, or saved session found in inspected secure sources; exact non-secret portal auth URLs now recorded for eleven tenant labels | Official login root `https://app.suitedash.com/` returns `SuiteDash - Login`; Secure API Swagger is reachable at `https://app.suitedash.com/secure-api/swagger/json-file` with server `https://app.suitedash.com/secure-api/` and required headers `X-Public-ID` + `X-Secret-Key`; dummy credentials validate read-only docs behavior; local key-only attempts against `/worlds` returned 401 when paired with guessed public IDs; DIG-63 verified exact portal auth URLs from the secure ENV sheet: 8/11 are live branded SuiteDash login pages (ClickOnPage, Desk Village, instaxis, Naija Clan, notroom, relguard, SitBid, Your Deputy) and 3/11 need repair/recheck (Coadjutant TLS, Dome Law parked/timeout, NAWA TLS/backend) | `tenant_urls_verified_public_auth_mixed_credentials_insufficient` | High: core product-domain evidence, demos, portals, and implementation context | Use only the live exact portal hosts for next human-assisted browser verification. Still need the real SuiteDash Public ID for each secret key and/or a human-approved browser credential/session. Do not use guessed `{slug}.suitedash.com` hosts; confirm or replace Coadjutant, Dome Law, and NAWA before use. |
| KonnectzIT | 20 redeemed rows | No obvious env API key; no tool-specific username/password in inspected secure sources; generic credential-pool attempts were rejected | Login/dashboard path verified at `https://app.konnectzit.com/`; SPA API base identified as `https://api.konnectzit.com`; safe login probes against `/api/v1/auth/login` returned HTTP 401 for available generic credential pairs | `browser_url_verified_credentials_invalid` | High: automation/integration layer | Correct entry path is known, but reusable browser access is not established. Blocker is invalid/non-matching credentials plus no verified persisted session, not missing URL. Need human-approved KonnectzIT account credential/session before mapping live workflows/apps/webhooks. |
| Agiled | 10 rows: 8 redeemed, 2 expired | `AGILED_API_KEY` present | `GET https://app.agiled.app/api/v1/users` with bearer token returned HTTP 200 | `api_verified` | High: CRM/PM/invoicing candidate | Safe next integration: build read-only Hermes/Paperclip connector for users/companies/projects, then decide whether Agiled is worth active workflow use. |
| Boost.space | 6 activated rows | `BOOST_SPACE_API_KEY`; Make Boost.space integrator credentials present; no system hostname found in inspected secure sources | DIG-42 confirmed official OpenAPI schema at `https://apidoc.boost.space/5.2.3.json` / `develop.json`; server is `https://{system}.boost.space/api` with bearer auth. Generic `api.boost.space` paths returned HTTP 404, and `developers.boost.space/api/user` returned HTTP 401 with the available key. | `tenant_base_missing` | High: data sync and record hub | Need the exact Boost.space system URL, for example `https://<system>.boost.space/`, before retrying. Do not treat the key as invalid until a tenant-shaped base is verified. |
| Flowlu | 6 rows: 5 redeemed, 1 expired | `FLOWLU_API_KEY` present; no company/workspace subdomain found in inspected secure sources | DIG-42 confirmed official Flowlu OpenAPI at `https://www.flowlu.com/api/json/openapien.json`; server is `https://{company}.flowlu.com/api/v1/module` and auth is query parameter `api_key`. Generic `www.flowlu.com/api/v1/module` checks returned HTTP 404 even with the key. | `tenant_subdomain_missing` | Medium-high: CRM/finance alternative | Need the exact Flowlu workspace URL, for example `https://<company>.flowlu.com/`, before retrying safe GETs such as CRM accounts, tasks, projects, or invoices in summary-only mode. Do not treat the key as invalid until the tenant-shaped base is verified. |
| FuseBase | 10 redeemed rows | No obvious env API key; no tool-specific credential entry, but one generic credential-pool pair authenticated successfully at runtime; credential values and cookies were not stored | Correct login path verified at `https://app.nimbusweb.me/auth/login` (page title `FuseBase - Login`). `app.fusebase.com` did not resolve; `nimbusweb.me/auth/login` redirects to the same FuseBase/Nimbus app path. Runtime-only login established an authenticated dashboard session and redirected to the tenant dashboard at `https://pinohu.nimbusweb.me/dashboard/u26090/tables/entity/spaces`. The organization-level workspace dashboard showed two workspaces and ready portal surfaces at a high level; no portal/content changes were made. | `browser_workspace_verified` | Medium-high: portals/docs/knowledge delivery | Treat as a viable reusable browser-operated surface in read-only mode. Highest-value first surfaces: organization workspace inventory, client portal inventory/settings, pages/docs/knowledge content, member/client access lists, task boards, database/dashboard tables, forms/responses, e-sign/file surfaces, AI assistant/agent settings, integrations/apps, and billing/security/org settings. Use a dedicated persisted ops browser profile before future browser runbooks; do not invite users, edit portals/pages, change permissions/settings/billing, send magic links, issue e-sign requests, run automations, or export private data without a separate write contract. |
| Brizy Cloud | 10 redeemed rows | No obvious env API key; no Brizy-specific username/password entry found in the inspected secure credential sources | DIG-48 verified the public marketing path, account login path, and Cloud admin sign-in/dashboard path. Runtime-only checks found 10 redeemed code-based inventory rows but no matching Brizy credential material; generic credential-pool pairs did not authenticate against the Brizy account login, and the Cloud admin sign-in requires browser/recaptcha execution before credential validity can be completed. | `browser_url_verified_credentials_invalid` | Medium: landing pages/mini-sites | Correct entry paths are `https://www.brizy.io/account/login` for the Brizy account portal and `https://admin.brizy.io/signin` -> `https://admin.brizy.io/dashboard` for Brizy Cloud admin. Reusable browser access is not established from the current credential pool. Need a human-approved Brizy account credential or dedicated persisted browser session before mapping live projects/sites. |
| Plerdy | 10 redeemed rows | No obvious env/API key; no tool-specific credential entry found in inspected secure sources | DIG-51 verified the canonical public/login paths and attempted runtime-only generic credential-pool authentication; no pair authenticated and no persisted browser session was verified because ChromeOps was profile-locked and fallback Chromium is missing a local shared library | `browser_url_verified_credentials_invalid` | Medium: CRO/user behavior analytics | Correct entry path is `https://a.plerdy.com/login` / `/auth/login`; `app.plerdy.com` does not resolve. Need a human-approved Plerdy account credential/session and an approved owned site/domain before mapping live analytics, heatmaps, session recordings, SEO, popups/forms, funnels, events, or instrumentation status. |
| Press Ranger | 10 redeemed rows | No obvious env API key; no Press Ranger-specific credential entry, but existing generic credential-pool material authenticated successfully at runtime | DIG-50 verified the public/login/dashboard path and authenticated dashboard access using runtime-only credential handling. Correct paths are `https://pressranger.com/`, `/login`, and `/dashboard`. Read-only navigation confirmed dashboard, journalist/podcast/publisher databases, campaigns, press releases, settings, team, companies, and billing surfaces; raw credentials, cookies, media lists, contacts, campaign data, and billing details were not stored. | `browser_dashboard_verified_readonly` | Medium: PR/outreach and launch publicity workflow | Treat as a viable browser-operated read-only surface. First safe workflows: account readiness, campaign/press-release inventory summary, and media discovery capability checks. Do not create campaigns/releases, mark media relationships, add lists/companies/team members, send/publish/distribute, upgrade/redeem, export media/contact data, or alter settings without a separate write contract. |
| Certopus | 10 redeemed rows | `CERTOPUS_API_KEY` present in secure operator dotenv; not in `tools/.env` | DIG-45 confirmed official Swagger at `https://api.certopus.com/` with `X-API-KEY` header auth. Runtime GET probes returned HTTP 200 for `/v1/templates`, `/v1/organisations`, `/v1/wallet`, and `/v1/smtp`; raw template/recipient/branding data was not stored. | `api_verified_readonly` | Medium: certificates/completion workflows | Safe next integration: disabled/manual-first health summary for template/category counts, organisation count/integration flag, wallet count, and SMTP presence only. No certificate issuance, sends, downloads, recipient writes/deletes, SMTP/domain/white-label changes, or exports without a separate write contract. |
| CallScaler | 9 rows: 7 redeemed, 2 expired | `CALLSCALER_API_KEY` and `_1` present in secure operator dotenv; not in `tools/.env` | DIG-64 loaded both secure keys runtime-only and ran minimal safe GET probes against `https://callscaler.com/api/v1/` with bearer auth; `/calls?limit=1`, `/dashboard/stats`, and `/numbers?limit=1` all returned HTTP 401 `unauthorized` for both keys, with no raw call data stored | `api_base_verified_credentials_invalid_or_unscoped` | Medium-low: phone attribution | Need operator to verify/rotate a real CallScaler API key from `https://v3.callscaler.com/app/settings?tab=api-keys` or provide an approved browser session. Do not add to n8n or fetch call records/recordings/transcripts/phone numbers until access is corrected and privacy scope is approved. |
| Lunacal | 1 activated row | `LUNACAL_API_KEY` present in secure operator dotenv; not in `tools/.env` | DIG-49 verified `https://lunacal.ai/`, `https://app.lunacal.ai/auth/login`, and `https://help.lunacal.ai/`; `api.lunacal.ai` still does not resolve. Public docs expose webhooks/Zapier/integrations but no REST/OpenAPI/API-key guide. Safe GET probes to guessed `/api/v1`, `/api/v2`, `/api/me`, and tRPC routes with bearer, `X-API-KEY`, `api-key`, and raw authorization shapes did not authenticate account reads; `/api/auth/session` only returns anonymous `{}`. | `browser_url_verified_api_not_public` | Medium: scheduling/booking | Do not add to n8n/probe yet. Need official API docs/support confirmation for the key, or a human-approved browser session for `app.lunacal.ai` plus read-only inspection of bookings/events/integrations/webhooks/API-key settings. |
| Emailit | 1 activated row | Multiple `EMAILIT_API_KEY*` env names in secure operator dotenv | DIG-39 confirmed docs + live GET-only v2 probes: `https://api.emailit.com/v2` with `Authorization: Bearer`; `GET /templates`, `/domains`, `/emails`, `/contacts`, `/audiences`, `/suppressions`, `/webhooks`, `/api-keys`, and `/events` returned HTTP 200 in summary-only checks | `api_verified_readonly` | Medium-high if transactional email is needed | Safe next integration: add a disabled/manual n8n health check for domains/events/templates using a dedicated automation-owned key. Do not send email, mutate domains/DNS, publish templates, or alter contacts/suppressions without a separate write contract. |
| Late/Zernio | 1 activated row | `GETLATE_DEV_API_KEY` present in secure operator dotenv; not in `tools/.env` | DIG-66 confirmed docs have rebranded from Late to Zernio and verified bearer-auth GET-only probes against both `https://getlate.dev/api/v1` and `https://zernio.com/api/v1`; `profiles`, `accounts`, `accounts/health`, `posts?limit=1`, `usage-stats`, and `users` returned HTTP 200 in summary-only checks | `api_verified_readonly` | Medium-high: social publishing/account readiness health | Safe next integration: disabled/manual-first n8n health digest for profiles/accounts/account-health/posts/usage/users using summary-only output and a dedicated automation key. Do not create/schedule/publish/edit/delete posts, connect/disconnect social accounts, handle inbox/comments/DMs, mutate webhooks/users/API keys/settings, or export raw handles/profile URLs/post/user data without a separate write contract. |
| SMS-iT CRM | 1 activated row | `SMS_IT_API_KEY*` present; no SMS-iT-specific browser username/password mapping in checked credential source | DIG-55 verified current entry paths and attempted runtime-only read-only auth checks. Marketing root is `https://www.smsit.ai/`; browser login is `https://aicpanel.smsit.ai/login`; `https://api.smsit.ai/` redirects to the Stoplight docs workspace at `https://smsit.stoplight.io/`; `https://app.smsit.ai/` is an empty index and should not be used as the CRM dashboard. Safe API-key probes against `https://aicpanel.smsit.ai/api/user` with bearer, `X-API-KEY`, `api-key`, and raw authorization shapes returned HTTP 401, and approved generic browser credential-pool probes did not establish a session before 403/429 throttling. Detailed handoff: `00-foundation/operator-system/browser-runbooks/smsit-access-classification.md` | `api_docs_and_login_verified_credentials_invalid_or_unmapped` | Medium: messaging/CRM | Need a human-approved SMS-iT browser session/credential or confirmation of the key's exact issuing context: base URL, workspace/account identifier if required, auth shape, and one safe read-only endpoint. Do not add to n8n/Paperclip connectors yet; no messaging, campaign, contact, automation, or billing writes. |
| WbizTool | 1 activated row | `WBIZTOOL_COM_API_KEY` present; no WbizTool-specific `client_id` or `whatsapp_client` found in checked secure env names | DIG-52 confirmed official docs/base at `https://wbiztool.com/api/v1/`; documented auth requires body fields `client_id` + `api_key`, with `whatsapp_client` required for report/history and send surfaces. A data-minimized key-only `POST /whatsapp-client/list/` probe returned JSON `status: 0` / `Auth Error` and no client list. | `credential_pair_incomplete` | Medium: WhatsApp operations | Need operator-provided WbizTool client ID and, for any report/history checks, WhatsApp client ID. Do not add to GET-only probe or n8n yet because WbizTool uses POST for read-like endpoints and can expose phone/message data. No sends, scheduling, cancellation, phone verification, media handling, group sends, or message-history exports without a separate write contract. |
| AgenticFlow | 1 activated row | AgenticFlow API-key material present in secure operator dotenv; not in `tools/.env` | DIG-58 verified official docs/CLI: current REST base is `https://api.agenticflow.ai/`, auth is `Authorization: Bearer`, and the documented lowest-risk read is project-scoped `GET /v1/agents/?workspace_id=...&project_id=...&limit=1`. Runtime CLI check with the key exported as `AGENTICFLOW_API_KEY` reported key present and exposed workspace/project context, but the documented REST read with that context returned HTTP 403 `API key does not have access to this project`. | `api_auth_verified_project_scope_mismatch` | Experimental | Need the correct project-scoped AgenticFlow API key/context, ideally as a dedicated `AGENTICFLOW_API_KEY_AUTOMATION`. A guarded `agenticflow agents` GET-only probe exists, but run it only summary-only with `--workspace-id` and `--project-id` after scope is corrected. Do not create/run agents, workflows, workforces, prompts, MCP connections, or webhooks without a separate write contract. |
| AITable.ai | 1 activated row | `AITABLE_API_KEY` present | DIG-35 recheck: `GET /spaces` returned HTTP 200 from the secure operator dotenv; `GET /spaces/{space_id}/nodes` and `GET /datasheets/{datasheet_id}/records` also returned HTTP 200 | `api_verified_readonly` | Medium-high: structured operational tables/apps | Access is working when the current key is loaded from the secure operator dotenv (for example via `--env-file /mnt/c/Users/ohu00/Documents/.env`). Keep read-only and data-minimized; do not promote writes without a separate contract/rollback issue. |
| Procesio | 1 activated row | `PROCESIO_API_KEY` value present in secure operator dotenv; no matching API key name or approved workspace header found | DIG-60 verified public docs and live Swagger/OpenAPI at `https://webapi.procesio.app/swagger/v1.19/swagger.json`; Web API auth requires separate `key` + `value` headers. Safe GET auth-shape probes against `/api/Users/me`, `/api/Workspaces`, `/api/Projects/count`, and `/api/Projects` narrowed the blocker: bearer/value-only auth returned 407, while guessed `key: PROCESIO_API_KEY` + value returned 401. | `api_base_verified_key_name_missing` | Experimental workflow layer | Need the exact Procesio API key name paired with the current `PROCESIO_API_KEY` value, plus approved workspace context. Then run only `users-me`, `workspaces`, `projects-count`, and optionally one summary-only `projects` page. Do not run projects or mutate workflows/webhooks/schedules/credentials/workspace settings without a separate write/execute contract. |
| Dadan | 1 activated row | `DADAN_API_KEY` present in secure operator dotenv; not in `tools/.env` | DIG-56 verified app-embedded developer docs and active API base `https://app.dadan.io/api/v1/usedadan` with `X-Dadan-API-Key`. Missing/invalid/valid-key-wrong-request probes returned distinct 401s; `https://api.dadan.io` still returns HTTP 525 and is not the current connector base. | `api_verified_limited_readonly` | Medium-low: demos/walkthroughs and external recording requests | Safe next step is only `GET /requestrecording/{RequestCode}` for an operator-approved request code created by the same key, using summary-only output. Do not create recording requests, upload/share videos, change webhooks/developer settings, or expose request/video/submission data without a separate write contract. |

## Recommended Hermes/Paperclip integration order

1. `Agiled` connector spike: already returns authenticated HTTP 200. Start read-only against users/companies/projects and map whether it can support product operations without replacing SuiteDash.
2. `AITable.ai` connector spike: read-only access is verified when using the current secure operator dotenv. Safe next step is a data-minimized n8n read-only sync against selected datasheets; do not write until a separate issue defines fields, rollback, and automation-owned credentials.
3. `Brilliant Directories` browser-operated surface: authenticated admin access is now verified for `Immigration Smarts` / `find.immigrationsmarts.com`. Build a secure persisted-session/runbook workflow before any writes, with read-only inspection coverage across members, content, interactions/leads, finance, emails, toolbox, settings, and developer hub.
4. `SuiteDash` credential completion: API base and login path are known (`https://app.suitedash.com/` and `https://app.suitedash.com/secure-api/`), but the local secure sources lack the required Public ID/header pair and browser login credential/session. Obtain the Public ID values from an admin logged into Integrations > Secure API, or have a human establish a dedicated ops browser session before attempting tenant reads.
5. `Emailit` read-only health connector: DIG-39 verified v2 bearer-auth GETs for domains, events, templates, and related resources. Promote only as a disabled/manual-first n8n health check with data-minimized summaries and a dedicated automation-owned key; no sends or contact/domain/template mutations without a separate write contract.
6. `Late/Zernio` read-only health connector: DIG-66 verified bearer-auth GETs for profiles, accounts, account health, posts, usage stats, and users. Promote only as a disabled/manual-first n8n health digest with data-minimized summaries and a dedicated automation-owned key; no post creation/scheduling/publishing, social-account changes, inbox/comment/DM handling, webhook/user/API-key/settings mutations, or raw profile/account/post/user exports without a separate write contract.
7. `Boost.space` / `Flowlu` tenant-base completion: DIG-42 confirmed both official API shapes but also confirmed the required tenant bases are missing. Obtain the exact Boost.space system URL and Flowlu company URL before any connector work; then use `tools/appsumo_readonly_probe.py` with `--base-url` and `--summary-only --json` for the first safe GET.
8. `Certopus` read-only health connector: DIG-45 verified the official `https://api.certopus.com` base with `X-API-KEY` auth and safe GETs for templates, organisations, wallet, and SMTP. Promote only as a disabled/manual-first metadata/count summary; no certificate issuance, sends, downloads, recipient mutations, SMTP/domain/white-label changes, or exports without a separate write contract.
9. `FuseBase` browser-operated surface: DIG-44 verified login at `https://app.nimbusweb.me/auth/login` and authenticated dashboard access for the `pinohu` organization. Treat as a viable read-only surface for portals/docs/knowledge delivery, but use a dedicated persisted ops browser profile/session before formal runbooks.
10. `Lunacal` access completion: DIG-49 verified the browser app and help/docs surfaces but found no public REST/OpenAPI API-key contract, and `LUNACAL_API_KEY` did not authenticate any safe guessed read-only route. Treat it as browser-session/webhook-first until official API docs/support confirmation or a human-approved browser session exists.
11. `KonnectzIT` credential/session completion: login URL and SPA API base are now known (`https://app.konnectzit.com/` and `https://api.konnectzit.com`), but no reusable authenticated browser surface is available from the inspected credential pool. The exact operator packet is `01-market-research/appsumo/konnectzit-access-completion-packet.md`; obtain a human-approved account credential or establish a dedicated ops browser session, then map workflows/apps/webhooks read-only before any automation changes.
12. `Press Ranger` browser-operated surface: DIG-50 verified authenticated dashboard access at `https://pressranger.com/dashboard` using runtime-only credential handling. Treat it as a viable read-only PR/outreach surface for account readiness, media database capability checks, and campaign/press-release inventory summaries; avoid contact/media exports and all outreach/distribution/settings writes without a separate contract.
13. `Dadan` limited recording-request detail check: DIG-56 verified `https://app.dadan.io/api/v1/usedadan` with `X-Dadan-API-Key` and added a guarded GET-only probe resource. Promote only after an operator supplies a non-sensitive request code created by the same key plus field-level approval for summary output. Do not automate request creation, uploads, sharing, webhooks, or raw submission/video exports without a separate write contract.
14. `Plerdy` is now classified by DIG-51 as `browser_url_verified_credentials_invalid`: the correct login path is known, but no current credential/session establishes access. Treat it as a later CRO/browser surface only after a human-approved Plerdy credential/session and exact owned site/domain are available. Brizy Cloud's DIG-48 pass found the correct entry paths but did not establish reusable access from the current credential pool.
15. `WbizTool` access completion: DIG-52 confirmed `https://wbiztool.com/api/v1/` and request-body `client_id` + `api_key` auth, with `whatsapp_client` required for report/history. Current secure sources only expose `WBIZTOOL_COM_API_KEY`, so obtain `WBIZTOOL_CLIENT_ID` and `WBIZTOOL_WHATSAPP_CLIENT_ID` before any manual-first, redacted status check. Do not add it to the GET-only probe or n8n until a read-like-POST safety wrapper exists.
16. `Procesio` access completion: DIG-60 verified `https://webapi.procesio.app` and `key` + `value` API-key headers, but current secure sources expose only the key value. Obtain the exact API key name and approved workspace header before running guarded `procesio users-me`, `workspaces`, or `projects-count` checks in summary-only mode. Do not run processes or mutate workflows/webhooks/credentials/schedules/workspace settings without a separate write/execute contract.
17. `CallScaler` access correction: DIG-64 verified the API base and confirmed secure dotenv key names exist, but both available keys return HTTP 401 on the smallest safe reads. Ask the operator to verify/rotate a real CallScaler API key from the v3 settings page or provide an approved browser session before any connector/n8n work; keep all call data, phone numbers, recordings, transcripts, exports, number provisioning, call-flow edits, webhook changes, and billing surfaces out of scope until a separate privacy/write contract exists.

## Brilliant Directories authenticated access pass (DIG-34)

Verification timestamp: 2026-05-08T02:41:55Z

- Authenticated admin access was established using runtime-only credentials from the secure local credential source. No raw password, cookie, API key, or screenshot of secrets was added to the repo.
- Active tenant/site observed after login: `Immigration Smarts`.
- Admin console title observed: `Immigration Smarts Administration Console`.
- Public/live site domain observed: `find.immigrationsmarts.com`.
- Session result: login redirected to `/admin/index.php` and set normal admin/session cookies at runtime only; cookies were not persisted into repo documentation.
- Highest-value reusable operator areas visible from the admin navigation:
  - Website/account switching and support tickets: `websiteDashboard.php`.
  - Dashboard and add-on/activity overview: `index.php`, `addonStatus.php`, `websiteActivity.php`.
  - Members and taxonomy: `viewMembers.php`, `websiteServices.php`, smart lists/tags, images, imports, business data.
  - Content and SEO: `contentManage.php`, post settings, SEO templates, media manager, web page builder.
  - Interactions: member leads, member reviews, post comments, private chats.
  - Finance: membership plans, billing history, subscriptions, coupon codes, payment settings, offers.
  - Email/forms: forms inbox, email outbox, compose email, email templates, newsletters, email accounts, contacts.
  - Toolbox/site operations: widget manager, sidebar manager, menu manager, form manager, sitemap generator.
  - Settings/developer surface: general/design settings, domain manager, admin accounts, text labels, advanced settings, developer hub.
- Integration recommendation: worth integrating as a browser-operated Hermes/Paperclip surface, initially read-only. The operator model should use a dedicated persisted browser profile/session and narrowly scoped runbooks that inspect pages and collect non-secret metadata before any write workflow is considered.
- Constraints retained: do not publish changes, alter billing/payment/admin settings, export private member data, or store credentials/cookies. Treat finance, payment settings, admin accounts, advanced settings, developer hub, and email-sending surfaces as read-only unless a future issue explicitly authorizes a safe mutation.

## AITable DIG-35 reconciliation pass

Verification timestamp: 2026-05-08T03:12:56Z
Related issue: DIG-35

- The current secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env` contains `AITABLE_API_KEY`; `tools/.env` does not. The key value was not printed or copied.
- With that explicit dotenv loaded, `GET /fusion/v1/spaces` returned HTTP 200 against all tested host variants: `https://aitable.ai/fusion/v1`, `https://api.aitable.ai/fusion/v1`, `https://apitable.com/fusion/v1`, and `https://api.apitable.com/fusion/v1`.
- The default `https://aitable.ai/fusion/v1` base is therefore acceptable for the current tool; the likely root cause of the earlier 401 was credential source/token drift rather than the API host.
- Two admin spaces were visible by name only: `nawa automation space` and `Hoang's Space`.
- Beyond `GET /spaces`, read-only pulls also returned HTTP 200 for:
  - `GET /spaces/spcjbFvCoF57M/nodes`, returning multiple folder/datasheet nodes.
  - `GET /spaces/spcg79VTfrMgs/nodes`, returning one datasheet node.
  - `GET /datasheets/dstHEhlAmeChAWQ5En/records`, returning a visible test/empty-fields record.
  - `GET /datasheets/dstlPn0Bty73sfLjJJ/records`, returning one AppSumo inventory-style record.
- The connector output remains redacted for secret-shaped fields, but datasheet records can contain operational/business data. Future runs should use `--page-size 1` for smoke checks and summarize counts/field names before committing any output.

## SuiteDash access classification pass (DIG-38)

Verification timestamp: 2026-05-08T04:19:23Z
Related issue: DIG-38
Access-completion handoff: `01-market-research/appsumo/suitedash-access-completion-packet.md` (DIG-41)

- Secure source inventory found eleven `SUITEDASH_*_API_KEY` values in `/mnt/c/Users/ohu00/Documents/.env`; no raw keys were printed or copied. `tools/.env` and `tools/.env.example` do not carry SuiteDash credentials.
- The AppSumo inventory still shows 136 redeemed SuiteDash rows, but the export does not include tenant URLs or browser login credentials beyond license-code inventory.
- The generic browser login path is verified at `https://app.suitedash.com/`; it returns the public login page titled `SuiteDash - Login` with email/password inputs. Browser automation could not establish an authenticated session because no matching username/password/session was present in the inspected secure sources, and the local ChromeOps/Playwright browser stack was unavailable in this WSL run.
- The Secure API base is verified from official live Swagger: `https://app.suitedash.com/secure-api/`. The documented authentication shape requires both `X-Public-ID` and `X-Secret-Key`; the local `SUITEDASH_*_API_KEY` values correspond only to secret-key-shaped material.
- Dummy SuiteDash API credentials from the public documentation returned successful read responses for dummy-allowed endpoints such as `/contact/meta` and `/companies`, confirming the base/auth shape without touching live tenant data.
- Live attempts using each local SuiteDash secret with absent or guessed public IDs returned 401 responses. Guessed public IDs derived from env names are therefore not valid, and key-only access is insufficient.
- Guessed tenant hostnames derived from env names, for example `{slug}.suitedash.com`, did not resolve in DNS. No tenant-specific browser URL was verified from the available sources.
- Classification: `api_base_verified_credentials_insufficient`. SuiteDash is not yet a reusable live browser/API operator surface. The blocker is key-scope/header mismatch plus missing tenant/browser access, not an unknown API base.
- Highest-value read-only operator surfaces once access is completed: Contacts/Companies CRM, Projects, Worlds/LMS if active, Forms/Data, Client Management/Portals, File Sharing, Calendar/Scheduling, Documents/eSigning, Email Marketing/Communication, Automations, Support Tickets, Office/Subscriptions, Integrations > Secure API usage/limits, and account/white-label settings. Finance, settings, staff/admin, email sending, automations, and API writes should remain read-only unless a future issue explicitly authorizes safe mutation.

## SuiteDash tenant portal registry refresh (DIG-63)

Verification timestamp: 2026-05-08T10:11:19Z
Related issue: DIG-63
Access-completion handoff: `01-market-research/appsumo/suitedash-access-completion-packet.md`

- A secure Google Drive ENV sheet was reviewed outside the repo and supplied exact non-secret SuiteDash portal authentication URLs for eleven existing tenant labels. No Public ID values, Secret Keys, API keys, passwords, cookies, sessions, or license codes were copied into repo output.
- Public unauthenticated `curl -L` checks against `/integrations/publicApi?t=authentication` found eight live branded SuiteDash login pages: ClickOnPage, Desk Village, instaxis, Naija Clan, notroom, relguard, SitBid, and Your Deputy. Each returned HTTP 200 and redirected to `/site/login` with a tenant-branded `*- Login` title.
- Three exact hosts are recorded but not currently useful for verification from this network: Coadjutant returned HTTPS TLS `wrong version number` and HTTP was intercepted by a network warning, Dome Law HTTPS timed out while HTTP redirected to a parked-domain sale page, and NAWA failed strict TLS certificate validation and returned 502 even with insecure TLS.
- Classification changed from `api_base_verified_credentials_insufficient` to `tenant_urls_verified_public_auth_mixed_credentials_insufficient`: tenant URL discovery is no longer the primary blocker for the eight live portals, but live access still requires a human-approved browser session/credential or the correct `X-Public-ID` + `X-Secret-Key` mapping.
- Next safe verification should choose one operator-approved live portal, use a human-established/persisted session or runtime credential entry, and record only page title/navigation labels. Do not try the three failing hosts until the operator confirms current DNS/TLS/backend state.

## Emailit read-only endpoint follow-up (DIG-39)

Verification timestamp: 2026-05-08T04:45:00Z
Related issue: DIG-39
Detailed handoff: `automation/emailit-readonly-endpoint-followup.md`

- Public docs confirmed Emailit API v2 is the current REST API and API v1 is deprecated. Correct base: `https://api.emailit.com/v2`.
- Correct auth shape is `Authorization: Bearer <api_key>`.
- Secure source inventory found `EMAILIT_API_KEY`, `EMAILIT_API_KEY_1`, `EMAILIT_API_KEY_2`, and `EMAILIT_API_KEY_FOR_AILUROPHOBIA`; no raw keys were printed or copied.
- All four runtime key names returned HTTP 200 for a safe `GET /domains?limit=1` probe.
- The default key returned HTTP 200 in `--summary-only --json` checks for `GET /templates`, `/domains`, `/emails`, `/contacts`, `/audiences`, `/suppressions`, `/webhooks`, `/api-keys`, and `/events`.
- Classification: `api_verified_readonly`. Emailit is viable for a disabled/manual-first read-only health connector. Future send/contact/domain/template/webhook writes require a separate issue, a dedicated automation key, idempotency, test-recipient policy, and rollback/audit plan.

## KonnectzIT access classification pass (DIG-43)

Verification timestamp: 2026-05-08T05:20:08Z
Related issue: DIG-43
Access-completion handoff: `01-market-research/appsumo/konnectzit-access-completion-packet.md` (DIG-62)

- Inventory source confirms 20 redeemed KonnectzIT AppSumo code-based rows. License/code values were treated as secret-like redemption material and were not copied into this ledger.
- Secure source inspection found no `KONNECTZIT_*` env/API key material and no tool-specific KonnectzIT username/password entry in the inspected credential file.
- Correct browser entry path is verified: `https://app.konnectzit.com/` and `https://app.konnectzit.com/login` return the KonnectzIT single-page app. Public marketing/root URL `https://konnectzit.com/` is reachable. `www.konnectzit.com`, `panel.konnectzit.com`, and `dashboard.konnectzit.com` did not resolve during this pass.
- SPA asset inspection identifies the live API base as `https://api.konnectzit.com` and the login route as `POST /api/v1/auth/login`. Other route/API signals visible from the unauthenticated app include `/dashboard`, `/apps`, `/app_events`, widget reads, signup, password reset, and account/user-profile endpoints.
- Safe runtime-only login probes using the available generic credential-pool pairs returned HTTP 401 from `https://api.konnectzit.com/api/v1/auth/login`. No token, account, tenant, workspace, workflow, webhook, app-connection, or dashboard surface was reached.
- Browser automation note: ChromeOps/browser profile access was unavailable in this run because the shared ops profile was already locked by another live ChromeOps process, and the alternate Playwright browser stack was missing a Chromium runtime library. The API-level login probes still establish that the currently available credential pairs do not authenticate.
- Classification: `browser_url_verified_credentials_invalid`. The blocker is no valid/non-matching credential or verified persisted session, not missing login URL. It is not an MFA/session-only classification yet, because no valid first-factor login was observed.
- Highest-value read-only operator surfaces to map after human-approved access is established: workflow/zap inventory, app connection catalog, webhook/API trigger settings, task/history logs, account plan/limits, app-event catalog, integrations/apps list, and billing/subscription overview. Do not create/edit workflows, alter webhooks, rotate API credentials, change connected app accounts, or run automations without a separate write contract.

## Boost.space and Flowlu API viability pass (DIG-42)

Verification timestamp: 2026-05-08T05:33:00Z
Related issue: DIG-42
Detailed handoff: `automation/boost-flowlu-api-viability.md`

- Secure source inventory found `BOOST_SPACE_API_KEY`, Make/Boost.space integrator variables, and `FLOWLU_API_KEY`; no raw keys or AppSumo license codes were printed or copied. `tools/.env` does not carry these keys.
- Boost.space official OpenAPI schemas are reachable at `https://apidoc.boost.space/5.2.3.json` and `https://apidoc.boost.space/develop.json`. The documented server is `https://{system}.boost.space/api` and auth is bearer-token based.
- Boost.space generic/non-tenant probes using the available runtime key returned HTTP 404 for `https://api.boost.space/`, `/v1/modules`, and `/api/modules`; `https://developers.boost.space/api/user` returned HTTP 401 `Token does not exists.` No tenant-shaped probe was attempted because no verified `{system}` hostname exists in the inspected sources.
- Flowlu official OpenAPI is reachable at `https://www.flowlu.com/api/json/openapien.json`. The documented server is `https://{company}.flowlu.com/api/v1/module` and auth is query parameter `api_key`.
- Flowlu generic host probes using the available runtime key returned HTTP 404 for `https://www.flowlu.com/api/v1/module` and `/crm/account/list`; no tenant-shaped probe was attempted because no verified `{company}` subdomain exists in the inspected sources.
- Classifications: Boost.space is `tenant_base_missing`; Flowlu is `tenant_subdomain_missing`. Neither is connector-ready, and neither key should be declared invalid until an operator supplies the exact tenant URL and approves the first read-only resource.
- `tools/appsumo_readonly_probe.py` now includes `boostspace` and `flowlu` configs that require `--base-url` before any HTTP request, preventing future tenant guesses or known-wrong generic-base retries.

## FuseBase browser access classification pass (DIG-44)

Verification timestamp: 2026-05-08T06:12:00Z
Related issue: DIG-44

- Inventory source confirms 10 redeemed FuseBase AppSumo rows. AppSumo license/code values were treated as secret-like redemption material and were not copied into this ledger.
- Secure source inspection found no `FUSEBASE_*`, `NIMBUS_*`, or tool-specific FuseBase credential/API key material in the inspected secure dotenv/credential sources. One generic credential-pool pair authenticated successfully at runtime; the other generic pairs did not. Raw usernames, passwords, cookies, and session IDs were not stored.
- Correct browser entry path is verified: `https://app.nimbusweb.me/auth/login` returns the FuseBase login page titled `FuseBase - Login`. `https://nimbusweb.me/auth/login` redirects to the same app path. `https://app.fusebase.com` did not resolve during this pass, so the reusable login path should remain the Nimbus/FuseBase app URL.
- Runtime-only login returned authenticated session markers and normal auth cookies, then read-only dashboard navigation redirected to `https://pinohu.nimbusweb.me/dashboard/u26090/tables/entity/spaces` with title `Dashboard`. No credentials/cookies were persisted into repo documentation.
- Verified tenant/workspace at a high level: organization `pinohu` on `pinohu.nimbusweb.me`; the organization workspaces dashboard showed two workspaces and ready portal surfaces. This is sufficient to classify FuseBase as a viable browser-operated surface without deep content inspection.
- Highest-value reusable operator surfaces visible from the dashboard bundle/routes and first authenticated page: organization workspace inventory, workspace settings, client portal inventory/settings/editor, pages/docs/knowledge content, member/client/group access management, task boards, database/dashboard tables, forms/responses, files/e-sign surfaces, AI assistant/agent settings, integrations/apps, billing, security, and organization settings.
- Classification: `browser_workspace_verified`. Recommended operating model is read-only first with a dedicated persisted ops browser profile/session and narrowly scoped runbooks. Do not invite users, edit portals/pages/docs, change permissions/settings/billing/security, send magic links or invitations, issue e-sign requests, run automations, mutate integrations/apps, export private data, or store cookies/session material without a separate write contract.

## Certopus read-only endpoint follow-up (DIG-45)

Verification timestamp: 2026-05-08T05:52:58Z
Related issue: DIG-45
Detailed handoff: `automation/certopus-readonly-endpoint-followup.md`

- Official Swagger UI is reachable at `https://api.certopus.com/` and embeds the `Certopus API` Swagger spec.
- Documented API base/auth shape: `https://api.certopus.com` with `X-API-KEY` header auth.
- Secure source inventory found `CERTOPUS_API_KEY` in `/mnt/c/Users/ohu00/Documents/.env`; `tools/.env` does not include it. No raw key was printed or copied.
- Runtime-only GET probes with the secure key returned HTTP 200 for `/v1/templates`, `/v1/organisations`, `/v1/wallet`, and `/v1/smtp`.
- Data-minimized observations: templates returned grouped category counts; organisations returned two visible records; wallet returned zero visible certificate records; SMTP returned `empty`. Raw template payloads, branding assets, recipient/certificate details, exports, and SMTP details were not stored.
- Classification: `api_verified_readonly`. Certopus is viable for a disabled/manual-first health connector over metadata/count summaries only. Certificate issuance, email sends, downloads/exports, recipient imports/deletes, SMTP/domain/white-label changes, wallet mutations, and n8n activation require a separate write contract and automation-owned credential.

## Brizy Cloud browser access classification pass (DIG-48)

Verification timestamp: 2026-05-08T06:55:34Z
Related issue: DIG-48

- Inventory source confirms 10 redeemed Brizy Cloud code-based rows. AppSumo redemption/license values were treated as secret-like material and were not copied into this ledger.
- Secure source inspection found no `BRIZY_*` env/API key material and no Brizy-specific username/password entry in the inspected credential sources. No raw passwords, cookies, API keys, or session tokens were stored.
- Correct public/product path is verified at `https://www.brizy.io/cloud`; `https://www.brizy.cloud/` redirects there.
- Correct Brizy account login path is verified at `https://www.brizy.io/account/login` with page title `Please login | Brizy`.
- Correct Brizy Cloud admin entry path is verified at `https://admin.brizy.io/signin` with page title `Brizy Cloud Admin`; after successful sign-in the JavaScript flow redirects to `https://admin.brizy.io/dashboard`. Unauthenticated dashboard requests redirect to the Cloud main-page proxy/marketing path.
- Runtime-only credential checks using the available generic credential-pool pairs did not authenticate against the Brizy account login path; each attempt remained on the login page. The Cloud admin sign-in endpoint also requires browser-side reCAPTCHA enterprise execution, so a clean credential validity result for that surface needs a functioning browser session or human-approved persisted session.
- Browser automation note: ChromeOps could not be opened because the shared ops profile was already locked by another ChromeOps process, and the alternate browser stack still lacks the local Chromium shared library needed to launch. No browser session/cookie inspection was performed.
- Classification: `browser_url_verified_credentials_invalid`. The blocker is not missing URL or tenant ambiguity; reusable access is blocked by absent Brizy-specific credentials plus non-authenticating generic credential pairs, with Cloud admin reCAPTCHA making a persisted/human-approved browser session the next safe path.
- Highest-value read-only operator surfaces to map after human-approved access is established: project/site inventory, published/staging URL list, page/template/library inventory, workspace/team/account settings, form/submission surfaces, lead/contact integrations, domain/publishing settings, billing/plan/license status, and e-commerce/membership features if active. Do not create/edit/publish pages, change domains/DNS, alter integrations/forms/billing/team settings, export private leads/submissions, or redeem/change license material without a separate write contract.

## Lunacal API viability pass (DIG-49)

Verification timestamp: 2026-05-08T07:32:32Z
Related issue: DIG-49
Detailed handoff: `automation/lunacal-api-viability.md`

- Secure source inspection found `LUNACAL_API_KEY` in `/mnt/c/Users/ohu00/Documents/.env`; `tools/.env` does not include it. The raw key was not printed or copied.
- Public surfaces are verified: `https://lunacal.ai/` returns HTTP 200, `https://app.lunacal.ai/` redirects anonymous users to `/auth/login`, and `https://help.lunacal.ai/` publishes reachable Mintlify docs plus `llms.txt` / `llms-full.txt`.
- `api.lunacal.ai` still does not resolve, so the earlier guessed API base is not valid.
- Public docs cover webhooks, Zapier, calendars, CRM integrations, payments, UTM tracking, and team booking workflows, but no public REST/OpenAPI/Swagger API-key contract was found.
- Safe runtime-only GET probes using the available key against guessed REST/tRPC routes did not authenticate any account read. `/api/v1/*` and `/api/v2/*` guesses returned 404, `/api/me` returned 409 Unauthorized, and `/api/auth/session` returned anonymous `{}`.
- Classification: `browser_url_verified_api_not_public`. Lunacal should not be added to `tools/appsumo_readonly_probe.py` or n8n yet. The next step is official API docs/support confirmation for the key, or a human-approved browser session for read-only inspection of bookings, event types, integrations, webhooks, workspace/team settings, and any API-key/settings page.

## Press Ranger browser access classification pass (DIG-50)

Verification timestamp: 2026-05-08T07:33:01Z
Related issue: DIG-50
Detailed handoff: `00-foundation/operator-system/browser-runbooks/press-ranger-readonly-pack.md`

- Inventory source confirms 10 redeemed Press Ranger rows. AppSumo redemption/license values were treated as secret-like material and were not copied into this ledger.
- Secure source inspection found no `PRESS_RANGER_*`, `PRESSRANGER_*`, or obvious Press Ranger API key material in the inspected dotenv, and no Press Ranger-specific credential entry in the inspected credential file. Existing generic credential-pool material authenticated successfully at runtime; raw usernames, passwords, cookies, and session IDs were not stored.
- Correct entry paths are verified: public site `https://pressranger.com/`, login `https://pressranger.com/login`, and authenticated dashboard `https://pressranger.com/dashboard`. `https://www.pressranger.com/` redirects to the canonical host.
- Runtime-only login reached the authenticated dashboard with page title `Welcome - Press Ranger`; no MFA or reCAPTCHA blocker was observed in this pass.
- Read-only browser navigation confirmed reusable surfaces for dashboard/account readiness, journalist database, podcast database, publisher database, AI campaigns, press releases, account settings, team settings, company settings, and billing. No companies, campaigns, press releases, lists, relationships, team members, billing settings, or account settings were created or changed.
- Classification: `browser_dashboard_verified_readonly`. Press Ranger is a viable browser-operated PR/outreach surface, not an API connector candidate until official API/key material is found.
- Highest-value first workflows: account readiness check, PR campaign/press-release inventory summary, media discovery capability check, and public-doc-assisted runbook validation. Do not create campaigns/releases, mark media relationships, add lists/companies/team members, send/publish/distribute, upgrade/redeem, export media/contact data, or alter account/billing/settings without a separate write contract.

## Plerdy browser access classification pass (DIG-51)

Verification timestamp: 2026-05-08T08:01:03Z
Related issue: DIG-51
Detailed handoff: `00-foundation/operator-system/browser-runbooks/plerdy-access-classification.md`

- Inventory source confirms 10 redeemed Plerdy code-based rows. AppSumo redemption/license values were treated as secret-like material and were not copied into this ledger.
- Secure source inspection found no `PLERDY_*` env/API key material and no Plerdy-specific credential entry in the inspected secure credential sources. Generic credential-pool probes were runtime-only; raw usernames, passwords, cookies, and session IDs were not stored.
- Correct public path is verified at `https://www.plerdy.com/`. Correct app login path is `https://a.plerdy.com/login`, which renders `Plerdy | Login Form`; the login form posts to `https://a.plerdy.com/auth/login` with `email`, `password`, `_token`, and optional `remember` fields. `https://app.plerdy.com/` did not resolve in DNS during this pass.
- Runtime-only login probes using the available generic credential-pool pairs each redirected back to `/auth/login` and remained on the login page. No MFA or reCAPTCHA blocker was observed in these HTTP-level probes.
- Browser automation note: ChromeOps could not be opened because the shared ops profile was already locked by another ChromeOps process, and the alternate browser stack still lacks the local Chromium shared library needed to launch. No browser cookie/session inspection was performed.
- Classification: `browser_url_verified_credentials_invalid`. The blocker is absent/non-matching credentials or absent verified persisted session, not an unknown entry URL. Plerdy is not yet a reusable live operator surface.
- Highest-value surfaces after human-approved access and owned-site confirmation: site/project inventory, instrumentation/tracking health, heatmaps, session recordings, conversion funnels, events/goals, SEO alerts, smart forms/popups/NPS/feedback widgets, e-commerce analytics, integrations, team/account, billing/plan, and data-retention settings. Do not install scripts, alter analytics/forms/popups/funnels/events/integrations/team/billing/settings, redeem license material, or export raw visitor/form/session data without a separate write contract.

## AgenticFlow API viability pass (DIG-58)

Verification timestamp: 2026-05-08T09:20:00Z
Related issue: DIG-58
Detailed handoff: `automation/agenticflow-api-viability.md`

- Inventory source confirms one activated AgenticFlow row. License/redemption material was treated as secret-like and was not copied into this ledger.
- Secure source inspection found AgenticFlow API-key material in `/mnt/c/Users/ohu00/Documents/.env`; `tools/.env` does not include it. No raw key, workspace ID, project ID, browser credential, session cookie, or AppSumo license material was copied into the repo.
- Official docs confirm the current REST base as `https://api.agenticflow.ai/`, API-key auth as `Authorization: Bearer`, and the lowest-risk documented read as `GET /v1/agents/?workspace_id={workspace_id}[&project_id={project_id}&limit=...]`. The older `api.agenticflow.com` example in the authentication page should not be used for new work.
- Runtime-only CLI smoke check with the key exported as `AGENTICFLOW_API_KEY` returned key-present/authenticated behavior and exposed workspace/project context at runtime; raw IDs were not committed.
- Direct GET probes without context returned HTTP 400 `Project ID must be provided for project-scoped resource access`. The guarded probe with CLI-returned workspace/project context returned HTTP 403 `API key does not have access to this project`.
- Classification: `api_auth_verified_project_scope_mismatch`. The blocker is project/key scoping, not an unknown API base or unauthenticated key.
- `tools/appsumo_readonly_probe.py` has a guarded `agenticflow agents` resource requiring `--workspace-id` before any request and supporting `--secret-name AGENTICFLOW_AI_KEY` when needed. Use `--project-id`, `--summary-only`, and `--json` only after the operator supplies/rotates a project-scoped key or confirms the correct project context.

## Procesio API viability pass (DIG-60)

Verification timestamp: 2026-05-08T09:40:12Z
Related issue: DIG-60
Detailed handoff: `automation/procesio-api-viability.md`

- Inventory source confirms one activated Procesio row. AppSumo redemption/license material was treated as secret-like and was not copied into this ledger.
- Official docs are reachable at `https://docs.procesio.com/`. Live Swagger UI is reachable at `https://webapi.procesio.app/swagger/index.html`, with OpenAPI JSON at `https://webapi.procesio.app/swagger/v1.19/swagger.json`.
- Documented/current API base: `https://webapi.procesio.app`. API-key auth uses separate headers `key` (API key name) and `value` (API key value); workspace-scoped routes may also require a `workspace` header.
- Secure source inspection found `PROCESIO_API_KEY` in `/mnt/c/Users/ohu00/Documents/.env`, but no matching `PROCESIO_API_KEY_NAME` or approved workspace header value. `tools/.env` does not include Procesio credentials. No raw key or private account/workspace data was stored.
- Safe GET auth-shape probes against `/api/Users/me`, `/api/Workspaces`, `/api/Projects/count`, and `/api/Projects` found bearer/value-only auth returns HTTP 407, while guessed `key: PROCESIO_API_KEY` + value returns HTTP 401. This confirms the API-key shape but proves the env-var name is not the required API key name.
- Classification: `api_base_verified_key_name_missing`. A guarded `procesio` resource set now exists in `tools/appsumo_readonly_probe.py`, but it exits before any request if `--api-key-name` is missing. First approved reads after unblock should be `users-me`, `workspaces`, `projects-count`, then optionally one summary-only `projects` page. Do not run `POST /api/Projects/{id}/run`, create workflows/webhooks/credentials/schedules, export run history, or mutate user/workspace/project settings without a separate write/execute contract.

## Late / Zernio API viability pass (DIG-66)

Verification timestamp: 2026-05-08T10:40:00Z
Related issue: DIG-66
Detailed handoff: `automation/late-zernio-api-viability.md`

- Inventory source confirms one activated Late row. AppSumo redemption/license material was treated as secret-like and was not copied into this ledger.
- Secure source inspection found `GETLATE_DEV_API_KEY` in `/mnt/c/Users/ohu00/Documents/.env`; `tools/.env` does not include Late/Zernio credentials. No raw key, account handles, profile URLs, user details, post bodies, or API response bodies were stored.
- Public docs have rebranded to Zernio: `https://docs.getlate.dev/` redirects to `https://docs.zernio.com/`, and `https://docs.zernio.com/api/openapi` publishes the OpenAPI spec. Auth is `Authorization: Bearer`, with documented base `https://zernio.com/api`; legacy/operator base `https://getlate.dev/api/v1` also works.
- Runtime-only safe GET probes returned HTTP 200 for `profiles`, `accounts`, `accounts/health`, `posts?limit=1`, `usage-stats`, and `users` against both legacy GetLate and current Zernio bases.
- Classification: `api_verified_readonly`. The guarded `late` resource set now exists in `tools/appsumo_readonly_probe.py`; use `--summary-only --json` and prefer an explicitly loaded secure dotenv or clean automation credential because one malformed process-environment value caused 401 during the pass.
- Safe next step: disabled/manual-first n8n health digest only. Do not create/schedule/publish/edit/delete posts, connect/disconnect social accounts, handle inbox/comments/DMs, mutate webhooks/users/API keys/settings, or export raw account/profile/post/user data without a separate write contract.

## CallScaler API viability pass (DIG-64)

Verification timestamp: 2026-05-08T10:11:35Z
Related issue: DIG-64
Detailed handoff: `automation/callscaler-api-viability.md`

- Inventory source confirms 9 CallScaler rows: 7 redeemed and 2 expired. AppSumo redemption/license material was treated as secret-like and was not copied into this ledger.
- Secure source inspection found `CALLSCALER_API_KEY` and `CALLSCALER_API_KEY_1` in `/mnt/c/Users/ohu00/Documents/.env`; `tools/.env` does not include CallScaler key names. No raw key value was printed or committed.
- Public API base/auth shape remains `https://callscaler.com/api/v1/` with `Authorization: Bearer`.
- Runtime-only safe GET probes using both available secure keys returned HTTP 401 JSON `unauthorized` for `GET /calls?limit=1`, `GET /dashboard/stats`, and `GET /numbers?limit=1`.
- Additional default-key probes returned HTTP 401 for `GET /analytics/calls` and `GET /call-flows`.
- Classification: `api_base_verified_credentials_invalid_or_unscoped`. The blocker is no longer missing env binding; it is likely expired/revoked/wrong-account key material, missing entitlement, or a key that must be regenerated from CallScaler's v3 API-key settings.
- Do not add CallScaler to n8n or scheduled health checks yet. A guarded GET-only `callscaler` resource exists in `tools/appsumo_readonly_probe.py` only for manual summary-only retries after access is corrected. Next operator ask: verify or rotate a real CallScaler API key from `https://v3.callscaler.com/app/settings?tab=api-keys`, confirm account/tenant scope, and approve one first read-only resource. Do not fetch or store raw calls, phone numbers, caller identities, recordings, transcripts, exports, webhook details, number inventory, call-flow payloads, or billing data without a separate privacy/write contract.

## Explicit blockers

- Browser credential handling: avoid exposing raw passwords in repo, issue comments, or command output. Browser-first tools need a persisted ops browser session or a human-approved credential-entry workflow.
- Tenant/base URLs missing or credential-pair incomplete: SuiteDash now has a known generic login/API base, but live access still needs real `X-Public-ID` values or browser credentials/session; Boost.space now needs the exact `{system}.boost.space` tenant base; Flowlu now needs the exact `{company}.flowlu.com` workspace base; some remaining browser-only tools still need exact tenant/dashboard URLs before API or session checks can be conclusive. FuseBase, AITable, and Emailit no longer belong in this blocker when the current secure sources are used correctly.
- API auth shape uncertainty: Lunacal requires official endpoint/auth confirmation before treating current keys as invalid. Procesio auth/base are no longer uncertain after DIG-60, but current runtime lacks the separate API key name and approved workspace context required for first successful reads. CallScaler auth/base are no longer uncertain after DIG-64, but both current secure keys return HTTP 401 and need operator verification/rotation before connector work. Late/Zernio auth/base are no longer uncertain after DIG-66: bearer auth returned HTTP 200 on both legacy GetLate and current Zernio bases for safe summary-only GETs. AgenticFlow auth/base are no longer uncertain after DIG-58, but the current key/context is project-scope blocked by REST HTTP 403. Dadan is no longer API-base/auth uncertain after DIG-56: use `https://app.dadan.io/api/v1/usedadan` with `X-Dadan-API-Key`, limited to approved `GET /requestrecording/{RequestCode}` checks. Boost.space and Flowlu auth shapes are documented, but they still require verified tenant bases before key validity can be tested. Certopus auth is no longer uncertain after DIG-45: official Swagger documents `X-API-KEY`, and the current key returned HTTP 200 for safe GETs.
- Priority scope: This pass intentionally stops at high-value AppSumo tools instead of trying all 309 products.

## Source inventory counts used

- Brilliant Directories: 5 activated
- SuiteDash: 136 redeemed
- KonnectzIT: 20 redeemed
- Agiled: 8 redeemed, 2 expired
- Boost.space: 6 activated
- Flowlu: 5 redeemed, 1 expired
- FuseBase: 10 redeemed
- Brizy Cloud: 10 redeemed
- Plerdy: 10 redeemed
- Press Ranger: 10 redeemed
- Certopus: 10 redeemed
- CallScaler: 7 redeemed, 2 expired
- Lunacal, Emailit, SMS-iT CRM, WbizTool, AgenticFlow, AITable.ai, Procesio, Dadan, Late/Zernio: 1 activated each
