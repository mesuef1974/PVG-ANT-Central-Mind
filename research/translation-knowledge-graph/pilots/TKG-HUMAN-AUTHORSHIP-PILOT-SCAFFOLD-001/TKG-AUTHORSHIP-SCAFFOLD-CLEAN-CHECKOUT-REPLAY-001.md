# TKG-AUTHORSHIP-SCAFFOLD-CLEAN-CHECKOUT-REPLAY-001

Status: `PASS — CLEAN-CHECKOUT REPLAY WITH QUALIFIED INDEPENDENCE`

Date: 2026-07-17

## Scope

This record closes only the reproducibility claim for the mechanical TKG human-authorship scaffold extractor.

It does not review, classify, or authorize any of the 37 queued records.

## Executed tree

The extractor was executed from a clean checkout pinned to:

```text
repository = mesuef1974/PVG-ANT-Central-Mind
branch_at_execution = agent/pvg-axis-sum-continuation-002
replayed_tree_commit = 9b6fc51990c34c85d688087a02fc539185cdd5d0
```

The branch name is contextual only. The immutable replay target is the commit SHA above.

## Execution result

The clean-checkout execution reported:

```text
exit_code = 0
registry_records = 120
rows = 37
TYPE_AND_CEILING = 12
TYPE_ONLY = 15
CEILING_ONLY = 10
human-judgement columns blank = 37/37
review_status = UNREVIEWED, 37/37
```

All nonblank lines in the fifteen TKG registry JSONL files parsed successfully after the recorded TKG-004 structural repair.

This evidence record does not contain the R2-level byte-exact package: it does not record environment details, stdout/stderr files, per-file SHA-256 values, or Git blob identifiers. Therefore it establishes only the claims explicitly separated below.

## Independence and determinism classification

The verification used two distinct forms of checking, which must not be conflated.

### Membership

```text
MEMBERSHIP = INDEPENDENTLY RE-DERIVED
implementation relation = DIFFERENT IMPLEMENTATION
result = PASS
```

The 37-record membership was re-derived from the registry by separate logic and matched the extractor output.

### Missingness classification

```text
CLASSIFICATION = INDEPENDENTLY RE-DERIVED
implementation relation = DIFFERENT IMPLEMENTATION
result = PASS
```

The `TYPE_AND_CEILING` / `TYPE_ONLY` / `CEILING_ONLY` categories were re-derived by separate logic and matched for all 37 records.

### Queue order

```text
QUEUE ORDER = DETERMINISM CONFIRMED
implementation relation = SAME COMMITTED EXTRACTOR, TWO RUNS
row-by-row match = PASS
```

This proves that the committed extractor deterministically reproduces its queue order from the pinned tree under the recorded procedure. It is not an independent validation that the chosen sort-and-shuffle policy is correct.

The reproduced order contract is:

1. parse every physical JSONL record;
2. block malformed records;
3. select records missing direct type and/or direct governance signal;
4. sort by `source_path ASC`, then `source_line ASC`;
5. apply `random.Random(2026071701).shuffle`;
6. assign queue identifiers.

## Independence-of-party boundary

The execution was performed by an agent within the user's working session and environment. It was not performed by an external laboratory, separate organization, or governance-independent reviewer.

Therefore:

```text
EXECUTION INDEPENDENCE = SEPARATE CLEAN-CHECKOUT RUN
IMPLEMENTATION INDEPENDENCE FOR MEMBERSHIP/CLASSIFICATION = YES
PARTY / INSTITUTIONAL INDEPENDENCE = NO
```

## Exact claims established

```text
EXTRACTOR CLEAN-CHECKOUT REPLAY AT 9b6fc51 = PASS
SCAFFOLD MEMBERSHIP INDEPENDENTLY RE-DERIVED = PASS
MISSINGNESS CLASSIFICATION INDEPENDENTLY RE-DERIVED = PASS
QUEUE ORDER DETERMINISM = PASS
```

These are narrow mechanical claims.

## Claims not established

This replay does not establish:

- independent correctness of the queue-order policy;
- correctness of any future human classification;
- correctness of any future authored claim ceiling;
- policy transfer from the Family-B-only TKG pilot to the 165-record RMG queue;
- party-level or institutional independence;
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