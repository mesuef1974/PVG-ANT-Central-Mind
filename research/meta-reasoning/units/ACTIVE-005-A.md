# ACTIVE-005-A — Meta-Reasoning Core for Research Mind 4

Status: architecture specification complete / implementation not yet built
Classification: Diagnostic
Validation status: architecture_only_unbenchmarked
Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Install a governed meta-reasoning layer above the existing knowledge, translation, diagnostic, and certificate systems. The layer does not solve the mathematical problem directly. It reviews how the problem was understood, why a strategy was selected, what information was lost, whether the certificate supports the conclusion, and whether the scientific classification is honest.

The canonical cycle is:

```text
UNDERSTAND
→ PLAN
→ REASON
→ REVIEW
→ JUDGE
→ EXPLAIN
```

## 2. Scope

The meta-reasoning core applies across PVG, analytic number theory, axis addition, Fourier channels, reconstruction, sieve interfaces, operator diagnostics, and certificate governance.

It must not:

- fabricate hidden evaluation success;
- expose sealed benchmark keys;
- invent a proof from a diagnostic;
- replace mathematical proof with confidence language;
- claim self-learning before an audited update mechanism exists.

## 3. Core engines

### 3.1 Understanding review

Checks whether the actual mathematical target was identified.

Required questions:

```text
What is the target object?
What domain is active?
What conclusion is requested?
What fields remain ambiguous?
Was an unstated assumption introduced?
```

### 3.2 Strategy review

Checks the chosen route:

```text
PVG
ANT
HYBRID
LINEAR_ALGEBRA
FOURIER
SIEVE
COF
FORMAL_PROOF
FINITE_COMPUTATION
```

The report must state why the chosen route fits and why materially different alternatives were not selected.

### 3.3 Information-loss review

Every translation is treated as a map with possible loss.

Examples:

- integer fiber to valuation transport may hide additive ordering unless retained explicitly;
- weight vector to modular channel may have a nontrivial kernel;
- full channel to retained frequencies loses omitted modes;
- finite experiments lose all-target control;
- a geometric reinterpretation does not supply analytic error bounds.

### 3.4 Certificate review

Checks whether the evidence matches the requested conclusion.

```text
IDENTITY
FINITE_ENUMERATION
RANK
KERNEL
RECONSTRUCTION
CONDITIONING
ASYMPTOTIC_MAIN_TERM
UNIFORM_ERROR
POSITIVITY
ALL_TARGET
FORMAL_PROOF
EXTERNAL_REVIEW
```

No conclusion may be stronger than its strongest valid certificate.

### 3.5 Classification review

Allowed classes:

```text
Known
Identity
Reinterpretation
Diagnostic
Finite verification
Boundary
Candidate mechanism
Conditional result
Open problem
New theorem
```

`New theorem` requires a proof package and independent review path.

### 3.6 Risk review

Detects overclaim and governance risks:

```text
finite_to_universal
average_to_pointwise
geometry_to_asymptotic
rank_to_stable_reconstruction
Lambda_to_prime_indicator
known_source_to_project_result
private_key_or_hidden_set_exposure
self_certification
```

### 3.7 Explanation generation

Produces a concise public explanation without exposing private chain-of-thought or sealed evaluation content. It reports decisions, evidence, alternatives, and missing certificates rather than hidden scratch work.

## 4. Meta-reasoning report schema

```json
{
  "schema_version": "ACTIVE-005-A-v1",
  "problem_id": "string",
  "understanding": {
    "target": "string",
    "domain": "string",
    "requested_conclusion": "string",
    "ambiguities": [],
    "assumptions": []
  },
  "strategy": {
    "chosen_route": "string",
    "selection_reason": [],
    "alternative_routes": [],
    "rejected_route_reasons": []
  },
  "information_loss": {
    "translations": [],
    "lost_information": [],
    "recoverability_conditions": []
  },
  "certificate_review": {
    "present": [],
    "missing": [],
    "strongest_supported_conclusion": "string"
  },
  "classification_review": {
    "proposed": "string",
    "approved": "string",
    "repair_required": "true|false"
  },
  "risk_review": {
    "risk_flags": [],
    "fatal_flags": [],
    "release_status": "release|repair|block"
  },
  "confidence": {
    "level": "high|medium|low|not_applicable",
    "basis": [],
    "not_a_certificate": true
  },
  "next_missing_step": [],
  "public_explanation": "string"
}
```

## 5. Confidence rule

Confidence is not subjective certainty and is never a substitute for proof.

```text
HIGH = exact identity, verified computation, formal proof, or complete certificate within declared scope
MEDIUM = supported diagnostic with explicit assumptions and known limitations
LOW = incomplete data, ambiguous routing, unverified inference, or missing central certificate
NOT_APPLICABLE = confidence language would be misleading
```

Any theorem-level claim with a missing proof certificate is blocked regardless of confidence.

## 6. Canonical example: N = 24

```text
UNDERSTANDING
- target: unordered prime representations of 24
- applicable: binary Goldbach instance

STRATEGY
- chosen: finite integer fiber + prime indicator
- optional: valuation transport for PVG interpretation
- ANT asymptotics not required for one finite target

INFORMATION LOSS
- unordered normalization identifies symmetric ordered pairs
- valuation transport must retain the source integer pairs

CERTIFICATE
- present: finite enumeration
- missing: all-target analytic certificate

CLASSIFICATION
- finite verification / diagnostic

RISK
- universal Goldbach promotion blocked

PUBLIC EXPLANATION
- 24 has the listed prime decompositions; this verifies only N=24 and is not a proof of Goldbach.
```

## 7. Meta-review of reconstruction

For any reconstruction claim, the layer must ask:

```text
What is the source space?
What is the measurement map?
What is its rank?
What is its kernel?
What normalization is used?
Is the requested recovery exact, modulo kernel, or numerical?
Is conditioning controlled?
```

A full Fourier spectrum of a channel does not by itself imply recovery of the original fiber weight.

## 8. Research Memory Graph interface

ACTIVE-005-A defines the future interface to a Research Memory Graph (RMG).

Node classes:

```text
CONCEPT
THEOREM
IDENTITY
TOOL
SKILL
BOOK
UNIT
CERTIFICATE
WALL
DATASET
BENCHMARK
DECISION
```

Edge classes:

```text
depends_on
translates_to
uses
certifies
blocked_by
refines
contradicts
implements
evaluates
supersedes
```

The RMG is not built by this unit. This unit only specifies that meta-reasoning reports must be able to cite the nodes and edges used in a decision.

## 9. Failure taxonomy

```text
ERR-META-TARGET-MISIDENTIFIED
ERR-META-ASSUMPTION-HIDDEN
ERR-META-ROUTE-UNJUSTIFIED
ERR-META-ALTERNATIVE-NOT-CONSIDERED
ERR-META-INFORMATION-LOSS-OMITTED
ERR-META-CERTIFICATE-MISMATCH
ERR-META-CONFIDENCE-AS-PROOF
ERR-META-SELF-CERTIFICATION
ERR-META-HIDDEN-KEY-EXPOSURE
ERR-META-SCIENTIFIC-OVERCLAIM
```

## 10. Acceptance state

```text
ACTIVE-005-A = ARCHITECTURE_SPECIFICATION_COMPLETE
META_REASONING_ENGINE_CODE = NOT_BUILT
CONFIDENCE_CALIBRATION = NOT_BENCHMARKED
ERROR_MEMORY = NOT_BUILT
STRATEGY_PLANNER = NOT_BUILT
RESEARCH_MEMORY_GRAPH = INTERFACE_ONLY
AUTONOMOUS_LEARNING = NOT_CLAIMED
AUTONOMOUS_SPECIALIST_VALIDATION = NOT_GRANTED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
NEXT_ACTION = ACTIVE-005-B
```
