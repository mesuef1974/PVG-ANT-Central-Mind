# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS033.

## Scope

- PASS001–PASS033 research reports: 33
- Python programs and reproducibility tests: 44
- Saved JSON experiment outputs: 51
- Figures: 1
- Preregistered diagnostic protocols: 10
- Retained source artifacts before this archive index: 139

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

PASS033 is complete. Its jackknife functional-stability protocol, implementation, and tests were committed before the locked analysis.

The raw oriented coherence of the five leave-one-window-out cancellation functionals is 0.552909, but this does not exceed the overlap-aware restricted-permutation null:

- oriented coherence: 0.552909;
- null mean: 0.609023;
- restricted-permutation p-value: 0.800840;
- axis coherence: 0.709707 with secondary p-value 0.302739;
- 15/70 pairwise signed cosines are negative.

The locked decision rejects a distinct stable oriented linear cancellation functional. PASS031 remains a containment result, while PASS032–PASS033 reject linear prediction and show that jackknife similarity is explained by overlapping training windows.

The next proposed diagnostic is PASS034: add the inexpensive e=14 full orbit window and compare early and late three-window training blocks with no overlap.

## Reproduction

```bash
python code/avrg_pass033.py
python -m unittest discover -v -s code -p 'test_avrg_pass033.py'
```
