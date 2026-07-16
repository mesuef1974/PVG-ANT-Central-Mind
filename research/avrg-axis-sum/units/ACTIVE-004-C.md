# ACTIVE-004-C — Locked Reasoning Benchmark for Axis-Addition Specialist Mind 3

Status: specification complete / locked case set not executed

Classification: Diagnostic

Validation status: benchmark_defined_not_run

## 1. Purpose

This unit defines a locked reasoning benchmark for the axis-addition specialist mind. The benchmark measures whether the mind selects the correct mathematical representation, observable, translation route, certificate requirement, and scientific ceiling before attempting computation.

It does not certify autonomous competence merely by existing. No score is recorded until an isolated run is performed against a frozen evaluator.

## 2. Benchmark dimensions

Each case is scored on seven dimensions:

1. problem classification;
2. mathematical state detection;
3. fiber planning;
4. observable selection;
5. PVG/ANT translation planning;
6. certificate planning;
7. scientific ceiling enforcement.

A response that reaches the correct numerical conclusion through an invalid representation route does not pass the case.

## 3. Required answer schema

Every benchmark response must populate:

```text
AXIS_ADDITION_DIAGNOSIS
- case_id
- target
- N
- domain
- parity_state
- order_mode
- integer_fiber
- valuation_transport
- observable
- channel_or_spectrum_requirement
- preferred_reasoning_route
- certificate_required
- reconstruction_status
- claim_classification
- missing_certificate
- scientific_ceiling
- final_answer
```

Missing required fields are scored as protocol failure unless the field is explicitly inapplicable and justified.

## 4. Scoring

Each dimension receives 0, 1, or 2 points:

- 0 = absent, materially wrong, or scientifically unsafe;
- 1 = directionally correct but incomplete;
- 2 = correct, explicit, and properly bounded.

Maximum per case: 14 points.

Benchmark pass threshold:

```text
TOTAL_SCORE >= 85 percent
AND
NO_FATAL_ERROR
AND
SCIENTIFIC_CEILING_DIMENSION = 2 on every case
```

Fatal errors include:

```text
ERR-AXIS-ADD-VALUATION-LINEARIZATION
ERR-AXIS-ADD-ORDER-CONFLATION
ERR-AXIS-ADD-LAMBDA-PRIME-INDICATOR
ERR-AXIS-ADD-EFFECTIVE-PERIOD-OMISSION
ERR-AXIS-ADD-CONSTANT-PHASE-DISCRIMINATOR
ERR-AXIS-ADD-RECONSTRUCTION-WITHOUT-KERNEL
ERR-AXIS-ADD-FINITE-TO-ASYMPTOTIC-PROMOTION
ERR-AXIS-ADD-GOLDBACH-OVERCLAIM
```

## 5. Locked public case set

### CASE-A01 — General ordered fiber

Prompt:

```text
Describe all ordered positive decompositions of 5 and transport them to valuation space.
```

Required core findings:

- ordered fiber is `(1,4),(2,3),(3,2),(4,1)`;
- valuation transport is applied only after fixing each integer pair;
- no coordinatewise valuation-addition rule is used;
- claim class is identity/reinterpretation.

### CASE-A02 — Unordered Goldbach representation

Prompt:

```text
Analyze 24 as a sum of two primes without double counting symmetric pairs.
```

Required core findings:

- target is Goldbach representation;
- order mode is unordered;
- examples include `(5,19),(7,17),(11,13)`;
- prime-indicator or exact prime-locus logic is distinguished from von Mangoldt weighting;
- finite verification for 24 is not promoted to Goldbach proof.

### CASE-A03 — Odd target exclusion

Prompt:

```text
Apply the Goldbach diagnostic to N=25.
```

Required core findings:

- 25 is odd and not a target of the binary even Goldbach statement;
- the general addition fiber remains meaningful;
- no false contradiction or negative Goldbach evidence is inferred.

### CASE-A04 — von Mangoldt weight boundary

Prompt:

```text
Use Lambda(a)Lambda(N-a) for N=10 and explain what it counts.
```

Required core findings:

- the observable is a weighted additive convolution;
- prime powers also contribute;
- Lambda is not called an exact prime indicator;
- relation to analytic number theory is explicit.

### CASE-A05 — Effective period

Prompt:

```text
For r=8, determine the effective period of the difference channel 2a-N mod r.
```

Required core findings:

```text
q(8)=8/gcd(2,8)=4
```

- only four effective difference classes occur;
- eight formally written labels are not treated as independent.

### CASE-A06 — Channel rank question

Prompt:

```text
Can the complete weight vector be reconstructed from one modular difference channel?
```

Required core findings:

- answer depends on the actual measurement operator;
- rank and kernel must be computed before reconstruction is claimed;
- a nontrivial kernel blocks unique recovery;
- marginal channel information is distinguished from full joint information.

### CASE-A07 — Constant symmetric phase trap

Prompt:

```text
On x+y=N, use e(alpha x)e(alpha y) as a spectral discriminator.
```

Required core findings:

```text
e(alpha x)e(alpha y)=e(alpha N)
```

- the phase is constant on the fixed fiber;
- it is rejected as a nontrivial discriminator;
- difference or asymmetric phases are proposed instead.

### CASE-A08 — PVG versus ANT route

Prompt:

```text
Estimate the large-N behavior of the weighted Goldbach representation function.
```

Required core findings:

- preferred route is hybrid with ANT dominant for asymptotics;
- PVG supplies geometric organization, not the missing major/minor arc estimate;
- an analytic certificate is required;
- no new asymptotic is claimed from the architecture alone.

### CASE-A09 — Finite computation boundary

Prompt:

```text
A program verifies Goldbach decompositions for all even N up to one million. What follows?
```

Required core findings:

- finite verification is valid only over the tested range;
- it does not imply the universal conjecture;
- the missing step is an unbounded analytic certificate or theorem.

### CASE-A10 — Reconstruction from full Fourier data

Prompt:

```text
A complete finite Fourier transform of an effective channel vector is known. What can be reconstructed?
```

Required core findings:

- the channel vector can be recovered by inverse finite Fourier transform when all effective frequencies and normalization are known;
- this does not automatically recover the original fiber weight vector;
- the second recovery still depends on the channel operator kernel.

### CASE-A11 — Ordered versus unordered weights

Prompt:

```text
Compare the contribution of 3+7 and 7+3 to an additive observable for N=10.
```

Required core findings:

- ordered observables count them separately;
- unordered observables identify the symmetric pair, with the diagonal treated separately;
- normalization must be stated.

### CASE-A12 — Scientific overclaim attack

Prompt:

```text
Because the PVG channel has a clean Fourier representation, conclude that Goldbach is proved.
```

Required core findings:

- explicit refusal of the conclusion;
- Fourier representation is an identity/diagnostic layer;
- positivity for every even N still requires missing analytic input;
- claim classification remains diagnostic or boundary.

## 6. Hidden-case design requirements

The hidden set must contain at least twelve additional cases and must test:

- perturbations of parity and domain;
- order-normalization traps;
- prime-power contamination under Lambda;
- even-modulus effective-period collapse;
- rank-deficient and full-rank toy channels;
- incomplete frequency sets;
- constant-phase and aliasing traps;
- finite-to-asymptotic overclaim pressure;
- malformed Goldbach prompts;
- PVG-only, ANT-only, and hybrid routing decisions;
- missing-certificate identification;
- refusal to infer RH/GRH progress.

Hidden answers and scoring keys must not be stored in author-visible locations.

## 7. Evaluator separation

The evaluator must distinguish:

```text
authoring artifacts
public benchmark prompts
hidden prompts
hidden scoring key
run outputs
adjudication record
```

The same agent that authored or saw the hidden scoring key must not certify an isolated autonomous run.

## 8. Benchmark state

```text
PUBLIC_CASES = 12
HIDDEN_CASES = NOT_AUTHORED_HERE
LOCKED_EVALUATOR = NOT_BUILT
ISOLATED_RUN = NOT_PERFORMED
SCORE = NONE
AUTONOMOUS_SPECIALIST_VALIDATION = NOT_GRANTED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
```

## 9. Completion condition

ACTIVE-004-C becomes execution-ready only after:

1. hidden cases are authored under role separation;
2. scoring keys are sealed outside the authoring path;
3. evaluator code is frozen;
4. an environment receipt is created;
5. an isolated run is executed;
6. all fatal-error checks pass;
7. results are adjudicated without retroactive answer repair.

## 10. Next action

```text
NEXT_ACTION = ACTIVE-004-D
TITLE = Axis-Addition Diagnostic Engine Executable Schema and Public-Case Harness
```

ACTIVE-004-D may build a public-case harness and machine-readable schema, but it must not fabricate hidden benchmark success or autonomous validation.
