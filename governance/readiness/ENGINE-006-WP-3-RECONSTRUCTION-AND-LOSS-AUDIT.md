# ENGINE-006 WP-3 — Reconstruction and Loss Audit Readiness

```text
Task ID: ENGINE-006-WP-3-RECONSTRUCTION-AND-LOSS-AUDIT
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-006
Basis: ENGINE-006-WP-2-PARENT-REVIEW-001
Decision: READY
Status: ACTIVE_CURRENT_SUBPASS
Date: 2026-07-23
Experimental expansion: NOT AUTHORIZED
Phase D: NOT AUTHORIZED
```

## Governing question

What is the exact compositional map structure connecting the integer/valuation presentation, prime-pair relation, centered coordinates, spectra, incidence rows, support projections, and parity route; and precisely where is information lost?

## Governed core

```text
O1 integer object with equivalent presentations N <-> nu(N)
O2 typed relation R={(N,p,q):p<q, p+q=N}
```

All other objects are derived and must be introduced only as codomains, fibers, rows, or projections of these cores.

## Required maps

At minimum audit:

```text
M1  N <-> nu(N)
M2  (N,p,q) -> (N,Delta=q-p)
M3  admissible (N,Delta) -> (N,p,q)
M4  (N,R_2(N)) <-> (N,D(N))
M5  relation R <-> integer-coordinate incidence I
M6  N -> supp(N)
M7  N -> parity route rho(N)
M8  integer-coordinate incidence -> support-coordinate incidence
M9  (N,D(N)) -> D(N)
M10 support -> parity route
```

## Required classification

Each map must be classified using only:

```text
BIJECTION
INJECTION
SURJECTION
LOSSY PROJECTION
PARTIAL MAP
TYPED EQUIVALENCE
```

A map may receive more than one typed description only when the domain restriction or retained labels are stated explicitly.

## Proof obligations

For each map provide:

1. typed domain and codomain;
2. definition;
3. retained labels;
4. inverse formula or proof that no inverse exists;
5. injectivity status;
6. surjectivity status relative to the declared codomain;
7. fiber description when noninjective;
8. one admitted witness of loss where available;
9. dependency on WP-1 claim IDs;
10. honest classification.

## Composition audit

The artifact must test at least these compositions:

```text
N -> nu(N) -> N
(N,p,q) -> (N,Delta) -> (N,p,q)
(N,R_2(N)) -> (N,D(N)) -> (N,R_2(N))
N -> supp(N) -> parity route
integer incidence -> support incidence -> route-conditioned incidence
(N,D(N)) -> D(N) -> attempted reconstruction
```

The final composition must explicitly show why discarding `N` destroys general invertibility.

## Loss-fiber audit

Describe fibers of:

```text
N -> supp(N)
N -> parity route
(N,D(N)) -> D(N)
integer owners -> support owners
support -> parity route
```

No new fiber counts may be computed. Only exact descriptions and already-admitted witnesses may be used.

## Required artifact

```text
research/pvg-space-deepening/engine-006-reconstruction-loss-map.md
```

## Prohibitions

```text
new numerical experiment = false
new dataset = false
new finite count = false
cap/support expansion = false
weighting/asymptotics = false
classifier work = false
new theorem target = false
novelty promotion = false
WP-4 = false
Phase D = false
```

## Scientific classification

```text
map definitions = IDENTITY
inverse and noninvertibility proofs = PROVED
previous frozen witnesses = FINITE-VERIFIED only where cited
geometric diagram language = INTERPRETATION
independent-theory status = OPEN
```

## Stop and return rule

Stop after the required artifact is complete and return to ENGINE-006 parent review. WP-4 is not authorized automatically.
