# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS028.

## Scope

- PASS001–PASS028 research reports: 28
- Python programs and reproducibility tests: 34
- Saved JSON experiment outputs: 46
- Figures: 1
- Preregistered diagnostic protocols: 5
- Retained source artifacts before this archive index: 114

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

PASS028 is complete. Its protocol, full-scan implementation, and tests were committed before computing the locked result.

FFT convolutions of the residue fibers reconstructed all 160 saved on-energy rows:

- maximum absolute relative error: 7.7841e-15;
- centered-log correlation: 1.000000;
- maximum pointwise orbit-closure error: 7.4005e-18.

Using every on-state value in the five windows, no modulus reached a top-orbit absolute attribution of 0.50. The preregistered classification is therefore that character instability is distributed across multiple nonzero residue-difference orbits.

The deterministic sample ladder first passed the PASS027 calibration thresholds stably at one-quarter coverage.

The next proposed diagnostic is PASS029: test whether the distributed nonzero-orbit pattern nevertheless has a stable low-dimensional collective structure under held-out windows or moduli.

## Reproduction

```bash
python code/avrg_pass028.py
python -m unittest discover -v -s code -p 'test_avrg_pass028.py'
```
