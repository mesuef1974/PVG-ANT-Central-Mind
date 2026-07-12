[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$RepoPath = "D:\PVG-ANT-Central-Mind",
    [string]$TaskName = "PVG-ANT-Canonical-Sync",
    [ValidateRange(5, 1440)]
    [int]$IntervalMinutes = 15
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$resolvedRepo = (Resolve-Path -LiteralPath $RepoPath).Path
$syncScript = Join-Path $resolvedRepo "tools\sync_canonical_main.ps1"
if (-not (Test-Path -LiteralPath $syncScript -PathType Leaf)) {
    throw "Synchronization script not found: $syncScript"
}

$gitDirectory = Join-Path $resolvedRepo ".git"
if (-not (Test-Path -LiteralPath $gitDirectory)) {
    throw "RepoPath is not the canonical Git clone: $resolvedRepo"
}

$powerShellExe = (Get-Command powershell.exe -ErrorAction Stop).Source
$arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$syncScript`" -Mode SafeSync"

$action = New-ScheduledTaskAction `
    -Execute $powerShellExe `
    -Argument $arguments `
    -WorkingDirectory $resolvedRepo

$trigger = New-ScheduledTaskTrigger `
    -Once `
    -At ((Get-Date).AddMinutes(1)) `
    -RepetitionInterval (New-TimeSpan -Minutes $IntervalMinutes) `
    -RepetitionDuration (New-TimeSpan -Days 3650)

$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal `
    -UserId $currentUser `
    -LogonType Interactive `
    -RunLevel Limited

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew

if ($PSCmdlet.ShouldProcess($TaskName, "Register safe canonical repository synchronization task")) {
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $action `
        -Trigger $trigger `
        -Principal $principal `
        -Settings $settings `
        -Description "Fetch origin/main continuously and fast-forward a clean local main only when safe." `
        -Force | Out-Null

    Start-ScheduledTask -TaskName $TaskName

    $task = Get-ScheduledTask -TaskName $TaskName
    Write-Host "Scheduled task installed."
    Write-Host ("Task name       : {0}" -f $task.TaskName)
    Write-Host ("Task state      : {0}" -f $task.State)
    Write-Host ("Repository      : {0}" -f $resolvedRepo)
    Write-Host ("Interval minutes: {0}" -f $IntervalMinutes)
    Write-Host "The task never hard-resets, force-pushes, stashes, deletes, or resolves conflicts."
}
