# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002-LOCAL-NEIGHBORHOOD + PASS-003-PRIME-PAIR-EDGE-ATLAS
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

## Installed on the branch

- `maps/pvg-point-classification-and-inverse-geometry-v1.md`
- `maps/pvg-local-neighborhood-and-axis-ratio-geometry-v1.md`
- `research/pvg-space-deepening/README.md`
- `research/pvg-space-deepening/pass-003-prime-pair-edge-atlas.md`
- `research/pvg-space-deepening/data/prime-pair-edge-atlas-primes-le-100-summary.json`
- `tools/pvg_inverse_geometry.py`
- `tools/pvg_local_neighborhood.py`
- `tools/pvg_prime_pair_edge_atlas.py`
- `tools/sync_pvg_inverse_geometry_worktree.ps1`
- `tests/test_pvg_inverse_geometry.py`
- `tests/test_pvg_local_neighborhood.py`
- `tests/test_pvg_prime_pair_edge_atlas.py`
- `.github/workflows/pvg-inverse-geometry-audit.yml`
- `governance/programs/PVG-INVERSE-GEOMETRY-001.md`

## Pass-001 exact capability

For a complete certified factorization, emit an exact labeled geometric passport containing
support, \(\omega\), \(\Omega\), radical, repeat depth, exponent partition, minimal face,
horizontal barycentric coordinates, primitive ray, divisor box, multiple-cone anchor, and
directional families.

## Pass-002 exact capability

For a completely factored point in an \(s\)-axis face:

- compute the axis-ratio matrix \(p_j/p_i\);
- generate all \(s(s-1)\) ordered primitive horizontal neighbors;
- identify the fixed-level direction lattice \(A_{s-1}\);
- generate complete pair-lines through the point as finite geometric sequences;
- compute axis-parallel and primitive-ray sequences;
- compute horizontal simplex vertices;
- recover adjacent local axes from gcd-reduced pairs;
- compute horizontal graph distance from valuation vectors;
- expose normalized sum, difference, gcd, and lcm edge signatures.

## Pass-003 exact capability

For every unordered prime-axis pair \(p<q\le100\):

- record the axis ratio \(q/p\), gap \(q-p\), and sum \(p+q\);
- verify
  \[
  \frac{q-p}{q+p}=\frac{q/p-1}{q/p+1};
  \]
- factor the reduced sum and difference transitions;
- record \(\omega\), \(\Omega\), support, and level defects
  \[
  \kappa_+=\Omega(p+q)-1,\qquad \kappa_-=\Omega(q-p)-1;
  \]
- verify that reduced transitions avoid the two original edge axes;
- verify the axis-2 routing and sum-difference gcd laws;
- classify sum, difference, and simultaneous level preservation;
- regenerate a 300-record CSV and compare its JSON summary semantically with the committed summary.

## Exact PASS-003 findings

```text
PRIMES <= 100 = 25
UNORDERED PAIRS = 300
EDGES INVOLVING AXIS 2 = 24
ODD-ODD EDGES = 276
SUM PRESERVED = 8
DIFFERENCE PRESERVED = 16
DIFFERENCE DOWN = 1, namely (2,3)
BOTH PRESERVED = 1, namely (2,5)
```

Universal classifications:

\[
\kappa_+(p,q)=0
\iff
p=2\text{ and }q+2\text{ is prime},
\]

\[
\kappa_-(p,q)=0
\iff
q-p\text{ is prime},
\]

and

\[
\kappa_+(p,q)=\kappa_-(p,q)=0
\iff
(p,q)=(2,5).
\]

These are elementary exact identities and classifications, not originality claims.

## Hard boundaries

Exact point or neighborhood geometry is not emitted without complete certified factorization.
Factorization remains the computational inverse bottleneck. Neighbor/gcd experiments are
exploratory diagnostics only until they beat appropriate classical baselines under a preregistered
benchmark. The bound-100 edge counts are finite diagnostics and support no asymptotic inference.
Visualization creates no theorem novelty, analytic estimate, or originality certificate.

## PowerShell synchronization correction

The first user-side run exposed a collision between the function parameter `$Args` and
PowerShell's automatic `$args` variable. The wrapper was corrected to use `$GitArgs`. Python
output/exit-code handling and cross-platform temporary-directory handling were also corrected. CI
executes the complete worktree-sync script, including PASS-003 generation, rather than checking
syntax alone.

## Validation on pre-closure head

```text
HEAD = 36c3ec42a2cb94ef0de1c5000776ead641bd4f1d
PVG Inverse Geometry Audit run 25 = PASS
Governance Required Gate run 617 = PASS
Python = 3.12
Inverse-geometry tests = 11/11 PASS
Local-neighborhood tests = 11/11 PASS
Prime-pair edge-atlas tests = 14/14 PASS
Combined deterministic tests = 36/36 PASS
Exact passport smoke test (n=900) = PASS
Local-neighborhood smoke test (n=30) = PASS
Prime-pair CSV records = 300
Committed/generated summary comparison = PASS
PowerShell worktree-sync syntax = PASS
PowerShell worktree-sync execution with PASS-003 = PASS
Large unfactored input refusal gate (n=2^64) = PASS
```

PR #63 remains draft and unmerged pending human review and explicit authorization. The
structural-laboratory branch, canonical worktree branch, and protected recovery stash remain
outside this branch and were not touched.
