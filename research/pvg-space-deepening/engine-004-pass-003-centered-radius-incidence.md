# ENGINE-004 PASS-003 — Centered-Radius Incidence Geometry

```text
Goal: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Scope: unchanged frozen 884-point box
Status: implementation checkpoint / CI pending
Phase D: NOT AUTHORIZED
```

## 1. Static incidence object

For the governed spectrum \(D(N)\), define

\[
\mathcal O(d)=\{N:d\in D(N)\},
\qquad
\mathcal F(d)=\{\operatorname{supp}(N):N\in\mathcal O(d)\}.
\]

The bipartite incidence graph has represented integers on one side and governed coordinates on the other, with an edge \(N\sim d\) exactly when \(d\in D(N)\). This is a static finite representation only; no iteration, orbit, basin, transition, or Phase-D object is introduced.

**Classification:** `IDENTITY / PROVED` for the definitions and exact reconstruction properties.

## 2. Exact recovery and projection

The coordinate-owner incidence relation recovers every nonempty spectrum by row restriction:

\[
D(N)=\{d:N\in\mathcal O(d)\}.
\]

Projection from integer owners to support owners is surjective by definition but need not be injective. Therefore

```text
same coordinate ≠ same pair
same coordinate ≠ same midpoint
same coordinate ≠ same integer
same support owner ≠ same integer owner
```

## 3. Complete frozen-box certificate

```text
integer points                              = 884
represented points                          = 745
coordinate occurrences                      = 218024
unique coordinates                          = 36797
shared coordinates                          = 27799
cross-route coordinates                     = 85
coordinates collapsing multiple integers
  onto one support face                     = 22423
support pairs with nonzero intersection     = 131
co-occurring coordinate-pair occurrences    = 78736278
bipartite connected components              = 12
```

Route partition:

```text
even-only coordinates = 36702
odd-only coordinates  = 10
cross-route coordinates = 85
```

The maximum integer-owner degree is

\[
|\mathcal O(7)|=64.
\]

The maximum support-owner degree is \(8\), attained exactly by

\[
d\in\{3,51,2691,3021\}.
\]

The largest support-pair coordinate intersection is between supports

\[
\{2,3,5\}
\quad\text{and}\quad
\{2,3,7\},
\]

with 9,904 shared governed coordinates inside the frozen box.

**Classification:** `FINITE-VERIFIED` in the registered box only.

## 4. Component structure

The static bipartite graph has 12 connected components:

- one component with 620 integers and 22,828 coordinates;
- one component with 115 integers and 13,959 coordinates;
- ten isolated one-integer/one-coordinate components.

Connectivity here is only a finite incidence invariant. It is not orbit dynamics and carries no assertion outside the registered domain.

## 5. Co-occurrence certificate

The complete coordinate co-occurrence relation is stored losslessly through the sorted nonempty hyperedge rows

```text
N:D(N)
```

because every unordered coordinate pair co-occurring at \(N\) is reconstructed from that row. The 745-row canonical encoding has SHA-256

```text
ca63d9767c96fe16593666586be6996868bb68d9e32c52a233f0e779292a8512
```

The compact generated summary has SHA-256

```text
3ded4b917a6d443bd27e80a0e5658f17f477a7808bcc28ae442ce97cf7e290d2
```

## 6. Independent verification

The production route indexes the certified spectra. The independent route rescans every prime pair and derives its governed coordinate directly from parity and the prime gap. The two routes agree on all owner, support, route, and spectrum indexes.

```text
independent index mismatches = 0
odd-route owner injectivity = PASS
row reconstruction = PASS
deterministic ordering = PASS
```

## 7. Claim ceiling

This pass does not establish or claim:

- an asymptotic law for coordinate degrees;
- a power law, logarithmic law, or monotonicity relation;
- graph dynamics, orbits, basins, or attractors;
- cap or support expansion;
- historical originality or publication readiness;
- a new lemma or theorem;
- Goldbach, PNT, RH, or GRH progress.

The numerical degree distributions are complete finite data, not evidence promoted to a global law.
