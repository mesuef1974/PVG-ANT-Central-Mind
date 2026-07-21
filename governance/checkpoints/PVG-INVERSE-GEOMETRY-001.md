# PVG Inverse Geometry 001 — Branch Checkpoint

```text
PROGRAM = PVG-INVERSE-GEOMETRY-001
PASS = PASS-001
BRANCH = agent/pvg-point-classification-inverse-geometry-001
BASE = main
STATUS = IMPLEMENTED_ON_BRANCH_AWAITING_PR_VALIDATION
ONTOLOGY-V1 = UNCHANGED
NEW-THEOREM-TARGET = NOT_AUTHORIZED
DATASET-004 = NOT_AUTHORIZED
LEAN-EXPANSION = NOT_AUTHORIZED
```

## Installed on the branch

- `maps/pvg-point-classification-and-inverse-geometry-v1.md`
- `tools/pvg_inverse_geometry.py`
- `tests/test_pvg_inverse_geometry.py`
- `.github/workflows/pvg-inverse-geometry-audit.yml`
- `governance/programs/PVG-INVERSE-GEOMETRY-001.md`

## Exact capability

For a complete certified factorization, emit an exact labeled geometric passport containing
support, \(\omega\), \(\Omega\), radical, repeat depth, exponent partition, minimal face,
horizontal barycentric coordinates, primitive ray, divisor box, multiple-cone anchor, and
directional families.

## Hard boundary

Exact inverse location is not emitted without complete certified factorization. The program
records factorization as the computational inverse bottleneck rather than hiding it behind a
visual embedding.

## Closure condition

Change `STATUS` to `CHECKPOINT_PASS` only after the dedicated workflow, governance gate, and
review all pass on the same head commit.
