# Manual Example: \(N=24\)

Status: hand-checkable example under `THEORY-FREEZE-v1.0`

Purpose: verify only the accepted definitions and proved results. No new observable, theorem, or conjecture is introduced.

## 1. Positive ordered addition fiber

\[\mathcal F_{24}^+=\{(a,24-a):1\le a\le23\},\qquad |\mathcal F_{24}^+|=23.\]

| \(a\) | \(24-a\) |
|---:|---:|
| 1 | 23 |
| 2 | 22 |
| 3 | 21 |
| 4 | 20 |
| 5 | 19 |
| 6 | 18 |
| 7 | 17 |
| 8 | 16 |
| 9 | 15 |
| 10 | 14 |
| 11 | 13 |
| 12 | 12 |
| 13 | 11 |
| 14 | 10 |
| 15 | 9 |
| 16 | 8 |
| 17 | 7 |
| 18 | 6 |
| 19 | 5 |
| 20 | 4 |
| 21 | 3 |
| 22 | 2 |
| 23 | 1 |

## 2. Prime-valuation vectors

Use coordinate order \((2,3,5,7,11,13,17,19,23)\).

| \(n\) | Factorization | \(\nu(n)\) | \(\Omega(n)\) | \(\omega(n)\) |
|---:|---|---|---:|---:|
| 1 | \(1\) | \((0,0,0,0,0,0,0,0,0)\) | 0 | 0 |
| 2 | \(2\) | \((1,0,0,0,0,0,0,0,0)\) | 1 | 1 |
| 3 | \(3\) | \((0,1,0,0,0,0,0,0,0)\) | 1 | 1 |
| 4 | \(2^2\) | \((2,0,0,0,0,0,0,0,0)\) | 2 | 1 |
| 5 | \(5\) | \((0,0,1,0,0,0,0,0,0)\) | 1 | 1 |
| 6 | \(2\cdot 3\) | \((1,1,0,0,0,0,0,0,0)\) | 2 | 2 |
| 7 | \(7\) | \((0,0,0,1,0,0,0,0,0)\) | 1 | 1 |
| 8 | \(2^3\) | \((3,0,0,0,0,0,0,0,0)\) | 3 | 1 |
| 9 | \(3^2\) | \((0,2,0,0,0,0,0,0,0)\) | 2 | 1 |
| 10 | \(2\cdot 5\) | \((1,0,1,0,0,0,0,0,0)\) | 2 | 2 |
| 11 | \(11\) | \((0,0,0,0,1,0,0,0,0)\) | 1 | 1 |
| 12 | \(2^2\cdot 3\) | \((2,1,0,0,0,0,0,0,0)\) | 3 | 2 |
| 13 | \(13\) | \((0,0,0,0,0,1,0,0,0)\) | 1 | 1 |
| 14 | \(2\cdot 7\) | \((1,0,0,1,0,0,0,0,0)\) | 2 | 2 |
| 15 | \(3\cdot 5\) | \((0,1,1,0,0,0,0,0,0)\) | 2 | 2 |
| 16 | \(2^4\) | \((4,0,0,0,0,0,0,0,0)\) | 4 | 1 |
| 17 | \(17\) | \((0,0,0,0,0,0,1,0,0)\) | 1 | 1 |
| 18 | \(2\cdot 3^2\) | \((1,2,0,0,0,0,0,0,0)\) | 3 | 2 |
| 19 | \(19\) | \((0,0,0,0,0,0,0,1,0)\) | 1 | 1 |
| 20 | \(2^2\cdot 5\) | \((2,0,1,0,0,0,0,0,0)\) | 3 | 2 |
| 21 | \(3\cdot 7\) | \((0,1,0,1,0,0,0,0,0)\) | 2 | 2 |
| 22 | \(2\cdot 11\) | \((1,0,0,0,1,0,0,0,0)\) | 2 | 2 |
| 23 | \(23\) | \((0,0,0,0,0,0,0,0,1)\) | 1 | 1 |

The columns \(\Omega\) and \(\omega\) are classical arithmetic functions included only to make the example easier to audit.

## 3. Prime-valuation addition fiber

| \(a\) | \(24-a\) | \(P_a=(\nu(a),\nu(24-a))\) |
|---:|---:|---|
| 1 | 23 | \(( (0,0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,0,1) )\) |
| 2 | 22 | \(( (1,0,0,0,0,0,0,0,0), (1,0,0,0,1,0,0,0,0) )\) |
| 3 | 21 | \(( (0,1,0,0,0,0,0,0,0), (0,1,0,1,0,0,0,0,0) )\) |
| 4 | 20 | \(( (2,0,0,0,0,0,0,0,0), (2,0,1,0,0,0,0,0,0) )\) |
| 5 | 19 | \(( (0,0,1,0,0,0,0,0,0), (0,0,0,0,0,0,0,1,0) )\) |
| 6 | 18 | \(( (1,1,0,0,0,0,0,0,0), (1,2,0,0,0,0,0,0,0) )\) |
| 7 | 17 | \(( (0,0,0,1,0,0,0,0,0), (0,0,0,0,0,0,1,0,0) )\) |
| 8 | 16 | \(( (3,0,0,0,0,0,0,0,0), (4,0,0,0,0,0,0,0,0) )\) |
| 9 | 15 | \(( (0,2,0,0,0,0,0,0,0), (0,1,1,0,0,0,0,0,0) )\) |
| 10 | 14 | \(( (1,0,1,0,0,0,0,0,0), (1,0,0,1,0,0,0,0,0) )\) |
| 11 | 13 | \(( (0,0,0,0,1,0,0,0,0), (0,0,0,0,0,1,0,0,0) )\) |
| 12 | 12 | \(( (2,1,0,0,0,0,0,0,0), (2,1,0,0,0,0,0,0,0) )\) |
| 13 | 11 | \(( (0,0,0,0,0,1,0,0,0), (0,0,0,0,1,0,0,0,0) )\) |
| 14 | 10 | \(( (1,0,0,1,0,0,0,0,0), (1,0,1,0,0,0,0,0,0) )\) |
| 15 | 9 | \(( (0,1,1,0,0,0,0,0,0), (0,2,0,0,0,0,0,0,0) )\) |
| 16 | 8 | \(( (4,0,0,0,0,0,0,0,0), (3,0,0,0,0,0,0,0,0) )\) |
| 17 | 7 | \(( (0,0,0,0,0,0,1,0,0), (0,0,0,1,0,0,0,0,0) )\) |
| 18 | 6 | \(( (1,2,0,0,0,0,0,0,0), (1,1,0,0,0,0,0,0,0) )\) |
| 19 | 5 | \(( (0,0,0,0,0,0,0,1,0), (0,0,1,0,0,0,0,0,0) )\) |
| 20 | 4 | \(( (2,0,1,0,0,0,0,0,0), (2,0,0,0,0,0,0,0,0) )\) |
| 21 | 3 | \(( (0,1,0,1,0,0,0,0,0), (0,1,0,0,0,0,0,0,0) )\) |
| 22 | 2 | \(( (1,0,0,0,1,0,0,0,0), (1,0,0,0,0,0,0,0,0) )\) |
| 23 | 1 | \(( (0,0,0,0,0,0,0,0,1), (0,0,0,0,0,0,0,0,0) )\) |

Every valuation pair recovers exactly one ordered integer pair, illustrating the no-information-loss theorem.

## 4. Reflection structure

\[\sigma(P_a)=P_{24-a}.\]

There are eleven two-point orbits

\[\{P_a,P_{24-a}\},\qquad 1\le a\le11,\]

and one fixed point

\[P_{12}=(\nu(12),\nu(12)).\]

Hence the unordered quotient contains twelve orbits.

## 5. Counting measure and convolution identity

\[\mu_{24}=\sum_{a=1}^{23}\delta_{P_a}.\]

For arithmetic functions \(f,g\),

\[\int_{\mathcal G_{24}}\widehat f(x)\widehat g(y)\,d\mu_{24}=\sum_{a=1}^{23}f(a)g(24-a).\]

For \(f=g=1\), both sides equal \(23\).

## 6. Prime and prime-power loci

The ordered prime-prime points are indexed by

\[a\in\{5,7,11,13,17,19\}.\]

Thus

\[\mathcal G_{24}\cap(\mathcal P_1\times\mathcal P_1)=\{(e_5,e_{19}),(e_7,e_{17}),(e_{11},e_{13}),(e_{13},e_{11}),(e_{17},e_7),(e_{19},e_5)\}.\]

Therefore the ordered Goldbach count is

\[G(24)=6,\]

and the unordered representations are

\[24=5+19=7+17=11+13.\]

This is an exact reformulation check, not a proof of Goldbach.

## 7. Exact integer difference coordinate

\[d_{24}(a)=2a-24.\]

| \(a\) | \(d_{24}(a)\) |
|---:|---:|
| 1 | -22 |
| 2 | -20 |
| 3 | -18 |
| 4 | -16 |
| 5 | -14 |
| 6 | -12 |
| 7 | -10 |
| 8 | -8 |
| 9 | -6 |
| 10 | -4 |
| 11 | -2 |
| 12 | 0 |
| 13 | 2 |
| 14 | 4 |
| 15 | 6 |
| 16 | 8 |
| 17 | 10 |
| 18 | 12 |
| 19 | 14 |
| 20 | 16 |
| 21 | 18 |
| 22 | 20 |
| 23 | 22 |

Reflection gives \(d_{24}(24-a)=-d_{24}(a)\).

## 8. Injective channels modulo \(r=23\)

Because \(23\) is odd and \(23=N-1\), the rank theorem gives

\[\operatorname{rank}D_{24,23}=23.\]

| residue \(d\) | unique index \(a\) |
|---:|---:|
| 0 | 12 |
| 1 | 1 |
| 2 | 13 |
| 3 | 2 |
| 4 | 14 |
| 5 | 3 |
| 6 | 15 |
| 7 | 4 |
| 8 | 16 |
| 9 | 5 |
| 10 | 17 |
| 11 | 6 |
| 12 | 18 |
| 13 | 7 |
| 14 | 19 |
| 15 | 8 |
| 16 | 20 |
| 17 | 9 |
| 18 | 21 |
| 19 | 10 |
| 20 | 22 |
| 21 | 11 |
| 22 | 23 |

Hence every weight is reconstructed by

\[w_a=(D_{24,23}w)_{2a-24\pmod{23}}.\]

After row reordering, the matrix is the \(23\times23\) identity, so all singular values equal \(1\) and

\[\kappa_2(D_{24,23})=1.\]

## 9. Noninjective comparison modulo \(r=11\)

The rank theorem gives

\[\operatorname{rank}D_{24,11}=11,\qquad \dim\ker D_{24,11}=12.\]

| residue \(d\) | indices in the channel | channel sum |
|---:|---|---|
| 0 | 1, 12, 23 | \(w_1+w_12+w_23\) |
| 1 | 7, 18 | \(w_7+w_18\) |
| 2 | 2, 13 | \(w_2+w_13\) |
| 3 | 8, 19 | \(w_8+w_19\) |
| 4 | 3, 14 | \(w_3+w_14\) |
| 5 | 9, 20 | \(w_9+w_20\) |
| 6 | 4, 15 | \(w_4+w_15\) |
| 7 | 10, 21 | \(w_10+w_21\) |
| 8 | 5, 16 | \(w_5+w_16\) |
| 9 | 11, 22 | \(w_11+w_22\) |
| 10 | 6, 17 | \(w_6+w_17\) |

A concrete kernel basis is obtained by choosing the first index in each channel as anchor and subtracting it from the others:

\[
\begin{aligned}
e_{1}-e_{12},\\
e_{1}-e_{23},\\
e_{7}-e_{18},\\
e_{2}-e_{13},\\
e_{8}-e_{19},\\
e_{3}-e_{14},\\
e_{9}-e_{20},\\
e_{4}-e_{15},\\
e_{10}-e_{21},\\
e_{5}-e_{16},\\
e_{11}-e_{22},\\
e_{6}-e_{17}.\\
\end{aligned}
\]

There are twelve vectors, matching the kernel dimension. Each moves weight within one residue channel while preserving the channel total.

## 10. Checklist against the canonical theory

- Exact recovery: verified for all integers from 1 to 23.
- No-information-loss theorem: visible from the full fiber table.
- Reflection theorem: eleven paired orbits and one fixed point.
- Fiber convolution identity: checked with constant weights.
- Prime-locus intersection: six ordered prime-prime points.
- Single-modulus rank theorem: checked at r=23 and r=11.
- Full reconstruction and perfect conditioning: explicit at r=23.
- Kernel dimension and a concrete basis: explicit at r=11.

No statement in this example exceeds the accepted definitions, proved theorems, or exact prime-locus reformulation.