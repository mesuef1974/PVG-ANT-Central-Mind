# Manual Example: \(N=12\)

Status: hand-checkable example under `THEORY-FREEZE-v1.0`

Purpose: illustrate only the accepted definitions and proved results. No new observable, conjecture, or research direction is introduced.

## 1. Positive ordered addition fiber

\[
\mathcal F_{12}^+
=
\{(a,12-a):1\le a\le11\}.
\]

Explicitly,

\[
\begin{aligned}
\mathcal F_{12}^+=\{&(1,11),(2,10),(3,9),(4,8),(5,7),(6,6),\\
&(7,5),(8,4),(9,3),(10,2),(11,1)\}.
\end{aligned}
\]

Hence

\[
|\mathcal F_{12}^+|=11=N-1.
\]

## 2. Prime-valuation vectors

Only the prime axes \(2,3,5,7,11\) occur for integers from \(1\) to \(11\). We display vectors in the coordinate order

\[
(2,3,5,7,11).
\]

| \(n\) | Factorization | \(\nu(n)\) |
|---:|---|---|
| 1 | \(1\) | \((0,0,0,0,0)\) |
| 2 | \(2\) | \((1,0,0,0,0)\) |
| 3 | \(3\) | \((0,1,0,0,0)\) |
| 4 | \(2^2\) | \((2,0,0,0,0)\) |
| 5 | \(5\) | \((0,0,1,0,0)\) |
| 6 | \(2\cdot3\) | \((1,1,0,0,0)\) |
| 7 | \(7\) | \((0,0,0,1,0)\) |
| 8 | \(2^3\) | \((3,0,0,0,0)\) |
| 9 | \(3^2\) | \((0,2,0,0,0)\) |
| 10 | \(2\cdot5\) | \((1,0,1,0,0)\) |
| 11 | \(11\) | \((0,0,0,0,1)\) |

The recovery map returns the original integer in every row. For example,

\[
\rho(3,0,0,0,0)=2^3=8,
\qquad
\rho(1,0,1,0,0)=2\cdot5=10.
\]

## 3. Prime-valuation addition fiber

The eleven points of \(\mathcal G_{12}\) are:

| \(a\) | \(12-a\) | \(P_a=(\nu(a),\nu(12-a))\) |
|---:|---:|---|
| 1 | 11 | \(((0,0,0,0,0),(0,0,0,0,1))\) |
| 2 | 10 | \(((1,0,0,0,0),(1,0,1,0,0))\) |
| 3 | 9 | \(((0,1,0,0,0),(0,2,0,0,0))\) |
| 4 | 8 | \(((2,0,0,0,0),(3,0,0,0,0))\) |
| 5 | 7 | \(((0,0,1,0,0),(0,0,0,1,0))\) |
| 6 | 6 | \(((1,1,0,0,0),(1,1,0,0,0))\) |
| 7 | 5 | \(((0,0,0,1,0),(0,0,1,0,0))\) |
| 8 | 4 | \(((3,0,0,0,0),(2,0,0,0,0))\) |
| 9 | 3 | \(((0,2,0,0,0),(0,1,0,0,0))\) |
| 10 | 2 | \(((1,0,1,0,0),(1,0,0,0,0))\) |
| 11 | 1 | \(((0,0,0,0,1),(0,0,0,0,0))\) |

This table makes the no-information-loss theorem visible: every valuation pair recovers exactly one ordered integer pair.

## 4. Reflection structure

The reflection is

\[
\sigma(P_a)=P_{12-a}.
\]

The five two-point orbits are

\[
\{P_1,P_{11}\},\quad
\{P_2,P_{10}\},\quad
\{P_3,P_9\},\quad
\{P_4,P_8\},\quad
\{P_5,P_7\},
\]

and the unique fixed point is

\[
P_6=(\nu(6),\nu(6)).
\]

Thus the unordered quotient has six orbits.

## 5. Counting measure and fiber convolution

The counting measure is

\[
\mu_{12}=\sum_{a=1}^{11}\delta_{P_a}.
\]

For arbitrary arithmetic functions \(f,g\),

\[
\int_{\mathcal G_{12}}\widehat f(x)\widehat g(y)\,d\mu_{12}
=
\sum_{a=1}^{11}f(a)g(12-a).
\]

For the constant functions \(f=g=1\), both sides equal \(11\).

## 6. Prime and prime-power loci

The prime numbers below \(12\) are

\[
2,3,5,7,11.
\]

Their valuation vectors are

\[
e_2,e_3,e_5,e_7,e_{11}.
\]

The ordered prime-prime points in \(\mathcal G_{12}\) are

\[
P_5=(e_5,e_7),
\qquad
P_7=(e_7,e_5).
\]

Therefore the ordered Goldbach count is

\[
G(12)=2.
\]

The corresponding unordered representation is

\[
12=5+7.
\]

This illustrates the exact intersection reformulation

\[
\mathcal G_{12}\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
\]

Prime powers appearing in the fiber are

\[
2,3,4,5,7,8,9,11.
\]

Their valuation vectors lie on the prime-power axis locus \(\mathcal A_1\). The numbers \(6\) and \(10\) do not lie on a single prime axis.

## 7. Exact integer difference coordinate

For \(a=1,\dots,11\),

\[
d_{12}(a)=2a-12.
\]

| \(a\) | \(d_{12}(a)\) |
|---:|---:|
| 1 | \(-10\) |
| 2 | \(-8\) |
| 3 | \(-6\) |
| 4 | \(-4\) |
| 5 | \(-2\) |
| 6 | \(0\) |
| 7 | \(2\) |
| 8 | \(4\) |
| 9 | \(6\) |
| 10 | \(8\) |
| 11 | \(10\) |

Reflection sends

\[
d_{12}(12-a)=-d_{12}(a).
\]

## 8. Difference channels modulo \(r=11\)

Because \(r=11\) is odd and

\[
r=N-1=11,
\]

the full-reconstruction corollary applies.

The modular labels are

\[
d_{12,11}(a)=2a-12\equiv2a-1\pmod{11}.
\]

| \(a\) | \(d_{12,11}(a)\) |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 5 |
| 4 | 7 |
| 5 | 9 |
| 6 | 0 |
| 7 | 2 |
| 8 | 4 |
| 9 | 6 |
| 10 | 8 |
| 11 | 10 |

All eleven residues occur exactly once. Hence

\[
\operatorname{rank}D_{12,11}=11.
\]

This agrees with the theorem:

\[
\min\!\left(11,\frac{11}{\gcd(2,11)}\right)=11.
\]

For a general weight vector

\[
w=(w_1,\dots,w_{11}),
\]

the channel vector, in residue order \(d=0,1,\dots,10\), is

\[
D_{12,11}w
=
(w_6,w_1,w_7,w_2,w_8,w_3,w_9,w_4,w_{10},w_5,w_{11}).
\]

The explicit reconstruction is

\[
\begin{aligned}
w_1&=(D_{12,11}w)_1,&
 w_2&=(D_{12,11}w)_3,&
 w_3&=(D_{12,11}w)_5,\\
w_4&=(D_{12,11}w)_7,&
 w_5&=(D_{12,11}w)_9,&
 w_6&=(D_{12,11}w)_0,\\
w_7&=(D_{12,11}w)_2,&
 w_8&=(D_{12,11}w)_4,&
 w_9&=(D_{12,11}w)_6,\\
w_{10}&=(D_{12,11}w)_8,&
 w_{11}&=(D_{12,11}w)_{10}.
\end{aligned}
\]

After row reordering, the matrix is the \(11\times11\) identity matrix. Therefore all singular values are \(1\) and

\[
\kappa_2(D_{12,11})=1.
\]

## 9. Intermediate comparison: modulo \(r=7\)

The rank theorem gives

\[
\operatorname{rank}D_{12,7}=\min(11,7)=7,
\]

so

\[
\dim\ker D_{12,7}=4.
\]

The labels are

| \(a\) | label modulo \(7\) |
|---:|---:|
| 1 | 4 |
| 2 | 6 |
| 3 | 1 |
| 4 | 3 |
| 5 | 5 |
| 6 | 0 |
| 7 | 2 |
| 8 | 4 |
| 9 | 6 |
| 10 | 1 |
| 11 | 3 |

Thus a concrete kernel basis is

\[
e_1-e_8,
\quad
e_2-e_9,
\quad
e_3-e_{10},
\quad
e_4-e_{11}.
\]

## 10. Noninjective comparison: modulo \(r=5\)

The theorem gives

\[
\operatorname{rank}D_{12,5}=\min(11,5)=5,
\]

and therefore

\[
\dim\ker D_{12,5}=11-5=6.
\]

The labels are

\[
2a-12\equiv2a-2\pmod5.
\]

| \(a\) | label modulo \(5\) |
|---:|---:|
| 1 | 0 |
| 2 | 2 |
| 3 | 4 |
| 4 | 1 |
| 5 | 3 |
| 6 | 0 |
| 7 | 2 |
| 8 | 4 |
| 9 | 1 |
| 10 | 3 |
| 11 | 0 |

Hence

\[
\begin{aligned}
(D_{12,5}w)_0&=w_1+w_6+w_{11},\\
(D_{12,5}w)_1&=w_4+w_9,\\
(D_{12,5}w)_2&=w_2+w_7,\\
(D_{12,5}w)_3&=w_5+w_{10},\\
(D_{12,5}w)_4&=w_3+w_8.
\end{aligned}
\]

A concrete kernel basis is

\[
e_1-e_6,
\quad
e_6-e_{11},
\quad
e_2-e_7,
\quad
e_3-e_8,
\quad
e_4-e_9,
\quad
e_5-e_{10}.
\]

Every basis vector transfers weight inside one residue channel while leaving all channel totals unchanged.

## 11. Checklist against the canonical theory

- Exact recovery: verified explicitly.
- No-information-loss theorem: visible from the valuation-pair table.
- Reflection structure: five paired orbits and one fixed point.
- Fiber convolution identity: checked for the constant weight.
- Prime-locus intersection: two ordered prime-prime points.
- Single-modulus rank theorem: checked for \(r=11,7,5\).
- Full reconstruction: written explicitly for \(r=11\).
- Kernel structure: written explicitly for \(r=7\) and \(r=5\).

No claim in this example goes beyond the canonical definitions, proved theorems, and exact Goldbach reformulation.
