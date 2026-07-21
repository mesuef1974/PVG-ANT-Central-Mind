# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002 + PASS-003 + PASS-004 + PASS-005 + PASS-006 + PASS-007 + PASS-008 + PASS-009-GLOBAL-LEVEL-TERRAIN
BRANCH = agent/pvg-point-classification-inverse-geometry-001
BASE = main
STATUS = CHECKPOINT_PASS_ON_BRANCH
PR = 63
ONTOLOGY-V1 = UNCHANGED
NEW-THEOREM-TARGET = NOT_AUTHORIZED
DATASET-004 = NOT_AUTHORIZED
LEAN-EXPANSION = NOT_AUTHORIZED
BOUND-EXPANSION = NOT_AUTHORIZED
MERGE = NOT_AUTHORIZED
```

## Capability ladder

- PASS-001: exact point passport and certified inverse geometry.
- PASS-002: local neighborhoods, axis ratios, root-lattice directions, and gcd recovery.
- PASS-003: 300 prime-pair edge transitions for `p<q<=100`.
- PASS-004: 2300 prime-axis triangles and composition laws.
- PASS-005: sum/difference triangle dynamics.
- PASS-006: 12650 prime-axis tetrahedra.
- PASS-007: general `m`-axis simplex laws.
- PASS-008: exact arithmetic-function changes on one horizontal edge.
- PASS-009: exact global terrain on one fixed simplex level.

## PASS-009 registered scope

```text
AXES = 2,3,5
OMEGA LEVEL = 6
DIMENSION = 2
POINT COUNT = C(8,2) = 28
```

The atlas enumerates every exponent vector

\[
(a,b,c)\in\mathbb N_0^3,
\qquad a+b+c=6,
\]

and records

\[
n,\ \omega,\ \Omega,\ \tau,\ \sigma,\ \varphi,\ \mu,\ \lambda,\ \operatorname{rad},\ \sigma(n)/n,\ \varphi(n)/n.
\]

## Exact structural conclusions

1. `Omega` and Liouville `lambda=(-1)^Omega` are constant on the whole level.
2. `log n` is linear in the exponent coordinates. Thus the minimum and maximum integer values occur at the smallest- and largest-prime vertices.
3. `tau=product(a_i+1)` is a shape field. Its edge-gradient law from PASS-008 implies that balancing two exponents increases `tau`, and the global maximum occurs at the balanced exponent vectors.
4. `phi(n)/n=product_(p|n)(1-1/p)` depends only on the support stratum, not on positive exponent sizes.
5. `sigma(n)/n` depends on both exponent multiplicities and prime labels, so it defines a genuinely weighted terrain.
6. `mu` is concentrated on the squarefree skeleton, while `omega` and `rad` detect support boundaries.

## Exact finite results for axes 2,3,5 and level 6

```text
minimum n = 64 at (6,0,0)
maximum n = 15625 at (0,0,6)

minimum tau = 7 at the three vertices
maximum tau = 27 at (2,2,2), corresponding to 900

minimum sigma(n)/n = 19531/15625 at (0,0,6)
maximum sigma(n)/n = 13/4 at (3,2,1), corresponding to 360

minimum phi(n)/n = 4/15 on every full-support point
maximum phi(n)/n = 4/5 at (0,0,6)
```

## Installed files

```text
tools/pvg_level_terrain.py
tests/test_pvg_level_terrain.py
research/pvg-space-deepening/pass-009-global-level-terrain.md
```

The audit workflow and safe detached-worktree synchronization execute PASS-009 tests and the global terrain smoke test for `(2,3,5), Omega=6`.

## Validation on pre-closure head

```text
HEAD = 6a62b03d3438650f500395d5ed6b2f1d6c89211b
PVG Inverse Geometry Audit run 70 = PASS
Governance Required Gate run 662 = PASS
Python = 3.12
PASS-001 tests = 11/11 PASS
PASS-002 tests = 11/11 PASS
PASS-003 tests = 14/14 PASS
PASS-004 tests = 14/14 PASS
PASS-005 tests = 13/13 PASS
PASS-006 tests = 12/12 PASS
PASS-007 tests = 14/14 PASS
PASS-008 tests = 10/10 PASS
PASS-009 tests = 8/8 PASS
Combined deterministic tests = 107/107 PASS
Global level terrain point count = 28
Core smoke tests = PASS
All committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored exact-input refusal = PASS
```

## Scientific boundary

PASS-009 is an exact finite atlas and geometric organization of elementary arithmetic identities. It does not install an asymptotic estimate, a general extremal theorem beyond explicitly proved balancing laws, an originality certificate, a factorization speedup, or progress on Goldbach, RH, or GRH.

The closure commit changes only checkpoint state. PR #63 remains draft and unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain untouched.
