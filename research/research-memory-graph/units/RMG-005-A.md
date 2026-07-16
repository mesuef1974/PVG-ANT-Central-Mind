# RMG-005-A — Additive Characters, Exponential Sums, Finite Fourier Transform, and Cancellation Certificates

**Status:** COMPLETED  
**Branch:** `agent/pvg-axis-sum-continuation-002`  
**Verification:** PASS 9/9

## Purpose

Extend the Research Memory Graph from multiplicative residue phases to the additive harmonic layer used by exponential sums, circle-method projectors, and addition fibers. This unit preserves the distinction between exact finite Fourier identities and genuine analytic cancellation estimates.

## Core objects

For modulus `q`, define

\[
e_q(an)=\exp\!\left(\frac{2\pi ian}{q}\right).
\]

These are additive characters:

\[
e_q(a(n+m))=e_q(an)e_q(am).
\]

They must not be confused with Dirichlet characters, which are multiplicative on reduced residue classes.

## Finite orthogonality

\[
\sum_{a\bmod q}e_q(a(n-m))=
\begin{cases}
q,&n\equiv m\pmod q,\\
0,&n\not\equiv m\pmod q.
\end{cases}
\]

This is an exact finite identity. It isolates congruence constraints but does not estimate incomplete exponential sums.

## Finite Fourier transform

For residue-channel data `f(r)`,

\[
\widehat f(a)=\sum_{r\bmod q}f(r)e_q(-ar),
\]

with inversion

\[
f(r)=\frac1q\sum_{a\bmod q}\widehat f(a)e_q(ar).
\]

Under the unnormalized convention,

\[
\sum_{a\bmod q}|\widehat f(a)|^2
=q\sum_{r\bmod q}|f(r)|^2.
\]

## Addition-fiber projector

The congruence constraint `x+y=N mod q` is represented exactly by

\[
\mathbf 1_{x+y\equiv N\, (q)}
=\frac1q\sum_{a\bmod q}e_q(a(x+y-N)).
\]

This is the finite harmonic interface for Addition Fibers. It decomposes a constraint into modes; it does not prove positivity of a prime-weighted representation count.

## ANT to PVG translation

For `v=nu(n)`, decode `v` to `n` and attach the additive phase

\[
v\longmapsto e(\alpha\,\operatorname{decode}(v)).
\]

Thus

\[
\sum_n a_ne(\alpha n)
=\sum_v A(v)e(\alpha\operatorname{decode}(v))
\]

is an exact reindexing whenever the coefficient assignment is transferred faithfully.

### What is preserved

- coefficients and signs;
- decoded integer values;
- residue classes;
- additive phases;
- finite Fourier inversion;
- exact congruence projectors.

### What is not created

- cancellation beyond the trivial bound;
- Weyl, van der Corput, or large-sieve estimates;
- major/minor arc bounds;
- prime-weighted asymptotics;
- Goldbach positivity.

## Cancellation certificate discipline

For

\[
S(\alpha)=\sum_{n\in I}a_ne(\alpha n),
\]

the trivial certificate is

\[
|S(\alpha)|\le \sum_{n\in I}|a_n|.
\]

A nontrivial cancellation claim must specify:

- coefficient family;
- interval or shape;
- frequency range;
- modulus or denominator restrictions;
- hypotheses;
- constants and uniformity;
- proof mechanism.

Observed smallness on one finite sample is not a uniform theorem.

## Numerical verification

The executable harness checks:

1. registry count and unique identifiers;
2. additive orthogonality modulo `7`;
3. Fourier inversion;
4. Parseval's identity;
5. the addition-fiber projector;
6. ANT/PVG additive-phase reindexing for `1 <= n <= 300`;
7. the distinction between complete-period cancellation and the trivial `l1` bound;
8. presence of claim-rejection records.

Recorded values include:

```text
orthogonality max gap          = 5.305963053683338e-15
Fourier inversion max gap      = 3.3051285367689413e-15
Parseval lhs                   = 244.99999999999997
Parseval rhs                   = 245
fiber projector max gap        = 1.354085741216204e-15
complete-period sum magnitude  = 5.551115123125783e-16
trivial l1 bound example       = 100
```

## Claim rejections

Rejected:

```text
finite orthogonality
=> nontrivial incomplete-sum cancellation
```

Rejected:

```text
exact Fourier projector for x+y=N
=> Goldbach theorem
```

Rejected:

```text
exact PVG additive-phase encoding
=> major/minor arc estimates
```

## Assimilation state

```text
additive-character definition              = L4_NUMERICALLY_VERIFIED
finite orthogonality                        = L5_COMPUTATIONALLY_REGRESSION_TESTED
finite Fourier inversion and Parseval       = L5_COMPUTATIONALLY_REGRESSION_TESTED
addition-fiber projector                    = L5_COMPUTATIONALLY_REGRESSION_TESTED
PVG additive-phase reindexing               = L4_NUMERICALLY_VERIFIED
cancellation-certificate discipline         = L3_BIDIRECTIONALLY_ANALYZED
nontrivial exponential-sum theory           = not assimilated here
Lean proof added                            = none
L6 promotion                                = not authorized
Goldbach progress                           = none
```

## Provenance and reuse

This unit integrates with:

- Addition Fibers and Difference Channels;
- existing finite Fourier/rank/kernel diagnostics;
- character-residue registries from `RMG-003-*`;
- large-sieve and average-distribution boundaries from `RMG-004-D`;
- Montgomery additive-prime and circle-method ledgers.

It creates no parallel ontology.

## Next unit

`RMG-005-B — Circle Method, Major/Minor Arcs, Singular Series, and Certificate-Separation Graph`.
