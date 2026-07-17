# TKG-SCHEMA-FAMILY-SPLIT-AUDIT-001

Status: BLOCKING SCHEMA AUDIT — EXPANDED TO FOUR AXES

Date: 2026-07-17

## Decision

The existing translation knowledge graph registries do not share one executable schema.

The current `TKG-DATA-EXECUTION-VERTICAL-SLICE-001` is therefore reclassified as:

`FAMILY-A-ONLY EXECUTION PROTOTYPE — NOT EVIDENCE OF GLOBAL REGISTRY EXECUTABILITY`

It must not be described as validating the schema of TKG-001 through TKG-015.

## The divergence has four independent axes

The earlier audit recorded only identity and naming. That was incomplete. The actual migration boundary includes:

1. identity field;
2. naming field;
3. type field and vocabulary;
4. claim-ceiling presence and authorship status.

### Identity axis

- Family A primarily uses `record_id`.
- Family B primarily uses `id`.
- A canonical migration can recover a record identifier for 118/118 records.

### Naming axis

- Family A concept-like records commonly use `name`.
- Family B concept-like records commonly use `concept`.
- A usable canonical name is available for 76/118 records under the measured mapping.
- The remaining records include edges, tasks, rejections, file headers, and metadata records that must not be forced into a concept-node contract.

### Type axis

- `record_type` occurs in 62 records.
- `kind` occurs in 29 records.
- 27 records contain neither field.
- Combining `record_type` and `kind` yields a recoverable source type for 91/118 records.
- Source type vocabularies are not normalized: uppercase underscore forms and lowercase hyphenated forms both occur.

A canonical schema must therefore use a closed enum and an explicit migration mapping. It must not preserve arbitrary source type strings as canonical types.

### Claim-ceiling axis

- `claim_ceiling` occurs in 73/118 records.
- Among the 76 concept-like records with usable names, 31 have no authored `claim_ceiling`.
- Absence of a ceiling is not permission to manufacture one during migration.

The required canonical representation is:

```json
{
  "claim_ceiling": null,
  "ceiling_status": "NOT_AUTHORED"
}
```

A migration script is prohibited from silently inserting `MATH-M0`, `Definition only`, or any other substantive ceiling. Only a human-authored review may change `ceiling_status` to `AUTHORED` and supply a nonempty ceiling.

A concept node with `ceiling_status: NOT_AUTHORED` is ineligible for `executable_rule`.

## Current satisfiability measurement

The first canonical schema required four fields on every record. Measured against the 118 source records:

```text
recoverable node_id                              118 / 118
recoverable record type using record_type|kind   91 / 118
recoverable name using name|concept              76 / 118
authored claim_ceiling                           73 / 118
intersection satisfying all four                 45 / 118
```

Thus only 45/118 records, approximately 38%, could satisfy the original all-record node contract without inventing data.

This number is a blocker, not a quality score. It demonstrates that one universal node schema was the wrong abstraction for the mixed registry corpus.

## Record classes must be separated

At least 42/118 records are not ordinary concept nodes. The corpus includes, among others:

- `REASONING_TASK`: 10;
- `CLAIM_REJECTION`: 9;
- `DEPENDENCY_EDGE`: 6;
- `IDENTITY_EDGE`: 2;
- `THEOREM_EQUIVALENCE_EDGE`: 1;
- file-level records such as `taxonomy`, `dependency-graph`, and `query_capability`;
- a record whose source type is literally `claim_ceiling`.

The canonical contract must therefore be a strict union of separate record classes:

- concept/theorem/PVG-object node;
- relation edge;
- reasoning task;
- claim rejection;
- file metadata.

Only concept/theorem/PVG-object nodes may carry `executable_rule`.

## Strict migration mode

Canonical migrated records must reject legacy fields rather than retaining them silently.

`additionalProperties: true` at the canonical root is prohibited because a record containing both canonical `names` and legacy `concept` could otherwise pass validation while preserving unresolved schema drift.

The canonical schema must use `additionalProperties: false` in each record contract. Source records remain unchanged; the strictness applies to migrated canonical output.

## Source locator requirements

The source locator must record all four source-axis fields, including explicit nulls when absent:

```json
{
  "source_id_field": "record_id",
  "source_name_field": "name",
  "source_type_field": "record_type",
  "source_ceiling_field": "claim_ceiling"
}
```

This provenance distinguishes authored source values from migration-normalized values and prevents a later reader from treating generated defaults as authored knowledge.

## Consequence for the existing vertical slice

TKG-002 belongs to Family A. A successful TKG-002 calculation can establish only that a prototype can be built around one Family-A sample. It cannot establish that:

- a common registry schema exists;
- Family B is loadable;
- all record classes are normalized;
- the fifteen registries are interchangeable execution sources;
- authored mathematical prose is executable;
- missing claim ceilings have been governed;
- the current loader generalizes beyond its selected sample.

Any earlier language suggesting otherwise is withdrawn.

## Human formulas are not executable rules

Fields such as:

```text
tau(n)=sum_{d|n}1
if n=prod p_i^{a_i}, tau(n)=prod(a_i+1)
```

are mathematical prose and notation. They are not a stable machine-execution contract.

The execution path must not infer operator semantics from unrestricted formula strings. Doing so would require a separately specified mathematical parser and semantic interpreter. A hidden mapping from node names or formula patterns to operators would reproduce hand-authored routing at another layer.

## Required executable contract

An execution-eligible concept node must carry an explicit field such as:

```json
{
  "ceiling_status": "AUTHORED",
  "claim_ceiling": "Finite divisor geometry only.",
  "executable_rule": {
    "operator_id": "OP-EVALUATE-DIVISOR-SUM-001",
    "args": {
      "summand": "one"
    },
    "result_symbol": "tau"
  }
}
```

The finite operator algebra remains project-authored code. Registry data selects an operator and supplies validated arguments; it does not create the operator implementation.

## Ordering gate

Before adapter or execution-composer work:

0. Record the four-axis schema audit, the 45/118 satisfiability result, and the no-invented-ceiling policy.
1. Define a strict canonical union schema for separate record classes.
2. Define explicit type-vocabulary mappings for both source families and untyped records.
3. Define adapters or migrations for both identity families.
4. Preserve missing ceilings as `null / NOT_AUTHORED`.
5. Add `executable_rule` only to human-reviewed, execution-eligible concept nodes.
6. Migrate at least one executable candidate from Family A and one structural/load-only candidate from Family B.
7. Validate that both normalize under their proper canonical record contracts.
8. Reject execution when `executable_rule` is absent or the ceiling is not authored.
9. Keep human formulas as citations and retrieval material, not executable instructions.

## Contamination audit rule

Contamination must be detected structurally inside `examples` and benchmark-case objects. Raw text search is prohibited as a decision rule.

A numeric value appearing in unrelated metadata, such as `case_count: 24`, does not contaminate a query whose structured case is `tau(360)=24`.

The audit must compare contextual tuples such as:

```text
(function or rule identity, input n, expected value, optional derivation artifacts)
```

and classify:

- `CLEAN_RULE_ONLY`;
- `PARTIALLY_CONTAMINATED`;
- `DIRECT_ANSWER_PRESENT`.

## Current scientific state

```text
MATH = MATH-M0
PNT progress = NONE
PNT-AP progress = NONE
Goldbach progress = NONE
RH progress = NONE
GRH progress = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
REASONING ENGINE CLAIM = PROHIBITED
GLOBAL EXECUTABLE-KB CLAIM = PROHIBITED
ADAPTER IMPLEMENTATION = BLOCKED PENDING TYPE MAPPING AND TWO-FAMILY MIGRATION PLAN
```

## Next authorized deliverable

`TKG-TWO-FAMILY-RECORD-CLASS-MIGRATION-SPEC-001`

No new orchestrator, larger benchmark, adapter implementation, or execution-composer expansion is authorized before that deliverable is reviewed.
