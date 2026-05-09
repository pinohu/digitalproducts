param(
    [string]$EnvFile = "$env:USERPROFILE\Documents\.env",
    [string]$PaperclipApiBase = "http://127.0.0.1:3100/api",
    [string]$CompanyId = "4b02078e-90d2-42ed-95d5-c5a54b7d3a16",
    [switch]$EnableStrictMode
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$paperclipConfigPath = Join-Path $env:USERPROFILE ".paperclip\instances\default\config.json"

function Write-Phase {
    param([string]$Message)
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Read-DotEnvFile {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Environment file not found: $Path"
    }

    $map = @{}
    foreach ($line in Get-Content -LiteralPath $Path) {
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed.StartsWith("#")) {
            continue
        }

        $match = [regex]::Match($trimmed, "^(?<key>[A-Za-z_][A-Za-z0-9_]*)=(?<value>.*)$")
        if (-not $match.Success) {
            continue
        }

        $key = $match.Groups["key"].Value
        $value = $match.Groups["value"].Value

        if ($value.Length -ge 2) {
            if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
                $value = $value.Substring(1, $value.Length - 2)
            }
        }

        $map[$key] = $value
    }

    return $map
}

function ConvertTo-PlainObject {
    param($InputObject)

    if ($null -eq $InputObject) {
        return $null
    }

    if ($InputObject -is [string] -or $InputObject -is [ValueType]) {
        return $InputObject
    }

    if ($InputObject -is [System.Collections.IDictionary]) {
        $hash = @{}
        foreach ($entry in $InputObject.GetEnumerator()) {
            $hash[$entry.Key] = ConvertTo-PlainObject $entry.Value
        }
        return $hash
    }

    if ($InputObject -is [System.Collections.IEnumerable]) {
        $items = @()
        foreach ($item in $InputObject) {
            $items += , (ConvertTo-PlainObject $item)
        }
        return $items
    }

    if ($InputObject.PSObject -and $InputObject.PSObject.Properties.Count -gt 0) {
        $hash = @{}
        foreach ($property in $InputObject.PSObject.Properties) {
            $hash[$property.Name] = ConvertTo-PlainObject $property.Value
        }
        return $hash
    }

    return $InputObject
}

function Invoke-PaperclipApi {
    param(
        [ValidateSet("GET", "POST", "PATCH")]
        [string]$Method,
        [string]$Path,
        $Body = $null
    )

    $uri = "{0}/{1}" -f $PaperclipApiBase.TrimEnd("/"), $Path.TrimStart("/")
    $invokeParams = @{
        Method      = $Method
        Uri         = $uri
        ContentType = "application/json"
    }

    if ($null -ne $Body) {
        $invokeParams.Body = ($Body | ConvertTo-Json -Depth 50 -Compress)
    }

    return Invoke-RestMethod @invokeParams
}

function Get-FirstPresentValue {
    param(
        [hashtable]$EnvMap,
        [string[]]$Candidates
    )

    foreach ($candidate in $Candidates) {
        if ($EnvMap.ContainsKey($candidate) -and -not [string]::IsNullOrWhiteSpace($EnvMap[$candidate])) {
            return $EnvMap[$candidate]
        }
    }

    return $null
}

function Join-Toolsets {
    param(
        [string]$Existing,
        [string[]]$Required
    )

    $ordered = New-Object System.Collections.Generic.List[string]
    $seen = New-Object "System.Collections.Generic.HashSet[string]" ([System.StringComparer]::OrdinalIgnoreCase)

    foreach ($token in ($Existing -split ",")) {
        $trimmed = $token.Trim()
        if (-not $trimmed) {
            continue
        }
        if ($seen.Add($trimmed)) {
            $ordered.Add($trimmed)
        }
    }

    foreach ($token in $Required) {
        $trimmed = $token.Trim()
        if (-not $trimmed) {
            continue
        }
        if ($seen.Add($trimmed)) {
            $ordered.Add($trimmed)
        }
    }

    return ($ordered -join ",")
}

function New-SecretRef {
    param([string]$SecretId)

    return @{
        type     = "secret_ref"
        secretId = $SecretId
        version  = "latest"
    }
}

$secretManifest = @(
    @{ Name = "OPENAI_API_KEY"; Candidates = @("OPENAI_API_KEY", "OPEN_AI_API_KEY"); Description = "Primary OpenAI credential for runtime APIs and auxiliary tooling." },
    @{ Name = "ANTHROPIC_API_KEY"; Candidates = @("ANTHROPIC_API_KEY", "NEW_ANTHROPIC_KEY"); Description = "Anthropic provider credential for cross-provider execution." },
    @{ Name = "OPENROUTER_API_KEY"; Candidates = @("OPENROUTER_API_KEY", "OPEN_ROUTER_API_KEY"); Description = "OpenRouter provider credential for fallback model routing." },
    @{ Name = "GITHUB_TOKEN"; Candidates = @("GITHUB_TOKEN_CROP_TOKEN", "GITHUB_CLASSIC_TOKEN", "NEW_GITHUB_REPO_CLAUDE_COMPANION_FINE_GRAINED_API_KEY"); Description = "GitHub token for repo, issue, and deployment operations." },
    @{ Name = "DATABASE_URL"; Candidates = @("DATABASE_URL"); Description = "Primary database connection string for repo tooling and automation." },
    @{ Name = "NEON_API_KEY"; Candidates = @("NEON_API_KEY"); Description = "Neon control-plane credential for database lifecycle work." },
    @{ Name = "N8N_API_KEY"; Candidates = @("N8N_API_KEY"); Description = "n8n API key for workflow deployment and inspection." },
    @{ Name = "N8N_CLIENT_ID"; Candidates = @("N8N_CLIENT_ID"); Description = "n8n OAuth client id when API integrations require it." },
    @{ Name = "N8N_CLIENT_SECRET"; Candidates = @("N8N_CLIENT_SECRET"); Description = "n8n OAuth client secret when API integrations require it." },
    @{ Name = "VERCEL_TOKEN"; Candidates = @("VERCEL_TOKEN_GITTOKEN"); Description = "Vercel token for preview and production deployments." },
    @{ Name = "CLOUDFLARE_API_TOKEN"; Candidates = @("CLOUDFLARE_API_TOKEN"); Description = "Cloudflare API token for DNS and deployment operations." },
    @{ Name = "CLOUDFLARE_ACCOUNT_ID"; Candidates = @("CLOUDFLARE_ACCOUNT_ID"); Description = "Cloudflare account identifier used by deployment tooling." },
    @{ Name = "RAILWAY_TOKEN"; Candidates = @("RAILWAY_API_TOKEN", "RAILWAY_TOKEN"); Description = "Railway token for app and environment management." },
    @{ Name = "RENDER_API_KEY"; Candidates = @("RENDER_API_KEY"); Description = "Render API credential for deployment and service control." },
    @{ Name = "SUPABASE_API_KEY_SECRET"; Candidates = @("SUPABASE_API_KEY_SECRET"); Description = "Supabase service key for backend integration tasks." },
    @{ Name = "SUPABASE_API_KEY_PUBLISHABLE"; Candidates = @("SUPABASE_API_KEY_PUBLISHABLE"); Description = "Supabase publishable key for app configuration." },
    @{ Name = "STRIPE_SECRET_KEY"; Candidates = @("STRIPE_SECRET_KEY"); Description = "Stripe secret key for billing and checkout integrations." },
    @{ Name = "STRIPE_PUBLISHABLE_KEY"; Candidates = @("STRIPE_PUBLISHABLE_KEY"); Description = "Stripe publishable key for storefront and checkout wiring." },
    @{ Name = "EXA_AI_MCP_API_KEY"; Candidates = @("EXA_AI_MCP_API_KEY"); Description = "Search and extraction credential for research tooling." },
    @{ Name = "COMPOSIO_API_KEY"; Candidates = @("COMPOSIO_API_KEY"); Description = "Composio credential for connected app automation." },
    @{ Name = "SMITHERY_API_KEY"; Candidates = @("SMITHERY_API_KEY"); Description = "Smithery credential for MCP ecosystem expansion." },
    @{ Name = "AGENTICFLOW_AI_KEY"; Candidates = @("AGENTICFLOW_AI_KEY"); Description = "AgenticFlow credential for agent workflow experiments." },
    @{ Name = "AITABLE_API_KEY"; Candidates = @("AITABLE_API_KEY"); Description = "AITable credential for structured operational data." },
    @{ Name = "BOOST_SPACE_API_KEY"; Candidates = @("BOOST_SPACE_API_KEY"); Description = "Boost.space credential for records and data sync." },
    @{ Name = "DADAN_API_KEY"; Candidates = @("DADAN_API_KEY"); Description = "Dadan credential for onboarding and product video assets." },
    @{ Name = "EMAILIT_API_KEY"; Candidates = @("EMAILIT_API_KEY", "EMAILIT_API_KEY_1", "EMAILIT_API_KEY_2", "EMAILIT_API_KEY_FOR_AILUROPHOBIA"); Description = "Emailit credential for transactional email operations." },
    @{ Name = "FLOTIQ_API_KEY"; Candidates = @("FLOTIQ_API_KEY"); Description = "Flotiq CMS credential for content modeling and delivery." },
    @{ Name = "FORMALOO_API_KEY"; Candidates = @("FORMALOO_API_KEY"); Description = "Formaloo credential for forms and workflows." },
    @{ Name = "FORMALOO_API_SECRET"; Candidates = @("FORMALOO_API_SECRET"); Description = "Formaloo secret for authenticated form automation." },
    @{ Name = "GETLATE_DEV_API_KEY"; Candidates = @("GETLATE_DEV_API_KEY"); Description = "Late credential for deploy and release operations." },
    @{ Name = "LUNACAL_API_KEY"; Candidates = @("LUNACAL_API_KEY"); Description = "Lunacal credential for scheduling and booking flows." },
    @{ Name = "PROCESIO_API_KEY"; Candidates = @("PROCESIO_API_KEY"); Description = "Procesio credential for low-code automation orchestration." },
    @{ Name = "SMS_IT_API_KEY"; Candidates = @("SMS_IT_API_KEY", "SMS_IT_API_KEY_1"); Description = "SMS-iT credential for CRM and messaging execution." },
    @{ Name = "THOUGHTLY_API_KEY"; Candidates = @("THOUGHTLY_API_KEY"); Description = "Thoughtly credential for voice and conversation workflows." },
    @{ Name = "TRAFFT_CLIENT_ID"; Candidates = @("TRAFFT_CLIENT_ID"); Description = "Trafft client id for scheduling workflows." },
    @{ Name = "TRAFFT_CLIENT_SECRET"; Candidates = @("TRAFFT_CLIENT_SECRET"); Description = "Trafft client secret for scheduling workflows." },
    @{ Name = "VADOO_AI_API_KEY"; Candidates = @("VADOO_AI_API_KEY"); Description = "Vadoo AI credential for short-form content generation." },
    @{ Name = "VISTA_SOCIAL_API_KEY"; Candidates = @("VISTA_SOCIAL_API_KEY"); Description = "Vista Social credential for social publishing." },
    @{ Name = "WBIZTOOL_COM_API_KEY"; Candidates = @("WBIZTOOL_COM_API_KEY"); Description = "WbizTool credential for business ops integrations." }
)

$browserOperatorInstructions = @"
# Browser Operations Lead

You are the browser-first operator for this business.

## Mission

- Own browser-only SaaS execution paths across launch, CRM, storefront, scheduling, analytics, and back-office tools.
- Prefer APIs when they are available and reliable.
- When APIs are absent, brittle, or incomplete, use the browser toolsets against the dedicated Windows Chrome profile documented in `00-foundation/operator-system/browser-ops.md`.
- Convert repeatable browser work into repo truth: checklists, SOPs, issue comments, and launch docs.

## Canon

- `FRAMEWORK.md`
- `ROADMAP.md`
- `automation/pipeline.md`
- `10-execution-sprints/current-sprint.md`
- `00-foundation/operator-system/README.md`
- `00-foundation/operator-system/approval-matrix.md`
- `00-foundation/operator-system/20-recurring-workflows.md`
- `00-foundation/operator-system/google-drive-knowledge-base.md`
- `00-foundation/operator-system/browser-ops.md`

## Workflow Rules

- Use `Authorization: Bearer $PAPERCLIP_API_KEY` on every Paperclip API request.
- Use `X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID` on every Paperclip API request that writes or mutates data.
- Use `http://127.0.0.1:3100/api` as the Paperclip API base.
- Use `/mnt/c/Users/ohu00/Desktop/digitalproducts` as the project workspace.
- Document any browser-only blocker, anti-bot friction, or missing credential path clearly in both the repo and the issue thread.

## Autonomy

- Follow the approval matrix.
- Be aggressive about shipping low-risk progress.
- Be conservative with destructive actions, financial operations, account security changes, or irreversible publishing steps.
"@

Write-Phase "Loading environment vault"
$envMap = Read-DotEnvFile -Path $EnvFile

Write-Phase "Checking Paperclip health"
$health = Invoke-RestMethod -Uri "$($PaperclipApiBase.TrimEnd('/'))/health"
if ($health.status -ne "ok") {
    throw "Paperclip is not healthy."
}

Write-Phase "Syncing encrypted company secrets"
$secretResponse = Invoke-PaperclipApi -Method GET -Path "/companies/$CompanyId/secrets"
$existingSecrets = @($secretResponse)
$secretIdsByName = @{}
$createdCount = 0
$rotatedCount = 0
$missingSecrets = New-Object System.Collections.Generic.List[string]

foreach ($entry in $secretManifest) {
    $value = Get-FirstPresentValue -EnvMap $envMap -Candidates $entry.Candidates
    if ([string]::IsNullOrWhiteSpace($value)) {
        $missingSecrets.Add($entry.Name)
        continue
    }

    $existing = $existingSecrets | Where-Object { $_.name -eq $entry.Name } | Select-Object -First 1
    if ($null -eq $existing) {
        $created = Invoke-PaperclipApi -Method POST -Path "/companies/$CompanyId/secrets" -Body @{
            name        = $entry.Name
            provider    = "local_encrypted"
            value       = $value
            description = $entry.Description
        }
        $secretIdsByName[$entry.Name] = $created.id
        $existingSecrets += $created
        $createdCount += 1
    }
    else {
        Invoke-PaperclipApi -Method POST -Path "/secrets/$($existing.id)/rotate" -Body @{
            value = $value
        } | Out-Null

        if ($entry.Description) {
            Invoke-PaperclipApi -Method PATCH -Path "/secrets/$($existing.id)" -Body @{
                name        = $entry.Name
                description = $entry.Description
            } | Out-Null
        }

        $secretIdsByName[$entry.Name] = $existing.id
        $rotatedCount += 1
    }
}

$sharedEnv = @{}
foreach ($secretName in $secretIdsByName.Keys) {
    $sharedEnv[$secretName] = New-SecretRef -SecretId $secretIdsByName[$secretName]
}

Write-Phase "Upgrading existing agents"
$agentResponse = Invoke-PaperclipApi -Method GET -Path "/companies/$CompanyId/agents"
$agents = @($agentResponse)
$requiredToolsets = @("browser", "mcp-chromeops", "mcp-local-deep-research")
$patchedAgents = New-Object System.Collections.Generic.List[string]

foreach ($agent in $agents) {
    $adapterConfig = @{
        cwd            = $agent.adapterConfig.cwd
        model          = $agent.adapterConfig.model
        graceSec       = $agent.adapterConfig.graceSec
        provider       = $agent.adapterConfig.provider
        toolsets       = Join-Toolsets -Existing ([string]$agent.adapterConfig.toolsets) -Required $requiredToolsets
        timeoutSec     = $agent.adapterConfig.timeoutSec
        checkpoints    = $agent.adapterConfig.checkpoints
        worktreeMode   = $agent.adapterConfig.worktreeMode
        hermesCommand  = $agent.adapterConfig.hermesCommand
        persistSession = $agent.adapterConfig.persistSession
        paperclipApiUrl = $agent.adapterConfig.paperclipApiUrl
        env            = $sharedEnv
    }

    $runtimeConfig = @{
        heartbeat = @{
            enabled           = $true
            maxConcurrentRuns = 1
        }
    }

    try {
        Invoke-PaperclipApi -Method PATCH -Path "/agents/$($agent.id)" -Body @{
            adapterConfig = $adapterConfig
            runtimeConfig = $runtimeConfig
        } | Out-Null
    }
    catch {
        throw "Failed to patch agent '$($agent.name)' ($($agent.id)): $($_.Exception.Message)"
    }

    $patchedAgents.Add($agent.name)
}

$chief = $agents | Where-Object { $_.name -eq "Chief of Staff" } | Select-Object -First 1
if ($null -ne $chief) {
    Write-Phase "Granting Chief of Staff controlled org-building permissions"
    Invoke-PaperclipApi -Method PATCH -Path "/agents/$($chief.id)/permissions" -Body @{
        canCreateAgents = $true
        canAssignTasks  = $true
    } | Out-Null
}

$browserOperator = $agents | Where-Object { $_.name -eq "Browser Operations Lead" } | Select-Object -First 1
if ($null -eq $browserOperator) {
    Write-Phase "Creating Browser Operations Lead"
    $browserOperator = Invoke-PaperclipApi -Method POST -Path "/companies/$CompanyId/agents" -Body @{
        name         = "Browser Operations Lead"
        role         = "engineer"
        title        = "Managed Hermes Browser Operations Lead"
        reportsTo    = if ($null -ne $chief) { $chief.id } else { $null }
        capabilities = "Owns browser-only SaaS execution, UI verification, and workflow completion across tools that lack reliable APIs."
        adapterType  = "hermes_local"
        adapterConfig = @{
            cwd            = "/mnt/c/Users/ohu00/Desktop/digitalproducts"
            model          = "gpt-5.5"
            graceSec       = 15
            provider       = "openai-codex"
            toolsets       = "terminal,file,todo,clarify,memory,session_search,skills,browser,mcp-chromeops,mcp-local-deep-research"
            timeoutSec     = 900
            checkpoints    = $false
            worktreeMode   = $false
            hermesCommand  = "/home/ohu/.local/bin/hermes"
            persistSession = $true
            paperclipApiUrl = "http://127.0.0.1:3100/api"
            env            = $sharedEnv
        }
        instructionsBundle = @{
            entryFile = "AGENTS.md"
            files     = @{
                "AGENTS.md" = $browserOperatorInstructions.Trim()
            }
        }
        runtimeConfig = @{
            heartbeat = @{
                enabled           = $true
                maxConcurrentRuns = 1
            }
        }
    }
}

if ($EnableStrictMode) {
    Write-Phase "Enabling Paperclip strict secret mode in local config"
    $config = Get-Content -Raw -LiteralPath $paperclipConfigPath | ConvertFrom-Json
    if (-not $config.secrets.strictMode) {
        $config.secrets.strictMode = $true
        $config | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $paperclipConfigPath
    }
}

Write-Phase "Verifying upgraded company state"
$postSecrets = Invoke-PaperclipApi -Method GET -Path "/companies/$CompanyId/secrets"
$postAgents = Invoke-PaperclipApi -Method GET -Path "/companies/$CompanyId/agents"

$summary = [pscustomobject]@{
    CompanyId             = $CompanyId
    SecretCount           = @($postSecrets).Count
    CreatedSecrets        = $createdCount
    RotatedSecrets        = $rotatedCount
    MissingSecretCount    = $missingSecrets.Count
    MissingSecrets        = @($missingSecrets)
    PatchedAgentCount     = $patchedAgents.Count
    BrowserOperatorExists = [bool](@($postAgents | Where-Object { $_.name -eq "Browser Operations Lead" }).Count)
    StrictModeRequested   = [bool]$EnableStrictMode
}

$summary | ConvertTo-Json -Depth 10
