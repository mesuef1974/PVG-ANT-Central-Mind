# Prime-Valuation Addition Fibers: Exact Translation and Reconstruction

## Status

Working draft for internal research development.

## Scientific classification

- Definitions are marked as definitions.
- Exact identities are proved.
- New theorem claims are limited to statements proved in this draft or in linked theorem files.
- Literature priority is not claimed.
- No Goldbach proof, no new major/minor-arc estimate, and no RH/GRH progress are claimed.

## Abstract

We introduce the ordered positive addition fiber

\[
\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}
\]

and its exact image in prime-valuation coordinates

\[
\mathcal G_N=\{(\nu(a),\nu(b)):a+b=N\}.
\]

The valuation map loses no information on positive integers, so \(\mathcal G_N\) is an exact recoding of the additive fiber rather than an approximation. We develop its counting measure, symmetry, additive-convolution identity, prime and prime-power loci, residue subfibers, and Fourier difference channels. We then prove an exact rank formula for the modular difference-channel operator:

\[
\operatorname{rank}D_{N,r}=\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

This yields complete reconstruction for odd \(r\ge N-1\), and identifies restricted and stable reconstruction as the nontrivial next problem.

## 1. Introduction

Prime-valuation coordinates linearize multiplication:

\[
\nu(ab)=\nu(a)+\nu(b).
\]

Addition is not linear in these coordinates. Instead, for fixed \(N\), the equation \(a+b=N\) defines a nonlinear finite fiber in valuation space. The purpose of this paper is to isolate this fiber as a mathematical object and to study exact observables and reconstruction operators on it.

The framework has three layers:

1. exact finite geometry of addition fibers;
2. exact translation of additive convolutions into weighted fiber sums;
3. rank, kernel, and stability questions for observable families.

Goldbach is used only as an application illustrating the prime-axis locus.

## 2. Prime-valuation preliminaries

### Definition 2.1 (valuation vector)

For \(n\ge1\), define

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}\in\mathbb N_0^{(\mathbb P)}.
\]

### Definition 2.2 (recovery map)

For finitely supported \(x=(x_p)_p\), define

\[
\rho(x)=\prod_p p^{x_p}.
\]

### Proposition 2.3 (exact recovery)

For every \(n\ge1\),

\[
\rho(\nu(n))=n.
\]

Consequently, \(\nu\) is injective on positive integers.

## 3. Addition fibers

### Definition 3.1 (ordered positive addition fiber)

For \(N\ge2\),

\[
\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}.
\]

### Definition 3.2 (prime-valuation addition fiber)

\[
\mathcal G_N=(\nu\times\nu)(\mathcal F_N^+).
\]

Equivalently,

\[
\mathcal G_N=\{(x,y):\rho(x)+\rho(y)=N\}.
\]

### Theorem 3.3 (no-loss fiber translation)

The map

\[
\iota_N:\mathcal F_N^+\to\mathcal G_N,
\qquad
(a,b)\mapsto(\nu(a),\nu(b))
\]

is a bijection.

#### Proof

Surjectivity is immediate from the definition of \(\mathcal G_N\). If

\[
(\nu(a),\nu(b))=(\nu(c),\nu(d)),
\]

then injectivity of \(\nu\) gives \(a=c\) and \(b=d\). Hence \(\iota_N\) is injective.

### Definition 3.4 (fiber reflection)

\[
\sigma(x,y)=(y,x).
\]

Then \(\sigma^2=\mathrm{id}\) and \(\sigma(\mathcal G_N)=\mathcal G_N\).

### Proposition 3.5 (reflection orbits)

If \(N\) is odd, every reflection orbit has size two. If \(N\) is even, there is exactly one fixed point:

\[
(\nu(N/2),\nu(N/2)).
\]

## 4. Fiber measure and additive convolution

### Definition 4.1 (counting measure)

\[
\mu_N=\sum_{a=1}^{N-1}\delta_{(\nu(a),\nu(N-a))}.
\]

### Definition 4.2 (valuation lift)

For an arithmetic function \(f:\mathbb N\to\mathbb C\), define

\[
\widehat f(x)=f(\rho(x)).
\]

### Theorem 4.3 (fiber convolution identity)

For arithmetic functions \(f,g\),

\[
(f*_+g)(N)
=
\int_{\mathcal G_N}\widehat f(x)\widehat g(y)\,d\mu_N(x,y),
\]

where

\[
(f*_+g)(N)=\sum_{a=1}^{N-1}f(a)g(N-a).
\]

#### Proof

By the definition of \(\mu_N\),

\[
\int_{\mathcal G_N}\widehat f(x)\widehat g(y)\,d\mu_N
=
\sum_{a=1}^{N-1}f(\rho(\nu(a)))g(\rho(\nu(N-a))).
\]

Exact recovery gives the desired sum.

## 5. Prime and prime-power loci

### Definition 5.1 (prime vertices)

\[
\mathcal P_1=\{e_p:p\in\mathbb P\}.
\]

### Definition 5.2 (prime-power axis locus)

\[
\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}.
\]

### Proposition 5.3 (von Mangoldt support)

The lifted von Mangoldt function \(\widehat\Lambda\) is supported exactly on \(\mathcal A_1\), and

\[
\widehat\Lambda(k e_p)=\log p.
\]

### Proposition 5.4 (Goldbach intersection form)

For even \(N\ge4\), binary Goldbach is equivalent to

\[
\mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
\]

This is an exact reformulation, not a proof.

## 6. Fourier and residue observables

### Definition 6.1 (difference coordinate)

For the fiber point indexed by \(a\), define

\[
d_N(a)=a-(N-a)=2a-N.
\]

### Definition 6.2 (difference-phase transform)

For a fiber weight \(w=(w_a)_{1\le a\le N-1}\),

\[
\mathcal A_\alpha w(N)=\sum_{a=1}^{N-1}w_a e(\alpha(2a-N)).
\]

Unlike the symmetric product phase \(e(\alpha a)e(\alpha(N-a))=e(\alpha N)\), this phase is nonconstant along the fiber.

### Definition 6.3 (modular difference-channel operator)

For \(r\ge1\), define

\[
(D_{N,r}w)_d
=
\sum_{\substack{1\le a\le N-1\\2a-N\equiv d\pmod r}}w_a,
\qquad d\in\mathbb Z/r\mathbb Z.
\]

### Definition 6.4 (finite Fourier channels)

\[
\widehat D_{N,r}w(k)
=
\sum_{d\bmod r}e(kd/r)(D_{N,r}w)_d.
\]

## 7. Exact rank and reconstruction

### Theorem 7.1 (difference-channel rank formula)

For \(N\ge2\) and \(r\ge1\),

\[
\operatorname{rank}D_{N,r}
=
\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

#### Proof

Each column of the matrix of \(D_{N,r}\) is a standard basis vector indexed by

\[
2a-N\pmod r.
\]

Therefore the rank equals the number of distinct residues attained by \(2a-N\) for \(1\le a\le N-1\). The image of multiplication by \(2\) on \(\mathbb Z/r\mathbb Z\) has cardinality \(r/\gcd(2,r)\). A consecutive run of \(N-1\) values of \(a\) attains exactly the minimum of these two cardinalities.

### Corollary 7.2 (kernel dimension)

\[
\dim\ker D_{N,r}
=
N-1-\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

### Corollary 7.3 (complete reconstruction for odd large modulus)

If \(r\) is odd and \(r\ge N-1\), then \(D_{N,r}\) is injective and

\[
w_a=(D_{N,r}w)_{2a-N\bmod r}.
\]

### Corollary 7.4 (Fourier invariance of rank)

Because the discrete Fourier transform on \(\mathbb Z/r\mathbb Z\) is invertible,

\[
\operatorname{rank}(F_rD_{N,r})=
\operatorname{rank}D_{N,r}.
\]

### Corollary 7.5 (zero-frequency redundancy)

The additive total

\[
\sum_{a=1}^{N-1}w_a
\]

is the zero-frequency coefficient of the difference channels and does not increase rank when all channels are already included.

## 8. Restricted reconstruction

The exact large-modulus theorem shows that unrestricted reconstruction is elementary. The nontrivial theory begins when the observable family is constrained.

### Definition 8.1 (observable family)

An observable family \(\mathcal O\) is a finite collection of linear functionals on \(\mathbb C^{N-1}\). Let \(A_N(\mathcal O)\) denote the associated measurement matrix.

### Definition 8.2 (sufficiency)

\(\mathcal O\) is sufficient if

\[
\ker A_N(\mathcal O)=\{0\}.
\]

### Definition 8.3 (restricted reconstruction number)

For an allowed dictionary \(\mathfrak D_N\) of observables,

\[
m_{\mathfrak D}(N)
=
\min\{|\mathcal O|:\mathcal O\subseteq\mathfrak D_N,
\ \ker A_N(\mathcal O)=\{0\}\}.
\]

A dimension lower bound gives

\[
m_{\mathfrak D}(N)\ge N-1
\]

when each observable is scalar-valued and no structural restriction on \(w\) is assumed. Therefore sublinear recovery requires either vector-valued measurements, structural assumptions, or multiple samples.

### Definition 8.4 (stability constant)

For injective \(A\), define

\[
\kappa_2(A)=\frac1{\sigma_{\min}(A)}.
\]

Then noisy data \(Aw+\varepsilon\) satisfy the least-squares bound

\[
\|\widetilde w-w\|_2\le\kappa_2(A)\|\varepsilon\|_2.
\]

## 9. Open problems

### Open Problem 9.1 (small-modulus design)

Determine the minimum collection of small moduli whose combined difference channels are injective on \(\mathbb C^{N-1}\).

### Open Problem 9.2 (stable design)

Among injective observable families with a fixed measurement budget, minimize \(\kappa_2\).

### Open Problem 9.3 (symmetry-reduced reconstruction)

Determine exact rank and stability on the symmetric and antisymmetric subspaces under \(a\leftrightarrow N-a\).

### Open Problem 9.4 (structured weights)

Study reconstruction on sparse, prime-supported, prime-power-supported, nonnegative, or multiplicatively generated fiber weights.

### Open Problem 9.5 (uniform families)

Construct observable designs whose description is uniform in \(N\), and determine asymptotic rank and conditioning.

### Research Question 9.6 (natural inter-fiber maps)

Determine whether there are nontrivial maps between \(\mathcal G_N\) and \(\mathcal G_M\) that preserve a specified set of observables. No category-theoretic claim is made before such maps are defined and verified.

## 10. Relation to analytic number theory

The fiber convolution identity is exact. Circle-method, character, and residue observables are coordinate systems on weighted additive fibers. Their usefulness for asymptotic number theory depends on estimates not supplied by the finite geometric reformulation itself.

The framework therefore separates:

- exact recoding;
- exact finite-dimensional reconstruction;
- analytic estimates;
- open prime-producing problems.

## 11. Reproducibility

The rank theorem is independently checked by:

- `code/verify_pvg_fiber_reconstruction_rank.py`;
- `results/pvg_fiber_reconstruction_rank_verification_001.json`.

The computational verification supports the proof but is not a substitute for it.

## 12. Current research direction

The next theorem target is the exact rank of combined small-modulus channel systems, followed by singular-value bounds and optimal stable designs.
