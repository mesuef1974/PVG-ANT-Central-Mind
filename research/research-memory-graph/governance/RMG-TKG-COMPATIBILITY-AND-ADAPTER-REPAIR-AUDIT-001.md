# RMG-TKG-COMPATIBILITY-AND-ADAPTER-REPAIR-AUDIT-001

Status: BLOCKING AUDIT AND REPAIR SPECIFICATION

Date: 2026-07-17

## Decision

RMG remains the preferred architectural authority for TKG research-memory records because it separates assimilation, mathematical contribution, operational maturity, and certificate strength.

That authority is conditional rather than operationally accepted:

```text
RMG ARCHITECTURAL AUTHORITY = PREFERRED
RMG REGISTRY GOVERNANCE FITNESS = NOT YET ESTABLISHED
RMG ADAPTER FOR TKG = NOT AUTHORIZED
TKG MIGRATION = BLOCKED
```

No TKG mapping table, adapter execution, or production migration is authorized until the three gates in this audit are closed.

## Finding 1 — latent adapter defaults have unequal detectability

The current adapter generates these values when source fields are absent:

```text
math_contribution_level = MATH-M0
operational_maturity = OPS-LEGACY-UNCLASSIFIED
certificate_strength = CERT-LEGACY-UNCLASSIFIED
```

The OPS and CERT defaults are visibly synthetic. A later scan can distinguish them from normal authored vocabulary.

`MATH-M0` is different. It is also a legitimate authored value. Once written without provenance, a generated `MATH-M0` is indistinguishable from an authored `MATH-M0`.

Therefore absence of `OPS-LEGACY-UNCLASSIFIED` and `CERT-LEGACY-UNCLASSIFIED` in the legal JSONL registry does not prove that no generated MATH value was ever written.

The repair must not replace `MATH-M0` with a different semantic judgment. It must preserve absence explicitly and attach provenance per axis.

Required representation pattern:

```json
{
  "math_contribution_level": null,
  "math_contribution_status": "NOT_AUTHORED",
  "math_contribution_source_field": null,
  "math_contribution_value_origin": "ABSENT_IN_SOURCE"
}
```

An alternative sentinel such as `MATH-NOT-AUTHORED` may be used only if the RMG namespace formally admits it. A nullable value plus status and origin is preferred because it cannot be confused with the mathematical ladder.

The same origin contract is required independently for all four axes:

- assimilation;
- mathematical contribution;
- operational maturity;
- certificate strength.

Allowed value-origin states must be closed and explicit, for example:

```text
AUTHORED_SOURCE
NORMALIZED_FROM_AUTHORED_SOURCE
GENERATED_PLACEHOLDER
ABSENT_IN_SOURCE
HUMAN_REVIEWED_OVERLAY
```

Generated placeholders must never be serialized as if they were authored values.

## Finding 2 — `verify_rmg_gov_002.py` currently certifies fabrication

The verifier constructs an artificial sample without `math_contribution_level`, passes it through the adapter, and checks:

```python
adapted["math_contribution_level"] == "MATH-M0"
```

This check is named `math_not_auto_promoted`, but it does not test source fidelity. It tests that the adapter inserted its own conservative default.

Consequences:

- the check cannot fail when a missing source value is fabricated as `MATH-M0`;
- it fails only if the adapter promotes above M0;
- the check name overstates the protection supplied;
- the verifier provides false assurance about provenance safety.

Required replacement:

1. Use real registry records selected by exact file and line or stable record identifier.
2. Include at least one record with authored MATH, one with an alias such as `math` or `math_state`, and one with no mathematical-state field.
3. Verify both value and value origin.
4. Require that absence remains absence or an explicit `NOT_AUTHORED` state.
5. Fail if an absent source field becomes an apparently authored `MATH-M0`.
6. Preserve the source record byte-for-byte or structurally unchanged in the adapter envelope.

Minimum assertions:

```text
AUTHORED MATH-M0 -> MATH-M0 + AUTHORED_SOURCE
alias math/math_state -> reviewed normalized value + NORMALIZED_FROM_AUTHORED_SOURCE
no source MATH signal -> null + NOT_AUTHORED + ABSENT_IN_SOURCE
```

Synthetic samples may remain as unit tests, but they cannot be the only evidence for migration safety.

## Finding 3 — RMG registry coverage is not yet measured against RMG-GOV-001

The legal RMG registry contains 252 measured records.

Current reported mathematical-contribution coverage:

```text
records with math_contribution_level     72 / 252
records without math_contribution_level 180 / 252
coverage                                approximately 29%
missing                                 approximately 71%
```

The 72 present values were reported as `MATH-M0`. This does not by itself establish whether each was authored, normalized, or generated.

RMG-GOV-001 defines four mandatory governance axes, but the existence of the governing document does not prove that the registry implements it. RMG must undergo the same source-to-contract coverage audit previously applied to TKG.

Required corpus-wide measurement for every legal JSONL record:

```text
assimilation_level: present / absent / alias / invalid vocabulary
math_contribution_level: present / absent / alias / invalid vocabulary
operational_maturity: present / absent / alias / invalid vocabulary
certificate_strength: present / absent / alias / invalid vocabulary
four-axis intersection
value-origin provenance coverage
record-class breakdown
```

The audit must distinguish:

- fields authored directly in the source record;
- fields introduced by a reviewed migration overlay;
- fields generated by an adapter;
- fields absent from both source and overlay.

A repository-wide authority decision cannot rely solely on the RMG governance documents while 71% of measured records lack one of the core axes.

## Registry safety observation

The synthetic markers:

```text
OPS-LEGACY-UNCLASSIFIED
CERT-LEGACY-UNCLASSIFIED
```

were reported absent from legal RMG JSONL records. This is good evidence that those exact generated defaults have not been serialized into the legal registry.

It is not evidence that generated `MATH-M0` values are absent, because `MATH-M0` is not a distinguishable marker.

Thus:

```text
DETECTED OPS/CERT CONTAMINATION = NONE FOUND
MATH DEFAULT CONTAMINATION = NOT AUDITABLE WITH CURRENT PROVENANCE
```

## Required repair sequence

### Gate A — coverage audit

Create a reproducible scanner over the 252 legal RMG records that emits:

- total records;
- record classes;
- per-axis presence counts;
- vocabulary distributions;
- four-axis intersection;
- alias fields;
- source versus overlay provenance where available;
- exact unresolved record identifiers.

The scanner must not mutate records.

### Gate B — adapter provenance repair

Repair `rmg_schema_adapter.py` so that:

- missing governance values remain explicit missing values;
- every axis has value-origin metadata;
- aliases are normalized only through reviewed maps;
- no default legitimate ladder value is inserted for absence;
- `claim_ceiling`, `math`, and `math_state` remain semantically distinct;
- adapter output records its adapter version and mapping decision.

### Gate C — verifier repair

Replace `math_not_auto_promoted` with source-fidelity checks against real records and negative cases.

The repaired verifier must fail when:

- a missing MATH signal becomes `MATH-M0` without authored provenance;
- OPS or CERT absence becomes an apparently authored value;
- a source alias is normalized without a reviewed mapping;
- generated data lacks a generated-value marker;
- source preservation fails.

## TKG compatibility condition

Only after Gates A-C pass may RMG govern a TKG migration operationally.

The TKG migration must then preserve independently:

- `assimilation_level`;
- `math_contribution_level` or reviewed aliases `math` / `math_state`;
- `operational_maturity`;
- `certificate_strength`;
- textual `claim_ceiling` as a separate field;
- source-field and value-origin provenance for each dimension.

The TKG executable vertical slice remains a non-authoritative Family-A prototype. It is not evidence that either TKG or RMG registries are globally execution-ready.

## Scientific and governance ceiling

```text
MATH = MATH-M0
PNT progress = NONE
PNT-AP progress = NONE
Goldbach progress = NONE
RH progress = NONE
GRH progress = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
RMG OPERATIONAL AUTHORITY OVER TKG = PENDING
ADAPTER EXECUTION = BLOCKED
```

## Next authorized deliverable

`RMG-FOUR-AXIS-REGISTRY-COVERAGE-AUDIT-001`

This must be a read-only measurement over the legal RMG registry. Adapter modification may follow only after the coverage report fixes the actual field and vocabulary distributions.