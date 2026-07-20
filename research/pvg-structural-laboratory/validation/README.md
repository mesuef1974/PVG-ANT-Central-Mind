# Independent validation lane

This directory is the canonical, dependency-free validation lane for the external PVG Structural Laboratory v6 application.

It intentionally reimplements the calculations in Python rather than importing browser code. It verifies:

- exact arithmetic baselines;
- exact smooth-number counts on reference cases;
- non-overlapping calibration and holdout grids;
- raw and partial correlations;
- counterexamples to standalone certification by `B`;
- additive-fiber reference counts.

Run:

```bash
cd research/pvg-structural-laboratory/validation
python -m unittest -v
python pvg_lab_validation.py
```

Scientific ceiling: finite diagnostics only. No theorem, publication, Goldbach, RH, or GRH claim.
