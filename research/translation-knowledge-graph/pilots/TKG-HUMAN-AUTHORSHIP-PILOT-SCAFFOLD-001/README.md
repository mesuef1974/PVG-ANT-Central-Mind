# TKG-HUMAN-AUTHORSHIP-PILOT-SCAFFOLD-001

Status: `EXTRACTOR_COMMITTED / ROWS_OUTSIDE_REPOSITORY / UNREVIEWED`

Registry snapshot commit: `01a91c1ab39ea4a1e6cc452ff137fae1dfe4234b`
Extractor commit: `89b1278442b04c9c504479717399b8c6201402c0`
Branch: `agent/pvg-axis-sum-continuation-002`

## Reproducible ordering contract

1. read `TKG-001` through `TKG-015` JSONL records;
2. reject any invalid line as `UNPARSEABLE / NEEDS_REPAIR`;
3. select parseable records missing direct type and/or direct governance signal;
4. sort candidates by `source_path ASC`, then `source_line ASC`;
5. apply `Python random.Random(2026071701).shuffle`;
6. assign `TKG-PILOT-001` onward.

The seed alone is not sufficient. The parse gate and canonical pre-shuffle order are part of the contract.

Corrected corpus and queue:

```text
TKG registry records       120
TYPE_AND_CEILING            12
TYPE_ONLY                   15
CEILING_ONLY                10
pilot rows                  37
axis-complete records       83
```

The generated `scaffold.csv` and `scaffold.jsonl` are not currently committed. All human-judgement columns remain blank. No type, ceiling, reasoning capability, or mathematical result is inferred.

Scientific ceiling: `MATH-M0`.

## Source-integrity correction

Two Family-A records in TKG-004 required structural JSONL repair before extraction:

- `TKG004-IDENTITY-ZETA-LAMBDA`;
- `TKG004-NODE-GENERALIZED-MANGOLDT`.

Both are type-and-governance complete after repair and do not enter the 37-row authorship queue. The repair is recorded in `TKG-004-JSONL-STRUCTURAL-REPAIR-001.md`.

## Sample-coverage constraint

```text
PILOT SAMPLE FAMILY COVERAGE = FAMILY-B ONLY (37/37)
FAMILY-A HUMAN-AUTHORSHIP EXERCISE = NONE
FAMILY-A SOURCE-INTEGRITY REPAIR = 2 RECORDS
POLICY TRANSFER TO RMG 165 = NOT ESTABLISHED BY THIS PILOT
```

Family A contains 66 records after the parse correction; all 66 are complete on the measured type-and-governance axes, but two required source-integrity repair. Family B contains 54 records, of which 17 are complete and 37 enter this pilot.

A successful review can validate the extraction and human-review workflow for this Family-B-shaped corpus only. It cannot establish transfer validity across RMG's 49 observed classes, its 66 untyped records, or its 99 typed mathematical records lacking governance axes.

## Claim boundary

This scaffold measures data incompleteness and organizes human review. It does not establish reasoning, generalization, executable knowledge, PNT progress, Goldbach progress, RH progress, or GRH progress.
