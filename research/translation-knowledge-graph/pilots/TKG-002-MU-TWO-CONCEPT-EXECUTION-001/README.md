# TKG-002-MU-TWO-CONCEPT-EXECUTION-001

Status: `IMPLEMENTED / COMMITTED / PINNED CLEAN-CHECKOUT REPLAY PENDING`

Date: 2026-07-17

## Scope

This gate tests whether the verified TKG-002 tau kernel can be extended with a mathematically different Mobius operator while preserving correct multi-rule routing, bidirectional rule isolation, and truthful provenance.

It does not authorize a general reasoning-engine claim.

## Architectural finding

The pre-mu engine constructed tau-shaped steps centrally:

- factor the integer;
- enumerate divisors;
- execute the selected operator.

That structure would have produced false provenance for Mobius evaluation because Mobius uses factor exponents, squarefreeness, and support parity rather than divisor enumeration.

The engine was therefore refactored so that every reviewed operator returns its own result and its own operator-provenance steps. The framework retains only:

- query parsing;
- rule selection by `result_symbol`;
- source-node validation;
- reviewed operator dispatch;
- composition of the source-contract step with operator-declared steps.

## Committed artifacts

- `code/tkg_002_executable_rule_engine_001.py`
- `registry/executable/tkg-002-executable-rules-001.jsonl`
- `code/verify_tkg_002_mu_two_concept_execution_001.py`

The descriptive source node `TKG002-NODE-MU` was not modified.

## Reviewed Mobius contract

```json
{
  "rule_id": "TKG002-EXEC-MU-001",
  "source_node_id": "TKG002-NODE-MU",
  "executable_rule": {
    "operator_id": "OP-EVALUATE-MOBIUS-001",
    "args": {},
    "result_symbol": "mu"
  }
}
```

The operator implements the finite rule:

```text
factor n
if any exponent is greater than one:
    return 0
otherwise:
    return -1 for odd support cardinality and 1 for even support cardinality
```

No special branch exists for `n=1`; the empty factorization has support cardinality zero and is tested explicitly.

## Ten-part gate

1. Parse every physical registry and executable-rule JSONL record.
2. Review the mu executable-rule contract.
3. Review the new operator, including domain, branches, `n=1`, codomain, failure behavior, and provenance.
4. Run structural contamination checks.
5. Test every logical branch and value.
6. Test the codomain over a wider range.
7. Test tau/mu coexistence and `result_symbol` routing.
8. Test bidirectional rule isolation.
9. Test exactly-one-source provenance and double deletion.
10. Replay from a pinned clean checkout of the committed tree.

## Required branch cases

```text
mu(1)  = 1
mu(6)  = 1
mu(30) = -1
mu(12) = 0
```

These values occur in authored examples and are branch-coverage cases, not unseen-input evidence.

## Unseen-input cases in the committed verifier

The verifier additionally uses example-input values absent from all TKG-002 `examples` arrays:

```text
mu(10)     = 1
mu(105)    = -1
mu(18)     = 0
mu(510510) = -1
mu(2)      = -1
mu(4)      = 0
mu(988027) = 1
```

The verifier also checks that the observed values on `1..2000` are exactly `{-1,0,1}`. Codomain testing is supplementary and does not replace branch-and-value testing.

## Routing and isolation requirements

With both rules present:

```text
tau(360) = 24
mu(12)   = 0
```

Deleting only the mu contract must yield:

```text
mu(12)   = INSUFFICIENT_KNOWLEDGE
tau(360) = 24
```

Deleting only the tau contract must yield:

```text
tau(360) = INSUFFICIENT_KNOWLEDGE
mu(12)   = 0
```

This detects broken `result_symbol` routing and hidden dependence on rule order.

## Provenance boundary

Every successful step must carry exactly one of:

- `source_node_id` for the reviewed executable contract;
- `operator_id` for mechanical computation.

Mobius execution must not report divisor enumeration. Tau now reports the more precise final step `Count divisors`; this is an intentional provenance-text correction. Its numeric result, rule selection, step count, and exactly-one-source invariant are intended to remain stable.

## Prior isolated-box evidence

Before these GitHub commits were created, an isolated working-box implementation was reported to pass:

- all ten gates;
- comparison against `sympy.mobius` on unseen inputs and on `1..2000`;
- the official tau verifier after the engine refactor.

That evidence motivated this implementation but does not close the committed-tree gate because the committed files were reconstructed and must be replayed from their own fixed SHA.

## Required committed-tree replay

Run from a clean checkout of the final committed SHA:

```text
python research/translation-knowledge-graph/code/verify_tkg_002_executable_rule_double_deletion_001.py
python research/translation-knowledge-graph/code/verify_tkg_002_mu_two_concept_execution_001.py
```

The gate may be closed only if both commands exit zero and the executed tree SHA is recorded.

## Claim boundary

Until the pinned replay passes:

```text
VERIFIED CONCEPTS = {tau}
MU IMPLEMENTATION = COMMITTED, NOT YET VERIFIED ON COMMITTED SHA
TWO-CONCEPT EXECUTION FRAMEWORK = CANDIDATE
GENERAL REASONING ENGINE = NOT AUTHORIZED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
BENCHMARK SEALED = NO
MERGE TO MAIN = NOT AUTHORIZED
```
