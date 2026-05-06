# Gumroad Workflows

Native email automation in Gumroad. Zero integration work, fires on the right triggers, free.

## Available Triggers

- **New subscriber** (when someone joins your list via the subscribe form)
- **Customer purchases this product** (per-product post-purchase)
- **Customer purchases anything** (cross-product post-purchase)
- **Cancelled subscription** (for membership / recurring products)
- **Member joins this membership** (for tiered access)
- **Abandoned cart** (single email, 24-hour timer, automatic)

## Setup Per Product

For every product:

1. **Post-Purchase Workflow** — trigger: customer purchases this product
   - Email 1 (0 hours): Welcome + Confirm — see `/05-email-workflows/post-purchase-sequence.md`
   - Email 2 (1 day): Quick Win
   - Email 3 (3 days): Common Mistakes
   - Email 4 (7 days): Case Study
   - Email 5 (14 days): Soft Pitch — Next Step
   - Email 6 (30 days): Testimonial Request

2. **Abandoned Cart Customization** — see `/05-email-workflows/abandoned-cart.md`
   - Customize the subject and body
   - Default 24-hour timer (Gumroad doesn't allow changing this)

## Setup Universally (Account-Level)

3. **New Subscriber Welcome Sequence** — trigger: new subscriber via the subscribe form
   - 5-email welcome sequence (see `/07-traffic-engine/newsletter-structure.md`)
   - Then they roll into the regular Friday newsletter cadence

## Limitations

Gumroad Workflows do *not* support:
- Conditional logic ("if buyer also bought X, send Y")
- A/B testing on subject lines
- Complex segmentation
- Branching based on email opens / clicks

When you need these: graduate to ConvertKit, Beehiiv, or MailerLite, and connect via n8n at `n8n.audreysplace.place`.

## Testing Each Workflow

Before going live with a new workflow:
1. Create a 100% discount code
2. Make a test purchase
3. Verify Email 1 fires immediately (within 5 minutes)
4. For subsequent emails, use the "Send to me now" preview feature

## Reply-To Address

Set the reply-to on every workflow email to a monitored inbox. Replies to launch and post-purchase emails are the highest-quality feedback you'll ever get.
