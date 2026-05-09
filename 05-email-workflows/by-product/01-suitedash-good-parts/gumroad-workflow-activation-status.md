# Gumroad Workflow Activation Status — The Good Parts of SuiteDash

Owner: Funnel and Launch Ops
Related issues: DIG-23, DIG-30
Operating date: 2026-05-08 sprint day / 2026-05-07 local system date
Status: blocked on live Gumroad product/download URL, checkout/founding URL, workflow admin evidence, and monitored reply-to inbox; workflow drafts are ready to paste.

## Executive status

DIG-23 cannot be truthfully completed as live Gumroad Workflows from this environment because the upstream Gumroad product has not been created and no Gumroad admin access/session is available. The workflow copy is drafted and mapped to the ROADMAP.md Definition of Done timing requirements, but it cannot be enabled until the live product, download URL, checkout URL, founding deadline, and monitored reply-to inbox exist.

## Definition of Done mapping

ROADMAP.md requires these workflow items before shipped status:

- Post-purchase email workflow live at 0hr / day 1 / day 3 / day 7 / day 14 / day 30
- Abandoned cart workflow enabled
- Gumroad deliverable uploaded and download link working
- First sale/test purchase evidence recorded before shipped catalog update

Current DIG-23 state:

| DoD item | Repo source | Live status |
|---|---|---|
| 0hr welcome + download | `post-purchase-sequence.md` Email 1 | BLOCKED: needs Gumroad product + download URL |
| Day 1 quick win | `post-purchase-sequence.md` Email 2 | BLOCKED: needs Gumroad Workflow admin access |
| Day 3 common mistakes | `post-purchase-sequence.md` Email 3 | BLOCKED: needs Gumroad Workflow admin access |
| Day 7 use case / proof slot | `post-purchase-sequence.md` Email 4 | BLOCKED: needs Gumroad Workflow admin access; replace proof slot if DIG-25 resolves |
| Day 14 next step | `post-purchase-sequence.md` Email 5 | BLOCKED: needs Gumroad Workflow admin access; next-rung link can be removed until defined |
| Day 30 testimonial request | `post-purchase-sequence.md` Email 6 | BLOCKED: needs Gumroad Workflow admin access |
| Abandoned cart at 24hr | `abandoned-cart.md` | BLOCKED: needs live checkout URL + founding deadline + abandoned-cart settings access |

## Gumroad post-purchase workflow to create

Trigger: customer purchases `The Good Parts of SuiteDash`.

Create these emails with these delays:

1. `0 hours` — Subject: `Welcome — The Good Parts of SuiteDash is inside`
2. `1 day` — Subject: `The 15-minute SuiteDash audit`
3. `3 days` — Subject: `Stuck? It is probably one of these three things.`
4. `7 days` — Subject: `The setup pattern I would start with`
5. `14 days` — Subject: `When you are ready for the next layer`
6. `30 days` — Subject: `Did this save you time?`

Source copy: `05-email-workflows/by-product/01-suitedash-good-parts/post-purchase-sequence.md`

Required replacements before enabling:

- `[DOWNLOAD_LINK]` → live Gumroad file/download link or product library link
- `[NEXT_RUNG_LINK]` → remove or replace with a real next-rung/waitlist link
- `[NAME]` → sender name/brand signature
- reply-to inbox → monitored support/customer-reply inbox

## Gumroad abandoned-cart workflow to enable

Trigger: checkout started but purchase not completed.
Timing: 24 hours after cart abandon, or Gumroad default abandoned-cart timing if it cannot be customized.

Source copy: `05-email-workflows/by-product/01-suitedash-good-parts/abandoned-cart.md`

Required replacements before enabling:

- `[CHECKOUT_LINK]` → live Gumroad checkout/founding URL
- `[FOUNDING_DEADLINE]` → exact launch-window deadline once discount exists
- `[NAME]` → sender name/brand signature

After the 48-hour founding window closes, remove or revise founding-price language so the email does not promise an expired discount.

## Exact external blockers

1. Gumroad product URL and product ID do not exist yet in repo.
2. Gumroad admin access/session is unavailable in this environment.
3. Product download URL cannot be inserted until DIG-22 creates/uploads the live Gumroad product.
4. Checkout URL/founding discount URL cannot be inserted until DIG-22 creates the product and discount.
5. Final founding deadline/timezone is not set.
6. Monitored support/reply-to inbox is not available.
7. Permission to run a test purchase or 100% discount-code test is not available.
8. DIG-25 permissioned proof/testimonials are still pending; do not insert fabricated beta proof into the Day 7 email or social-proof blocks.

## Operator enablement checklist

Once DIG-22 produces the live product/download URL:

1. Open Gumroad product admin for `The Good Parts of SuiteDash`.
2. Create a product-specific post-purchase workflow triggered by purchase.
3. Paste all 6 emails from `post-purchase-sequence.md`.
4. Set delays to 0 hours, 1 day, 3 days, 7 days, 14 days, and 30 days.
5. Replace `[DOWNLOAD_LINK]`, `[NAME]`, and `[NEXT_RUNG_LINK]`/remove next-rung language.
6. Set reply-to to the monitored support/customer inbox.
7. Enable Gumroad abandoned-cart recovery for the product.
8. Paste abandoned-cart copy from `abandoned-cart.md` if Gumroad allows custom copy; otherwise confirm Gumroad default is enabled and record the limitation.
9. Replace `[CHECKOUT_LINK]` and `[FOUNDING_DEADLINE]` in abandoned-cart copy.
10. Run a test purchase and confirm the 0hr email arrives within 5 minutes.
11. Start an abandoned checkout test and confirm the recovery email timing/settings.
12. Record evidence and final URLs in this file, `01-suitedash-good-parts-activation-checklist.md`, `analytics/by-product/01-suitedash-good-parts.md`, and current sprint docs.

## DIG-30 post-unblock execution attempt — 2026-05-08

DIG-30 was selected as the highest-priority actionable Funnel and Launch Ops issue because it is assigned and in progress, but its acceptance criteria depend on DIG-29 live URLs/evidence. That upstream evidence is still absent: this runtime has no `GUMROAD_*` environment variables, no Gumroad admin/session credential, and no repo-visible live Gumroad product URL, checkout/founding URL, download URL, product ID, final founding deadline/timezone, monitored reply-to inbox, or workflow-admin screenshot/evidence.

Result: no live workflow can be truthfully enabled from this environment. The post-purchase 0hr/day1/day3/day7/day14/day30 sequence and abandoned-cart copy remain ready to paste once DIG-29 supplies live product/download/checkout URLs and an operator supplies Gumroad workflow/admin access.

DIG-30 acceptance remains incomplete until all of the following are recorded in this file and the activation checklist:

- Gumroad product URL and product ID.
- Gumroad checkout URL and founding discount URL.
- Final founding-price deadline and timezone.
- Monitored support/reply-to inbox used for workflow replies.
- Post-purchase workflow admin evidence showing 0hr/day1/day3/day7/day14/day30 emails enabled.
- Abandoned-cart recovery evidence showing the workflow/settings are enabled for this product.
- Test purchase evidence confirming the 0hr email arrives within 5 minutes.
- Abandoned-checkout test evidence or a recorded Gumroad limitation if custom abandoned-cart testing is unavailable.

## Current DIG-23/DIG-30 outcome

Repo-side workflow mapping is complete and exact platform blockers are documented. No live workflow, abandoned-cart recovery, or 0hr welcome email can be claimed until Gumroad product/admin access, live checkout/download URLs, and test evidence exist.
