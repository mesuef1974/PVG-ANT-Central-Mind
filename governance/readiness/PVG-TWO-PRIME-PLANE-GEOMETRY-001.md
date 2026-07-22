# Readiness — PVG Two-Prime Plane Geometry 001

```text
Program ID: PVG-TWO-PRIME-PLANE-GEOMETRY-001
Operational goal: GOAL-OP-TWO-PRIME-PLANE-GEOMETRY-001
Date: 2026-07-23
Decision: READY
Status: ACTIVE_CURRENT
Parent program: GOAL-PVG-INVERSE-GEOMETRY-001
Foundation parent: GOAL-PVG-FOUNDATIONS-001
Computational parent: GOAL-PVG-COMPUTATIONAL-LAB-001
Engine assignment: NONE — independent native-plane track
```

## Owner directive

The active research front returns to the native geometry of PVG itself. The first governed case is the complete labeled face on the prime axes `2` and `3`:

\[
\mathcal P_{2,3}=\{2^a3^b:a,b\in\mathbb Z_{\ge0}\}
\longleftrightarrow
\mathbb Z_{\ge0}^2.
\]

The route studies the plane before any move to three prime axes.

## Separation from existing engines

```text
ENGINE-004 PASS-004 = PAUSED_BY_OWNER / retained / not closed
ENGINE-005 = CANDIDATE / inactive
PVG-TWO-PRIME-PLANE-GEOMETRY-001 = ACTIVE_CURRENT
```

This track does not reuse an ENGINE-004 pass number, certificate namespace, frozen box, or prime-fiber data contract. It does not activate ENGINE-005 and does not authorize Phase D.

## Exact objects authorized

1. The labeled lattice point `(a,b)` and integer `2^a3^b`.
2. The monoid law induced by multiplication.
3. The group completion on `Z^2` and positive rationals supported on `{2,3}`.
4. Coordinatewise divisibility, gcd, lcm, divisor boxes, and multiple cones.
5. `Omega=a+b` layers and axis-step path multiplicities.
6. Primitive rays, radial index, projective slope, and ray-layer periods.
7. Determinants, lattice areas, unimodular adjacency, Farey neighbors, mediants, and Stern–Brocot organization.
8. Parallelogram product identities.
9. Manhattan, Euclidean, logarithmic, and weighted logarithmic metrics.
10. Exact finite geometry under `2^a3^b <= X`.
11. Geometric versus prime-weighted axis-swap symmetry.
12. A dedicated interactive plane inside PVG Explorer.

## Frozen finite verification box

```text
coordinate cap: 0 <= a,b <= 12
layer cap: a+b <= 12
numeric cap: X = 10^12
```

These caps are diagnostic and reproducibility choices. They are not canonical constants and support no asymptotic inference.

## Required deliverables

- `research/pvg-space-deepening/pvg-two-prime-plane-geometry-001.md`
- `tools/pvg_two_prime_plane.py`
- `tests/test_pvg_two_prime_plane.py`
- `tests/test_pvg_two_prime_plane_explorer.py`
- `research/pvg-space-deepening/data/two-prime-plane-summary.json`
- `web/pvg-pareto-explorer/two-prime-plane.html`
- `web/pvg-pareto-explorer/assets/two-prime-plane.js`
- `tools/open_pvg_two_prime_plane.ps1`
- dedicated CI audit
- current-state, capability-map, goal-memory, and research-compass synchronization

## Claim classes

Every result must be labeled from:

```text
IDENTITY
PROVED
FINITE-VERIFIED
INTERPRETATION
HYPOTHESIS
OPEN
```

Classical Farey, Stern–Brocot, determinant, lattice-area, binomial, and totient facts are used without an originality claim. A separate literature audit is mandatory before any historical-priority statement.

## Stop rules

A separate readiness or Stage Review is required before:

- moving to the `2,3,5` three-axis simplex as the active object;
- claiming the two-prime plane study complete;
- promoting working terminology into the frozen ontology;
- opening asymptotic counting, density, equidistribution, or Diophantine-approximation claims;
- treating finite pictures as general proofs;
- reactivating ENGINE-004, ENGINE-005, the theorem route, or an ANT target;
- claiming a primality test or progress on Goldbach, PNT, RH, or GRH;
- claiming historical originality or publication readiness.

## Readiness conclusion

The object is exact, bounded verification is defined, the parent goals and return gate are explicit, and the new route is cleanly separated from ENGINE-004 and ENGINE-005.

**Decision: READY.**
