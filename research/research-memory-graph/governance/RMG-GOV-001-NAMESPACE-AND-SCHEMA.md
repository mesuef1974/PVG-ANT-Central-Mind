# RMG-GOV-001 — Namespace Separation and Canonical Schema

Status: `implemented_specification / migration_not_yet_executed`

## Purpose

Prevent collisions between mathematical depth, assimilation, operational maturity, and certificate strength.

## Canonical namespaces

### Assimilation

`ASSIM-L0` mentioned
`ASSIM-L1` defined in ANT
`ASSIM-L2` translated to PVG
`ASSIM-L3` bidirectionally analysed
`ASSIM-L4` numerically verified
`ASSIM-L5` regression tested
`ASSIM-L6` formally verified
`ASSIM-L7` benchmarked for reasoning

### Mathematical contribution depth

`MATH-M0` no mathematical contribution claim
`MATH-M1` classical restatement
`MATH-M2` verified reinterpretation or transfer
`MATH-M3` PVG-generated diagnostic or observable
`MATH-M4` new theorem candidate pending prior-art audit
`MATH-M5` original theorem with independent proof and novelty audit

### Operational maturity

`OPS-DISCUSSION`, `OPS-SPECIFIED`, `OPS-IMPLEMENTED`, `OPS-REGRESSION-TESTED`, `OPS-PRODUCTION-READY`

### Certificate strength

`CERT-UNVERIFIED`, `CERT-FINITE`, `CERT-REGRESSION`, `CERT-FORMAL`, `CERT-INDEPENDENT-REVIEW`, `CERT-PEER-REVIEWED`

Bare `L0..L7` labels are deprecated in new RMG records.

## Canonical concept record

Every new or migrated concept record must expose:

- `id`
- `name`
- `ant_standard_definition`
- `equivalent_forms`
- `hypotheses`
- `examples`
- `counterexamples`
- `related_results`
- `ant_to_pvg_map`
- `pvg_geometric_object`
- `pvg_to_ant_return_map`
- `translation_type`
- `injectivity_status`
- `surjectivity_status`
- `kernel_or_information_loss`
- `preserved_information`
- `lost_information`
- `computational_realization`
- `numerical_evidence`
- `formalization_status`
- `assimilation_level`
- `math_contribution_level`
- `operational_maturity`
- `certificate_strength`
- `provenance`
- `claim_ceiling`

Missing fields must be explicit using `NOT_APPLICABLE`, `NOT_YET_ANALYSED`, or `ABSENT`; silent omission is forbidden.

## Adapter rule

Legacy fields such as `ant_view`, `pvg_view`, and `inverse_status` remain readable only through a documented adapter. They are not canonical write fields after this unit.

## Supersession rule

No charter, standard, or maturity ladder is treated as superseded merely by chronology. A separate supersession ledger must name the active authority and retained clauses.
