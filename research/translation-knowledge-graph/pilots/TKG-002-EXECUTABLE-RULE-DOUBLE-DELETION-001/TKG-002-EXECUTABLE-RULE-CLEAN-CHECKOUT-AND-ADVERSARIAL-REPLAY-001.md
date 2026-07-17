# TKG-002-EXECUTABLE-RULE-CLEAN-CHECKOUT-AND-ADVERSARIAL-REPLAY-001

Status: `PASS — SINGLE-CONCEPT EXECUTION KERNEL VERIFIED`

Date: 2026-07-17

## Executed tree

```text
repository = mesuef1974/PVG-ANT-Central-Mind
branch context = agent/pvg-axis-sum-continuation-002
replayed_tree_commit = f500511d8ea5aa955d64cc01c65e67c5f392ae35
```

The commit SHA, not the moving branch name, is the replay target.

## Official verifier replay

The committed verifier was executed from a clean checkout of the pinned tree.

Reported result:

```text
exit_code = 0
baseline tau(360) = 24
delete examples, keep executable_rule = 24
delete executable_rule, keep examples = INSUFFICIENT_KNOWLEDGE
engine_contains_case_result = false
provenance = PASS
```

This closes the double-deletion gate for the reviewed executable rule attached to `TKG002-NODE-TAU`.

## Independently added unseen-value tests

A separate test implementation evaluated the committed engine on values not authored in the TKG-002 examples and not listed in the official verifier. Results were compared against `sympy.divisor_count`.

Reported examples include:

```text
tau(4620) = 48       PASS
tau(59049) = 11      PASS
tau(997) = 2         PASS
tau(1000000) = 49    PASS
```

Eight independently selected values were reported as matching the external reference calculation.

The exact scientific claim supported is that the generic factorization and divisor-enumeration operators apply the reviewed tau rule to new positive-integer inputs. This is not a lookup-table result.

## Adversarial refusal tests

The same engine was queried for concepts present in the descriptive registry but lacking reviewed executable rules.

```text
sigma(12) = INSUFFICIENT_KNOWLEDGE
mu(30) = INSUFFICIENT_KNOWLEDGE
```

This verifies the intended refusal boundary: descriptive registry presence alone does not authorize execution.

## Provenance

Every successful execution step carries exactly one provenance source:

- `source_node_id` for the reviewed executable contract;
- `operator_id` for mechanical computation.

No step carries both or neither.

## Exact claim established

```text
TKG-002 TAU EXECUTABLE_RULE DOUBLE-DELETION GATE = PASS
UNSEEN-INPUT RULE APPLICATION FOR TAU = PASS
MISSING-RULE REFUSAL = PASS
SINGLE-CONCEPT EXECUTION KERNEL = VERIFIED
```

This is rule application in the narrowest operational sense: a reviewed general rule is loaded from data, applied to a new input by generic operators, and refused when the rule is absent.

## Claims not established

This result does not establish:

- a general reasoning engine;
- a multi-concept reasoning layer;
- semantic understanding;
- transfer to sigma, mu, Lambda, or other TKG nodes;
- policy transfer to RMG;
- theorem discovery;
- mathematical progress.

Each additional executable concept requires its own authored rule contract, contamination audit, unseen-input tests, adversarial refusal tests, provenance verification, and double-deletion gate.

## Current scientific boundary

```text
reasoning_claim = NOT_AUTHORIZED
classification = VERIFIED_SINGLE-CONCEPT_EXECUTION_KERNEL
implemented concept = tau only
implemented reviewed operator contract = OP-EVALUATE-DIVISOR-SUM-001 / summand=one
MATH = MATH-M0
PNT / PNT-AP / Goldbach / RH / GRH progress = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
```
