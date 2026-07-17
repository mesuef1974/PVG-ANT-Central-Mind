# TKG-AUTHORSHIP-SCAFFOLD-CLEAN-CHECKOUT-REPLAY-001

Status: `PASS — INDEPENDENT CLEAN-CHECKOUT EXECUTION`

Date: 2026-07-17

## Scope

This record closes only the reproducibility claim for the mechanical TKG human-authorship scaffold extractor.

It does not review, classify, or authorize any of the 37 queued records.

## Independently reported execution

The extractor was executed from a clean checkout of:

```text
repository = mesuef1974/PVG-ANT-Central-Mind
branch = agent/pvg-axis-sum-continuation-002
```

The independent execution reported:

```text
exit_code = 0
registry_records = 120
rows = 37
TYPE_AND_CEILING = 12
TYPE_ONLY = 15
CEILING_ONLY = 10
```

All nonblank lines in the fifteen TKG registry JSONL files parsed successfully after the recorded TKG-004 structural repair.

## Comparison against the previously generated scaffold

The independently generated output was compared with the existing out-of-repository scaffold.

Reported result:

```text
membership match = PASS
missingness-category match = PASS
queue-order match, row by row = PASS
human-judgement columns blank, 37/37 = PASS
review_status = UNREVIEWED, 37/37 = PASS
```

Thus the complete queue-order contract was reproduced from repository data alone:

1. parse every physical JSONL record;
2. block malformed records;
3. select records missing direct type and/or direct governance signal;
4. sort by `source_path ASC`, then `source_line ASC`;
5. apply `random.Random(2026071701).shuffle`;
6. assign queue identifiers.

## Exact claim established

```text
EXTRACTOR CLEAN-CHECKOUT REPLAY = PASS
SCAFFOLD MEMBERSHIP REPRODUCIBLE = YES
MISSINGNESS CLASSIFICATION REPRODUCIBLE = YES
QUEUE ORDER REPRODUCIBLE = YES
```

This is a narrow mechanical reproducibility result.

## Claims not established

This replay does not establish:

- correctness of any future human classification;
- correctness of any future authored claim ceiling;
- policy transfer from the Family-B-only TKG pilot to the 165-record RMG queue;
- executable knowledge;
- reasoning or generalization;
- mathematical progress.

## Current boundary

```text
HUMAN REVIEW = NOT STARTED
EXECUTABLE_RULE DOUBLE-DELETION GATE = OPEN
RMG OPERATIONAL AUTHORITY = NOT GRANTED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
```
