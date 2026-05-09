# Formaloo API Viability

Verification timestamp: 2026-05-08T11:03:54Z
Owner: Automation Engineer
Related issue: DIG-67

## Verdict

Formaloo is `api_verified_readonly` for disabled/manual-first metadata health checks.

The secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env` contains the required Formaloo runtime names:

- `FORMALOO_API_KEY`
- `FORMALOO_API_SECRET`

No raw key, secret, JWT, form response, respondent record, cookie, password, or export file was copied into the repo.

## Official sources used

- Formaloo developer collection: `https://help.formaloo.com/en/collections/3330828-for-developers`
- API key flow: `https://help.formaloo.com/en/articles/8143469-how-to-use-formaloo-api-keys-in-formaloo-api`
- API documentation entry: `https://help.formaloo.com/en/articles/9310643-formaloo-api-documentation`
- Redoc/OpenAPI docs: `https://docs.formaloo.com/#/`

Current docs show this auth pattern:

1. Send `x-api-key: {API Key}` plus `Authorization: Basic {Secret Key}` to the authorization-token endpoint.
2. Include `grant_type=client_credentials`.
3. Use the returned short-lived `authorization_token` as `Authorization: JWT {token}` with `x-api-key` for API reads.

The current Redoc examples use `https://api.formaloo.me/v3.0/oauth2/authorization-token/` and `https://api.formaloo.me/v3.0/forms/`. The older help article also references `https://api.formaloo.net/v1.0/oauth2/authorization-token/`; live checks confirmed all tested token bases returned HTTP 200, but repo tooling uses the current v3 `api.formaloo.me` base.

## Runtime checks performed

All checks used runtime-only secret loading from `/mnt/c/Users/ohu00/Documents/.env`.

| Probe | Result | Safe signal |
|---|---|---|
| `POST https://api.formaloo.me/v3.0/oauth2/authorization-token/` | HTTP 200 | API key + secret can mint a short-lived token. Token was not printed or stored. |
| `POST https://api.formaloo.net/v1.0/oauth2/authorization-token/` | HTTP 200 | Older documented base still accepts the same auth flow. Not used as the default. |
| `POST https://api.formaloo.me/v1.0/oauth2/authorization-token/` | HTTP 200 | Legacy `api.formaloo.me` v1 token route also works. Not used as the default. |
| `GET https://api.formaloo.me/v3.0/forms/` | HTTP 200 | Account has 27 visible forms. Summary-only tooling reports counts and field names only; no raw form URLs, owner emails, respondent data, or form bodies are committed. |
| `GET https://api.formaloo.me/v3.0/profile/` | HTTP 200 | Profile endpoint authenticates. Summary-only tooling reports coarse safe fields only. |

## Tooling added

`tools/appsumo_readonly_probe.py` now supports:

```bash
python tools/appsumo_readonly_probe.py formaloo --list-resources
python tools/appsumo_readonly_probe.py formaloo forms \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json
python tools/appsumo_readonly_probe.py formaloo profile \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --summary-only \
  --json
```

The helper performs one token-minting POST, then only the requested GET. It does not submit forms, create apps, update schemas, export responses, create webhooks, change team settings, or persist secrets.

## Safe operator surface

Allowed under this read-only classification:

- Count visible forms.
- Count/profile-check account readiness without exposing profile PII.
- Surface non-secret field-name inventory for form metadata only.
- Run disabled/manual-first n8n health checks after an operator reviews the summary output.

Out of scope without a separate write/export contract:

- Form submissions or test submissions.
- Creating/updating/deleting forms, apps, projects, dashboards, portals, fields, webhooks, teams, or settings.
- Exporting rows/submissions/responses.
- Exposing respondent PII, owner emails, form URLs, custom domains, webhook URLs, API keys, JWTs, or raw form descriptions/bodies.
- Enabling scheduled n8n runs against the discovery credential; use a dedicated `FORMALOO_API_KEY_AUTOMATION` + `FORMALOO_API_SECRET_AUTOMATION` or n8n credential before Cron.

## n8n promotion recommendation

A disabled/manual-first health pack now exists at:

- `automation/n8n-workflows/formaloo-readonly-health-check.md`
- `automation/n8n-workflows/formaloo-readonly-health-check.draft.json`

Before importing or scheduling it in real n8n:

1. Create dedicated n8n credential records for Formaloo API key and secret.
2. Run manually with `--summary-only --json`.
3. Review the notification payload for accidental PII leakage.
4. Keep Cron disabled until an operator approves cadence and data minimization.

## Classification

`api_verified_readonly`

Formaloo is viable for guarded metadata/count health checks and operator readiness summaries. It is not approved for form submission, response export, schema mutation, workflow/webhook mutation, or live scheduled automation writes.
