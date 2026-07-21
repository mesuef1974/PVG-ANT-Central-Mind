param(
    [string]$Repo = "D:\PVG-ANT-Inverse-Geometry-001"
)

$ErrorActionPreference = "Stop"
$Page = Join-Path $Repo "web\pvg-pareto-explorer\visual-lab-3d.html"

if (-not (Test-Path $Page)) {
    throw "PVG Immersive 3D Visual Lab page not found: $Page`nSynchronize the inverse-geometry worktree first."
}

Write-Host "Opening PVG Immersive 3D Visual Lab..."
Write-Host "Page: $Page"
Start-Process $Page
