param(
    [switch]$Prod
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$sitePath = Join-Path $repoRoot "08-platforms\vercel-sites\suitedash-good-parts-preview"
$envPath = Join-Path $repoRoot "tools\.env"
$vercelCli = "C:\Users\ohu00\AppData\Roaming\npm\vercel.cmd"
$linkPath = Join-Path $sitePath ".vercel\project.json"

function Get-EnvValue {
    param(
        [string]$Path,
        [string]$Name
    )

    $line = Get-Content $Path | Where-Object { $_ -match "^$Name=" } | Select-Object -First 1
    if (-not $line) {
        return $null
    }

    return (($line -split "=", 2)[1]).Trim()
}

if (-not (Test-Path $envPath)) {
    throw "Missing tools environment file at $envPath"
}

if (-not (Test-Path $sitePath)) {
    throw "Missing Vercel site path at $sitePath"
}

if (-not (Test-Path $vercelCli)) {
    throw "Vercel CLI not found at $vercelCli"
}

if (-not (Test-Path $linkPath)) {
    throw "Missing local Vercel link state at $linkPath. Run a first manual deploy or link this folder before using the helper."
}

$token = Get-EnvValue -Path $envPath -Name "VERCEL_TOKEN"
if (-not $token) {
    throw "VERCEL_TOKEN is missing in $envPath"
}

$target = if ($Prod) { "production" } else { "preview" }

$arguments = @(
    "deploy",
    $sitePath,
    "-y",
    "--target",
    $target,
    "--token",
    $token
)

& $vercelCli @arguments
