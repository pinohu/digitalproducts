# Certopus Read-Only Endpoint Follow-Up

Verification timestamp: 2026-05-08T05:52:58Z
Related issue: DIG-45
Owner: Automation Engineer

## Verdict

Certopus is now classified as `api_verified_readonly` for a small, safe, manual-first connector surface.

The previous `api_key_unverified` state was caused by incomplete auth-shape knowledge, not by proof that the key was invalid. The current reachable Swagger UI documents `https://api.certopus.com` with API-key authentication in the `X-API-KEY` header. Runtime-only probes using the secure operator dotenv confirmed that the available `CERTOPUS_API_KEY` can access safe GET endpoints.

## Sources checked

- Official Swagger UI: `https://api.certopus.com/`
  - Title observed in embedded Swagger spec: `Certopus API`
  - Host: `api.certopus.com`
  - Scheme: `https`
  - Base path: `/`
  - Security definition: `apiKeyAuth`, `in: header`, `name: X-API-KEY`
- Certopus help center integration collection: `https://help.certopus.com/en/collections/6331613-integrations`
- API-key help articles visible from the integration collection:
  - `https://help.certopus.com/en/articles/15016284-where-to-find-your-api-key-in-certopus`
  - `https://help.certopus.com/en/articles/9053973-where-to-find-api-key`

## Credential-source result

- Secure operator dotenv checked: `/mnt/c/Users/ohu00/Documents/.env`
- `CERTOPUS_API_KEY` is present there.
- `tools/.env` does not contain Certopus credentials.
- No raw API key, token, password, cookie, AppSumo code, certificate recipient data, or rendered certificate content was copied into this repo document.

## Safe GET probes run

All probes used `GET` only and `X-API-KEY: ***` from runtime memory.

| Resource | Endpoint | Result | Data-minimized observation |
|---|---|---|---|
| Templates | `GET https://api.certopus.com/v1/templates` | HTTP 200 | Response groups visible templates by format/category. Category counts observed: A4 Landscape 20, A4 Portrait 6, Badges 40, Legacy 22. Sample field names include `id`, `title`, `eventId`, `template`, `generated`, `updatedAt`, dimensions, and email-template metadata. Raw template bodies/backgrounds were not stored. |
| Organisations | `GET https://api.certopus.com/v1/organisations` | HTTP 200 | Response message `success`; two organisation records visible. Sample field names include `id`, `name`, `imageUrl`, `integrationAllowed`, `brandImages`, and `brandSignatures`. Organisation names were not copied into this document. |
| Wallet | `GET https://api.certopus.com/v1/wallet` | HTTP 200 | Response message `success`; zero visible wallet certificate records in this check. |
| SMTP | `GET https://api.certopus.com/v1/smtp` | HTTP 200 | Response message `empty`; no SMTP configuration details copied. |

## Endpoint/auth classification

- API base: `https://api.certopus.com`
- Auth header: `X-API-KEY: ***`
- Key validity: verified for read-only GETs listed above.
- Current classification: `api_verified_readonly`
- Prior bad route/auth attempts should not be treated as key-invalid evidence unless they used the official `X-API-KEY` header against the current Swagger-documented endpoints.

## Supported local probe usage

`tools/appsumo_readonly_probe.py` now includes a guarded Certopus config for these read-only resources:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate

python appsumo_readonly_probe.py certopus templates --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 5 --summary-only --json
python appsumo_readonly_probe.py certopus organisations --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 5 --summary-only --json
python appsumo_readonly_probe.py certopus wallet --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 5 --summary-only --json
python appsumo_readonly_probe.py certopus smtp --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 5 --summary-only --json
```

The probe uses `X-API-KEY`, redacts secret/PII-shaped fields, exits non-zero on HTTP errors, and supports `--summary-only --json` for Paperclip/n8n-safe reporting.

## Data-minimization rules

- Allowed in repo/Paperclip summaries: endpoint status codes, record counts, category names, non-secret field names, and high-level capability notes.
- Avoid storing raw: certificate PDFs/images, recipient names/emails, template/background payloads, email bodies, SMTP settings, organisation branding assets, API keys, wallet IDs tied to recipients, downloadable exports, and AppSumo license/redemption codes.
- Use `--summary-only --json` by default for any automation output.
- Keep page size low (`--page-size 1` to `5`) for smoke checks.

## Explicitly out of scope

The Swagger spec exposes write-capable and sensitive routes, but they are not authorized by DIG-45:

- `POST /v1/certificates`
- `POST /v1/recipients`
- `DELETE /v1/recipients`
- `POST /v1/send_mails_smtp`
- SMTP/domain/white-label mutations
- Polygon/wallet mutation routes
- Certificate issuance, sends, downloads, or exports

Do not add n8n write nodes, certificate issuance, email sends, exports/downloads, recipient imports/deletes, SMTP changes, domain verification, wallet updates, or webhook-style automation without a separate write contract, dedicated automation key, idempotency/rollback plan, and operator approval.

## Smallest safe connector recommendation

If Certopus becomes relevant to productized training/completion workflows, the smallest safe next connector is a disabled/manual-first health check that summarizes:

1. `templates`: category counts and visible non-secret field names.
2. `organisations`: count and whether integration is allowed, without copying names or branding payloads.
3. `wallet`: certificate count only.
4. `smtp`: presence/empty status only.

Recommended cadence: manual on demand, then at most weekly after an operator reviews the summary for leakage. Live n8n activation still requires a dedicated n8n credential record for `CERTOPUS_API_KEY` or a rotated automation-owned key. No live n8n workflow was created or activated during DIG-45.
