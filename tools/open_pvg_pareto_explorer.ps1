param(
    [string]$Repo = "D:\PVG-ANT-Inverse-Geometry-001"
)

$ErrorActionPreference = "Stop"
$Page = Join-Path $Repo "web\pvg-pareto-explorer\index.html"

if (-not (Test-Path $Page)) {
    throw "PVG Pareto Explorer page not found: $Page`nSynchronize the inverse-geometry worktree first."
}

Write-Host "Opening PVG Pareto Explorer..."
Write-Host "Page: $Page"
Start-Process $Page
