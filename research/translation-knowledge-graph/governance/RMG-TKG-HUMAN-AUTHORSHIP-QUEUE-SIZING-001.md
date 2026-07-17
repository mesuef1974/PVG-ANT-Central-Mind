# RMG-TKG-HUMAN-AUTHORSHIP-QUEUE-SIZING-001

Status: COMPLETED READ-ONLY QUEUE-SIZING DECISION — CORRECTED AFTER TKG-004 PARSE REPAIR

Date: 2026-07-17

## Correction

The earlier 118-record TKG count silently omitted two malformed JSONL records in TKG-004. The source-integrity repair is recorded in `TKG-004-JSONL-STRUCTURAL-REPAIR-001.md`.

Corrected TKG corpus size: 120 records.

The two repaired records are Family-A records complete on the measured type-and-governance axes. Therefore the 37-record human-authorship queue is unchanged, but the complete-record count changes from 81 to 83.

## TKG queue

```text
needs type and claim ceiling     12
needs type only                  15
needs claim ceiling only         10
complete on both axes            83
                                 ---
total                           120
```

The 12 records missing both type and ceiling are contained inside the 27 untyped records and are counted once.

```text
TKG HUMAN-AUTHORSHIP QUEUE = 37 / 120
TKG COMPLETE ON TYPE+CEILING = 83 / 120 ≈ 69%
TKG SOURCE-INTEGRITY REPAIR = 2 RECORDS
```

## Family composition

```text
Family A records                         66
Family A human-authorship rows            0
Family A source-integrity repairs          2
Family A complete after repair            66

Family B records                         54
Family B complete                         17
Family B human-authorship rows             37
```

Thus the pilot remains Family-B-only, but the prior statement `64/64 complete, no work` is withdrawn. Family A required two structural repairs even though it contributes no human-authorship rows.

## RMG queue

```text
untyped and missing MATH/OPS/CERT              66
mathematical-content records missing axes       99
structural records requiring applicability      15
                                                 ---
records requiring authored classification       165
separate applicability judgments                 15
```

```text
RMG HUMAN-AUTHORSHIP QUEUE = 165 / 252
RMG APPLICABILITY-JUDGMENT QUEUE = 15
RMG MATH COVERAGE = 72 / 252 ≈ 29%
```

## Combined workload

The TKG and RMG corpora remain disjoint.

```text
TKG records requiring human authorship      37
RMG records requiring human authorship     165
                                            ---
exact authored-record queue                202

additional structural applicability judgments 15
```

The corrected TKG corpus size does not change the 202-record authorship workload because the two recovered records are already complete after structural repair.

## Ordering decision

The 37-record TKG queue remains the authorized pilot because it is smaller and bounded. It tests a human-review workflow on Family-B-shaped data only. It does not establish policy transfer to the 165-record RMG queue.

## Required parse gate

Before classification or queue construction:

```text
UNPARSEABLE / NEEDS_REPAIR
```

must be treated as a blocking source-integrity state. Invalid records must never be skipped silently or counted as absent.

## Policy failure conditions

The pilot fails if:

1. missing type is inferred solely from filename or field pattern;
2. missing MATH becomes `MATH-M0` without a human-authored decision;
3. `math`, `math_state`, and `claim_ceiling` are treated as synonyms;
4. generated values lack value-origin provenance;
5. structural records receive governance axes without an applicability judgment;
6. unparseable records are skipped;
7. a reviewer cannot reconstruct the decision from source and evidence.

## Current state

```text
TKG REGISTRY RECORDS = 120
TKG HUMAN-AUTHORSHIP PILOT SIZE = 37
TKG AXIS-COMPLETE RECORDS = 83
TKG SOURCE-INTEGRITY REPAIRS = 2
RMG HUMAN-AUTHORSHIP QUEUE = 165
RMG APPLICABILITY QUEUE = 15
COMBINED AUTHORED-RECORD QUEUE = 202
AUTOMATIC CLASSIFICATION = PROHIBITED
AUTOMATIC CEILING COMPLETION = PROHIBITED
TKG MIGRATION = NOT AUTHORIZED
RMG OPERATIONAL AUTHORITY OVER TKG = NOT GRANTED
MERGE TO MAIN = NOT AUTHORIZED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
```

The next deliverable remains a human review form for exactly 37 records. It is not a migration, adapter execution, benchmark expansion, or reasoning-engine claim.
