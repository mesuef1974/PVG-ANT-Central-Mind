# Canonical Definitions and Results — Theory Freeze v1.0

This document is the normalized mathematical core for Paper 1. It introduces no new research direction; it consolidates the accepted definitions, proved results, exact reformulations, and open problems already present in the repository.

## 1. Prime-valuation coordinates

### Definition 1.1 (prime-valuation vector)

For \(n\in\mathbb N_{\ge1}\), define

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}\in\mathbb N_0^{(\mathbb P)}.
\]

By convention, \(\nu(1)=0\).

### Definition 1.2 (recovery map)

For a finitely supported vector \(x=(x_p)_{p\in\mathbb P}\in\mathbb N_0^{(\mathbb P)}\), define

\[
\rho(x)=\prod_{p\in\mathbb P}p^{x_p}.
\]

### Proposition 1.3 (exact recovery)

For every \(n\ge1\),

\[
\rho(\nu(n))=n.
\]

Consequently, \(\nu\) is injective on positive integers.

#### Proof

This is the uniqueness part of the fundamental theorem of arithmetic.

## 2. Ordered addition fibers

### Definition 2.1 (positive ordered addition fiber)

For \(N\ge2\), define

\[
\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}.
\]

### Definition 2.2 (prime-valuation addition fiber)

Define

\[
\mathcal G_N
=(\nu\times\nu)(\mathcal F_N^+)
=\{(\nu(a),\nu(N-a)):1\le a\le N-1\}.
\]

Equivalently,

\[
\mathcal G_N
=\{(x,y)\in(\mathbb N_0^{(\mathbb P)})^2:\rho(x)+\rho(y)=N\}.
\]

### Theorem 2.3 (no-information-loss theorem)

The map

\[
\iota_N:\mathcal F_N^+\longrightarrow\mathcal G_N,
\qquad
(a,b)\longmapsto(\nu(a),\nu(b))
\]

is a bijection.

#### Proof

Surjectivity holds by Definition 2.2. If

\[
(\nu(a),\nu(b))=(\nu(c),\nu(d)),
\]

then Proposition 1.3 implies \(a=c\) and \(b=d\). Hence \(\iota_N\) is injective.

### Definition 2.4 (fiber reflection)

Define

\[
\sigma(x,y)=(y,x).
\]

### Proposition 2.5 (reflection structure)

The map \(\sigma\) preserves \(\mathcal G_N\) and satisfies \(\sigma^2=\mathrm{id}\). If \(N\) is odd, every orbit has size two. If \(N\) is even, the unique fixed point is

\[
(\nu(N/2),\nu(N/2)).
\]

#### Proof

Swapping \(a\) and \(N-a\) preserves their sum. A fixed point requires \(a=N-a\), hence \(a=N/2\), which exists exactly when \(N\) is even.

## 3. Fiber measure and additive convolution

### Definition 3.1 (fiber counting measure)

Define

\[
\mu_N
=\sum_{a=1}^{N-1}\delta_{(\nu(a),\nu(N-a))}.
\]

### Definition 3.2 (valuation lift)

For an arithmetic function \(f:\mathbb N\to\mathbb C\), define

\[
\widehat f(x)=f(\rho(x)).
\]

### Definition 3.3 (additive convolution)

For arithmetic functions \(f,g\), define

\[
(f*_+g)(N)=\sum_{a=1}^{N-1}f(a)g(N-a).
\]

### Theorem 3.4 (fiber convolution identity)

For every \(N\ge2\),

\[
(f*_+g)(N)
=\int_{\mathcal G_N}\widehat f(x)\widehat g(y)\,d\mu_N(x,y).
\]

#### Proof

By Definition 3.1, the right-hand side equals

\[
\sum_{a=1}^{N-1}f(\rho(\nu(a)))g(\rho(\nu(N-a))).
\]

Apply Proposition 1.3.

## 4. Prime and prime-power loci

### Definition 4.1 (prime point locus)

Define

\[
\mathcal P_1=\{e_p:p\in\mathbb P\}.
\]

### Definition 4.2 (prime-power axis locus)

Define

\[
\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}.
\]

### Proposition 4.3 (von Mangoldt support)

The lifted von Mangoldt function \(\widehat\Lambda\) is supported exactly on \(\mathcal A_1\), and

\[
\widehat\Lambda(k e_p)=\log p.
\]

#### Proof

The von Mangoldt function is nonzero exactly on prime powers \(p^k\), whose valuation vectors are \(k e_p\).

### Exact reformulation 4.4 (binary Goldbach)

For even \(N\ge4\), binary Goldbach for \(N\) is equivalent to

\[
\mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
\]

This is an exact reformulation, not a proof of Goldbach.

## 5. Difference channels

### Definition 5.1 (fiber weight space)

For fixed \(N\ge2\), define

\[
V_N=\mathbb C^{N-1},
\]

with coordinates indexed by \(a=1,\dots,N-1\). Write \(w=(w_a)_{a=1}^{N-1}\).

### Definition 5.2 (difference coordinate)

Define

\[
d_N(a)=a-(N-a)=2a-N.
\]

For a modulus \(r\ge1\), write

\[
d_{N,r}(a)=2a-N\pmod r.
\]

### Definition 5.3 (difference-channel operator)

Define

\[
D_{N,r}:V_N\to\mathbb C^r
\]

by

\[
(D_{N,r}w)_d
=\sum_{\substack{1\le a\le N-1\\2a-N\equiv d\pmod r}}w_a,
\qquad d\in\mathbb Z/r\mathbb Z.
\]

### Theorem 5.4 (single-modulus rank theorem)

For every \(N\ge2\) and \(r\ge1\),

\[
\operatorname{rank}D_{N,r}
=\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

#### Proof

The matrix of \(D_{N,r}\) has one nonzero entry in each column. Two columns indexed by \(a,b\) coincide exactly when

\[
2a-N\equiv2b-N\pmod r,
\]

or equivalently

\[
2(a-b)\equiv0\pmod r.
\]

Let \(g=\gcd(2,r)\). This is equivalent to

\[
a\equiv b\pmod{r/g}.
\]

Thus the rank equals the number of distinct residue classes modulo \(r/g\) met by the consecutive indices \(1,\dots,N-1\), namely

\[
\min(N-1,r/g).
\]

### Corollary 5.5 (kernel dimension)

\[
\dim\ker D_{N,r}
=N-1-\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

### Corollary 5.6 (exact injectivity criterion)

The operator \(D_{N,r}\) is injective if and only if

\[
\frac r{\gcd(2,r)}\ge N-1.
\]

When this condition holds,

\[
w_a=(D_{N,r}w)_{2a-N\pmod r}.
\]

In particular, every odd modulus \(r\ge N-1\) gives full reconstruction.

### Proposition 5.7 (zero-frequency identity)

For every \(w\in V_N\),

\[
\sum_{d\bmod r}(D_{N,r}w)_d
=\sum_{a=1}^{N-1}w_a.
\]

#### Proof

Every index \(a\in\{1,\dots,N-1\}\) belongs to exactly one residue channel.

### Proposition 5.8 (Fourier equivalence)

Let \(F_r\) be the full discrete Fourier transform on \(\mathbb Z/r\mathbb Z\). Then

\[
\operatorname{rank}(F_rD_{N,r})
=\operatorname{rank}D_{N,r}.
\]

#### Proof

The discrete Fourier matrix \(F_r\) is invertible.

## 6. Multiple moduli

### Definition 6.1 (joint-signature operator)

For a modulus family \(\mathbf r=(r_1,\dots,r_s)\), let

\[
\Sigma_{\mathbf r}
=\{(d_{N,r_1}(a),\dots,d_{N,r_s}(a)):1\le a\le N-1\}.
\]

Define

\[
J_{N;\mathbf r}:V_N\to\mathbb C^{\Sigma_{\mathbf r}}
\]

by

\[
(J_{N;\mathbf r}w)_\eta
=\sum_{\substack{1\le a\le N-1\\(d_{N,r_1}(a),\dots,d_{N,r_s}(a))=\eta}}w_a,
\qquad \eta\in\Sigma_{\mathbf r}.
\]

Let

\[
L=\operatorname{lcm}(r_1,\dots,r_s).
\]

### Theorem 6.2 (joint-modulus rank theorem)

\[
\operatorname{rank}J_{N;\mathbf r}
=\min\!\left(N-1,\frac L{\gcd(2,L)}\right).
\]

#### Proof

Two indices \(a,b\) have the same joint signature exactly when

\[
2(a-b)\equiv0\pmod{r_j}
\]

for every \(j\), equivalently when

\[
2(a-b)\equiv0\pmod L.
\]

Apply Theorem 5.4 with modulus \(L\).

### Corollary 6.3 (joint reconstruction criterion)

The operator \(J_{N;\mathbf r}\) is injective if and only if

\[
\frac L{\gcd(2,L)}\ge N-1.
\]

### Proposition 6.4 (conditioning in the injective case)

After ordering the rows of \(\mathbb C^{\Sigma_{\mathbf r}}\) by the unique indices they represent, an injective joint-signature matrix is a permutation matrix. Hence all its singular values are \(1\) and

\[
\kappa_2(J_{N;\mathbf r})=1.
\]

### Definition 6.5 (marginal stacked operator)

Define

\[
M_{N;\mathbf r}
=\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_s}
\end{pmatrix}.
\]

The operator \(M_{N;\mathbf r}\) must not be identified with \(J_{N;\mathbf r}\): it records separate marginals but not the cross-modulus coupling.

## 7. Difference phases

### Definition 7.1 (difference-phase transform)

Using \(e(t)=e^{2\pi i t}\), define

\[
\mathcal A_\alpha w(N)
=\sum_{a=1}^{N-1}w_a e(\alpha(2a-N)).
\]

### Proposition 7.2 (symmetric-phase correction and constancy criterion)

On a fixed fiber,

\[
e(\alpha a)e(\alpha(N-a))=e(\alpha N)
\]

is constant. Thus the symmetric product phase cannot produce a nontrivial spectral observable on a fixed exact fiber.

If \(N=2\), the fiber has a single index and the difference phase is constant for every \(\alpha\). If \(N\ge3\), the difference phase \(a\mapsto e(\alpha(2a-N))\) is constant on all indices \(a=1,\dots,N-1\) if and only if \(2\alpha\in\mathbb Z\).

#### Proof

For \(N=2\), there is only the index \(a=1\). For \(N\ge3\), at least two consecutive indices occur, and the ratio of consecutive phase values is \(e(2\alpha)\). Hence all values are equal exactly when \(e(2\alpha)=1\), equivalently \(2\alpha\in\mathbb Z\).

## 8. Approved open problems and deferred observations

### Open Problem 8.1 (marginal rank)

Determine the exact rank, kernel, and singular spectrum of \(M_{N;\mathbf r}\).

### Open Problem 8.2 (natural kernel basis)

For restricted measurement families, determine whether their kernels admit canonical generators with a direct fiber-geometric interpretation.

### Open Problem 8.3 (restricted stable reconstruction)

Under an explicit structured class of weights or a fixed observable budget, determine optimal injectivity and stability bounds.

### Open Problem 8.4 (literature priority)

Determine precisely which components of this combined addition-fiber and reconstruction framework have precedents in the literature.

### Deferred Observation 8.5 (Dirichlet-character rows)

The claim that Dirichlet-character rows are information-redundant relative to complete difference-channel data is not part of the proved core in this version. It requires an explicit operator definition and proof and remains deferred during `THEORY-FREEZE-v1.0`.

## 9. Frozen items

No further definitions, conjectures, dynamics, categories, network structures, nonlinear manifolds, or new Goldbach claims enter this document during `THEORY-FREEZE-v1.0`.