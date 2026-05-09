# Productization Factory

This folder turns the `digitalproducts` repo into a workflow-productization system.

The core rule is simple:

- do not productize tools
- productize outcomes, workflows, and buyer pain

The owned software stack is the factory. The things sold to buyers are:

- trust-tripwire playbooks
- toolkits
- setup sprints
- recurring managed services

## Role split

### Paperclip

Paperclip is the company operating layer.

Paperclip owns:

- product-family priorities
- work-order status
- sprint sequencing
- governance gates
- agent assignments

### Hermes

Hermes is the persistent operating memory layer.

Hermes owns:

- decision logs
- reusable skills
- tool-capability memory
- product-family memory
- Codex-ready task preparation

### Codex

Codex is the implementation layer.

Codex owns:

- repo edits
- templates
- scripts
- validation tooling
- reports

## What lives here

| Path | Purpose |
|---|---|
| `config/` | Product-family registries, tool-capability registries, roles, governance, pricing ladders |
| `work-orders/` | Backlog, active, review, and completed work orders |
| `templates/` | Reusable Markdown and YAML skeletons for factory output |
| `scripts/` | Validation, scoring, and work-order automation |
| `reports/` | Human-readable rollups and scoreboards |

## First implementation target

The first generated family should be:

- `client-portal-service-delivery-os`

The first live ladder should remain:

- `The Good Parts of SuiteDash`

This layer is additive. It extends the current repo and active sprint; it does not replace them.

## Quick start

1. Review `config/product-families.yml`.
2. Review `config/appsumo-tool-capabilities.yml`.
3. Create or promote a work order with `scripts/create_work_order.py`.
4. Score family or product opportunities with `scripts/score_product_opportunity.py`.
5. Validate product completeness with `scripts/validate_product_folder.py`.

## Working rules

- One buyer, one pain, one promise, one primary outcome per product.
- Every low-ticket product must ladder into a toolkit, setup sprint, and managed service.
- Every product must map back into the canonical repo stages:
  - `01-market-research`
  - `02-offers`
  - `03-products`
  - `04-sales-pages`
  - `05-email-workflows`
  - `06-launch-playbooks`
  - `09-iteration-and-scale`
- The repo remains the source of truth even if Hermes keeps parallel memory.
