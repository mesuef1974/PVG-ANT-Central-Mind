# ENGINE-003 — Inverse Integer Fibers

**ID:** `ENGINE-003-INVERSE-INTEGER-FIBERS`  
**Goal:** `GOAL-PVG-INVERSE-GEOMETRY-001`  
**Phase:** B — Inverse Integer Fibers  
**Classification:** `Identity / Finite-Verified / Diagnostic`  
**Date:** 2026-07-22

## 1. Purpose

Phase A recovered support predecessors. Phase B resolves each support face into the exact integers that live on it, while preserving exponent data rather than collapsing immediately to support.

For a finite prime face

\[
F=\{p_1,\ldots,p_k\},
\]

define

\[
\mathcal N(F)=\{n\ge1:\operatorname{supp}(n)=F\}.
\]

## 2. Exponent-lattice bijection

Unique factorization gives the exact identity

\[
\boxed{
\mathcal N(F)=
\left\{\prod_{j=1}^k p_j^{e_j}:e_j\ge1\right\}.
}
\]

Therefore

\[
\Phi_F:\mathbb N_{\ge1}^{k}\to\mathcal N(F),
\qquad
(e_1,\ldots,e_k)\mapsto\prod_{j=1}^k p_j^{e_j}
\]

is a bijection.

This turns every integer fiber into a translated positive orthant lattice. The support face fixes the axes; the exponent vector locates the integer inside the fiber.

**Classification:** `Known / Identity`.

## 3. Geometry inside one fiber

### 3.1 Minimum

The smallest point is the radical:

\[
\min\mathcal N(F)=\operatorname{rad}(F)=\prod_{p\in F}p.
\]

### 3.2 Divisibility

For

\[
n=\prod p_j^{a_j},\qquad m=\prod p_j^{b_j},
\]

we have

\[
n\mid m
\iff
a_j\le b_j\quad\text{for every }j.
\]

Thus divisibility is coordinatewise order.

### 3.3 Hasse edges

A cover relation increments exactly one exponent by one:

\[
(e_1,\ldots,e_i,\ldots,e_k)
\prec
(e_1,\ldots,e_i+1,\ldots,e_k).
\]

The bounded fiber is therefore a finite induced subgraph of the positive orthant lattice.

## 4. Arithmetic closure laws

If \(m,n\in\mathcal N(F)\), then:

\[
mn\in\mathcal N(F),
\qquad
\gcd(m,n)\in\mathcal N(F),
\qquad
\operatorname{lcm}(m,n)\in\mathcal N(F).
\]

The reason is that sums, minima, and maxima of positive exponent coordinates remain positive.

In contrast, the fiber is not generally closed under addition or integer quotient. For example:

\[
2,4\in\mathcal N(\{2\}),
\qquad
2+4=6\notin\mathcal N(\{2\}),
\]

and

\[
4/4=1
\]

has empty support.

**Classification:** `Known / Exact structural laws`.

## 5. Dirichlet-series identity

For \(\Re(s)>0\), absolute convergence of finitely many geometric series gives

\[
\begin{aligned}
\sum_{n\in\mathcal N(F)}\frac1{n^s}
&=
\sum_{e_1,\ldots,e_k\ge1}
\prod_{j=1}^k p_j^{-e_js}\\
&=
\prod_{j=1}^k
\sum_{e_j\ge1}p_j^{-e_js}\\
&=
\boxed{
\prod_{p\in F}\frac1{p^s-1}
}.
\end{aligned}
\]

This is the first exact analytic translation native to Phase B. The formula itself is a direct geometric-series identity and carries no originality claim.

## 6. Frozen complete box

```text
support primes <= 11
support sizes = 1,2,3
integer cap = 100000
Dirichlet test point s = 2
```

The support universe contains 25 faces. For each face the exponent-lattice generator was compared with an independent scan of every integer from 1 through 100000.

Registered totals:

```text
support faces checked             = 25
fiber points across all faces     = 884
Hasse edges across all faces      = 1503
complete-scan matches             = 25
complete-scan mismatches          = 0
```

The largest bounded fiber in the box is:

\[
F=\{2,3,5\},
\]

with 127 points up to 100000.

## 7. Example: the fiber \(F=\{2,3,5\}\)

The first points are:

\[
30,60,90,120,150,180,240,270,300,360,\ldots
\]

They correspond to exponent vectors:

\[
(1,1,1),
(2,1,1),
(1,2,1),
(3,1,1),
(1,1,2),
(2,2,1),\ldots
\]

Different integers can have the same total exponent \(\Omega(n)\), but distinct directions inside the exponent lattice. Phase B therefore restores information lost by the support projection.

## 8. What Phase B adds

Phase B supplies:

1. an exact generator for integer fibers;
2. a canonical exponent coordinate system;
3. a divisibility lattice and Hasse graph;
4. closure laws for multiplication, gcd, and lcm;
5. a deterministic bounded data contract;
6. an exact Dirichlet-series bridge.

It does not yet supply:

1. prime-pair representations of fiber elements;
2. estimates for the counting function of a union of fibers;
3. cancellation in weighted sums;
4. a new Euler product theorem;
5. a Goldbach result;
6. a transfer lemma serving the theorem program.

## 9. Candidate next analytic questions

These are questions only, not authorized tasks:

- weighted fiber series
  \[
  \sum_{n\in\mathcal N(F)}f(n)n^{-s};
  \]
- exact or asymptotic counting of fiber points under alternative height functions;
- unions of fibers selected by inverse-orbit class;
- interaction of Möbius, von Mangoldt, or divisor weights with fixed support;
- whether an orbit-stratified Dirichlet series yields a material transfer principle.

## 10. Verification assets

```text
tools/pvg_inverse_integer_fibers.py
tests/test_pvg_inverse_integer_fibers.py
research/pvg-space-deepening/data/inverse-integer-fibers-summary.json
.github/workflows/pvg-inverse-integer-fibers-audit.yml
```

## 11. Stage boundary

Phase B stops at exact integer fibers and their elementary analytic generating function.

```text
Phase C is not authorized.
```

Opening prime fibers requires a separate readiness card, fixed representation scope, and explicit return gate. The existence of the Dirichlet product formula does not by itself justify moving to Goldbach-type computation.

## 12. Scientific ceiling

- No originality claim is attached to the exponent-lattice or geometric-series identities.
- Finite counts are valid only inside the registered box.
- No asymptotic counting theorem is claimed.
- No Phase C, Goldbach, PNT, RH, or GRH progress is claimed.
- No publication readiness follows from this infrastructure.

**Honest classification:** exact classical structure exposed in PVG coordinates, plus a complete finite implementation certificate. No new theorem certified.
