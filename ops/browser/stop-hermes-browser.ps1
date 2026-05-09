param(
    [int]$Port = 9222,
    [string]$ProfileDir = "$env:USERPROFILE\\.agent-ops\\chrome-hermes-ops"
)

$ErrorActionPreference = "Stop"

$normalizedProfileDir = [System.IO.Path]::GetFullPath($ProfileDir)
$targetProcesses = Get-CimInstance Win32_Process |
    Where-Object {
        ($_.Name -in @("chrome.exe", "msedge.exe")) -and
        $_.CommandLine -like "*--remote-debugging-port=$Port*" -and
        $_.CommandLine -like "*$normalizedProfileDir*"
    }

if (-not $targetProcesses) {
    Write-Host "No Hermes browser processes matched port $Port and profile $normalizedProfileDir"
    exit 0
}

$targetProcesses | ForEach-Object {
    Stop-Process -Id $_.ProcessId -Force
}

Write-Host "Stopped $($targetProcesses.Count) Hermes browser process(es)."
