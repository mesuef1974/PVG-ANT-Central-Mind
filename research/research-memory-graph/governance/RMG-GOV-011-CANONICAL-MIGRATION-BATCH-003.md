# RMG-GOV-011 — Canonical Registry Migration Batch 003

## Scope

This batch migrates two historical RMG registries:

- `prime-distribution-ap-character-chebyshev.jsonl`
- `primitive-characters-conductors-gauss-functional-equation.jsonl`

Total migrated records: `24`.

## Governing rule

Legacy `L3/L4/L5` labels are not inherited mechanically. A record keeps `ASSIM-L3+` only when the canonical semantic fields are substantively populated. Otherwise it is conservatively placed at `ASSIM-L2` or below while preserving the legacy label in `legacy_assimilation_level`.

Finite numerical evidence is separated into `OPS-*` and `CERT-*`; it does not raise `MATH-*`.

## Preserved invariants

- record count preserved;
- every `record_id` preserved;
- claim ceilings preserved or tightened;
- all mathematical-contribution levels remain `MATH-M0`;
- PNT-AP remains a known theorem, not a project theorem;
- zero-free regions remain external analytic certificates;
- exceptional-zero handling remains a boundary;
- GRH progress remains `NONE`;
- Gauss-sum computations do not imply functional equations;
- finite residue-phase encodings do not determine global zero locations.

## Explicit conservative downgrades

Examples include:

- `RMG003B-PNTAP-001`: legacy `L3_BIDIRECTIONALLY_ANALYZED` to `ASSIM-L2` because the translation is a restatement and does not carry the analytic proof mechanism.
- `RMG-003-C-0001`: legacy `L3_BIDIRECTIONALLY_ANALYZED` to `ASSIM-L2` because the finite character/conductor data omit continuation and the functional equation.
- `RMG-003-C-0009`: legacy `L3_BIDIRECTIONALLY_ANALYZED` to `ASSIM-L2` because the root number is a scalar interface, not a complete bidirectional analytic translation.

## Verification

`research/research-memory-graph/code/verify_rmg_gov_011.py` checks:

- exactly 24 records;
- unique identifiers;
- canonical-field completeness;
- no unresolved placeholders;
- no automatic mathematical promotion;
- selected conservative downgrades;
- GRH claim ceiling.

## Honest status

```text
BATCH_003_DATA_MIGRATION = COMPLETE
MIGRATED_RECORDS = 24
CUMULATIVE_MIGRATED_RECORDS = 72
VERIFIER_CODE = COMMITTED
VERIFIER_EXECUTION = NOT_CLAIMED
FULL_HISTORICAL_MIGRATION = NOT_COMPLETE
NEW_PNT_AP_RESULT = NONE
GRH_PROGRESS = NONE
```
