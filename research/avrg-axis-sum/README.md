# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS025.

## Scope

- PASS001–PASS025 research reports: 25
- Python programs and reproducibility tests: 28
- Saved JSON experiment outputs: 43
- Figures: 1
- Preregistered diagnostic protocols: 2
- Retained source artifacts before this archive index: 99

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

PASS025 is complete. Its protocol and executable analysis were committed before computing the new held-out window e=19.

The sole preregistered phase predictor, centered `Re chi_k(2^e)`, failed on the holdout:

- phase skill versus zero: -0.113830 (required > 0.10);
- phase SSE was lower than the static-signature SSE: 0.110647 < 0.118146;
- global permutation p-value: 0.376876 (required <= 0.05).

The larger-modulus mean-ratio phenomenon nevertheless persisted: for r=23,29,31 in e=19, the mean of modulus means was 1.995274.

The next proposed diagnostic is PASS026: use the exact identity
`log rho = log E_on - log E_off` to determine whether window-dependent character variation is driven primarily by the on-energy channel or by the off-mode cancellation budget.

## Reproduction

Fast checks:

```bash
python -m unittest discover -v -s code -p 'test_avrg_pass*.py'
```

PASS025:

```bash
python code/avrg_pass025_holdout.py --progress
python code/avrg_pass025.py
python -m unittest discover -v -s code -p 'test_avrg_pass025.py'
```
