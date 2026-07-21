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
Write-Host "Running PVG tests through the local Pareto explorer..."
Push-Location $Worktree
try {
    $Suites=@(
        "tests/test_pvg_inverse_geometry.py","tests/test_pvg_local_neighborhood.py",
        "tests/test_pvg_prime_pair_edge_atlas.py","tests/test_pvg_prime_triangle_atlas.py",
        "tests/test_pvg_prime_triangle_dynamics.py","tests/test_pvg_prime_tetrahedron_atlas.py",
        "tests/test_pvg_prime_simplex_general.py","tests/test_pvg_arithmetic_terrain.py",
        "tests/test_pvg_level_terrain.py","tests/test_pvg_level_flow.py",
        "tests/test_pvg_multiobjective_geometry.py","tests/test_pvg_pareto_frontier_geometry.py",
        "tests/test_pvg_pareto_explorer.py","tests/test_pvg_pascal_explorer.py",
        "tests/test_pvg_local_additive_cell_atlas.py","tests/test_pvg_additive_face_transition_graph.py",
        "tests/test_pvg_iterated_additive_face_dynamics.py","tests/test_pvg_additive_attraction_basins.py",
        "tests/test_pvg_additive_basin_overlap_geometry.py"
    )
    foreach ($Suite in $Suites) { Invoke-Python312 -PythonArgs @("-m","unittest","-v",$Suite); Assert-LastExitCode -FailureMessage "Test suite failed: $Suite" }
    Invoke-Python312 -PythonArgs @("tools/pvg_inverse_geometry.py","900","--compact"); Assert-LastExitCode -FailureMessage "Passport smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_local_neighborhood.py","30","--steps","3","--compact"); Assert-LastExitCode -FailureMessage "Local-neighborhood smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_prime_simplex_general.py","2,3,5,7,11","--compact"); Assert-LastExitCode -FailureMessage "General simplex smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_arithmetic_terrain.py","60","2","3","--factors","2^2,3,5","--compact"); Assert-LastExitCode -FailureMessage "Edge terrain smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_level_terrain.py","2,3,5","6","--compact"); Assert-LastExitCode -FailureMessage "Global level terrain smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_level_flow.py","2,3,5","6","--compact"); Assert-LastExitCode -FailureMessage "Level flow smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_multiobjective_geometry.py","2,3,5","6","--compact"); Assert-LastExitCode -FailureMessage "Multiobjective geometry smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_pareto_frontier_geometry.py","2,3,5","6","--compact"); Assert-LastExitCode -FailureMessage "Pareto frontier geometry smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_local_additive_cell_atlas.py","--limit","100","--compact"); Assert-LastExitCode -FailureMessage "Local additive cell atlas smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_additive_face_transition_graph.py","--limit","100","--compact"); Assert-LastExitCode -FailureMessage "Additive face transition graph smoke test failed"
    Invoke-Python312 -PythonArgs @("tools/pvg_iterated_additive_face_dynamics.py","--limit","100","--depth","4","--compact"); Assert-LastExitCode -FailureMessage "Iterated additive face dynamics smoke test failed"
    $Pass016Raw=Invoke-Python312 -PythonArgs @("tools/pvg_additive_attraction_basins.py","--limit","100","--depth","5","--summary-only","--compact")
    Assert-LastExitCode -FailureMessage "Additive attraction basins smoke test failed"
    $Pass016=($Pass016Raw | Out-String | ConvertFrom-Json)
    if ($Pass016.scope.start_face_count -ne 300) { throw "PASS-016 start-face count mismatch" }
    if ($Pass016.single_terminal_start_count -ne 195 -or $Pass016.multiple_terminal_start_count -ne 105) { throw "PASS-016 endpoint multiplicity mismatch" }
    if ($Pass016.unresolved_start_count -ne 0 -or $Pass016.reappearing_start_count -ne 10 -or $Pass016.observed_cycle_start_count -ne 0) { throw "PASS-016 bounded status mismatch" }
    if (@($Pass016.verification.PSObject.Properties | Where-Object { -not [bool]$_.Value }).Count -ne 0) { throw "PASS-016 verification flag failure" }
    $Pass017Raw=Invoke-Python312 -PythonArgs @("tools/pvg_additive_basin_overlap_geometry.py","--limit","100","--depth","5","--summary-only","--compact")
    Assert-LastExitCode -FailureMessage "Additive basin overlap geometry smoke test failed"
    $Pass017=($Pass017Raw | Out-String | ConvertFrom-Json)
    if ($Pass017.scope.start_face_count -ne 300 -or $Pass017.scope.terminal_axis_count -ne 10 -or $Pass017.scope.endpoint_signature_count -ne 19) { throw "PASS-017 scope mismatch" }
    if ($Pass017.axis_overlap_graph.edge_count -ne 13 -or ($Pass017.axis_overlap_graph.component_sizes -join ',') -ne '6,1,1,1,1') { throw "PASS-017 overlap graph mismatch" }
    if (($Pass017.axis_overlap_graph.isolated_axes -join ',') -ne '31,43,61,73' -or $Pass017.axis_overlap_graph.cycle_rank -ne 8) { throw "PASS-017 component structure mismatch" }
    if ($Pass017.axis_overlap_graph.pair_overlaps[0].axes[0] -ne 5 -or $Pass017.axis_overlap_graph.pair_overlaps[0].axes[1] -ne 7 -or $Pass017.axis_overlap_graph.pair_overlaps[0].intersection_size -ne 75) { throw "PASS-017 strongest overlap mismatch" }
    if ($Pass017.signature_poset.cover_edge_count -ne 25 -or ($Pass017.signature_poset.rank_distribution.'1') -ne 10 -or ($Pass017.signature_poset.rank_distribution.'2') -ne 1 -or ($Pass017.signature_poset.rank_distribution.'3') -ne 8) { throw "PASS-017 signature poset mismatch" }
    if ($Pass017.gateway_start_count -ne 105 -or @($Pass017.verification.PSObject.Properties | Where-Object { -not [bool]$_.Value }).Count -ne 0) { throw "PASS-017 verification failure" }
    $ExplorerPage=Join-Path $Worktree "web\pvg-pareto-explorer\index.html"
    $PascalPage=Join-Path $Worktree "web\pvg-pareto-explorer\pascal.html"
    if (-not (Test-Path $ExplorerPage)) { throw "PVG Pareto Explorer page missing: $ExplorerPage" }
    if (-not (Test-Path $PascalPage)) { throw "PVG Pascal Explorer page missing: $PascalPage" }
    if ((Get-Item $ExplorerPage).Length -lt 10000) { throw "PVG Pareto Explorer page is unexpectedly small" }
    $TempRoot=[System.IO.Path]::GetTempPath()
    $Jobs=@(
        @{ Tool="tools/pvg_prime_pair_edge_atlas.py"; Dir="pvg-prime-pair-edge-atlas"; Summary="prime-pair-edge-atlas-primes-le-100-summary.json"; CountField="unordered_pair_count"; Expected=300 },
        @{ Tool="tools/pvg_prime_triangle_atlas.py"; Dir="pvg-prime-triangle-atlas"; Summary="prime-triangle-atlas-primes-le-100-summary.json"; CountField="unordered_triangle_count"; Expected=2300 },
        @{ Tool="tools/pvg_prime_triangle_dynamics.py"; Dir="pvg-prime-triangle-dynamics"; Summary="prime-triangle-dynamics-primes-le-100-summary.json"; CountField="unordered_triangle_count"; Expected=2300 },
        @{ Tool="tools/pvg_prime_tetrahedron_atlas.py"; Dir="pvg-prime-tetrahedron-atlas"; Summary="prime-tetrahedron-atlas-primes-le-100-summary.json"; CountField="unordered_tetrahedron_count"; Expected=12650 }
    )
    foreach ($Job in $Jobs) {
        $Output=Join-Path $TempRoot $Job.Dir; if (Test-Path $Output) { Remove-Item -Recurse -Force $Output }
        Invoke-Python312 -PythonArgs @($Job.Tool,"--limit","100","--output-dir",$Output); Assert-LastExitCode -FailureMessage "Atlas generation failed: $($Job.Tool)"
        $Generated=Get-Content -Raw (Join-Path $Output $Job.Summary) | ConvertFrom-Json
        if ($Generated.scope.prime_count -ne 25 -or $Generated.scope.($Job.CountField) -ne $Job.Expected) { throw "Atlas scope verification failed: $($Job.Tool)" }
    }
}
finally { Pop-Location }
Write-Host ""; Write-Host "PVG inverse-geometry worktree synchronized and verified."; Write-Host "Worktree: $Worktree"; Write-Host "HEAD:     $Head"; Write-Host "Explorer: $Worktree\web\pvg-pareto-explorer\index.html"; Write-Host "Pascal:   $Worktree\web\pvg-pareto-explorer\pascal.html"; Write-Host ""; Write-Host "The canonical worktree branch and all stashes were left untouched."
