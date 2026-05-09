# SuiteDash Access-Completion Packet

Verification timestamp: 2026-05-08T10:11:19Z
Operator: Browser Operations Lead
Related issues: DIG-38, DIG-41, DIG-63

## Purpose

This packet is the exact operator handoff required before agents resume SuiteDash browser or Secure API verification. It exists because DIG-38 verified the public login/API bases but also proved the current local secure sources do not contain the tenant-specific inputs needed for safe live access.

SuiteDash remains high-value for this repo because `The Good Parts of SuiteDash` is the active product domain. Do not convert assumptions into tenant facts. Resume only after the missing values below are provided through an approved secure channel.

## Current classification

Status: `tenant_urls_verified_public_auth_mixed_credentials_insufficient`

Already known from DIG-38 and DIG-63:

- Generic browser login path: `https://app.suitedash.com/`
- Browser login page title observed: `SuiteDash - Login`
- Official Secure API base: `https://app.suitedash.com/secure-api/`
- Official Swagger JSON: `https://app.suitedash.com/secure-api/swagger/json-file`
- API authentication shape: both `X-Public-ID` and `X-Secret-Key` headers are required.
- The secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env` contains eleven `SUITEDASH_*_API_KEY` values, handled runtime-only and not copied into repo docs.
- `tools/.env` and `tools/.env.example` do not contain SuiteDash credentials.
- Dummy/documentation credentials confirmed the API base/auth shape on dummy-allowed endpoints without touching live tenant data.
- Each local secret-key-shaped value failed live access when paired with absent or guessed public IDs; guessed public IDs returned 401.
- DIG-63 replaced the prior guessed `{slug}.suitedash.com` tenant-host language with the exact portal hosts found in the secure ENV sheet. The host names below are non-secret tenant labels/URLs; no Public ID, Secret Key, API key, password, cookie, or session value is stored here.

## Tenant portal host registry from secure ENV sheet

Verification command shape: `curl -L --max-time 20 -A 'Mozilla/5.0' <portal-auth-url>` against the non-secret public authentication URL only. These checks did not send credentials and did not inspect authenticated tenant data.

| Tenant label | Public authentication URL | HTTP result | Observed final URL / title | Usefulness for next step |
|---|---|---:|---|---|
| ClickOnPage | `https://portal.clickonpage.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.clickonpage.com/site/login`; title `ClickOnPage - Login` | Live SuiteDash portal login. Useful for human-assisted browser login and for matching a future Public ID/secret pair to the correct tenant. |
| Coadjutant | `https://portal.coadjutant.com/integrations/publicApi?t=authentication` | 000 | TLS handshake failed with `wrong version number` on HTTPS; HTTP was intercepted by ISP/security warning, so not treated as tenant evidence. | Exact host is recorded, but the public auth page was not reachable from this network. Recheck from a clean network or ask operator to confirm whether the portal is retired/misconfigured. |
| Desk Village | `https://portal.deskvillage.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.deskvillage.com/site/login`; title `Desk Village - Login` | Live SuiteDash portal login. Useful for next secure verification step. |
| Dome Law | `https://portal.domelaw.com/integrations/publicApi?t=authentication` | 000 | HTTPS timed out; HTTP redirected to HugeDomains sale page for `domelaw.com`. | Host is likely retired, parked, or DNS/tenant routing is broken. Do not use until operator confirms the current tenant host. |
| instaxis | `https://portal.instaxis.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.instaxis.com/site/login`; title `instaxis - Login` | Live SuiteDash portal login. Useful for next secure verification step. |
| Naija Clan | `https://portal.naijaclan.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.naijaclan.com/site/login`; title `Naija Clan. - Login` | Live SuiteDash portal login. Useful for next secure verification step. |
| NAWA | `https://portal.nawa.ai/integrations/publicApi?t=authentication` | 000/502 | Strict TLS failed because certificate SAN did not match `portal.nawa.ai`; `curl -k` and HTTP returned `502 Bad Gateway`. | Exact host is recorded, but current TLS/backend state is not usable. Recheck after DNS/cert/backend fix or operator confirmation. |
| notroom | `https://portal.notroom.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.notroom.com/site/login`; title `notroom - Login` | Live SuiteDash portal login. Useful for next secure verification step. |
| relguard | `https://portal.relguard.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.relguard.com/site/login`; title `relguard - Login` | Live SuiteDash portal login. Useful for next secure verification step. |
| SitBid | `https://portal.sitbid.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.sitbid.com/site/login`; title `SitBid - Login` | Live SuiteDash portal login. Useful for next secure verification step. |
| Your Deputy | `https://portal.yourdeputy.com/integrations/publicApi?t=authentication` | 200 | Redirects to `https://portal.yourdeputy.com/site/login`; title `Your Deputy - Login` | Live SuiteDash portal login. Useful for next secure verification step. |

Reachability summary: 8 of 11 exact tenant portal auth URLs are live and redirect to branded SuiteDash login pages. 3 need operator/network/tenant repair before use: Coadjutant, Dome Law, and NAWA.

## Missing values the operator must provide

Provide these through the approved secure credential/session channel. Do not paste secrets into Git, Paperclip comments, screenshots, chat, or terminal output.

| Required input | Exact value needed | Why it is required | Acceptable evidence format |
|---|---|---|---|
| Tenant URL(s) | Exact public portal hosts are now recorded in the registry above. For the three non-live hosts, provide replacement/current hosts or confirm retirement. | Prevents agents from guessing `{slug}.suitedash.com` or treating generic `app.suitedash.com` as a tenant. | Non-secret URL plus a short label such as `client portal`, `internal ops portal`, `inactive/retired`, or `demo tenant`. |
| Browser login/session path | Either a human-established persisted ops browser profile/session, or a dedicated username/password entered by a human into the browser at runtime. | Browser verification cannot proceed without authenticated access. | Preferred: persisted Chrome/Playwright profile path and tenant label. Alternative: operator joins a live session and types credentials without exposing them. |
| MFA/session prerequisite | Whether MFA, device approval, SSO, CAPTCHA, email magic link, or IP allowlisting is required. | Prevents repeated failed login attempts and account lockouts. | Plain-language note, no recovery codes or OTP values. |
| `X-Public-ID` to `X-Secret-Key` mapping | For each SuiteDash API key intended for use, the exact Public ID that pairs with that secret key. | SuiteDash Secure API requires both headers; the existing local values appear to be secret-key-shaped only. | Store in secure dotenv or secret manager as paired names, e.g. `SUITEDASH_<LABEL>_PUBLIC_ID` + `SUITEDASH_<LABEL>_SECRET_KEY`, or document which existing `SUITEDASH_*_API_KEY` maps to which Public ID without revealing values. |
| Tenant/project label for each key pair | Human-readable label for what each key can access: internal ops tenant, demo portal, customer portal, inactive test tenant, etc. | Lets agents choose the lowest-risk read-only target and avoid client/private data by default. | Non-secret label and access scope summary. |
| API permission/scope note | Whether each key is read-only, full access, implementation/client scoped, expired, or unknown. | Prevents accidental use of a write-capable key without a separate write contract. | Plain-language scope note copied from SuiteDash admin UI, with no secret values. |
| Approved first-read target | The tenant and endpoint/screen that should be used for the first smoke check. | Keeps verification narrow and reversible. | Example: `Use demo/internal tenant only; first browser read = dashboard title; first API read = /contact/meta`. |

## Recommended secure variable shape

Use whatever secure store is standard for the operator environment, but pair values explicitly so future agents do not guess. Example names only; do not commit values:

```text
SUITEDASH_<LABEL>_TENANT_URL=
SUITEDASH_<LABEL>_AUTH_URL=
SUITEDASH_<LABEL>_PUBLIC_ID=
SUITEDASH_<LABEL>_SECRET_KEY=
SUITEDASH_<LABEL>_BROWSER_PROFILE_PATH=
SUITEDASH_<LABEL>_SCOPE_NOTE=
```

If keeping the current `SUITEDASH_*_API_KEY` names, add a separate secure mapping table outside the repo that says which `SUITEDASH_*_API_KEY` pairs with which `X-Public-ID` and tenant label.

## Safe first-read verification plan

### Guardrails for both paths

- Read-only only.
- Use the lowest-risk internal/demo tenant first.
- Do not export contacts, clients, invoices, files, tickets, email lists, or full record tables.
- Do not create, update, delete, publish, send, invite, sync, import, approve, or change settings.
- Do not record screenshots that contain secrets, private client data, tokens, billing details, email addresses, or session cookies.
- Summarize metadata only: reachable/unreachable, page title, endpoint status, counts where safe, and high-level surface names.
- Stop immediately on MFA, unexpected write prompts, account warnings, permission-denied loops, or private client-data exposure.

### Browser path

Prerequisite: live exact tenant portal URL from the registry plus human-approved session/credential path.

1. Open the verified tenant URL in the approved ops browser profile.
2. If already authenticated, record only the page title, tenant/workspace label, and whether the account appears to be internal/demo/client-facing.
3. If not authenticated, have the human enter credentials at runtime; do not paste credentials into terminal or repo docs.
4. If MFA/session approval appears, stop and ask the operator to complete it or provide a persistent approved session.
5. After login, inspect navigation labels only. Do not open private record tables until an approved first target is chosen.
6. Record a one-paragraph result in this file or the AppSumo ledger: tenant label, access status, read-only surfaces visible, and any remaining blockers.

Minimum browser success definition:

- Authenticated SuiteDash tenant page loads.
- Tenant/workspace label is identified at a high level.
- No secrets/client data are copied.
- At least the top-level navigation/surface map can be described.

### Secure API path

Prerequisite: exact `X-Public-ID` + `X-Secret-Key` pair and scope/tenant label.

1. Load credentials only from the secure runtime source.
2. Confirm Swagger/base remains reachable at `https://app.suitedash.com/secure-api/swagger/json-file` and `https://app.suitedash.com/secure-api/`.
3. Run the lowest-risk GET first, preferably a metadata endpoint such as `/contact/meta` if it is still documented for the tenant/key pair.
4. Then run one tiny page-size read against the approved first-read target only, e.g. `limit=1` or equivalent if supported.
5. Summarize only HTTP status, endpoint name, object type, and redacted/count metadata. Do not commit response bodies containing people, emails, files, billing, or private project text.
6. If 401/403 occurs, classify precisely: invalid Public ID/secret pairing, insufficient scope, expired key, wrong tenant, or MFA/session-only browser path.

Minimum API success definition:

- A live tenant key pair returns HTTP 200 on a documented read-only endpoint.
- The tenant/project label and key scope are known.
- Output is redacted/data-minimized.

## Read-only surface map to prioritize after access is restored

Prioritize surfaces that improve the SuiteDash product evidence and operator understanding without exposing sensitive client data.

| Priority | Surface | Why it matters | First-read approach | Write risk |
|---:|---|---|---|---|
| 1 | Integrations > Secure API | Confirms key inventory, Public ID pairings, docs, usage limits, and scope. | Browser-only metadata read: key labels/scopes, no secret reveal. | High if keys are created/rotated; do not mutate. |
| 2 | Dashboard / workspace overview | Confirms tenant identity, active modules, and whether this is demo/internal/client. | Browser navigation/title summary only. | Low if read-only. |
| 3 | CRM: Contacts / Companies | Core SuiteDash operating surface and product relevance. | API/browser count + field-name summary; no exports. | High because client PII may appear. |
| 4 | Projects / Tasks | Shows real implementation workflows and operator setup patterns. | Count/status/category summary only from approved tenant. | Medium-high; avoid edits/imports. |
| 5 | Portals / Client Management | Product-domain proof for client portal guidance. | Top-level labels/features only. | High; client/private data likely. |
| 6 | Worlds / LMS | Relevant if training/course delivery is active. | Module existence + title/count summary only. | Medium; avoid publishing/course edits. |
| 7 | Forms / Data collection | Reveals intake workflow patterns. | Form names/counts and field categories only. | Medium-high; no submissions/exports. |
| 8 | File Sharing / Documents / eSigning | Useful for delivery workflows but sensitive. | Surface existence only unless operator approves a demo folder. | High; no downloads. |
| 9 | Calendar / Scheduling | Relevant to service workflow packaging. | Settings labels/counts only. | Medium; no bookings or sync changes. |
| 10 | Support Tickets / Communication | Reveals customer ops workflow. | Count/status summary only if demo/internal; avoid message content. | High; no replies/status changes. |
| 11 | Email Marketing / Automations | High leverage but dangerous. | Inventory names/status only; do not trigger sends or automations. | Very high; separate write contract required. |
| 12 | Office / Billing / Subscriptions / Settings / Staff | Important for governance, not first-read. | Defer unless specifically authorized. | Very high; read-only only. |

## What remains blocked vs known

### Known

- The generic SuiteDash browser login page is live at `https://app.suitedash.com/`.
- SuiteDash Secure API docs/base are live at `https://app.suitedash.com/secure-api/`.
- SuiteDash Secure API requires both `X-Public-ID` and `X-Secret-Key`.
- Local secure sources have secret-key-shaped SuiteDash values but no matching Public IDs.
- Exact non-secret portal auth URLs are now recorded for eleven SuiteDash tenant labels from the secure ENV sheet.
- Eight portal auth URLs are live from this network and redirect to branded SuiteDash login pages: ClickOnPage, Desk Village, instaxis, Naija Clan, notroom, relguard, SitBid, and Your Deputy.
- Three portal auth URLs are not currently usable from this network: Coadjutant (HTTPS TLS `wrong version number`), Dome Law (HTTPS timeout / HTTP parked-domain redirect), and NAWA (TLS certificate mismatch plus 502 backend response).

### Blocked

- Authenticated browser verification of any SuiteDash tenant.
- Live API reads against a real SuiteDash tenant.
- Tenant/workspace identification beyond public portal login branding.
- Determining whether existing keys are platform-admin capable, tenant/client scoped, expired, or wrong-environment.
- Any read-only evidence from actual SuiteDash records or authenticated navigation.
- Current-host confirmation for Coadjutant, Dome Law, and NAWA before those three are used.

### Not allowed without a future explicit write issue

- Creating/rotating API keys.
- Changing account, staff, role, billing, white-label, portal, automation, email, form, file, LMS, or project settings.
- Exporting client/contact/project/file/ticket/billing data.
- Sending emails, invites, automations, or notifications.
- Creating demo records in a live tenant.

## Operator checklist

Before assigning another SuiteDash verification issue, complete this checklist:

- [x] Exact public tenant portal URL(s) recorded for eleven labels; 8 live, 3 require operator recheck/repair.
- [ ] Browser access path provided: persisted approved session/profile or human-assisted login plan.
- [ ] MFA/session prerequisites documented.
- [ ] At least one `X-Public-ID` + `X-Secret-Key` pair is available in the secure runtime source.
- [ ] Each key pair has a tenant/project label and scope note.
- [ ] A lowest-risk first-read target is selected.
- [ ] Agent is instructed to keep output redacted, data-minimized, and read-only.

## Recommended next issue after completion

Once the operator provides the missing secure inputs, create a narrow read-only verification issue with this scope:

- Verify one approved live SuiteDash tenant in browser or API, not all eleven keys/portals.
- First browser read: authenticated page title + navigation labels only.
- First API read: one metadata endpoint, then one `limit=1` approved endpoint if safe.
- Update `01-market-research/appsumo/2026-05-08-priority-access-ledger.md` with the final classification.
- Do not perform writes or exports.
