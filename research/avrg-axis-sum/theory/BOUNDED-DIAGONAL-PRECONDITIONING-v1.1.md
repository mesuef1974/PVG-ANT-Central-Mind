# Bounded Diagonal Preconditioning for Marginal Operators — v1.1

Status: `PROVED STRUCTURAL FACTS + NUMERICAL OPTIMIZATION PROTOCOL`

## 1. Object

Let

\[
M=M_{N;\mathbf q}\in\mathbb R^{m\times (N-1)}
\]

be a marginal measurement matrix after deleting zero rows. For a positive diagonal matrix

\[
P(\ell)=\operatorname{diag}(e^{\ell_1},\dots,e^{\ell_m}),
\]

consider the left-preconditioned operator

\[
M_\ell=P(\ell)M.
\]

Because `P(ℓ)` is invertible,

\[
\ker M_\ell=\ker M,
\qquad
\operatorname{rank}M_\ell=\operatorname{rank}M.
\]

Thus diagonal left preconditioning changes conditioning but not recoverable information.

## 2. Gauge normalization

Multiplying every row weight by the same scalar does not change the positive condition number. We therefore fix the gauge

\[
\sum_{i=1}^{m}\ell_i=0.
\]

Equivalently,

\[
\prod_{i=1}^{m}e^{\ell_i}=1.
\]

## 3. Why the unrestricted problem is unsafe

The formal problem

\[
\inf_{\ell:\,\sum_i\ell_i=0}
\kappa_2^+(P(\ell)M)
\]

need not have a well-behaved interior minimizer when rows are linearly dependent. Optimization can drive some row weights toward zero while compensating with very large weights on other rows. The information space remains unchanged for every finite positive scaling, but the sequence may approach a boundary where selected redundant measurements are effectively suppressed.

Therefore an unconstrained numerical optimum must not be reported as a certified attained optimum without a coercivity or existence proof.

## 4. Governed bounded problem

For a declared dynamic-range budget `τ>0`, define

\[
\mathcal L_\tau
=
\left\{
\ell\in\mathbb R^m:
\sum_i\ell_i=0,
\quad
|\ell_i|\le\tau
\right\}.
\]

The governed optimization problem is

\[
\boxed{
\kappa_{\tau}^{\star}(M)
=
\min_{\ell\in\mathcal L_\tau}
\kappa_2^+(P(\ell)M)
}
\]

The feasible set is compact. Since the positive singular values vary continuously while rank is fixed under positive invertible scaling, a minimizer exists for every finite `τ`.

## 5. Certified structural consequences

For every feasible `ℓ`:

1. `rank(P(ℓ)M)=rank(M)`;
2. `ker(P(ℓ)M)=ker(M)`;
3. no Goldbach, prime-distribution, sieve, RH, or GRH information is created;
4. all improvement is numerical stabilization of the already-visible subspace;
5. the reported optimum is conditional on `τ`, the candidate modulus family, and the chosen matrix convention.

## 6. Baselines

Three baselines must be reported:

- unscaled `M`;
- row-normalized `P_row M`;
- bounded optimized `P(ℓ*)M`.

A bounded optimizer is useful only if it improves on row normalization under the same rank tolerance.

## 7. Numerical classification

The current implementation uses multiple-start smooth optimization of

\[
\log \kappa_2^+(P(\ell)M)
\]

in centered log coordinates. This is a numerical search protocol, not a proof of global optimality. The best value found is classified as:

`COMPUTATIONAL UPPER BOUND ON THE BOUNDED OPTIMUM`.

## 8. Scientific ceiling

This unit concerns conditioning of finite measurement operators only. It does not establish novelty, does not solve an analytic number theory problem, and does not constitute progress on Goldbach or RH/GRH.
