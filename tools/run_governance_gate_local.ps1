[CmdletBinding()]
param(
    [switch]$InstallDependencies,
    [string]$ExpectedBranch = "agent/pvg-addition-fibers-theory-001",
    [string]$OutputRoot = "artifacts/local-governance-gate",
    [string]$PythonExe = ""
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Write-Section {
    param([string]$Title)
    Write-Host ""
    Write-Host ("=" * 78) -ForegroundColor DarkCyan
    Write-Host $Title -ForegroundColor Cyan
    Write-Host ("=" * 78) -ForegroundColor DarkCyan
}

function Test-PythonCandidate {
    param([string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) { return $false }
    if ($Path -like "*\Microsoft\WindowsApps\*") { return $false }
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $false }

    $item = Get-Item -LiteralPath $Path -ErrorAction SilentlyContinue
    if ($null -eq $item) { return $false }
    if ($item.Length -eq 0) { return $false }

    try {
        $null = & $Path -c "import sys" 2>&1
    }
    catch {
        return $false
    }

    return ($LASTEXITCODE -eq 0)
}

function Resolve-PythonExe {
    param([string]$Requested)

    if (-not [string]::IsNullOrWhiteSpace($Requested)) {
        if (Test-PythonCandidate -Path $Requested) { return $Requested }
        throw ("The interpreter passed via -PythonExe is not usable: {0}" -f $Requested)
    }

    $candidates = New-Object System.Collections.Generic.List[string]

    foreach ($name in @("python.exe", "python3.exe")) {
        $found = Get-Command $name -All -ErrorAction SilentlyContinue
        foreach ($entry in $found) {
            if ($entry.Source) { $candidates.Add($entry.Source) }
        }
    }

    $launcher = Get-Command "py.exe" -ErrorAction SilentlyContinue
    if ($launcher) {
        try {
            $listed = & $launcher.Source -0p 2>&1
            foreach ($line in $listed) {
                $text = [string]$line
                if ($text -match "([A-Za-z]:\\[^\r\n]*python\.exe)") {
                    $candidates.Add($matches[1])
                }
            }
        }
        catch {
            # The launcher is optional; ignore inventory failures.
        }
    }

    foreach ($fallback in @(
        "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
        "C:\Python313\python.exe",
        "C:\Python312\python.exe",
        "C:\Python311\python.exe"
    )) {
        $candidates.Add($fallback)
    }

    foreach ($candidate in $candidates) {
        if (Test-PythonCandidate -Path $candidate) { return $candidate }
    }

    throw "No usable Python interpreter was found. The 'python' entries under Microsoft\WindowsApps are Store aliases (0 bytes) and are skipped on purpose. Install Python from python.org, or re-run with -PythonExe <full path to python.exe>."
}

function Invoke-GateCommand {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][string[]]$Command
    )

    $safeName = ($Name -replace '[^A-Za-z0-9_.-]', '_')
    $logPath = Join-Path $script:RunDirectory ("{0}.log" -f $safeName)
    $started = Get-Date
    $exe = $Command[0]
    $argsList = @()
    if ($Command.Count -gt 1) {
        $argsList = $Command[1..($Command.Count - 1)]
    }
    $rendered = $Command -join ' '

    Write-Host ("[RUN ] {0}" -f $Name) -ForegroundColor Yellow
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- RUN {0}: {1}" -f $Name, $rendered)

    try {
        $output = & $exe @argsList 2>&1
        $exitCode = $LASTEXITCODE
        if ($null -eq $exitCode) { $exitCode = 0 }
        $output | Tee-Object -FilePath $logPath | ForEach-Object { Write-Host $_ }
    }
    catch {
        ($_ | Out-String) | Set-Content -LiteralPath $logPath -Encoding UTF8
        $exitCode = 1
        Write-Host ($_ | Out-String) -ForegroundColor Red
    }

    $elapsed = [math]::Round(((Get-Date) - $started).TotalSeconds, 2)
    if ($exitCode -eq 0) {
        $status = "PASS"
        $color = "Green"
    }
    else {
        $status = "FAIL"
        $color = "Red"
    }

    Write-Host ("[{0}] {1} ({2} sec)" -f $status, $Name, $elapsed) -ForegroundColor $color

    $script:Results += [pscustomobject]@{
        Name = $Name
        Status = $status
        ExitCode = $exitCode
        Seconds = $elapsed
        Log = $logPath
        Command = $rendered
    }

    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - status: {0}" -f $status)
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - exit_code: {0}" -f $exitCode)
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - seconds: {0}" -f $elapsed)
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - log: {0}" -f $logPath)

    return $exitCode
}

Write-Section "PVG-ANT Local Governance Gate"

$repoRoot = (git rev-parse --show-toplevel 2>$null)
if (-not $repoRoot) {
    throw "Run this script from inside the PVG-ANT-Central-Mind Git repository."
}
$repoRoot = $repoRoot.Trim()
Set-Location $repoRoot

$branch = (git branch --show-current).Trim()
$head = (git rev-parse HEAD).Trim()

$script:PythonExe = Resolve-PythonExe -Requested $PythonExe
$pythonVersion = (& $script:PythonExe --version 2>&1 | Out-String).Trim()
$gitVersion = (& git --version 2>&1 | Out-String).Trim()
Write-Host ("Python interpreter: {0}" -f $script:PythonExe) -ForegroundColor Cyan
Write-Host ("Python version: {0}" -f $pythonVersion) -ForegroundColor Cyan

if ($branch -ne $ExpectedBranch) {
    throw ("Wrong branch. Expected '{0}' but found '{1}'." -f $ExpectedBranch, $branch)
}

$initialStatus = git status --porcelain
if ($initialStatus) {
    throw ("Working tree is not clean before the audit. Commit or stash changes first.`n{0}" -f ($initialStatus -join "`n"))
}

if (Test-Path "formal/lean/audit/LeanP3Pass009Discovery.lean") {
    throw "LeanP3Pass009Discovery.lean is not authorized by the current closure."
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$script:RunDirectory = Join-Path $OutputRoot $timestamp
New-Item -ItemType Directory -Force -Path $script:RunDirectory | Out-Null
$script:SummaryPath = Join-Path $script:RunDirectory "LOCAL-GOVERNANCE-GATE-RECEIPT.md"
$script:Results = @()

$header = @(
    "# Local Governance Gate Receipt",
    "",
    ("- timestamp: {0}" -f (Get-Date -Format o)),
    ("- repository: {0}" -f $repoRoot),
    ("- branch: {0}" -f $branch),
    ("- head: {0}" -f $head),
    ("- python: {0}" -f $pythonVersion),
    ("- python_executable: {0}" -f $script:PythonExe),
    ("- git: {0}" -f $gitVersion),
    "- execution_class: local_equivalent_of_governance-required-gate",
    "- GitHub Actions replacement claim: NO",
    "",
    "This receipt records an actual local execution of the same project-owned commands used by",
    ".github/workflows/governance-required-gate.yml. It does not claim that GitHub Actions ran.",
    "",
    "## Commands"
)
$header | Set-Content -LiteralPath $script:SummaryPath -Encoding UTF8

if ($InstallDependencies) {
    Write-Section "Install symbolic dependencies"
    & $script:PythonExe -m pip install sympy mpmath
    if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
}
else {
    & $script:PythonExe -c "import sympy, mpmath; print('symbolic dependencies: present')"
    if ($LASTEXITCODE -ne 0) {
        throw "sympy/mpmath are missing. Re-run with -InstallDependencies."
    }
}

$commands = @(
    @{ Name = "honesty_audit"; Command = @($script:PythonExe, "tools/honesty_audit.py") },
    @{ Name = "registry_sync_audit"; Command = @($script:PythonExe, "tools/registry_sync_audit.py") },
    @{ Name = "no_pdf_audit"; Command = @($script:PythonExe, "tools/no_pdf_audit.py") },
    @{ Name = "forbidden_promotion_audit"; Command = @($script:PythonExe, "tools/forbidden_promotion_audit.py") },
    @{ Name = "duplicate_concept_audit"; Command = @($script:PythonExe, "tools/duplicate_concept_audit.py") },
    @{ Name = "citation_audit"; Command = @($script:PythonExe, "tools/citation_audit.py") },
    @{ Name = "state_coherence_audit"; Command = @($script:PythonExe, "tools/state_coherence_audit.py") },
    @{ Name = "research_compass_audit"; Command = @($script:PythonExe, "tools/research_compass_audit.py") },
    @{ Name = "legacy_assets_audit"; Command = @($script:PythonExe, "tools/legacy_assets_audit.py") },
    @{ Name = "central_mind_continuity_audit"; Command = @($script:PythonExe, "tools/central_mind_continuity_audit.py") },
    @{ Name = "p8_deadline_audit"; Command = @($script:PythonExe, "tools/p8_deadline_audit.py") },
    @{ Name = "language_kernel_regenerate"; Command = @($script:PythonExe, "tools/pvg_ant_kernel_examples.py") },
    @{ Name = "language_kernel_audit"; Command = @($script:PythonExe, "tools/language_kernel_audit.py") },
    @{ Name = "translation_v2_pass001_regenerate"; Command = @($script:PythonExe, "tools/pvg_ant_translation_v2_examples.py") },
    @{ Name = "translation_v2_pass001_audit"; Command = @($script:PythonExe, "tools/translation_kernel_v2_audit.py") },
    @{ Name = "translation_v2_pass002_regenerate"; Command = @($script:PythonExe, "tools/translation_kernel_v2_pass002_examples.py") },
    @{ Name = "translation_v2_pass002_audit"; Command = @($script:PythonExe, "tools/translation_kernel_v2_pass002_audit.py") },
    @{ Name = "benchmark001_regenerate"; Command = @($script:PythonExe, "tools/pvg_ant_benchmark_001.py") },
    @{ Name = "benchmark001_pass002_rescore"; Command = @($script:PythonExe, "tools/pvg_ant_benchmark_001_pass002_rescore.py") },
    @{ Name = "pvg_core_ontology_regenerate"; Command = @($script:PythonExe, "tools/pvg_core_ontology_examples.py") },
    @{ Name = "pvg_core_ontology_audit"; Command = @($script:PythonExe, "tools/pvg_core_ontology_audit.py") },
    @{ Name = "original_lemma_candidate_checks"; Command = @($script:PythonExe, "tools/original_lemma_candidate_checks.py") },
    @{ Name = "original_lemma_selection_audit"; Command = @($script:PythonExe, "tools/original_lemma_selection_audit.py") },
    @{ Name = "one_theorem_symbolic_audit"; Command = @($script:PythonExe, "tools/one_theorem_symbolic_audit.py") },
    @{ Name = "one_theorem_phase_audit"; Command = @($script:PythonExe, "tools/one_theorem_phase_audit.py") },
    @{ Name = "one_theorem_p7_audit"; Command = @($script:PythonExe, "tools/one_theorem_p7_audit.py") },
    @{ Name = "one_theorem_p8_audit"; Command = @($script:PythonExe, "tools/one_theorem_p8_audit.py") },
    @{ Name = "one_theorem_external_validation_audit"; Command = @($script:PythonExe, "tools/one_theorem_external_validation_audit.py") }
)

Write-Section "Run project-owned governance commands"
foreach ($item in $commands) {
    [void](Invoke-GateCommand -Name $item.Name -Command $item.Command)
}

Write-Section "Verify deterministic repository state"
$diffLog = Join-Path $script:RunDirectory "git-diff.log"
$diffOutput = git diff -- . ':!artifacts/local-governance-gate' 2>&1
$diffOutput | Set-Content -LiteralPath $diffLog -Encoding UTF8
if ($diffOutput) {
    $script:Results += [pscustomobject]@{ Name = "deterministic_git_diff"; Status = "FAIL"; ExitCode = 1; Seconds = 0; Log = $diffLog; Command = "git diff" }
}
else {
    $script:Results += [pscustomobject]@{ Name = "deterministic_git_diff"; Status = "PASS"; ExitCode = 0; Seconds = 0; Log = $diffLog; Command = "git diff" }
}

$failed = @($script:Results | Where-Object { $_.Status -ne "PASS" })
$passed = @($script:Results | Where-Object { $_.Status -eq "PASS" })
if ($failed.Count -eq 0) {
    $overall = "PASS"
    $finalColor = "Green"
}
else {
    $overall = "FAIL"
    $finalColor = "Red"
}

Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ""
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value "## Final result"
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ""
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- passed: {0}" -f $passed.Count)
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- failed: {0}" -f $failed.Count)
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- result: {0}" -f $overall)
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value "- merge_authorization: NOT_GRANTED_BY_THIS_SCRIPT"

$script:Results | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $script:RunDirectory "results.json") -Encoding UTF8

Write-Section "Final result"
Write-Host ("Passed: {0}" -f $passed.Count) -ForegroundColor Green
Write-Host ("Failed: {0}" -f $failed.Count) -ForegroundColor $finalColor
Write-Host ("Receipt: {0}" -f $script:SummaryPath) -ForegroundColor Cyan
Write-Host ("Result: {0}" -f $overall) -ForegroundColor $finalColor

if ($failed.Count -gt 0) {
    Write-Host "Failed checks:" -ForegroundColor Red
    $failed | ForEach-Object { Write-Host (" - {0} (exit {1})" -f $_.Name, $_.ExitCode) -ForegroundColor Red }
    exit 1
}

exit 0
