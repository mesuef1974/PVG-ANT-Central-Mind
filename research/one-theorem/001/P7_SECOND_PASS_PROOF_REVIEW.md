# One-Theorem Program 001 — P7 Second-Pass Proof Review

**Reviewed artifacts:** P2 local factorization, P3–P5 smoothed theorem proof, P4 analytic prerequisites, P6 adversarial review.  
**Review type:** independent reconstruction from the frozen statement, not an external referee report.  
**Decision:** `PASS MATHEMATICAL RECONSTRUCTION / EXTERNAL PRIORITY REVIEW STILL REQUIRED`.

## 1. Independent reconstruction of the coefficient

For a prime power `p^alpha`, the condition that a divisor coordinate remain at least `r` from both endpoints is

\[
r\le \beta\le \alpha-r.
\]

The number of allowed values is

\[
\max(\alpha-2r+1,0).
\]

Independence of distinct prime coordinates gives

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

Equivalently,

\[
I_r(n)=
\mathbf 1_{\operatorname{rad}(n)^{2r}\mid n}
\tau\!\left(n/\operatorname{rad}(n)^{2r}\right).
\]

Both derivations agree. Multiplicativity follows immediately.

**Decision:** pass.

## 2. Independent Bell-series reconstruction

At a prime,

\[
I_r(p^\alpha)=0\quad(1\le\alpha<2r),
\]

and

\[
I_r(p^{2r+j})=j+1\quad(j\ge0).
\]

Hence

\[
\sum_{\alpha\ge0}I_r(p^\alpha)y^\alpha
=1+y^{2r}\sum_{j\ge0}(j+1)y^j
=1+\frac{y^{2r}}{(1-y)^2}.
\]

**Decision:** pass.

## 3. Independent L-factor extraction

The local Bell series has initial expansion

\[
1+y^{2r}+2y^{2r+1}+O_r(y^{2r+2}).
\]

The inverse of

\[
(1-y^{2r})(1-y^{2r+1})^2
\]

has the same first two nonconstant coefficients. Therefore

\[
h_r(y)=
(1-y^{2r})(1-y^{2r+1})^2
\left(1+\frac{y^{2r}}{(1-y)^2}\right)
=1+O_r(y^{2r+2}).
\]

With `y=chi(p)p^(-s)`, primewise multiplication gives

\[
D_{r,\chi}(s)=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s).
\]

At primes dividing `q`, every character value is zero and all three local factors equal one. No bad-prime correction is missing.

**Decision:** pass.

## 4. Residual Euler product

On a compact subset of

\[
\Re(s)>\frac1{2r+2},
\]

we have

\[
|h_r(\chi(p)p^{-s})-1|
\ll p^{-(2r+2)\sigma_0}
\]

for large primes. The prime majorant is summable. Finite exceptional local factors are holomorphic because `|chi(p)p^(-s)|<1` in the positive half-plane.

The proof correctly claims holomorphy, not global nonvanishing.

**Decision:** pass.

## 5. Pole set

The only poles in the continuation half-plane can arise from principal Dirichlet L-functions:

- `s=1/(2r)` when `chi^(2r)=chi_0`, simple;
- `s=1/(2r+1)` when `chi^(2r+1)=chi_0`, double.

The locations are distinct. If both character conditions hold, `chi=chi_0`, but this does not merge the poles.

Zeros of L-functions or of `H` cannot create additional poles.

**Decision:** pass.

## 6. Character decomposition

For reduced `a mod q`,

\[
\mathbf1_{n\equiv a\pmod q}
=\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n).
\]

When `(n,q)>1`, both sides vanish. Thus no coprimality correction is missing.

**Decision:** pass.

## 7. Mellin normalization

For `W in C_c^infinity(0,infinity)`,

\[
W(n/x)=\frac1{2\pi i}\int_{(c)}\widehat W(s)x^s n^{-s}\,ds.
\]

This is Mellin inversion, not Perron inversion. Therefore there is **no factor `1/s`** and no derivative of `1/s` in the double-pole constant.

The starting line `c>1/(2r)` lies in the absolute-convergence half-plane.

**Decision:** pass.

## 8. Contour shift

Choose

\[
\sigma_0=\frac1{2r+2}+\varepsilon_0
<\frac1{2r+1}.
\]

The residual product is bounded vertically on the closed strip, fixed-modulus L-functions have polynomial vertical growth, and `W-hat` has rapid decay. The horizontal sides vanish and the new vertical integral is

\[
O_{q,r,W,\varepsilon_0}(x^{\sigma_0}).
\]

The extension from sufficiently small `epsilon_0` to arbitrary `epsilon>0` is a valid weakening for `x>=1`.

**Decision:** pass, subject only to inserting an exact standard citation in a publication manuscript.

## 9. Simple-pole residue

At

\[
\alpha_r=1/(2r),
\]

scaling the principal pole by `u=2rs` gives residue

\[
\frac{\rho_q}{2r}.
\]

The remaining factor is holomorphic because `(2r+1)alpha_r>1`.

**Decision:** pass.

## 10. Double-pole residue

At

\[
\beta_r=1/(2r+1),
\]

write `m=2r+1` and `t=s-beta_r`. Then

\[
L(ms,\chi_0)^2
=\frac{\rho_q^2}{m^2t^2}
+\frac{2\rho_q\kappa_q}{mt}+O(1).
\]

Multiplication by

\[
Q_\chi(\beta_r)+Q_\chi'(\beta_r)t+O(t^2)
\]

and

\[
x^{\beta_r}(1+t\log x+O(t^2))
\]

produces exactly

\[
B_\chi=
\frac{\rho_q^2}{m^2}Q_\chi(\beta_r)
\]

and

\[
C_\chi=
\frac{\rho_q^2}{m^2}Q_\chi'(\beta_r)
+\frac{2\rho_q\kappa_q}{m}Q_\chi(\beta_r).
\]

This agrees with the independent symbolic certificate.

**Decision:** pass.

## 11. Principal finite part

For

\[
L(u,\chi_0)=\zeta(u)\prod_{p\mid q}(1-p^{-u}),
\]

the residue is

\[
\rho_q=\varphi(q)/q,
\]

and the finite part is

\[
\kappa_q=ho_q\left(\gamma+\sum_{p\mid q}\frac{\log p}{p-1}\right).
\]

The sign of the correction is positive. The symbolic/numerical checks at sample moduli agree.

**Decision:** pass.

## 12. Uniformity and quantifiers

The proof is for fixed `q`, fixed `r`, fixed `W`, and `x to infinity`. The error is uniform in the reduced class `a mod q` because only unit-modulus character coefficients depend on `a`.

No growing-modulus, growing-margin, sharp-cutoff, or unsmoothed statement is proved.

**Decision:** pass after adding the phrase `as x tends to infinity` explicitly in any manuscript theorem statement.

## 13. PVG-necessity audit

PVG is materially responsible for:

- selecting the margin-interior observable;
- deriving the product over coordinate margins;
- predicting the first two surviving analytic layers.

However, after the classical identity

\[
I_r(n)=\mathbf1_{rad(n)^{2r}|n}\tau(n/rad(n)^{2r})
\]

is stated, the analytic proof is conventional. Thus:

```text
PVG discovery contribution: material.
PVG proof necessity: weak.
New analytic method: no.
```

## 14. Second-pass decision

\[
\boxed{\text{THE MANUAL PROOF IS MATHEMATICALLY COHERENT AT FIXED PARAMETERS}}
\]

No formula correction was found. The remaining obstacle is priority/significance classification, not an identified proof gap.

## 15. Ceiling

```text
Second-pass mathematical reconstruction: PASS.
External human referee review: not performed.
Exact-source publication citations: still to pin.
Originality: not certified.
Certified theorem: no.
RH/GRH progress: none.
```
