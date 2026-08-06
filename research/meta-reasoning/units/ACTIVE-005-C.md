# ACTIVE-005-C — Governed Error Memory and Correction Ledger

Status: specification complete / implementation not yet built

Classification: Diagnostic

Validation status: architecture_only_unbenchmarked

Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Create a governed error-memory layer for the PVG–ANT Research Mind so that mistakes, failed assumptions, audit findings, and corrective decisions become cumulative project knowledge rather than transient conversation context.

The layer must record not only that an error occurred, but also why it occurred, what it affected, how it was repaired, what generalized rule was learned, and what future checks must prevent recurrence.

## 2. Governing principle

```text
An unrecorded correction is not organizational learning.
A recorded correction without an affected-scope audit is incomplete.
A learned rule without future enforcement is advisory only.
```

## 3. Error classes

The ledger must support at least:

```text
MATHEMATICAL_ERROR
DEFINITION_DRIFT
DOMAIN_MISMATCH
NORMALIZATION_ERROR
ORDERED_UNORDERED_CONFLATION
VALUATION_LINEARIZATION_ERROR
WEIGHT_INTERPRETATION_ERROR
FOURIER_ALIASING_ERROR
RANK_KERNEL_ERROR
CERTIFICATE_GAP
SCIENTIFIC_OVERCLAIM
NOVELTY_OVERCLAIM
STATUS_MISREPORT
GOVERNANCE_BREACH
REGISTRY_DESYNCHRONIZATION
DEPENDENCY_OMISSION
IMPLEMENTATION_BUG
ENVIRONMENT_ERROR
CI_INFRASTRUCTURE_ERROR
DOCUMENTATION_GAP
```

## 4. Canonical error record

Each entry must have this shape:

```text
ERROR_MEMORY_RECORD
- error_id
- detected_at
- source_context
- affected_branch
- affected_commit
- error_class
- severity
- symptom
- false_assumption
- root_cause
- affected_artifacts
- downstream_risk
- immediate_correction
- generalized_rule
- prevention_guard
- validation_performed
- residual_uncertainty
- closure_status
- superseding_record
```

No field may be silently omitted when material. Unknown values must be marked `UNKNOWN`, `NOT_RUN`, or `NOT_APPLICABLE`.

## 5. Severity ladder

```text
S0 — cosmetic only
S1 — local wording or metadata defect
S2 — local reasoning defect without downstream claims
S3 — cross-unit inconsistency or failed guard
S4 — invalid certificate, invalid benchmark state, or merge blocker
S5 — scientific overclaim, hidden-evaluation contamination, or custody breach
```

Severity is determined by consequence, not embarrassment.

## 6. Root-cause taxonomy

The system must distinguish at least:

```text
missing specification
ambiguous input
incorrect inference
incorrect mathematical identity
unstated domain restriction
normalization omitted
registry not updated
workflow assumption invalid
local environment dependency
status copied from stale context
premature promotion of evidence
role separation failure
hidden benchmark exposure
```

## 7. Correction protocol

Every non-cosmetic error passes through:

```text
detect
→ freeze affected claim
→ identify scope
→ repair source artifact
→ inspect dependent artifacts
→ run relevant guards or audits
→ record residual uncertainty
→ close or keep open
```

A correction is not complete merely because one file was edited.

## 8. Generalization rule

For every closed error, derive a reusable prevention rule:

```text
specific correction
→ generalized failure pattern
→ future guard or checklist item
→ affected-scope backfill
```

Example:

```text
specific error:
`python` resolved to a zero-byte WindowsApps stub.

generalized rule:
Never trust an interpreter command name without resolving and executing the candidate binary.

future prevention:
Interpreter resolver validates candidate path, file size, exclusion policy, and version execution before use.
```

## 9. Affected-scope analysis

The ledger must identify:

```text
directly affected files
dependent units
derived artifacts
registries
dashboards
benchmarks
claims
release notes
```

If the project later installs a Research Memory Graph, every error record must be linked to all impacted nodes and edges.

## 10. Confidence interaction

ACTIVE-005-C integrates with ACTIVE-005-B.

Rules:

1. an unresolved material error lowers release confidence;
2. a corrected error does not automatically restore confidence;
3. restoration requires validation evidence appropriate to the defect;
4. repeated recurrence lowers process confidence even if each instance is repaired;
5. unknown affected scope blocks high release confidence.

## 11. Canonical project examples

### Example C1 — PowerShell parser incompatibility

```text
error_class = IMPLEMENTATION_BUG
symptom = local governance runner failed to parse on PowerShell 5.1
root_cause = unsupported or parser-sensitive syntax
correction = rewrite for explicit PowerShell 5.1 compatibility
validation = parser execution and full gate run
```

### Example C2 — WindowsApps Python alias

```text
error_class = ENVIRONMENT_ERROR
symptom = zero-byte python.exe alias intercepted execution
root_cause = reliance on bare `python`
correction = resolve and validate a real interpreter path
validation = Python 3.12.10 executed and governance gate completed
```

### Example C3 — unregistered identifier in an audit file

```text
error_class = REGISTRY_DESYNCHRONIZATION
symptom = registry audit failed
root_cause = prose token matched formal identifier syntax
correction = register legitimately or rewrite as ordinary description
validation = registry sync audit PASS
```

### Example C4 — GitHub Actions billing diagnosis

```text
error_class = STATUS_MISREPORT
symptom = required check described as queued
root_cause = incomplete inspection of job annotations
correction = record failure-before-start due to account billing
validation = direct annotation and run-state inspection
```

## 12. Non-learning boundaries

The system must not:

- treat every disagreement as an error;
- rewrite history to hide incorrect earlier states;
- infer a general law from one accidental failure without justification;
- store hidden benchmark answers in author-visible locations;
- claim autonomous self-improvement merely because an error ledger exists;
- modify scientific claims without an explicit affected-scope audit.

## 13. Closure states

```text
OPEN
CONTAINED
CORRECTED_NOT_REVALIDATED
REVALIDATED
CLOSED_WITH_RESIDUAL_RISK
SUPERSEDED
```

`CLOSED` is not used without revalidation evidence.

## 14. Machine-readable future schema

A future implementation should provide JSONL-compatible records with stable IDs and append-only history. Corrections should supersede prior records rather than erase them.

Suggested prefix:

```text
ERRMEM-PVGANT-###
```

No new live registry identifier is claimed by this specification alone.

## 15. Acceptance criteria

ACTIVE-005-C is specification-complete when:

1. error classes and severity are explicit;
2. every record captures cause, scope, repair, validation, and residual risk;
3. correction cannot close without revalidation;
4. confidence interaction is defined;
5. hidden-evaluation and role-separation risks are protected;
6. no autonomous-learning claim is made.

## 16. Current state

```text
ACTIVE-005-C = SPECIFICATION_COMPLETE
ERROR_LEDGER_SCHEMA = DEFINED
APPEND_ONLY_LEDGER = NOT_BUILT
AUTOMATED_AFFECTED_SCOPE_GRAPH = NOT_BUILT
RECURRENCE_ANALYSIS = NOT_RUN
AUTONOMOUS_LEARNING = NOT_GRANTED
NEXT_ACTION = ACTIVE-005-D
```

## 17. Next action

```text
ACTIVE-005-D
Governed Strategy Planner and Route Selection Layer
```
