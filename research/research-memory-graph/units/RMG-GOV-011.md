# RMG-GOV-011 — Canonical Registry Migration Batch 003

## Decision

`COMPLETE — DATA MIGRATION COMMITTED / VERIFIER EXECUTION NOT CLAIMED`

## Migrated registries

1. `prime-distribution-ap-character-chebyshev.jsonl`
2. `primitive-characters-conductors-gauss-functional-equation.jsonl`

## Record count

```text
batch records = 24
cumulative migrated records = 72
```

## Scientific ceiling

- PNT in arithmetic progressions remains a known theorem.
- Zero-free regions and exceptional-zero analysis remain external ANT inputs.
- Functional equations remain known analytic theorems.
- Finite Gauss-sum verification does not prove analytic continuation.
- No RH or GRH progress is claimed.
- All migrated records remain at `MATH-M0`.

## Governance effect

This batch replaces ambiguous legacy maturity labels with separated `ASSIM`, `MATH`, `OPS`, and `CERT` fields. Legacy labels remain visible for audit. Records lacking complete bidirectional semantic content are conservatively capped at `ASSIM-L2` rather than inheriting legacy `L3+` automatically.

## Verification

Verifier committed:

`research/research-memory-graph/code/verify_rmg_gov_011.py`

Execution status:

`NOT_CLAIMED`

## Next batch

`RMG-GOV-012 — Dirichlet L-zero explicit-formula and sieve registries`.
