# RMG-GOV-008 — First Historical Registry Migration Batch

## Scope

This batch migrates two historical RMG registries from the ambiguous legacy schema to the canonical governed schema:

- `weyl-vdc-exponential-sum-minor-arc.jsonl`
- `prime-weighted-exponential-vaughan-major-minor.jsonl`

## Preservation guarantees

- record count preserved: 12 + 12 = 24;
- record identifiers preserved;
- statements and claim ceilings preserved in substance;
- legacy assimilation labels retained in `legacy_assimilation_level`;
- no automatic mathematical promotion;
- every migrated record has `math_contribution_level = MATH-M0`.

## Canonical fields added

- `ant_standard_definition`
- `ant_to_pvg_map`
- `pvg_geometric_object`
- `pvg_to_ant_return_map`
- `translation_type`
- `injectivity_status`
- `kernel_or_information_loss`
- `assimilation_level = ASSIM-*`
- `math_contribution_level = MATH-*`
- `operational_maturity = OPS-*`
- `certificate_strength = CERT-*`
- `claim_ceiling`

## Scientific ceiling

This migration changes schema and governance semantics only. It does not prove new Weyl, van der Corput, Vaughan, Type I, Type II, major-arc, minor-arc, Goldbach, RH, or GRH results.

## Status

```text
BATCH_RECORDS = 24
IDENTIFIERS_PRESERVED = CLAIMED_BY_CONSTRUCTION
MATHEMATICAL_PROMOTION = NONE
HISTORICAL_REGISTRY_MIGRATION = PARTIAL
REPOSITORY_WIDE_MIGRATION = NOT_COMPLETE
VERIFIER_CODE = COMMITTED
VERIFIER_EXECUTION = NOT_CLAIMED
```
