# The Good Parts of SuiteDash — Manuscript Outline

**Target:** ~30 PDF pages. 8 chapters + intro + outro. ~7,500–9,000 words total.

**Voice:** Direct. Numbers. Frameworks. Builder-to-builder. No hype words.

**Reader's promise:** They finish this in 60 minutes of reading and walk away with a deployable plan.

---

## Front Matter

- Title page
- One-page TL;DR ("If you only read one page")
- How to use this PDF (the recommended reading + execution order)

---

## Chapter 1 — Why SuiteDash Is the Way It Is

- Why SuiteDash competes on feature breadth (HubSpot + ClickUp + Basecamp + Dubsado + ClientPortal in one license)
- Why that breadth is the source of the configuration problem — not a bug, a deliberate trade-off
- The mental model shift: stop trying to "learn SuiteDash"; start picking the 7 modules you'll actually run
- The ROI math on the LTD: what payback looks like at 1, 3, and 5 active clients

## Chapter 2 — The 7 Modules That Matter

The opinionated module short-list, with one paragraph per module on what it does, what to configure first, and what to ignore inside it:

1. **CRM / Contacts** — the spine of the whole system
2. **Projects / Tasks** — the operational layer
3. **Client Portals** — the customer-facing surface
4. **Files / Folders** — shared deliverables, version control
5. **Forms** — the intake gateway
6. **Automations (Flows)** — the multiplier
7. **Templates** — the reusability layer

## Chapter 3 — The 12 Modules to Skip (and Why)

A short paragraph on each of 12 SuiteDash features that exist but should not consume your configuration time at this stage. Reasoning patterns: replaceable by purpose-built tool, brittle, low ROI on config time, over-promised, niche use case.

## Chapter 4 — The Configuration Order

The sequence in which to configure SuiteDash so you don't rebuild later. Why this order matters (each step depends on the previous one). The 7-step sequence:

1. Branding + subdomain
2. Custom fields on CRM contacts
3. Pipeline / lifecycle stages
4. Project + task templates
5. Forms + intake
6. Client portal templates
7. Automations on top

## Chapter 5 — Automation Pattern #1: Intake-to-Portal Pipeline

The end-to-end flow:

- Form submission → CRM contact created with custom fields
- Project spawned from template, assigned to lifecycle stage "Onboarding"
- Client portal provisioned with the project + welcome assets
- Welcome email triggered with portal credentials
- Internal Slack/email notification fires to operator

Includes exact UI breadcrumbs, the trigger / condition / action pattern, and the 4 mistakes that break this in production.

## Chapter 6 — Automation Pattern #2: Template-Driven Project Spawning

The reusability play:

- One project template per service line
- Spawning logic (manual, automated, or form-triggered)
- Task pre-population with assigned roles, durations, and dependencies
- Portal-side visibility settings (what the client sees vs. internal)
- The 80/20: 1–3 templates cover 90% of agency project types

Why this pattern is what makes SuiteDash beat Notion/ClickUp on operational throughput.

## Chapter 7 — When SuiteDash Is the Wrong Tool

Honest comparison vs. the four serious alternatives:

- **Notion** — when knowledge graph + flexibility matter more than client-facing structure
- **Basecamp** — when fewer-but-deeper features and lighter onboarding matter
- **ClickUp** — when internal task complexity exceeds client-portal complexity
- **Custom build (Supabase + Next.js + custom portal)** — when you're past 10 active clients and SuiteDash's customization ceiling becomes a constraint

Decision rubric included: 5 yes/no questions to make the call in 60 seconds.

## Chapter 8 — The 90-Minute Lock-In Path

A condensed step-by-step that walks the reader through the actual deployment, calibrated to a 90-minute time budget. Mirrors the structure of Bonus #1 but with the *why* behind each step.

Time allocation:
- 0–10 min: branding + subdomain
- 10–25 min: CRM custom fields + pipeline
- 25–45 min: projects + task templates
- 45–60 min: forms + intake
- 60–75 min: client portal template
- 75–90 min: first automation live (intake-to-portal)

---

## Closing — What's Next

- Recap of the 7-modules / 12-skips / 1-protocol structure
- The natural next problem (you have a deployment; now what?)
- CTA to the next ladder rung (SuiteDash Setup Service / Dynasty Operator Cohort)
- Reply-to-this-email ask: testimonial in 30 days for free upgrade
