# The Good Parts of SuiteDash

*The 7 modules that matter, the 12 to skip, and the 90-minute deployment path for operators who already know what they're doing.*

— Ike Ohu / Dynasty Empire

---

## TL;DR (Read This First)

If you only read one page of this PDF, read this one.

SuiteDash is not a tool you learn. It's a tool you configure. The difference matters: "learning" implies you should understand all 19 modules. "Configuring" means you pick the 7 that move revenue and ignore the rest.

The 7 modules that matter: CRM/Contacts, Projects/Tasks, Client Portals, Files/Folders, Forms, Automations, Templates. Configure them in that order. Don't touch the other 12 until you have a live client portal running.

The two automations that pay back the LTD inside week one: (1) an intake-to-portal pipeline that turns a form submission into a provisioned client in under 30 seconds and (2) template-driven project spawning that turns one click into a fully-populated project with tasks, files, and portal access.

Skip Estimates, LMS, Marketing Campaigns, Affiliate Tracker, the AI tools, and seven other features. They exist; they're not where the leverage is at this stage.

If you do nothing else this week, run Bonus 1 (the 90-Minute Lock-In Protocol). Everything else compounds from there.

---

## How to Use This PDF

This document is structured as a deployment guide, not a textbook. Read it in order. After Chapter 4, stop reading and start configuring — Chapter 8 (and Bonus 1) walk you through the actual deployment in real time.

Estimated time:
- Read: 50–70 minutes
- Configure (with the protocol): 90 minutes
- Total to live deployment: under three hours

Total page count: ~30 pages. Word count: ~8,000.

---

## Chapter 1 — Why SuiteDash Is the Way It Is

SuiteDash markets itself as an all-in-one. That's accurate, and it's the source of every problem you've had with it.

The product replaces, in a single license: HubSpot CRM (contacts, pipelines), ClickUp or Asana (projects, tasks), Basecamp (client portals, messaging), Dubsado (proposals, contracts, invoicing), Dropbox or ClientPortal (file sharing), Typeform or JotForm (intake forms), Calendly (scheduling), and Mailchimp's transactional layer (email automations). For an LTD price of $149–$499, that math is brutal in your favor — the replacement value is $200–$400 per month in subscriptions cancelled.

But here's what nobody tells you when you buy the license: SuiteDash is built to win a feature-checkbox war against eight competitors simultaneously. The UI exposes 19 modules. The default configuration is "everything is on." The onboarding videos walk you through every one of them in feature order, not in deployment order. There is no opinionated default. There is no "start here" button that takes you to a working state.

This is not a UX failure. It's a deliberate market position. SuiteDash's job is to be replaceable for any of those 8 specialists. Yours is to pick which 2–3 of the specialists you actually want to replace, configure those modules, and ignore the rest.

**The mental model shift:** stop trying to "learn SuiteDash." You will not learn it. There is too much surface area and most of it doesn't apply to your business. Instead, treat SuiteDash like a 19-drawer toolbox: pick the 7 drawers you'll open weekly, configure those, and never look in the other 12.

**The ROI math on the LTD.** Assume you bought a Pinnacle license at $499 (mid-tier AppSumo pricing). Assume you currently pay for: Basecamp ($15/user × 4 = $60), Dubsado ($40), JotForm ($35), and a shared Google Drive Workspace seat for clients ($12). That's $147/month of replaceable spend. Cancelling all four pays back the LTD in 3.4 months. At 5 active clients, you also save 6–10 hours/week of admin work that would otherwise live in Slack DMs and email threads. At a $75/hr internal rate, that's $1,950–$3,250/month of recovered founder time. Total payback: under 60 days from a working deployment.

The deployment is the constraint. The platform is fine.

---

## Chapter 2 — The 7 Modules That Matter

Here is the entire short list, in priority order. Configure them in this order.

**1. CRM / Contacts.** Every other module in SuiteDash hangs off the contact record. A project is owned by a contact. A portal belongs to a contact (or a "circle" of contacts). A form submission creates or updates a contact. If your contact schema is wrong, everything downstream is wrong. Configure 3–5 custom fields here before doing anything else: `company_name`, `service_tier`, `onboarding_stage`, `account_owner`, and one tag-style field for segmentation.

**2. Projects / Tasks.** This is the operational layer. SuiteDash's project module is the closest competitor to ClickUp/Asana inside the platform — it has tasks, subtasks, dependencies, assignees, due dates, and Kanban/list views. It is good enough. Don't try to make it as flexible as ClickUp; use it for the 70% of tasks that are repeatable and template-able, and put the genuinely-novel work somewhere else (or just in your head).

**3. Client Portals.** This is the customer-facing surface and the reason SuiteDash exists in your stack. A portal is a branded URL where your client logs in and sees their projects, files, invoices, and messages. Configure one portal *template* (not 20 individual portals). Every new client gets a portal cloned from this template via automation.

**4. Files / Folders.** SuiteDash's file system is unremarkable but functional. The pattern that matters: folder templates that auto-attach to projects. When you spawn a project from a template, the folder structure spawns with it. This is the alternative to "we're using Google Drive but I keep forgetting to make folders."

**5. Forms.** Forms are the intake gateway. A form submission can: create a contact, populate custom fields, trigger an automation, spawn a project, and provision a portal — in under 5 seconds, unattended. If you build one form well, you've built your entire client onboarding.

**6. Automations (Flows).** The multiplier. Every other module gets 2–3x more useful when an automation is sitting on top of it. SuiteDash's Flows engine is trigger-condition-action, similar to Zapier or Make but native (no per-task billing). Most operators never configure a single flow, which is why most operators never get LTD payback.

**7. Templates.** The reusability layer. Template a project, template a portal, template a folder structure, template a task list. The first time you template something, you save 30 minutes the next time you use it. By the third reuse, the template has paid back the time you spent making it. By the tenth, it's pure profit.

That's it. Seven modules. If you configure these in order and use them weekly, you have what 90% of small agencies need from a client portal stack.

---

## Chapter 3 — The 12 Modules to Skip (and Why)

These exist. Most are functional. None of them are where you should spend setup time at this stage.

**1. Estimates / Proposals.** Replaceable by PandaDoc, Better Proposals, or a Notion template you already have. SuiteDash's proposal builder is brittle and the e-signature flow has had reliability issues historically. If you already have a proposal tool, keep it.

**2. Invoicing / Subscriptions.** SuiteDash can invoice and process payments via Stripe integration. It works. But: if you already use Stripe Billing, Stripe Invoicing, or QuickBooks, switching to SuiteDash's billing layer is a downgrade in reporting, reconciliation, and tax-prep workflows. Keep your existing billing stack.

**3. LMS (Learning Management).** SuiteDash has a course module. It is a worse Teachable. If you teach courses, use a real LMS (Teachable, Thinkific, Kajabi). If you don't teach courses, ignore this entirely.

**4. Marketing Campaigns / Email Blasts.** SuiteDash can send marketing email. It is a worse ConvertKit/Beehiiv/MailerLite. Deliverability is mediocre and the editor is dated. Use a real ESP for marketing email; use SuiteDash's automations only for transactional/portal-related email.

**5. Appointments / Scheduling.** SuiteDash has a booking module. It is a worse Calendly/Cal.com. The friction of getting clients to use it (vs. clicking your existing Calendly link) is not worth the 10% efficiency gain from "everything in one place."

**6. Affiliate Manager.** Niche. Low traffic. If you actually run an affiliate program, use Rewardful, FirstPromoter, or PartnerStack. Ignore SuiteDash's version unless you've stress-tested those alternatives and rejected them.

**7. AI Assistant features.** Generic LLM wrapping. The AI features (auto-task generation, summary writing, etc.) lag the standalone tools (ChatGPT, Claude, Gemini) by 12+ months in capability. Don't build workflows on top of them.

**8. Custom Code / White-Labeled Mobile App.** The mobile-app whitelabel is a five-figure commitment in time and customization. Nobody at $50K–$400K revenue needs this. If you're at $1M+ and selling enterprise, revisit. Until then, skip.

**9. Knowledge Base / FAQ Builder.** Replaceable by a Notion site, GitBook, or even a Google Doc. SuiteDash's KB is fine; standing up your KB inside SuiteDash also makes it a worse SEO surface. Host docs publicly elsewhere.

**10. Internal Team Chat.** Replaceable by Slack/Teams/Discord. SuiteDash has internal messaging; nobody on your team will adopt it because they already live in Slack. Don't fight that battle.

**11. Time Tracking.** Functional but minimal. If you bill hourly, use Harvest or Toggl (they integrate with QuickBooks/Xero out of the box). If you bill flat-fee retainer, you don't need time tracking at all.

**12. Custom Database / Secure Data Sharing.** Power-user feature. Configurable record sets, custom CRUD interfaces. The use case for this is narrow (internal data tools where you don't want to use Airtable). Most operators will never need it; if you're the rare exception, you'll already know.

The pattern across all 12: each is replaceable by a purpose-built tool you probably already pay for, and the configuration time to get them to "as good as the alternative" exceeds the cost of just keeping the alternative. Skip them.

---

## Chapter 4 — The Configuration Order

Configure SuiteDash in this exact order. The order matters because each step depends on the previous one — flipping the order forces rebuilds.

**Step 1: Branding + subdomain (10 min).** Settings > Branding. Upload logo (light + dark variants), set primary color, point a custom subdomain (e.g., `portal.youragency.com`) at the SuiteDash CNAME. This must be done first because every link you generate later carries the branding. If you set up a portal first and then change the branding, you'll regenerate every portal asset.

**Step 2: CRM custom fields (15 min).** Settings > Customization > Custom Fields > Contacts. Add the five fields: `company_name` (text), `service_tier` (dropdown: starter / growth / premium), `onboarding_stage` (dropdown: lead / qualified / signed / onboarded / active / churned), `account_owner` (user reference), `referral_source` (text). These fields drive everything downstream — segmentation, automations, portal templates.

**Step 3: Pipeline / lifecycle stages (5 min).** CRM > Pipelines > New. Build one pipeline ("Client Lifecycle") with stages mirroring `onboarding_stage`. The pipeline is what makes your CRM browsable as a Kanban; the field is what makes it filterable and automatable.

**Step 4: Project + task templates (20 min).** Projects > Templates > New Template. Build one template per service line (most agencies need 1–3). For each template: name, description, task list with assignees and durations, folder structure, and starting status. The first template takes 20 minutes; cloning it for variants takes 5.

**Step 5: Forms + intake (15 min).** Forms > New Form. Build one intake form. Map every form field to a CRM custom field. Set the post-submit action to "Create or update contact." This is the trigger you'll use in the automation in Step 7.

**Step 6: Client portal template (10 min).** Portals > Templates > New. Configure visibility (which modules the client sees: typically Projects, Files, Messages, Invoices). Apply branding. Set a default landing page. Save as template.

**Step 7: First automation (15 min).** Automations > Flows > New Flow. Trigger: Form submission. Conditions: `service_tier` is set. Actions: create contact (if not exists), spawn project from template, provision portal from template, send welcome email. Save and activate.

Total time: 90 minutes. The protocol in Bonus 1 is this list, time-boxed and ruthless. Use it.

**Why this order:** branding first because it propagates. Custom fields before pipeline because the pipeline references the fields. Project templates before forms because the form's automation will spawn projects. Portal template before automation because the automation provisions portals. Automation last because it depends on everything else existing.

If you skip a step or do them out of order, you will rebuild. I have seen this happen six times in beta-testing this protocol. The order is the protocol.

---

## Chapter 5 — Automation Pattern #1: The Intake-to-Portal Pipeline

This is the single highest-leverage automation in SuiteDash. If you build only one automation in your life, build this one.

**What it does:** A prospect fills out your intake form on your marketing site. Within 30 seconds, unattended:
- A contact is created in your CRM with all custom fields populated
- The contact is assigned to the "Qualified" stage of your pipeline
- A project is spawned from the appropriate service-tier template
- A client portal is provisioned with the project and a welcome video pre-loaded
- A welcome email goes out to the prospect with their portal login credentials and a link to the kickoff call calendar
- An internal notification (email or Slack via webhook) fires to the operator

**Why this is the leverage:** Without this, every new client is 20–40 minutes of manual setup (create contact, spin up project, share folder, write welcome email, send credentials, schedule kickoff). With it, every new client is 0 minutes. At 5 new clients/month, that's 100–200 minutes/month back. At 15 new clients/month, the automation pays back the entire SuiteDash LTD in operator-time savings every single month.

**Configuration breadcrumbs:**

→ `Forms > New Form` — build the intake form. Fields: name, email, company, service_tier, referral_source.

→ `Form > Settings > Post-submit actions > Create/update contact` — map every form field to its CRM custom field. This is non-obvious; the default is "no action."

→ `Automations > Flows > New Flow`
- Trigger: `Form submitted` → select the intake form
- Condition: `service_tier ≠ empty` (filters out incomplete submissions)
- Action 1: `Create or update contact` (already handled by the form, this is the safety net)
- Action 2: `Update contact field` → `onboarding_stage = qualified`
- Action 3: `Create project from template` → branch on `service_tier` value (starter → starter template, growth → growth template, premium → premium template)
- Action 4: `Provision portal from template` → assign to the contact + the new project
- Action 5: `Send email` → use the welcome-email template, merge in portal credentials and calendar link
- Action 6: `Send webhook` → POST to your Slack incoming webhook URL with a "new client" payload

→ Activate the flow. Submit a test form yourself. Verify all six actions fire.

**The four mistakes that break this in production:**

1. **Forgetting the post-submit action mapping.** The default form behavior is to capture submissions but not create contacts. If you skip the mapping in form settings, the form fills the submission table but the automation downstream sees no contact. Symptom: form submissions exist, but no projects spawn.

2. **Conditional logic on a field that's optional.** If your `service_tier` field is optional on the form and the prospect skips it, the automation's branching logic falls through and no project spawns. Fix: make `service_tier` required on the form.

3. **Portal provisioning before the project exists.** If you put the portal provisioning action *before* the project creation action, the portal launches without a project to display, and the client logs in to an empty dashboard. Order matters: project first, portal second.

4. **Welcome email merge tags pulling stale data.** SuiteDash merge tags evaluate at action-fire time, not at flow-end time. If your portal-credentials merge tag is on action 5 but the portal is provisioned in action 4, you'll have a race condition where the credentials field is sometimes blank. Fix: add a 30-second delay action between portal provisioning and the email send.

Once this automation is live, you have a working client onboarding pipeline that runs without you. That alone justifies the price of this PDF.

---

## Chapter 6 — Automation Pattern #2: Template-Driven Project Spawning

The second pattern is the reusability play. It's the engine of operational throughput.

**The premise:** You don't have 50 unique projects. You have 1–3 project archetypes that you run on every client. Templating those archetypes turns project setup from a 30-minute hand-build into a 30-second click.

**What it looks like in practice:**

You sell three service tiers: Starter ($1K/mo), Growth ($3K/mo), Premium ($7K/mo). Each tier has a defined scope, a defined cadence, and a defined deliverable schedule. That means each tier has:

- A fixed task list (15–25 tasks for Starter, 30–50 for Growth, 50–80 for Premium)
- A fixed folder structure (Brand Assets, Deliverables, Working Files, Client Uploads)
- A fixed timeline (12 weeks for Starter, 24 weeks for Growth, ongoing for Premium)
- Fixed assignees (account owner, project manager, contractor pool)

Build one template per tier. Then every new client is `Projects > New > From Template > [tier]`. Done.

**Configuration breadcrumbs:**

→ `Projects > Templates > New Template`
- Name: `[Tier] - Standard Engagement`
- Task list: paste in the full task list from your existing process. Set assignee role (not specific user — use roles like "Account Owner" or "PM"), duration in days, and dependency relationships.
- Folder structure: build the four standard folders inside the template. Add starter files (welcome doc, kickoff agenda template, brand questionnaire) directly into the template.
- Visibility settings: which tasks are client-visible vs. internal? Mark internal-only tasks with a tag.

→ `Projects > Templates > [tier] > Settings`
- Default project status: "In Progress"
- Default duration calculation: relative to project start date
- Auto-assign by role: enabled

→ Test by creating a project from the template manually. Confirm task list, folders, files, and assignees populate correctly.

**The 80/20 you should be aware of:** The first template you build will take 90 minutes. The second will take 30. The third will take 15. If you find yourself wanting a fourth, fifth, or sixth template, stop — you're over-fragmenting. Three templates cover ~90% of agency use cases. If a project doesn't fit one of three templates, it probably shouldn't be in SuiteDash at all (it's bespoke; treat it bespoke).

**Spawn triggers (three options, ordered by frequency):**

1. **Form-triggered (best).** Hooked into the Pattern #1 automation above. New form submission → template-spawned project. Most clients enter this way.
2. **Pipeline-stage-triggered.** When a contact moves from "Qualified" to "Signed," automatically spawn the project. Works for cases where the form isn't the entry point (e.g., DM-sourced clients).
3. **Manual.** A button click inside the contact record. Useful for irregular cases (referrals, expansions, scope-change projects).

Once both Pattern #1 and Pattern #2 are running, the rest of SuiteDash starts to feel like glue holding the two patterns together — which is exactly the right mental model.

---

## Chapter 7 — When SuiteDash Is the Wrong Tool

Honest, direct comparisons. SuiteDash is not the right call for every operator. Here is when it isn't.

**Vs. Notion.** Notion wins when your work is knowledge-graph-shaped: interconnected docs, dynamic databases that get queried 50 different ways, lightweight project tracking, and an emphasis on flexibility. Notion loses when you need a polished client-facing surface (Notion's "publish as site" is fine for content but uncomfortable as a paid client portal) or when you need real automation logic without bolting on a third-party tool. Use Notion if your business runs on docs and databases. Use SuiteDash if your business runs on client portals and recurring project execution.

**Vs. Basecamp.** Basecamp wins when you want fewer features, deeper opinion, and a 10-minute onboarding for every team member. Basecamp's Campfire, Hill Charts, and message boards are excellent for a tight in-house team that doesn't want to think about configuration. Basecamp loses on CRM (it has none), automation (it has none), and white-labeling (it has none). Use Basecamp if you have a small in-house team and don't need CRM or automation. Use SuiteDash if you need a CRM + portal + automation stack in one place.

**Vs. ClickUp.** ClickUp wins on task complexity. If your work involves 40+ task fields, intricate dependency networks, custom views per team member, and you bill on time tracked at the task level, ClickUp's depth is unmatched. ClickUp loses on client-facing experience — even with guests-and-views configured, a ClickUp workspace is uncomfortable to send to a non-technical client. Use ClickUp when internal task complexity > client portal complexity. Use SuiteDash when client portal experience is the customer's primary touchpoint with you.

**Vs. Custom Build (Supabase + Next.js + Stripe).** Custom wins past ~10 active clients when SuiteDash's customization ceiling becomes a constraint and the per-client revenue justifies engineering time. Custom loses on the first 9 clients, where every hour spent building auth flows and CRUD interfaces is an hour not spent acquiring clients. Use SuiteDash from client 1 to client 9 (or 19, depending on margin). Use custom past that, where the unit economics support a 3–6 month engineering build.

**The 5-question decision rubric:**

1. Do you have 1+ active clients today, or are you pre-revenue? (No → SuiteDash is overkill; use a Notion + Stripe setup.)
2. Is your work template-able, or is every engagement bespoke? (Bespoke → Notion or custom; template-able → SuiteDash.)
3. Do you need a branded client-facing portal, or do clients just need email + Google Drive access? (Email + Drive → don't bother; portal → SuiteDash.)
4. Is internal task complexity higher than external client experience complexity? (Internal → ClickUp; external → SuiteDash.)
5. Are you running 10+ active retainer clients with $5K+/mo each? (Yes → start scoping a custom build; no → SuiteDash is correct.)

If you answered "SuiteDash" to questions 2–4, you're in the right tool. Configure it. Ship.

---

## Chapter 8 — The 90-Minute Lock-In Path

This chapter mirrors Bonus 1 — but where the bonus is a stripped checklist, this chapter explains the *why* behind each step. Read this once. Then run the checklist.

**Minute 0 — Open SuiteDash. Close every other tab.** This is not metaphorical. If your inbox is open in another tab, you will lose 20 minutes to a Slack notification at minute 47, and the protocol will fail. Single-task or fail. Set a 90-minute timer.

**Minutes 0–10: Branding + subdomain.** Settings > Branding. Logo (light + dark variants — most operators forget the dark variant and the portal looks broken when a client is in dark mode). Primary color. Custom subdomain (point your DNS at the SuiteDash CNAME; if DNS is slow to propagate, use the SuiteDash default subdomain temporarily and swap later). Save.

**Minutes 10–25: CRM custom fields + pipeline.** Settings > Customization > Custom Fields > Contacts. Add the five fields named in Chapter 4. Then CRM > Pipelines > New. Build the Client Lifecycle pipeline with the six stages. The pipeline takes 90 seconds to build once the fields exist.

**Minutes 25–45: Project template.** Build one project template — your most common service tier. Don't build all three on day one. Get one working, ship one client through it, learn what's missing, then template variants. Tasks, folders, assignees-by-role.

**Minutes 45–60: Intake form.** Forms > New. Fields mapped to CRM custom fields. Required fields: name, email, service tier. Optional: company, referral source. Set post-submit action to create/update contact. Get the public form URL.

**Minutes 60–75: Portal template.** Portals > Templates > New. Configure visibility — which modules the client sees. For most agencies: Projects, Files, Messages, Invoices. Apply branding. Set landing page to the project view. Save as template.

**Minutes 75–90: First automation.** Automations > Flows > New Flow. Build the intake-to-portal pipeline from Chapter 5. Trigger, condition, six actions. Activate. Submit a test form to your own intake. Verify the contact, project, portal, and welcome email all fire.

**Minute 90: stop.** SuiteDash is deployed. You have a branded portal, a CRM, a project template, an intake form, and an automation that turns form submissions into provisioned clients in 30 seconds.

What you don't have: invoices, proposals, courses, marketing email blasts, scheduling. You also don't need them on Day 1. Add them in week 2 if and only if you've onboarded a real client through the existing flow first. Don't build for hypothetical needs.

The deployment is the constraint. The platform is fine. Now you have both.

---

## Closing — What's Next

You've configured SuiteDash. You've run the protocol. You're at "live deployment." If you want to take this further, here's the natural sequence:

1. **Onboard your first real client through the new flow this week.** Don't wait for "perfect." Imperfect with a real client beats perfect with no clients every time. The flow will reveal its rough edges only when a real human runs through it.

2. **Set a 30-day calendar reminder to revisit.** What broke? What didn't fire? What's missing? Iterate. By Day 30, the system is yours, not mine.

3. **If this PDF saved you 5+ hours of fumbling, the next ladder rung is the SuiteDash Setup Service or the Dynasty Operator Cohort.** The Setup Service is a $497 done-with-you engagement where I or a vetted operator runs the protocol on your tenant in a 90-minute working session. The Operator Cohort is a $997 quarterly community where stack-stitchers like you ship faster together. Neither is required. Both exist if you want compression.

4. **Reply to your purchase email if you got stuck anywhere.** I read every reply. The friction points you hit become the next version of this PDF. Your feedback is what makes version 2 better — and the testimonial you write at Day 30 becomes the social proof for the next launch.

That's the entire game.

Stop reading. Open SuiteDash. Set a 90-minute timer.

Ship.

— Ike

---

*The Good Parts of SuiteDash, v1.0. Dynasty Empire / PNR Holdings LLC. ikeohu.com.*
