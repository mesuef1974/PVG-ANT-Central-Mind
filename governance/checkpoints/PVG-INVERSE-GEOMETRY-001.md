# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002 + PASS-003 + PASS-004 + PASS-005-PRIME-TRIANGLE-DYNAMICS
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

## Installed capabilities

### PASS-001 — exact point passport

Exact support, `omega`, `Omega`, exponent shape, primitive ray, divisor box, multiple cone, barycentric position, and certified inverse geometry.

### PASS-002 — local neighborhood

Axis ratios, primitive neighbors, root-lattice directions, gcd axis recovery, horizontal distance, pair-lines, simplex vertices, and geometric-mean identities.

### PASS-003 — 300 prime-pair edges

For all `p<q<=100`, classify ratios, gaps, sums, differences, supports, level defects, axis-2 routing, and preservation classes.

### PASS-004 — 2300 prime-axis triangles

For all `p<q<r<=100`, verify ratio and normalized-gap composition, closed holonomy, vertex recovery, axis-2 routing, and `Sx_Dy` profiles.

### PASS-005 — triangle transforms

For every registered prime triangle, encode

\[
T_-(p,q,r)=(q-p,r-q,r-p)
\]

and

\[
T_+(p,q,r)=(p+q,q+r,p+r).
\]

The installed exact classification is:

- `T_-` is invariant under common translation and loses absolute position;
- `T_+` is injective and exactly invertible from the three labeled pair sums;
- the common gcd of the sum triple is `2` for all-odd source triangles and `1` for triangles containing axis `2`;
- `T_+` never produces three prime values;
- `T_-` produces a distinct prime triangle only from `(2,5,7)`;
- the unique prime-triangle transition is
  `(2,5,7) -> (2,3,5)`, followed by terminal triple `(1,2,3)`;
- no prime-triangle cycle exists.

## Finite PASS-005 counts

```text
PRIME DIFFERENCES PER TRIANGLE
0 = 1969
1 = 295
2 = 35
3 = 1

PRIME SUMS PER TRIANGLE
0 = 2144
1 = 128
2 = 28
3 = 0

PRIME DIFFERENCE TRIANGLES = 1
DETECTED CYCLES = 0
```

The committed deterministic summary is
`research/pvg-space-deepening/data/prime-triangle-dynamics-primes-le-100-summary.json`.

## Hard boundaries

All atlases are finite diagnostics at prime bound `100`. They provide no asymptotic estimate, factorization speedup, originality certificate, or progress on Goldbach, RH, or GRH. Exact inverse geometry still requires complete certified factorization.

## Validation on pre-closure head

```text
HEAD = 1b53d83a9e3de038daeaa1c09fdaa6f93b6568cc
PVG Inverse Geometry Audit run 42 = PASS
Governance Required Gate run 634 = PASS
Python = 3.12
PASS-001 tests = 11/11 PASS
PASS-002 tests = 11/11 PASS
PASS-003 tests = 14/14 PASS
PASS-004 tests = 14/14 PASS
PASS-005 tests = 13/13 PASS
Combined deterministic tests = 63/63 PASS
Prime-pair records = 300
Prime-triangle records = 2300
Triangle-dynamics records = 2300
All committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored exact-input refusal = PASS
```

PR #63 remains draft and unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain untouched.
