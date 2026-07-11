# BRIDGE-SQUAREFREE-MOBIUS-001

**Family:** squarefree support / Möbius  
**Maturity:** L2 structural  
**Classification:** Known exact and analytic bridge

## Classical object

Squarefree integers, the Möbius function, and Dirichlet inversion.

## PVG object

The Boolean sublattice `v_p(n)∈{0,1}` and parity of support cardinality.

## Exact forward map

\[
\mu(n)=
\begin{cases}
(-1)^{|\operatorname{supp}\nu(n)|},&\nu(n)\text{ Boolean},\\
0,&\text{otherwise}.
\end{cases}
\]

Squarefreeness is the condition `||ν(n)||∞≤1`.

## Reverse map and loss

The labeled Boolean point recovers the integer and its Möbius value. Support cardinality alone loses prime labels and logarithmic size.

## Analytic transform

For `Re(s)>1`,

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)},
\qquad
\sum_{n\ge1}\frac{\mu(n)^2}{n^s}=\frac{\zeta(s)}{\zeta(2s)}.
\]

These identities do not supply cancellation estimates without additional analytic input.

## Simplification gain

**Structural:** squarefreeness becomes Boolean geometry and the sign becomes support parity.

## Finite certificate

`EX-MOBIUS-001`: `30` is Boolean with support size three, so `μ(30)=-1`; `12` lies off the Boolean cube, so `μ(12)=0`.

## Research use

Natural starting point for conditioned support observables. Any claim about Möbius cancellation remains analytic, not geometric by definition.
