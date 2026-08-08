# Manual Example: \(N=10\)

Status: hand-checkable example under `THEORY-FREEZE-v1.0`

Purpose: illustrate only the accepted definitions and proved results. No new observable or conjecture is introduced.

## 1. Positive ordered addition fiber

\[
\mathcal F_{10}^+
=
\{(a,10-a):1\le a\le9\}.
\]

Explicitly,

\[
\begin{aligned}
\mathcal F_{10}^+=\{&(1,9),(2,8),(3,7),(4,6),(5,5),\\
&(6,4),(7,3),(8,2),(9,1)\}.
\end{aligned}
\]

Hence

\[
|\mathcal F_{10}^+|=9=N-1.
\]

## 2. Prime-valuation vectors

Only the prime axes \(2,3,5,7\) occur for integers from \(1\) to \(9\). We therefore display vectors in the coordinate order

\[
(2,3,5,7).
\]

| \(n\) | Factorization | \(\nu(n)\) |
|---:|---|---|
| 1 | \(1\) | \((0,0,0,0)\) |
| 2 | \(2\) | \((1,0,0,0)\) |
| 3 | \(3\) | \((0,1,0,0)\) |
| 4 | \(2^2\) | \((2,0,0,0)\) |
| 5 | \(5\) | \((0,0,1,0)\) |
| 6 | \(2\cdot3\) | \((1,1,0,0)\) |
| 7 | \(7\) | \((0,0,0,1)\) |
| 8 | \(2^3\) | \((3,0,0,0)\) |
| 9 | \(3^2\) | \((0,2,0,0)\) |

The recovery map returns the original integer in every row. For example,

\[
\rho(3,0,0,0)=2^3=8,
\qquad
\rho(1,1,0,0)=2\cdot3=6.
\]

## 3. Prime-valuation addition fiber

The nine points of \(\mathcal G_{10}\) are:

| \(a\) | \(10-a\) | \(P_a=(\nu(a),\nu(10-a))\) |
|---:|---:|---|
| 1 | 9 | \(((0,0,0,0),(0,2,0,0))\) |
| 2 | 8 | \(((1,0,0,0),(3,0,0,0))\) |
| 3 | 7 | \(((0,1,0,0),(0,0,0,1))\) |
| 4 | 6 | \(((2,0,0,0),(1,1,0,0))\) |
| 5 | 5 | \(((0,0,1,0),(0,0,1,0))\) |
| 6 | 4 | \(((1,1,0,0),(2,0,0,0))\) |
| 7 | 3 | \(((0,0,0,1),(0,1,0,0))\) |
| 8 | 2 | \(((3,0,0,0),(1,0,0,0))\) |
| 9 | 1 | \(((0,2,0,0),(0,0,0,0))\) |

This table makes the no-information-loss theorem visible: every valuation pair recovers exactly one ordered integer pair.

## 4. Reflection structure

The reflection is

\[
\sigma(P_a)=P_{10-a}.
\]

The four two-point orbits are

\[
\{P_1,P_9\},\quad
\{P_2,P_8\},\quad
\{P_3,P_7\},\quad
\{P_4,P_6\},
\]

and the unique fixed point is

\[
P_5=(\nu(5),\nu(5)).
\]

Thus the unordered quotient has five orbits.

## 5. Counting measure and fiber convolution

The counting measure is

\[
\mu_{10}=\sum_{a=1}^{9}\delta_{P_a}.
\]

For arbitrary arithmetic functions \(f,g\),

\[
\int_{\mathcal G_{10}}\widehat f(x)\widehat g(y)\,d\mu_{10}
=
\sum_{a=1}^{9}f(a)g(10-a).
\]

For the constant functions \(f=g=1\), both sides equal \(9\).

## 6. Prime and prime-power loci

The prime numbers below \(10\) are

\[
2,3,5,7.
\]

Their valuation vectors are the unit vectors

\[
e_2,e_3,e_5,e_7.
\]

The ordered prime-prime points in \(\mathcal G_{10}\) are

\[
P_3=(e_3,e_7),
\qquad
P_5=(e_5,e_5),
\qquad
P_7=(e_7,e_3).
\]

Therefore the ordered Goldbach count is

\[
G(10)=3.
\]

The corresponding unordered representations are

\[
10=3+7=5+5.
\]

This illustrates the exact intersection reformulation

\[
\mathcal G_{10}\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
\]

Prime powers appearing in the fiber include

\[
2,3,4,5,7,8,9,
\]

whose valuation vectors lie on the axis locus \(\mathcal A_1\), except \(6\), whose vector has support on two prime axes.

## 7. Exact integer difference coordinate

For \(a=1,\dots,9\),

\[
d_{10}(a)=2a-10.
\]

| \(a\) | \(d_{10}(a)\) |
|---:|---:|
| 1 | \(-8\) |
| 2 | \(-6\) |
| 3 | \(-4\) |
| 4 | \(-2\) |
| 5 | \(0\) |
| 6 | \(2\) |
| 7 | \(4\) |
| 8 | \(6\) |
| 9 | \(8\) |

Reflection sends

\[
d_{10}(10-a)=-d_{10}(a).
\]

## 8. Difference channels modulo \(r=9\)

Because \(r=9\) is odd and

\[
r=N-1=9,
\]

Corollary 5.6 predicts full reconstruction.

The modular labels are

\[
d_{10,9}(a)=2a-10\equiv2a-1\pmod9.
\]

| \(a\) | \(d_{10,9}(a)\) |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 5 |
| 4 | 7 |
| 5 | 0 |
| 6 | 2 |
| 7 | 4 |
| 8 | 6 |
| 9 | 8 |

All nine residues occur exactly once. Hence

\[
\operatorname{rank}D_{10,9}=9.
\]

This agrees with the theorem:

\[
\min\!\left(9,\frac9{\gcd(2,9)}\right)=\min(9,9)=9.
\]

For a general weight vector

\[
w=(w_1,\dots,w_9),
\]

the channel vector is

\[
D_{10,9}w
=
(w_5,w_1,w_6,w_2,w_7,w_3,w_8,w_4,w_9),
\]

when its coordinates are listed in residue order \(d=0,1,\dots,8\).

The explicit reconstruction is therefore

\[
\begin{aligned}
w_1&=(D_{10,9}w)_1,&
w_2&=(D_{10,9}w)_3,&
w_3&=(D_{10,9}w)_5,\\
w_4&=(D_{10,9}w)_7,&
w_5&=(D_{10,9}w)_0,&
w_6&=(D_{10,9}w)_2,\\
w_7&=(D_{10,9}w)_4,&
w_8&=(D_{10,9}w)_6,&
w_9&=(D_{10,9}w)_8.
\end{aligned}
\]

After row reordering, the matrix is the \(9\times9\) identity matrix. Thus all singular values are \(1\) and

\[
\kappa_2(D_{10,9})=1.
\]

## 9. Noninjective comparison: modulo \(r=5\)

The theorem gives

\[
\operatorname{rank}D_{10,5}
=
\min(9,5)=5,
\]

so

\[
\dim\ker D_{10,5}=9-5=4.
\]

The labels are

\[
2a-10\equiv2a\pmod5,
\]

which repeat with period \(5\):

| \(a\) | label modulo \(5\) |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 1 |
| 4 | 3 |
| 5 | 0 |
| 6 | 2 |
| 7 | 4 |
| 8 | 1 |
| 9 | 3 |

Thus

\[
\begin{aligned}
(D_{10,5}w)_0&=w_5,\\
(D_{10,5}w)_1&=w_3+w_8,\\
(D_{10,5}w)_2&=w_1+w_6,\\
(D_{10,5}w)_3&=w_4+w_9,\\
(D_{10,5}w)_4&=w_2+w_7.
\end{aligned}
\]

A concrete kernel basis is

\[
e_1-e_6,
\quad
e_2-e_7,
\quad
e_3-e_8,
\quad
e_4-e_9.
\]

These vectors are invisible because each shifts weight inside one channel while preserving the channel total.

## 10. Checklist against the canonical theory

- Exact recovery: verified explicitly.
- No-information-loss theorem: visible from the table.
- Reflection structure: four paired orbits and one fixed point.
- Fiber convolution identity: checked for the constant weight.
- Prime-locus intersection: three ordered prime-prime points.
- Single-modulus rank theorem: checked for \(r=9\) and \(r=5\).
- Full reconstruction: written explicitly for \(r=9\).
- Kernel structure: written explicitly for \(r=5\).

No claim in this example goes beyond the canonical definitions, proved theorems, and exact Goldbach reformulation.