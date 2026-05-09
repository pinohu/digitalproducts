# FuseBase Read-Only Browser-Ops Runbook Pack

Related issues: DIG-44, DIG-46
Status: accepted read-only operating pack
Verified entry path: `https://app.nimbusweb.me/auth/login`
Verified tenant shape: `https://pinohu.nimbusweb.me/dashboard/u26090/tables/entity/spaces`
Verified organization: `pinohu`

## Purpose

FuseBase is verified as a browser-operated surface for portals, docs, knowledge delivery, and lightweight client-work operations. This pack gives Hermes/Paperclip browser operators reusable read-only workflows that collect useful operational evidence without changing portal content, users, permissions, billing, security, AI settings, integrations, automations, or private data exports.

The default outcome of every workflow here is a concise evidence summary in the issue comment and, when useful, a redacted repo update. The default action is inspection only.

## Global operating rules

### Allowed by default

- Navigate authenticated pages with the dedicated ops browser session.
- Record high-level names, counts, route names, statuses, and configuration presence/absence.
- Capture browser titles, visible section labels, navigation paths, and non-secret metadata.
- Summarize whether a surface is present, empty, configured, stale, or blocked.

### Not allowed without a separate write-contract issue

- Editing portals, workspaces, pages, docs, tasks, tables, forms, files, e-sign requests, AI agents, integrations, apps, billing, security, or organization settings.
- Inviting users, changing roles, sending magic links, resending invitations, issuing e-sign requests, running automations, or connecting apps.
- Exporting private data, downloading files, bulk-copying content, or scraping member/client records.
- Saving raw passwords, cookies, local/session storage, API keys, license keys, OAuth tokens, or secret-bearing screenshots into the repo or Paperclip comments.

### Persisted-session and credential handling

1. Use the dedicated Windows-side Hermes/ChromeOps browser profile launched from `ops/browser/` helpers when browser automation is required.
2. Prefer a human-established or already-persisted ops session over retyping credentials.
3. If a login is required, use runtime-only credential handling. Do not print credentials, paste them into repo files, include them in comments, or store them in screenshots.
4. After login, verify only stable non-secret signals: page title, host, organization/workspace name, and route.
5. Never inspect, copy, or persist cookies/localStorage/sessionStorage values. If debugging session state, report only whether authenticated navigation works.
6. Before taking screenshots, confirm the viewport does not expose email addresses, tokens, invoices, billing details, private client content, or personal data. Prefer text summaries over screenshots.
7. If MFA, password reset, magic-link, account recovery, or invite flows appear, stop and block/ask for authorization. Do not trigger sends.

## Safe evidence schema

Use this shape in issue comments and repo notes:

```text
Surface: <workspace inventory | portals | pages/docs | members | tasks | tables/forms | AI | integrations | billing/security>
Entry path: <route or navigation label, no secret query params>
Observed: <counts/statuses/high-level names only>
Evidence collected: <browser title, route, section labels, count summaries>
Avoided: <buttons/forms/settings/exports not touched>
Result: <ready | empty | needs human decision | blocked by auth/session>
Recommended next step: <manual follow-up or safe automation candidate>
```

## Runbook 1: Workspace inventory

Goal: Build a high-level inventory of visible FuseBase workspaces and distinguish active business surfaces from empty/test areas.

Entry path:
- Start at `https://app.nimbusweb.me/auth/login` if not authenticated.
- After authentication, navigate to `https://pinohu.nimbusweb.me/dashboard/u26090/tables/entity/spaces` or the visible workspace/dashboard switcher.

Evidence to collect:
- Organization/tenant name.
- Count of visible workspaces.
- Workspace names if they are business-level labels and not client/private-data-heavy.
- Presence of workspace-level portal, docs, table, task, or settings affordances.
- Browser title and route path.

Avoid touching:
- Create workspace, rename, archive/delete, transfer ownership, import, export, sharing, member invite, and settings-save controls.

Safe completion summary:
- `Workspace inventory completed read-only: org pinohu, <n> workspaces visible, <high-level readiness notes>. No create/edit/share/settings/export controls touched.`

## Runbook 2: Client portal inventory

Goal: Determine which client portal surfaces exist and whether they are ready, draft, empty, or stale without opening sensitive client payloads unnecessarily.

Entry path:
- From the workspace dashboard, use visible portal/client portal navigation.
- If route discovery is needed, search only via navigation labels and avoid editor/save paths unless they are read-only previews.

Evidence to collect:
- Portal count and high-level portal names/statuses when visible.
- Presence of custom domain/branding indicators without copying billing/DNS secrets.
- Whether each portal has pages, members/groups, files, docs, tasks, forms, or announcements enabled.
- Last updated/status labels if visible at list level.

Avoid touching:
- Portal editor save/publish, theme changes, domain changes, invite/magic-link buttons, member role changes, visibility toggles, file uploads, delete/archive buttons.

Safe completion summary:
- `Client portal inventory completed read-only: <n> portals/surfaces visible; readiness classified as <ready/draft/empty/mixed>. No portal edits, publishes, invites, magic links, domain, permission, or export actions touched.`

## Runbook 3: Pages, docs, and knowledge content

Goal: Map the knowledge-delivery footprint and identify reusable content areas for product/customer delivery.

Entry path:
- From a selected workspace/portal, open pages, docs, notes, knowledge base, or content library list views.
- Stay at list/outline/preview level unless the issue explicitly asks for a specific document review.

Evidence to collect:
- Top-level folders/spaces/categories.
- Count of docs/pages/knowledge items if shown.
- High-level titles that are not private client-specific or secret-bearing.
- Publication/draft/archive status, if visible.
- Presence of templates, public links, comments, attachments, or permissions indicators.

Avoid touching:
- Edit mode, publish/unpublish, duplicate, delete/archive, share-link generation, public-link toggles, comments, attachment downloads, AI rewrite/summarize buttons, imports/exports.

Safe completion summary:
- `Pages/docs/knowledge scan completed read-only: <n> top-level content areas and <n> visible items/statuses observed. No edits, publishes, public-link changes, comments, downloads, AI actions, or exports touched.`

## Runbook 4: Member, client, and group access

Goal: Understand access structure and potential delivery audiences without exposing or changing private user/account data.

Entry path:
- From workspace or portal settings, open members, clients, users, groups, roles, access, or team list pages in read-only/list mode.

Evidence to collect:
- Aggregate counts of members/clients/groups/roles.
- Role/group names only when they are generic business labels.
- Presence of pending invites or inactive users as counts only.
- Whether SSO, guest access, role-based access, or group permissions are present as enabled/disabled/status labels.

Avoid touching:
- Invite/add user, resend invitation, send magic link, reset password, impersonate/login-as, role/permission dropdowns, group assignment changes, remove/suspend/delete, CSV export, member profile detail pages unless specifically authorized.

Safe completion summary:
- `Member/client access scan completed read-only: counts by users/groups/roles recorded at aggregate level. No emails copied, no invites/magic links/password/role/group/export actions touched.`

## Runbook 5: Task boards and client work tracking

Goal: Identify whether FuseBase is being used for work tracking, client delivery tasks, or internal boards.

Entry path:
- From workspace navigation, open task, board, project, kanban, or dashboard table surfaces.

Evidence to collect:
- Board/project count and generic names.
- Column/status names and item counts.
- Presence of assignee/due-date/custom-field patterns as aggregate signals.
- Whether boards appear active, empty, template-like, or stale.

Avoid touching:
- Drag/drop, status changes, checkbox completion, assignment, due date, comments, attachments, automation buttons, board settings, create/delete/import/export.

Safe completion summary:
- `Task-board scan completed read-only: <n> boards/projects visible; status columns/counts summarized. No cards moved, statuses/comments/assignees/dates/settings/import/export actions touched.`

## Runbook 6: Tables, dashboards, and forms

Goal: Map structured-data surfaces that may support product operations, lightweight CRM, intake, or delivery reporting.

Entry path:
- Start from the verified `tables/entity/spaces` dashboard route or visible tables/forms/database navigation.
- Use list and metadata views first.

Evidence to collect:
- Count of table/database spaces and forms.
- Generic table/form names and field-count summaries if visible.
- View types: grid, dashboard, form, calendar, kanban, gallery, etc.
- Whether responses/records exist as counts only.
- Integration/automation indicators at presence level only.

Avoid touching:
- Add/edit/delete records, field schema changes, form publish/share toggles, response exports, file downloads, automations, webhook/API settings, imports, sync/connect buttons.

Safe completion summary:
- `Tables/forms scan completed read-only: <n> table spaces/forms visible; view/record-count readiness summarized. No records, fields, shares, exports, imports, automations, webhooks, or integrations touched.`

## Runbook 7: Files and e-sign surfaces

Goal: Determine whether FuseBase is storing delivery files or e-sign workflows while avoiding private document exposure.

Entry path:
- From workspace/portal navigation, open files, attachments, documents, signatures, e-sign, or shared resources list pages.

Evidence to collect:
- Presence and aggregate counts of folders/files/e-sign templates/requests.
- High-level categories or template names only when non-sensitive.
- Status counts such as draft/sent/completed/expired if visible.
- Whether storage integrations or signing providers appear configured, without opening credentials.

Avoid touching:
- File preview/download/export, upload, delete/archive, share-link generation, permission changes, send/request signature, resend reminders, template editing, provider connection settings.

Safe completion summary:
- `Files/e-sign scan completed read-only: storage/signature surfaces classified by count/status only. No previews/downloads/uploads/shares/signature sends/reminders/templates/provider settings touched.`

## Runbook 8: AI assistant and agent settings

Goal: Classify AI features for future automation potential without leaking prompts, keys, or private knowledge sources.

Entry path:
- Open visible AI assistant, AI agent, chatbot, automation assistant, or AI settings pages.
- Stay at overview/list/config-presence level.

Evidence to collect:
- Whether AI assistants/agents exist and how many.
- Generic assistant names/statuses if visible and non-sensitive.
- Presence of knowledge sources, channels, widgets, or model/provider settings as enabled/disabled only.
- Safety/visibility controls presence.

Avoid touching:
- Prompt editing, training/retraining, publishing widgets, test chats with private data, provider/API-key fields, model changes, knowledge-source connect/disconnect, deleting or cloning agents.

Safe completion summary:
- `AI settings scan completed read-only: <n> assistants/agents and configuration-presence signals observed. No prompts, chats, training, model/provider/API-key, source, publish, clone, or delete actions touched.`

## Runbook 9: Integrations, apps, and automation settings

Goal: Identify integration footprint and automation potential without connecting, disconnecting, running, or exposing credentials.

Entry path:
- From workspace/org settings, open integrations, apps, marketplace, connected apps, automations, webhooks, or API pages.

Evidence to collect:
- Count/list of connected or available integrations at provider-name level.
- Enabled/disabled status, last sync/status labels, and automation categories.
- Presence of API/webhook/OAuth surfaces without revealing values.
- Which integration areas appear relevant to delivery, CRM, email, storage, signing, or analytics.

Avoid touching:
- Connect/disconnect, OAuth authorization, API-key reveal/copy/regenerate, webhook creation/editing, run/test automation, sync now, app installation/removal, billing-plan upgrade prompts.

Safe completion summary:
- `Integrations/apps scan completed read-only: provider/status categories summarized; no connects/disconnects/OAuth/API-key/webhook/run/sync/install/remove actions touched.`

## Runbook 10: Billing, security, and organization settings

Goal: Capture operational risk/readiness at the safest possible level while treating this surface as manual-first and highly sensitive.

Entry path:
- Only when explicitly requested, open organization settings, billing, plan, subscription, invoices, security, SSO, audit log, admin settings, or domain settings.
- Stop at overview pages. Do not open payment method, invoice detail, API secrets, SSO secret, or advanced destructive settings pages.

Evidence to collect:
- Plan tier/status as a high-level label if already visible.
- Seat/user limits as aggregate numbers if visible.
- Security controls present: MFA, SSO, audit log, allowed domains, admin roles, session/device management.
- Organization/domain configuration presence without copying DNS records, verification tokens, or payment data.
- Billing/security blocker categories only.

Avoid touching:
- Payment method, invoice downloads, plan changes, cancellation, seat purchase/removal, owner transfer, domain/DNS verification changes, SSO/SAML/OAuth secret fields, MFA resets, session revocation, audit-log exports, API key reveal/regenerate, org deletion.

Safe completion summary:
- `Billing/security/org scan completed read-only at overview level: plan/security/domain/admin-presence summarized. No payment/invoice/download/plan/seat/domain/SSO/MFA/session/API-key/export/delete actions touched.`

## Automation recommendations

### Automate first, if the browser session is stable

1. Workspace inventory: low sensitivity, stable navigation, high value for future routing.
2. Portal inventory: automate list-level presence/status/count collection only.
3. Tables/forms metadata: automate counts, names, view types, and empty/active classification without opening records.
4. Task-board metadata: automate board/column/count summaries without card interactions.
5. Pages/docs list metadata: automate top-level folders/status counts, not full content extraction.

### Keep manual-first due to sensitivity

1. Member/client access: emails, roles, invites, and permissions are too easy to expose or mutate accidentally.
2. Billing/security/org settings: payment, plan, owner, domain, SSO, audit, and API-key surfaces require human supervision.
3. Integrations/apps/webhooks: connect/disconnect, OAuth, keys, syncs, and automations are mutation-prone.
4. AI assistant/agent settings: prompts, private knowledge sources, training, widgets, and provider keys are sensitive.
5. Files/e-sign: private documents, downloads, signature sends, and reminders are sensitive.

## Browser-operator checklist

Before run:
- Confirm the issue authorizes read-only FuseBase inspection.
- Confirm the browser profile/session is the dedicated ops profile, not a personal browsing session.
- Confirm no write, export, send, invite, billing, security, or permission change is in scope.
- Prepare an evidence schema before opening sensitive pages.

During run:
- Stay on list/overview pages when possible.
- Prefer counts/statuses/routes over raw content.
- Treat warning modals, save buttons, toggles, and send/export/connect buttons as stop signs.
- If an action would trigger a side effect, stop and ask for a separate write-contract issue.

After run:
- Close with the safe evidence schema.
- Mention explicitly which sensitive controls were avoided.
- Do not attach screenshots unless they are manually reviewed for secrets and personal data.
- If the session fails, classify the blocker precisely: expired session, MFA required, invalid credential, permission missing, or tenant ambiguity.
