# Focused Literature Review — Addition Fibers Theory v1

Status: scoped literature review under `THEORY-FREEZE-v1.0`.

Purpose: identify established antecedents for the ingredients of the current framework, distinguish standard components from project-specific packaging, and avoid unsupported priority claims.

## 1. Scope

The review was restricted to four components:

1. prime-exponent / valuation-vector encoding of positive integers;
2. additive representation fibers and additive convolution;
3. modular residue aggregation and Fourier channels;
4. reconstruction from grouped sums, including finite Radon transforms and discrete tomography.

This is a focused review, not an exhaustive bibliographic survey.

## 2. Prime-exponent vectors

The representation

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}
\]

is a direct expression of unique factorization. The multiplicative monoid of positive integers is identified with the free commutative monoid on the primes, and multiplication becomes coordinatewise addition of exponent vectors.

Closely related exponent-vector language is standard in:

- factorization theory of commutative monoids;
- monomial and semigroup algebras;
- integer-factorization algorithms such as sieve methods, where parity vectors of prime exponents are used for linear algebra.

Representative source:

- S. Tringali, *Factorization in monoids and rings*, arXiv:2005.01681.

Assessment: the valuation-vector encoding and exact recovery map are standard consequences of unique factorization. No originality claim should be attached to this component alone.

## 3. Additive representation fibers

For fixed \(N\), the set

\[
\mathcal F_N^+=\{(a,b)\in\mathbb N_{\ge1}^2:a+b=N\}
\]

is the fiber of the addition map. Counting weighted points in this fiber is exactly the additive convolution

\[
(f*_+g)(N)=\sum_{a=1}^{N-1}f(a)g(N-a).
\]

Representation functions of the form

\[
r_{A,B}(N)=\#\{(a,b)\in A\times B:a+b=N\}
\]

are standard in additive combinatorics and additive prime number theory. Goldbach representation functions are a central example.

Representative sources:

- T. T. Nguyen, *Goldbach Representations with several primes*, arXiv:2409.13368.
- J. Brüdern, J. Kaczorowski, A. Perelli, *Explicit formulae for averages of Goldbach representations*, arXiv:1712.00737.
- J. Pintz, *A new explicit formula in the additive theory of primes with applications I*, arXiv:1804.05561.

Assessment: the additive fiber and convolution identity are standard structures. The project-specific step is to transport the whole fiber through the injective prime-valuation map and then treat the transported object as the primary geometric carrier.

## 4. Residue aggregation and Fourier channels

The operator

\[
(D_{N,r}w)_d
=
\sum_{2a-N\equiv d\pmod r}w_a
\]

is an incidence / aggregation operator that groups coordinates according to a modular label. Its Fourier transform is a change of basis on the full residue-channel space. The use of complete residue data, discrete Fourier transforms, and Chinese-remainder reconstruction is standard in harmonic analysis on finite abelian groups and in modular reconstruction.

Representative sources:

- O. Knill, *A Multivariable Chinese Remainder Theorem*, arXiv:1206.5114.
- G. Guo and X.-G. Xia, *Robust Multidimensional Chinese Remainder Theorem with Non-Diagonal Moduli and Multi-Stage Framework*, arXiv:2604.00995.

Assessment: CRT equivalence of joint residue signatures and single residues modulo the least common multiple is standard. The exact rank formula in the present finite interval setting is elementary once the operator is written as an incidence matrix.

## 5. Reconstruction from grouped sums

The broader inverse problem of recovering a function from sums over structured subsets is classical in finite Radon transforms and discrete tomography. Noninjectivity is commonly described through kernel elements, switching functions, or invisible deformations.

Representative sources:

- J. Ilmavirta, *On Radon transforms on finite groups*, arXiv:1411.3829.
- M. Ceko, S. M. C. Pagani, R. Tijdeman, *Algorithms for linear time reconstruction by discrete tomography II*, arXiv:2010.07862.

Assessment: the reconstruction viewpoint, kernel analysis, and stability questions have clear precedents in inverse problems. The present project specializes these ideas to the one-dimensional index set of an addition fiber and to the modular difference label \(2a-N\).

## 6. What appears standard

The following components are established or immediate from established theory:

- prime-exponent vectors and exact recovery;
- additive representation functions and additive convolution;
- residue-class aggregation;
- Fourier equivalence of complete channel data;
- Chinese-remainder identification of compatible joint residues;
- rank as the number of distinct incidence columns;
- kernel interpretation as invisible redistributions within channels;
- reconstruction and conditioning questions for incidence operators.

## 7. What may be project-specific

The focused search did not identify a source presenting the following package in the same form:

1. the exact positive addition fiber transported into prime-valuation coordinates;
2. a named prime-valuation addition fiber \(\mathcal G_N\);
3. the counting measure on that transported fiber as the carrier of all additive convolutions;
4. modular difference-channel operators defined directly on fiber weights;
5. the combined rank, kernel, reconstruction, and conditioning program attached to this object;
6. Goldbach represented as intersection with the prime-point locus inside the same framework.

This is only a negative result from a limited search. It does **not** establish novelty or priority.

## 8. Priority classification

Current classification:

- **Known / standard:** valuation vectors, additive convolution, representation functions, CRT, finite Fourier transforms, incidence-matrix rank reasoning.
- **Exact reinterpretation:** transport of additive fibers and Goldbach representation sets into valuation coordinates.
- **Project-specific synthesis:** the unified addition-fiber object plus its reconstruction operators and governance structure.
- **Novelty status:** unresolved.

No claim of mathematical priority should be made until a broader search includes MathSciNet, zbMATH, Google Scholar citation chaining, monographs on additive combinatorics, discrete tomography, factorization theory, and finite harmonic analysis.

## 9. Safe wording for Paper 1

Recommended wording:

> Prime-exponent coordinates, additive representation functions, residue decompositions, and finite Fourier analysis are classical. The contribution of the present framework is their exact organization around the transported addition fiber and the associated finite reconstruction operators. We do not claim that every component is new, and a complete priority analysis remains open.

## 10. Freeze decision

The focused literature-review requirement is complete at the preliminary level.

Result:

```text
PRECISE PRECEDENT FOR FULL PACKAGE = NOT FOUND IN FOCUSED SEARCH
NOVELTY CLAIM = NOT AUTHORIZED
PRIORITY CLAIM = NOT AUTHORIZED
BROADER BIBLIOGRAPHIC REVIEW = REQUIRED BEFORE SUBMISSION
```

Scientific ceiling: this review does not strengthen any Goldbach estimate, establish a new theorem about primes, or claim progress on RH/GRH.