# ENGINE-006 WP-3 — Reconstruction and Loss Map

```text
Engine: ENGINE-006
Work package: WP-3 — Reconstruction and Loss Audit
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Status: COMPLETE_FOR_REVIEW
Experimental expansion: NOT USED
New finite count: NOT USED
Phase D: NOT AUTHORIZED
Date: 2026-07-23
```

## 1. Governed core

WP-2 reduced the framework to two governed cores:

```text
O1 integer object, presented as N or its finite-support valuation vector nu(N)
O2 typed distinct-prime representation relation
   R = {(N,p,q): p<q, p and q prime, p+q=N}
```

Every remaining object is a derived row, coordinate, incidence presentation, or projection of these cores.

## 2. Typed domains

Let

\[
\mathcal V=\bigoplus_{\ell\in\mathbb P}\mathbb Z_{\ge 0}
\]

be the finite-support nonnegative valuation vectors, and let

\[
\Phi(a)=\prod_{\ell\in\mathbb P}\ell^{a_\ell}.
\]

Let

\[
\mathcal R=\{(N,p,q):p<q,\ p,q\text{ prime},\ p+q=N\}.
\]

For fixed \(N\), define

\[
\mathcal R_2(N)=\{(p,q):(N,p,q)\in\mathcal R\}.
\]

For \((N,p,q)\in\mathcal R\), define \(\Delta=q-p\). The governed coordinate \(d\) is

\[
d=\begin{cases}
\Delta/2,&N\text{ even},\\
\Delta,&N\text{ odd}.
\end{cases}
\]

and \(D(N)\) is the row of governed coordinates arising from \(\mathcal R_2(N)\).

## 3. Lossless maps

### M1 — Integer / valuation presentation

\[
N\longmapsto \nu(N),\qquad a\longmapsto \Phi(a).
\]

**Type:** `BIJECTION` between positive integers and finite-support nonnegative valuation vectors.

**Inverse laws:**

\[
\Phi(\nu(N))=N,
\qquad
\nu(\Phi(a))=a.
\]

**Retained information:** complete integer identity, factor exponents, support, parity.

**Loss:** none.

**Classification:** `IDENTITY / PROVED`.

### M2 — Prime pair / centered gap over fixed base

\[
(N,p,q)\longmapsto (N,\Delta=q-p).
\]

On the image, the inverse is

\[
p=\frac{N-\Delta}{2},
\qquad
q=\frac{N+\Delta}{2}.
\]

**Type:** `TYPED EQUIVALENCE` between \(\mathcal R\) and the admissible image

\[
\mathcal A_\Delta
=\{(N,\Delta): ((N-\Delta)/2,(N+\Delta)/2)\text{ is a governed prime pair}\}.
\]

The coordinate formula alone does not test primality; admissibility is part of the typed codomain.

**Retained labels:** \(N\), pair order convention \(p<q\), distinctness, primality.

**Loss:** none on the typed image.

**Classification:** `PROVED`.

### M3 — Prime-pair row / governed spectrum row

\[
(N,\mathcal R_2(N))\longmapsto (N,D(N)).
\]

Apply M2 coordinatewise, using the route-dependent normalization. The inverse applies the relevant reconstruction formula to every coordinate.

**Type:** `TYPED EQUIVALENCE`.

**Retained labels:** base point \(N\), route convention, set semantics, distinct unordered-pair convention.

**Loss:** none while \(N\) and route typing are retained.

Consequently,

\[
|D(N)|=|\mathcal R_2(N)|.
\]

**Classification:** `PROVED`.

### M4 — Representation relation / integer-coordinate incidence

Define

\[
I=\{(N,d):d\in D(N)\}.
\]

Then the typed relation \(\mathcal R\) and \(I\) determine one another via M2/M3.

**Type:** `TYPED EQUIVALENCE`.

**Retained labels:** integer owner \(N\), coordinate \(d\), route convention.

**Loss:** none relative to the governed distinct-prime relation.

**Boundary:** the ordinary graph presentation of \(I\) is only a representation of membership, not a new arithmetic relation.

**Classification:** `PROVED`.

## 4. Lossy projections and their fibers

### P1 — Integer to support

\[
\sigma:N\longmapsto \operatorname{supp}(N)
=\{\ell:\nu_\ell(N)>0\}.
\]

**Type:** `LOSSY PROJECTION`.

For a finite prime set \(F\), the fiber is

\[
\sigma^{-1}(F)
=\left\{\prod_{\ell\in F}\ell^{a_\ell}:a_\ell\ge1\right\}.
\]

The fiber is infinite for every nonempty \(F\).

**Retained:** which prime coordinates are nonzero.

**Lost:** every positive exponent, magnitude, exact integer identity, additive representation data.

**Classification:** `IDENTITY / PROVED`.

### P2 — Integer to parity route

Let

\[
\rho(N)=\begin{cases}
\text{even route},&2\mid N,\\
\text{odd route},&2\nmid N.
\end{cases}
\]

**Type:** `LOSSY PROJECTION`.

Fibers are the even and odd positive integers.

**Retained:** presence or absence of the prime 2 in the support.

**Lost:** all other support coordinates, exponents, integer identity, fiber multiplicity.

The factorization

\[
N\xrightarrow{\sigma}\operatorname{supp}(N)
\longrightarrow \rho(N)
\]

shows that parity route is a coarsening of support.

**Classification:** `PROVED`.

### P3 — Forgetting the base point from the spectrum

\[
\pi_D:(N,D(N))\longmapsto D(N).
\]

**Type:** `LOSSY PROJECTION` in general.

For a spectrum value \(S\), the fiber is

\[
\pi_D^{-1}(S)=\{N:D(N)=S\}.
\]

A fiber can contain multiple base points; hence \(D(N)\) alone does not determine \(N\), midpoint, support, or pair labels.

**Retained:** the coordinate set only.

**Lost:** the base point required by the inverse formulas.

**Exact exception:** on represented odd points, the singleton coordinate determines \(N=d+4\); this route-specific injectivity does not make the unrestricted projection injective.

**Classification:** `PROVED`.

### P4 — Integer-owner incidence to support-owner incidence

From

\[
I=\{(N,d):d\in D(N)\},
\]

define

\[
J=\{(\operatorname{supp}(N),d):(N,d)\in I\}.
\]

**Type:** `LOSSY PROJECTION` induced by \((N,d)\mapsto(\sigma(N),d)\).

For a support-coordinate pair \((F,d)\), the fiber is

\[
\{N:\operatorname{supp}(N)=F,\ d\in D(N)\}.
\]

**Retained:** support face and coordinate ownership.

**Lost:** integer owner, exponent vector, multiplicity of distinct owners unless explicitly stored.

**Classification:** `PROVED`.

### P5 — Support to parity route

\[
F\longmapsto \begin{cases}
\text{even route},&2\in F,\\
\text{odd route},&2\notin F.
\end{cases}
\]

**Type:** `LOSSY PROJECTION`.

Fibers are all support sets containing 2 and all support sets excluding 2.

**Retained:** only membership of the prime 2.

**Lost:** every other support prime and support size.

**Classification:** `IDENTITY / PROVED`.

## 5. Composition laws

### C1 — Complete integer reconstruction

\[
N\xrightarrow{\nu}\nu(N)\xrightarrow{\Phi}N
\]

and

\[
a\xrightarrow{\Phi}\Phi(a)\xrightarrow{\nu}a
\]

are identity compositions.

### C2 — Pair-coordinate reconstruction

On \(\mathcal R\),

\[
(N,p,q)\mapsto(N,\Delta)\mapsto(N,p,q)
\]

is the identity. The reverse composition is the identity only on the admissible coordinate image.

### C3 — Row-incidence equivalence

\[
\{(N,D(N))\}_N
\longleftrightarrow
I=\{(N,d):d\in D(N)\}
\]

is a transpose/change-of-presentation equivalence when empty registered rows are retained separately. If empty rows are omitted, the incidence relation alone cannot recover which registered integers have empty fibers.

### C4 — Irreversibility after support projection

The composition

\[
N\to \operatorname{supp}(N)\to \rho(N)
\]

loses exponent data at the first arrow and all support data except membership of 2 at the second. No later map can recover information already discarded without external labels.

### C5 — Irreversibility after deleting N

The composition

\[
(N,\mathcal R_2(N))
\leftrightarrow
(N,D(N))
\to
D(N)
\]

is lossless before the final projection and generally noninvertible after it. The failure is caused by deleting the base point, not by centered coordinates themselves.

### C6 — Support-incidence collapse

\[
\mathcal R
\leftrightarrow I
\to J
\]

first changes presentation without loss, then collapses all integer owners sharing a support-coordinate label. Therefore any support-conditioned summary is downstream of an irreversible quotient.

## 6. Reconstruction hierarchy

```text
FULLY LOSSLESS, WITH TYPES RETAINED
N <-> nu(N)
(N,p,q) <-> admissible (N,Delta)
(N,R_2(N)) <-> (N,D(N))
representation relation <-> integer-coordinate incidence

LOSSY PROJECTIONS
N -> support
support -> parity route
(N,D(N)) -> D(N)
integer-coordinate incidence -> support-coordinate incidence
```

No lossy projection becomes lossless merely because it is displayed geometrically.

## 7. What the audit establishes

1. The valuation presentation is a complete coordinate presentation of the integer object.
2. Centered coordinates are complete coordinates for governed prime pairs only over a retained base point and typed admissible domain.
3. Spectrum rows and integer-coordinate incidence are equivalent presentations of the same relation.
4. Support, route, base-forgetting, and support-incidence maps are genuine quotients/projections with explicit fibers.
5. The useful durable contribution is the disciplined separation of reversible coordinate changes from irreversible projections.

## 8. What the audit does not establish

```text
new primitive arithmetic object = NOT ESTABLISHED
new theorem beyond elementary typed consequences = NOT ESTABLISHED
predictive support law = NOT ESTABLISHED
causal support effect = NOT ESTABLISHED
independent PVG theory = OPEN
novelty/publication readiness = NOT ESTABLISHED
Goldbach/PNT/RH/GRH progress = false
```

## 9. Work-package decision

```text
WP-3 RECONSTRUCTION AND LOSS AUDIT = COMPLETE_FOR_REVIEW
WP-4 STANDARD-STRUCTURE COMPARISON = NOT YET OPENED
new experiment = NOT AUTHORIZED
Phase D = NOT AUTHORIZED
```

**Honest conclusion:** the completed map system is mathematically exact, but its presently proved content is a typed organization of standard equivalences and quotient maps. Whether this organization has value beyond clarification, software contracts, and proof hygiene must be decided by the parent review and the standard-structure comparison.