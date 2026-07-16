# RMG-002-E — Prime Number Theorem Equivalence Graph and Error-Term Certificate Ladder

Status: completed / finite verification PASS 10/10

Classification: Known Theorem Graph / Certificate Discipline / Diagnostic

Validation state: equivalence_graph_and_error_ladder_verified

Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Represent the standard Prime Number Theorem equivalences and the hierarchy of quantitative error claims without collapsing finite evidence, PVG restatement, zero-free regions, or RH into one another.

## 2. Delivered artifacts

```text
research/research-memory-graph/registry/pnt-equivalence-error-term-ladder.jsonl
research/research-memory-graph/code/verify_rmg_002_e.py
research/research-memory-graph/results/rmg_002_e_verification.json
```

## 3. Standard equivalence graph

The unit records the classical equivalence family

\[
\pi(x)\sim\frac{x}{\log x},
\qquad
\theta(x)\sim x,
\qquad
\psi(x)\sim x.
\]

These are known ANT statements. Their PVG readings are:

- `pi`: count of unit single-axis points below the decoded cutoff;
- `theta`: logarithmic mass of unit single-axis points;
- `psi`: logarithmic mass of all positive single-axis points.

The translation preserves the values and asymptotic statement once imported. It does not prove the asymptotic.

## 4. Analytic dependency

The graph records the classical route from nonvanishing of zeta on `Re(s)=1` to PNT as a literature-certified analytic dependency.

PVG does not currently generate that nonvanishing certificate. A geometric restatement of `psi(x)` is not a zero-free-region proof.

## 5. Error-term certificate ladder

### Level 0 — qualitative PNT

\[
\psi(x)=x+o(x).
\]

This proves the qualitative asymptotic but supplies no declared decay rate.

### Level 1 — effective error form

\[
\psi(x)=x+O\bigl(xE(x)\bigr),
\qquad E(x)\to0.
\]

This requires the function `E`, constants, and range to be declared. Merely writing `O(...)` is not a certificate.

### Level 2 — zero-free-region scale

The registry stores the schematic classical model

\[
\psi(x)=x+O\!\left(xe^{-c\sqrt{\log x}}\right),
\]

with required zero-free-region and contour certificates. It is recorded as a dependency pattern, not as a new project estimate.

### Level 3 — RH scale

Under RH, a standard form is

\[
\psi(x)=x+O\bigl(x^{1/2}\log^2 x\bigr).
\]

This is conditional on RH and explicit-formula/truncation control. Recording it does not establish RH.

## 6. Anti-collapse rules

The executable registry rejects:

```text
finite verification of pi, theta, psi
=> any asymptotic error theorem

PNT
=> RH

PVG restatement of psi=x+error
=> improved error term

zero-free-region error
=> RH
```

A stronger conclusion requires its own theorem and certificate.

## 7. Numerical diagnostics

The verifier computes finite observables at `x=100,1000,10000,100000`.

At `x=100000`:

```text
pi(x) log(x) / x = 1.1043198105999443
theta(x) / x     = 0.9968538926861255
psi(x) / x       = 1.0005156402565796
```

These values are consistent with PNT. They are not a proof of PNT and do not certify an error term.

It also checks the exact finite inequality

\[
\theta(x)\le\psi(x),
\]

because `psi` includes all prime powers while `theta` includes only primes.

## 8. Verification result

```text
REGISTRY AND UNIQUE IDS            PASS
ERROR LADDER 0..3                  PASS
PI/THETA/PSI COVERAGE              PASS
FINITE OBSERVABLES                 PASS
THETA <= PSI                       PASS
ANTI-COLLAPSE RULES                PASS
RH CONDITIONAL LABEL               PASS
ZERO-FREE-REGION REQUIREMENTS      PASS
NO UNJUSTIFIED L6                  PASS
CLAIM CEILING                      PASS
TOTAL                              PASS 10/10
```

## 9. Assimilation state

```text
PNT_EQUIVALENCE_GRAPH = L5_COMPUTATIONALLY_REGRESSION_TESTED
ERROR_TERM_CERTIFICATE_LADDER = L5_COMPUTATIONALLY_REGRESSION_TESTED
CLASSICAL_ZERO_FREE_REGION = dependency represented, not project-derived
RH_ERROR_TERM = conditional known statement
NEW_ERROR_TERM = none
LEAN_PROOF_ADDED = none
L6_PROMOTION = not authorized
```

## 10. Scientific ceiling

```text
KNOWN PNT EQUIVALENCES + FINITE DIAGNOSTICS
NOT A NEW PNT PROOF
NOT A NEW ERROR TERM
NOT A NEW ZERO-FREE REGION
NO RH OR GRH PROGRESS
NO TRAINING CORPUS AUTHORIZATION
```

## 11. Acceptance decision

```text
PNT_EQUIVALENCE_GRAPH = PASS
ERROR_TERM_LADDER = PASS
PVG_TRANSLATION_HONESTY = PASS
FINITE_REGRESSION = PASS 10/10
RMG-002-E = COMPLETED
```

## 12. Next governed step

```text
RMG-002-F — Zeta Zero / Explicit Formula / Prime-Observable Dependency Boundary
```

The next unit should register the explicit-formula dependency, truncation and smoothing requirements, what zero data can generate about prime observables, and why finite prime observables do not invert uniquely to all nontrivial zeros.
