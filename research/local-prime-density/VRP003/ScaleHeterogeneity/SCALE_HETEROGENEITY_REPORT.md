# Scale-Heterogeneity Diagnostic and Proof-Strategy Pass

**Pass ID:** `PVG-LPD-SCALE-HETEROGENEITY-001`  
**Parent result:** `CLOSE DATASET 003 — PASS`  
**Status:** `CLOSED — DIAGNOSTIC PASS / MECHANISM NOT ESTABLISHED`  
**Scientific ceiling:** no theorem about primes, no replicated candidate signal, no RH/GRH progress.

## 1. Governing question

Dataset 003 produced a small positive aggregate point estimate, but the effect changed sign by window scale:

```text
h = x^(1/2)    negative gain
h = x^(2/3)    positive gain
h = x^(3/4)    positive gain
```

The purpose of this pass was not to fit another model. It was to identify the exact object controlling whether the frozen past-only correction helps, and to separate the exact algebra from the empirical arithmetic pattern and the conditional analytic bridge.

## 2. Source and reproducibility

The pass is derived from the certified Dataset 003 artifact:

```text
workflow run = 29164273761
artifact id  = 8251699912
digest       = sha256:9fd56a0b99b198e44ebeaa73fb3bf36b69a5e3d40425e1d7c76cec23a493c889
```

The committed certificate is regenerated from the Dataset 003 data, predictions, and frozen coefficients. CI compares the generated and committed certificates recursively.

## 3. Layer A — exact algebraic identities

Let

```text
y   = observed standardized prime-count residual
c   = classical prediction
d   = primary prediction - classical prediction
e_c = y - c
```

Then the primary error is `e_c-d`, and pointwise

\[
e_c^2-(e_c-d)^2=2e_cd-d^2.
\]

Averaging gives

\[
\operatorname{MSE}_{\rm classical}
-
\operatorname{MSE}_{\rm primary}
=
2\mathbb E(e_cd)-\mathbb E(d^2).
\]

Therefore the correction helps exactly when

\[
2\mathbb E(e_cd)>\mathbb E(d^2).
\]

The first term is **alignment** with the remaining classical error; the second is **correction energy**.

The alignment also splits exactly as

\[
2\mathbb E(e_cd)
=
2\operatorname{Cov}(e_c,d)
+
2\mathbb E(e_c)\mathbb E(d).
\]

These are known finite algebra/probability identities, not number-theory theorems.

## 4. Layer B — Dataset 003 scale diagnostic

| Family | MSE gain | Alignment | Correction energy | Alignment / energy |
|---|---:|---:|---:|---:|
| overall | 0.0043848996 | 0.0083464404 | 0.0039615408 | 2.1069 |
| `x^(1/2)` | -0.0096869635 | -0.0032291680 | 0.0064577955 | -0.5000 |
| `x^(2/3)` | 0.0108128318 | 0.0139406431 | 0.0031278114 | 4.4570 |
| `x^(3/4)` | 0.0120288306 | 0.0143278461 | 0.0022990155 | 6.2322 |

The shortest-window failure is not merely a weak positive signal. Its alignment is negative and its energy penalty is the largest. At the longer scales, alignment is positive and exceeds correction energy.

## 5. Feature-group decomposition

The primary correction is reconstructed from:

1. the shift in the three classical coefficients;
2. lagged von Mangoldt features;
3. character-weighted features;
4. reduced-residue energy features.

The maximum reconstruction error is

\[
2.0261570199409107\times10^{-15}.
\]

The lagged-Lambda group carries the main scale change:

| Family | Alignment | Self-energy | Corr(classical error, Lambda correction) |
|---|---:|---:|---:|
| `x^(1/2)` | -0.0013490656 | 0.0048456963 | -0.0136524 |
| `x^(2/3)` | 0.0082773338 | 0.0016919513 | 0.2022895 |
| `x^(3/4)` | 0.0102417246 | 0.0011140698 | 0.3661522 |

All six frozen lagged-Lambda coefficients are negative. The model therefore behaves as an **anti-persistence correction**, not a positive-memory model.

## 6. Adjacent von Mangoldt increments

Define centered adjacent increments

\[
A_h(x)=\psi(x)-\psi(x-h)-h,
\qquad
B_h(x)=\psi(x+h)-\psi(x)-h.
\]

They satisfy exactly

\[
2A_h(x)B_h(x)
=
(A_h(x)+B_h(x))^2-A_h(x)^2-B_h(x)^2.
\]

Dataset 003 gives negative adjacent covariance in every family:

| Family | Covariance | Correlation | Mean `A_hB_h/(h log x)` |
|---|---:|---:|---:|
| `x^(1/2)` | -2,658.7531 | -0.0533318 | -0.0126138 |
| `x^(2/3)` | -61,341.7943 | -0.1317231 | -0.0262725 |
| `x^(3/4)` | -356,217.3861 | -0.2488871 | -0.0455799 |

This is an empirical observation on the frozen sample, not a theorem about adjacent prime intervals.

## 7. Numerical-repair note

The previous draft used one absolute tolerance `10^-12` for every identity. That was inappropriate for the cancellation-prone expression

\[
(A+B)^2-A^2-B^2.
\]

In the certified data:

```text
maximum absolute discrepancy = 1.862645149230957e-09
maximum scale-relative discrepancy = 3.7473279654308245e-14
```

The repaired implementation uses:

```text
MSE/bias identities: absolute tolerance 1e-12
correction reconstruction: absolute tolerance 1e-10
adjacent square identity: absolute tolerance 1e-12 plus relative tolerance 256*eps(float64)
```

This is a numerical-evaluation repair, not a mathematical repair of the exact identity.

## 8. Layer C — exact variance-to-covariance bridge

Let

\[
E_h(x)=\psi(x+h)-\psi(x)-h.
\]

Then

\[
E_{2h}(x)=E_h(x)+E_h(x+h),
\]

so pointwise

\[
2E_h(x)E_h(x+h)
=
E_{2h}(x)^2-E_h(x)^2-E_h(x+h)^2.
\]

After integration over a common admissible domain, adjacent covariance is exactly a difference of three second moments.

## 9. Conditional proof strategy — not a project theorem

If one has a sufficiently uniform short-interval variance asymptotic at `h` and `2h`, together with control of shifted versus unshifted domains and boundary terms, the doubling identity suggests an adjacent covariance main term of schematic size

\[
-hX\log 2.
\]

This statement remains conditional. The missing certificates are:

1. a uniform variance asymptotic in the required range of `h`;
2. shifted/unshifted second-moment control;
3. boundary-domain control;
4. a bridge from von Mangoldt covariance to the standardized unweighted prime-count residual.

No claim of novelty is made until a targeted literature and assumption audit is completed.

## 10. What PVG contributes — and does not yet contribute

PVG currently contributes:

- a structured description of past-only valuation and residue observables;
- a decomposition of the frozen correction into geometric/character groups;
- the alignment-versus-energy diagnostic;
- a precise route from the computational sign change to a named analytic covariance object.

PVG has not yet supplied:

- a new bound for the Selberg integral;
- a proof of adjacent anti-correlation;
- a uniform prime-count/weighted-increment covariance theorem;
- a mechanism unavailable in classical ANT.

Therefore the PVG-necessity test is not passed.

## 11. Closure decision

```text
CLOSE SCALE-HETEROGENEITY DIAGNOSTIC — PASS AS DIAGNOSTIC, NOT AS MECHANISM
```

Classification:

```text
Exact correction-gain identities              KNOWN / PROVED
Dataset 003 scale heterogeneity               COMPUTATIONAL DIAGNOSTIC
Adjacent von Mangoldt anti-correlation         COMPUTATIONAL DIAGNOSTIC
Variance-to-covariance identity                EXACT BRIDGE
-hX log 2 statement                            CONDITIONAL PROOF STRATEGY
PVG research mechanism                         NOT ESTABLISHED
New theorem about primes                       NONE
RH/GRH progress                                NONE
```

## 12. Next action

Do not start Dataset 004 and do not open a Lean pass for the elementary identities. The next program stage is `PVG–ANT Language Kernel v1`, followed by a targeted originality/literature audit of candidate transfer lemmas.