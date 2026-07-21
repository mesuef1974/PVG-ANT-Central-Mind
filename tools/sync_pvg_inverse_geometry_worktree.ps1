param(
    [string]$Repo = "D:\PVG-ANT-Central-Mind",
    [string]$Worktree = "D:\PVG-ANT-Inverse-Geometry-001",
    [string]$Remote = "origin",
    [string]$Branch = "agent/pvg-point-classification-inverse-geometry-001",
    [string]$Python = "py.exe"
)

$ErrorActionPreference = "Stop"
function Invoke-Git { param([Parameter(Mandatory=$true)][string]$At,[Parameter(Mandatory=$true)][string[]]$GitArgs); & git -C $At @GitArgs; if ($LASTEXITCODE -ne 0) { throw "git -C '$At' $($GitArgs -join ' ') failed with exit code $LASTEXITCODE" } }
function Invoke-Python312 { param([Parameter(Mandatory=$true)][string[]]$PythonArgs); $LauncherName=[System.IO.Path]::GetFileName($Python).ToLowerInvariant(); if ($LauncherName -eq "py.exe" -or $LauncherName -eq "py") { & $Python -3.12 @PythonArgs } else { & $Python @PythonArgs } }
function Assert-LastExitCode { param([Parameter(Mandatory=$true)][string]$FailureMessage); if ($LASTEXITCODE -ne 0) { throw "$FailureMessage (exit code $LASTEXITCODE)" } }

if (-not (Test-Path $Repo)) { throw "Canonical repository not found: $Repo" }
Write-Host "Fetching remote state without switching the canonical worktree..."
Invoke-Git -At $Repo -GitArgs @("fetch","--prune",$Remote)
$RemoteRef="$Remote/$Branch"
& git -C $Repo rev-parse --verify $RemoteRef *> $null
if ($LASTEXITCODE -ne 0) { throw "Remote branch not found: $RemoteRef" }
if (-not (Test-Path $Worktree)) { Invoke-Git -At $Repo -GitArgs @("worktree","add","--detach",$Worktree,$RemoteRef) }
else {
    & git -C $Worktree rev-parse --is-inside-work-tree *> $null
    if ($LASTEXITCODE -ne 0) { throw "Existing path is not a Git worktree: $Worktree" }
    $Dirty=(& git -C $Worktree status --porcelain)
    if ($Dirty) { throw "Inverse-geometry worktree has local changes. Refusing to overwrite them." }
    Invoke-Git -At $Worktree -GitArgs @("switch","--detach",$RemoteRef)
}
$Head=(& git -C $Worktree rev-parse HEAD).Trim(); $RemoteHead=(& git -C $Repo rev-parse $RemoteRef).Trim()
if ($Head -ne $RemoteHead) { throw "Synchronization verification failed: HEAD=$Head remote=$RemoteHead" }

Write-Host "Running PVG tests through global level terrain..."
Push-Location $Worktree
try {
    $Suites=@(
        "tests/test_pvg_inverse_geometry.py","tests/test_pvg_local_neighborhood.py",
        "tests/test_pvg_prime_pair_edge_atlas.py","tests/test_pvg_prime_triangle_atlas.py",
        "tests/test_pvg_prime_triangle_dynamics.py","tests/test_pvg_prime_tetrahedron_atlas.py",
        "tests/test_pvg_prime_simplex_general.py","tests/test_pvg_arithmetic_terrain.py",
        "tests/test_pvg_level_terrain.py"
    )
    foreach ($Suite in $Suites) { Invoke-Python312 -PythonArgs @("-m","unittest","-v",$Suite); Assert-LastExitCode -FailureMessage "Test suite failed: $Suite" }
    Invoke-Python312 -PythonArgs @("tools/pvg_inverse_geometry.py","900","--compact"); Assert-LastExitCode -FailureMessage "Passport smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_local_neighborhood.py","30","--steps","3","--compact"); Assert-LastExitCode -FailureMessage "Local-neighborhood smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_prime_simplex_general.py","2,3,5,7,11","--compact"); Assert-LastExitCode -FailureMessage "General simplex smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_arithmetic_terrain.py","60","2","3","--factors","2^2,3,5","--compact"); Assert-LastExitCode -FailureMessage "Edge terrain smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_level_terrain.py","2,3,5","6","--compact"); Assert-LastExitCode -FailureMessage "Global level terrain smoke test failed"
    $TempRoot=[System.IO.Path]::GetTempPath()
    $Jobs=@(
        @{ Tool="tools/pvg_prime_pair_edge_atlas.py"; Dir="pvg-prime-pair-edge-atlas"; Summary="prime-pair-edge-atlas-primes-le-100-summary.json"; Csv="prime-pair-edge-atlas-primes-le-100.csv"; CountField="unordered_pair_count"; Expected=300 },
        @{ Tool="tools/pvg_prime_triangle_atlas.py"; Dir="pvg-prime-triangle-atlas"; Summary="prime-triangle-atlas-primes-le-100-summary.json"; Csv="prime-triangle-atlas-primes-le-100.csv"; CountField="unordered_triangle_count"; Expected=2300 },
        @{ Tool="tools/pvg_prime_triangle_dynamics.py"; Dir="pvg-prime-triangle-dynamics"; Summary="prime-triangle-dynamics-primes-le-100-summary.json"; Csv="prime-triangle-dynamics-primes-le-100.csv"; CountField="unordered_triangle_count"; Expected=2300 },
        @{ Tool="tools/pvg_prime_tetrahedron_atlas.py"; Dir="pvg-prime-tetrahedron-atlas"; Summary="prime-tetrahedron-atlas-primes-le-100-summary.json"; Csv="prime-tetrahedron-atlas-primes-le-100.csv"; CountField="unordered_tetrahedron_count"; Expected=12650 }
    )
    foreach ($Job in $Jobs) {
        $Output=Join-Path $TempRoot $Job.Dir; if (Test-Path $Output) { Remove-Item -Recurse -Force $Output }
        Invoke-Python312 -PythonArgs @($Job.Tool,"--limit","100","--output-dir",$Output); Assert-LastExitCode -FailureMessage "Atlas generation failed: $($Job.Tool)"
        $Generated=Get-Content -Raw (Join-Path $Output $Job.Summary) | ConvertFrom-Json
        if ($Generated.scope.prime_count -ne 25 -or $Generated.scope.($Job.CountField) -ne $Job.Expected) { throw "Atlas scope verification failed: $($Job.Tool)" }
    }
}
finally { Pop-Location }
Write-Host ""; Write-Host "PVG inverse-geometry worktree synchronized and verified."; Write-Host "Worktree: $Worktree"; Write-Host "HEAD:     $Head"; Write-Host ""; Write-Host "The canonical worktree branch and all stashes were left untouched."
