# BENCHMARK-TKG-001

## Status

`draft_structural / execution_not_claimed / MATH-M0`

## Purpose

This benchmark tests whether `REASONING-ORCHESTRATOR-001` routes questions through the correct TKG units, preserves hypothesis ledgers, detects invalid inference edges, and keeps the scientific claim ceiling conservative.

It does **not** test whether deep analytic theorems have been proved. It does not authorize MATH promotion.

## Scope

The benchmark covers:

1. definitional reasoning;
2. finite computational routing;
3. multi-hop reasoning;
4. diagnostic rejection of invalid shortcuts;
5. adversarial governance prompts;
6. out-of-scope handling.

The initial registry contains 12 cases.

## Case families

### Definitional

- Dirichlet convolution;
- conductor and primitive-source semantics.

### Computational

- `Lambda(27)` and its labelled prime-power PVG point;
- the distinction between multiplicativity and complete multiplicativity through `tau(4) != tau(2)^2`.

### Multi-hop

- Euler product to logarithmic derivative to von Mangoldt coefficients;
- Perron/Mellin/contour/residue prerequisites before an explicit formula.

### Diagnostic

- reject `Euler product => PNT`;
- reject `functional-equation symmetry => RH`.

### Adversarial

- reject verifier-file existence as MATH promotion;
- reject finite Goldbach checks as a universal proof;
- reject PVG reinterpretation alone as a new theorem.

### Coverage

- return an unclassified/out-of-scope route for unrelated material.

## Files

```text
registry/benchmark-tkg-001.jsonl
code/run_benchmark_tkg_001.py
code/verify_benchmark_tkg_001.py
units/BENCHMARK-TKG-001.md
```

## Runner output

The runner reports:

```text
case id
case family
selected units
blocked edges
individual checks
class-level counts
global pass/fail
claim ceiling
```

A global structural pass means only that the encoded routing expectations and governance invariants match the current orchestrator.

## Governance invariants

Every case must retain:

```text
MATH = MATH-M0
PNT = NONE
PNT-AP = NONE
Goldbach = NONE
RH = NONE
GRH = NONE
automatic promotion = false
```

## Important correction discovered during construction

Benchmark construction exposed two weaknesses in the first orchestrator version:

1. weak routing for `tau`, `sigma`, divisor functions, and prime-power coefficient questions;
2. no explicit blocked edge from syntactic verifier completeness to MATH promotion.

The orchestrator was strengthened before the benchmark verifier was added. This is the intended role of a benchmark: expose reasoning gaps rather than merely document existing behavior.

## Execution

Suggested commands:

```bash
python research/translation-knowledge-graph/code/run_benchmark_tkg_001.py
python research/translation-knowledge-graph/code/run_benchmark_tkg_001.py --case-id DIAG-001
python research/translation-knowledge-graph/code/verify_benchmark_tkg_001.py
```

Execution is not claimed from the connector-only environment. A committed verifier file is not itself an execution certificate.

## Claim ceiling

```text
benchmark structure = ASSIM-L3
routing diagnostics = ASSIM-L3
scientific theorem certification = NONE
MATH = MATH-M0
```

## Next governed action

Run the orchestrator and benchmark in an executable checkout, archive the machine-readable report, repair any failing cases, and only then consider a sealed benchmark revision.
