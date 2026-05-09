# Operator System

This folder defines how Hermes, Paperclip, and any managed agents should operate when acting as the business operator for `digitalproducts`.

## Canon

These files are operational canon for autonomous work:

- `FRAMEWORK.md`
- `ROADMAP.md`
- `automation/pipeline.md`
- `10-execution-sprints/current-sprint.md`
- `00-foundation/operator-system/approval-matrix.md`
- `00-foundation/operator-system/20-recurring-workflows.md`
- `00-foundation/operator-system/google-drive-knowledge-base.md`
- `00-foundation/operator-system/browser-ops.md`
- `00-foundation/operator-system/design-tool-routing.md`
- `00-foundation/operator-system/productization-factory-implementation-plan.md`
- `productization-factory/README.md`
- `01-market-research/appsumo/2026-05-08-appsumo-business-factory-map.md`
- `00-foundation/operator-system/governance-stack.md`
- `00-foundation/operator-system/manual-actions-ledger.md`
- `00-foundation/operator-system/mobile-control-center.md`
- `00-foundation/operator-system/observability-and-mobile.md`

## What This Folder Solves

- Defines what agents may do without confirmation
- Defines what still requires an explicit approval gate
- Maps the Google Drive knowledge base that contains operating context
- Turns recurring work into repeatable SOPs
- Documents how browser automation should be launched and verified
- Routes design, landing-page, media, and conversion work through the preferred owned tool stack
- Defines how the Paperclip company, Hermes memory, and Codex implementation layer should build the productization factory
- Routes non-design AppSumo tools by job-to-be-done, engine, and operating-system priority
- Defines how quality, accessibility, release governance, and observability are enforced
- Gives the operator a mobile continuation path and a single manual-action ledger

## Operating Intent

The goal is not passive assistance. The goal is durable operator capacity:

- keep the repo truthful
- keep the board moving
- use APIs first where possible
- use browser automation where APIs are absent
- document blockers instead of silently stalling
- preserve irreversible and high-risk actions behind explicit approval rules

## Deployment Rule

If code, content, configuration, or agent behavior changes because of work done by Hermes or Paperclip, the repo should be updated to reflect the new truth.

## Bootstrap

Run the operator-mode bootstrap from the repo when you need to resync secrets or reapply the agent fleet configuration:

```powershell
cd "C:\Users\ohu00\Desktop\digitalproducts"
.\ops\paperclip\enable-operator-mode.ps1 -EnableStrictMode
```

This bootstrap:

- syncs the curated SaaS and infrastructure secrets from `C:\Users\ohu00\Documents\.env` into Paperclip `local_encrypted` storage
- upgrades the existing agent fleet to use browser and research toolsets
- adds secret-backed environment bindings to managed agents
- enables agent heartbeats
- creates the `Browser Operations Lead` role if it does not already exist
- can switch the Paperclip instance to strict secret mode

## Governance artifacts

The repo-level governance workspace lives at the root and is anchored by:

- `package.json`
- `playwright.config.mjs`
- `.pa11yci.json`
- `.lighthouserc.json`
- `.storybook/`
- `tests/e2e/suitedash-preview.spec.js`
- `governance/release-state.json`
- `.github/workflows/quality-gates.yml`
- `.github/workflows/release-governance.yml`
- `.github/workflows/scorecards.yml`
