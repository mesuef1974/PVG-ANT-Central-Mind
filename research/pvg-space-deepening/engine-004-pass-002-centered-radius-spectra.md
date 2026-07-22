# ENGINE-004 PASS-002 — Centered-Radius Spectra

```text
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Status: implementation_checkpoint
Scope: frozen 884-point box only
Phase D: NOT AUTHORIZED
```

## Object

For a fixed integer `N` and every distinct-prime representation

\[
N=p+q,\qquad p<q,
\]

define the exact normalized centered radius

\[
\rho_N(p,q)=\frac{q-p}{N}.
\]

The centered-radius spectrum is

\[
\Sigma(N)=\left\{\frac{q-p}{N}:\{p,q\}\in\mathcal R_2(N)\right\}.
\]

The implementation stores every radius as a reduced rational number, never as a floating-point approximation.

## Exact identities

For every admitted radius `rho`:

\[
0<\rho<1,
\]

and the normalized prime coordinates are reconstructed exactly by

\[
\frac pN=\frac{1-\rho}{2},
\qquad
\frac qN=\frac{1+\rho}{2}.
\]

Thus `rho` is a lossless coordinate for the **relative shape** of one representation, while forgetting the absolute scale `N`.

Equal radii satisfy

\[
\frac{q_1-p_1}{p_1+q_1}
=
\frac{q_2-p_2}{p_2+q_2},
\]

which means equal ordered prime proportions. It does not imply equal sums or equal prime pairs.

## Finite relations to compute

Inside the frozen box only, the analyzer records:

1. **spectrum equality** — two points have identical nonempty rational spectra;
2. **proper containment** — one spectrum is a strict subset of another;
3. **radius collision** — the same rational radius occurs at multiple integer points;
4. **spectrum collision** — multiple integer points share one complete spectrum;
5. **compression** — the map from representable integer points to unique spectra loses absolute scale.

These are exact finite set relations, not statistical estimates.

## Implementation

```text
tools/pvg_centered_radius_spectra.py
tests/test_pvg_centered_radius_spectra.py
```

Required commands:

```text
python -m unittest -v tests/test_pvg_centered_radius_spectra.py
python tools/pvg_centered_radius_spectra.py --registered-summary --compact
```

## Current classification

```text
Definitions and reconstruction laws: IDENTITY / PROVED
Frozen-box equality and collision enumeration: FINITE-VERIFIED after successful regeneration
Interpretation as relative shape compression: INTERPRETATION
Historical originality: NOT CLAIMED
```

## Governance ceiling

This pass does not authorize:

- cap expansion;
- Phase D or orbit dynamics;
- return to `GOAL-OP-ONE-THEOREM-001`;
- an asymptotic law;
- any Goldbach, PNT, RH, or GRH claim;
- any historical-originality or publication-readiness claim.
