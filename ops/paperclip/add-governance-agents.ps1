[CmdletBinding()]
param(
    [string]$CompanyId = "4b02078e-90d2-42ed-95d5-c5a54b7d3a16",
    [switch]$WakeAgents
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-LocalPaperclipApi {
    param(
        [Parameter(Mandatory = $true)][string]$Method,
        [Parameter(Mandatory = $true)][string]$Path,
        [object]$Body
    )

    $uri = "http://127.0.0.1:3100/api$Path"
    $invokeParams = @{
        Method      = $Method
        Uri         = $uri
        ContentType = "application/json"
    }

    if ($null -ne $Body) {
        $invokeParams.Body = ($Body | ConvertTo-Json -Depth 20)
    }

    Invoke-RestMethod @invokeParams
}

function ConvertTo-HashtableDeep {
    param([Parameter(Mandatory = $true)]$InputObject)

    if ($InputObject -is [System.Collections.IDictionary]) {
        $table = @{}
        foreach ($key in $InputObject.Keys) {
            $table[$key] = ConvertTo-HashtableDeep -InputObject $InputObject[$key]
        }
        return $table
    }

    if ($InputObject -is [System.Collections.IEnumerable] -and -not ($InputObject -is [string])) {
        $items = @()
        foreach ($item in $InputObject) {
            $items += ,(ConvertTo-HashtableDeep -InputObject $item)
        }
        return $items
    }

    if ($InputObject -is [pscustomobject]) {
        $table = @{}
        foreach ($property in $InputObject.PSObject.Properties) {
            $table[$property.Name] = ConvertTo-HashtableDeep -InputObject $property.Value
        }
        return $table
    }

    return $InputObject
}

$agents = @(Invoke-LocalPaperclipApi -Method GET -Path "/companies/$CompanyId/agents")
$chief = $agents | Where-Object { $_.name -eq "Chief of Staff" } | Select-Object -First 1
$template = $agents | Where-Object { $_.name -eq "Automation Engineer" } | Select-Object -First 1

if ($null -eq $template) {
    throw "Automation Engineer template agent not found."
}

$definitions = @(
    @{
        name         = "Quality Gatekeeper"
        title        = "Managed Hermes Quality Gatekeeper"
        capabilities = "Owns Playwright, Storybook, Lighthouse, Pa11y, and CI evidence. Keeps repo truth and release evidence aligned."
        instructions = @"
Specialization:
- Own package.json, .storybook/, tests/e2e/, .github/workflows/quality-gates.yml, .lighthouserc.json, .pa11yci.json, and governance/release-state.json quality fields.
- Run quality checks, fix failures, and keep evidence artifacts aligned with repo truth.
- Refuse to imply release readiness when checks or docs disagree.
"@
    }
    @{
        name         = "Accessibility Auditor"
        title        = "Managed Hermes Accessibility Auditor"
        capabilities = "Owns WCAG 2.2 AA enforcement, keyboard flow review, focus states, semantics, contrast, and usability for browser-facing surfaces."
        instructions = @"
Specialization:
- Own accessibility and usability quality across static pages, forms, and future product surfaces.
- Prioritize keyboard navigation, visible focus, semantic HTML, form clarity, contrast, motion safety, and mobile readability.
- Update docs when a surface still needs human validation instead of hiding the gap.
"@
    }
    @{
        name         = "Release Governor"
        title        = "Managed Hermes Release Governor"
        capabilities = "Owns release-state policy, manual approvals, shipped-gate truth, and launch-readiness evidence."
        instructions = @"
Specialization:
- Own governance/release-state.json, governance/policies/, manual-actions-ledger.md, mobile-control-center.md, and shipped-gate docs.
- Keep release claims truthful. Block 'done', 'live', and 'shipped' states until evidence and approvals exist.
- Prefer explicit blockers and operator asks over optimistic wording.
"@
    }
)

$created = New-Object System.Collections.Generic.List[string]

foreach ($definition in $definitions) {
    $existing = $agents | Where-Object { $_.name -eq $definition.name } | Select-Object -First 1
    if ($null -ne $existing) {
        continue
    }

    $body = @{
        name          = $definition.name
        role          = "engineer"
        title         = $definition.title
        capabilities  = $definition.capabilities
        adapterType   = "hermes_local"
        adapterConfig = @{
            cwd             = "/mnt/c/Users/ohu00/Desktop/digitalproducts"
            model           = "gpt-5.5"
            graceSec        = 15
            provider        = "openai-codex"
            toolsets        = "terminal,file,todo,clarify,memory,session_search,skills,browser,mcp-chromeops,mcp-local-deep-research"
            timeoutSec      = 900
            checkpoints     = $false
            worktreeMode    = $false
            hermesCommand   = "/home/ohu/.local/bin/hermes"
            persistSession  = $true
            paperclipApiUrl = "http://127.0.0.1:3100/api"
        }
        instructionsBundle = @{
            entryFile = "AGENTS.md"
            files     = @{
                "AGENTS.md" = $definition.instructions.Trim()
            }
        }
        runtimeConfig = @{
            heartbeat = @{
                enabled           = $true
                maxConcurrentRuns = 1
            }
        }
    }

    $createdAgent = Invoke-LocalPaperclipApi -Method POST -Path "/companies/$CompanyId/agents" -Body $body
    $created.Add($createdAgent.name) | Out-Null

    if ($WakeAgents) {
        Invoke-LocalPaperclipApi -Method POST -Path "/agents/$($createdAgent.id)/wakeup" -Body @{} | Out-Null
    }
}

[pscustomobject]@{
    CompanyId     = $CompanyId
    CreatedAgents = @($created)
    CreatedCount  = $created.Count
} | ConvertTo-Json -Depth 10
