# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS026.

## Scope

- PASS001–PASS026 research reports: 26
- Python programs and reproducibility tests: 30
- Saved JSON experiment outputs: 44
- Figures: 1
- Preregistered diagnostic protocols: 3
- Retained source artifacts before this archive index: 104

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

PASS026 is complete. Its protocol and code were committed before computing the on/off channel shares.

Using the exact centered identity

`log(rho) = log(E_on) - log(E_off)`,

the five-window character instability was classified as on-channel dominated:

- symmetric on share: 1.636623;
- symmetric off share: -0.636623;
- on-only skill versus zero: 0.487952;
- off-only skill versus zero: -1.785295;
- on dominance held in all five windows, all seven moduli, and all five leave-one-window-out recomputations.

The signed shares reflect strong positive on/off co-movement (correlation 0.961845): the smaller off variation cancels part of the larger on variation.

The next proposed diagnostic is PASS027: decompose the on-energy character variation into diagonal and off-diagonal terms, then localize the off-diagonal contribution by lag residue h mod r.

## Reproduction

```bash
python code/avrg_pass026.py
python -m unittest discover -v -s code -p 'test_avrg_pass026.py'
```
