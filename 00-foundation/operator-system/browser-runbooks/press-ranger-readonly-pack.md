# Press Ranger Read-Only Browser Operator Pack

Verification timestamp: 2026-05-08T07:33:01Z
Operator: Browser Operations Lead
Related issue: DIG-50

## Security handling

- Runtime-only credential sources were inspected without copying raw usernames, passwords, cookies, session tokens, AppSumo codes, private contact records, or media-list exports into this document.
- Source files checked:
  - `C:\Users\ohu00\Downloads\tigertail-product-list-07-05-2026.csv`
  - `C:\Users\ohu00\Documents\SOFTWARE TOOLS LOGIN CREDENTIALS.txt`
  - `C:\Users\ohu00\Documents\.env`
- The secure dotenv contains no obvious Press Ranger API key material.
- The credential file contains no Press Ranger-specific credential entry, but existing generic credential-pool material authenticated successfully at runtime. Credential values and session cookies were not stored.
- Inspection stayed browser/read-only. No companies, campaigns, press releases, lists, relationships, team members, billing settings, or account settings were created or changed.

## Access classification

Status: `browser_dashboard_verified_readonly`

Press Ranger is a viable reusable browser-operated surface in read-only mode.

Verified entry paths:

- Public site: `https://pressranger.com/` (the `www` URL redirects to this host)
- Login: `https://pressranger.com/login`
- Authenticated dashboard: `https://pressranger.com/dashboard`

Authentication result:

- Login page title observed: `Login - Press Ranger`
- Dashboard title observed after runtime-only credential entry: `Welcome - Press Ranger`
- The authenticated dashboard rendered without login inputs and exposed account navigation for dashboard, media databases, campaigns, press releases, settings, team, companies, and billing.
- No MFA or reCAPTCHA blocker was observed during this pass.

## Reusable operator surface

Highest-value read-only surfaces verified by authenticated navigation:

1. Dashboard overview
   - Route: `/dashboard`
   - Use: account readiness summary, company-profile status, CRM summary, suggested media recommendations, and quick links into guides/campaigns/press releases.
   - Safe read-only checks: page loads, company profile present/missing, suggested-recommendation module present, CRM empty/non-empty state, guide links.

2. Journalist database
   - Route: `/journalists`
   - Use: media discovery and fit review.
   - Safe read-only checks: search/filter form availability, pagination availability, detail-page link availability, relationship/status controls present.
   - Do not store raw journalist lists, emails, or scraped contact records in repo output.

3. Podcast database
   - Route: `/podcasts`
   - Use: podcast outreach discovery.
   - Safe read-only checks: search/filter availability, pagination availability, detail-page link availability.
   - Do not export or persist podcast/contact lists.

4. Publisher database
   - Route: `/publishers`
   - Use: publisher/outlet discovery and targeting.
   - Safe read-only checks: search/filter availability, pagination availability, detail-page link availability.
   - Do not export or persist outlet/contact lists.

5. AI campaigns
   - Route: `/campaigns`
   - Use: campaign inventory and readiness review.
   - Observed state: campaign page was reachable and exposed create/start actions.
   - Safe read-only checks: existing campaign count/statuses if present, draft/published state, page accessibility.
   - Do not create campaigns, generate pitches, send outreach, or change campaign state without a separate write issue.

6. Press releases
   - Route: `/press-releases`
   - Use: press-release inventory and publication-readiness review.
   - Observed state: page was reachable and exposed a create action plus an inventory table shell.
   - Safe read-only checks: count/status summary only, title/status/date metadata if a future issue explicitly allows data-minimized inventory.
   - Do not create, edit, submit, publish, pay for, or distribute press releases without a separate write issue.

7. Account settings
   - Route: `/settings`
   - Use: verify account profile fields are present.
   - Safe read-only checks: account page reachable, profile completeness high-level only.
   - Do not change profile fields, password, email, preferences, or API/account settings.

8. Team settings
   - Route: `/settings/team`
   - Use: team-seat and invite-surface awareness.
   - Safe read-only checks: page reachable, plan/upgrade gate visible, team area present.
   - Do not invite users, remove users, change roles, or upgrade seats.

9. Company settings
   - Route: `/settings/companies`
   - Use: company-profile inventory/readiness.
   - Observed state: companies page reachable with add-company/help actions and table shell.
   - Safe read-only checks: count only and profile-completeness status if visible.
   - Do not add, edit, delete, or select companies unless a separate write contract defines the exact change.

10. Billing/settings
    - Route: `/settings/billing`
    - Use: plan/license/readiness awareness.
    - Safe read-only checks: current plan/tier status at a high level only.
    - Do not upgrade, redeem codes, change plans, submit payments, or alter billing details.

## First safe read-only workflows

1. Account readiness check
   - Open `/dashboard`, `/settings`, `/settings/companies`, and `/settings/billing`.
   - Report only: authenticated yes/no, company profile present/missing, billing/plan gate visible, and whether campaign/press-release actions are available.

2. PR campaign readiness map
   - Open `/campaigns` and `/press-releases`.
   - Report only: pages reachable, existing inventory count/status summary if visible, and whether create actions are present.
   - Do not open paid distribution flows or submit content.

3. Media discovery capability check
   - Open `/journalists`, `/publishers`, and `/podcasts`.
   - Report only: database page reachable, filters present, pagination present, and detail links present.
   - Do not export, scrape, or persist individual contacts/media rows.

4. Documentation-assisted runbook check
   - Open `https://pressranger.com/docs/getting-started/dashboard-overview` from the dashboard guides link.
   - Summarize public docs only; do not mix private dashboard data into public docs output.

## Explicit blockers and constraints

- No Press Ranger-specific API key or API documentation was found in the inspected secure dotenv, so this should be treated as a browser-operated surface rather than an API connector.
- Browser automation reliability blocker: the default ChromeOps profile was locked by another live process and the Linux Playwright Chromium was missing NSS/NSPR shared libraries. Verification was completed through a dedicated Windows Chrome remote-debug profile instead.
- Do not store raw credentials, cookies, session IDs, media database rows, private contact details, campaign content, press-release drafts, or billing/payment details in repo output.
- Do not trigger state-changing controls: create campaign, create press release, add company, add list, mark media relationship/status, send/publish/distribute, invite team, upgrade plan, redeem license, or change account/billing settings without a separate write-authorized issue.

## Recommendation

Promote Press Ranger from `browser_deferred` to `browser_dashboard_verified_readonly` in the AppSumo access ledger. It is a strong PR/outreach operator candidate for launch-readiness work, especially for media database capability checks and press-release/campaign inventory summaries. The first production-safe integration should be a read-only browser runbook, not an API connector or automation that touches outreach/distribution state.
