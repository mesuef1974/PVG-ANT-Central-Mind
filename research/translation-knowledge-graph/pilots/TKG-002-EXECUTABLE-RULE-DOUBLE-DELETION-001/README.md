# TKG-002-EXECUTABLE-RULE-DOUBLE-DELETION-001

Status: `PASS — VERIFIED SINGLE-CONCEPT EXECUTION KERNEL`

Date: 2026-07-17

## Scope

This gate tests whether `tau(360)` can be computed from a reviewed executable contract attached to the authored TKG-002 node, rather than from examples, textual-formula parsing, target-specific branches, or a stored answer.

## Executed tree

```text
replayed_tree_commit = f500511d8ea5aa955d64cc01c65e67c5f392ae35
branch context = agent/pvg-axis-sum-continuation-002
```

The commit SHA is the replay target. The branch name is contextual and may move.

## Implemented artifacts

- `registry/executable/tkg-002-executable-rules-001.jsonl`
- `code/tkg_002_executable_rule_engine_001.py`
- `code/verify_tkg_002_executable_rule_double_deletion_001.py`
- `TKG-002-EXECUTABLE-RULE-CLEAN-CHECKOUT-AND-ADVERSARIAL-REPLAY-001.md`

The descriptive TKG-002 registry remains unchanged. Execution is authorized through a separate reviewed overlay:

```json
{
  "source_node_id": "TKG002-NODE-TAU",
  "executable_rule": {
    "operator_id": "OP-EVALUATE-DIVISOR-SUM-001",
    "args": {"summand": "one"},
    "result_symbol": "tau"
  }
}
```

## Clean-checkout double-deletion replay

The committed verifier was executed from a clean checkout of the pinned tree and exited successfully:

```text
exit_code = 0
baseline tau(360)                         24
examples deleted, executable rule kept   24
executable rule deleted, examples kept   INSUFFICIENT_KNOWLEDGE
engine_contains_case_result               false
provenance                                PASS
```

This closes the original double-deletion gate.

## Independently added unseen-input tests

A separate test implementation evaluated the committed engine on eight inputs not authored in the registry examples or official verifier and compared the results with `sympy.divisor_count`.

Reported examples:

```text
tau(4620)      = 48   PASS
tau(59049)     = 11   PASS
tau(997)       = 2    PASS
tau(1000000)   = 49   PASS
```

These tests establish that the operator contract applies to new positive-integer inputs rather than replaying stored fixture values.

## Adversarial refusal boundary

```text
sigma(12) = INSUFFICIENT_KNOWLEDGE
mu(30)    = INSUFFICIENT_KNOWLEDGE
```

The descriptive presence of sigma and mu nodes does not authorize execution without reviewed `executable_rule` contracts.

## Provenance rule

Every successful step carries exactly one provenance source:

- `source_node_id` for the reviewed executable contract; or
- `operator_id` for mechanical computation.

## Exact claim established

```text
TKG-002 TAU DOUBLE-DELETION GATE = PASS
UNSEEN-INPUT TAU RULE APPLICATION = PASS
MISSING-RULE REFUSAL = PASS
VERIFIED SINGLE-CONCEPT EXECUTION KERNEL = YES
```

This is narrow rule application on one concept through one reviewed operator contract. It is not authorization to call the system a reasoning engine or a mathematical mind.

## Claim boundary

```text
REASONING ENGINE = NOT CLAIMED
GENERAL REASONING LAYER = NOT ESTABLISHED
EXECUTABLE CONCEPTS = TAU ONLY
OPERATOR CONTRACTS VERIFIED = 1
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
```

Every additional concept requires its own reviewed executable rule, contamination audit, unseen-input tests, adversarial refusal checks, provenance validation, and double-deletion gate.
