# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS030.

## Scope

- PASS001–PASS030 research reports: 30
- Python programs and reproducibility tests: 38
- Saved JSON experiment outputs: 48
- Figures: 1
- Preregistered diagnostic protocols: 7
- Retained source artifacts before this archive index: 124

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

PASS030 is complete. Its equal-rank sum-aware subspace protocol, implementation, and tests were committed before the locked analysis.

Forcing the normalized all-ones direction into every PASS029 rank budget preserves the scalar orbit sum exactly, but costs too much held-out vector structure:

- constrained vector skill: 0.493599;
- unconstrained PASS029 vector skill: 0.676575;
- absolute vector-skill loss: 0.182977;
- constrained-random p-value: 0.001200;
- modulus-level constrained vector skill >= 0.50 in 3/7 moduli.

The sum direction alone carries only 0.0447% of aggregate held-out vector energy, yet it is essential for the scalar cancellation. The locked equal-rank claim is rejected.

The next proposed diagnostic is PASS031: add the sum direction as one extra coordinate beyond the original PASS029 rank, and test whether this recovers the vector geometry while preserving the scalar sum.

## Reproduction

```bash
python code/avrg_pass030.py
python -m unittest discover -v -s code -p 'test_avrg_pass030.py'
```
