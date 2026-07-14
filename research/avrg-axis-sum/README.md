# AVRG Axis-Sum Research Archive

This directory preserves the complete retained research trail for the additive axis-sum program in Prime Valuation Geometry (PVG), from the foundational definition through PASS034.

## Scope

- PASS001–PASS034 research reports: 34
- Python programs and reproducibility tests: 46
- Saved JSON experiment outputs: 52
- Figures: 1
- Preregistered diagnostic protocols: 11
- Retained source artifacts before this archive index: 144

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

PASS034 is complete. It added the exact e=14 full-orbit window and compared two disjoint three-window training blocks:

- early block: e=14,15,16;
- late block: e=17,18,19.

The e=14 computation passed its exact safety gate:

- 32 representative character rows;
- 3,190 on-state values across seven moduli;
- maximum pointwise closure error: `6.13e-18`;
- maximum averaged closure error: `2.20e-18`;
- zero-residue variation across characters: `0`.

The locked non-overlap result rejects a stable transferable linear cancellation functional:

- mean signed early/late functional cosine: **0.207815**;
- restricted-permutation cosine p-value: **0.092981**;
- bidirectional scalar skill: **-0.136844**;
- restricted-permutation skill p-value: **0.000400**;
- moduli with signed cosine at least 0.30: **4/7**;
- moduli with nonnegative bidirectional skill: **2/7**;
- locked decision: `no_stable_nonoverlapping_linear_cancellation_functional_under_locked_rule`.

The small skill p-value does not mean successful prediction. The observed model is substantially better than the broken-coupling permutation null, whose mean skill is -1.119957, but it remains worse than the zero-prediction baseline because its absolute skill is negative.

The next proposed diagnostic is PASS035: separate directional failure from gain/calibration drift between the independent early and late functionals. Oracle target recalibration must remain a diagnostic and must not be reported as held-out prediction.

## Reproduction

```bash
python code/avrg_pass034.py
python -m unittest discover -v -s code -p 'test_avrg_pass034.py'
sha256sum results/avrg_pass034_results.json
```

Expected PASS034 result SHA-256:

```text
fa92d9fa771740dd6083bf9bb6dbd530219e5c25bffee54991db4f50900196ce
```
