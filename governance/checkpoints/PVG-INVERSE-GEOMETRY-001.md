# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002 + PASS-003 + PASS-004 + PASS-005 + PASS-006 + PASS-007-GENERAL-PRIME-SIMPLEX-LAWS
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

## Installed capability ladder

### PASS-001 — exact point passport

Exact support, `omega`, `Omega`, exponent shape, primitive ray, divisor box, multiple cone, barycentric position, and certified inverse geometry.

### PASS-002 — local neighborhood

Axis ratios, primitive neighbors, root-lattice directions, gcd axis recovery, horizontal distance, pair-lines, simplex vertices, and geometric-mean identities.

### PASS-003 — prime-pair edges

For all `p<q<=100`, classify ratios, gaps, sums, differences, supports, level defects, axis-2 routing, and preservation classes.

### PASS-004 — prime-axis triangles

For all `p<q<r<=100`, verify ratio and normalized-gap composition, closed holonomy, pair-sum recovery, axis-2 routing, and preservation profiles.

### PASS-005 — triangle dynamics

Classify difference and sum transforms. The unique prime-triangle difference transition is `(2,5,7)->(2,3,5)`, followed by terminal `(1,2,3)`, with no prime-triangle cycle.

### PASS-006 — prime-axis tetrahedra

For all `p<q<r<s<=100`, verify six-edge and four-face compatibility, path independence, pair-sum recovery, axis-2 routing, and preservation profiles across `12650` tetrahedra.

### PASS-007 — general prime-simplex laws

For arbitrary ordered distinct prime axes

\[
p_1<\cdots<p_m,
\qquad m\ge2,
\]

install the common law:

- support dimension `m-1` and horizontal root lattice `A_(m-1)`;
- `k`-face count `C(m,k+1)` and total nonempty face count `2^m-1`;
- edge count `C(m,2)` and ordered interior degree `m(m-1)`;
- path-independent ratio transport;
- `m-1` independent consecutive-gap coordinates;
- reconstruction from one anchor and the consecutive gaps;
- exact reconstruction from all labeled pair sums for `m>=3`;
- pair-sum gcd rule for `m>=3`;
- general axis-2 transition-routing counts;
- universal sum-preserving-edge ceiling `m-1`;
- normalized-gap composition on every triangular subface.

## Exact general reconstruction law

Let

\[
s_{ij}=p_i+p_j,
\qquad
S=\sum_{i=1}^m p_i,
\qquad
E=\sum_{i<j}s_{ij}.
\]

Since every vertex occurs in `m-1` pair sums,

\[
E=(m-1)S,
\qquad
S=\frac{E}{m-1}.
\]

If

\[
I_i=\sum_{j\ne i}s_{ij},
\]

then

\[
I_i=(m-2)p_i+S,
\]

and for `m>=3`,

\[
\boxed{p_i=\frac{I_i-S}{m-2}}.
\]

The edge case `m=2` is correctly excluded: one pair sum does not determine two separate vertices, and the global pair-sum gcd rule is not available from one edge alone.

## Exact general axis-2 routing

For all-odd prime vertices, all

\[
m(m-1)
\]

reduced sum/difference transitions contain axis `2`.

If axis `2` is a vertex, then

\[
2(m-1)
\]

transitions on incident edges exclude axis `2`, while

\[
(m-1)(m-2)
\]

transitions on odd-odd edges contain it.

## Installed files

```text
tools/pvg_prime_simplex_general.py
tools/pvg_prime_simplex.py
tests/test_pvg_prime_simplex_general.py
research/pvg-space-deepening/pass-007-general-prime-simplex-laws.md
```

`tools/pvg_prime_simplex.py` is the canonical boundary-correct command interface. The lower-level module remains an internal implementation layer.

## Hard boundaries

The general laws are elementary exact identities and geometric reinterpretations. They provide no asymptotic estimate, factorization speedup, originality certificate, or progress on Goldbach, RH, or GRH. The pass does not authorize a five-axis finite atlas or expansion beyond prime bound `100`.

## Validation on pre-closure head

```text
HEAD = 9814a1b9da16be1a77f6f510385fd10e5321b511
PVG Inverse Geometry Audit run 57 = PASS
Governance Required Gate run 649 = PASS
Python = 3.12
PASS-001 tests = 11/11 PASS
PASS-002 tests = 11/11 PASS
PASS-003 tests = 14/14 PASS
PASS-004 tests = 14/14 PASS
PASS-005 tests = 13/13 PASS
PASS-006 tests = 12/12 PASS
PASS-007 tests = 14/14 PASS
Combined deterministic tests = 89/89 PASS
General simplex smoke test = PASS
Prime-pair records = 300
Prime-triangle records = 2300
Triangle-dynamics records = 2300
Prime-tetrahedron records = 12650
All committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored exact-input refusal = PASS
```

PR #63 remains draft and unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain untouched.
