# RMG-GOV-010 — Canonical Registry Migration Batch 002

## Scope

This batch migrates two registry files:

- `additive-characters-exponential-sums-fourier-cancellation.jsonl`
- `circle-method-major-minor-singular-series.jsonl`

Total migrated records: `24`.

## Migration rule

The batch preserves record IDs, statements, claim ceilings, and legacy assimilation labels while replacing ambiguous bare `L*` values with governed namespaces.

Every migrated record now carries:

- ANT standard definition;
- ANT to PVG map;
- PVG geometric object;
- PVG to ANT return map;
- translation type;
- injectivity status;
- kernel or information-loss statement;
- `ASSIM-*`, `MATH-*`, `OPS-*`, and `CERT-*` fields;
- the legacy assimilation value for provenance.

## Honest downgrade rule

A historical `L3`, `L4`, or `L5` label is not automatically copied into `ASSIM-L3+`.

When the seven semantic fields were not previously justified as a complete bidirectional analysis, the canonical level is lowered. In this batch:

- the Lean-status record is set to `ASSIM-L2`;
- the circle-method provenance record is set to `ASSIM-L2`;
- the singular integral remains `ASSIM-L1` because no intrinsic PVG translation is established.

No record receives a mathematical promotion:

`math_contribution_level = MATH-M0` for all 24 records.

## Claim ceilings

The migration preserves the following boundaries:

- finite Fourier identities do not imply analytic cancellation;
- Fourier projectors do not prove Goldbach;
- major arcs do not replace minor-arc control;
- local singular-series data do not prove convergence or positivity;
- PVG reindexing does not generate the Archimedean singular integral;
- no RH/GRH progress is claimed.

## Verification

Verifier:

`research/research-memory-graph/code/verify_rmg_gov_010.py`

The verifier checks record counts, unique IDs, canonical fields, namespace validity, absence of unresolved placeholders, no mathematical promotion, and the two explicit honest downgrades.

## Status

```text
MIGRATED_FILES = 2
MIGRATED_RECORDS = 24
CUMULATIVE_MIGRATED_RECORDS = 48
MATHEMATICAL_PROMOTIONS = 0
HONEST_DOWNGRADES = 2
FULL_HISTORICAL_MIGRATION = NOT_COMPLETE
VERIFIER_CODE = COMMITTED
VERIFIER_EXECUTION = NOT_CLAIMED
```
