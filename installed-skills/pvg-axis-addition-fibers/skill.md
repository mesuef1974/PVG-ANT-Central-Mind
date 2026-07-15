# PVG Axis Addition and Addition-Fiber Reasoning

Status: installed specialist capability

## Mission

Make the Central Mind competent in the full axis-addition research program developed in `research/avrg-axis-sum/`, including exact addition fibers, valuation transport, weighted additive observables, modular difference channels, Fourier reduction, reconstruction, certificate optimization, and scientific boundaries.

## Core distinction

Prime-valuation coordinates linearize multiplication:

\[
\nu(xy)=\nu(x)+\nu(y).
\]

They do not linearize ordinary addition. The correct carrier for `x+y=N` is the exact ordered addition fiber

\[
\mathcal F_N=\{(x,y)\in\mathbb N_{\ge1}^2:x+y=N\},
\]

or its valuation transport

\[
\mathcal G_N=\{(\nu(x),\nu(y)):x+y=N\}.
\]

Never infer `\nu(x+y)` from `\nu(x),\nu(y)` by coordinatewise addition.

## Required working knowledge

The skill must reason fluently with:

1. ordered and unordered addition fibers;
2. additive representation functions and convolution;
3. prime and prime-power loci inside valuation space;
4. von Mangoldt fiber weights `\Lambda(a)\Lambda(N-a)`;
5. modular difference labels `2a-N mod r`;
6. effective period `q(r)=r/gcd(2,r)`;
7. residue-channel operator
   \[
   (D_{N,r}w)_d=\sum_{2a-N\equiv d\pmod r}w_a;
   \]
8. finite Fourier transform of the channel vector;
9. exact rank, kernel, reconstruction, marginal-versus-joint information, and conditioning;
10. frequency-retention certification and the Certificate Optimization Framework;
11. dominance, precedence, mandatory closures, target compatibility, and minimal forbidden hyperedges;
12. the separation of abstract COF, Fourier realization, arithmetic input, and computational evidence.

## Canonical examples

The mind must be able to reconstruct and explain at least:

- `5=1+4=2+3=3+2=4+1`;
- `10=3+7=5+5=7+3`;
- `24=5+19=7+17=11+13`;
- `30=7+23=11+19=13+17`.

For every example it must distinguish the integer pair, its valuation pair, the fiber weight, residue channel, and any Fourier observable.

## Mandatory reasoning protocol

For every axis-addition question:

1. identify the ambient domain and whether order matters;
2. define the exact fiber before introducing geometry;
3. transport through `\nu` only after the integer relation is fixed;
4. state the chosen weight and observable;
5. identify whether the claim is an identity, reinterpretation, diagnostic, finite verification, theorem, boundary, or open problem;
6. distinguish complete channel information from marginal information;
7. check rank or kernel before claiming reconstruction;
8. separate finite computation from asymptotic number theory;
9. state the missing analytic certificate before discussing Goldbach consequences.

## Important correction

On a fixed fiber `x+y=N`, the symmetric product phase is constant:

\[
e(\alpha x)e(\alpha y)=e(\alpha N).
\]

Therefore it is not a nontrivial spectral discriminator. Use difference phases, asymmetric phases, or an ambient-pair projection when nonconstant spectral information is required.

## Scientific ceiling

This capability may express Goldbach as a prime-locus intersection or as positivity of a weighted representation function. It must not claim:

- a proof of Goldbach;
- a new major/minor arc estimate without proof;
- asymptotic reconstruction from finite experiments;
- RH or GRH progress;
- historical novelty for COF or the full addition-fiber package before the external literature audit is complete.

## Source map

Primary source tree: `research/avrg-axis-sum/`

COF source tree: `research/certificate-optimization-framework/`

Current integration branch: `agent/pvg-addition-fibers-theory-001`
