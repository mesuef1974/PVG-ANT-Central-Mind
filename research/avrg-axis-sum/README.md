# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS034.

## Scope

- PASS001–PASS034 research reports: 34
- Python programs and reproducibility tests: 46
- Saved JSON experiment outputs: 52
- Figures: 1
- Preregistered diagnostic protocols: 11
- Retained research artifacts: 144

PASS001–PASS004 are preserved as full research reports containing their finite calculations and derivations. Standalone scripts were first retained from PASS005 onward. No missing standalone PASS001–PASS004 scripts are claimed.

## Layout

- `reports/`: the Arabic research reports in chronological order.
- `code/`: executable Python programs, plotting code, artifact builders, and tests.
- `results/`: retained JSON outputs, including sampled, full-window, and held-out runs.
- `figures/`: generated static figures.
- `protocols/`: diagnostic protocols fixed before the corresponding detailed analysis.
- `site/`: publication record for the PASS023 reader page.
- `MANIFEST.json` and `SHA256SUMS.txt`: archive inventory and integrity hashes; these are refreshed at consolidation checkpoints.

## Scientific ceiling

This archive contains finite computational diagnostics, structural reformulations, refutations of intermediate empirical laws, and reproducible evidence. It contains no asymptotic proof, no proof of Goldbach, and no claim of direct progress toward a proof of Goldbach.

## Current stopping point

PASS034 is complete. Its protocol, implementation, tests, and GitHub Actions workflow were committed before the locked 5,000-permutation outcome was computed.

PASS034 tested whether the five cancellation functionals per modulus lie in a stable rank-two plane despite the absence of a stable signed direction in PASS033.

Locked global metrics:

- mean rank-one projection score: 0.591932;
- mean rank-two projection score: 0.784602;
- mean gain over rank one: 0.192671;
- folds with rank-two score at least 0.60: 29/35;
- restricted-null mean: 0.705393;
- restricted-permutation p-value: 0.038792.

Four of the five preregistered conditions passed, but the locked significance condition required p <= 0.01. The decision is therefore:

```text
no_stable_rank2_functional_plane_under_locked_rule
```

The correct interpretation is narrower than a geometric null: a strong finite rank-two signal is present, but it is not sufficiently distinguished from the overlap-preserving null under the locked rule. The early held-out window e=15 is markedly weaker than e=16..19, motivating a preregistered temporal-regime test rather than an automatic increase in rank.

## Reproduction

```bash
python code/avrg_pass034.py
python -m unittest discover -v -s code -p 'test_avrg_pass034.py'
```
