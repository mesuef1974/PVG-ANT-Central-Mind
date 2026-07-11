# Scale-Heterogeneity Lemma Ledger

**Status:** closed diagnostic ledger.  
**Rule:** known algebraic identities are recorded for reuse but do not trigger a Lean pass or originality claim.

## SHD-LEMMA-001 — Finite Correction-Gain Identity

For finite real sequences `y_i`, `c_i`, and `d_i`, define `e_i=y_i-c_i`. Then

\[
\sum_i\left[e_i^2-(e_i-d_i)^2\right]
=
2\sum_i e_id_i-
\sum_i d_i^2.
\]

### Proof

For each index,

\[
e_i^2-(e_i-d_i)^2=2e_id_i-d_i^2.
\]

Sum over the finite set.

**Classification:** exact known algebraic identity.  
**Research value:** identifies alignment and correction energy.  
**Originality:** none.

---

## SHD-LEMMA-002 — Positive Correction Criterion

On a nonempty finite sample,

\[
\operatorname{MSE}(c)-\operatorname{MSE}(c+d)
=
2\mathbb E(ed)-\mathbb E(d^2).
\]

Hence

\[
\operatorname{MSE}(c+d)<\operatorname{MSE}(c)
\iff
2\mathbb E(ed)>\mathbb E(d^2).
\]

**Classification:** exact corollary.  
**Interpretation:** alignment must exceed correction energy.  
**Originality:** none.

---

## SHD-LEMMA-003 — Bias/Covariance Split

For finite uniform averaging,

\[
\mathbb E(ed)=\operatorname{Cov}(e,d)+\mathbb E(e)\mathbb E(d).
\]

Therefore

\[
2\mathbb E(ed)
=
2\operatorname{Cov}(e,d)+2\mathbb E(e)\mathbb E(d).
\]

**Classification:** exact finite-probability identity.  
**Originality:** none.

---

## SHD-LEMMA-004 — Adjacent Increment Square Identity

Let `F` be real-valued and define

\[
A_h(x)=F(x)-F(x-h)-h,
\qquad
B_h(x)=F(x+h)-F(x)-h.
\]

Then

\[
A_h(x)+B_h(x)=F(x+h)-F(x-h)-2h
\]

and

\[
2A_h(x)B_h(x)
=
(A_h(x)+B_h(x))^2-A_h(x)^2-B_h(x)^2.
\]

For `F=ψ`, this relates adjacent centered von Mangoldt increments to the doubled interval.

**Classification:** exact known algebraic/interval identity.  
**Originality:** none.

---

## SHD-LEMMA-005 — Shifted Second-Moment Covariance Identity

Let

\[
E_h(x)=\psi(x+h)-\psi(x)-h.
\]

On a common domain `I` on which all terms are admissible,

\[
2\int_I E_h(x)E_h(x+h)\,dx
=
\int_I E_{2h}(x)^2\,dx
-
\int_I E_h(x)^2\,dx
-
\int_I E_h(x+h)^2\,dx.
\]

### Proof

Apply SHD-LEMMA-004 pointwise to `E_h(x)` and `E_h(x+h)`, then integrate.

**Classification:** exact analytic identity, subject only to integrability and domain admissibility.  
**Research role:** bridge from adjacent covariance to short-interval second moments.  
**Originality status:** requires literature audit; no claim made.

---

## SHD-PROP-001 — Conditional Adjacent Anticorrelation Transfer

Assume a sufficiently uniform asymptotic of the form

\[
J(X,h)=hX\left(\log\frac{X}{h}+C\right)+o(hX)
\]

at both `h` and `2h`, together with

- common-domain control;
- shifted versus unshifted second-moment control;
- boundary errors `o(hX)`.

Then SHD-LEMMA-005 formally gives

\[
\int E_h(x)E_h(x+h)\,dx
=
-hX\log 2+o(hX).
\]

**Classification:** conditional consequence / proof strategy.  
**Not established:** the required uniform hypotheses in the project’s precise domain.  
**No unconditional theorem is claimed.**

---

## SHD-WALL-001 — Prime-Count / Weighted-Increment Covariance Wall

The computational target is a standardized residual of the unweighted prime count, whereas the dominant correction group uses past von Mangoldt and residue-weighted increments.

The missing analytic certificate has the form

\[
C_\theta(X;m)
=
\operatorname{Avg}_x
\left[
R_\pi(x,x^\theta)L_m(x,x^\theta)
\right],
\]

where `R_π` is the classical prime-count residual and `L_m` is a centered past weighted/residue observable.

A usable result would need:

1. sign and order as a function of `θ`;
2. uniformity over the lag scales `m∈{1,2,4}`;
3. comparison between prime-count and von-Mangoldt targets;
4. separation of prime powers, residue terms, and boundaries;
5. exact assumptions if pair correlation or Hardy–Littlewood input is used.

**Status:** missing certificate.  
**Prohibited interpretation:** the computational sign pattern is not a theorem about `C_θ`.

---

## Formalization decision

No Lean pass is authorized for SHD-LEMMA-001–004 merely because they are easy to formalize. They are elementary known identities and do not advance the active originality target.

Formalization becomes justified only if:

- a later original transfer lemma depends on a reusable abstract finite-energy interface; or
- the analytic proof has enough complexity that machine verification materially reduces risk.

## Closure

This ledger closes the experiment-to-analysis translation step. The retained research object is SHD-LEMMA-005 plus the hypothesis audit needed for SHD-PROP-001. No item is currently an original project theorem.