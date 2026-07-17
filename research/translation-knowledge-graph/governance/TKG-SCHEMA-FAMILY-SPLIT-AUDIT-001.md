# TKG-SCHEMA-FAMILY-SPLIT-AUDIT-001

Status: BLOCKING SCHEMA AUDIT — SUPERSEDED IN AUTHORITY BY TKG-RMG-AUTHORITY-DECISION-001

Date: 2026-07-17

## Decision

The existing translation knowledge graph registries do not share one executable schema.

The current `TKG-DATA-EXECUTION-VERTICAL-SLICE-001` remains classified as:

`FAMILY-A-ONLY EXECUTION PROTOTYPE — NOT EVIDENCE OF GLOBAL REGISTRY EXECUTABILITY`

TKG is now governed as a domain-specific client/source corpus of RMG. This audit remains evidence about source heterogeneity; it is not an independent canonical-schema authority.

## The divergence has five independent axes

1. identity field;
2. naming field;
3. type field and vocabulary;
4. record class;
5. governance-field names and authorship status.

### Identity axis

- `record_id` and `id` are both used.
- A source identifier is recoverable for 118/118 records.

### Naming axis

- concept-like records use `name` or `concept`.
- a usable concept name is available for 76/118 records.
- edges, tasks, rejections, metadata, and operators must not be forced into a concept-name contract.

### Type axis

The corpus is better described by three operational groups, not two complete schema families:

```text
record_type-style records   64
kind-style records          29
untyped records             27
```

The source vocabulary contains roughly thirty distinct labels. A preliminary canonical enum matched only a small subset directly. `OPERATOR` has no approved canonical class.

The 27 untyped records require human-reviewed classification. Canonical type assignment by filename, field pattern, or heuristic inference is prohibited.

### Record-class axis

The corpus includes concept/theorem/PVG-object records, relation edges, reasoning tasks, claim rejections, file metadata, query capability records, taxonomies, dependency graphs, and operators.

A single universal node contract is invalid for this corpus.

### Governance-field axis

The previous audit overstated the unauthored-ceiling count.

Among 31 concept-like records without textual `claim_ceiling`:

- 19 carry authored state under `math`;
- the broader corpus also uses `math_state` in 4 records;
- only 12 concept-like records lack any identified authored signal among `claim_ceiling`, `math`, and `math_state`.

These fields are not synonyms:

- `math` and `math_state` are candidates for the RMG mathematical-contribution namespace after vocabulary review;
- `claim_ceiling` is a textual claim boundary;
- an authored mathematical level must not be erased merely because textual `claim_ceiling` is absent;
- missing values must remain explicitly unauthored.

No migration may insert `MATH-M0`, `Definition only`, or any other substantive state and present it as authored source data.

## Historical satisfiability measurement

The first TKG canonical schema required identity, type, name, and textual claim ceiling on every record. Against the 118-record source corpus:

```text
recoverable node_id                              118 / 118
recoverable source type                           91 / 118
recoverable name                                  76 / 118
textual claim_ceiling                             73 / 118
intersection satisfying all four                  45 / 118
```

The 45/118 result remains valid as a measurement of that rejected all-record contract. It must not be interpreted as the number of records carrying any authored mathematical-governance state, because `math` and `math_state` were omitted from that calculation.

## RMG authority interaction

RMG already governs separate axes for:

- `assimilation_level`;
- `math_contribution_level`;
- `operational_maturity`;
- `certificate_strength`.

TKG records substantially reuse these exact namespaces. Therefore a free-text-only TKG canonical schema would collapse dimensions that RMG intentionally separates.

The decision is:

```text
TKG = RMG CLIENT / SOURCE CORPUS
RMG = GOVERNING MEMORY AUTHORITY
```

However, the current RMG adapter is not authorized for TKG because it creates defaults such as `MATH-M0`, `OPS-LEGACY-UNCLASSIFIED`, and `CERT-LEGACY-UNCLASSIFIED` when source values are absent. Conservative generated values still require explicit generated-value provenance and must not masquerade as authored facts.

## Source locator

The preliminary TKG `source_record_locator` is not an independent authority.

RMG-GOV-005 remains the governing source-locator protocol. Record-level source line and original-field names may be retained only as subordinate extensions under the RMG locator and migration registry.

## Human formulas and executable rules

Human mathematical formulas remain descriptive and retrievable, not executable instructions.

Execution requires an explicit reviewed operator contract. This design principle is retained from the TKG experiment, but any durable executable extension must live under RMG governance and preserve all four RMG axes independently.

## Contamination audit rule

Contamination must be detected structurally inside `examples` and benchmark-case objects. Raw text search is prohibited as a decision rule.

A numeric value appearing in unrelated metadata, such as `case_count: 24`, does not contaminate a structured case such as `tau(360)=24`.

## Current state

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
TKG INDEPENDENT SCHEMA AUTHORITY = WITHDRAWN
RMG GOVERNING AUTHORITY = ACCEPTED WITH REPAIR GATE
ADAPTER IMPLEMENTATION = BLOCKED
```

## Next authorized deliverable

`RMG-TKG-COMPATIBILITY-AND-ADAPTER-REPAIR-AUDIT-001`

No mapping table, adapter implementation, migration execution, new orchestrator, or larger benchmark is authorized before that audit is reviewed.