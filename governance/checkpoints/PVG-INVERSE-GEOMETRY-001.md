# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002 + PASS-003 + PASS-004 + PASS-005 + PASS-006-PRIME-AXIS-TETRAHEDRA
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

### PASS-003 — 300 prime-pair edges

For all `p<q<=100`, classify ratios, gaps, sums, differences, supports, level defects, axis-2 routing, and preservation classes.

### PASS-004 — 2300 prime-axis triangles

Verify ratio and normalized-gap composition, closed face holonomy, vertex recovery, axis-2 routing, and `Sx_Dy` profiles.

### PASS-005 — triangle dynamics

Classify difference and sum transforms. The difference transform preserves shape but loses translation; the sum transform is injective. The unique prime-triangle difference transition is `(2,5,7)->(2,3,5)`, followed by terminal `(1,2,3)`, with no cycle.

### PASS-006 — 12650 prime-axis tetrahedra

For every `p<q<r<s<=100`:

- enumerate six edges and four triangular faces;
- verify all endpoint ratio transports are path independent;
- verify holonomy `1` on all four boundary triangles;
- verify composition of the three consecutive gaps into all longer gaps;
- reconstruct all four vertices from the six pair sums;
- verify the pair-sum gcd rule: `2` for all-odd tetrahedra and `1` when axis `2` is present;
- verify edgewise axis-2 routing on all twelve reduced sum/difference transitions;
- assign a six-edge preservation profile `Sx_Dy`;
- regenerate a deterministic 12650-record CSV and committed JSON summary.

## Exact PASS-006 reconstruction law

Let `T=p+q+r+s`. Since every vertex occurs in three pair sums,

\[
\sum_{i<j}(p_i+p_j)=3T.
\]

If `I_i` is the sum of the three pair sums incident to `p_i`, then

\[
I_i=2p_i+T,
\qquad
p_i=\frac{I_i-T}{2}.
\]

Thus the six labeled pair sums encode the tetrahedron injectively. The six differences remain invariant under common translation and require one anchor for absolute reconstruction.

## Finite PASS-006 counts

```text
PRIMES <= 100 = 25
UNORDERED TETRAHEDRA = 12650
CONTAINS AXIS 2 = 2024
ALL ODD = 10626

SUM-PRESERVED EDGES
0 = 11186
1 = 960
2 = 448
3 = 56

DIFFERENCE-PRESERVED EDGES
0 = 9386
1 = 2607
2 = 537
3 = 113
4 = 7
```

The maximum observed difference-preservation count is `4`, attained by seven bound-100 tetrahedra recorded in the committed summary. The universal maximum for sum-preserving edges is `3`, because every such edge must be incident to the unique possible vertex `2`.

## Hard boundaries

All atlases remain finite diagnostics at prime bound `100`. They provide no asymptotic estimate, factorization speedup, originality certificate, or progress on Goldbach, RH, or GRH. Exact inverse geometry still requires complete certified factorization. No move to five-axis simplices or bound expansion is authorized by this checkpoint.

## Validation on pre-closure head

```text
HEAD = 728ae1aa71575d1680ef6a8227b48ab33450083c
PVG Inverse Geometry Audit run 49 = PASS
Governance Required Gate run 641 = PASS
Python = 3.12
PASS-001 tests = 11/11 PASS
PASS-002 tests = 11/11 PASS
PASS-003 tests = 14/14 PASS
PASS-004 tests = 14/14 PASS
PASS-005 tests = 13/13 PASS
PASS-006 tests = 12/12 PASS
Combined deterministic tests = 75/75 PASS
Prime-pair records = 300
Prime-triangle records = 2300
Triangle-dynamics records = 2300
Prime-tetrahedron records = 12650
All committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored exact-input refusal = PASS
```

PR #63 remains draft and unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain untouched.
