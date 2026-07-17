# TKG-SCHEMA-FAMILY-SPLIT-AUDIT-001

Status: BLOCKING SCHEMA AUDIT

Date: 2026-07-17

## Decision

The existing translation knowledge graph registries do not share one executable schema.

The current `TKG-DATA-EXECUTION-VERTICAL-SLICE-001` is therefore reclassified as:

`FAMILY-A-ONLY EXECUTION PROTOTYPE — NOT EVIDENCE OF GLOBAL REGISTRY EXECUTABILITY`

It must not be described as validating the schema of TKG-001 through TKG-015.

## Observed schema families

### Family A

Scope: TKG-001 through TKG-008.

Primary identity fields:

- `record_id`
- `name`

### Family B

Scope: TKG-009 through TKG-015.

Primary identity fields:

- `id`
- `concept`

The split is treated as a hard compatibility boundary until a migration audit verifies every file.

## Consequence for the existing vertical slice

TKG-002 belongs to Family A. A successful TKG-002 calculation can establish only that a loader and executor can be built around one Family-A sample. It cannot establish that:

- a common registry schema exists;
- Family B is loadable;
- the fifteen registries are interchangeable execution sources;
- the authored mathematical prose is executable;
- the current loader generalizes beyond its selected sample.

Any earlier language suggesting otherwise is withdrawn.

## Human formulas are not executable rules

Fields such as:

```text
tau(n)=sum_{d|n}1
if n=prod p_i^{a_i}, tau(n)=prod(a_i+1)
```

are mathematical prose and notation. They are not a stable machine-execution contract.

The execution path must not infer operator semantics from unrestricted formula strings. Doing so would require a separately specified mathematical parser and semantic interpreter. A hidden mapping from node names or formula patterns to operators would merely reproduce hand-authored routing at another layer.

## Required executable contract

Executable nodes must carry an explicit field such as:

```json
{
  "executable_rule": {
    "operator_id": "OP-EVALUATE-DIVISOR-SUM-001",
    "args": {
      "summand": "one"
    },
    "result_symbol": "tau"
  }
}
```

The finite operator algebra remains project-authored code. This is acceptable and must be stated openly. Registry data selects an operator and supplies validated arguments; it does not create the operator implementation.

## Ordering gate

Before further execution-composer work:

1. Define one canonical schema.
2. Define adapters or migrations for both identity families.
3. Add explicit `executable_rule` only to nodes selected for execution.
4. Migrate at least one executable candidate from Family A and one structural/load-only candidate from Family B.
5. Validate that both normalize into the same `KnowledgeNode` contract.
6. Reject execution when `executable_rule` is absent.
7. Keep human formulas as citations and retrieval material, not executable instructions.

## Contamination audit rule

Contamination must be detected structurally inside `examples` and benchmark-case objects. Raw text search is prohibited as a decision rule.

A numeric value appearing in unrelated metadata, such as `case_count: 24`, does not contaminate a query whose structured case is `tau(360)=24`.

The audit must compare contextual tuples such as:

```text
(function or rule identity, input n, expected value, optional derivation artifacts)
```

and classify:

- `CLEAN_RULE_ONLY`
- `PARTIALLY_CONTAMINATED`
- `DIRECT_ANSWER_PRESENT`

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
```

## Next authorized deliverable

`TKG-CANONICAL-EXECUTABLE-SCHEMA-001`

No new orchestrator and no larger benchmark are authorized before that deliverable and a two-family migration check.