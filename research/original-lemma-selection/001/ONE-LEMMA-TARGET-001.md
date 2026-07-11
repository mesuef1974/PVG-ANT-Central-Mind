# ONE-LEMMA-TARGET-001

## Working title

**Smoothed torsion layers of margin-interior divisor boxes in arithmetic progressions**

## Status

```text
Target: FROZEN FOR READINESS REVIEW
Originality: plausible, not certified
Proof: not yet executed
Claim class: candidate theorem package
```

## 1. Geometric observable

Fix an integer `r>=1`. For

\[
n=\prod_{p^a\parallel n}p^a,
\]

define

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0),
\qquad I_r(1)=1.
\]

Equivalently,

\[
I_r(n)
=
\#\left\{
 d\mid n:
 r\le v_p(d)\le v_p(n)-r
 \text{ for every }p\mid n
\right\}.
\]

Thus `I_r(n)` counts lattice points whose coordinate distance from every facet of the divisor box is at least `r`.

## 2. Twisted Dirichlet series

Fix a modulus `q>=1`. Dirichlet characters modulo `q` are extended by zero off the reduced residue classes. For a character `chi mod q`, define

\[
D_{r,\chi}(s)
=
\sum_{n\ge1}\frac{I_r(n)\chi(n)}{n^s}.
\]

For each prime put

\[
y_p=\chi(p)p^{-s}
\]

and

\[
H_{r,\chi}(s)
=
\prod_p
(1-y_p^{2r})(1-y_p^{2r+1})^2
\left(1+\frac{y_p^{2r}}{(1-y_p)^2}\right).
\]

### Target Lemma A — exact factorization

Initially in the absolute-convergence region,

\[
\boxed{
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s).
}
\]

Moreover, `H_{r,chi}` converges absolutely and locally uniformly for

\[
\Re s>\frac1{2r+2}.
\]

The convention at primes dividing `q` must be stated explicitly; there `chi(p)=0` and every displayed local factor equals `1`.

## 3. Principal-character Laurent data

Let `chi_0` be the principal character modulo `q`, and define

\[
\rho_q
=
\operatorname*{Res}_{u=1}L(u,\chi_0)
=
\prod_{p\mid q}\left(1-\frac1p\right)
=
\frac{\varphi(q)}q,
\]

and

\[
\kappa_q
=
\operatorname*{FP}_{u=1}L(u,\chi_0).
\]

Equivalently,

\[
\kappa_q
=
\rho_q
\left(
\gamma+
\sum_{p\mid q}\frac{\log p}{p-1}
\right).
\]

## 4. Smoothed residue-class sum

Let `W in C_c^infinity(0,infinity)` and

\[
\widehat W(s)=\int_0^\infty W(t)t^{s-1}\,dt.
\]

For `(a,q)=1`, define

\[
S_{r;q,a,W}(x)
=
\sum_{\substack{n\ge1\\n\equiv a\pmod q}}
I_r(n)W(n/x).
\]

Set

\[
\alpha_r=\frac1{2r},
\qquad
\beta_r=\frac1{2r+1}.
\]

For each character define

\[
P_\chi(s)
=
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s)\widehat W(s),
\]

and

\[
Q_\chi(s)
=
L(2rs,\chi^{2r})
H_{r,\chi}(s)\widehat W(s).
\]

### Target Theorem B — smoothed torsion-layer expansion

For fixed `q,r,W` and every `epsilon>0`, as `x→infinity`,

\[
\boxed{
\begin{aligned}
S_{r;q,a,W}(x)
=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(a)}
\Bigg[&
\mathbf1_{\chi^{2r}=\chi_0}
\frac{\rho_q}{2r}
P_\chi(\alpha_r)x^{\alpha_r}
\\
&+
\mathbf1_{\chi^{2r+1}=\chi_0}
 x^{\beta_r}
 \left(
 B_\chi\log x+C_\chi
 \right)
\Bigg]
\\
&+
O_{q,r,W,\varepsilon}
\left(x^{1/(2r+2)+\varepsilon}\right),
\end{aligned}
}
\]

where

\[
B_\chi
=
\frac{\rho_q^2}{(2r+1)^2}
Q_\chi(\beta_r),
\]

and

\[
C_\chi
=
\frac{\rho_q^2}{(2r+1)^2}
Q_\chi'(\beta_r)
+
\frac{2\rho_q\kappa_q}{2r+1}
Q_\chi(\beta_r).
\]

## 5. Meaning of the theorem

The first geometric interior layer occurs at exponent `2r`; it produces the `x^(1/(2r))` scale and is visible only in character coordinates satisfying

\[
\chi^{2r}=\chi_0.
\]

The next layer occurs at exponent `2r+1`; its squared L-factor produces an `x^(1/(2r+1))log x` term and is visible only when

\[
\chi^{2r+1}=\chi_0.
\]

This is the proposed **torsion-selection law** linking divisor-box geometry to residue-fiber Fourier coordinates.

## 6. Special cases

### q=1, r=1

The theorem gives the smoothed strict-interior average

\[
\sum_n I_1(n)W(n/x)
=
A_Wx^{1/2}
+x^{1/3}(B_W\log x+C_W)
+O_{W,\varepsilon}(x^{1/4+\varepsilon}).
\]

### z-family context

`I_1=Phi_0`, where

\[
\Phi_z(n)=\prod_{p^a\parallel n}(a-1+2z).
\]

Thus the target describes the singularity transition that occurs when the ordinary `zeta(s)^(2z)` scale disappears at `z=0`.

## 7. Proof route

1. coordinate enumeration of margin-interior points;
2. exact Bell-series computation;
3. local factor cancellation through order `2r+1`;
4. absolute convergence of `H_{r,chi}`;
5. character orthogonality;
6. Mellin inversion;
7. contour shift to `Re(s)=1/(2r+2)+epsilon`;
8. simple-pole residue at `alpha_r`;
9. double-pole residue at `beta_r`;
10. vertical-line estimate from rapid Mellin decay and polynomial L-function bounds.

## 8. Failure conditions

The target is rejected or reclassified if:

- an exact prior theorem with the same weight and expansion is located;
- the local factorization or Laurent constants fail symbolic review;
- the contour remainder cannot be proved with the stated exponent;
- the PVG-necessity review concludes the geometry is merely decorative;
- bad-prime/imprimitive-character conventions alter the stated constants.

## 9. Scientific ceiling

```text
Frozen candidate target only.
No original lemma certified.
No theorem proved.
No RH/GRH progress.
```
