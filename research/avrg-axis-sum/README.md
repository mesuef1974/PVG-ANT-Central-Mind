# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS027.

## Scope

- PASS001–PASS027 research reports: 27
- Python programs and reproducibility tests: 32
- Saved JSON experiment outputs: 45
- Figures: 1
- Preregistered diagnostic protocols: 4
- Retained source artifacts before this archive index: 109

PASS001–PASS004 are preserved as full research reports containing their finite calculations and derivations. Standalone scripts were first retained from PASS005 onward. No missing standalone PASS001–PASS004 scripts are claimed.

## Layout

- `reports/`: the Arabic research reports in chronological order.
- `code/`: executable Python programs, plotting code, artifact builders, and tests.
- `results/`: all retained JSON outputs, including sampled, full-window, and held-out runs.
- `figures/`: generated static figures.
- `protocols/`: diagnostic protocols fixed before the corresponding detailed analysis.
- `site/`: publication record for the PASS023 reader page.
- `MANIFEST.json` and `SHA256SUMS.txt`: exact inventory and integrity hashes.

## Scientific ceiling

This archive contains finite computational diagnostics, structural reformulations, refutations of intermediate empirical laws, and reproducible evidence. It contains no asymptotic proof, no proof of Goldbach, and no claim of direct progress toward a proof of Goldbach.

## Current stopping point

PASS027 is complete. Its protocol, implementation, and tests were committed before the locked residue-difference computation.

For on states (`r | N`), the exact decomposition by `b = alpha - beta (mod r)` proves that the complete `b=0` channel is character-independent. The true diagonal is character-independent as well, so every within-modulus character variation in on energy comes from nonzero difference orbits.

The locked 16-value sample did not represent full-window on-energy variation well enough:

- centered-log correlation: 0.108518 (required at least 0.90);
- median absolute relative error: 0.198465 (required at most 0.10);
- all algebraic closure and independence checks were at machine precision.

Accordingly, PASS027 issues no concentration classification. The orbit allocations are retained as exploratory diagnostics only.

The next proposed diagnostic is PASS028: preregister a deterministic sample-size convergence ladder and establish a calibrated sample size before attempting residue-orbit concentration again.

## Reproduction

```bash
python code/avrg_pass027.py
python -m unittest discover -v -s code -p 'test_avrg_pass027.py'
```
