# Divisor-Box Face Enumerator — Exact Derivation and Proof Risks

## 1. Definition

For

\[
n=\prod_{p^a\parallel n}p^a
\]

and `d|n`, let

\[
b_n(d)=\#\{p\mid n:v_p(d)\in\{0,a_p\}\}.
\]

Define

\[
\Phi_z(n)=\sum_{d\mid n}z^{b_n(d)}.
\]

At each coordinate of length `a`, there are two endpoints of weight `z` and `a-1` strict interior points of weight `1`. Therefore

\[
\boxed{\Phi_z(n)=\prod_{p^a\parallel n}(a-1+2z).}
\]

This is the exact PVG-to-ANT bridge for the candidate family.

## 2. Local generating function

Put `u=p^{-s}`. Then

\[
\sum_{a\ge0}\Phi_z(p^a)u^a
=
1+\sum_{a\ge1}(a-1+2z)u^a
\]

and hence

\[
F_z(u)
=
1+\frac{2zu}{1-u}+\frac{u^2}{(1-u)^2}.
\]

Since

\[
F_z(u)=1+2zu+(1+2z)u^2+O_z(u^3),
\]

we may factor

\[
F_z(u)=(1-u)^{-2z}G_z(u),
\]

where

\[
G_z(u)=(1-u)^{2z}
\left(1+\frac{2zu}{1-u}+\frac{u^2}{(1-u)^2}\right)
=1+O_K(u^2)
\]

uniformly for `z` in a compact set `K`.

Thus, in the absolute-convergence region,

\[
\sum_{n\ge1}\frac{\Phi_z(n)}{n^s}
=
\zeta(s)^{2z}G_z(s),
\]

with `G_z(s)` represented by an Euler product converging absolutely for `Re(s)>1/2` on bounded parameter sets.

## 3. The interior phase transition

At `z=0`,

\[
I(n):=\Phi_0(n)=\prod_{p^a\parallel n}(a-1),
\]

and

\[
F_0(u)=1+\frac{u^2}{(1-u)^2}.
\]

The coefficient of `u` is zero. Geometrically, a one-step axis has no strict interior point. Analytically, the `zeta(s)` singularity disappears and the first scale moves to `2s`.

Multiplying by the first square and cube singular factors gives

\[
H_p(u)
=(1-u^2)(1-u^3)^2
\left(1+\frac{u^2}{(1-u)^2}\right).
\]

Direct formal expansion yields

\[
H_p(u)=1+O(u^4).
\]

Therefore

\[
\boxed{
D_I(s)=\zeta(2s)\zeta(3s)^2H(s)
}
\]

with

\[
H(s)=\prod_pH_p(p^{-s})
\]

absolutely convergent for `Re(s)>1/4`.

## 4. Candidate residue constants

At `s=1/2`, `zeta(2s)` has residue `1/2`. Applying Perron's kernel `x^s/s` predicts

\[
C_2=\zeta(3/2)^2H(1/2).
\]

At `s=1/3`, `zeta(3s)^2` has leading part

\[
\frac{1}{9(s-1/3)^2}.
\]

Thus the coefficient of `x^{1/3}log x` is predicted to be

\[
C_{31}=\frac{\zeta(2/3)H(1/3)}{3}.
\]

The constant `C_{30}` depends on Euler's constant, the derivative of `zeta(2s)H(s)`, and the derivative of `1/s` at `s=1/3`. It must be derived explicitly before target freeze.

## 5. r-margin hierarchy

For fixed `r>=1`, define

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0).
\]

Its local series is

\[
1+\sum_{a\ge2r}(a-2r+1)u^a
=
1+\frac{u^{2r}}{(1-u)^2}.
\]

The candidate factor extraction is

\[
H_{r,p}(u)
=(1-u^{2r})(1-u^{2r+1})^2
\left(1+\frac{u^{2r}}{(1-u)^2}\right).
\]

The deterministic formal-series check confirms

\[
H_{r,p}(u)=1+O(u^{2r+2})
\]

for `r=1,...,5`, and the identity is algebraically expected for all fixed `r`. Therefore

\[
D_r(s)=\zeta(2rs)\zeta((2r+1)s)^2H_r(s),
\]

with absolute convergence of `H_r` for `Re(s)>1/(2r+2)`.

## 6. Character twist

For a Dirichlet character `chi`, put

\[
y_p=\chi(p)p^{-s}.
\]

The same coordinate algebra gives

\[
\sum_{n\ge1}\frac{I_r(n)\chi(n)}{n^s}
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

where

\[
H_{r,\chi}(s)
=
\prod_p
(1-y_p^{2r})(1-y_p^{2r+1})^2
\left(1+\frac{y_p^{2r}}{(1-y_p)^2}\right).
\]

This predicts that residue-class main terms at the square layer are controlled by characters with `chi^(2r)=chi_0`, while cube-layer logarithmic terms are controlled by `chi^(2r+1)=chi_0`.

## 7. What is proved at intake

- the face-enumerator product identity;
- the local generating functions;
- the formal extraction of the `2r` and `2r+1` factors;
- the first residual local order through deterministic checks;
- the twisted local algebra.

## 8. What is not proved

- the full summatory asymptotics;
- the stated error term;
- explicit `C_{30}`;
- interchange and uniformity required for complex `z`;
- the residue-class theorem and its exact remainder;
- originality relative to older weighted powerful-number literature.

## 9. Proof-risk ranking

1. **Priority risk:** the weighted formula may be covered by a general theorem under different terminology.
2. **Error-term risk:** `O_epsilon(x^(1/4+epsilon))` is not automatic from the Euler-product factorization.
3. **Secondary-pole risk:** all double-pole constants and interactions must be computed exactly.
4. **Character risk:** imprimitive characters and primes dividing `q` require a fixed convention.
5. **PVG-necessity risk:** the proof may become entirely classical once the observable is defined.

**Classification:** exact derivation plus candidate proof architecture; no theorem claim.
