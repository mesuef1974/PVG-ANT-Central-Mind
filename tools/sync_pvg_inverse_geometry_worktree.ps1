param(
    [string]$Repo = "D:\PVG-ANT-Central-Mind",
    [string]$Worktree = "D:\PVG-ANT-Inverse-Geometry-001",
    [string]$Remote = "origin",
    [string]$Branch = "agent/pvg-point-classification-inverse-geometry-001",
    [string]$Python = "py.exe"
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([string]$At, [string[]]$Args)
    & git -C $At @Args
    if ($LASTEXITCODE -ne 0) {
        throw "git -C '$At' $($Args -join ' ') failed with exit code $LASTEXITCODE"
    }
}

if (-not (Test-Path $Repo)) {
    throw "Canonical repository not found: $Repo"
}

Write-Host "Fetching remote state without switching the canonical worktree..."
Invoke-Git -At $Repo -Args @("fetch", "--prune", $Remote)

$RemoteRef = "$Remote/$Branch"
& git -C $Repo rev-parse --verify $RemoteRef *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Remote branch not found: $RemoteRef"
}

if (-not (Test-Path $Worktree)) {
    Write-Host "Creating detached worktree at $Worktree..."
    Invoke-Git -At $Repo -Args @("worktree", "add", "--detach", $Worktree, $RemoteRef)
}
else {
    & git -C $Worktree rev-parse --is-inside-work-tree *> $null
    if ($LASTEXITCODE -ne 0) {
        throw "Existing path is not a Git worktree: $Worktree"
    }

    $Dirty = (& git -C $Worktree status --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to inspect worktree status: $Worktree"
    }
    if ($Dirty) {
        throw "Inverse-geometry worktree has local changes. Refusing to overwrite them."
    }

    Write-Host "Updating detached worktree to $RemoteRef..."
    Invoke-Git -At $Worktree -Args @("switch", "--detach", $RemoteRef)
}

$Head = (& git -C $Worktree rev-parse HEAD).Trim()
$RemoteHead = (& git -C $Repo rev-parse $RemoteRef).Trim()
if ($Head -ne $RemoteHead) {
    throw "Synchronization verification failed: HEAD=$Head remote=$RemoteHead"
}

Write-Host "Running PVG inverse-geometry and local-neighborhood tests..."
Push-Location $Worktree
try {
    & $Python -3.12 -m unittest -v tests/test_pvg_inverse_geometry.py
    if ($LASTEXITCODE -ne 0) { throw "Inverse-geometry tests failed" }

    & $Python -3.12 -m unittest -v tests/test_pvg_local_neighborhood.py
    if ($LASTEXITCODE -ne 0) { throw "Local-neighborhood tests failed" }

    & $Python -3.12 tools/pvg_inverse_geometry.py 900 --compact
    if ($LASTEXITCODE -ne 0) { throw "Passport smoke test failed" }

    & $Python -3.12 tools/pvg_local_neighborhood.py 30 --steps 3 --compact
    if ($LASTEXITCODE -ne 0) { throw "Local-neighborhood smoke test failed" }
}
finally {
    Pop-Location
}

Write-Host ""
Write-Host "PVG inverse-geometry worktree synchronized and verified."
Write-Host "Worktree: $Worktree"
Write-Host "HEAD:     $Head"
Write-Host ""
Write-Host "The canonical worktree branch and all stashes were left untouched."
