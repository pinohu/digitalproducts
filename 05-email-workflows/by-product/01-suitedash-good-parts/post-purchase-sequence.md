# The Good Parts of SuiteDash — Post-Purchase Workflow Draft

Trigger: Customer purchases The Good Parts of SuiteDash in Gumroad.

Source inputs:
- `03-products/01-suitedash-good-parts/README.md`
- `05-email-workflows/post-purchase-sequence.md`
- `ROADMAP.md` Definition of Done: 0hr / day 1 / day 3 / day 7 / day 14 / day 30 workflow must be live before product is shipped.

Status: Drafted for Gumroad Workflows. Not live until Gumroad product, download links, and reply-to address are configured. DIG-23 live activation blocker handoff lives at `gumroad-workflow-activation-status.md`.

Placeholders to replace before publishing:
- `[DOWNLOAD_LINK]`
- `[NEXT_RUNG_LINK]` or remove until next-rung offer exists
- `[NAME]`

---

## Email 1 — 0 hours: Welcome + download

Subject: Welcome — The Good Parts of SuiteDash is inside

Preview: Thanks for grabbing it. Here is the download link in case Gumroad hides it.

Body:

Hey [first name],

Thanks for grabbing The Good Parts of SuiteDash.

Download it here: [DOWNLOAD_LINK]

I made this because SuiteDash has a strange problem: the platform is useful, but the useful path is buried under too many features. Most technically capable operators do not need another tutorial. They need a filter, a setup order, and permission to skip the parts that do not matter yet.

As you go through it, hit reply and tell me what is resonating, what is confusing, and what is missing. I read every reply, and those notes become version 2.

If you get stuck, reply to this email. Keep your message specific: name the workflow you chose, where you got stuck, and what decision is blocking you.

[NAME]

P.S. Fastest path: open the 90-Minute Lock-In Protocol first, then read the core PDF with that checklist beside you.

---

## Email 2 — Day 1: Quick win

Subject: The 15-minute SuiteDash audit

Preview: If you only do one thing today, do this.

Body:

Hey [first name],

If you only have 15 minutes with The Good Parts of SuiteDash today, do this:

Open the “7 modules that actually matter” section and compare it against your current SuiteDash setup.

For each module, mark one of three states:

1. In use and configured well.
2. Needed but not configured yet.
3. Not needed right now.

That single pass usually exposes the real issue: most SuiteDash accounts are not underbuilt. They are cluttered with features that looked important before the actual workflow was clear.

Do not try to rebuild everything today. Just identify the modules that belong in your first deployment.

[NAME]

---

## Email 3 — Day 3: Common mistakes

Subject: Stuck? It is probably one of these three things.

Preview: Most SuiteDash rebuild loops start here.

Body:

Hey [first name],

By now you have probably hit at least one SuiteDash decision that feels bigger than it should.

Most people get stuck in one of three places:

**Mistake #1: Customizing before deciding the workflow.** Configure the client journey first. Brand polish comes after the workflow is usable.

**Mistake #2: Turning on too many modules at once.** SuiteDash can do a lot. Your first deployment should not. Start with the modules that support one clear client path.

**Mistake #3: Building automations before the manual process is clear.** If you cannot describe the handoff in plain English, the automation will hide the mess instead of fixing it.

If you are hitting one of these, you are normal. If you are hitting a different wall, reply and tell me where. I want to know what is missing from the next version.

[NAME]

---

## Email 4 — Day 7: Use case / case study slot

Subject: The setup pattern I would start with

Preview: If your SuiteDash account still feels too broad, narrow it to this.

Body:

Hey [first name],

Here is the use case I would start with if SuiteDash still feels too broad:

**Client onboarding + status visibility.**

That means:

- Intake form captures the right setup details.
- Client portal gives one obvious place to find files, tasks, and next steps.
- Project/status workflow tells the client what is happening without another manual email.
- One automation moves the client from intake to the next operational state.

Do not start with every possible SuiteDash feature. Start with the flow that removes repeated client-update work.

Beta testimonial slot: once real beta feedback exists, replace this email with a specific reader story and outcome.

[NAME]

---

## Email 5 — Day 14: Next step

Subject: When you are ready for the next layer

Preview: The PDF helps you choose the path. The next problem is implementation.

Body:

Hey [first name],

If you have been working through The Good Parts of SuiteDash, you are probably starting to see the next wall:

Knowing the right setup path is not the same as having the whole thing implemented.

That is where the natural next rung will live: a deeper SuiteDash setup service, walkthrough, or operator cohort for people who want help turning the map into a working deployment.

No pressure. If you are still using the guide, keep going. If you want the next layer when it exists, use this link: [NEXT_RUNG_LINK]

And remember: the 30-day guarantee is still active. If the guide has not been worth it, reply with “refund” and you are done. No hoops.

[NAME]

---

## Email 6 — Day 30: Testimonial request

Subject: Did this save you time?

Preview: Quick favor — and I want the honest answer.

Body:

Hey [first name],

It has been 30 days since you grabbed The Good Parts of SuiteDash.

Quick question: did it save you time or help you make a clearer SuiteDash decision?

If yes, would you reply with a 2-3 sentence testimonial I can use on the sales page?

The most useful format is specific:

“Before this, I was stuck on ____. After reading it, I _____. It saved me roughly ____ hours / helped me decide ____.”

If no, also reply. I want to know what did not land, what was missing, or where SuiteDash still felt confusing. No hard feelings — the guarantee exists for a reason.

Either way, thanks for trying it.

[NAME]

---

## Gumroad setup checklist

- [ ] Product created in Gumroad.
- [ ] Download URL added to Email 1.
- [ ] All 6 workflow emails created with correct delays: 0 hours, 1 day, 3 days, 7 days, 14 days, 30 days.
- [ ] Reply-to address routes to monitored inbox.
- [ ] Test purchase via 100% discount code confirms Email 1 fires.
- [ ] Day 14 next-rung link either configured or copy revised to remove it.
- [ ] Day 30 testimonial request incentive chosen, if any.

## External blockers

- Gumroad product/admin access required to make workflow live.
- Final deliverable upload required before download link can be inserted.
- Next-rung offer link is not defined yet.
- Testimonials do not exist yet; Day 7 and Day 30 should feed the testimonial bank once buyers respond.
