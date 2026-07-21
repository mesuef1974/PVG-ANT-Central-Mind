# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASSES = PASS-001 + PASS-002-LOCAL-NEIGHBORHOOD
BRANCH = agent/pvg-point-classification-inverse-geometry-001
BASE = main
STATUS = CHECKPOINT_PASS_ON_BRANCH
PR = 63
ONTOLOGY-V1 = UNCHANGED
NEW-THEOREM-TARGET = NOT_AUTHORIZED
DATASET-004 = NOT_AUTHORIZED
LEAN-EXPANSION = NOT_AUTHORIZED
MERGE = NOT_AUTHORIZED
```

## Installed on the branch

- `maps/pvg-point-classification-and-inverse-geometry-v1.md`
- `maps/pvg-local-neighborhood-and-axis-ratio-geometry-v1.md`
- `research/pvg-space-deepening/README.md`
- `tools/pvg_inverse_geometry.py`
- `tools/pvg_local_neighborhood.py`
- `tools/sync_pvg_inverse_geometry_worktree.ps1`
- `tests/test_pvg_inverse_geometry.py`
- `tests/test_pvg_local_neighborhood.py`
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

## Hard boundaries

Exact point or neighborhood geometry is not emitted without complete certified factorization.
Factorization remains the computational inverse bottleneck. Neighbor/gcd experiments are
exploratory diagnostics only until they beat appropriate classical baselines under a preregistered
benchmark. Visualization creates no theorem, analytic estimate, or originality certificate.

## Validation on pre-closure head

```text
HEAD = de0ae8c3e1aa652c7fdce1febaafef298367c582
PVG Inverse Geometry Audit run 11 = PASS
Governance Required Gate run 603 = PASS
Python = 3.12
Inverse-geometry tests = 11/11 PASS
Local-neighborhood tests = 11/11 PASS
Combined deterministic tests = 22/22 PASS
Exact passport smoke test (n=900) = PASS
Local-neighborhood smoke test (n=30) = PASS
PowerShell worktree-sync syntax = PASS
Large unfactored input refusal gate (n=2^64) = PASS
```

The closure commit changes only this checkpoint state. PR #63 remains draft and unmerged pending
human review and explicit authorization. The structural-laboratory branch and protected recovery
stash remain outside this branch and were not touched.
