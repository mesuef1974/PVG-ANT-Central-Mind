# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS024.

## Scope

- PASS001–PASS024 research reports: 24
- Python programs and reproducibility tests: 25
- Saved JSON experiment outputs: 41
- Figures: 1
- Preregistered diagnostic protocols: 1
- Retained source artifacts before this archive index: 92

PASS001–PASS004 are preserved as full research reports containing their finite calculations and derivations. Standalone scripts were first retained from PASS005 onward. No missing standalone PASS001–PASS004 scripts are claimed.

## Layout

- `reports/`: the Arabic research reports in chronological order.
- `code/`: executable Python programs, plotting code, artifact builders, and tests.
- `results/`: all retained JSON outputs, including sampled and full-window runs.
- `figures/`: generated static figures.
- `protocols/`: diagnostic protocols fixed before the corresponding detailed analysis.
- `site/`: publication record for the PASS023 reader page.
- `MANIFEST.json` and `SHA256SUMS.txt`: exact inventory and integrity hashes.

## Scientific ceiling

This archive contains finite computational diagnostics, structural reformulations, refutations of intermediate empirical laws, and reproducible evidence. It contains no asymptotic proof, no proof of Goldbach, and no claim of direct progress toward a proof of Goldbach.

## Current stopping point

PASS024 is complete. It exactly separates modulus/window means from within-modulus character deviations. The preregistered stable-character-signature rule failed all three conditions:

- persistence fraction: 0.344666 (required > 0.50);
- global permutation p-value: 0.057809 (required <= 0.05);
- leave-one-window-out skill: -0.165039 (required > 0).

The next proposed diagnostic is PASS025: preregister and test whether the window-dependent character residual is organized by the endpoint phase `chi_k(2^e)`, including a genuinely held-out new window.

## Reproduction

The fast checks are:

```bash
python -m unittest discover -v -s code -p 'test_avrg_pass*.py'
```

PASS024 can be reproduced with:

```bash
python code/avrg_pass024.py
python -m unittest discover -v -s code -p 'test_avrg_pass024.py'
```
