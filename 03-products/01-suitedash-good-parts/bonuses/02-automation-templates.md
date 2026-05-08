# Bonus 2 — 7 SuiteDash Automation Recipes

*Standalone value: $197. Format: recipe pack with exact UI breadcrumbs.*

Each recipe follows the same structure: **trigger → conditions → actions → setup steps → common failure**. Build them in order. Each one stacks on the previous.

---

## Recipe 1 — New Lead → Assigned Welcome Sequence

**What it does:** Captures a new lead from any source (form, manual entry, import) and immediately puts them into a 5-email welcome sequence over 14 days.

**Trigger:** `Contact created` OR `Contact field updated` where `onboarding_stage = lead`

**Conditions:** `email ≠ empty`, `service_tier ≠ empty`

**Actions:**
1. Update contact: tag with `welcome-sequence-active`
2. Send email: Welcome 1 (immediate)
3. Wait 2 days
4. Send email: Welcome 2 (case study)
5. Wait 3 days
6. Send email: Welcome 3 (FAQ + objection handling)
7. Wait 4 days
8. Send email: Welcome 4 (offer)
9. Wait 5 days
10. Send email: Welcome 5 (last call)

**Setup breadcrumbs:**

→ `Automations > Flows > New Flow > Trigger: Contact updated`
→ `Add condition: onboarding_stage equals "lead"`
→ Pre-build all five emails in `Email Templates > New Template` first; reference them in the flow
→ Use `Wait` action between each email

**Common failure:** Sending all 5 emails at once because someone forgets the `Wait` actions between sends. Add the waits *before* the email sends, not after.

---

## Recipe 2 — Project Status Change → Client Portal Notification

**What it does:** When a project status changes (e.g., "In Progress" → "Awaiting Client Review"), automatically notify the client via portal message + email.

**Trigger:** `Project field updated` where field = `status`

**Conditions:** `new_status = "Awaiting Client Review"` OR `new_status = "Completed"`

**Actions:**
1. Send email: project-status-update template (merge: project name, new status, link to portal)
2. Post to portal: in-portal notification with same content
3. Update contact field: `last_status_update = [now]`

**Setup breadcrumbs:**

→ `Automations > Flows > New Flow > Trigger: Project status changed`
→ `Conditions: status in [Awaiting Client Review, Completed]`
→ `Action: Send email → status-update template`
→ `Action: Send portal message → same content`

**Common failure:** Notifying on every status change including internal ones (e.g., "In Review" → "QA Pass"). Filter conditions to only client-relevant statuses or you'll spam them and they'll mute portal notifications.

---

## Recipe 3 — Form Submission → Contact + Project + Welcome Email

**What it does:** The intake-to-portal pipeline from Chapter 5 of the main PDF. Form fills in 30 seconds turn into provisioned clients.

**Trigger:** `Form submitted` → "New Client Intake"

**Conditions:** `service_tier ≠ empty`, `email ≠ empty`

**Actions:**
1. Create or update contact (form does this; safety net)
2. Update contact: `onboarding_stage = qualified`
3. Create project from template (branch on `service_tier`):
   - starter → "Starter Engagement" template
   - growth → "Growth Engagement" template
   - premium → "Premium Engagement" template
4. Provision portal from "Standard Client Portal" template
5. Wait 30 seconds (prevents merge-tag race condition)
6. Send email: welcome-with-credentials template (merge: portal URL, login email, temp password, kickoff calendar link)
7. Send webhook: POST to Slack #new-clients channel

**Setup breadcrumbs:**

→ `Forms > New Client Intake > Settings > Post-submit actions > Create/update contact`
→ Map every form field to its CRM custom field
→ `Automations > Flows > New Flow > Trigger: Form submitted`
→ Build the conditional branching for `service_tier`

**Common failure:** Skipping the 30-second wait between portal provisioning and email send. Result: welcome email goes out with empty portal credentials. Always add the wait.

---

## Recipe 4 — Stalled Task → Escalation

**What it does:** When a task is overdue by >3 days, escalate to the project lead and the operator.

**Trigger:** `Task overdue` (built-in trigger; fires daily on overdue tasks)

**Conditions:** `days_overdue > 3`, `assignee_role = contractor` (escalate only contractor tasks; internal team tasks are visible already)

**Actions:**
1. Send email to project lead: "Task [name] is [X] days overdue, assigned to [contractor name]"
2. Add task tag: `stalled`
3. Send Slack webhook to #ops channel
4. (Optional) Reassign task to project lead if `days_overdue > 7`

**Setup breadcrumbs:**

→ `Automations > Flows > New Flow > Trigger: Task is overdue`
→ `Conditions: days_overdue greater than 3`
→ `Action: Send email → escalation template`
→ `Action: Add task tag "stalled"`

**Common failure:** Escalating *every* overdue task including ones that are intentionally on hold. Add a condition `task_status ≠ on_hold` to filter.

---

## Recipe 5 — Onboarding Milestone → Invoice Generated

**What it does:** When the onboarding project reaches a specific milestone (e.g., "Kickoff Complete"), automatically generate the first month's invoice.

**Trigger:** `Task completed` where `task_name = "Kickoff Call Complete"`

**Conditions:** `project_status = "In Progress"`, `client_invoiced = false`

**Actions:**
1. Generate invoice from template (merge: client info, service tier, monthly amount)
2. Send invoice via email
3. Update contact: `client_invoiced = true`, `onboarding_stage = active`
4. Add internal note to project: "First invoice sent [date]"

**Setup breadcrumbs:**

→ `Automations > Flows > New Flow > Trigger: Task completed`
→ `Condition: task_name equals "Kickoff Call Complete"`
→ `Action: Create invoice from template`
→ `Action: Send invoice email`

**Common failure:** Triggering on the wrong task. SuiteDash's task name matching is exact-string. If you rename "Kickoff Call Complete" to "Kickoff Complete" in one template, the automation breaks silently. Use task tags instead of task names for triggering: tag the kickoff task with `triggers-invoice`, then filter on the tag.

---

## Recipe 6 — Recurring Monthly Check-In

**What it does:** First Monday of every month, send each active client a brief check-in email with a link to a 1-question feedback form.

**Trigger:** `Scheduled` — first Monday of every month, 9 AM

**Conditions:** `onboarding_stage = active`

**Actions:**
1. For each contact matching condition:
   - Send email: monthly-check-in template (merge: contact name, project name, last status update)
   - Increment custom field: `check_ins_sent = check_ins_sent + 1`

**Setup breadcrumbs:**

→ `Automations > Flows > New Flow > Trigger: Schedule`
→ `Schedule: Monthly, first Monday, 9:00 AM, [your timezone]`
→ `Filter contacts: onboarding_stage equals "active"`
→ `Action: Send email → monthly-check-in template`

**Common failure:** Sending the same check-in email to clients who've already responded this month. Add a condition: `last_check_in_response_date < 30 days ago` so you skip recently-engaged clients.

---

## Recipe 7 — Lost Lead Recovery Sequence

**What it does:** When a lead has been in `qualified` stage for 14+ days without progressing to `signed`, drop them into a 3-email recovery sequence over 10 days.

**Trigger:** `Scheduled` — daily, 8 AM

**Conditions:** `onboarding_stage = qualified` AND `days_in_current_stage >= 14` AND `recovery_sequence_sent != true`

**Actions:**
1. Update contact: `recovery_sequence_sent = true` (prevents re-trigger)
2. Send email: recovery-1 template ("checking in")
3. Wait 4 days
4. Send email: recovery-2 template (case study)
5. Wait 6 days
6. Send email: recovery-3 template (last call + offer to close)
7. After all 3 sent: if no response, update `onboarding_stage = churned`

**Setup breadcrumbs:**

→ `Automations > Flows > New Flow > Trigger: Schedule (daily 8 AM)`
→ `Filter: onboarding_stage = qualified AND days_in_current_stage >= 14 AND recovery_sequence_sent ≠ true`
→ Build the 3 wait + send pairs

**Common failure:** Re-triggering the sequence on the same lead because the `recovery_sequence_sent` flag isn't set early enough. Set the flag in the *first* action of the flow, not the last.

---

## Build Order Recommendation

Build them in this order:

1. Recipe 3 (intake-to-portal) — highest leverage; build first
2. Recipe 5 (onboarding milestone → invoice) — closes the revenue loop
3. Recipe 1 (lead welcome sequence) — feeds Recipe 3 with warmer leads
4. Recipe 2 (status change notifications) — improves client experience
5. Recipe 6 (monthly check-ins) — retention layer
6. Recipe 4 (stalled task escalation) — operational hygiene
7. Recipe 7 (lost lead recovery) — recovery revenue

Don't try to build all 7 in one sitting. Build one. Run a real client through it. Then build the next.

---

## Per-Recipe Setup Time (Estimated)

| Recipe | Build Time | Test Time |
|---|---:|---:|
| 1 — Welcome sequence | 25 min | 10 min |
| 2 — Status notifications | 10 min | 5 min |
| 3 — Intake-to-portal | 20 min | 10 min |
| 4 — Stalled task escalation | 10 min | n/a (real-world test) |
| 5 — Milestone-to-invoice | 15 min | 5 min |
| 6 — Monthly check-in | 10 min | n/a (calendar test) |
| 7 — Lost lead recovery | 15 min | n/a (real-world test) |

**Total: ~2 hours of build time. Lifetime savings at 5 active clients: 8–12 hours per month.**

— Ike
