# AppSumo Priority Access Plan

Operating date: 2026-05-08
Related company: `Digital Products Operating System`
Primary operator role: `Browser Operations Lead`

## Purpose

Turn the AppSumo portfolio into actual operator leverage for Hermes and Paperclip.

This plan does not treat the AppSumo collection as a flat list. It prioritizes the tools that can immediately improve:

- product launch operations
- browser-only execution paths
- automation and data sync
- sales-page, CRM, and support workflows
- reusable business infrastructure for future products

## Secure source materials

Do not copy raw passwords or secret values into the repo.

Use these secure sources at runtime only:

- inventory export: `C:\Users\ohu00\Downloads\tigertail-product-list-07-05-2026.csv`
- candidate browser-login pool: `C:\Users\ohu00\Documents\SOFTWARE TOOLS LOGIN CREDENTIALS.txt`
- API vault: `C:\Users\ohu00\Documents\.env`
- research/source corpus:
  - `01-market-research/appsumo/2026-05-07-appsumo-portfolio-inventory.md`
  - related Google Drive research files described there

## Access rules

1. Prefer API or token-based access if a working credential exists in the Paperclip secret store.
2. Use browser login only when API coverage is missing, weak, or insufficient for the required task.
3. Record status in repo truth:
   - verified access
   - needs MFA or human login assist
   - wrong credential pool
   - product no longer relevant
   - API available but not yet validated
4. Never store plaintext passwords, screenshots of secrets, or copied session cookies in repo files or Paperclip comments.

## Priority tiers

### Tier 1: Immediate ops leverage

These are the best candidates to strengthen the current business operator stack.

| Tool | Why it matters now | Best access mode | Current signal |
|---|---|---|---|
| `SuiteDash` | Core product domain, proof, demos, implementation examples, customer ops context | Browser first; product/account-specific API keys second | Multiple `SUITEDASH_*` keys exist in `.env`, but they look like implementation/client keys rather than SuiteDash platform-admin access |
| `Brilliant Directories` | Explicit tool-specific login mapping already exists; useful for directory/business-site operations | Browser first | Login URL plus tool-specific username/password mapping exists in secure credential file |
| `KonnectzIT` | Integration/automation layer that may reduce launch and follow-up friction | Browser first, then API if found in product admin | No obvious API key in `.env`; inventory volume suggests substantial license coverage |
| `Agiled` | CRM, PM, invoicing, and ops system candidate | API first if valid, browser second | `AGILED_API_KEY` exists in `.env` |
| `Boost.space` | Data sync and record system for future multi-tool automations | API first, browser second | `BOOST_SPACE_API_KEY` plus Make integrator credentials exist |
| `Flowlu` | Alternative ops/CRM/finance platform that may support launch workflows | API first, browser second | `FLOWLU_API_KEY` exists in `.env` |
| `FuseBase` | Client-facing docs, portals, and internal knowledge delivery | Browser first | No obvious API key found in `.env` |
| `Brizy Cloud` | Fast landing-page or mini-site surface if additional product pages are needed | Browser first | No obvious API key found in `.env` |

### Tier 2: Supporting growth and execution

| Tool | Why it matters | Best access mode | Current signal |
|---|---|---|---|
| `Plerdy` | CRO and user-behavior analytics | Browser first | No obvious key found |
| `Press Ranger` | PR/outreach support for launches | Browser first | No obvious key found |
| `Certopus` | Certificates/completion workflows if used for productized training or cohorts | API first, browser second | `CERTOPUS_API_KEY` exists |
| `CallScaler` | Phone attribution/sales workflow support | API first, browser second | `CALLSCALER_API_KEY` exists |
| `Lunacal` | Scheduling and booking flows | API first, browser second | `LUNACAL_API_KEY` exists |
| `Emailit` | Transactional or programmatic email support | API first | `EMAILIT_API_KEY` exists |
| `SMS-iT CRM` | Messaging and CRM execution | API first, browser second | `SMS_IT_API_KEY` exists |
| `WbizTool` | WhatsApp operations and messaging automation | API first, browser second | `WBIZTOOL_COM_API_KEY` exists |

### Tier 3: Experimental or future-platform leverage

| Tool | Why it matters | Best access mode | Current signal |
|---|---|---|---|
| `AgenticFlow` | Agent workflow experiments | API first | `AGENTICFLOW_AI_KEY` exists |
| `AITable.ai` | Structured tables and lightweight operational apps | API first | `AITABLE_API_KEY` exists |
| `Procesio` | Additional low-code workflow layer | API first | `PROCESIO_API_KEY` exists |
| `Dadan` | Product demo and walkthrough recording | API first, browser second | `DADAN_API_KEY` exists |

## Candidate browser-login strategy

Use the secure credential file as labeled candidate pools, not repo-stored values.

Suggested attempt order unless a tool-specific mapping is found:

1. `Username1`
2. `Username2`
3. `Username3`
4. `Username4`

For each username, try the password labels in this order:

1. `Password1`
2. `Password2`
3. `Password3`
4. `Password4`

Tool-specific exception already known:

- `Brilliant Directories`
  - use the explicit URL and explicit tool-specific credential mapping from `SOFTWARE TOOLS LOGIN CREDENTIALS.txt`

## What to record during access verification

For each priority tool, record:

- product name
- product URL / login URL
- access mode used: `api`, `browser`, or `both`
- account email label used
- outcome:
  - `verified`
  - `blocked_mfa`
  - `invalid_credentials`
  - `session_exists`
  - `api_only`
  - `deferred`
- notes on tenant/workspace name
- next action

## Immediate execution order

1. Verify `Brilliant Directories` first because it has an explicit tool-specific credential mapping.
2. Verify whether `SuiteDash` platform access is available through browser login or existing sessions.
3. Verify `Agiled`, `Boost.space`, and `Flowlu` because they have both portfolio relevance and API-key signals.
4. Verify `KonnectzIT`, `FuseBase`, and `Brizy Cloud` through browser login.
5. Record every result in a repo-side access ledger before moving on to lower-priority tools.

## Definition of done for this access pass

This pass is complete when:

- the top-priority AppSumo tools have a verified access status recorded
- browser-only blockers and MFA blockers are explicit
- API-backed tools are distinguished from browser-only tools
- the operator can point to the next tools that are actually worth integrating into Hermes/Paperclip

This pass does not require every AppSumo tool to be accessed. It requires a truthful, prioritized operator view of the tools most likely to improve the current business system.
