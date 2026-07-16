# RMG-004-B — Sieve Weights, Fundamental Lemma, Upper/Lower Functions, and Remainder Norms

**Status:** COMPLETED  
**Branch:** `agent/pvg-axis-sum-continuation-002`  
**Verification:** PASS 9/9  
**Assimilation ceiling:** L5 for finite identities and certificate discipline; no L6 proof added.

## Purpose

This unit connects the existing Harman / Opera de Cribro sieve knowledge to the executable Research Memory Graph without creating a parallel sieve ontology. It focuses on the distinction between:

1. a finite sieve weight;
2. a one-sided pointwise inequality;
3. a fundamental-lemma certificate;
4. an aggregate remainder estimate;
5. a sifted-set conclusion;
6. a prime-producing conclusion.

These are not interchangeable.

## Core objects

For a sequence `A=(a_n)`, define divisor-channel aggregates

\[
A_d=\sum_{d\mid n} a_n.
\]

A declared local model has the form

\[
A_d=Xg(d)+r_d.
\]

Upper and lower sieve weights are finitely supported systems `lambda_d^+` and `lambda_d^-`. Their useful content is not their existence alone, but a certified inequality, support range, normalization, target sequence, and admissible parameter regime.

The dimensionless sieve parameter is

\[
s=\frac{\log D}{\log z}.
\]

It records the relation between the available distribution level `D` and the sieving threshold `z`; it does not by itself certify an asymptotic.

## PVG translation

For `v=nu(n)`, each divisor `d|n` corresponds bijectively to a valuation subvector

\[
u(d)=u\le v.
\]

Therefore

\[
\sum_{d\mid n}\lambda_d
=
\sum_{u\le \nu(n)}\lambda_{\operatorname{decode}(u)},
\]

with the support restriction inherited exactly from the divisor weight.

This translation preserves:

- divisor support;
- signs and numerical weights;
- finite one-sided inequalities already proved in the ANT formulation.

It does not create:

- a remainder estimate;
- the fundamental lemma;
- positivity of the lower sieve function;
- prime purity;
- a solution of the parity problem.

## Fundamental-lemma dependency

A usable fundamental-lemma statement must name at least:

- the sequence and its total scale `X`;
- the local density `g(d)` and its dimension hypothesis;
- `z`, `D`, and `s=log D/log z`;
- the upper or lower weight convention;
- the normalization of `F_kappa(s)` and `f_kappa(s)`;
- the remainder norm and its range;
- the error term and all uniformity conditions.

The functions `F_kappa(s)` and `f_kappa(s)` are theorem- and normalization-dependent. In particular, a lower function outside its positivity range gives no positive lower-bound certificate.

## Remainder certificate discipline

A pointwise assertion such as

\[
|r_d|\le R_d
\]

is not the same as an aggregate estimate such as

\[
\sum_{d<D}|r_d|\le R
\]

or the weight-sensitive bound

\[
\sum_{d<D}|\lambda_d r_d|\le R_\lambda.
\]

The norm, range, support restrictions, and weights must be explicit. Changing any of these changes the certificate.

## Numerical regression

The executable harness verifies:

1. 12 registry records and unique IDs.
2. Exact weighted divisor-box identity for the weight supported on `{1,2,3,6}` for every `n<=300`.
3. Exact finite inclusion-exclusion for removing prime axes `2,3,5` on `n<=500`; 134 integers survive.
4. For the elementary model `A_d=floor(1000/d)`, `g(d)=1/d`, the remainder satisfies
   \[
   \max_{d<100}|r_d|=0.989010989010989<1.
   \]
5. The corresponding finite aggregate norm is explicitly
   \[
   \sum_{d<100}|r_d|=45.37751763962025.
   \]
6. For `D=1000`, `z=11`,
   \[
   s=2.880757703367382.
   \]
7. Required certificate and rejection record types are present.

These calculations test definitions and finite identities. They do not prove a general fundamental lemma.

## Claim rejections

The registry rejects:

```text
finite sieve weights
=> fundamental lemma
```

```text
small finite sampled remainder
=> uniform asymptotic remainder norm
```

```text
positive lower bound for a sifted set
=> prime-producing theorem
```

A sifted set can contain composites and almost-primes. Prime production requires a separate target-purity certificate and, where relevant, mechanisms beyond parity-insensitive sieve information.

## Assimilation levels

```text
finite sieve weights and divisor-box translation = L5
finite inclusion-exclusion regression            = L5
remainder-norm certificate discipline             = L5
fundamental-lemma dependency graph                = L3
upper/lower sieve function theory                 = L2
prime-producing transfer                          = not established
Lean proof added                                  = none
L6 promotion                                      = not authorized
```

## Reused project components

- `maps/bridges/BRIDGE-SIEVE-INFORMATION-001.md`
- Harman sieve ledger and tools
- Opera de Cribro scope, normalization, and certificate separation
- `RMG-004-A` sieve objects / aggregation kernel / level-of-distribution graph

## Files

- `registry/sieve-weights-fundamental-lemma-remainders.jsonl`
- `code/verify_rmg_004_b.py`
- `results/rmg_004_b_verification.json`
- `units/RMG-004-B.md`

## Next unit

```text
RMG-004-C
Type I / Type II Information,
Bilinear Decomposition,
and Level-of-Distribution Transfer Graph
```
