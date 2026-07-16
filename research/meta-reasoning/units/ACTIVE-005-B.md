# ACTIVE-005-B — Evidence-Calibrated Confidence System

Status: specification complete / implementation not yet built

Classification: Diagnostic

Validation status: architecture_only_unbenchmarked

Depends on: `ACTIVE-005-A`, `ACTIVE-004-A..D`

## 1. Mission

Build a confidence system for Research Mind 4 in which confidence is determined by evidence and certificate strength, not by rhetorical fluency, number of examples, or internal familiarity.

The system must answer separately:

```text
How confident are we that the object was understood correctly?
How confident are we that the computation is correct?
How confident are we that the representation route is appropriate?
How confident are we that the available certificate supports the claim?
How confident are we in any novelty or publication-level statement?
```

These are not one scalar by default.

## 2. Governing principle

```text
confidence cannot exceed certificate strength
```

More precisely, the released confidence for a claim is bounded by the weakest load-bearing component:

```text
released_confidence
<= min(
  problem_understanding,
  representation_validity,
  derivation_validity,
  evidence_quality,
  certificate_adequacy,
  classification_reliability
)
```

This is an architectural rule, not yet a calibrated probabilistic theorem.

## 3. Confidence vector

Every governed answer must be able to emit:

```text
CONFIDENCE_VECTOR
- understanding_confidence
- representation_confidence
- computation_confidence
- route_confidence
- certificate_confidence
- classification_confidence
- novelty_confidence
- publication_readiness_confidence
- overall_release_confidence
```

A field must be `NOT_ASSESSED` when no defensible estimate exists.

## 4. Evidence classes

Evidence is classified before confidence is assigned:

```text
E0 = unsupported assertion
E1 = heuristic or analogy
E2 = finite example or exploratory computation
E3 = reproducible finite computation with exact inputs
E4 = exact identity or proved finite theorem
E5 = established external theorem with verified hypotheses
E6 = project proof package independently audited
E7 = formal proof or equivalent highest-assurance certificate within declared scope
```

The scale is ordinal. It must not be interpreted as a numerical probability without a separate calibration study.

## 5. Claim classes and confidence ceilings

### Finite computation

A reproducible finite computation may receive high computation confidence for the tested instance. It receives no universal confidence outside the tested domain.

### Exact identity

An exact derivation with checked hypotheses may receive high identity confidence. It does not automatically grant novelty confidence.

### Reconstruction claim

Confidence is capped until rank, kernel, normalization, and retained measurements are certified. Numerical recovery additionally requires conditioning evidence.

### Asymptotic claim

Confidence is capped until a main-term certificate, error estimate, domain of validity, and uniformity conditions are identified.

### Goldbach-facing claim

A finite verified decomposition supports confidence only for that target. Universal or all-large-even confidence remains blocked without an all-target analytic certificate.

### Novelty claim

Novelty confidence remains low or `NOT_ASSESSED` without a literature and priority certificate. Mathematical correctness does not imply novelty.

### Publication readiness

Publication-readiness confidence is independent of local mathematical plausibility and requires governance, source, proof, exposition, reproducibility, and scope review.

## 6. Confidence labels

The default release labels are:

```text
VERY_LOW
LOW
MODERATE
HIGH
VERY_HIGH
NOT_ASSESSED
BLOCKED_BY_MISSING_CERTIFICATE
```

Labels must be accompanied by reasons. Numeric percentages are prohibited until empirical calibration is performed.

## 7. Downgrade rules

Confidence must be downgraded when any of the following occurs:

```text
material input field inferred rather than stated
multiple plausible problem interpretations remain
representation loses information relevant to the claim
route choice is not compared with alternatives
rank or kernel is unknown in a reconstruction problem
finite evidence is used for an unbounded claim
external theorem hypotheses are not checked
source provenance is incomplete
novelty has not been searched or certified
hidden benchmark has not been run
```

## 8. Fatal confidence errors

```text
ERR-CONFIDENCE-RHETORICAL-INFLATION
ERR-CONFIDENCE-FINITE-TO-UNIVERSAL
ERR-CONFIDENCE-CERTIFICATE-CEILING-BREACH
ERR-CONFIDENCE-NOVELTY-WITHOUT-SEARCH
ERR-CONFIDENCE-PUBLICATION-WITHOUT-GOVERNANCE
ERR-CONFIDENCE-RECONSTRUCTION-WITHOUT-KERNEL
ERR-CONFIDENCE-AUTONOMY-WITHOUT-LOCKED-EVAL
ERR-CONFIDENCE-SINGLE-SCALAR-COLLAPSE
```

A fatal confidence error blocks release of a theorem-level or capability-level claim.

## 9. Meta-reasoning integration

ACTIVE-005-A produces a reasoning audit. ACTIVE-005-B consumes that audit and records:

```text
load_bearing_steps
supporting_evidence_per_step
weakest_step
missing_certificate
alternative_interpretations
confidence_downgrades
release_decision
```

The system must explain why the overall confidence is lower than any strong local component.

## 10. Canonical examples

### Example B1 — `24=5+19`

```text
computation_confidence = VERY_HIGH
scope = this finite target only
Goldbach_universal_confidence = BLOCKED_BY_MISSING_CERTIFICATE
novelty_confidence = NOT_ASSESSED
```

### Example B2 — full Fourier inversion of a channel

If all effective frequencies and normalization are known:

```text
channel_recovery_confidence = HIGH or VERY_HIGH
original_weight_recovery_confidence = BLOCKED_BY_MISSING_CERTIFICATE
```

until the channel operator kernel is checked.

### Example B3 — clean PVG reformulation of an ANT problem

```text
representation_confidence = HIGH
asymptotic_conclusion_confidence = LOW or BLOCKED
```

when no analytic error estimate has been supplied.

## 11. Output schema

```text
EVIDENCE_CALIBRATED_CONFIDENCE_REPORT
  claim_id
  claim_text
  claim_class
  scope
  load_bearing_steps
  evidence_class_per_step
  weakest_step
  missing_certificate
  understanding_confidence
  representation_confidence
  computation_confidence
  route_confidence
  certificate_confidence
  classification_confidence
  novelty_confidence
  publication_readiness_confidence
  overall_release_confidence
  release_decision
  explanation
```

## 12. Acceptance criteria

ACTIVE-005-B is specification-complete when:

1. confidence is vector-valued rather than a single unsupported scalar;
2. every confidence label is tied to evidence and scope;
3. certificate ceilings are explicit;
4. finite and universal confidence are separated;
5. novelty and publication readiness are separately governed;
6. fatal confidence errors are defined;
7. no empirical calibration success is claimed.

## 13. Honest current state

```text
ACTIVE-005-B = SPECIFICATION_COMPLETE
CONFIDENCE_ENGINE_CODE = NOT_BUILT
NUMERICAL_CALIBRATION = NOT_PERFORMED
PUBLIC_TESTS = NOT_BUILT
LOCKED_EVALUATION = NOT_RUN
AUTONOMOUS_CALIBRATION = NOT_GRANTED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
NEXT_ACTION = ACTIVE-005-C
TITLE = Governed Error Memory and Correction Ledger
```
