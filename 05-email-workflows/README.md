# 05 · Email Workflows

Every product ships with email workflows live on day one. The post-purchase sequence is the single highest-leverage marketing asset in the entire stack — it's the only place buyers are 100% paying attention to messages from us, and it's the bridge between Product N and Product N+1.

## Files in this folder

- [`post-purchase-sequence.md`](./post-purchase-sequence.md) — The 6-email sequence that runs after every purchase.
- [`waitlist-sequence.md`](./waitlist-sequence.md) — Pre-launch nurture for people who joined the waitlist.
- [`launch-sequence.md`](./launch-sequence.md) — The 7-day launch email sequence (founding-price window).
- [`abandoned-cart.md`](./abandoned-cart.md) — Cart abandonment recovery (Gumroad handles this natively).
- [`nurture-sequence.md`](./nurture-sequence.md) — Long-tail nurture for the email list between launches.
- `by-product/<slug>/` — Customized versions of each sequence for each specific product.

## Platform Notes

For first 1–2 products: use **Gumroad Workflows**. They're free, they trigger on the right events (purchase, subscriber, abandoned cart), and they require zero integration work. The trade-off: limited segmentation, plain-text design, no advanced personalization.

When the email list crosses ~2,500 subscribers OR when sequences need conditional logic, graduate to **ConvertKit**, **Beehiiv**, or **MailerLite**, with Gumroad → email-tool sync via n8n.

Don't graduate too early. Most solopreneurs over-engineer their email setup before they need to.

## Email Performance Targets

| Metric | Floor | Target | Best |
|---|---|---|---|
| Open rate (post-purchase email #1) | 60% | 75% | 90%+ |
| Open rate (nurture email) | 25% | 35% | 50%+ |
| Click rate (sales email) | 3% | 7% | 15%+ |
| Conversion to next-rung product | 5% | 10% | 20%+ |
| Reply rate (asking for feedback) | 2% | 5% | 10%+ |

## Writing Principles

- **One idea per email.** No "and also..." mid-email pivots.
- **Subject lines under 50 characters.** Mobile previews truncate after that.
- **First line is a continuation of the subject.** Inbox preview = subject + first line. Both work together to earn the open.
- **One CTA per email.** Two CTAs = neither happens.
- **Plain text > designed templates.** Plain emails feel like 1:1 messages. Designed emails feel like newsletters. The former converts better at the post-purchase stage.
- **Reply asks beat link clicks.** Asking for a reply ("hit reply and tell me what you're stuck on") boosts deliverability, drives feedback, builds relationship.
