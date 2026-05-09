# Bonus 2 — 7 SuiteDash Automation Recipes

Status: v1 recipe scaffolds. These are production-minded patterns, not verified import files yet. Before packaging as importable JSON/config, test each recipe in a SuiteDash account and update the status below.

## Recipe status

| # | Recipe | V1 status | Import tested? |
|---|---|---|---|
| 1 | Paid Client Onboarding Kickoff | Drafted | No |
| 2 | Intake Form to Project Template | Drafted | No |
| 3 | Missing Intake Reminder | Drafted | No |
| 4 | Milestone Status Update | Drafted | No |
| 5 | Invoice Follow-Up / Payment Reminder | Drafted | No |
| 6 | Support Request Triage | Drafted | No |
| 7 | Testimonial Request Loop | Drafted | No |

---

## Recipe 1: Paid Client Onboarding Kickoff

### Use when

A client pays or is marked won, and the next step should happen without a manual “now what?” email.

### Trigger

- Invoice paid, OR
- Deal marked won, OR
- Manual admin action: “Start onboarding.”

### Preconditions

- Contact/company exists.
- Package/service field exists.
- Onboarding project template exists.
- Welcome/access email template exists.

### Actions

1. Update client status to `Onboarding`.
2. Assign onboarding project template.
3. Send welcome/access email.
4. Create internal kickoff review task.
5. Notify owner that onboarding has started.

### Definition of done

- Client receives a clear next step.
- Owner receives an internal task.
- Project/template exists and is linked to the client.

### Failure mode to watch

Do not trigger this before payment or a confirmed manual approval unless you intentionally onboard before payment.

---

## Recipe 2: Intake Form to Project Template

### Use when

You need form answers to create the work structure automatically.

### Trigger

Client onboarding/intake form submitted.

### Preconditions

- Intake form fields are mapped to contact/project data.
- Project template exists.
- Required fields are minimal and meaningful.

### Actions

1. Create/update client record.
2. Save key answers to custom fields.
3. Assign the appropriate project template.
4. Attach or reference submitted files/answers.
5. Notify owner.

### Definition of done

- Submission produces a usable project/task structure.
- Internal owner does not need to copy/paste form answers manually.

### Failure mode to watch

If the project template branches into too many variations, split service types before automating.

---

## Recipe 3: Missing Intake Reminder

### Use when

A client has paid or started onboarding but has not completed the intake form.

### Trigger

Client status is `Onboarding` and intake form is incomplete after 48 hours.

### Preconditions

- Intake completion status field exists.
- Reminder email template exists.
- Owner is assigned.

### Actions

1. Send client reminder with intake link.
2. Create internal follow-up task if still incomplete after 72 hours.
3. Notify owner if deadline is approaching.

### Definition of done

- Client receives one clear reminder.
- Owner has visibility before the workflow stalls.

### Failure mode to watch

Do not spam daily reminders. One client-facing reminder plus one owner escalation is enough for v1.

---

## Recipe 4: Milestone Status Update

### Use when

Clients ask “where are we?” because status is not visible.

### Trigger

Project phase/milestone changes.

### Preconditions

- Project template has named phases.
- Status update email/template exists.
- Client-facing status field/page exists if used.

### Actions

1. Update client-facing status.
2. Send short progress notification.
3. Create next internal task if phase handoff is needed.
4. Log evidence of milestone completion.

### Definition of done

- Client can tell what changed and what happens next.
- Internal owner knows the next action.

### Failure mode to watch

Avoid sending low-value notifications for every tiny task. Trigger on phase/milestone changes, not micro-updates.

---

## Recipe 5: Invoice Follow-Up / Payment Reminder

### Use when

Payment status blocks onboarding or delivery.

### Trigger

Invoice sent and unpaid after chosen interval, or due date approaching/past.

### Preconditions

- Invoice/payment module is used for the workflow.
- Payment status is visible on client record.
- Reminder language is approved.

### Actions

1. Send payment reminder.
2. Update payment follow-up status.
3. Create internal task if overdue.
4. Pause onboarding/delivery automation if payment is required before work starts.

### Definition of done

- Payment block is visible.
- Client receives a clear path to pay.
- Internal owner knows whether to proceed or pause.

### Failure mode to watch

Do not pause mission-critical client work automatically unless the business policy is explicit.

---

## Recipe 6: Support Request Triage

### Use when

Clients need one structured place to request help instead of sending scattered emails/texts.

### Trigger

Support/request form submitted or ticket created.

### Preconditions

- Support form has category, urgency, description, and attachment fields.
- Owner or queue assignment rules exist.
- SLA expectation is defined.

### Actions

1. Create support task/ticket.
2. Categorize by issue type.
3. Assign owner/queue.
4. Send client acknowledgment.
5. Escalate if unresolved by SLA threshold.

### Definition of done

- Request has an owner.
- Client receives acknowledgment.
- Urgent requests are not buried.

### Failure mode to watch

Do not build a full help desk if the business only receives occasional requests. A structured form + task may be enough.

---

## Recipe 7: Testimonial Request Loop

### Use when

A project or onboarding flow reaches a successful outcome and you need proof for the sales page.

### Trigger

Project marked complete, milestone achieved, or 30 days after purchase/completion.

### Preconditions

- Completion status exists.
- Testimonial request template exists.
- Permission language is included.

### Actions

1. Send testimonial request.
2. Ask for a specific before/after statement.
3. Create internal task to review response.
4. Save usable quote to testimonial bank.

### Definition of done

- Client is asked at the right moment.
- Response gets captured in a reusable location.

### Failure mode to watch

Do not fabricate proof. If no response exists, keep the sales page testimonial blocker open.

---

## Packaging notes

For v1, these can ship as a readable recipe pack. For v2 / SuiteDash Operator Pack, convert into importable or copy-paste configuration templates after live testing.