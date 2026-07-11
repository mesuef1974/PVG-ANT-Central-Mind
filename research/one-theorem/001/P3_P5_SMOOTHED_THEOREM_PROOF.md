# One-Theorem Program 001 — P3–P5 Smoothed Theorem Proof

**Target:** `ONE-LEMMA-TARGET-001`  
**Status:** complete manual proof candidate, pending adversarial and priority review.  
**Dependencies:** P2 local factorization, standard character orthogonality, Mellin inversion, and fixed-modulus Dirichlet-L growth.

## Theorem

Fix integers `q>=1` and `r>=1`, a reduced residue class `(a,q)=1`, a real parameter `x>=1`, and a function

\[
W\in C_c^\infty(0,\infty).
\]

Let

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0),
\qquad I_r(1)=1,
\]

and

\[
S_{r;q,a,W}(x)
=
\sum_{\substack{n\ge1\\n\equiv a\pmod q}}
I_r(n)W(n/x).
\]

Write

\[
\alpha_r=\frac1{2r},
\qquad
\beta_r=\frac1{2r+1}.
\]

For a character `chi mod q`, define

\[
D_{r,\chi}(s)
=
\sum_{n\ge1}\frac{I_r(n)\chi(n)}{n^s},
\]

\[
H_{r,\chi}(s)
=
\prod_p
(1-y_p^{2r})(1-y_p^{2r+1})^2
\left(1+\frac{y_p^{2r}}{(1-y_p)^2}\right),
\qquad
y_p=\chi(p)p^{-s},
\]

and

\[
\widehat W(s)=\int_0^\infty W(t)t^{s-1}\,dt.
\]

Let `chi_0` be the principal character modulo `q`, and put

\[
\rho_q
=
\operatorname*{Res}_{u=1}L(u,\chi_0)
=
\frac{\varphi(q)}q,
\]

\[
\kappa_q
=
\operatorname*{FP}_{u=1}L(u,\chi_0)
=
\rho_q\left(
\gamma+
\sum_{p\mid q}\frac{\log p}{p-1}
\right).
\]

Define

\[
P_\chi(s)
=
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s)\widehat W(s),
\]

\[
Q_\chi(s)
=
L(2rs,\chi^{2r})
H_{r,\chi}(s)\widehat W(s).
\]

Then, for every `epsilon>0`,

\[
\begin{aligned}
S_{r;q,a,W}(x)
=\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}
\Bigg[&
\mathbf1_{\chi^{2r}=\chi_0}
\frac{\rho_q}{2r}
P_\chi(\alpha_r)x^{\alpha_r}
\\
&+
\mathbf1_{\chi^{2r+1}=\chi_0}
 x^{\beta_r}
 \left(B_\chi\log x+C_\chi\right)
\Bigg]
\\
&+
O_{q,r,W,\varepsilon}
\left(x^{1/(2r+2)+\varepsilon}\right),
\end{aligned}
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

The implied constant may depend on `q,r,W,epsilon`, but not on `a` or `x`.

---

## Step 1 — character decomposition

For `(a,q)=1`, character orthogonality gives, for every integer `n`,

\[
\mathbf1_{n\equiv a\pmod q}
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n).
\]

Indeed, if `(n,q)>1`, both sides vanish; otherwise this is the ordinary Fourier inversion formula on `(\mathbb Z/q\mathbb Z)^\times`.

Because `W` has compact support, the sum over `n` is finite for each `x`. Hence

\[
S_{r;q,a,W}(x)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}S_{r,\chi,W}(x),
\]

where

\[
S_{r,\chi,W}(x)
=
\sum_{n\ge1}I_r(n)\chi(n)W(n/x).
\]

---

## Step 2 — Mellin inversion

Since `W` is smooth with compact support in `(0,infinity)`, its Mellin transform is entire and, in every fixed vertical strip, decays faster than any power of `|Im(s)|`.

Choose

\[
c>\frac1{2r}.
\]

Mellin inversion gives

\[
W(n/x)
=
\frac1{2\pi i}\int_{(c)}
\widehat W(s)x^sn^{-s}\,ds.
\]

The Dirichlet series for `D_{r,chi}` converges absolutely on this line, so summation and integration may be interchanged:

\[
S_{r,\chi,W}(x)
=
\frac1{2\pi i}\int_{(c)}
D_{r,\chi}(s)\widehat W(s)x^s\,ds.
\]

By P2,

\[
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

and the right side is meromorphic for

\[
\Re(s)>\frac1{2r+2}.
\]

---

## Step 3 — contour shift and remainder

First suppose

\[
0<\varepsilon<
\frac1{2r+1}-\frac1{2r+2}.
\]

Set

\[
\sigma_0=\frac1{2r+2}+\varepsilon.
\]

Shift the line of integration from `Re(s)=c` to `Re(s)=sigma_0`.

The only poles crossed are:

1. `s=alpha_r`, if `chi^(2r)=chi_0`, and it is simple;
2. `s=beta_r`, if `chi^(2r+1)=chi_0`, and it is double.

To justify the shift, truncate at heights `+-T`. On the closed strip between `sigma_0` and `c`:

- `H_{r,chi}(s)` is bounded uniformly in the vertical direction, because its Euler product converges absolutely with a majorant independent of `Im(s)`;
- each fixed-modulus Dirichlet L-function has at most polynomial growth in `|Im(s)|` on fixed vertical strips;
- `W-hat(s)` decays faster than every polynomial.

Therefore the horizontal integrals tend to zero as `T` tends to infinity, and the new vertical integral converges absolutely. It satisfies

\[
\int_{(\sigma_0)}
D_{r,\chi}(s)\widehat W(s)x^s\,ds
\ll_{q,r,W,\varepsilon}x^{\sigma_0}.
\]

For an arbitrary larger `epsilon`, apply the result with a smaller positive `epsilon_0` below the displayed gap. Since `x^(boundary+epsilon_0)<=x^(boundary+epsilon)` for `x>=1`, the stated error follows for every `epsilon>0`.

It remains to calculate the crossed residues.

---

## Step 4 — the simple pole at `alpha_r`

Suppose

\[
\chi^{2r}=\chi_0.
\]

Near

\[
\alpha_r=\frac1{2r},
\]

we have

\[
L(2rs,\chi_0)
=
\frac{\rho_q}{2r(s-\alpha_r)}
+
\kappa_q
+
O(s-\alpha_r).
\]

The factor `P_chi(s)` is holomorphic at `alpha_r`: the other L-function is evaluated at

\[
(2r+1)\alpha_r=1+\frac1{2r}>1.
\]

Hence

\[
\operatorname*{Res}_{s=\alpha_r}
D_{r,\chi}(s)\widehat W(s)x^s
=
\frac{\rho_q}{2r}
P_\chi(\alpha_r)x^{\alpha_r}.
\]

If `chi^(2r)` is not principal, there is no pole at `alpha_r`.

---

## Step 5 — the double pole at `beta_r`

Suppose

\[
\chi^{2r+1}=\chi_0.
\]

Put

\[
m=2r+1,
\qquad
\beta_r=\frac1m,
\qquad
t=s-\beta_r.
\]

Then

\[
L(ms,\chi_0)
=
\frac{\rho_q}{mt}+\kappa_q+O(t),
\]

so

\[
L(ms,\chi_0)^2
=
\frac{\rho_q^2}{m^2t^2}
+
\frac{2\rho_q\kappa_q}{mt}
+
O(1).
\]

The factor `Q_chi(s)` is holomorphic at `beta_r`; in particular, the remaining L-function is evaluated at

\[
2r\beta_r=\frac{2r}{2r+1}<1
\]

but away from its only possible pole at `1`.

Expand

\[
Q_\chi(s)
=
Q_\chi(\beta_r)
+Q_\chi'(\beta_r)t
+O(t^2)
\]

and

\[
x^s
=x^{\beta_r}
\left(1+t\log x+O(t^2)\right).
\]

The coefficient of `t^(-1)` is

\[
x^{\beta_r}
\left[
\frac{\rho_q^2}{m^2}
Q_\chi(\beta_r)\log x
+
\frac{\rho_q^2}{m^2}
Q_\chi'(\beta_r)
+
\frac{2\rho_q\kappa_q}{m}
Q_\chi(\beta_r)
\right].
\]

This is exactly

\[
x^{\beta_r}(B_\chi\log x+C_\chi).
\]

If `chi^(2r+1)` is not principal, there is no pole at `beta_r`.

---

## Step 6 — sum over characters

Insert the residues and shifted-line error into the character decomposition. There are only `phi(q)` characters, and `q` is fixed. The error remains

\[
O_{q,r,W,\varepsilon}
\left(x^{1/(2r+2)+\varepsilon}\right).
\]

The resulting formula is precisely the theorem statement.

This completes the manual proof candidate.

---

## Principal-character Laurent constants

For completeness,

\[
L(u,\chi_0)
=
\zeta(u)E_q(u),
\qquad
E_q(u)=\prod_{p\mid q}(1-p^{-u}).
\]

Now

\[
E_q(1)=\rho_q
\]

and

\[
\frac{E_q'(1)}{E_q(1)}
=
\sum_{p\mid q}\frac{\log p}{p-1}.
\]

Using

\[
\zeta(u)=\frac1{u-1}+\gamma+O(u-1),
\]

we obtain

\[
L(u,\chi_0)
=
\frac{\rho_q}{u-1}
+
\rho_q\left(
\gamma+\sum_{p\mid q}\frac{\log p}{p-1}
\right)
+O(u-1),
\]

which is the stated formula for `kappa_q`.

---

## Edge cases

### `q=1`

There is one character, the principal character. Empty products give

\[
\rho_1=1,
\qquad
\kappa_1=\gamma.
\]

The theorem reduces to the smoothed global formula.

### Vanishing residue coefficient

It may happen that `P_chi(alpha_r)=0` or `Q_chi(beta_r)=0`. The displayed term then vanishes. The pole analysis still remains correct: the product can have a removable singularity after cancellation by a zero in the holomorphic factor. The formula records the actual residue, including the possibility of zero.

### Complex weights

The argument is valid for complex-valued `W`; for real-valued `W`, conjugate character terms combine to give a real result.

---

## Proof classification

```text
Geometric definition: exact.
Bell series and factorization: proved in P2.
Character decomposition: proved.
Mellin inversion: standard and justified by absolute convergence.
Contour shift: justified by smooth Mellin decay and fixed-q polynomial L-growth.
Residues: calculated explicitly.
Remainder: proved for fixed q,r,W.
Originality: not certified.
Publication readiness: not certified.
```

## Ceiling

This is a complete manual proof candidate of the frozen smoothed statement. It is not yet a certified original theorem, and it implies no RH/GRH progress.
