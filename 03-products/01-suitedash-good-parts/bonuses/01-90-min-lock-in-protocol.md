# Bonus 1 — The 90-Minute SuiteDash Lock-In Protocol

*Standalone value: $97. Format: 1-page checklist. Goal: live deployment in 90 minutes.*

---

## Before You Start (5 min, doesn't count toward 90)

- [ ] Close every browser tab except SuiteDash
- [ ] Silence Slack, email, and phone notifications
- [ ] Open a 90-minute timer on your phone, screen-up, in view
- [ ] Have your logo files (light + dark PNG) on your desktop
- [ ] Have your DNS provider login open in a separate tab (one-time use)

If any of the above isn't ready, fix it first. The protocol fails on interruption, not on skill.

---

## 0–10 minutes — Branding + Subdomain

→ `Settings > Branding`

- [ ] Upload logo — light variant
- [ ] Upload logo — dark variant
- [ ] Set primary brand color (hex)
- [ ] Set secondary / accent color
- [ ] Save branding

→ `Settings > White Label > Custom Domain`

- [ ] Copy the SuiteDash CNAME target
- [ ] Add CNAME record in DNS (`portal.yourdomain.com → [SuiteDash CNAME]`)
- [ ] Save the custom subdomain in SuiteDash (if DNS not propagated yet, use default subdomain — swap later)

**Stop at minute 10. Do not iterate on logo size. Do not pick a third color. Move on.**

---

## 10–25 minutes — CRM Custom Fields + Pipeline

→ `Settings > Customization > Custom Fields > Contacts`

- [ ] Add field: `company_name` (text)
- [ ] Add field: `service_tier` (dropdown — values: starter, growth, premium)
- [ ] Add field: `onboarding_stage` (dropdown — values: lead, qualified, signed, onboarded, active, churned)
- [ ] Add field: `account_owner` (user reference)
- [ ] Add field: `referral_source` (text)
- [ ] Save

→ `CRM > Pipelines > New Pipeline`

- [ ] Name: "Client Lifecycle"
- [ ] Stages: lead → qualified → signed → onboarded → active → churned
- [ ] Link pipeline stage to `onboarding_stage` field
- [ ] Save

**Stop at minute 25.**

---

## 25–45 minutes — Project Template (one only)

→ `Projects > Templates > New Template`

- [ ] Name: `[Your Most Common Tier] - Standard Engagement`
- [ ] Build task list — paste from your existing process doc, ~15–30 tasks
- [ ] Set assignee role (not user) on each task
- [ ] Set duration in days, relative to project start
- [ ] Add task dependencies for the obvious ones (3–5 max)
- [ ] Build folder structure: Brand Assets / Deliverables / Working Files / Client Uploads
- [ ] Drop welcome doc + kickoff agenda template into folders
- [ ] Save template

**Don't build all three tier templates today. One template, real client through it, then iterate.**

**Stop at minute 45.**

---

## 45–60 minutes — Intake Form

→ `Forms > New Form`

- [ ] Name: "New Client Intake"
- [ ] Field: Name (required, → contact name)
- [ ] Field: Email (required, → contact email)
- [ ] Field: Company (optional, → `company_name`)
- [ ] Field: Service Tier (required dropdown, → `service_tier`)
- [ ] Field: Referral Source (optional, → `referral_source`)
- [ ] Form Settings > Post-submit actions > **Create or update contact** (this is the non-obvious one — most operators miss it)
- [ ] Map every form field to its CRM custom field
- [ ] Get public form URL — paste it into a notes doc for later

**Stop at minute 60.**

---

## 60–75 minutes — Client Portal Template

→ `Portals > Templates > New Portal Template`

- [ ] Name: "Standard Client Portal"
- [ ] Visibility: Projects ✅ / Files ✅ / Messages ✅ / Invoices ✅ / everything else ❌
- [ ] Apply branding (should auto-pull from Step 1)
- [ ] Set default landing page: Project view
- [ ] Save as template

**Stop at minute 75.**

---

## 75–90 minutes — First Automation (Intake-to-Portal)

→ `Automations > Flows > New Flow`

- [ ] Name: "Intake to Portal Pipeline"
- [ ] Trigger: `Form submitted` → "New Client Intake"
- [ ] Condition: `service_tier ≠ empty`
- [ ] Action 1: Update contact field → `onboarding_stage = qualified`
- [ ] Action 2: Create project from template → branch on `service_tier`
- [ ] Action 3: Provision portal from "Standard Client Portal" template → assign to contact + project
- [ ] Action 4: Delay 30 seconds (prevents merge-tag race condition)
- [ ] Action 5: Send email → welcome template, merge in portal credentials
- [ ] Action 6: Send webhook → POST to your Slack incoming webhook (optional)
- [ ] Save and **activate**

→ Test it.

- [ ] Open the public form URL in an incognito window
- [ ] Submit a test entry with your own email
- [ ] Within 60 seconds: confirm contact created, project spawned, portal provisioned, welcome email received
- [ ] If any step fails, fix that step only — don't restart the protocol

**Stop the timer at minute 90. SuiteDash is deployed.**

---

## What You Just Built

- Branded client portal at your custom subdomain
- CRM with five custom fields driving segmentation and automation
- One project template ready to spawn
- Intake form live and capturing leads
- Portal template ready to clone per client
- One unattended automation turning form submissions into onboarded clients

## What You Did Not Build (and Don't Need Today)

- Invoices, proposals, scheduling, courses, marketing email, knowledge base
- A second or third project template
- A second automation

These come in week 2 — *after* you've onboarded a real human through the existing flow.

## If You Got Stuck

Email the receipt-reply address with a screenshot of where you stopped. Per the 90-Minute Guarantee, I'll either help you finish or refund + you keep the bonuses.

— Ike
