[CmdletBinding()]
param(
    [switch]$InstallDependencies,
    [string]$ExpectedBranch = "agent/pvg-addition-fibers-theory-001",
    [string]$OutputRoot = "artifacts/local-governance-gate"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Write-Section([string]$Title) {
    Write-Host ""
    Write-Host ("=" * 78) -ForegroundColor DarkCyan
    Write-Host $Title -ForegroundColor Cyan
    Write-Host ("=" * 78) -ForegroundColor DarkCyan
}

function Invoke-GateCommand {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][string[]]$Command
    )

    $safeName = ($Name -replace '[^A-Za-z0-9_.-]', '_')
    $logPath = Join-Path $script:RunDirectory ("{0}.log" -f $safeName)
    $started = Get-Date

    Write-Host ("[RUN ] {0}" -f $Name) -ForegroundColor Yellow
    $rendered = ($Command -join ' ')
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- RUN  `{0}`: `{1}`" -f $Name, $rendered)

    try {
        $output = & $Command[0] $Command[1..($Command.Count - 1)] 2>&1
        $exitCode = $LASTEXITCODE
        $output | Tee-Object -FilePath $logPath | ForEach-Object { Write-Host $_ }
    }
    catch {
        $_ | Out-String | Set-Content -LiteralPath $logPath -Encoding UTF8
        $exitCode = 1
        Write-Host $_ -ForegroundColor Red
    }

    $elapsed = [math]::Round(((Get-Date) - $started).TotalSeconds, 2)
    $status = if ($exitCode -eq 0) { "PASS" } else { "FAIL" }
    $color = if ($exitCode -eq 0) { "Green" } else { "Red" }
    Write-Host ("[{0}] {1} ({2}s)" -f $status, $Name, $elapsed) -ForegroundColor $color

    $script:Results += [pscustomobject]@{
        Name = $Name
        Status = $status
        ExitCode = $exitCode
        Seconds = $elapsed
        Log = $logPath
        Command = $rendered
    }

    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - status: **{0}**" -f $status)
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - exit_code: `{0}`" -f $exitCode)
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - seconds: `{0}`" -f $elapsed)
    Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("  - log: `{0}`" -f $logPath)

    return $exitCode
}

Write-Section "PVG-ANT Local Governance Gate"

$repoRoot = (git rev-parse --show-toplevel 2>$null)
if (-not $repoRoot) {
    throw "Run this script from inside the PVG-ANT-Central-Mind Git repository."
}
Set-Location $repoRoot

$branch = (git branch --show-current).Trim()
$head = (git rev-parse HEAD).Trim()
$pythonVersion = (& python --version 2>&1 | Out-String).Trim()
$gitVersion = (& git --version 2>&1 | Out-String).Trim()

if ($branch -ne $ExpectedBranch) {
    throw "Wrong branch. Expected '$ExpectedBranch' but found '$branch'."
}

$initialStatus = git status --porcelain
if ($initialStatus) {
    throw "Working tree is not clean before the audit. Commit or stash changes first.`n$initialStatus"
}

if (Test-Path "formal/lean/audit/LeanP3Pass009Discovery.lean") {
    throw "LeanP3Pass009Discovery.lean is not authorized by the current closure."
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$script:RunDirectory = Join-Path $OutputRoot $timestamp
New-Item -ItemType Directory -Force -Path $script:RunDirectory | Out-Null
$script:SummaryPath = Join-Path $script:RunDirectory "LOCAL-GOVERNANCE-GATE-RECEIPT.md"
$script:Results = @()

@"
# Local Governance Gate Receipt

- timestamp: $(Get-Date -Format o)
- repository: `$repoRoot`
- branch: `$branch`
- head: `$head`
- python: `$pythonVersion`
- git: `$gitVersion`
- execution_class: `local_equivalent_of_governance-required-gate`
- GitHub Actions replacement claim: `NO`

This receipt records an actual local execution of the same project-owned commands used by
`.github/workflows/governance-required-gate.yml`. It does not claim that GitHub Actions ran.

## Commands
"@ | Set-Content -LiteralPath $script:SummaryPath -Encoding UTF8

if ($InstallDependencies) {
    Write-Section "Install symbolic dependencies"
    & python -m pip install sympy mpmath
    if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
}
else {
    & python -c "import sympy, mpmath; print('symbolic dependencies: present')"
    if ($LASTEXITCODE -ne 0) {
        throw "sympy/mpmath are missing. Re-run with -InstallDependencies."
    }
}

$commands = @(
    @{ Name = "honesty_audit"; Command = @("python", "tools/honesty_audit.py") },
    @{ Name = "registry_sync_audit"; Command = @("python", "tools/registry_sync_audit.py") },
    @{ Name = "no_pdf_audit"; Command = @("python", "tools/no_pdf_audit.py") },
    @{ Name = "forbidden_promotion_audit"; Command = @("python", "tools/forbidden_promotion_audit.py") },
    @{ Name = "duplicate_concept_audit"; Command = @("python", "tools/duplicate_concept_audit.py") },
    @{ Name = "citation_audit"; Command = @("python", "tools/citation_audit.py") },
    @{ Name = "state_coherence_audit"; Command = @("python", "tools/state_coherence_audit.py") },
    @{ Name = "research_compass_audit"; Command = @("python", "tools/research_compass_audit.py") },
    @{ Name = "legacy_assets_audit"; Command = @("python", "tools/legacy_assets_audit.py") },
    @{ Name = "central_mind_continuity_audit"; Command = @("python", "tools/central_mind_continuity_audit.py") },
    @{ Name = "p8_deadline_audit"; Command = @("python", "tools/p8_deadline_audit.py") },

    @{ Name = "language_kernel_regenerate"; Command = @("python", "tools/pvg_ant_kernel_examples.py") },
    @{ Name = "language_kernel_audit"; Command = @("python", "tools/language_kernel_audit.py") },

    @{ Name = "translation_v2_pass001_regenerate"; Command = @("python", "tools/pvg_ant_translation_v2_examples.py") },
    @{ Name = "translation_v2_pass001_audit"; Command = @("python", "tools/translation_kernel_v2_audit.py") },
    @{ Name = "translation_v2_pass002_regenerate"; Command = @("python", "tools/translation_kernel_v2_pass002_examples.py") },
    @{ Name = "translation_v2_pass002_audit"; Command = @("python", "tools/translation_kernel_v2_pass002_audit.py") },

    @{ Name = "benchmark001_regenerate"; Command = @("python", "tools/pvg_ant_benchmark_001.py") },
    @{ Name = "benchmark001_pass002_rescore"; Command = @("python", "tools/pvg_ant_benchmark_001_pass002_rescore.py") },

    @{ Name = "pvg_core_ontology_regenerate"; Command = @("python", "tools/pvg_core_ontology_examples.py") },
    @{ Name = "pvg_core_ontology_audit"; Command = @("python", "tools/pvg_core_ontology_audit.py") },

    @{ Name = "original_lemma_candidate_checks"; Command = @("python", "tools/original_lemma_candidate_checks.py") },
    @{ Name = "original_lemma_selection_audit"; Command = @("python", "tools/original_lemma_selection_audit.py") },

    @{ Name = "one_theorem_symbolic_audit"; Command = @("python", "tools/one_theorem_symbolic_audit.py") },
    @{ Name = "one_theorem_phase_audit"; Command = @("python", "tools/one_theorem_phase_audit.py") },
    @{ Name = "one_theorem_p7_audit"; Command = @("python", "tools/one_theorem_p7_audit.py") },
    @{ Name = "one_theorem_p8_audit"; Command = @("python", "tools/one_theorem_p8_audit.py") },
    @{ Name = "one_theorem_external_validation_audit"; Command = @("python", "tools/one_theorem_external_validation_audit.py") }
)

Write-Section "Run project-owned governance commands"
foreach ($item in $commands) {
    [void](Invoke-GateCommand -Name $item.Name -Command $item.Command)
}

Write-Section "Verify deterministic repository state"
$diffLog = Join-Path $script:RunDirectory "git-diff.log"
$diffOutput = git diff -- . ':!artifacts/local-governance-gate' 2>&1
$diffExit = $LASTEXITCODE
$diffOutput | Set-Content -LiteralPath $diffLog -Encoding UTF8
if ($diffOutput) {
    $script:Results += [pscustomobject]@{
        Name = "deterministic_git_diff"
        Status = "FAIL"
        ExitCode = 1
        Seconds = 0
        Log = $diffLog
        Command = "git diff -- . ':!artifacts/local-governance-gate'"
    }
}
else {
    $script:Results += [pscustomobject]@{
        Name = "deterministic_git_diff"
        Status = "PASS"
        ExitCode = 0
        Seconds = 0
        Log = $diffLog
        Command = "git diff -- . ':!artifacts/local-governance-gate'"
    }
}

$failed = @($script:Results | Where-Object { $_.Status -ne "PASS" })
$passed = @($script:Results | Where-Object { $_.Status -eq "PASS" })
$overall = if ($failed.Count -eq 0) { "PASS" } else { "FAIL" }

Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ""
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value "## Final result"
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ""
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- passed: `{0}`" -f $passed.Count)
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- failed: `{0}`" -f $failed.Count)
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value ("- result: **{0}**" -f $overall)
Add-Content -LiteralPath $script:SummaryPath -Encoding UTF8 -Value "- merge_authorization: `NOT_GRANTED_BY_THIS_SCRIPT`"

$script:Results | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $script:RunDirectory "results.json") -Encoding UTF8

Write-Section "Final result"
Write-Host ("Passed: {0}" -f $passed.Count) -ForegroundColor Green
Write-Host ("Failed: {0}" -f $failed.Count) -ForegroundColor $(if ($failed.Count -eq 0) { "Green" } else { "Red" })
Write-Host ("Receipt: {0}" -f $script:SummaryPath) -ForegroundColor Cyan
Write-Host ("Result: {0}" -f $overall) -ForegroundColor $(if ($overall -eq "PASS") { "Green" } else { "Red" })

if ($failed.Count -gt 0) {
    Write-Host "Failed checks:" -ForegroundColor Red
    $failed | ForEach-Object { Write-Host (" - {0} (exit {1})" -f $_.Name, $_.ExitCode) -ForegroundColor Red }
    exit 1
}

exit 0
