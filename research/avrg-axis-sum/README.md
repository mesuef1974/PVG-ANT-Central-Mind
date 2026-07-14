# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS023.

## Scope

- PASS001–PASS023 research reports: 23
- Python programs and reproducibility tests: 23
- Saved JSON experiment outputs: 40
- Figures: 1
- Retained source artifacts before this archive index: 87

PASS001–PASS004 are preserved as full research reports containing their finite calculations and derivations. Standalone scripts were first retained from PASS005 onward. No missing standalone PASS001–PASS004 scripts are claimed.

## Layout

- `reports/`: the Arabic research reports in chronological order.
- `code/`: executable Python programs, plotting code, artifact builder, and tests.
- `results/`: all retained JSON outputs, including sampled and full-window runs.
- `figures/`: generated static figures.
- `site/`: publication record for the PASS023 reader page.
- `MANIFEST.json` and `SHA256SUMS.txt`: exact inventory and integrity hashes.

## Scientific ceiling

This archive contains finite computational diagnostics, structural reformulations, refutations of intermediate empirical laws, and reproducible evidence. It contains no asymptotic proof, no proof of Goldbach, and no claim of direct progress toward a proof of Goldbach.

## Current stopping point

PASS023 is complete. The next proposed diagnostic is PASS024, separating modulus scale from character variation:

\[
\rho_{e,r,k}=2+\frac{A_e}{r}+G_r(k)+\varepsilon_{e,r,k}.
\]

## Reproduction

The latest fast checks are:

```bash
python -m unittest discover -v -s code -p 'test_avrg_pass*.py'
```

PASS023 can be recomputed with the commands recorded in `reports/AVRG-Research-Pass-023-Multi-Window-Larger-Moduli-Stability-ar.md`.
