# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002 + PASS-003 + PASS-004-PRIME-AXIS-TRIANGLES
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

Exact labeled support, `omega`, `Omega`, radical, repeat depth, exponent partition, primitive ray,
divisor box, multiple cone, barycentric position, and directional families.

### PASS-002 — local neighborhood

Axis-ratio matrix, `A_(s-1)` horizontal geometry, primitive neighbors, gcd axis recovery, horizontal
distance, pair-lines, simplex vertices, and geometric-mean identities.

### PASS-003 — 300 prime-pair edges

For all `p<q<=100`, record ratio, gap, sum, difference, transition supports, defects `kappa_+` and
`kappa_-`, axis-2 routing, and level-preservation classes.

### PASS-004 — 2300 prime-axis triangles

For all `p<q<r<=100`:

- verify `(q/p)(r/q)=r/p` and closed holonomy `1`;
- verify `(q-p)+(r-q)=r-p`;
- verify normalized-gap composition;
- recover all three vertices from pair sums;
- verify complete axis-2 routing;
- classify each triangle by `Sx_Dy` preservation profile;
- regenerate deterministic CSV and JSON outputs.

## Exact PASS-004 findings

```text
PRIMES <= 100 = 25
UNORDERED TRIANGLES = 2300
CONTAINS AXIS 2 = 276
ALL ODD = 2024

SUM-PRESERVED EDGE COUNTS
0 edges = 2144 triangles
1 edge  = 128 triangles
2 edges = 28 triangles
3 edges = 0 triangles

DIFFERENCE-PRESERVED EDGE COUNTS
0 edges = 1969 triangles
1 edge  = 295 triangles
2 edges = 35 triangles
3 edges = 1 triangle, namely (2,5,7)
```

The unique all-odd triangle with two difference-preserving edges is `(3,5,7)`. The complete profile
distribution is committed in
`research/pvg-space-deepening/data/prime-triangle-atlas-primes-le-100-summary.json`.

## Hard boundaries

The atlas is finite and deterministic. It provides no asymptotic estimate, no factorization speedup,
no novelty certificate, and no Goldbach, RH, or GRH progress. Exact inverse geometry still requires
complete certified factorization. No expansion beyond prime bound 100 is authorized here.

## Validation before closure

```text
PRE-CLOSURE HEAD = ffc579af29ce322f29e271bbfae16b03226e2b3a
PVG Inverse Geometry Audit run 28 = PASS
Governance Required Gate run 620 = PASS
Inverse-geometry tests = 11/11 PASS
Local-neighborhood tests = 11/11 PASS
Prime-pair atlas tests = 14/14 PASS
Prime-triangle atlas tests = 13/13 PASS
Combined deterministic tests = 49/49 PASS
Prime-pair records = 300
Prime-triangle records = 2300
Committed/generated summaries = PASS
Safe PowerShell worktree execution = PASS
Large unfactored input refusal = PASS
```

The closure commit changes only governed program/checkpoint metadata. PR #63 remains draft and
unmerged. The canonical worktree branch, structural-laboratory branch, and protected stash remain
untouched.
