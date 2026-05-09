# AgenticFlow API Viability Handoff

Related issue: DIG-58
Verification date: 2026-05-08
Owner: Automation Engineer

## Verdict

Classification: `api_auth_verified_project_scope_mismatch`

AgenticFlow is a viable future read-only operator surface, but it is not yet ready for a scheduled n8n/Paperclip connector. The current secure runtime source contains AgenticFlow API-key material, and the official CLI can authenticate with it when exported as `AGENTICFLOW_API_KEY`. The CLI now exposes workspace/project context in its read-only `whoami --json` output, but the documented REST `GET /v1/agents/` check with that context returns HTTP 403: `API key does not have access to this project`.

Do not create AgenticFlow agents, workflows, workforces, prompts, MCP connections, runs, or n8n workflow activations from this repo until an operator confirms the correct project-scoped API key or supplies a dedicated automation-owned key plus a separate write contract.

## Secure-source handling

- Secure dotenv checked: `/mnt/c/Users/ohu00/Documents/.env`.
- AgenticFlow API-key material is present in the secure dotenv under the runtime names used by the CLI/probe. The raw value was not printed, copied, committed, or posted to Paperclip.
- No standalone `AGENTICFLOW_WORKSPACE_ID`, `AGENTICFLOW_PROJECT_ID`, AgenticFlow browser credential, or persisted browser session was found in the inspected secure sources.
- The official CLI `whoami --json` can expose workspace/project context at runtime, but the current key was not accepted for the returned project by the REST API.
- The AppSumo inventory confirms one activated AgenticFlow row. License/redemption material was not copied into this repo.

## Official docs and endpoint shape

Official sources checked:

- `https://docs.agenticflow.ai/developers/api-keys.md`
- `https://docs.agenticflow.ai/developers/authentication.md`
- `https://docs.agenticflow.ai/developers/api-reference.md`
- `https://docs.agenticflow.ai/developers/cli.md`
- `https://docs.agenticflow.ai/developers/agenticflow-cli-capabilities.md`
- `https://docs.agenticflow.ai/integrations/agenticflow-mcp/connecting-to-agenticflow-mcp.md`

Current documented REST base and auth:

- REST base: `https://api.agenticflow.ai/`
- API-key auth: `Authorization: Bearer ***`
- API keys are created/found in the web app at `https://agenticflow.ai/app/workspaces/{WORKSPACE_ID}/settings/api-keys`.
- The documented lowest-risk REST read is `GET /v1/agents/?workspace_id={workspace_id}[&project_id={project_id}&limit=...]`.
- Agents, workflows, knowledge datasets, and sub-agents are project-scoped. Requests outside key scope return `403 Forbidden`; missing/invalid keys return `401 Unauthorized`.

Important doc discrepancy / implementation note:

- `developers/authentication.md` contains an older example host `https://api.agenticflow.com/v1/agents`.
- `developers/api-reference.md`, CLI doctor output, and live probes confirm the current host is `https://api.agenticflow.ai/`.
- Use `https://api.agenticflow.ai/` for new work.

## Runtime verification performed

No writes were performed.

### Public/docs checks

- `https://agenticflow.ai/` returned HTTP 200.
- `https://app.agenticflow.ai/` resolves back to the public AgenticFlow app/marketing entry.
- `https://api.agenticflow.ai/` returned JSON HTTP 404 `Not Found`, confirming a live API host rather than a generic marketing page.
- `https://docs.agenticflow.ai/llms.txt` and `https://docs.agenticflow.ai/llms-full.txt` are reachable and expose the developer/API/CLI pages used above.

### CLI authentication check

The local environment has Node.js 22 and can run the published CLI:

```bash
npx --yes @pixelml/agenticflow-cli --version
# 1.10.5
```

The secure dotenv uses `AGENTICFLOW_AI_KEY`; the CLI expects `AGENTICFLOW_API_KEY`, so the runtime-only smoke check exported the same value under the CLI-recognized name without printing it:

```bash
export AGENTICFLOW_API_KEY=<secure runtime value from AGENTICFLOW_AI_KEY>
npx --yes @pixelml/agenticflow-cli whoami --json
npx --yes @pixelml/agenticflow-cli bootstrap --json
```

Observed safe results:

- `whoami --json` reported `api_key_present: true`.
- `whoami --json` exposed workspace/project context at runtime; the raw IDs were not committed.
- `bootstrap --json` reported auth/backend health when the key was exported under the CLI-recognized env name.
- No existing agents or workforces were returned by the CLI bootstrap summary.
- The CLI returned a model list, blueprint list, schemas, playbooks, and command cheatsheet, which is enough to classify the key as accepted by the platform but not enough to prove REST project access.

### REST checks

Runtime-only `GET` checks with the current key:

- `GET https://api.agenticflow.ai/openapi.json` returned HTTP 401 `Not authenticated` even with bearer auth. Do not use this route as a key-validity probe.
- `GET https://api.agenticflow.ai/v1/agents` returns an HTTP 307 redirect to a non-TLS `http://.../v1/agents/` location. Avoid following this redirect; use the trailing slash form directly.
- `GET https://api.agenticflow.ai/v1/agents/` with bearer auth and no context returned HTTP 400 `Project ID must be provided for project-scoped resource access`.
- `GET https://api.agenticflow.ai/v1/agents/?workspace_id=<cli_context>&project_id=<cli_context>&limit=1` returned HTTP 403 `API key does not have access to this project`. This is the current blocker: the key authenticates, but the available project context is not accepted for this REST read.
- Guessed discovery routes such as `/v1/workspaces`, `/v1/projects`, `/v1/me`, and `/v1/auth/me` are not documented and returned 404 or redirect/degraded behavior. Do not build against them.

## Smallest safe non-mutating endpoint set

Use these only after an operator supplies a project-scoped API key or confirms the correct workspace/project pair for the current key:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate

# If using the current secure dotenv name, pass --secret-name because the repo tool defaults to AGENTICFLOW_API_KEY.
python appsumo_readonly_probe.py agenticflow agents \
  --secret-name AGENTICFLOW_AI_KEY \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --workspace-id <workspace_uuid> \
  --project-id <project_uuid> \
  --page-size 1 \
  --summary-only --json
```

Expected success condition: HTTP 200 with a summary-only count/field report. Any 401 means missing/invalid key. Any 403 means the key is valid but not scoped to that workspace/project; this is the latest observed result for the current runtime key and CLI-returned context. Any 400 about project scope means the workspace/project context is still incomplete for this key.

## Repo tooling update

`tools/appsumo_readonly_probe.py` now includes a guarded `agenticflow agents` resource:

- GET-only.
- Requires `--workspace-id` before making a request.
- Accepts optional `--project-id`; for the current project-scoped API behavior, provide it.
- Supports `--secret-name AGENTICFLOW_AI_KEY` for secure dotenv naming drift, while also working with the default `AGENTICFLOW_API_KEY` name.
- Uses `Authorization: Bearer` and summary-only output like the other AppSumo probes.

The guard intentionally prevents blind calls without workspace context and avoids guessed workspace/project discovery routes.

## n8n / Paperclip recommendation

Do not create a live n8n workflow yet.

Next operator ask:

1. Confirm the AgenticFlow workspace URL, e.g. `https://agenticflow.ai/app/workspaces/<workspace_uuid>/...`.
2. Confirm which project UUID the current API key is scoped to, or create a new key scoped to the CLI-returned project.
3. Prefer a dedicated automation-owned key named `AGENTICFLOW_API_KEY_AUTOMATION` before any scheduled health check.
4. Approve the first summary-only read: list at most one agent via `GET /v1/agents/?workspace_id=...&project_id=...&limit=1`.

After that returns HTTP 200, the smallest disabled/manual-first n8n pack would only summarize counts/metadata for agents. It must not run agents, stream messages, publish, trigger webhooks, create/update/delete agents, create workflows/workforces, or configure MCP connections without a separate write contract and rollback/audit plan.
