# BENCHMARK-TKG-001 Independent Sealing Review

Status: NOT SEALED
Decision: FAIL SEALING REVIEW / REMEDIATION REQUIRED
Scope: structural benchmark only
MATH status: MATH-M0
Scientific progress: NONE

## Review question

Does the current 12/12 structural execution provide enough evidence to seal BENCHMARK-TKG-001 as a reliable benchmark for the research mind?

## Decision

No.

The benchmark execution is reproducible at the routing/governance layer and the structural verifier passes. However, the current evidence and runner semantics are insufficient for sealing.

## Evidence reviewed

- `registry/benchmark-tkg-001.jsonl`
- `code/query_reasoning_orchestrator_001.py`
- `code/run_benchmark_tkg_001.py`
- `code/verify_benchmark_tkg_001.py`
- `reports/benchmark-tkg-001-execution-report.json`
- `units/BENCHMARK-TKG-001-EXECUTION-PASS.md`

The structural verifier was replayed in Python and returned PASS with 12/12 routing/governance cases.

## Passing findings

1. The registry contains 12 unique cases across six declared classes.
2. The runner preserves `MATH-M0` and all progress fields at `NONE`.
3. The principal blocked-edge cases are detected after the recorded repairs.
4. The unclassified coverage case remains outside the selected TKG units.
5. The verifier correctly states that no mathematical theorem is certified.

## Seal-blocking findings

### SB-01 — Declared semantic expectations are not evaluated

The registry declares fields including:

- `must_include`
- `must_not_claim`
- `expected_facts`
- `expected_path`

The runner does not evaluate these fields. Therefore the current 12/12 result does not test answer content, numerical correctness, explanation quality, or actual multi-hop derivation. It tests only unit selection, selected blockers, claim ceilings, and authorization flags.

This is the primary blocker.

### SB-02 — Evidence integrity is incomplete

The execution report does not bind the result to:

- an exact executed commit SHA;
- cryptographic hashes of the registry, orchestrator, runner, and verifier;
- the raw command line;
- raw stdout/stderr;
- process exit codes;
- a complete machine-readable per-case report in the committed evidence.

The report is a summary, not a complete replay receipt.

### SB-03 — Source reconstruction is weaker than checkout execution

The report states that files were reconstructed after connector fetch because direct GitHub clone was unavailable. This is acceptable for a diagnostic execution, but not sufficient for a final seal unless exact blob SHAs and content hashes are recorded and checked before execution.

### SB-04 — Independence is incomplete

The benchmark designer, repairer, executor, and sealing reviewer are not cleanly separated roles. This review can identify blockers and refuse sealing, but it cannot honestly satisfy a strong independent-review claim by itself.

### SB-05 — Case adequacy is too narrow

Twelve hand-written cases do not adequately test:

- paraphrase robustness;
- Arabic/English equivalence;
- punctuation and hyphen variants beyond the repaired examples;
- false-positive routing;
- ambiguous mixed-intent questions;
- missing-hypothesis prioritization;
- preservation/loss reporting;
- adversarial certificate injection;
- regression against unrelated mathematical vocabulary.

### SB-06 — No mutation or negative-control suite

The benchmark lacks systematic mutations, minimal pairs, and negative controls. A keyword router can therefore pass while remaining brittle.

## Required remediation

1. Build `BENCHMARK-TKG-001-R2` or revise the runner so every declared expectation field is either evaluated or removed from the registry.
2. Separate routing tests from answer-semantic tests.
3. Commit a complete execution manifest containing exact head SHA, blob SHAs, SHA-256 hashes, command, environment, exit codes, stdout/stderr, and full per-case output.
4. Add paraphrase, bilingual, minimal-pair, mutation, and false-positive cases.
5. Add cases that test `required_hypotheses`, `missing_certificates`, PVG translation class, preserved information, and lost information.
6. Require a second-role replay or an independently generated review artifact before sealing.

## Current governed state

```text
BENCHMARK EXECUTED = YES
STRUCTURAL ROUTING PASS = 12/12
STRUCTURAL VERIFIER REPLAY = PASS
SEMANTIC ANSWER BENCHMARK = NOT EXECUTED
EVIDENCE INTEGRITY GATE = FAIL
CASE ADEQUACY GATE = FAIL
INDEPENDENCE GATE = FAIL
BENCHMARK SEALED = NO
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

The 12/12 result is retained as a valid structural routing/governance execution result. It is not revoked, but it is not sufficient for benchmark sealing.

## Next governed action

Build the remediation layer `BENCHMARK-TKG-001-R2` with semantic expectation evaluation and a cryptographically bound execution manifest, then rerun before a new sealing review.
