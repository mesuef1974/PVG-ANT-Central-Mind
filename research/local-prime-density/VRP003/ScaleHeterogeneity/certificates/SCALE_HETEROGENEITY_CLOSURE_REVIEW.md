# Scale-Heterogeneity Closure Review 001

**Decision:** `CLOSE SCALE-HETEROGENEITY DIAGNOSTIC — PASS AS DIAGNOSTIC, NOT AS MECHANISM`  
**Date:** 2026-07-12  
**Parent research closure:** `a0f93f4 — Close Dataset 003 independent replication`

## Scope reviewed

- repaired Python decomposition;
- declared numerical tolerances;
- committed scientific certificate;
- recursive regenerated-certificate comparison;
- report and lemma ledger;
- full Dataset 003 reproduction, including Python/R agreement.

## Repair finding

The previous draft incorrectly applied a universal absolute tolerance of `1e-12` to the cancellation-prone evaluation

\[
(A+B)^2-A^2-B^2.
\]

The exact identity was never in doubt. The certified data exhibit:

```text
maximum absolute discrepancy = 1.862645149230957e-09
maximum scale-relative discrepancy = 3.7473279654308245e-14
```

The repaired implementation uses separate, declared checks:

```text
finite MSE/bias identities       absolute 1e-12
correction reconstruction        absolute 1e-10
adjacent square identity         absolute 1e-12 + relative 256*eps(float64)
```

## Reproduction evidence

GitHub Actions:

```text
run id      = 29168930360
head commit = 996b96967a498e8cb64aeb50033363626ef0d469
conclusion  = success
```

All stages passed:

1. frozen Dataset 003 protocol validation;
2. Dataset 001 and Dataset 002 rebuild and verification;
3. segmented-sieve Dataset 003 rebuild;
4. schema and leakage verification;
5. Dataset 003 Python analysis;
6. Dataset 003 R analysis;
7. Python/R agreement;
8. committed Dataset 003 result verification;
9. scale-heterogeneity analysis;
10. regenerated scale certificate verification;
11. artifact upload.

Artifact:

```text
id     = 8252969380
name   = dataset003-scale-heterogeneity-edd9354dd8fc5ea6ceb36ab5ab9ee27c77172b88
digest = sha256:5276945f2f8a2d872b6c0493572580071d4f76a66c4aca9b24d84a416e6c6eb1
```

## Scientific findings retained

### Exact known layer

- correction-gain identity;
- positive correction criterion;
- bias/covariance split;
- adjacent-increment square identity;
- shifted second-moment covariance identity.

### Empirical layer

- negative correction gain at `h=x^(1/2)`;
- positive point gains at `h=x^(2/3)` and `h=x^(3/4)`;
- negative adjacent von Mangoldt covariance in all three frozen families;
- six frozen lagged-Lambda coefficients are negative.

### Conditional layer

A uniform variance law at `h` and `2h`, plus shifted-domain and boundary control, would lead schematically to an adjacent covariance term `-hX log 2`.

This is a conditional proof strategy, not an unconditional project theorem.

## PVG-necessity decision

`NOT ESTABLISHED`.

PVG organizes the observables and exposes the alignment-versus-energy diagnostic, but no new classical estimate, unique PVG mechanism, or theorem has been established.

## Prohibitions after closure

- no Dataset 004;
- no model retuning;
- no Lean pass for the elementary identities;
- no promotion to Candidate Mechanism;
- no RH/GRH claim.

## Stage transition

The active Scale-Heterogeneity operational goal is closed. The next active operational goal becomes:

```text
GOAL-OP-LANGUAGE-KERNEL-V1-001
```

The six legacy-reconciled bridges and the experiment-to-covariance bridge become inputs to the kernel audit; they are not automatically certified L3 transfer principles.

**Final classification:** reproducible diagnostic closure; no original lemma; no theorem; no RH/GRH progress.