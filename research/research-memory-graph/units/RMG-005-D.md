# RMG-005-D — Prime-Weighted Exponential Sums, Vaughan Decomposition, and Major/Minor-Arc Transfer Graph

**Status:** COMPLETED  
**Branch:** `agent/pvg-axis-sum-continuation-002`  
**Verification:** `PASS 8/8`

## Purpose

Connect the prime-weighted exponential sum

\[
S(\alpha;N)=\sum_{n\le N}\Lambda(n)e(\alpha n)
\]

to Vaughan-style decompositions, Type I/II estimates, and major/minor-arc certificate obligations, while preserving the distinction between exact algebraic decomposition and nontrivial analytic cancellation.

## Core graph

```text
Lambda-weighted exponential sum
  -> Vaughan identity with explicit U,V
  -> Type I pieces
  -> Type II pieces
  -> remainder/short pieces
  -> quantitative estimates with stated ranges
  -> minor-arc bound

Prime distribution in progressions
  + local Fourier analysis
  -> major-arc approximation

major-arc main term
  + minor-arc domination
  + local admissibility
  -> representation asymptotic/positivity certificate
```

No arrow is reversible without an independent theorem.

## Exact algebraic layer

The finite identity

\[
\Lambda=\mu*\log
\]

was regression-tested in the form

\[
\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d)
\]

for `1 <= n <= 300`.

Maximum floating-point discrepancy:

```text
9.992007221626409e-16
```

This identity is an algebraic source for decompositions. It does not itself produce cancellation.

## PVG translation

For a product `mn`,

\[
\nu(mn)=\nu(m)+\nu(n).
\]

Hence bilinear pieces may be reindexed as sums over valuation-vector splits

\[
w=u+v.
\]

The translation preserves:

- factor pairs;
- coefficient values and signs;
- decoded integers;
- additive phases `e(alpha mn)`;
- chosen parameter ranges.

It does not create:

- Type I or Type II savings;
- uniformity in `alpha`;
- major-arc constants;
- minor-arc domination;
- a representation theorem.

## Certificate separation

```text
exact decomposition
!= Type I estimate
!= Type II estimate
!= uniform minor-arc bound
!= major-arc asymptotic
!= positive additive theorem
```

A valid Type I/II certificate must state at least:

- coefficient norms;
- variable ranges;
- cutoffs `U,V`;
- alpha-domain or arc family;
- uniformity parameters;
- quantitative saving relative to the trivial bound;
- handling of residual pieces.

## Finite numerical diagnostics

Parameters:

```text
N = 500
alpha in {sqrt(2) mod 1, sqrt(3) mod 1, 0.271828}
```

Measured magnitudes:

```text
42.744541932168325
54.45351061329357
40.39173886486805
```

Trivial `L1` bound:

```text
501.65211664974765
```

These values demonstrate finite cancellation at selected points only. They do not establish a uniform bound on an arc.

## Negative benchmarks

The registry rejects:

1. Vaughan decomposition implies a nontrivial minor-arc estimate.
2. Small values on a finite alpha grid imply continuous uniform control.
3. Prime-weighted exponential-sum identities imply binary Goldbach.
4. Exact PVG factor splitting implies analytic cancellation.
5. A major-arc approximation removes the need for a minor-arc certificate.

## Assimilation levels

```text
prime-weighted exponential sum definition      = L4
finite Lambda = mu * log regression             = L5
valuation-factor split translation              = L5
Vaughan decomposition dependency graph          = L3
Type I/Type II certificate discipline           = L3
major/minor-arc transfer graph                   = L3
uniform exponential-sum estimates               = not added
Lean proof added                                 = none
L6 promotion                                     = not authorized
Goldbach progress                                = none
```

## Claim ceiling

This unit adds a governed translation and dependency graph. It proves no new exponential-sum estimate, no major-arc asymptotic, no minor-arc domination, and no progress on binary Goldbach.

## Files

- `registry/prime-weighted-exponential-vaughan-major-minor.jsonl`
- `code/verify_rmg_005_d.py`
- `results/rmg_005_d_verification.json`

## Next unit

```text
RMG-006-A
Zero-Density Estimates, Large Values,
and Prime-Error-Term Transfer Graph
```
