# BENCHMARK-TKG-001 Execution Pass

Status: EXECUTED / STRUCTURAL PASS 12/12 / NOT SEALED

Date: 2026-07-17

## Scope

This execution tested structural routing and governance behavior only. It did not test or certify mathematical theorem proofs.

## Execution method

Direct cloning from GitHub was unavailable because the execution environment could not resolve `github.com`. The current branch versions of the orchestrator, benchmark runner, and benchmark registry were fetched through the GitHub connector, reconstructed exactly in a local Python 3.13.5 execution directory, and run there.

## First execution

```text
passed = false
passed cases = 9/12
```

Failing cases:

```text
COMP-001
DIAG-002
ADV-003
```

The failures exposed three routing defects:

1. `logarithmic-derivative coefficient` did not route to TKG-004 because the hyphenated wording was not recognized.
2. `functional-equation symmetry` did not trigger the RH shortcut blocker because only the space-separated spelling was recognized.
3. `PVG reinterpretation ... new theorem` triggered the blocker but did not route to the governance orchestrator unit.

## Repairs

The orchestrator was repaired to:

- accept both `logarithmic derivative` and `logarithmic-derivative`;
- accept both `functional equation` and `functional-equation`;
- add a governed `discovery_claim` route for reinterpretation-to-new-theorem prompts.

## Final execution

```text
passed = true
passed cases = 12/12
```

Class results:

```text
definitional  2/2
computational 2/2
multi_hop     2/2
diagnostic    2/2
adversarial   3/3
coverage      1/1
```

## Scientific ceiling

```text
MATH = MATH-M0
PNT progress = NONE
PNT-AP progress = NONE
Goldbach progress = NONE
RH progress = NONE
GRH progress = NONE
```

A 12/12 structural pass certifies only that the tested routing expectations and governance invariants were satisfied in this execution.

It does not certify:

- correctness of analytic theorems;
- validity of user-supplied certificates;
- completeness beyond the 12 benchmark prompts;
- mathematical novelty;
- MATH promotion.

## Seal state

```text
BENCHMARK EXECUTED = YES
STRUCTURAL PASS = 12/12
BENCHMARK SEALED = NO
INDEPENDENT SEALING REVIEW = REQUIRED
```
