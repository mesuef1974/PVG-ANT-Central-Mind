# Prime-Valuation Addition Fibers: Exact Translation and Reconstruction

## Status

Integrated Paper 1 draft under `THEORY-FREEZE-v1.0`.

## Scientific classification

- Definitions are explicitly marked.
- General identities and rank statements are proved.
- Finite computations are used only as verification and exposition.
- Binary Goldbach appears only as an exact reformulation.
- No literature-priority claim is made.
- No Goldbach proof, new major/minor-arc estimate, or RH/GRH progress is claimed.

## Abstract

For an integer \(N\ge2\), define the ordered positive addition fiber

\[
\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}
\]

and its image in prime-valuation coordinates

\[
\mathcal G_N=(\nu\times\nu)(\mathcal F_N^+).
\]

Because the prime-valuation map is injective on positive integers, this passage loses no information. We develop the counting measure on \(\mathcal G_N\), prove an exact fiber form of additive convolution, identify the prime and prime-power loci, and define modular difference-channel operators on fiber weights. For a modulus \(r\), we prove

\[
\operatorname{rank}D_{N,r}
=
\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

For a family of moduli with least common multiple \(L\), the corresponding joint-signature operator has rank

\[
\operatorname{rank}J_{N;\mathbf r}
=
\min\!\left(N-1,\frac L{\gcd(2,L)}\right).
\]

When this joint operator is injective, its nonzero singular values are all \(1\). The paper separates exact recoding, exact finite-dimensional reconstruction, analytic estimates, and open prime-producing questions.

## 1. Introduction

Prime-valuation coordinates linearize multiplication:

\[
\nu(ab)=\nu(a)+\nu(b).
\]

Addition is not linear in these coordinates. For fixed \(N\), the relation \(a+b=N\) instead defines a finite nonlinear fiber. The purpose of this paper is to isolate that fiber, translate additive convolutions exactly into valuation coordinates, and study what can be reconstructed from modular difference measurements.

The framework has three layers:

1. exact finite geometry of addition fibers;
2. exact translation of additive convolution into weighted fiber sums;
3. rank, kernel, and conditioning of residue-channel operators.

Goldbach is used only to illustrate the prime-point locus. Analytic estimates required by the circle method or sieve methods remain external to the finite geometric identities proved here.

## 2. Prime-valuation coordinates

### Definition 2.1 (prime-valuation vector)

For \(n\in\mathbb N_{\ge1}\), define

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}
\in\mathbb N_0^{(\mathbb P)}.
\]

By convention, \(\nu(1)=0\).

### Definition 2.2 (recovery map)

For finitely supported \(x=(x_p)_{p\in\mathbb P}\), define

\[
\rho(x)=\prod_{p\in\mathbb P}p^{x_p}.
\]

### Proposition 2.3 (exact recovery)

For every \(n\ge1\),

\[
\rho(\nu(n))=n.
\]

Consequently, \(\nu\) is injective on positive integers.

#### Proof

This is the uniqueness statement in the fundamental theorem of arithmetic.

## 3. Ordered addition fibers

### Definition 3.1 (positive ordered addition fiber)

For \(N\ge2\), define

\[
\mathcal F_N^+
=
\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}.
\]

### Definition 3.2 (prime-valuation addition fiber)

Define

\[
\mathcal G_N
=
(\nu\times\nu)(\mathcal F_N^+)
=
\{(\nu(a),\nu(N-a)):1\le a\le N-1\}.
\]

Equivalently,

\[
\mathcal G_N
=
\{(x,y):\rho(x)+\rho(y)=N\}.
\]

### Theorem 3.3 (no-information-loss theorem)

The map

\[
\iota_N:\mathcal F_N^+\longrightarrow\mathcal G_N,
\qquad
(a,b)\longmapsto(\nu(a),\nu(b))
\]

is a bijection.

#### Proof

Surjectivity holds by definition. If

\[
(\nu(a),\nu(b))=(\nu(c),\nu(d)),
\]

then Proposition 2.3 gives \(a=c\) and \(b=d\).

### Definition 3.4 (fiber reflection)

Define

\[
\sigma(x,y)=(y,x).
\]

### Proposition 3.5 (reflection structure)

The map \(\sigma\) preserves \(\mathcal G_N\) and satisfies \(\sigma^2=\mathrm{id}\). If \(N\) is odd, all reflection orbits have size two. If \(N\) is even, the unique fixed point is

\[
(\nu(N/2),\nu(N/2)).
\]

#### Proof

Swapping \(a\) and \(N-a\) preserves the equation \(a+(N-a)=N\). A fixed point requires \(a=N-a\).

## 4. Fiber measure and additive convolution

### Definition 4.1 (fiber counting measure)

Define

\[
\mu_N
=
\sum_{a=1}^{N-1}
\delta_{(\nu(a),\nu(N-a))}.
\]

### Definition 4.2 (valuation lift)

For an arithmetic function \(f:\mathbb N\to\mathbb C\), define

\[
\widehat f(x)=f(\rho(x)).
\]

### Definition 4.3 (additive convolution)

For arithmetic functions \(f,g\), define

\[
(f*_+g)(N)
=
\sum_{a=1}^{N-1}f(a)g(N-a).
\]

### Theorem 4.4 (fiber convolution identity)

For every \(N\ge2\),

\[
(f*_+g)(N)
=
\int_{\mathcal G_N}
\widehat f(x)\widehat g(y)\,d\mu_N(x,y).
\]

#### Proof

By Definition 4.1, the right-hand side is

\[
\sum_{a=1}^{N-1}
 f(\rho(\nu(a)))g(\rho(\nu(N-a))).
\]

Apply Proposition 2.3.

## 5. Prime and prime-power loci

### Definition 5.1 (prime-point locus)

Define

\[
\mathcal P_1=\{e_p:p\in\mathbb P\}.
\]

### Definition 5.2 (prime-power axis locus)

Define

\[
\mathcal A_1=\{k e_p:p\in\mathbb P,\ k\ge1\}.
\]

### Proposition 5.3 (von Mangoldt support)

The lifted von Mangoldt function \(\widehat\Lambda\) is supported exactly on \(\mathcal A_1\), and

\[
\widehat\Lambda(k e_p)=\log p.
\]

### Exact reformulation 5.4 (binary Goldbach)

For even \(N\ge4\), binary Goldbach for \(N\) is equivalent to

\[
\mathcal G_N\cap(\mathcal P_1\times\mathcal P_1)
e\varnothing.
\]

This is an exact reformulation, not a proof.

## 6. Difference channels

### Definition 6.1 (fiber weight space)

For fixed \(N\ge2\), let

\[
V_N=\mathbb C^{N-1},
\]

with coordinates \(w=(w_a)_{1\le a\le N-1}\).

### Definition 6.2 (difference coordinate)

Define

\[
d_N(a)=a-(N-a)=2a-N.
\]

For a modulus \(r\ge1\), write

\[
d_{N,r}(a)=2a-N\pmod r.
\]

### Definition 6.3 (difference-channel operator)

Define

\[
D_{N,r}:V_N\to\mathbb C^r
\]

by

\[
(D_{N,r}w)_d
=
\sum_{\substack{1\le a\le N-1\\2a-N\equiv d\pmod r}}w_a,
\qquad d\in\mathbb Z/r\mathbb Z.
\]

### Theorem 6.4 (single-modulus rank theorem)

For every \(N\ge2\) and \(r\ge1\),

\[
\operatorname{rank}D_{N,r}
=
\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

#### Proof

Each column of the matrix of \(D_{N,r}\) is a standard basis vector indexed by \(2a-N\pmod r\). Two columns indexed by \(a,b\) coincide exactly when

\[
2(a-b)\equiv0\pmod r.
\]

Let \(g=\gcd(2,r)\). This is equivalent to

\[
a\equiv b\pmod{r/g}.
\]

The consecutive indices \(1,\ldots,N-1\) therefore meet exactly

\[
\min(N-1,r/g)
\]

distinct channel classes.

### Corollary 6.5 (kernel dimension)

\[
\dim\ker D_{N,r}
=
N-1-
\min\!\left(N-1,\frac r{\gcd(2,r)}\right).
\]

### Corollary 6.6 (exact injectivity criterion)

\[
D_{N,r}\text{ is injective}
\iff
\frac r{\gcd(2,r)}\ge N-1.
\]

Whenever this holds,

\[
w_a=(D_{N,r}w)_{2a-N\pmod r}.
\]

### Proposition 6.7 (Fourier equivalence)

Let \(F_r\) be the full discrete Fourier transform on \(\mathbb Z/r\mathbb Z\). Then

\[
\operatorname{rank}(F_rD_{N,r})
=
\operatorname{rank}D_{N,r}.
\]

#### Proof

The Fourier matrix \(F_r\) is invertible.

### Proposition 6.8 (zero-frequency identity)

\[
\sum_{d\bmod r}(D_{N,r}w)_d
=
\sum_{a=1}^{N-1}w_a.
\]

Thus the ordinary total is the zero Fourier coordinate of the complete channel vector.

## 7. Joint modulus signatures

### Definition 7.1 (realized joint-signature set)

For a modulus family \(\mathbf r=(r_1,\ldots,r_s)\), define

\[
\Sigma_{\mathbf r}
=
\{(d\bmod r_1,\ldots,d\bmod r_s):d\in\mathbb Z\}.
\]

### Definition 7.2 (joint-signature operator)

Define

\[
J_{N;\mathbf r}:V_N\to\mathbb C^{\Sigma_{\mathbf r}}
\]

by

\[
(J_{N;\mathbf r}w)_{\boldsymbol\delta}
=
\sum_{\substack{1\le a\le N-1\\
(d_{N,r_1}(a),\ldots,d_{N,r_s}(a))=\boldsymbol\delta}}w_a.
\]

Let

\[
L=\operatorname{lcm}(r_1,\ldots,r_s).
\]

### Theorem 7.3 (joint-modulus rank theorem)

\[
\operatorname{rank}J_{N;\mathbf r}
=
\min\!\left(N-1,\frac L{\gcd(2,L)}\right).
\]

#### Proof

Two integers have the same compatible residue tuple modulo \(r_1,\ldots,r_s\) exactly when they are congruent modulo \(L\). Hence two columns indexed by \(a,b\) coincide exactly when

\[
2(a-b)\equiv0\pmod L.
\]

Apply the argument of Theorem 6.4 with modulus \(L\).

### Corollary 7.4 (joint reconstruction criterion)

\[
J_{N;\mathbf r}\text{ is injective}
\iff
\frac L{\gcd(2,L)}\ge N-1.
\]

### Proposition 7.5 (conditioning in the injective case)

If \(J_{N;\mathbf r}\) is injective, then after deleting zero rows and reordering the remaining rows, its matrix is the identity. Hence all singular values are \(1\) and

\[
\kappa_2(J_{N;\mathbf r})=1.
\]

### Definition 7.6 (marginal stacked operator)

Define

\[
M_{N;\mathbf r}
=
\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_s}
\end{pmatrix}.
\]

The marginal operator \(M_{N;\mathbf r}\) must not be identified with \(J_{N;\mathbf r}\): the former stores separate residue marginals, while the latter stores their coupling.

## 8. Difference phases

### Definition 8.1 (difference-phase transform)

Using \(e(t)=e^{2\pi i t}\), define

\[
\mathcal A_\alpha w(N)
=
\sum_{a=1}^{N-1}w_a e(\alpha(2a-N)).
\]

### Proposition 8.2 (phase constancy criterion)

The map

\[
a\longmapsto e(\alpha(2a-N))
\]

is constant on the full fiber if and only if

\[
2\alpha\in\mathbb Z.
\]

Also,

\[
e(\alpha a)e(\alpha(N-a))=e(\alpha N)
\]

is always constant on a fixed addition fiber. Thus the symmetric product phase carries no within-fiber variation.

## 9. Worked evidence

Four complete hand-checkable examples are supplied for

\[
N=10,12,24,30.
\]

They verify exact recovery, reflection structure, fiber convolution, prime-locus intersections, injective and noninjective difference channels, explicit reconstruction, and explicit kernel bases.

A dedicated joint-modulus example uses

\[
N=10,\qquad \mathbf r=(3,5),\qquad L=15.
\]

Neither \(D_{10,3}\) nor \(D_{10,5}\) is injective, but

\[
\operatorname{rank}J_{10;(3,5)}=9,
\]

and the injective joint matrix has condition number \(1\).

## 10. Computational verification

The verifier

`research/avrg-axis-sum/code/verify_pvg_fiber_reconstruction_rank.py`

checks the single-modulus rank formula for

\[
2\le N\le100,\qquad1\le r\le100.
\]

Across 9,900 parameter pairs, it reports zero rank mismatches, verifies that the ordinary sum row does not increase the complete channel rank, and checks explicit recovery for every tested odd \(r\ge N-1\). This finite verification supports the proof but does not replace it.

## 11. Relation to analytic number theory

The fiber-convolution identity is exact. Circle-method, residue, and character decompositions may be interpreted as coordinate systems on weighted additive fibers. Their asymptotic usefulness depends on analytic estimates not supplied by the finite recoding itself.

The framework therefore separates:

- exact recoding;
- exact finite-dimensional reconstruction;
- analytic estimates;
- open prime-producing problems.

The Goldbach intersection statement does not improve any known estimate and does not prove Goldbach.

## 12. Literature position

The ingredients of the framework have established precedents when considered separately:

- unique factorization and valuation vectors;
- additive representation functions and convolutions;
- residue-class aggregation and finite Fourier transforms;
- Chinese-remainder coupling;
- rank and kernel analysis of finite incidence transforms.

A focused preliminary review did not identify a source presenting the complete package in the same prime-valuation addition-fiber form. This absence is not evidence of novelty. No novelty or priority claim is authorized without a deeper bibliographic review.

## 13. Open problems

1. Determine the exact rank, kernel, and singular spectrum of the marginal stacked operator \(M_{N;\mathbf r}\).
2. Find natural geometric generators for kernels of restricted measurement families.
3. Study stable reconstruction under explicit structured classes of weights or fixed measurement budgets.
4. Complete a deeper literature-priority investigation before any novelty claim.

## 14. Reproducibility and companion files

Canonical theory and audits:

- `research/avrg-axis-sum/theory/CANONICAL-DEFINITIONS-AND-RESULTS-v1.md`;
- `research/avrg-axis-sum/governance/PROOF-AUDIT-v1.md`;
- `research/avrg-axis-sum/governance/DEPENDENCY-AND-NUMBERING-AUDIT-v1.md`;
- `research/avrg-axis-sum/governance/THEOREM-EVIDENCE-CROSSLINKS-v1.md`.

Manual examples:

- `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N10.md`;
- `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N12.md`;
- `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N24.md`;
- `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N30.md`;
- `research/avrg-axis-sum/examples/JOINT-MODULUS-WORKED-EXAMPLE-N10-R3-R5.md`.

Literature review:

- `research/avrg-axis-sum/literature/FOCUSED-LITERATURE-REVIEW-v1.md`.

## 15. Scientific ceiling

This paper establishes an exact finite framework and rank/reconstruction theorems for explicitly defined channel operators. It does not prove Goldbach, improve circle-method or sieve estimates, establish a literature-priority claim, or constitute progress on RH/GRH.
