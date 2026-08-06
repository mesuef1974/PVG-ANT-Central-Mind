# RMG-GOV-007

## Title

Canonical Goal Namespace Repair and CI Enforcement Activation

## Decision

`IMPLEMENTED — PARTIAL REPOSITORY MIGRATION`

## Completed

- migrated `registries/program-goals.jsonl` away from bare `L*` targets;
- separated assimilation, mathematical contribution, operational maturity, certificate strength, and PVG necessity targets;
- added changed-record canonical schema enforcement;
- added semantic completion enforcement;
- wired both guards into the required governance workflow.

## Boundary

This unit prevents new or modified RMG registry records from extending legacy schema debt. It does not claim that all historical registry records have been migrated.

## Claim ceiling

```text
POLICY_IS_NOW_ENFORCED_FOR_CHANGED_RMG_RECORDS
SCHEMA_PASS_DOES_NOT_IMPLY_SEMANTIC_COMPLETION
HISTORICAL_REGISTRY_MIGRATION_REMAINS_OPEN
CI_GREEN_STATUS_IS_NOT_CLAIMED_WHILE_GITHUB_ACTIONS_IS_BILLING_BLOCKED
```

## Next

`RMG-GOV-008 — Historical Canonical Registry Migration Batch 001`
