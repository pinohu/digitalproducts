# Approval Matrix

This matrix defines which actions agents may execute autonomously, which require confirmation, and which are prohibited without human intervention.

## Autonomous

Agents may do these without asking first:

- read and summarize Google Drive files that are already accessible
- read and update repo files
- create, refine, and close Paperclip issues
- run local tests, audits, builds, and staging validations
- create preview or staging deployments
- draft copy, SOPs, assets, briefs, and internal documentation
- create or patch automations that do not spend money or affect live customers
- update non-destructive CRM records, notes, tags, and internal statuses
- use browser automation for read-only workflows and low-risk data entry
- create dashboards, scorecards, and structured research inventories
- connect tools through already-authorized APIs when the action is reversible

## Confirmation Required

Agents must pause for explicit confirmation before:

- sending outbound campaigns to real customers or leads at scale
- publishing or replacing live sales copy that changes revenue claims, pricing, guarantees, or legal language
- changing DNS, domains, SSL, or live routing
- rotating root credentials or MFA methods
- altering billing settings, subscription plans, or tax settings
- deleting production content, databases, or customer records
- moving from preview/staging to production when customer impact is immediate
- creating or approving net-new agent roles that materially widen permissions
- using browser automation to submit forms that create financial, legal, or contractual commitments

## Never Autonomous

Agents must not do these on their own:

- spend money beyond pre-authorized SaaS usage
- initiate wire transfers, ACH transfers, or card purchases
- sign contracts or agree to legal terms on your behalf
- file taxes, legal filings, or regulated compliance submissions
- delete the primary source-of-truth Drive folders or business repos
- disable your access, remove your admin role, or lock you out of core systems
- publish fabricated testimonials, fake case studies, or false revenue claims

## Conflict Rule

If a task looks autonomous in one place but risky in practice, treat it as `confirmation required`.

## Browser Rule

Browser automation may proceed autonomously only when all of the following are true:

- the session is already authenticated
- the action is reversible or low-risk
- the target is operational, not legal or financial
- the workflow is documented in `20-recurring-workflows.md`

Otherwise, stop and require confirmation.
