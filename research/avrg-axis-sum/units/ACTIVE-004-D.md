# ACTIVE-004-D — Axis-Addition Executable Schema and Public-Case Harness

Status: specification complete / executable harness contract installed
Classification: Diagnostic
Validation status: public_harness_defined_not_run
Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Translate the reasoning protocol of ACTIVE-004-A, the diagnostic engine of ACTIVE-004-B, and the public benchmark of ACTIVE-004-C into one deterministic executable schema for Mind 3.

This unit defines the machine contract and public-case harness only. It does not create hidden cases, certify autonomous competence, or claim a benchmark score.

## 2. Canonical execution route

```text
INPUT_PACKET
→ NORMALIZE
→ CLASSIFY
→ DETECT_MATHEMATICAL_STATE
→ PLAN_FIBER
→ PLAN_OBSERVABLE
→ ROUTE_PVG_ANT
→ PLAN_CERTIFICATE
→ CHECK_SCIENTIFIC_CEILING
→ EMIT_DIAGNOSIS
→ SCORE_PUBLIC_CASE_IF_REQUESTED
```

No stage may be skipped when its fields affect the conclusion.

## 3. Input schema

```json
{
  "query_id": "string",
  "target_integer": "integer|null",
  "ambient_domain": "positive_integers|nonnegative_integers|integers|primes|prime_powers|custom|unspecified",
  "order_mode": "ordered|unordered|unspecified",
  "representation_target": "general|prime_pair|goldbach|weighted|channel|fourier|reconstruction|certificate|unspecified",
  "weight": "unit|prime_indicator|von_mangoldt|custom|unspecified",
  "modulus": "positive_integer|null",
  "requested_observable": "fiber|count|channel|spectrum|rank|kernel|reconstruction|asymptotic|unspecified",
  "target_claim": "identity|finite_computation|reconstruction|asymptotic|positivity|all_target|theorem|unspecified"
}
```

Malformed or materially ambiguous fields must be surfaced as errors or `UNSPECIFIED`; they must not be silently invented.

## 4. Output schema

```json
{
  "schema_version": "ACTIVE-004-D-v1",
  "query_id": "string",
  "problem_class": "string",
  "secondary_flags": [],
  "applicability": "applicable|not_applicable|underspecified",
  "mathematical_state": {
    "parity": "even|odd|unknown",
    "positive": "true|false|unknown",
    "goldbach_applicable": "true|false|unknown",
    "fiber_status": "finite|empty|infinite|unknown"
  },
  "fiber_plan": {
    "definition": "string",
    "order_mode": "ordered|unordered|unspecified",
    "valuation_transport": "required|optional|not_required",
    "warning": "integer_relation_first"
  },
  "observable_plan": {
    "weight": "string",
    "prime_power_contamination": "present|absent|not_applicable|unknown"
  },
  "channel_plan": {
    "modulus": "integer|null",
    "effective_period": "integer|null",
    "fourier_normalization": "string|null"
  },
  "reasoning_route": "PVG|ANT|HYBRID|LINEAR_ALGEBRA|COF|FINITE",
  "certificate": {
    "present": [],
    "missing": [],
    "rank_status": "known|unknown|not_applicable",
    "kernel_status": "known|unknown|not_applicable",
    "reconstruction_status": "exact|modulo_kernel|denied|conditional|not_requested"
  },
  "claim_classification": "Known|Identity|Reinterpretation|Diagnostic|Finite verification|Boundary|Candidate mechanism|Open problem|New theorem",
  "scientific_ceiling": [],
  "fatal_errors": [],
  "final_answer": "string"
}
```

## 5. Deterministic rules

1. For ordinary addition, never compute `nu(a+b)` by coordinatewise addition of `nu(a)` and `nu(b)`.
2. For binary Goldbach applicability, require even `N >= 4`.
3. `Lambda` is not a pure prime indicator; prime powers contribute.
4. For modulus `r`, compute `q(r)=r/gcd(2,r)` before channel-independence claims.
5. Full Fourier recovery reconstructs the effective channel vector only; recovery of the original weight still requires an injective channel operator.
6. No reconstruction verdict is `exact` before rank and kernel are known.
7. Finite verification never becomes an all-target theorem.
8. A fixed-fiber symmetric phase `e(alpha a)e(alpha(N-a))` is constant and not a discriminator.

## 6. Public-case harness contract

The harness consumes the twelve public cases frozen in ACTIVE-004-C. For each case it must:

```text
load prompt
→ produce output schema
→ validate required fields
→ check fatal errors
→ score seven dimensions on {0,1,2}
→ write immutable case receipt
```

Maximum score per case: 14.

Pass condition:

```text
TOTAL_SCORE >= 85 percent
AND NO_FATAL_ERROR
AND SCIENTIFIC_CEILING_SCORE = 2 FOR EVERY CASE
```

## 7. Public harness receipt

A run receipt must record:

```text
run_id
commit_sha
schema_version
case_set_hash
interpreter_or_model_identifier
environment
start_time
end_time
case_scores
fatal_errors
total_score
pass_or_fail
```

No score may be recorded without these fields.

## 8. Role separation

The public harness may be authored and inspected on the research branch. Hidden prompts, hidden scoring keys, and isolated adjudication remain outside this unit.

```text
PUBLIC_HARNESS = AUTHOR_VISIBLE
HIDDEN_CASES = OUTSIDE_AUTHOR_PATH
HIDDEN_KEY = SEALED
AUTONOMOUS_VALIDATION = NOT_GRANTED
```

## 9. Failure taxonomy

```text
ERR-A004D-SCHEMA-MISSING-FIELD
ERR-A004D-AMBIGUOUS-INPUT-SILENTLY-INFERRED
ERR-A004D-VALUATION-LINEARIZATION
ERR-A004D-LAMBDA-MISCLASSIFICATION
ERR-A004D-EFFECTIVE-PERIOD-OMITTED
ERR-A004D-RECONSTRUCTION-WITHOUT-KERNEL
ERR-A004D-CHANNEL-TO-WEIGHT-CONFLATION
ERR-A004D-FINITE-TO-UNIVERSAL-PROMOTION
ERR-A004D-GOLDBACH-OVERCLAIM
ERR-A004D-HIDDEN-BENCHMARK-FABRICATION
```

## 10. Acceptance state

```text
ACTIVE-004-D = SPECIFICATION_COMPLETE
EXECUTABLE_SCHEMA = DEFINED
PUBLIC_CASE_HARNESS_CONTRACT = DEFINED
PUBLIC_HARNESS_CODE = NOT_BUILT
PUBLIC_RUN = NOT_PERFORMED
HIDDEN_CASES = NOT_AUTHORED_HERE
AUTONOMOUS_SPECIALIST_VALIDATION = NOT_GRANTED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
NEXT_ACTION = ACTIVE-005-A
```
