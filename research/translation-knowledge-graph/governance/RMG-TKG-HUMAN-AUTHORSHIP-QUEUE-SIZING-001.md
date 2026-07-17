# RMG-TKG-HUMAN-AUTHORSHIP-QUEUE-SIZING-001

Status: COMPLETED READ-ONLY QUEUE-SIZING DECISION

Date: 2026-07-17

## Decision

The human-authorship and classification debt is now measured exactly enough to determine work order.

The TKG and RMG corpora are disjoint on the current branch. No legal RMG record refers to TKG and no prior TKG-to-RMG migration is evidenced in the measured registries.

Therefore cross-corpus overlap is zero for queue-sizing purposes.

## TKG queue

Corpus size: 118 records.

```text
needs type and claim ceiling     12
needs type only                  15
needs claim ceiling only         10
complete on both axes            81
                                ---
total                           118
```

The 12 records missing both type and ceiling are contained inside the 27 untyped records. They must not be counted twice.

Thus:

```text
TKG HUMAN-AUTHORSHIP QUEUE = 37 / 118
TKG COMPLETE ON TYPE+CEILING = 81 / 118 ≈ 69%
```

## RMG queue

Corpus size: 252 records.

```text
untyped and missing MATH/OPS/CERT              66
mathematical-content records missing axes       99
structural records requiring applicability      15
                                                ---
records requiring authored classification       165
separate applicability judgments                 15
```

The 15 structural records must receive an explicit reviewed applicability decision such as `NOT_APPLICABLE`; they must not receive invented ladder values merely to satisfy completeness.

Thus:

```text
RMG HUMAN-AUTHORSHIP QUEUE = 165 / 252
RMG APPLICABILITY-JUDGMENT QUEUE = 15
RMG MATH COVERAGE = 72 / 252 ≈ 29%
```

## Combined exact workload

The corpora are disjoint.

```text
TKG records requiring human authorship      37
RMG records requiring human authorship     165
                                           ---
exact authored-record queue                202

additional structural applicability judgments 15
```

The previous approximate figure of 204 is withdrawn.

## Ordering decision

The 37-record TKG queue is the authorized pilot.

Reason:

1. It is smaller and bounded.
2. Its overlap structure is known exactly.
3. TKG is more complete on the measured type-and-ceiling axes than RMG is on MATH coverage.
4. Policy defects can be exposed on 37 records before applying the policy to 165 RMG records.
5. Starting with RMG would combine policy design, type normalization, record-class repair, and authorship at the larger scale.

This ordering does not create a second governance authority. The pilot tests the human-review policy and provenance contract that may later be adopted under RMG architecture.

## Required pilot outputs

`TKG-HUMAN-AUTHORSHIP-AND-CLASSIFICATION-PILOT-001` must be a review queue, not an automatic classifier.

Each of the 37 rows must contain at least:

- immutable source locator;
- source record identifier;
- source file and line when available;
- source type field and source type value, or explicit absence;
- source ceiling fields among `claim_ceiling`, `math`, and `math_state`;
- queue category: `TYPE_AND_CEILING`, `TYPE_ONLY`, or `CEILING_ONLY`;
- proposed canonical record class, initially blank;
- proposed mathematical-governance value, initially blank;
- textual claim ceiling, initially blank when unauthored;
- reviewer identity;
- review evidence;
- decision status;
- second-review requirement for high-risk claims;
- explicit prohibition on heuristic completion.

## Policy test criteria

The pilot policy fails if any of the following occurs:

1. Missing type is inferred solely from filename or field pattern.
2. Missing MATH becomes `MATH-M0` without a human-authored decision.
3. `math`, `math_state`, and `claim_ceiling` are treated as synonyms.
4. A generated value is serialized without value-origin provenance.
5. A structural record receives governance axes without an applicability judgment.
6. A reviewer cannot distinguish source-authored, normalized, and newly authored values.
7. A second reviewer cannot reconstruct the decision from the locator and evidence.

## Scientific interpretation

This work does not add a reasoning layer or a mathematical result.

It converts unknown governance debt into a measured review population:

```text
fixture regression                         24/24
stubbed generator                           0/24
TKG authored-record queue                  37
RMG authored-record queue                 165
structural applicability judgments         15
combined human-authorship queue           202
MATH / PNT / PNT-AP / Goldbach / RH / GRH progress = NONE
```

The project now knows the measured size of the human judgment that prior schemas, adapters, and guards had deferred.

## Current state

```text
TKG HUMAN-AUTHORSHIP PILOT = AUTHORIZED AS NEXT DELIVERABLE
TKG PILOT SIZE = 37
RMG HUMAN-AUTHORSHIP QUEUE = 165
RMG APPLICABILITY QUEUE = 15
COMBINED AUTHORED-RECORD QUEUE = 202
AUTOMATIC CLASSIFICATION = PROHIBITED
AUTOMATIC CEILING COMPLETION = PROHIBITED
RMG ADAPTER REPAIR = BLOCKED UNTIL PILOT POLICY REVIEW
TKG MIGRATION = NOT AUTHORIZED
RMG OPERATIONAL AUTHORITY OVER TKG = NOT GRANTED
MERGE TO MAIN = NOT AUTHORIZED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
```

## Next authorized deliverable

`TKG-HUMAN-AUTHORSHIP-AND-CLASSIFICATION-PILOT-001`

It is an inventory and review form for exactly 37 records. It is not a migration, adapter execution, benchmark expansion, or reasoning-engine claim.
