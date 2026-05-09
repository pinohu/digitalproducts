param(
    [int]$Port = 9222
)

$ErrorActionPreference = "Stop"
$healthUrl = "http://127.0.0.1:$Port/json/version"

try {
    $response = Invoke-RestMethod -Uri $healthUrl -TimeoutSec 5
    [pscustomobject]@{
        ok = $true
        browser = $response.Browser
        protocolVersion = $response.ProtocolVersion
        userAgent = $response.'User-Agent'
        webSocketDebuggerUrl = $response.webSocketDebuggerUrl
        endpoint = $healthUrl
    } | ConvertTo-Json -Depth 4
} catch {
    [pscustomobject]@{
        ok = $false
        endpoint = $healthUrl
        error = $_.Exception.Message
    } | ConvertTo-Json -Depth 4
    exit 1
}
