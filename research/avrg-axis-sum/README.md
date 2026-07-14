# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS029.

## Scope

- PASS001–PASS029 research reports: 29
- Python programs and reproducibility tests: 36
- Saved JSON experiment outputs: 47
- Figures: 1
- Preregistered diagnostic protocols: 6
- Retained source artifacts before this archive index: 119

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

PASS029 is complete. Its held-out-window subspace protocol, implementation, and tests were committed before the locked analysis.

A training-only SVD subspace captures nonzero-orbit vectors across held-out windows better than equal-rank random subspaces:

- weighted rank fraction: 0.466667;
- held-out vector skill: 0.676575;
- random-subspace p-value: 0.000200;
- modulus-level vector skill >= 0.50 in 7/7 moduli.

However, the same projections fail to reconstruct the scalar sum of the orbit contributions: scalar skill = -0.480997, negative in all seven moduli. The preregistered five-condition rule therefore rejects a stable low-dimensional subspace that also preserves on-energy variation.

The result separates stable vector geometry from the cancellation-sensitive sum direction.

The next proposed diagnostic is PASS030: compare equal-rank bases that explicitly preserve or supervise the orbit-sum direction against the unsupervised SVD basis under held-out windows.

## Reproduction

```bash
python code/avrg_pass029.py
python -m unittest discover -v -s code -p 'test_avrg_pass029.py'
```
