# The Good Parts of SuiteDash — Abandoned Cart Draft

Trigger: Checkout started but purchase not completed, if Gumroad abandoned-cart workflow is available for this product.

Source inputs:
- `05-email-workflows/abandoned-cart.md`
- `02-offers/by-product/01-suitedash-good-parts.md`
- `ROADMAP.md` Definition of Done: abandoned cart workflow must be enabled before shipped status.

Status: Drafted. Not enabled until Gumroad checkout/product exists. DIG-23 live activation blocker handoff lives at `gumroad-workflow-activation-status.md`.

Placeholders:
- `[CHECKOUT_LINK]`
- `[FOUNDING_DEADLINE]`
- `[NAME]`

---

## Email — 24 hours after cart abandon

Subject: Still want the SuiteDash shortcut?

Preview: Your checkout did not finish. Here is the link again.

Body:

Hey [first name],

Looks like you started checkout for The Good Parts of SuiteDash but did not finish.

If that was intentional, no problem. If Gumroad got in the way or you wanted to come back later, here is the link again:

[CHECKOUT_LINK]

Quick reminder of what is inside:

- The core PDF: the 90-minute opinionated path through the SuiteDash modules that matter first.
- The 90-Minute SuiteDash Lock-In Protocol.
- 7 SuiteDash Automation Recipes.
- The Kill List: 12 SuiteDash features to ignore until later.

Total value: $540. Founding price: $29 until [FOUNDING_DEADLINE], then public price is $49.

And it is covered by the 30-day money-back guarantee. If it does not clarify your SuiteDash setup path, reply “refund” and you are done.

Finish checkout here: [CHECKOUT_LINK]

[NAME]

---

## Enablement checklist

- [ ] Gumroad product checkout URL inserted.
- [ ] Founding deadline inserted only after discount code exists.
- [ ] Workflow enabled in Gumroad abandoned-cart settings.
- [ ] Test abandoned checkout confirms email timing and CTA.
- [ ] Disable or revise founding-price language after 48-hour launch window closes.

## External blockers

- Requires Gumroad product/admin access.
- Requires live checkout URL.
- Requires real founding discount deadline.
