# Local Governance Gate Runbook

Status: ACTIVE FALLBACK WHILE GITHUB ACTIONS IS PRE-STEP BLOCKED

## Purpose

Run the same project-owned commands used by:

`.github/workflows/governance-required-gate.yml`

on the canonical Windows workstation and preserve a complete local receipt.

This is an execution fallback, not a claim that GitHub Actions passed.

## Preconditions

```powershell
cd D:\PVG-ANT-Central-Mind
git fetch origin
git switch agent/pvg-addition-fibers-theory-001
git pull --ff-only origin agent/pvg-addition-fibers-theory-001
git status --short
```

Required:

```text
branch = agent/pvg-addition-fibers-theory-001
working tree = clean
Python = available
Git = available
```

## Execute

First run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\tools\run_governance_gate_local.ps1 -InstallDependencies
```

Later runs, after dependencies are present:

```powershell
.\tools\run_governance_gate_local.ps1
```

## Generated evidence

The script creates a timestamped directory:

```text
artifacts/local-governance-gate/YYYYMMDD-HHMMSS/
```

containing:

```text
LOCAL-GOVERNANCE-GATE-RECEIPT.md
results.json
one log per command
git-diff.log
```

## Interpretation

A valid local PASS requires:

```text
all project-owned commands = PASS
deterministic git diff = PASS
working tree was clean before execution
branch and HEAD recorded in receipt
```

The script explicitly records:

```text
GitHub Actions replacement claim = NO
merge authorization = NOT_GRANTED_BY_THIS_SCRIPT
```

A local PASS permits `CENTRAL-MIND-PR58-INTEGRATION-AUDIT-004` to distinguish:

1. project-content execution evidence: PASS locally;
2. hosted GitHub Actions execution: infrastructure-blocked;
3. merge authorization: a separate governance decision.

## After execution

Do not edit the receipt. Report:

```text
Result: PASS or FAIL
Receipt path
Branch
HEAD
Failed checks, if any
```

If the result is PASS, commit only the receipt selected for governance evidence, not all transient logs unless the audit explicitly requires them.

## Scientific ceiling

A local gate cannot certify historical novelty, publication readiness, hidden benchmark performance, Goldbach, RH, or GRH progress.
