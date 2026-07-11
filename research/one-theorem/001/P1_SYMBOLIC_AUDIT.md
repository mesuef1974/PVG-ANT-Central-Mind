# One-Theorem Program 001 — P1 Symbolic Audit

**Target:** `ONE-LEMMA-TARGET-001`  
**Decision:** `P1 SYMBOLIC PASS`, subject to CI reproduction.  
**Role:** independent check of the frozen statement before manual proof.

## 1. Local factor

For

\[
I_r(p^a)=
\begin{cases}
1,&a=0,\\
0,&1\le a<2r,\\
a-2r+1,&a\ge2r,
\end{cases}
\]

and `y=chi(p)p^{-s}`, direct summation gives

\[
\sum_{a\ge0}I_r(p^a)y^a
=1+\frac{y^{2r}}{(1-y)^2}.
\]

The residual local factor is

\[
h_r(y)=
(1-y^{2r})(1-y^{2r+1})^2
\left(1+\frac{y^{2r}}{(1-y)^2}\right).
\]

Symbolic expansion for `r=1,...,8` confirms

\[
h_r(y)=1+O(y^{2r+2}),
\]

with the first nonzero residual coefficient exactly at degree `2r+2`.

This supports absolute convergence of the Euler product for

\[
\Re s>\frac1{2r+2}.
\]

The finite checks do not replace the general algebraic proof, which remains a P2 task.

## 2. Simple pole

Let `m=2r`, `alpha=1/m`, and suppose

\[
L(ms,\chi_0)=\frac{\rho_q}{m(s-\alpha)}+\kappa_q+O(s-\alpha).
\]

If `P(s)` is regular at `alpha`, the residue of

\[
L(ms,\chi_0)P(s)x^s
\]

is

\[
\frac{\rho_q}{m}P(\alpha)x^\alpha.
\]

The frozen coefficient `rho_q P_chi(alpha_r)/(2r)` is correct.

## 3. Double pole

Let `m=2r+1`, `beta=1/m`, and write

\[
L(ms,\chi_0)=\frac{\rho_q}{m(s-\beta)}+\kappa_q+O(s-\beta).
\]

For a regular factor

\[
Q(s)=Q_0+Q_1(s-\beta)+O((s-\beta)^2),
\]

the residue of

\[
L(ms,\chi_0)^2Q(s)x^s
\]

is

\[
x^\beta
\left[
\frac{\rho_q^2Q_0}{m^2}\log x
+
\frac{\rho_q^2Q_1}{m^2}
+
\frac{2\rho_q\kappa_qQ_0}{m}
\right].
\]

Thus the frozen formulas

\[
B_\chi=\frac{\rho_q^2}{(2r+1)^2}Q_\chi(\beta_r)
\]

and

\[
C_\chi=
\frac{\rho_q^2}{(2r+1)^2}Q_\chi'(\beta_r)
+
\frac{2\rho_q\kappa_q}{2r+1}Q_\chi(\beta_r)
\]

are symbolically correct.

## 4. Principal-character finite part

For

\[
L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}),
\]

let

\[
\rho_q=\prod_{p\mid q}(1-p^{-1})=\frac{\varphi(q)}q.
\]

Differentiating the finite Euler factor at `s=1` gives

\[
\kappa_q
=
\rho_q
\left(
\gamma+
\sum_{p\mid q}\frac{\log p}{p-1}
\right).
\]

High-precision independent finite-part checks are included for `q=1,2,6,30`.

## 5. Statement changes

No coefficient correction is required after P1. The frozen target survives unchanged.

## 6. Remaining proof obligations

- prove the residual local estimate for all `r` and uniformly over primes;
- define powers of characters and bad-prime conventions cleanly;
- justify absolute/local uniform convergence of `H_{r,chi}`;
- state the exact Mellin inversion and contour-shift lemma;
- prove vertical-line bounds with all parameter dependence;
- continue the priority audit.

## 7. Ceiling

```text
Symbolic verification only.
No manual theorem proof yet.
No originality certificate.
No RH/GRH progress.
```
