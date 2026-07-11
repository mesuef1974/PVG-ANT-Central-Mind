# BRIDGE-LOG-HALFSPACE-LATTICE-SUM-001

**Family:** logarithmic half-spaces / weighted sums  
**Maturity:** L1 exact translation  
**Classification:** Exact identity with order-loss warning

## Classical object

Size restrictions `n≤x`, intervals, and weighted arithmetic sums.

## PVG object

The logarithmic functional

\[
\ell(\alpha)=\sum_p\alpha_p\log p
\]

and weighted lattice half-spaces or slabs.

## Exact forward map

\[
\ell(\nu(n))=\log n,
\qquad
n\leq x\iff \ell(\nu(n))\leq\log x.
\]

A short interval maps to a thin slab between two logarithmic levels.

## Reverse map and information loss

For a full labeled point the map is lossless. A coarse slab or projected statistic does not preserve successor order, additive spacing, phase, or local correlations. Calling a slab “local” does not solve a short-interval problem.

## Analytic transform

Arithmetic sums become weighted lattice sums. Estimating them still requires counting, Dirichlet-series, sieve, harmonic-analysis, or probabilistic input.

## Simplification gain

**Expository:** the size constraint becomes geometric, but no analytic estimate is gained automatically.

## Finite certificate

`EX-HALFSPACE-001`: for integers through `19`, the weighted valuation sum equals `log n`, and membership in `n≤12` agrees with the half-space test.

## Research use

A routing bridge for summatory problems. It must always carry the order-loss warning when used for short intervals or gaps.
