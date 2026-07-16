# RMG-GOV-007 — Program-Goal Namespace Repair and CI Enforcement Activation

## Scope

This unit executes three concrete repairs:

1. replace bare `maturity_target: L*` values in `registries/program-goals.jsonl` with orthogonal governed targets;
2. add a changed-record schema guard for new or modified RMG registry files;
3. add a semantic completion guard so placeholder-filled records cannot claim high assimilation.

## Program-goal migration

Each goal now separates:

- `assimilation_target = ASSIM-*`;
- `math_contribution_target = MATH-*`;
- `operational_target = OPS-*`;
- `certificate_target = CERT-*`;
- `pvg_necessity_target = PVG-N*`.

No bare `maturity_target` remains in the migrated goal registry.

## CI enforcement

The required governance workflow now runs:

- `tools/rmg_changed_record_policy_audit.py`;
- `tools/rmg_semantic_completion_audit.py`.

The first guard applies only to RMG registry files added or modified relative to `origin/main`, preventing new legacy-schema debt without falsely claiming historical migration.

The second guard rejects an `ASSIM-L3` or higher claim when core semantic fields remain one of:

- `NOT_YET_ANALYSED`;
- `NOT_YET_ANALYZED`;
- `UNMAPPED_LEGACY_VALUE`;
- `AMBIGUOUS_REQUIRES_REVIEW`.

Therefore schema conformance is not treated as semantic completion.

## Honest state

```text
PROGRAM_GOAL_NAMESPACE_REPAIR = COMPLETE
NEW_OR_CHANGED_RMG_RECORD_ENFORCEMENT = WIRED_TO_REQUIRED_WORKFLOW
SEMANTIC_PLACEHOLDER_CEILING = WIRED_TO_REQUIRED_WORKFLOW
HISTORICAL_22_FILE_REGISTRY_MIGRATION = NOT_COMPLETE
HISTORICAL_249_RECORD_COMPLIANCE = NOT_CLAIMED
CI_EXECUTION_RESULT = NOT_CLAIMED_DUE_TO_ACTIONS_BILLING_BLOCK
FULL_REPOSITORY_COMPLIANCE = NOT_CLAIMED
```

## Next action

Execute the canonical migration over the historical RMG registries in bounded batches, preserving IDs, record counts, source fields, and mathematical claim ceilings.
