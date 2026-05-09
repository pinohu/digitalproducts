param(
    [int]$Port = 9222,
    [string]$StartUrl = "about:blank",
    [string]$ProfileDir = "$env:USERPROFILE\\.agent-ops\\chrome-hermes-ops",
    [int]$StartupTimeoutSeconds = 30
)

$ErrorActionPreference = "Stop"

$chromeCandidates = @(
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe"
)

$chromePath = $chromeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $chromePath) {
    throw "Could not find Chrome or Edge."
}

$healthUrl = "http://127.0.0.1:$Port/json/version"

function Test-CdpEndpoint {
    param([string]$Url)

    try {
        $response = Invoke-RestMethod -Uri $Url -TimeoutSec 3
        return [bool]$response.Browser
    } catch {
        return $false
    }
}

if (Test-CdpEndpoint -Url $healthUrl) {
    Write-Host "Hermes browser is already reachable at $healthUrl"
    Write-Host "Profile dir: $ProfileDir"
    exit 0
}

New-Item -ItemType Directory -Force -Path $ProfileDir | Out-Null

$arguments = @(
    "--remote-debugging-port=$Port",
    "--user-data-dir=$ProfileDir",
    "--no-first-run",
    "--no-default-browser-check",
    "--new-window",
    $StartUrl
)

Start-Process -FilePath $chromePath -ArgumentList $arguments | Out-Null

$deadline = (Get-Date).AddSeconds($StartupTimeoutSeconds)
while ((Get-Date) -lt $deadline) {
    if (Test-CdpEndpoint -Url $healthUrl) {
        Write-Host "Hermes browser is reachable at $healthUrl"
        Write-Host "Executable: $chromePath"
        Write-Host "Profile dir: $ProfileDir"
        exit 0
    }
    Start-Sleep -Seconds 1
}

throw "Chrome started but the CDP endpoint did not become healthy within $StartupTimeoutSeconds seconds."
