# Tech Stack — Dynasty Empire Digital Products

The full reference for the stack supporting this repo's products.

## Storefront / Sales

| Layer | Tool | Notes |
|---|---|---|
| Storefront | Gumroad | Primary — until graduation criteria |
| Custom checkout (graduate) | Vercel + Stripe | When fee differential justifies build time |
| Sales page hosting | Vercel | Standalone pages at custom subdomains |
| Domain management | 20i | Reseller account ID 10455 |

## Email

| Layer | Tool | Notes |
|---|---|---|
| Transactional / post-purchase | Gumroad Workflows | Default for first 1–2K subscribers |
| Newsletter (graduate) | Beehiiv | Recommended graduate path |
| Email automation (advanced) | n8n at n8n.audreysplace.place | For conditional logic, multi-step flows |
| Bulk email (legacy) | Acumbamail | Already in stack via PA CROP infra |

## Authority / Audience

| Layer | Tool | Notes |
|---|---|---|
| Long-form essays | ikeohu.com | Six-lane authority strategy |
| Primary social | LinkedIn | B2B operator audience |
| Secondary social | X / Twitter | Faster iteration, builders |
| Newsletter delivery | ikeohu.com → Beehiiv (planned) | |

## Backend / Data

| Layer | Tool | Notes |
|---|---|---|
| Database | Neon Postgres | Org: `org-small-credit-59990711` |
| Hosting (apps) | Vercel | Team: `team_fuTLGjBMk3NAD32Bm5hA7wkr` |
| Static / WordPress hosting | 20i | Pinnacle / WordPress Pinnacle packages |
| Code | GitHub (private repos) | `pinohu/digitalproducts` (this repo) |

## Automation Layer

| Layer | Tool | Notes |
|---|---|---|
| Workflow automation | n8n | `n8n.audreysplace.place` |
| Cross-tool integration | n8n + KonnectzIT | KonnectzIT has 20 LTD licenses |
| AI / agents | Claude (this) + Flint VM | Bridge: `claude-inbox/outbox.audreysplace.place` |

## Membership / Auth (Future Higher Rungs)

| Layer | Tool | Notes |
|---|---|---|
| Membership | SuiteDash | 136 Pinnacle licenses available |
| Directory layer | Brilliant Directories | 100 license deployments available |
| Course delivery | TBD — Hyax / FastSpring evaluated | When graduating beyond PDF format |

## Payment

| Layer | Tool | Notes |
|---|---|---|
| Primary processor | Gumroad (uses Stripe under the hood) | |
| Direct Stripe (graduate) | Stripe | Account prefix `51TF63A5` |
| Subscription billing | Stripe + custom dashboard | When recurring rungs activate |

## Support

| Layer | Tool | Notes |
|---|---|---|
| Email support | Reply-to from Gumroad → monitored inbox | Default |
| Helpdesk (graduate) | Insighto.ai | LTD already in stack |
| Voice / SMS | Thoughtly + CallScaler + SMS-iT | Already deployed for PA CROP |

## Analytics

| Layer | Tool | Notes |
|---|---|---|
| Sales / revenue | Gumroad dashboard | Native |
| Site analytics | Vercel Analytics + Plausible | Privacy-friendly |
| Email analytics | Gumroad / Beehiiv native dashboards | |
| Custom reporting (graduate) | Neon + Metabase | When data crosses platforms |

## Brand / Design

| Layer | Tool | Notes |
|---|---|---|
| Design | Canva (LTD) + Figma | |
| Cover art | Custom + AI assist | |
| Brand assets | `/shared-assets/brand-elements/` | This repo |
