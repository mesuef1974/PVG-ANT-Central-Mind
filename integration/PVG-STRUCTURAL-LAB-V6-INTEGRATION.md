# PVG Structural Laboratory v6 — Canonical Integration

**Stage:** `PVG-STRUCTURAL-LAB-V6-INTEGRATION-001`  
**External asset:** `EXT-ASSET-PVG-STRUCTURAL-LAB-001`  
**Date:** 2026-07-20  
**Classification:** capability maturation / finite computational diagnostics  
**Claim ceiling:** no theorem, no Goldbach proof, no RH/GRH progress, no originality claim.

## Policy decision

The canonical repository explicitly excludes heavy HTML applications. Therefore the browser application remains an external, hashed research asset. The repository stores only the durable integration layer:

- an external-asset registry record;
- an experiment registry;
- an independent Python validation lane;
- regression tests and CI;
- a checkpoint/certificate;
- a maturation receipt;
- the external package manifest and hashes.

This preserves the repository policy while making the laboratory reproducible and auditable.

## Seven-step closure map

| Step | Deliverable | Status |
|---|---|---|
| 1. Canonical integration | external asset registration + integration note | PASS |
| 2. Split the code | HTML shell, CSS, legacy explorer, arithmetic, smooth, statistics, additive, UI modules | PASS in external package |
| 3. Regression tests and CI | Node core tests externally; independent Python tests and GitHub workflow canonically | PASS |
| 4. Independent validation | non-overlapping calibration and holdout grids | PASS |
| 5. Partial correlations and counterexamples | controls for `pi(y)`, max variance share, and alpha; deliberate counterexample search | PASS |
| 6. Additive fibers | ordered fiber, primality/prime-power classes, residue channels, finite DFT | PASS as finite interactive diagnostic |
| 7. Registry, certificate, hashes | JSONL experiment registry, checkpoint, receipt, SHA-256 manifest | PASS |

## External package

```text
asset_id: EXT-ASSET-PVG-STRUCTURAL-LAB-001
version: 6.0.0
bundle_sha256: 88ee222e2a466d7a1e6c417beec25041bb3e327d514324caf0bd32d6a75cbd6b
manifest_sha256: 8f1a9cbc147ad49a9ae2b24f0626cb2ada12ff7f2e4d20cd356ee32064fc0b23
```

Key files:

```text
index.html              4db0c4d18fdf036dbaf442f4dc75257bb035cee0a9345e85d3291eb0a7b6e26b
src/app.js              e8d9fd97823be2b970ebad94e0fb93dc09a14f7843f05511ea244b4380421b72
src/core/arithmetic.js  3845c604c204d9b48a7a3e972d9d32dd44080ee5214a4a3f68bdd06be375dbd0
src/core/smooth.js      836e2036b895e5f3150ada2dcfbca8753e745cdac66ae8e19509da17d3d56672
src/core/statistics.js  6ce62b51f65bb3da583fb60cfba4668907f68824beb9dc0a869a2480845a9598
src/core/additive.js    8ec38733ae9c84fd7a59cda507fd4698435a851a25c80d1df4a33d320544eacf
```

## Independent validation design

Calibration:

```text
x: 10 logarithmic points through 100000
y: 2, 3, 5, 7, 11, 19
cases: 60
```

Holdout:

```text
x: 11 offset logarithmic points through 87000
y: 3, 5, 7, 13, 17, 23
cases: 66
```

The holdout `x` grid is offset and the `y` family differs from the calibration family. Calibration quartiles are frozen before holdout scoring.

## Validation result

Raw holdout association:

```text
Pearson(B, saddle error)  =  0.8058846295
Spearman(B, saddle error) =  0.7330967540
```

After linear residualization:

```text
partial(B,error | pi(y), max-share)        = -0.1646316285
partial(B,error | pi(y), max-share, alpha) =  0.1661740560
```

Interpretation:

- the raw association reproduces on a disjoint holdout;
- most of the apparent association does not survive controls for dimension and axis dominance;
- `B` is therefore retained as a companion diagnostic, not promoted to a standalone error certificate.

The counterexample search found two holdout cases with

```text
delta B     = 0.0065453343
delta error = 0.0472699796
```

and a rank reversal of the same error gap. This is a direct negative witness against monotone standalone certification by `B`.

## Additive-fiber capability

For each `N`, the external application constructs

```text
F_N = {(nu(x), nu(N-x)) : 1 <= x < N}
```

and records:

- ordered pairs;
- prime-prime pairs;
- pairs containing a prime power;
- residue counts by `x mod q`;
- the finite discrete Fourier transform of the prime-pair residue channel;
- exact factorization, `gcd`, and `dlog` per displayed pair.

This is a finite diagnostic implementation. Nonzero Fourier channels do not prove asymptotic distribution, minor-arc control, or Goldbach positivity.

## Knowledge return

The integration changes the Central Mind capability as follows:

```text
before:
  one-page exploratory application with same-grid empirical correlations

after:
  policy-compliant external modular laboratory;
  independent canonical validation lane;
  holdout calibration and partial-correlation audit;
  explicit counterexample memory;
  executable additive-fiber and residue/Fourier diagnostics.
```

No mathematical theorem is added by this integration.
