# TKG-RMG-AUTHORITY-DECISION-001

Status: ARCHITECTURAL DECISION — RMG GOVERNING, REPAIR GATE OPEN

Date: 2026-07-17

## Decision

TKG is not an independent governance authority and must not maintain a competing canonical research-memory schema.

The governing direction is:

`TKG = DOMAIN-SPECIFIC CLIENT / SOURCE CORPUS OF RMG`

`RMG = GOVERNING RESEARCH-MEMORY NAMESPACE AND MIGRATION AUTHORITY`

This decision is architectural, not a claim that the current RMG implementation is already safe for TKG migration.

## Why RMG governs

RMG already defines the repository-level separation of:

- assimilation depth;
- mathematical contribution depth;
- operational maturity;
- certificate strength.

TKG source records already carry these namespaces in substantial portions of the corpus through fields such as:

- `assimilation_level`;
- `math_contribution_level`;
- `operational_maturity`;
- `certificate_strength`.

A parallel TKG canonical schema would create two active legal models for the same research-memory objects and would collapse governed multidimensional state into a free-text `claim_ceiling` field.

## RMG is not adopted without repair

The current `rmg_schema_adapter.py` is not safe as a TKG migration engine because it generates governance-bearing defaults, including:

- `math_contribution_level = MATH-M0` when absent;
- `operational_maturity = OPS-LEGACY-UNCLASSIFIED` when absent;
- `certificate_strength = CERT-LEGACY-UNCLASSIFIED` when absent;
- generated missing-value objects for `claim_ceiling`.

These values may be conservative, but they are not authored source facts. They must remain distinguishable from authored values.

Therefore:

`RMG AUTHORITY = ACCEPTED`

`CURRENT RMG ADAPTER FOR TKG = NOT AUTHORIZED`

## Fifth schema axis: governance-field aliases

The TKG audit previously treated `claim_ceiling` absence as missing governance. That was too broad.

For concept-like records without textual `claim_ceiling`:

- 19 carry authored governance state under `math`;
- 4 records in the broader corpus use `math_state`;
- only 12 concept-like records lack any identified authored ceiling or mathematical-state signal.

The exact overlap among these fields must be preserved in the migration inventory; no migration may infer that `math`, `math_state`, and `claim_ceiling` are semantically identical.

Canonical treatment:

- `math` or `math_state` maps only to the RMG mathematical-contribution namespace after vocabulary review;
- `claim_ceiling` remains a separate textual claim boundary when authored;
- absence of textual `claim_ceiling` does not erase an authored `math` or `math_state` value;
- absence of all three is represented as explicit unauthored state, never as an invented default.

## Source locator decision

TKG must reuse and, where necessary, extend the RMG source-locator contract rather than maintain an independent locator authority.

RMG locator fields remain authoritative:

- `claim_id`;
- `repository`;
- `branch_or_commit`;
- `source_path`;
- `section_or_symbol`;
- `source_resolution_status`;
- `content_review_status`;
- `overlay_id`.

Record-level JSONL provenance may add subordinate fields such as source line and original field names, but these are extensions under RMG, not a replacement contract.

## Record-class and type problem remains open

The corpus is not adequately described by two schema families. It contains three operational groups:

- 64 records with `record_type`-style typing;
- 29 records with `kind`-style typing;
- 27 records with no explicit type field.

The source vocabulary contains roughly thirty distinct type labels, while the preliminary TKG enum directly matched only a small subset. `OPERATOR` currently has no approved canonical class.

The 27 untyped records require reviewed classification. Heuristic classification is prohibited for canonical migration.

## Status of the TKG canonical schema

`TKG-CANONICAL-EXECUTABLE-SCHEMA-001` is frozen as a non-authoritative experiment.

It may be retained as design evidence for:

- strict record unions;
- explicit executable rules;
- no silent legacy fields;
- execution prohibition when governance is unauthored.

It must not become a second canonical memory schema and must not receive adapters or migrated production records.

## Required repair gate before migration

Before any TKG-to-RMG adapter or mapping table:

1. inventory all source type labels and classify them into RMG record classes;
2. create a human-reviewed queue for the 27 untyped records;
3. define an `OPERATOR` record class or explicitly place operators outside canonical memory records;
4. preserve the four RMG axes independently;
5. distinguish authored, normalized, and generated values for every governance field;
6. repair the RMG adapter so missing values never masquerade as authored values;
7. reconcile `claim_ceiling`, `math`, and `math_state` without treating them as synonyms;
8. reuse the RMG source-locator protocol with subordinate record-level provenance;
9. register TKG migration in `rmg-migration-registry.jsonl` only after independent review.

## Current state

```text
TKG AUTHORITY = CLIENT OF RMG
RMG GOVERNING AUTHORITY = ACCEPTED
RMG TKG-ADAPTER = BLOCKED PENDING REPAIR
TKG CANONICAL SCHEMA = FROZEN NON-AUTHORITATIVE EXPERIMENT
TYPE MAPPING = NOT AUTHORIZED
UNTYPED RECORD CLASSIFICATION = HUMAN REVIEW REQUIRED
EXECUTION VERTICAL SLICE = FAMILY-A PROTOTYPE ONLY
MERGE TO MAIN = NOT AUTHORIZED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
```

## Next authorized deliverable

`RMG-TKG-COMPATIBILITY-AND-ADAPTER-REPAIR-AUDIT-001`

This is an audit and repair specification. It is not an adapter implementation and not a migration execution.