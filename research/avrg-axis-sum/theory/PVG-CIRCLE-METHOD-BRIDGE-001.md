# PVG Circle-Method Bridge 001

Status: exact Fourier identities plus geometric interpretation.

Scientific ceiling: no new major-arc estimate, no new minor-arc estimate, and no proof of Goldbach.

## 1. Fourier phase lifted to PVG

Write

\[
e(\alpha)=e^{2\pi i\alpha}.
\]

For a valuation vector \(x\), define

\[
\boxed{\mathcal E_\alpha(x)=e(\alpha\rho(x)).}
\]

This is nonlinear in valuation coordinates:

\[
\mathcal E_\alpha(x)
=
\exp\left(2\pi i\alpha\prod_p p^{x_p}\right).
\]

## 2. Orthogonality

For every integer \(m\),

\[
\int_0^1e(\alpha m)\,d\alpha
=
\mathbf1_{m=0}.
\]

Therefore

\[
\mathbf1_{a+b=N}
=
\int_0^1e(\alpha(a+b-N))\,d\alpha.
\]

## 3. Fourier convolution theorem

For finitely supported arithmetic functions \(f,g\), define

\[
S_f(\alpha)=\sum_{n\ge1}f(n)e(\alpha n),
\qquad
S_g(\alpha)=\sum_{n\ge1}g(n)e(\alpha n).
\]

Then

\[
\boxed{
(f*_+g)(N)
=
\int_0^1S_f(\alpha)S_g(\alpha)e(-\alpha N)\,d\alpha.
}
\]

After lifting to PVG,

\[
\mathscr F_f(\alpha)
=
\sum_x\widehat f(x)\mathcal E_\alpha(x)
=
S_f(\alpha),
\]

and hence

\[
\boxed{
(f*_+g)(N)
=
\int_0^1
\mathscr F_f(\alpha)
\mathscr F_g(\alpha)
e(-\alpha N)\,d\alpha.
}
\]

## 4. Goldbach circle integral

For \(f=g=\Lambda\),

\[
S(\alpha;N)=\sum_{n\le N}\Lambda(n)e(\alpha n)
\]

and

\[
\boxed{
R_\Lambda(N)
=
\int_0^1S(\alpha;N)^2e(-\alpha N)\,d\alpha.
}
\]

In PVG,

\[
S(\alpha;N)
=
\sum_{\rho(x)\le N}
\widehat\Lambda(x)\mathcal E_\alpha(x).
\]

Since \(\widehat\Lambda\) is supported on prime-power axes,

\[
S(\alpha;N)
=
\sum_{p^k\le N}(\log p)e(\alpha p^k).
\]

Interpretation: the Goldbach circle method studies interference among waves supported on prime-power axes. This interpretation is exact at the level of the displayed identity, but it does not by itself improve any estimate.

## 5. Major arcs as residue-fiber resonance

For

\[
\alpha=\frac aq+\beta,
\]

we have

\[
S(\alpha;N)
=
\sum_{c\bmod q}
e\left(\frac{ac}{q}\right)
\sum_{\substack{n\le N\\n\equiv c\pmod q}}
\Lambda(n)e(\beta n).
\]

In PVG,

\[
\boxed{
S(\alpha;N)
=
\sum_{c\bmod q}
e\left(\frac{ac}{q}\right)
\sum_{\substack{x:\rho(x)\le N\\\rho(x)\equiv c\pmod q}}
\widehat\Lambda(x)\mathcal E_\beta(x).
}
\]

Thus a rational frequency \(a/q\) reads the valuation space through its residue-fiber partition modulo \(q\).

The major-arc layer couples:

1. prime-axis geometry;
2. residue-fiber geometry;
3. a slowly varying perturbation \(e(\beta\rho(x))\).

## 6. Ramanujan sums

The Ramanujan sum

\[
c_q(N)
=
\sum_{\substack{a\bmod q\\(a,q)=1}}
e\left(\frac{aN}{q}\right)
\]

is the Fourier response of the reduced-residue geometry at frequency \(N\).

Because \(N\) indexes the addition fiber, \(c_q(N)\) describes how that fiber interacts with the reduced-residue system modulo \(q\).

## 7. Local residue-fiber density

For a prime \(p\), define

\[
\mathcal L_{N,p}
=
\{(a,b)\in(\mathbb F_p^\times)^2:a+b=N\}.
\]

Then

\[
|\mathcal L_{N,p}|
=
\begin{cases}
p-2,&p\nmid N,\\
p-1,&p\mid N.
\end{cases}
\]

Proof:

- If \(p\nmid N\), \(a\) must avoid \(0\) and \(N\), leaving \(p-2\) choices.
- If \(p\mid N\), then \(b=-a\), and each nonzero \(a\) is valid, giving \(p-1\) choices.

After the standard normalization, the singular series is interpreted as an Euler product of these local residue-fiber corrections:

\[
\boxed{
\mathfrak S(N)
=
\prod_p\delta_p(N),
}
\]

with the precise factor \(\delta_p(N)\) depending on the chosen normalization.

This is a geometric interpretation of a known analytic object, not a newly proved singular-series formula.

## 8. The special role of \(p=2\)

If \(N\) is odd, two odd primes cannot sum to \(N\). Hence any prime-prime point on an odd addition fiber must contain \(e_2\):

\[
\mathcal G_N\cap(\mathcal P_1^2)
\subset
(\{e_2\}\times\mathcal P_1)
\cup
(\mathcal P_1\times\{e_2\}).
\]

This is the valuation-geometric expression of the parity obstruction at the local factor \(2\).

## 9. Minor arcs

On minor arcs, \(\alpha\) is not well approximated by rationals of small denominator. The phase

\[
\mathcal E_\alpha(x)=e(\alpha\rho(x))
\]

therefore does not align with a simple small-modulus residue partition.

The analytic task remains to prove sufficient cancellation in

\[
\sum_x\widehat\Lambda(x)\mathcal E_\alpha(x).
\]

PVG language does not remove this wall. Any claimed advance must provide a quantitatively stronger bound or a new mechanism for this cancellation.

## 10. Circle-method dictionary

| Circle method | PVG translation |
|---|---|
| \(e(\alpha n)\) | \(\mathcal E_\alpha(x)=e(\alpha\rho(x))\) |
| exponential sum \(S(\alpha)\) | sum of weighted valuation waves |
| \(\alpha\approx a/q\) | resonance with residue fibers modulo \(q\) |
| major arcs | small-modulus local structure |
| minor arcs | nonresonant cancellation wall |
| Ramanujan sums | reduced-residue Fourier response |
| singular series | product of normalized local fiber densities |
| main term | local-density contribution times global scale |
| error term | contribution not controlled by local resonances |

## 11. Next operator layer

A candidate fiber Fourier operator is

\[
\mathcal T_\alpha W(N)
=
\int_{\mathcal G_N}
W(x,y)
\mathcal E_\alpha(x)
\mathcal E_\alpha(y)
\,d\mu_N(x,y).
\]

Because \(\rho(x)+\rho(y)=N\) on \(\mathcal G_N\),

\[
\mathcal E_\alpha(x)\mathcal E_\alpha(y)=e(\alpha N),
\]

so on a fixed exact fiber this operator collapses to

\[
\mathcal T_\alpha W(N)
=
e(\alpha N)
\int_{\mathcal G_N}W\,d\mu_N.
\]

This observation is crucial: a nontrivial Fourier operator must act before imposing the exact fiber constraint, or use asymmetric/difference phases. The next construction should therefore employ one of:

\[
\mathcal E_\alpha(x)e(-\alpha N),
\qquad
\mathcal E_\alpha(x)\overline{\mathcal E_\alpha(y)},
\qquad
\chi(\rho(x)-\rho(y)),
\]

or an ambient-pair operator followed by fiber projection.

This prevents a false claim of spectral richness from an operator that is constant on every exact addition fiber.
