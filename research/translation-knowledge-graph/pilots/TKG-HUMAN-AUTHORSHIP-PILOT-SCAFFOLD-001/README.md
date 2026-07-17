# TKG-HUMAN-AUTHORSHIP-PILOT-SCAFFOLD-001

Status: `EXTRACTOR_COMMITTED / ROWS_OUTSIDE_REPOSITORY / UNREVIEWED`

Registry snapshot commit: `9c69f1d7672cc378694d2e594b470c9e0583c894`
Branch: `agent/pvg-axis-sum-continuation-002`

Committed extractor:

`research/translation-knowledge-graph/code/extract_tkg_human_authorship_pilot_scaffold_001.py`

## Reproducible ordering contract

The queue order is defined by the following complete procedure:

1. read `TKG-001` through `TKG-015` JSONL records;
2. select records missing direct type and/or direct governance signal;
3. sort candidates by `source_path ASC`, then `source_line ASC`;
4. apply `Python random.Random(2026071701).shuffle`;
5. assign `TKG-PILOT-001` onward in shuffled order.

The seed alone is not treated as sufficient. The canonical pre-shuffle input order is part of the contract.

Distribution:

- `TYPE_AND_CEILING`: 12
- `TYPE_ONLY`: 15
- `CEILING_ONLY`: 10
- total: 37

The generated `scaffold.csv` and `scaffold.jsonl` are not currently committed. They remain outside the repository until separately authorized and committed. The repository currently contains the extractor, this README, and the manifest only.

All human-judgement columns are blank by design. No type, ceiling, reasoning capability, or mathematical result is inferred.

Scientific ceiling: `MATH-M0`.

## Sample-coverage constraint

```text
PILOT SAMPLE FAMILY COVERAGE = FAMILY-B ONLY (37/37)
FAMILY-A EXERCISE = NONE (64/64 complete, no work)
POLICY TRANSFER TO RMG 165 = NOT ESTABLISHED BY THIS PILOT
```

The 37 queued records all come from `TKG-009` through `TKG-015`. This is a consequence of measured missingness, not a balanced family sample.

A successful review can validate the extraction and human-review workflow for this Family-B-shaped corpus only. It cannot establish transfer validity across RMG's 49 observed classes, its 66 untyped records, or its 99 typed mathematical records lacking governance axes.

## Claim boundary

This scaffold measures data incompleteness and organizes human review. It does not establish reasoning, generalization, executable knowledge, PNT progress, Goldbach progress, RH progress, or GRH progress.
