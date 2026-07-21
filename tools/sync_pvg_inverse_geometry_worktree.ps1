param(
    [string]$Repo = "D:\PVG-ANT-Central-Mind",
    [string]$Worktree = "D:\PVG-ANT-Inverse-Geometry-001",
    [string]$Remote = "origin",
    [string]$Branch = "agent/pvg-point-classification-inverse-geometry-001",
    [string]$Python = "py.exe"
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)][string]$At,
        [Parameter(Mandatory = $true)][string[]]$GitArgs
    )

    & git -C $At @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git -C '$At' $($GitArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
}

function Invoke-Python312 {
    param([Parameter(Mandatory = $true)][string[]]$PythonArgs)

    $LauncherName = [System.IO.Path]::GetFileName($Python).ToLowerInvariant()
    if ($LauncherName -eq "py.exe" -or $LauncherName -eq "py") {
        & $Python -3.12 @PythonArgs
    }
    else {
        & $Python @PythonArgs
    }
}

function Assert-LastExitCode {
    param([Parameter(Mandatory = $true)][string]$FailureMessage)

    if ($LASTEXITCODE -ne 0) {
        throw "$FailureMessage (exit code $LASTEXITCODE)"
    }
}

if (-not (Test-Path $Repo)) {
    throw "Canonical repository not found: $Repo"
}

Write-Host "Fetching remote state without switching the canonical worktree..."
Invoke-Git -At $Repo -GitArgs @("fetch", "--prune", $Remote)

$RemoteRef = "$Remote/$Branch"
& git -C $Repo rev-parse --verify $RemoteRef *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Remote branch not found: $RemoteRef"
}

if (-not (Test-Path $Worktree)) {
    Write-Host "Creating detached worktree at $Worktree..."
    Invoke-Git -At $Repo -GitArgs @("worktree", "add", "--detach", $Worktree, $RemoteRef)
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
    Invoke-Git -At $Worktree -GitArgs @("switch", "--detach", $RemoteRef)
}

$Head = (& git -C $Worktree rev-parse HEAD).Trim()
$RemoteHead = (& git -C $Repo rev-parse $RemoteRef).Trim()
if ($Head -ne $RemoteHead) {
    throw "Synchronization verification failed: HEAD=$Head remote=$RemoteHead"
}

Write-Host "Running PVG point, neighborhood, pair-edge, and prime-triangle tests..."
Push-Location $Worktree
try {
    Invoke-Python312 -PythonArgs @("-m", "unittest", "-v", "tests/test_pvg_inverse_geometry.py")
    Assert-LastExitCode -FailureMessage "Inverse-geometry tests failed"

    Invoke-Python312 -PythonArgs @("-m", "unittest", "-v", "tests/test_pvg_local_neighborhood.py")
    Assert-LastExitCode -FailureMessage "Local-neighborhood tests failed"

    Invoke-Python312 -PythonArgs @("-m", "unittest", "-v", "tests/test_pvg_prime_pair_edge_atlas.py")
    Assert-LastExitCode -FailureMessage "Prime-pair edge atlas tests failed"

    Invoke-Python312 -PythonArgs @("-m", "unittest", "-v", "tests/test_pvg_prime_triangle_atlas.py")
    Assert-LastExitCode -FailureMessage "Prime-axis triangle atlas tests failed"

    Invoke-Python312 -PythonArgs @("tools/pvg_inverse_geometry.py", "900", "--compact")
    Assert-LastExitCode -FailureMessage "Passport smoke test failed"

    Invoke-Python312 -PythonArgs @("tools/pvg_local_neighborhood.py", "30", "--steps", "3", "--compact")
    Assert-LastExitCode -FailureMessage "Local-neighborhood smoke test failed"

    $TempRoot = [System.IO.Path]::GetTempPath()

    $PairOutput = Join-Path $TempRoot "pvg-prime-pair-edge-atlas"
    if (Test-Path $PairOutput) {
        Remove-Item -Recurse -Force $PairOutput
    }
    Invoke-Python312 -PythonArgs @(
        "tools/pvg_prime_pair_edge_atlas.py",
        "--limit", "100",
        "--output-dir", $PairOutput
    )
    Assert-LastExitCode -FailureMessage "Prime-pair edge atlas generation failed"

    $PairSummaryPath = Join-Path $PairOutput "prime-pair-edge-atlas-primes-le-100-summary.json"
    $PairCsvPath = Join-Path $PairOutput "prime-pair-edge-atlas-primes-le-100.csv"
    if (-not (Test-Path $PairSummaryPath) -or -not (Test-Path $PairCsvPath)) {
        throw "Prime-pair atlas outputs were not created"
    }

    $PairGenerated = Get-Content -Raw $PairSummaryPath | ConvertFrom-Json
    if ($PairGenerated.scope.prime_count -ne 25 -or $PairGenerated.scope.unordered_pair_count -ne 300) {
        throw "Prime-pair atlas scope verification failed"
    }
    if ($PairGenerated.distinguished_pairs.both_level_preserved.Count -ne 1) {
        throw "Prime-pair double-preservation verification failed"
    }

    $TriangleOutput = Join-Path $TempRoot "pvg-prime-triangle-atlas"
    if (Test-Path $TriangleOutput) {
        Remove-Item -Recurse -Force $TriangleOutput
    }
    Invoke-Python312 -PythonArgs @(
        "tools/pvg_prime_triangle_atlas.py",
        "--limit", "100",
        "--output-dir", $TriangleOutput
    )
    Assert-LastExitCode -FailureMessage "Prime-axis triangle atlas generation failed"

    $TriangleSummaryPath = Join-Path $TriangleOutput "prime-triangle-atlas-primes-le-100-summary.json"
    $TriangleCsvPath = Join-Path $TriangleOutput "prime-triangle-atlas-primes-le-100.csv"
    if (-not (Test-Path $TriangleSummaryPath) -or -not (Test-Path $TriangleCsvPath)) {
        throw "Prime-axis triangle atlas outputs were not created"
    }

    $TriangleGenerated = Get-Content -Raw $TriangleSummaryPath | ConvertFrom-Json
    if ($TriangleGenerated.scope.prime_count -ne 25 -or $TriangleGenerated.scope.unordered_triangle_count -ne 2300) {
        throw "Prime-axis triangle atlas scope verification failed"
    }
    if ($TriangleGenerated.distinguished_triangles.all_three_difference_preserved.Count -ne 1) {
        throw "Prime-axis triangle rigidity verification failed"
    }
    $VerificationFailures = @(
        $TriangleGenerated.verification.PSObject.Properties |
            Where-Object { -not [bool]$_.Value }
    )
    if ($VerificationFailures.Count -ne 0) {
        throw "Prime-axis triangle composition verification failed"
    }
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
