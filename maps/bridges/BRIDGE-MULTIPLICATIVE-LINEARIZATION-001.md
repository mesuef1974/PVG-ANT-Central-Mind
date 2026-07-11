# BRIDGE-MULTIPLICATIVE-LINEARIZATION-001

**Family:** multiplication / divisibility / order  
**Maturity:** L2 structural  
**Classification:** Known exact identity / structural reinterpretation

## Classical object

Integer multiplication, divisibility, gcd, and lcm.

## PVG object

Finite-support vectors `ν(n)=(v_p(n))_p`, vector addition, and coordinate order.

## Exact forward map

\[
\nu(mn)=\nu(m)+\nu(n),
\qquad
d\mid n\iff \nu(d)\leq\nu(n),
\]

\[
\nu(\gcd(m,n))=\min(\nu(m),\nu(n)),
\qquad
\nu(\operatorname{lcm}(m,n))=\max(\nu(m),\nu(n)).
\]

## Reverse map and loss

Unique factorization reconstructs `n` from the labeled vector. The bridge is lossless for multiplicative structure. It does not encode addition, successor order, or distances on the integer line.

## Simplification gain

**Structural:** multiplication becomes addition and divisibility becomes product order.

## Finite certificate

`EX-MULT-001`: `12·18=216`, with vector addition; gcd and lcm become coordinate min/max.

## Research use

Foundation for every later bridge. It is not itself an original theorem and cannot be used to transfer additive or spectral claims without another bridge.

## Sources

Unique factorization; Lean P3 valuation laws; canonical language kernel.
