param(
    [string]$Distro = "Ubuntu",
    [string]$SessionName = "paperclip-ops",
    [int]$Port = 3100,
    [int]$StartupTimeoutSeconds = 60
)

$ErrorActionPreference = "Stop"

$healthUrl = "http://127.0.0.1:$Port/api/health"
$startCommand = 'export TERM=xterm-256color; ~/.npm-global/bin/paperclipai run >> ~/.paperclip/instances/default/logs/paperclip-tmux.log 2>&1'

function Test-PaperclipHealth {
    param([string]$Url)

    try {
        $response = Invoke-WebRequest -UseBasicParsing -Uri $Url -TimeoutSec 5
        return $response.StatusCode -eq 200
    } catch {
        return $false
    }
}

function Test-TmuxSession {
    param(
        [string]$DistroName,
        [string]$Name
    )

    wsl -d $DistroName -- bash -lc "tmux has-session -t '$Name' 2>/dev/null"
    return $LASTEXITCODE -eq 0
}

if (Test-PaperclipHealth -Url $healthUrl) {
    Write-Host "Paperclip is already healthy at $healthUrl"
    exit 0
}

$sessionExists = Test-TmuxSession -DistroName $Distro -Name $SessionName

if (-not $sessionExists) {
    wsl -d $Distro -- tmux new-session -d -s $SessionName -c /home/ohu
    Start-Sleep -Seconds 1
    wsl -d $Distro -- tmux send-keys -t $SessionName $startCommand Enter
}

$deadline = (Get-Date).AddSeconds($StartupTimeoutSeconds)
while ((Get-Date) -lt $deadline) {
    if (Test-PaperclipHealth -Url $healthUrl) {
        Write-Host "Paperclip is healthy at $healthUrl"
        Write-Host "Attach with: wsl -d $Distro -- tmux attach -t $SessionName"
        exit 0
    }
    Start-Sleep -Seconds 2
}

Write-Error "Paperclip did not become healthy within $StartupTimeoutSeconds seconds. Inspect the tmux session with: wsl -d $Distro -- tmux attach -t $SessionName"
