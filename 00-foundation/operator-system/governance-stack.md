# Governance Stack

This repo now has an explicit governance layer instead of relying on informal judgment.

## Owners

- `Chief of Staff`: overall governance owner; decides what is ready to close and what must stay blocked.
- `Quality Gatekeeper`: owns CI quality, failing checks, and release evidence.
- `Accessibility Auditor`: owns WCAG 2.2 AA enforcement, keyboard flow review, focus states, and form usability.
- `Release Governor`: owns release readiness, evidence quality, rollback notes, and production gating.
- `Product Builder`: owns UI implementation quality, mobile fit, clarity, and visual consistency.
- `Browser Operations Lead`: owns end-to-end logged-in verification where APIs are not enough.

## Enforced stack

The repo-level governance workspace integrates these tools:

- `Playwright` for end-to-end browser checks and mobile smoke coverage.
- `axe-core` via `@axe-core/playwright` for blocking accessibility violations in tests.
- `Pa11y` for URL-level accessibility smoke checks.
- `Lighthouse CI` for accessibility, best-practices, SEO, and performance budgets.
- `Storybook` for visual review and mobile/desktop iframe review of the landing page.
- `Changesets` for release-note discipline and intentional governance changes.
- `OPA` for policy-as-code release gating using `governance/release-state.json`.
- `OpenSSF Scorecard` for repository security posture and supply-chain observability.

## Repo entry points

- `package.json`
- `playwright.config.mjs`
- `.pa11yci.json`
- `.lighthouserc.json`
- `.storybook/`
- `tests/e2e/suitedash-preview.spec.js`
- `governance/release-state.json`
- `governance/policies/release.rego`
- `.github/workflows/quality-gates.yml`
- `.github/workflows/release-governance.yml`
- `.github/workflows/scorecards.yml`

## Browser runtime setup

Run `npm run quality:setup` before collecting local browser evidence in a fresh clone or WSL environment. The command installs the Playwright Chromium used by `npm run test:e2e` and the Puppeteer Chrome used by `npm run test:a11y`.

On Linux/WSL the browser binaries also require OS shared libraries. GitHub Actions handles this through `npx playwright install --with-deps chromium`; local WSL runs may still need the equivalent system packages installed by an operator with sudo access before Playwright, Pa11y, or Lighthouse results count as current evidence.

Do not mark `governance/release-state.json` quality booleans true unless the corresponding gate has actually passed in the current environment or a fresh GitHub Actions artifact exists.

## What "done" means now

Work is not complete just because an agent stopped. It is complete only when:

- the repo truth matches reality;
- the relevant quality gates pass or are explicitly exempted with reason;
- accessibility and mobile behavior are reviewed;
- release-state still describes the real launch situation;
- the remaining blockers are documented honestly.
