# Von Mangoldt Additive-Fiber Observables — v1.2

Status: `PROVED IDENTITIES / ARITHMETIC ACTIVATION`

## 1. Arithmetic weight on an addition fiber

For an integer `N >= 2`, define

\[
w_N(a)=\Lambda(a)\Lambda(N-a),\qquad 1\le a\le N-1,
\]

and the weighted additive representation function

\[
R_\Lambda(N)=\sum_{a=1}^{N-1}\Lambda(a)\Lambda(N-a).
\]

Under the valuation encoding, the same quantity is

\[
R_\Lambda(N)
=
\int_{\mathcal G_N}
\widehat\Lambda(x)\widehat\Lambda(y)\,d\mu_N(x,y).
\]

This is an exact translation, not a new estimate.

## 2. Difference-channel observable

For a modulus `r >= 1`, define

\[
Y_{N,r}(d)
=
\sum_{\substack{1\le a\le N-1\\2a-N\equiv d\pmod r}}
\Lambda(a)\Lambda(N-a).
\]

Equivalently,

\[
Y_{N,r}=D_{N,r}w_N.
\]

### Theorem 2.1 — zero-frequency mass identity

\[
\boxed{
\sum_{d\bmod r}Y_{N,r}(d)=R_\Lambda(N)
}
\]

for every `N` and `r`.

### Proof

The congruence classes partition the index set `1 <= a <= N-1`, so summing all channel coordinates returns the complete fiber sum.

## 3. Reflection symmetry

Since

\[
w_N(N-a)=\Lambda(N-a)\Lambda(a)=w_N(a),
\]

and

\[
2(N-a)-N=-(2a-N),
\]

we obtain:

### Theorem 3.1 — channel reflection law

\[
\boxed{
Y_{N,r}(d)=Y_{N,r}(-d)
}
\]

for every residue class `d mod r`.

Consequently, only one representative from each pair `{d,-d}` is independent.

## 4. Support geometry

The von Mangoldt function satisfies

\[
\Lambda(n)\ne0
\iff
n=p^k
\]

for some prime `p` and integer `k>=1`.

Therefore:

### Proposition 4.1 — prime-power-pair support

\[
\boxed{
w_N(a)\ne0
\iff
a=p^k\text{ and }N-a=q^\ell}
\]

for primes `p,q` and integers `k,l>=1`.

In valuation geometry, the support lies on

\[
\mathcal A_1\times\mathcal A_1,
\]

not merely on

\[
\mathcal P_1\times\mathcal P_1.
\]

This distinction is essential: `R_Lambda(N)` is a prime-power weighted representation function, not the pure Goldbach count.

## 5. Exact decomposition into prime and higher-prime-power channels

Write

\[
\Lambda=\Lambda_{\mathrm{pr}}+\Lambda_{\mathrm{hpp}},
\]

where

\[
\Lambda_{\mathrm{pr}}(n)=
\begin{cases}
\log n,&n\text{ prime},\\
0,&\text{otherwise},
\end{cases}
\]

and `Lambda_hpp` is supported on prime powers `p^k` with `k>=2`.

Then

\[
R_\Lambda(N)
=
R_{\mathrm{pp}}(N)
+R_{\mathrm{ph}}(N)
+R_{\mathrm{hp}}(N)
+R_{\mathrm{hh}}(N),
\]

with the four exact terms

\[
R_{\alpha\beta}(N)
=
\sum_{a=1}^{N-1}
\Lambda_\alpha(a)\Lambda_\beta(N-a),
\qquad
\alpha,\beta\in\{\mathrm{pr},\mathrm{hpp}\}.
\]

By reflection,

\[
R_{\mathrm{ph}}(N)=R_{\mathrm{hp}}(N).
\]

Thus

\[
\boxed{
R_\Lambda(N)
=
R_{\mathrm{pp}}(N)
+2R_{\mathrm{ph}}(N)
+R_{\mathrm{hh}}(N)
}
\]

where `R_pp` is the logarithmically weighted pure-prime Goldbach observable.

The same decomposition holds coordinatewise in every difference, marginal, and joint channel.

## 6. Joint and marginal arithmetic data

For a modulus family `r = (r_1,...,r_s)`, define the joint arithmetic cell data

\[
Z_{N;\mathbf r}(\eta)
=
\sum_{\substack{1\le a\le N-1\\
(2a-N\bmod r_j)_j=\eta}}
\Lambda(a)\Lambda(N-a).
\]

Then

\[
Z_{N;\mathbf r}=J_{N;\mathbf r}w_N,
\qquad
(Y_{N,r_1},\dots,Y_{N,r_s})=M_{N;\mathbf r}w_N,
\]

and the previously proved factorization gives

\[
M_{N;\mathbf r}w_N
=
B_{N;\mathbf r}J_{N;\mathbf r}w_N.
\]

Therefore all previously proved rank, kernel, information-gap, and conditioning results apply to the arithmetic weight `w_N` without modification.

## 7. What is and is not gained

The activation yields exact arithmetic observables and exact information-loss statements. It does not by itself yield:

- a positive lower bound for `R_pp(N)`;
- a proof that every even `N` has a prime-prime representation;
- a new major-arc or minor-arc estimate;
- a new sieve estimate;
- progress on RH or GRH.

The next valid question is whether the compressed channel data permit a nontrivial estimate or certificate for `R_pp(N)` after controlling the higher-prime-power contamination.
