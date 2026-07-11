# Scale-Heterogeneity Lemma Ledger

## SHD-LEMMA-001 — Finite Correction-Gain Identity

For finite real sequences `y_i`, `c_i`, and `d_i`, define

```text
e_i = y_i - c_i.
```

Then

```text
Σ[e_i^2 - (e_i-d_i)^2]
  = 2Σ[e_i d_i] - Σ[d_i^2].
```

### Proof

For every index,

```text
e_i^2 - (e_i-d_i)^2
= e_i^2 - (e_i^2 - 2e_i d_i + d_i^2)
= 2e_i d_i - d_i^2.
```

Sum over the finite index set.

**Classification:** exact algebraic lemma.  
**Dependencies:** commutative ring arithmetic.  
**Lean readiness:** immediate; no number-theory dependency.

---

## SHD-LEMMA-002 — Positive Correction Criterion

Under the definitions of SHD-LEMMA-001, for a nonempty finite index set,

```text
MSE(c) - MSE(c+d)
  = 2 average(e_i d_i) - average(d_i^2).
```

Therefore

```text
MSE(c+d) < MSE(c)
```

if and only if

```text
2 average(e_i d_i) > average(d_i^2).
```

**Classification:** exact corollary.  
**Interpretation:** alignment must exceed correction energy.  
**Lean readiness:** immediate after SHD-LEMMA-001 and nonempty-cardinality handling.

---

## SHD-LEMMA-003 — Bias/Covariance Split

For finite real sequences with uniform averaging,

```text
E[e d] = Cov(e,d) + E[e]E[d].
```

Hence

```text
2E[e d] = 2Cov(e,d) + 2E[e]E[d].
```

**Classification:** exact finite-probability identity.  
**Lean readiness:** straightforward but requires a chosen finite-average/covariance API.

---

## SHD-LEMMA-004 — Adjacent Increment Square Identity

Let `F` be any real-valued function and let `h` be an admissible shift. Define

```text
A_h(x) = F(x)   - F(x-h) - h
B_h(x) = F(x+h) - F(x)   - h.
```

Then

```text
A_h(x) + B_h(x) = F(x+h) - F(x-h) - 2h
```

and

```text
2 A_h(x) B_h(x)
  = [A_h(x)+B_h(x)]^2 - A_h(x)^2 - B_h(x)^2.
```

For `F=psi`, this relates two adjacent centered von Mangoldt increments to the centered increment over the doubled interval.

**Classification:** exact algebraic/interval identity.  
**Lean readiness:** immediate at the abstract function level; later instantiate with arithmetic prefix sums.

---

## SHD-LEMMA-005 — Shifted Second-Moment Covariance Identity

Let

```text
E_h(x) = psi(x+h)-psi(x)-h.
```

On any domain `I` for which `x`, `x+h`, and `x+2h` are admissible,

```text
2 ∫_I E_h(x)E_h(x+h) dx
 = ∫_I E_(2h)(x)^2 dx
   - ∫_I E_h(x)^2 dx
   - ∫_I E_h(x+h)^2 dx.
```

### Proof strategy

Apply SHD-LEMMA-004 pointwise with the adjacent increments `E_h(x)` and `E_h(x+h)`, then integrate.

**Classification:** exact analytic identity once integrability is supplied.  
**Lean readiness:** suitable for a later measure/integration layer, not required for the first P3 pass.

---

## SHD-PROP-001 — Conditional Adjacent Anticorrelation Transfer

Assume a short-interval variance asymptotic, uniform enough at `h` and `2h`, of schematic form

```text
J(X,h) = hX[log(X/h)+C] + o(hX),
```

and assume the shifted second moment differs from the unshifted one by `o(hX)` on the common integration domain.

Then SHD-LEMMA-005 predicts

```text
∫ E_h(x)E_h(x+h) dx
  = -hX log 2 + o(hX).
```

### Derivation

```text
J(X,2h)-2J(X,h)
≈ 2hX[log(X/(2h))+C]
  -2hX[log(X/h)+C]
= -2hX log 2.
```

Divide by two using SHD-LEMMA-005.

**Classification:** conditional consequence/proof strategy, not unconditional theorem.  
**Load-bearing missing certificates:** variance asymptotic, uniformity, boundary/shift control.

---

## SHD-WALL-001 — Prime-Count / Weighted-Increment Covariance Wall

The model target is a standardized residual of the unweighted prime count, while the dominant predictor group is built from past von Mangoldt and residue-weighted increments.

The missing analytic certificate is a uniform estimate for an averaged covariance of the form

```text
C_theta(X;m)
 = Average_x [ R_pi(x,x^theta) * L_m(x,x^theta) ],
```

where

```text
R_pi = standardized prime-count residual,
L_m  = centered past weighted/residue observable on length m x^theta.
```

Required output:

- sign and order of magnitude as a function of `theta`;
- stability across `m in {1,2,4}`;
- comparison of prime-count and von-Mangoldt targets;
- separation of prime-power, residue, and boundary terms;
- explicit assumptions if pair correlation or Hardy–Littlewood input is used.

**Status:** open missing certificate.  
**Prohibited interpretation:** computational sign changes are not a theorem about `C_theta`.

---

## Formalization queue

1. `SHD-LEMMA-001` — P2 proof, then Lean/P3.
2. `SHD-LEMMA-002` — P2 proof, then Lean/P3.
3. `SHD-LEMMA-004` — abstract function identity, then Lean/P3.
4. `SHD-LEMMA-003` — after selecting the finite covariance API.
5. `SHD-LEMMA-005` — defer until the analytic integration layer is justified.

No item in this queue is a new theorem about prime distribution. The value is a checked bridge from the experiment to a precisely named analytic wall.
