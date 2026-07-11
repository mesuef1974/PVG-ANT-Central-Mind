# BRIDGE-DIVISOR-BOX-CONVOLUTION-001

**Family:** divisor boxes / convolution  
**Maturity:** L2 structural  
**Classification:** Known exact identity / structural bridge

## Classical object

The divisor set of `n`, divisor-count functions, and Dirichlet convolution.

## PVG object

The integer box

\[
[0,\nu(n)]=\{\beta:0\leq\beta\leq\nu(n)\}
\]

and additive decompositions `β+γ=ν(n)`.

## Exact forward map

\[
d\mid n\iff 0\leq\nu(d)\leq\nu(n),
\]

\[
(f*g)(n)=\sum_{\beta+\gamma=\nu(n)}F(\beta)G(\gamma).
\]

The box cardinality is

\[
\tau(n)=\prod_p(v_p(n)+1).
\]

## Reverse map and loss

The labeled lattice point recovers each divisor and each convolution split. Sorting divisors by numerical size is extra order information, not box geometry.

## Analytic transform

Inside a common absolute-convergence region, Dirichlet series convert convolution to multiplication. That analytic step requires its convergence certificate.

## Simplification gain

**Structural:** divisor enumeration and convolution become finite lattice decomposition.

## Finite certificate

`EX-BOX-001`: the six divisors of `12` are the six points in the box below `(2,1)`, and `(1*1)(12)=τ(12)=6`.

## Research use

Candidate base language for divisor observables and information-deficiency questions. No asymptotic follows from the box picture alone.
