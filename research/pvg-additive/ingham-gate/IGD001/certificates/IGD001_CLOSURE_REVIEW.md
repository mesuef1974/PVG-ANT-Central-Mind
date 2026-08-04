# IGD001 — Closure Review

## What this pass is

A numerical diagnostic that checks whether the constants transcribed from secondary sources
into the Ingham-gate specification are corrupted, before derivation work is built on them.

## What this pass is not

```text
NOT a pass of the Ingham gate.
NOT a verification of Ingham's theorem or Estermann's expansion.
NOT a reading of any primary text.
NOT a demonstration that the PVG lattice contributes anything.
```

The gate is **derivational**: it is passed by deriving the asymptotic inside the framework,
with error `o_h(x log^2 x)`. Citing a published formula is not passing it. Reproducing it
numerically is not passing it. This pass did the second thing only.

## Claim-level audit

| claim | level | basis |
|---|---|---|
| `K = 2.5887066` not corrupted | DATA-CONSISTENT | three estimators agree to 4.5e−04; all alternative scenarios excluded by ≥2.5e3 × spread |
| `C_1*` formula not corrupted at h=1 | NUMERICALLY-CORROBORATED | predicted −0.8625768 vs measured −0.8625592 |
| h-dependence `sigma, sigma', sigma''` | STRONGLY-CORROBORATED on 4 shifts | residual/predicted-Q ratio constant to 0.6 % across an 8× range |
| residual is `O(1/log^3 x)` | CONSISTENT, NOT UNIQUELY IDENTIFIED | 5 cumulative checkpoints cannot separate competing lower-order forms |
| error exponent nearer `x^{1/2}` | **WITHDRAWN** | small spread does not determine an exponent |
| `a_1(h)` correct | still PENDING-PRIMARY-TEXT | numerics never promote this tag |

## Blind spots by construction

- At `h = 1` the quantity `sigma'_{-1}(1) = 0`, so the coefficient `-24/pi^2` — the entire
  h-dependent content of `a_1(h)` — is **invisible** to Phase 1. Likewise `rho_1 = tau_1 = 0`
  makes the h-dependent part of `C_h*` invisible. Phase 2 is what tests those, and it does
  so only on four shifts, all with small `sigma''`.
- The `h` values tested are 2, 6, 12, 30 — all smooth, all small. Nothing here probes
  uniformity in `h`, large `h`, or prime `h` beyond `h = 2`.

## Protocol defects recorded

1. **`M_h` slope estimator unfit at this range.** Registered as a first-order estimator; it
   is contaminated at ≈18 % by the quadratic term at `u ~ 0.05`. The post-run corrected form
   overshoots by 5–7 % because `Q_h(x)` itself has reached only ≈89 % of its limit. Neither
   form carries verdict weight.
2. **Tolerance never frozen as a number.** Defined operationally as estimator spread
   (1.7e−04). Applied literally to Phase 2, the first-order model fails by two orders of
   magnitude; the pass depends on including the pre-derived second-order term. The headline
   is therefore "two-term model consistent", not "first-order model passed".
3. **Calibration shifts `{3,4,5,8}` declared but never run.** Recorded rather than dropped.
4. **No repository freeze before execution.** The specification entered Git after the run;
   its pre-registration rests on the session record only. See `PRE_RUN_SPECIFICATION.md`.

## Standing items

```text
PRIMARY-TEXT-VERIFICATION = OPEN
  Ingham 1927        10.1112/jlms/s1-2.3.202          METADATA-VERIFIED / TEXT-NOT-READ
  Estermann 1931     10.1515/crll.1931.164.173        METADATA-VERIFIED / TEXT-NOT-READ
  Estermann 1932     10.1515/crll.1932.166.64         METADATA-VERIFIED / TEXT-NOT-READ
  Motohashi 1994     Ann. Sci. ENS 27(5) 529-572      CITED / NOT-READ
  Halberstam         10.1112/jlms/s1-30.1.43          JOINT-EK-LOCATION-UNRESOLVED

INGHAM-GATE      = NOT-ATTEMPTED
PVG-ADDITIVE     = NOT-OPENED
PVG-CONTRIBUTION = NOT-SHOWN  (dated 2026-08-04, undisturbed by this pass)
```

The 1932 correction is a single page and has not been read; it cannot be assumed harmless
to the coefficients used here.

## Net assessment

Zero RH progress. Zero GRH progress. No secured path. What was gained is narrower and real:
a falsifiable admission test now exists where none did, its constants survived an
order-one corruption check, and two defects in the test's own design were exposed by running
it rather than by arguing about it.
