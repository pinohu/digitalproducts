param(
    [string]$Distro = "Ubuntu",
    [string]$SessionName = "paperclip-ops"
)

$ErrorActionPreference = "Stop"

wsl -d $Distro -- bash -lc "tmux has-session -t '$SessionName' 2>/dev/null"
if ($LASTEXITCODE -ne 0) {
    Write-Host "No Paperclip tmux session named '$SessionName' is running."
    exit 0
}

wsl -d $Distro -- tmux kill-session -t $SessionName
Write-Host "Stopped Paperclip tmux session '$SessionName'."
