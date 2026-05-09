# Boost.space and Flowlu API Viability Follow-up

Related issue: DIG-42
Verification timestamp: 2026-05-08T05:33:00Z
Owner: Automation Engineer

## Safety rules used

- Read-only probes only.
- No raw API keys, AppSumo license codes, passwords, cookies, or customer exports are stored in this repo document.
- Runtime-only credential sources inspected:
  - `/mnt/c/Users/ohu00/Documents/.env`
  - `/mnt/c/Users/ohu00/Downloads/tigertail-product-list-07-05-2026.csv`
  - `/mnt/c/Users/ohu00/Documents/SOFTWARE TOOLS LOGIN CREDENTIALS.txt`
- No destructive writes, syncs, imports, webhook changes, record exports, billing changes, or tenant guesses were performed.

## Executive verdict

Neither Boost.space nor Flowlu is ready for a live read-only connector from the currently available local material.

Both tools have real API-key signals, but both official APIs are tenant-shaped:

- Boost.space official OpenAPI server: `https://{system}.boost.space/api`
- Flowlu official OpenAPI server: `https://{company}.flowlu.com/api/v1/module`

The inspected sources contain API keys / code signals but do not contain the required Boost.space system name or Flowlu company subdomain. Generic host checks confirm the earlier failures were endpoint/base problems, not proof that the keys are invalid.

## Boost.space

### Secure-source signals

- AppSumo inventory: 6 `Boost.space` rows, all `activated`.
- Secure operator dotenv contains `BOOST_SPACE_API_KEY`.
- Secure operator dotenv also contains Make/Boost.space integrator client/key/secret variables.
- The credential text file did not expose a tenant/system URL for Boost.space during this pass.

### Official API shape found

Public developer app assets reference the OpenAPI schema at `https://apidoc.boost.space/5.2.3.json` and `https://apidoc.boost.space/develop.json`.

The OpenAPI server is tenant-shaped:

```text
https://{system}.boost.space/api
```

Authentication is bearer-token based:

```text
Authorization: Bearer <token>
```

The token is described as a bearer token created in a Boost.space user profile.

### Safe probes performed

Using the runtime `BOOST_SPACE_API_KEY`, these non-tenant/generic endpoints did not establish API access:

| Probe | Result | Interpretation |
|---|---:|---|
| `GET https://api.boost.space/` | HTTP 404 | Generic host is not the official tenant API server. |
| `GET https://api.boost.space/v1/modules` | HTTP 404 | Earlier `/v1/modules` base guess is not a valid Boost.space API path. |
| `GET https://api.boost.space/api/modules` | HTTP 404 | Generic `api.boost.space` remains the wrong base. |
| `GET https://developers.boost.space/api/user` | HTTP 401 `Token does not exists.` | Developer app endpoint does not accept the available key as a logged-in app session token. |

No tenant-shaped `https://{system}.boost.space/api` probe was attempted because no verified `{system}` value was present. Fabricating likely subdomains would create false repo truth.

### Classification

`tenant_base_missing`

Boost.space has an API key signal and official API documentation, but current runtime materials do not include the required system/tenant hostname. The key should not be called invalid until a verified system hostname is supplied and a safe GET is retried.

### Smallest safe next step if unblocked

Ask the operator for the exact Boost.space system URL, for example `https://<system>.boost.space/`, and confirm the API key belongs to a user profile in that system. Then run a single data-minimized read-only smoke check:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate
python appsumo_readonly_probe.py boostspace address-countries \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --base-url https://<verified-system>.boost.space/api \
  --page-size 1 \
  --summary-only --json
```

If that returns HTTP 200, a second check against `boostspace activities` can determine whether activity summaries are useful. Keep outputs summary-only because activity records can expose operational/customer data.

## Flowlu

### Secure-source signals

- AppSumo inventory: 6 `Flowlu` rows; 5 `redeemed`, 1 `expired`.
- Secure operator dotenv contains `FLOWLU_API_KEY`.
- The credential text file did not expose a Flowlu account URL/subdomain during this pass.

### Official API shape found

Official Flowlu OpenAPI is available at:

```text
https://www.flowlu.com/api/json/openapien.json
```

The OpenAPI server is tenant-shaped:

```text
https://{company}.flowlu.com/api/v1/module
```

Authentication is query-parameter based:

```text
api_key=<key>
```

This explains the previous `access_token_missing` / unauthorized-style result from generic endpoint guesses: the live API needs the account company subdomain and the documented `api_key` parameter shape.

### Safe probes performed

Using the runtime `FLOWLU_API_KEY`, generic host checks did not establish API access:

| Probe | Result | Interpretation |
|---|---:|---|
| `GET https://www.flowlu.com/api/v1/module?api_key=...` | HTTP 404 | Documentation host is not the tenant API server. |
| `GET https://www.flowlu.com/api/v1/module/crm/account/list?api_key=...` | HTTP 404 | A real `{company}.flowlu.com` subdomain is required. |

No tenant-shaped `https://{company}.flowlu.com/api/v1/module` probe was attempted because no verified `{company}` value was present.

### Classification

`tenant_subdomain_missing`

Flowlu has a real API key signal and a known auth shape, but current runtime materials do not include the account/company subdomain. The key should not be called invalid until a verified tenant base is supplied and a safe GET is retried.

### Smallest safe next step if unblocked

Ask the operator for the exact Flowlu workspace URL, for example `https://<company>.flowlu.com/`. Then run one low-sensitivity read-only smoke check:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate
python appsumo_readonly_probe.py flowlu crm-accounts \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --base-url https://<verified-company>.flowlu.com/api/v1/module \
  --page-size 1 \
  --summary-only --json
```

If CRM accounts are too sensitive for the first read, use `flowlu agile-projects` or `flowlu tasks` with `--page-size 1 --summary-only --json`, and do not commit raw samples.

## Tooling update

`tools/appsumo_readonly_probe.py` now includes disabled-by-default support for these two tenant-shaped platforms:

- `boostspace` resources: `address-countries`, `activities`
- `flowlu` resources: `crm-accounts`, `agile-projects`, `tasks`, `invoices`

Both platform configs require `--base-url`; the script exits before any HTTP request if the verified tenant base is omitted. This prevents future runs from silently guessing tenant subdomains or retrying known-wrong generic bases.

## External blocker packet

To promote either tool into an n8n-ready health check, a human/operator must provide:

1. Boost.space: exact system URL and confirmation that `BOOST_SPACE_API_KEY` is a profile bearer token for that system.
2. Flowlu: exact company/workspace URL and confirmation that `FLOWLU_API_KEY` is active for that workspace.
3. Approval for the first read-only resource to inspect.
4. Confirmation that output should be data-minimized summaries only until a later issue authorizes broader exports.

No live n8n workflow was created or activated in this pass.
