# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS032.

## Scope

- PASS001–PASS032 research reports: 32
- Python programs and reproducibility tests: 42
- Saved JSON experiment outputs: 50
- Figures: 1
- Preregistered diagnostic protocols: 9
- Retained source artifacts before this archive index: 134

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

PASS032 is complete. Its cancellation-coupling protocol, implementation, and tests were committed before the locked analysis.

A no-intercept linear map learned from four windows does not predict the cancellation coefficient from the held-out amplitude coordinates:

- aggregate scalar skill: -0.484642;
- Pearson correlation: 0.067530;
- restricted-permutation p-value: 0.672665;
- positive scalar skill in 0/7 moduli and nonnegative skill in 2/5 windows;
- sign accuracy: 0.51875.

All five preregistered conditions fail. PASS031 remains a finite subspace-containment result, but PASS032 rejects the stronger claim that its cancellation coordinate is linearly determined by the amplitude coordinates across windows.

The next proposed step is to expand or independently diagnose window stability before preregistering any more flexible coupling model.

## Reproduction

```bash
python code/avrg_pass032.py
python -m unittest discover -v -s code -p 'test_avrg_pass032.py'
```
