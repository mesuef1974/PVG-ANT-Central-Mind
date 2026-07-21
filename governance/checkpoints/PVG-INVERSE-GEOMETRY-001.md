# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 ... PASS-010-LEVEL-FLOW-DYNAMICS
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
- PASS-002: local neighborhoods, axis ratios, and gcd recovery.
- PASS-003: prime-pair edge transitions through `100`.
- PASS-004: prime-axis triangle composition.
- PASS-005: triangle sum/difference dynamics.
- PASS-006: prime-axis tetrahedron geometry.
- PASS-007: general `m`-axis simplex laws.
- PASS-008: arithmetic gradients on one horizontal edge.
- PASS-009: global scalar terrain on one fixed level.
- PASS-010: strict flows, plateaus, sinks, and ascent basins induced by scalar fields.

## PASS-010 registered scope

```text
AXES = 2,3,5
OMEGA LEVEL = 6
DIMENSION = 2
POINT COUNT = 28
FIELDS = n, tau, sigma(n)/n, phi(n)/n
```

For each scalar field `f`, every primitive horizontal edge is oriented by

\[
x\to y\iff f(y)>f(x).
\]

Equal-value edges form plateau components. Contracting plateaus yields a condensation graph.

## Exact flow laws

1. Every strict flow is acyclic because `f` strictly increases along each directed edge.
2. Every plateau-condensation graph is acyclic for the same reason.
3. Every strongest-ascent path on the finite level terminates at a local maximum.
4. Strongest-ascent basins depend on deterministic tie breaking; strict sinks and plateau components do not.
5. There is no field-independent ascent direction: the same edge may point differently under different arithmetic observables.

## Exact finite results

```text
n:
  unique global minimum = (6,0,0)
  unique global maximum = (0,0,6)

tau:
  unique global maximum = (2,2,2), corresponding to 900

sigma(n)/n:
  unique global maximum = (3,2,1), corresponding to 360

phi(n)/n:
  global minimum plateau = all 10 full-support points
```

The qualitative winds are:

- `n`: moves valuation mass toward larger prime axes;
- `tau`: balances exponent mass;
- `sigma/n`: moves toward a small-prime-weighted interior balance;
- `phi/n`: is constant on support strata and changes at support boundaries.

## Installed files

```text
tools/pvg_level_flow.py
tests/test_pvg_level_flow.py
research/pvg-space-deepening/pass-010-level-flow-dynamics.md
```

The audit workflow and detached-worktree synchronizer execute PASS-010 tests and the `(2,3,5), Omega=6` flow smoke test.

## Validation on pre-closure head

```text
HEAD = 8da29a95a38753982b9bfaec8449d0bef1dfffc0
PVG Inverse Geometry Audit run 76 = PASS
Governance Required Gate run 668 = PASS
Python = 3.12
PASS-001..009 tests = 107/107 PASS
PASS-010 tests = 9/9 PASS
Combined deterministic tests = 116/116 PASS
Strict-flow acyclicity = PASS
Plateau-condensation acyclicity = PASS
Core smoke tests = PASS
All committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored exact-input refusal = PASS
```

## Scientific boundary

PASS-010 installs exact finite graph dynamics induced by declared scalar fields. It does not create a canonical differential manifold, a limiting flow theorem, an asymptotic estimate, an originality certificate, a factorization speedup, or progress on Goldbach, RH, or GRH.

The closure commit changes checkpoint state only. PR #63 remains draft and unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain untouched.
