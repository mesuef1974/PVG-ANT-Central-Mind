# TKG-RMG-AUTHORITY-DECISION-001

Status: ARCHITECTURAL PREFERENCE — OPERATIONAL AUTHORITY CONDITIONAL

Date: 2026-07-17

## Decision

TKG must not maintain a competing repository-wide research-memory governance schema.

The architectural direction remains:

`TKG = DOMAIN-SPECIFIC CLIENT / SOURCE CORPUS OF RMG`

`RMG = PREFERRED GOVERNING RESEARCH-MEMORY NAMESPACE`

This is not yet an operational acceptance of the current RMG registry or adapter.

The previous state:

```text
RMG GOVERNING AUTHORITY = ACCEPTED
```

is withdrawn and replaced by:

```text
RMG ARCHITECTURAL AUTHORITY = PREFERRED
RMG OPERATIONAL AUTHORITY OVER TKG = PENDING COVERAGE AND PROVENANCE AUDIT
```

## Why RMG remains the preferred architecture

RMG defines separate namespaces for:

- assimilation depth;
- mathematical contribution depth;
- operational maturity;
- certificate strength.

TKG source records already use these namespaces in substantial portions of the corpus through fields such as:

- `assimilation_level`;
- `math_contribution_level`;
- `operational_maturity`;
- `certificate_strength`.

A parallel TKG authority would create two legal models for the same research-memory objects and could collapse governed multidimensional state into free-text claim language.

## Why operational acceptance is withheld

The legal RMG registry has not yet been shown to satisfy its own four-axis governance contract.

Reported measurement over 252 legal records found:

```text
math_contribution_level present     72 / 252
math_contribution_level absent     180 / 252
```

Thus approximately 71% of measured records lack the mathematical-contribution field that RMG-GOV-001 declares part of the canonical concept contract.

This does not prove those records are invalid; some may be non-concept records, aliases, overlays, or deliberately incomplete records. It does prove that document-level governance cannot be treated as registry-level implementation without a record-class-aware coverage audit.

## Adapter hazard

The current `rmg_schema_adapter.py` generates governance-bearing defaults when source fields are absent:

- `math_contribution_level = MATH-M0`;
- `operational_maturity = OPS-LEGACY-UNCLASSIFIED`;
- `certificate_strength = CERT-LEGACY-UNCLASSIFIED`;
- generated missing-value objects for `claim_ceiling`.

The OPS and CERT placeholders are visibly synthetic. `MATH-M0` is not: it is also a legitimate authored value. If serialized without provenance, a generated `MATH-M0` cannot later be distinguished from an authored one.

The absence of `OPS-LEGACY-UNCLASSIFIED` and `CERT-LEGACY-UNCLASSIFIED` from legal JSONL records is evidence that those exact placeholders have not been written there. It does not establish that no generated `MATH-M0` has ever been written.

Therefore:

```text
CURRENT RMG ADAPTER FOR TKG = NOT AUTHORIZED
MATH DEFAULT CONTAMINATION = NOT AUDITABLE WITH CURRENT PROVENANCE
```

## Verifier hazard

`verify_rmg_gov_002.py` builds a synthetic sample without `math_contribution_level`, adapts it, and treats this assertion as success:

```python
adapted["math_contribution_level"] == "MATH-M0"
```

The check named `math_not_auto_promoted` verifies a conservative generated value, not source fidelity. It cannot detect the fabrication of an apparently authored `MATH-M0`.

The verifier must be replaced with record-backed tests that check both value and value origin.

## Fifth schema axis: governance-field aliases

The TKG audit previously treated absence of textual `claim_ceiling` as absence of governance. That was too broad.

Among concept-like records without textual `claim_ceiling`:

- 19 carry authored state under `math`;
- the broader corpus also uses `math_state` in 4 records;
- only 12 concept-like records lack any identified signal among `claim_ceiling`, `math`, and `math_state`.

These fields are not synonyms:

- `math` or `math_state` may map to the RMG mathematical-contribution namespace only after vocabulary review;
- `claim_ceiling` remains a separate textual boundary;
- absence of textual `claim_ceiling` does not erase authored mathematical state;
- absence of all signals remains explicit absence and must not become `MATH-M0` by default.

## Source locator decision

TKG should reuse and, where necessary, extend the RMG source-locator contract rather than maintain an independent locator authority.

RMG locator fields remain the preferred base:

- `claim_id`;
- `repository`;
- `branch_or_commit`;
- `source_path`;
- `section_or_symbol`;
- `source_resolution_status`;
- `content_review_status`;
- `overlay_id`.

Record-level JSONL provenance may add subordinate fields such as source line, source field name, adapter version, and value origin.

This reuse is conditional on the RMG repair gate and does not authorize migration.

## Record-class and type problem remains open

The TKG corpus contains three operational groups:

- 64 records with `record_type`-style typing;
- 29 records with `kind`-style typing;
- 27 records with no explicit type field.

The source vocabulary contains roughly thirty distinct labels. `OPERATOR` has no approved canonical class.

The 27 untyped records require human-reviewed classification. Heuristic classification is prohibited for canonical migration.

## Status of the TKG canonical schema

`TKG-CANONICAL-EXECUTABLE-SCHEMA-001` remains frozen as a non-authoritative experiment.

It may be retained as design evidence for:

- strict record unions;
- explicit executable rules;
- rejection of silent legacy fields;
- execution prohibition when governance is unauthored.

It must not become a second canonical memory authority and must not receive production adapters or migrated records.

## Required gates before RMG may govern TKG operationally

1. Audit all legal RMG records against the four RMG axes by record class.
2. Measure authored, aliased, normalized, generated, and absent values separately.
3. Repair `rmg_schema_adapter.py` so absence never becomes an apparently authored ladder value.
4. Add per-axis source and value-origin provenance.
5. Replace the hollow `math_not_auto_promoted` check with real-record source-fidelity tests.
6. Inventory all TKG source type labels.
7. Create a human-reviewed queue for the 27 untyped TKG records.
8. Resolve the canonical treatment of `OPERATOR`.
9. Reconcile `claim_ceiling`, `math`, and `math_state` without treating them as synonyms.
10. Register a TKG migration only after independent review.

## Current state

```text
TKG AUTHORITY = CLIENT CANDIDATE OF RMG
RMG ARCHITECTURAL AUTHORITY = PREFERRED
RMG OPERATIONAL AUTHORITY OVER TKG = PENDING
RMG REGISTRY FOUR-AXIS COVERAGE = NOT YET AUDITED
RMG TKG-ADAPTER = BLOCKED
RMG GOV-002 VERIFIER = FALSE-ASSURANCE DEFECT RECORDED
TKG CANONICAL SCHEMA = FROZEN NON-AUTHORITATIVE EXPERIMENT
TYPE MAPPING = NOT AUTHORIZED
UNTYPED RECORD CLASSIFICATION = HUMAN REVIEW REQUIRED
EXECUTION VERTICAL SLICE = FAMILY-A PROTOTYPE ONLY
MERGE TO MAIN = NOT AUTHORIZED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
```

## Governing repair audit

`RMG-TKG-COMPATIBILITY-AND-ADAPTER-REPAIR-AUDIT-001`

## Next authorized deliverable

`RMG-FOUR-AXIS-REGISTRY-COVERAGE-AUDIT-001`

This is a read-only, record-class-aware measurement over the legal RMG registry. No adapter repair, TKG mapping table, migration execution, new orchestrator, or larger benchmark is authorized before its report is reviewed.