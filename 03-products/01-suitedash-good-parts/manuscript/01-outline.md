# Manuscript Outline — The Good Parts of SuiteDash

## Working subtitle

The 90-minute operator path through the 20% of SuiteDash that creates 80% of the client-ops value.

## Reader outcome

By the end, the reader should have a keep/skip decision, a configuration order, and a first client workflow mapped clearly enough to build inside SuiteDash without spending another weekend in docs.

---

# Front matter: Start here

## Opening promise

You do not need to master SuiteDash. You need to deploy the part of it that makes your business easier to run.

## What this guide is

- An operator’s cut through SuiteDash.
- A setup order for a first useful deployment.
- A filter for what to skip until real usage justifies it.

## What this guide is not

- Not a complete SuiteDash course.
- Not a replacement for SuiteDash support docs.
- Not a guarantee that every business should centralize everything in SuiteDash.

## 90-minute usage path

1. Read the module keep list.
2. Run the Lock-In Protocol checklist.
3. Pick one client workflow.
4. Configure only what supports that workflow.
5. Return to the Kill List before turning on new modules.

---

# Part 1: Why SuiteDash Feels Hard

## Thesis

SuiteDash is not hard because it lacks features. It is hard because it has too many plausible starting points.

## Key beats

- SuiteDash sells the “replace 10+ tools” dream.
- The buyer’s real problem is sequencing, not intelligence.
- The biggest cost is the rebuild loop: configure menus/roles/pages before the workflow is clear, then redo them later.
- All-in-one software punishes curiosity when curiosity turns into premature configuration.

## Include

- The “SuiteDash tax”: 5-40 hours of wandering.
- The difference between a feature reference and an implementation path.
- Permission to ship an intentionally narrow first deployment.

## Draft note

Use validation language: the buyer is technically capable, tool-rich, and time-starved.

---

# Part 2: The 7 Modules That Matter First

## Thesis

Your first SuiteDash deployment only needs seven module categories. Everything else is optional until there is workflow pressure.

## Module 1: CRM contacts and companies

Purpose: make SuiteDash the relationship record before trying to automate anything.

Minimum setup:
- Contact/company naming standard.
- Lead/customer status.
- Owner/assignee.
- Source.
- Primary service/product.

Avoid:
- Over-customizing every possible field.
- Importing messy historical contacts before deciding field rules.

## Module 2: Custom fields

Purpose: capture the handful of decisions that drive routing, onboarding, and delivery.

V1 fields:
- Client type.
- Primary service / package.
- Onboarding status.
- Portal access status.
- Payment status.
- Next milestone.

Optional advanced fields from source docs:
- Lead score.
- Budget authority.
- Primary pain point.
- Implementation timeline.

## Module 3: Forms and intake

Purpose: stop collecting client setup details manually.

V1 forms:
- Lead/demo/contact form.
- Client onboarding/kickoff form.
- Project update or support request form.

## Module 4: Client portal and white-label basics

Purpose: give clients one trusted place to find next steps, files, invoices, and project visibility.

V1 setup:
- Logo/domain basics.
- Simple portal landing page.
- One client-facing navigation path.
- File/request visibility.

Avoid:
- Complex page design before workflow proof.
- Overbuilding a portal home page no client uses.

## Module 5: Projects, tasks, and templates

Purpose: make delivery repeatable.

V1 setup:
- One project template for the first client workflow.
- Task lists by phase.
- Due dates/SLA expectations.
- Internal owner vs client-visible tasks.

## Module 6: Files, docs, proposals, invoices

Purpose: move the transaction and evidence layer into the client workflow.

V1 setup:
- File request conventions.
- Folder/naming rules.
- Proposal/invoice/payment handoff.
- Evidence log for completed work.

## Module 7: Automations and notifications

Purpose: reduce repeated handoff/status work only after the manual process is clear.

V1 setup:
- Form submitted → contact/project/task created.
- Invoice paid → onboarding sequence starts.
- Project milestone changed → client/internal update sent.

Avoid:
- Automating unclear processes.
- Building complex conditional workflows before clients use the system.

---

# Part 3: The 90-Minute Configuration Order

## Thesis

The order matters more than the number of features. Configure in the wrong order and you create rebuild work.

## Minute 0-10: Pick the workflow

Choose one spine:
- Client onboarding.
- Lead-to-client conversion.
- Project/status visibility.
- Support/escalation intake.

Recommended v1: client onboarding + status visibility.

## Minute 10-20: Define the record

- Contact/company naming.
- Client type/status.
- Required custom fields.
- Tags/circles only if they drive workflow behavior.

## Minute 20-35: Build intake

- Create the intake form.
- Map fields back to the client record.
- Decide which answers trigger tasks or routing.

## Minute 35-50: Build the portal shell

- Branding basics.
- One landing page.
- Where the client gets files, invoices, and project status.

## Minute 50-65: Build the project template

- Phases.
- Tasks.
- Owner/accountability.
- Client-visible vs internal work.

## Minute 65-80: Add the first automation

- Intake submitted → create/update record and task/project.
- Payment/invoice event → onboarding next step.
- Milestone/status event → client update.

## Minute 80-90: QA the workflow

Run a fake client through the flow and check:
- Can the record be found?
- Does the form collect enough information?
- Does the portal make the next step obvious?
- Does the project template assign the right work?
- Does one useful notification fire?

---

# Part 4: Two Automation Patterns Worth Shipping First

## Pattern 1: Paid client onboarding

Trigger: invoice paid, form submitted, or deal marked won.

Actions:
1. Update client status.
2. Assign onboarding project template.
3. Send welcome/access email.
4. Create internal kickoff task.
5. Notify owner if kickoff form is incomplete after 48 hours.

Why it matters:
- Converts purchase into action.
- Reduces “what happens next?” emails.
- Makes SuiteDash feel useful to the client immediately.

## Pattern 2: Status visibility / update loop

Trigger: project phase, milestone, or task status changes.

Actions:
1. Update client-facing status.
2. Send short notification or portal update.
3. Create internal follow-up if a due date is missed.
4. Log evidence in the project/client record.

Why it matters:
- Reduces manual update requests.
- Makes the portal worth logging into.
- Creates operational proof for the business owner.

## Optional pattern for later: lead qualification

Source docs contain deeper CLOSER and Value Equation fields. Mention as next-rung/advanced path, not core v1.

---

# Part 5: The Kill List

## Thesis

The most valuable early SuiteDash decision is often “not yet.”

## Framing

A feature belongs in v1 only if it supports the selected client workflow. Otherwise it waits for a trigger.

## Kill list summary

1. LMS/course area.
2. Full email newsletter/autoresponder stack.
3. Advanced white-label design.
4. Complex dashboard customization.
5. Deep financial reporting.
6. Time tracking/time clock.
7. Full help desk/ticketing.
8. Multi-department permissions.
9. Fancy portal pages.
10. Broad historical CRM migration.
11. Complex external integrations.
12. Multiple service workflows at once.

For each feature in the final manuscript:
- Why it tempts operators.
- Why to skip it now.
- Trigger that makes it worth adding.

---

# Part 6: SuiteDash vs. Purpose-Built Tools

## Thesis

SuiteDash should be your client-ops hub only when consolidation creates less friction than specialization.

## Keep inside SuiteDash when

- The workflow is client-facing.
- The record, portal, files, project, and invoice belong together.
- Good-enough built-in functionality prevents extra tool sprawl.
- The client benefits from one login/location.

## Use a purpose-built tool when

- The feature is mission-critical and SuiteDash is only average at it.
- The team already has a mature specialist workflow.
- Reporting/compliance/deep integration demands exceed SuiteDash’s native limits.
- You are forcing SuiteDash into work it was not designed to own.

## Examples

- Email newsletter: okay for simple buyer workflows, not always a ConvertKit/Beehiiv replacement.
- Project management: good for client delivery visibility, not always a Jira/Linear replacement.
- Automations: good for native handoffs, but n8n/Make/Activepieces may own complex external integrations.

---

# Back matter: Next steps

## Reader next action

Run the 90-Minute Lock-In Protocol, then configure one workflow before exploring additional modules.

## Testimonial ask

Before/after prompt:

“Before this, I was stuck on ____. After reading it, I decided/configured ____. It saved me roughly ____ hours or helped me avoid ____.”

## Next-rung tease

If the guide helped you choose the path, the next layer is implementation: templates, walkthroughs, and an operator pack for turning the map into a working deployment.

## Guarantee reminder

If this did not clarify the setup path or save time, reply within 30 days for a refund.