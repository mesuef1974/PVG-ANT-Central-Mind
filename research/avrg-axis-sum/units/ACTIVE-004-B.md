# ACTIVE-004-B — Axis Addition Diagnostic Engine

Status: specification complete / implementation not yet built
Classification: Diagnostic
Validation status: architecture_only_unbenchmarked

## 1. Mission

Convert the axis-addition specialist capability from a stored theory package into a governed diagnostic engine that classifies a new problem before calculation, chooses the correct mathematical carrier and observable, routes between PVG and analytic number theory, requests the needed certificate, and enforces the scientific ceiling.

This unit depends on `ACTIVE-004-A`, which fixed the seven-layer specialist reasoning protocol.

## 2. Governing principle

The engine must not begin by computing a representation. It must first determine what kind of question has been asked and what evidence would count as an answer.

The canonical route is:

```text
problem classification
→ mathematical state detection
→ fiber planning
→ observable planning
→ PVG/ANT translation planning
→ certificate planning
→ scientific ceiling check
→ governed answer
```

## 3. Input contract

The diagnostic engine accepts a problem packet with the following fields when available:

```text
target_integer
ambient_domain
order_mode
representation_target
weight_request
modulus
channel_request
Fourier_request
reconstruction_request
asymptotic_request
Goldbach_request
certificate_request
```

Missing fields are not silently invented. The engine must either infer them from an explicit mathematical statement or mark them `UNSPECIFIED`.

## 4. Layer A — Problem classification

Every query is assigned one primary class and zero or more secondary classes.

Primary classes:

```text
GENERAL_ADDITIVE_REPRESENTATION
PRIME_REPRESENTATION
GOLDBACH_DIAGNOSTIC
WEIGHTED_ADDITIVE_OBSERVABLE
RESIDUE_CHANNEL_ANALYSIS
FOURIER_CHANNEL_ANALYSIS
RANK_KERNEL_ANALYSIS
RECONSTRUCTION_PROBLEM
CERTIFICATE_OPTIMIZATION
ASYMPTOTIC_TRANSFER
```

Secondary flags:

```text
ORDERED
UNORDERED
WEIGHTED
UNWEIGHTED
FINITE
ASYMPTOTIC
PVG_ONLY
ANT_ONLY
HYBRID_PVG_ANT
```

The classifier must reject category collapse. For example, `PRIME_REPRESENTATION` is not automatically `GOLDBACH_DIAGNOSTIC`; Goldbach additionally requires an even target at least four and an all-target or specified-target logical interpretation.

## 5. Layer B — Mathematical state detection

For a target integer `N`, the engine records at minimum:

```text
N_is_integer
N_positive
N_parity
N_size_class
N_prime_or_composite_if_needed
Goldbach_applicable
fiber_nonempty
```

Goldbach applicability rule:

```text
Goldbach_applicable = TRUE only if N is even and N >= 4.
```

This is an applicability flag, not a truth certificate for the conjecture.

The engine must distinguish:

```text
question not applicable
question applicable but unresolved in general
specific finite instance verified
general theorem available
```

## 6. Layer C — Fiber planner

The planner selects the exact carrier before any valuation geometry is introduced.

Ordered fiber:

\[
\mathcal F_N^{\mathrm{ord}}=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}.
\]

Unordered fiber:

\[
\mathcal F_N^{\mathrm{unord}}=\{\{a,b\}:a+b=N,\ a\le b\}.
\]

Valuation transport:

\[
\mathcal G_N=\{(\nu(a),\nu(b)):(a,b)\in\mathcal F_N\}.
\]

Mandatory rule:

```text
integer relation first
valuation transport second
```

Forbidden substitution:

```text
nu(a+b) = nu(a)+nu(b)
```

unless an independent statement proves such an identity in a special case. Prime-valuation coordinates linearize multiplication, not ordinary addition.

## 7. Layer D — Observable planner

The planner chooses the observable by target class.

### 7.1 Counting observable

For general additive representation:

\[
r_w(N)=\sum_{a+b=N} w(a,b).
\]

With unit weight, this is the fiber count.

### 7.2 Prime-indicator observable

For exact prime-pair counting, an explicit prime indicator may be used:

\[
\sum_{a+b=N}1_{\mathbb P}(a)1_{\mathbb P}(b).
\]

### 7.3 von Mangoldt observable

For analytic number theory transfer:

\[
R_\Lambda(N)=\sum_{a+b=N}\Lambda(a)\Lambda(b).
\]

The engine must state that `\Lambda` detects prime powers, not only primes.

### 7.4 Channel observable

For modulus `r`:

\[
(D_{N,r}w)_d=\sum_{2a-N\equiv d\pmod r}w_a.
\]

Effective period:

\[
q(r)=\frac{r}{\gcd(2,r)}.
\]

The planner must reduce channel independence to the effective period before rank or reconstruction claims.

## 8. Layer E — PVG/ANT translation planner

The engine chooses one of three routes.

### Route P — PVG-primary

Use when the task is principally about:

```text
valuation support
prime-power loci
geometric organization of fiber points
support or height diagnostics
finite valuation transport
```

### Route A — ANT-primary

Use when the task is principally about:

```text
weighted convolution
Dirichlet characters
circle method
major/minor arcs
asymptotic main terms
error bounds
positivity for all large targets
```

### Route H — Hybrid

Use when geometry is used to organize the additive fiber but the certificate requires analytic estimates.

Canonical declaration:

```text
GEOMETRY organizes the object.
ANALYSIS supplies asymptotic control.
CERTIFICATE determines what may be claimed.
```

The engine must not claim that a geometric reformulation alone resolves an analytic wall.

## 9. Layer F — Certificate planner

The engine identifies the exact certificate required by the requested conclusion.

Certificate ladder:

```text
IDENTITY_CERTIFICATE
FINITE_ENUMERATION_CERTIFICATE
CHANNEL_RANK_CERTIFICATE
KERNEL_CERTIFICATE
EXACT_RECONSTRUCTION_CERTIFICATE
STABILITY_CONDITIONING_CERTIFICATE
ASYMPTOTIC_MAIN_TERM_CERTIFICATE
UNIFORM_ERROR_CERTIFICATE
POSITIVITY_CERTIFICATE
ALL_TARGET_CERTIFICATE
```

Examples:

- A complete finite fiber listing requires a finite enumeration certificate.
- Recovery of arbitrary weights from channel data requires rank and kernel certificates.
- Stable numerical recovery additionally requires conditioning control.
- A Goldbach conclusion for all sufficiently large even integers requires an asymptotic main term, a uniform error smaller than the main term, and positivity.
- A finite verification up to `X` is not an all-target certificate.

Mandatory output fields:

```text
certificate_present
certificate_missing
conclusion_supported
conclusion_not_supported
```

## 10. Layer G — Scientific ceiling detector

Before release, the engine checks the proposed answer against the following walls.

```text
NO_GOLDBACH_PROOF_FROM_FINITE_DATA
NO_RH_OR_GRH_PROGRESS_CLAIM
NO_ASYMPTOTIC_FROM_RANK_ALONE
NO_RECONSTRUCTION_WITHOUT_KERNEL_CHECK
NO_PRIME_ONLY_INTERPRETATION_OF_VON_MANGOLDT
NO_HISTORICAL_NOVELTY_CLAIM_WITHOUT_LITERATURE_CERTIFICATE
NO_AUTONOMOUS_SPECIALIST_VALIDATION_WITHOUT_LOCKED_BENCHMARK
```

Allowed classifications:

```text
Known
Identity
Reinterpretation
Diagnostic
Finite verification
Boundary
Candidate mechanism
Open problem
New theorem
```

`New theorem` requires a proof package and independent governance path. It is never inferred from the diagnostic engine itself.

## 11. Decision table

| Question signal | Primary route | Observable | Minimum certificate |
|---|---|---|---|
| List all `a+b=N` | PVG-neutral finite | unit weight | finite enumeration |
| Represent `N` by two primes | hybrid | prime indicator | finite verification for one `N` |
| Study Goldbach analytically | ANT-primary | von Mangoldt convolution | asymptotic + uniform error + positivity |
| Analyze residue classes | hybrid | difference channel | effective-period + channel definition |
| Recover weights from channels | linear-algebra primary | channel vector | rank + kernel |
| Optimize retained frequencies | COF | Fourier measurements | target compatibility + feasibility certificate |
| Infer all-even positivity | ANT-primary | weighted representation | all-target analytic certificate |

## 12. Canonical worked diagnoses

### Case B1 — `N=24`, list prime representations

```text
primary_class = PRIME_REPRESENTATION
Goldbach_applicable = TRUE
order_mode = UNORDERED unless otherwise requested
fiber_carrier = integer fiber first
observable = prime indicator
finite_result = {5+19, 7+17, 11+13}
claim_classification = Finite verification
all_target_certificate = ABSENT
Goldbach_proof = NO
```

### Case B2 — `N=25`, Goldbach question

```text
primary_class = GOLDBACH_DIAGNOSTIC
Goldbach_applicable = FALSE
reason = target is odd
result = NOT_APPLICABLE_AS_STATED
```

The engine may suggest a related odd additive problem, but it must not silently replace the user target.

### Case B3 — `r=8`, channel analysis

```text
requested_modulus = 8
effective_period = 8/gcd(2,8) = 4
independent_channel_count cannot exceed 4 before other constraints
rank claim requires explicit matrix analysis
```

### Case B4 — full reconstruction claim

```text
request = recover w from D_{N,r}w
required = rank(D_{N,r}) = dimension of target weight space
also required = kernel(D_{N,r}) = {0}
if kernel nontrivial → exact arbitrary reconstruction denied
```

### Case B5 — symmetric phase on a fixed fiber

For `a+b=N`:

\[
e(\alpha a)e(\alpha b)=e(\alpha N).
\]

Diagnosis:

```text
phase = constant on the fiber
spectral_discrimination = NONE
use difference phase or asymmetric observable instead
```

## 13. Governed output schema

```text
AXIS_ADDITION_DIAGNOSIS
  query_id
  target
  primary_class
  secondary_flags
  applicability
  domain
  order_mode
  integer_fiber_definition
  valuation_transport_needed
  weight
  observable
  modulus
  effective_period
  channel
  Fourier_route
  PVG_ANT_route
  rank_status
  kernel_status
  reconstruction_status
  certificate_present
  certificate_missing
  claim_classification
  scientific_ceiling
  answer
```

Every field not established must be marked `UNKNOWN`, `UNSPECIFIED`, or `NOT_RUN`; omission is not treated as evidence.

## 14. Failure taxonomy

```text
ERR-AXIS-ADD-CATEGORY-COLLAPSE
ERR-AXIS-ADD-DOMAIN-UNSPECIFIED
ERR-AXIS-ADD-ORDER-AMBIGUITY
ERR-AXIS-ADD-VALUATION-LINEARIZATION
ERR-AXIS-ADD-WEIGHT-MISMATCH
ERR-AXIS-ADD-EFFECTIVE-PERIOD-OMITTED
ERR-AXIS-ADD-RANK-WITHOUT-MATRIX
ERR-AXIS-ADD-RECONSTRUCTION-WITHOUT-KERNEL
ERR-AXIS-ADD-FINITE-TO-ASYMPTOTIC-PROMOTION
ERR-AXIS-ADD-GOLDBACH-OVERCLAIM
ERR-AXIS-ADD-NOVELTY-OVERCLAIM
```

## 15. Acceptance criteria

ACTIVE-004-B is specification-complete when:

1. all seven diagnostic layers are explicit;
2. the PVG/ANT route decision is machine-readable;
3. certificate requirements are tied to requested conclusions;
4. the scientific ceiling is enforced before answer release;
5. canonical examples cover applicability, channel reduction, reconstruction, and overclaim rejection;
6. no benchmark success is claimed.

## 16. Current state

```text
ACTIVE-004-B = SPECIFICATION_COMPLETE
DIAGNOSTIC_ENGINE_CODE = NOT_BUILT
LOCKED_CASE_SET = NOT_CREATED
AUTONOMOUS_EXECUTION = NOT_VALIDATED
HIDDEN_EVALUATION = NOT_RUN
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
NEXT_ACTION = ACTIVE-004-C
```

## 17. Next action

`ACTIVE-004-C` will define the locked reasoning benchmark for Axis Addition Specialist Mind 3. It must score route selection, carrier correctness, observable selection, certificate discipline, reconstruction logic, and scientific ceiling compliance—not merely final arithmetic answers.
