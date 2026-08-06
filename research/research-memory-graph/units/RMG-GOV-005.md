# RMG-GOV-005

Title: Source-Locator Resolution, Prior-Art Citation Queue, and Governed Source-File Migration Plan

Status: COMPLETE_AS_GOVERNANCE_UNIT

## Deliverables

- source-locator resolution protocol;
- five-item prior-art citation queue;
- governed source-file migration plan;
- static verifier.

## Decisions

1. Source location and novelty evidence are separate dimensions.
2. Unverified prior art remains explicitly `UNVERIFIED`.
3. Historical source files are not modified until exact path, section, and blob SHA are resolved.
4. Bulk automatic rewriting of mathematical claims is prohibited.
5. Goldbach, RH, and GRH translations retain conservative claim ceilings.
6. Computation and regression cannot raise mathematical contribution level.

## Honest state

```text
SOURCE_LOCATOR_PROTOCOL = ACTIVE
PRIOR_ART_QUEUE = OPEN
SOURCE_FILE_MIGRATION = NOT_STARTED
VERIFIER_CODE = COMMITTED
VERIFIER_EXECUTION = NOT_CLAIMED
REPOSITORY_WIDE_PRIOR_ART_AUDIT = NOT_COMPLETE
FULL_COMPLIANCE = NOT_CLAIMED
```

## Next action

`RMG-GOV-006`: exact source resolution and first governed source-file migration for one P0 claim.
