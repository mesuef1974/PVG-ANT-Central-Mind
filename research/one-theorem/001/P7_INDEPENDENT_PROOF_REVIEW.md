# P7 Independent Proof Review — ONE-LEMMA-TARGET-001

**Scope:** line-by-line mathematical review of P2 and P3–P5  
**Reviewer mode:** adversarial internal review independent of the original proof drafting  
**Decision:** proof candidate passes internally after one range clarification  
**Scientific ceiling:** mathematical correctness review only; no originality certification

## 1. Reviewed statement

For fixed `q>=1`, `r>=1`, `(a,q)=1`, `x>=1`, and `W in C_c^infinity(0,infinity)`, review the claimed smoothed expansion for

\[
S_{r;q,a,W}(x)=\sum_{n\equiv a\pmod q}I_r(n)W(n/x),
\]

where

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

## 2. P2 local geometry and Bell series

### Check P2-A — geometric count

For a prime-power coordinate of length `alpha`, the allowed divisor exponent interval is

\[
r\le \beta\le \alpha-r.
\]

Its cardinality is `max(alpha-2r+1,0)`. Independence across prime coordinates proves the product formula and multiplicativity.

**Review result:** PASS.

### Check P2-B — Bell series

The local coefficient sequence is

```text
1, 0, ..., 0, 1, 2, 3, ...
             exponent 2r onward
```

and hence

\[
\sum_{\alpha\ge0}I_r(p^\alpha)y^\alpha
=1+y^{2r}\sum_{j\ge0}(j+1)y^j
=1+\frac{y^{2r}}{(1-y)^2}.
\]

**Review result:** PASS.

### Check P2-C — residual order

Multiplying the Bell series by

\[
(1-y^{2r})(1-y^{2r+1})^2
\]

cancels the terms of degrees `2r` and `2r+1`. The first possible surviving degree is `2r+2`. The special case `r=1` is covered because `4r=2r+2=4`, so no omitted cross term falls below the claimed threshold.

**Review result:** PASS.

## 3. Euler factorization and convergence

For `y_p=chi(p)p^{-s}`, the extracted local factors are

\[
(1-y_p^{2r})^{-1}
\quad\text{and}\quad
(1-y_p^{2r+1})^{-2}.
\]

These are exactly the Euler factors of

\[
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2.
\]

At primes dividing `q`, `chi(p)=0`; all local factors equal `1`, so no bad-prime correction is missing.

The residual local factor satisfies

\[
h_r(y_p)-1=O_r(p^{-(2r+2)\sigma})
\]

uniformly on compact subsets. Therefore

\[
\sum_p|h_r(y_p)-1|<\infty
\]

when `sigma>1/(2r+2)`.

**Review result:** PASS.

## 4. Character decomposition

Because `(a,q)=1`, if `n congruent a mod q` then `(n,q)=1`. For non-coprime `n`, every Dirichlet character modulo `q` vanishes. Thus the identity

\[
\mathbf1_{n\equiv a\pmod q}
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n)
\]

is valid for every integer `n` in the summation.

**Review result:** PASS.

## 5. Mellin inversion

For `W in C_c^infinity(0,infinity)`, the Mellin transform is entire and rapidly decreasing in fixed vertical strips. On a line `c>1/(2r)`, the Dirichlet series converges absolutely. Interchanging the finite or absolutely convergent sum with the Mellin integral is justified.

No Perron factor `1/s` occurs because this is smooth Mellin inversion, not a sharp cutoff.

**Review result:** PASS.

## 6. Contour shift

Choose

\[
\sigma_0=\frac1{2r+2}+\varepsilon
\]

with initially

\[
0<\varepsilon<\frac1{2r+1}-\frac1{2r+2}.
\]

Then `sigma_0` lies strictly left of both candidate poles and strictly inside the absolute-convergence half-plane of `H`.

On the closed strip:

- `H` is uniformly bounded by its absolutely convergent product;
- fixed-modulus Dirichlet `L`-functions have polynomial vertical growth;
- `W-hat` decays faster than every polynomial.

Hence horizontal edges vanish and the shifted integral is

\[
O_{q,r,W,\varepsilon}(x^{\sigma_0}).
\]

For arbitrary larger `epsilon`, the proof invokes a smaller admissible `epsilon_0` and uses `x>=1`.

### Correction made during P7

The original statement did not state `x>=1` explicitly although the final monotonic comparison of error powers used it. The theorem statement has now been corrected to include `x>=1`.

**Review result:** PASS AFTER CLARIFICATION.

## 7. Pole analysis

### Simple pole

If `chi^(2r)=chi_0`, then

\[
L(2rs,\chi_0)
=
\frac{\rho_q}{2r(s-\alpha_r)}+\kappa_q+O(s-\alpha_r).
\]

The other `L`-factor is evaluated at `1+1/(2r)>1`, so it is holomorphic. The residue coefficient is

\[
\frac{\rho_q}{2r}P_\chi(\alpha_r)x^{\alpha_r}.
\]

**Review result:** PASS.

### Double pole

If `chi^(2r+1)=chi_0`, squaring the principal Laurent expansion gives

\[
\frac{\rho_q^2}{m^2t^2}
+
\frac{2\rho_q\kappa_q}{mt}
+O(1),
\qquad m=2r+1.
\]

Multiplication by

\[
Q_\chi(\beta_r)+Q_\chi'(\beta_r)t+\cdots
\]

and by

\[
x^{\beta_r}(1+t\log x+\cdots)
\]

produces exactly the recorded logarithmic and constant coefficients.

**Review result:** PASS.

## 8. Possible hidden singularities

The review checked the following:

- zeros of other `L`-factors do not create singularities;
- an imprimitive nonprincipal character still gives an entire Dirichlet `L`-function;
- a character power equal to the principal character modulo `q` correctly produces the principal `L`-factor with residue `phi(q)/q`;
- `H` is holomorphic in the shifted half-plane;
- the two poles are distinct;
- simultaneous torsion conditions imply `chi=chi_0`, but do not merge the two pole locations.

**Review result:** PASS.

## 9. Parameter dependence and reality

The theorem is for fixed `q`, fixed `r`, and fixed `W`. No uniformity in these parameters is claimed. Summing over finitely many characters preserves the stated error and makes it independent of the reduced residue `a`.

For real `W`, conjugate characters pair to give a real total. Complex intermediate coefficients are harmless.

**Review result:** PASS.

## 10. Proof-review decision

\[
\boxed{\text{P7 INDEPENDENT INTERNAL PROOF REVIEW: PASS}}
\]

The reviewed smoothed theorem follows from the stated local factorization and standard fixed-modulus analytic prerequisites. No mathematical gap was found after adding the explicit condition `x>=1`.

## 11. What this decision does not establish

It does not establish:

- historical originality;
- publication-level novelty;
- a new analytic method;
- uniformity for growing `q` or `r`;
- an unsmoothed theorem with the same error;
- RH or GRH progress.

## 12. Remaining gate

P8 must classify the result after completing the older-source audit. The admissible classifications are:

1. original theorem candidate;
2. new PVG-derived application of a known general theorem;
3. known result in different notation;
4. corrected weaker result;
5. negative originality certificate.
