# PVG Core Grammar v1

## 1. Ambient object

Every positive integer is represented by its finitely supported labeled valuation vector

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}\in\mathbb N^{(\mathbb P)}.
\]

The prime labels are part of the object. Forgetting them is a nontrivial quotient, not a harmless notation change.

## 2. Six data layers

### Labeled exact layer

- full valuation vector;
- labeled height profile;
- labeled divisor box;
- fully labeled factorization decompositions.

These can reconstruct \(n\) exactly.

### Labeled structural layer

- support;
- radical;
- labeled face incidence;
- truncated labeled profiles.

These retain arithmetic labels but erase some heights or depths.

### Unlabeled shape layer

- exponent multiset;
- box side-length multiset;
- boundary-coordinate counts;
- factorization type.

These retain shape while erasing which primes realize it.

### Scalar observable layer

- \(\omega(n)\);
- \(\Omega(n)\);
- \(\tau(n)\);
- \(I_r(n)\);
- logarithmic or weighted linear functionals.

A scalar can be analytically powerful while being geometrically noninjective.

### Population pushforward layer

- residue-fiber masses;
- divisibility aggregates \(A_d\);
- second moments;
- sieve remainders.

These describe a collection rather than an individual vector.

### Analytic certificate layer

- Bell-series identities;
- Euler products;
- continuation regions;
- pole and residue data;
- error terms and uniformity.

This layer is not contained automatically in the geometry. It requires independent analysis.

## 3. Reconstruction lattice

The following implications are exact when the stated labels are retained:

```text
full labeled valuation vector
  <-> labeled height profile
  <-> labeled divisor box with upper corner
  -> labeled support
  <-> radical
  -> support size omega

full labeled valuation vector
  -> unlabeled exponent multiset
  -> symmetric exponent statistics

full labeled valuation vector
  -> total height Omega

full labeled valuation vector
  -> log mass log n
  -> n
  -> full labeled valuation vector
```

The log-mass arrow is injective on genuine integer valuation vectors because of unique factorization. It is not a geometric isometry and does not preserve additive neighborhoods.

## 4. Non-reconstruction laws

The mind must reject the following inverse claims unless extra data are supplied:

1. \(\omega(n)\) does not recover the support.
2. \(\Omega(n)\) does not recover the exponent multiset.
3. \(\tau(n)\) does not recover the divisor-box shape.
4. an unlabeled exponent multiset does not recover residues modulo \(q\).
5. one character value \(\chi(n)\) does not recover the residue class or vector.
6. a character second moment does not recover phases or individual discrepancies.
7. aggregate sieve data \(A_d\) do not recover pointwise profiles in general.
8. a continuation half-plane does not uniquely recover the first local residual degree.
9. a pole does not uniquely recover the geometric observable that generated it.
10. an asymptotic formula does not establish that PVG was materially necessary.

## 5. Composition discipline

A valid composite translation records every intermediate loss:

```text
PVG object
-> geometric projection
-> arithmetic observable
-> local prime-power data
-> Bell series
-> Euler/L-factor model
-> analytic transfer theorem
-> asymptotic certificate
```

At each arrow, the mind records:

- injectivity;
- preserved information;
- lost information;
- hypotheses;
- compatible tools;
- missing certificate;
- counterexample to an invalid reverse step.

## 6. ANT interface table

| PVG structure | Exact ANT interface | Missing analytic work |
|---|---|---|
| vector addition | multiplication | none for the identity |
| coordinate order | divisibility | none for the identity |
| divisor box | divisors and convolution | estimates for weighted regions |
| local axis germ | Bell series | convergence and global assembly |
| residue projection | characters | bounds for twisted sums |
| truncation | sieve visibility | sequence-specific remainder control |
| two-block decomposition | Type I/II | bilinear cancellation |
| scalar additive functional | additive-function theory | moments, tails, limit transfer |
| character phase | Dirichlet L-functions or pretentious distance | conductor, vertical, and phase estimates |
| log half-space | size cutoff | Mellin/Perron/Tauberian certificates |

## 7. Materiality gate

PVG is materially useful only if removing it loses at least one of:

- a natural observable;
- a simplification;
- a reusable factorization;
- a correct tool-routing decision;
- a previously hidden information-loss obstruction;
- a provable statement or sharper certificate.

If removal changes only terminology or visualization, classify the contribution as reinterpretation.

## 8. Scientific ceiling

This grammar is a reasoning and translation infrastructure. It creates no theorem, no analytic estimate, no publication claim, and no RH/GRH progress.