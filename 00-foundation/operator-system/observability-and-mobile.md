# Observability and Mobile Operation

## Observability sources

- `governance/release-state.json`: machine-readable release gate truth
- `npm run observability:summary`: console summary for current release blockers
- GitHub Actions artifacts:
  - Playwright HTML report
  - Storybook static build
  - Lighthouse reports
  - Scorecard SARIF
- `Paperclip`: live task orchestration and issue status
- `10-execution-sprints/current-sprint.md`: human-readable execution narrative

## Mobile-friendly checkpoints

When checking from a phone, the fastest truth sources are:

- `mobile-control-center.md`
- `manual-actions-ledger.md`
- `current-sprint.md`
- `ROADMAP.md`

## Expected artifact cadence

- Every UI or governance change should produce fresh Playwright, Pa11y, and Lighthouse evidence on GitHub.
- Every change to production-readiness truth should be reflected in `governance/release-state.json`.
- Every new operator-side blocker should be recorded in the manual-actions ledger or the AppSumo operator-input bundle.
