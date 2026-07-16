# RMG-GOV-009 — Guard Correction and Honest Migration Semantics

## Decision

`IMPLEMENTED / EXECUTION NOT CLAIMED`

## Trigger

Adversarial review found three content failures after CI wiring:

1. `research_compass_audit.py` still required deprecated `maturity_target`.
2. changed-record enforcement compared against `origin/main`, where the entire RMG is absent, so all historical records were treated as newly changed.
3. semantic placeholder detection compared `str(dict)` against scalar placeholder tokens, allowing structured adapter placeholders to escape.

## Repairs

### Program-goal consumer repair

`tools/research_compass_audit.py` now requires:

- `assimilation_target`
- `math_contribution_target`
- `operational_target`
- `certificate_target`
- `pvg_necessity_target`

It rejects deprecated `maturity_target` and validates namespace prefixes.

### Enforcement activation anchor

Both RMG guards now compare changes against the governance activation commit:

`78ed2fa1da04ceb55fc50a03688842cb90466da3`

The anchor may be overridden by `RMG_POLICY_BASE_REF`.

This means:

- records existing before activation remain explicit migration debt;
- records added or modified after activation must satisfy the canonical policy;
- migrated historical files become governed when modified;
- the guard does not falsely claim that the entire unmerged RMG is new.

### Structured placeholder normalization

`tools/rmg_semantic_completion_audit.py` now descends into dictionaries and lists and extracts `status`, `value`, or `classification` before placeholder comparison.

Therefore values such as:

```json
{"status":"NOT_YET_ANALYSED"}
```

are treated as unresolved.

## Migration rule clarified

Mechanical migration must not preserve a legacy `L3+` label as `ASSIM-L3+` when canonical semantic fields remain unresolved.

Permitted outcomes are:

1. complete the semantic analysis honestly; or
2. assign at most `ASSIM-L2` while unresolved fields remain explicit.

No adapter or regression evidence may promote `MATH-*`.

## Honest state

```text
PROGRAM_GOAL_DATA_MIGRATION = COMPLETE
PROGRAM_GOAL_CONSUMER_REPAIR = IMPLEMENTED
CHANGED_RECORD_SCOPE_REPAIR = IMPLEMENTED
STRUCTURED_PLACEHOLDER_REPAIR = IMPLEMENTED
HISTORICAL_REGISTRY_MIGRATION = PARTIAL
LOCAL_FULL_GATE_EXECUTION = NOT_CLAIMED
CI_GREEN = NOT_CLAIMED
BILLING_ONLY_BLOCKER = NOT_CLAIMED
```

Until the full required gate is executed successfully, content failures remain possible and billing must not be described as the sole blocker.
