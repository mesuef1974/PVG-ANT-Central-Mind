# Manual Example: \(N=30\)

Status: hand-checkable example under `THEORY-FREEZE-v1.0`

Purpose: complete the fourth canonical reference example using only accepted definitions and proved results. No new observable, conjecture, or prime-distribution claim is introduced.

## 1. Positive ordered addition fiber

\[
\mathcal F_{30}^+=\{(a,30-a):1\le a\le29\}.
\]

Hence

\[
|\mathcal F_{30}^+|=29=N-1.
\]

Explicitly, the ordered pairs run from \((1,29)\) through \((29,1)\).

## 2. Prime-valuation data

The relevant prime axes are

\[
2,3,5,7,11,13,17,19,23,29.
\]

The factorizations for \(1\le n\le29\) are:

| \(n\) | Factorization | Valuation form |
|---:|---|---|
| 1 | \(1\) | \(0\) |
| 2 | \(2\) | \(e_2\) |
| 3 | \(3\) | \(e_3\) |
| 4 | \(2^2\) | \(2e_2\) |
| 5 | \(5\) | \(e_5\) |
| 6 | \(2\cdot3\) | \(e_2+e_3\) |
| 7 | \(7\) | \(e_7\) |
| 8 | \(2^3\) | \(3e_2\) |
| 9 | \(3^2\) | \(2e_3\) |
| 10 | \(2\cdot5\) | \(e_2+e_5\) |
| 11 | \(11\) | \(e_{11}\) |
| 12 | \(2^2\cdot3\) | \(2e_2+e_3\) |
| 13 | \(13\) | \(e_{13}\) |
| 14 | \(2\cdot7\) | \(e_2+e_7\) |
| 15 | \(3\cdot5\) | \(e_3+e_5\) |
| 16 | \(2^4\) | \(4e_2\) |
| 17 | \(17\) | \(e_{17}\) |
| 18 | \(2\cdot3^2\) | \(e_2+2e_3\) |
| 19 | \(19\) | \(e_{19}\) |
| 20 | \(2^2\cdot5\) | \(2e_2+e_5\) |
| 21 | \(3\cdot7\) | \(e_3+e_7\) |
| 22 | \(2\cdot11\) | \(e_2+e_{11}\) |
| 23 | \(23\) | \(e_{23}\) |
| 24 | \(2^3\cdot3\) | \(3e_2+e_3\) |
| 25 | \(5^2\) | \(2e_5\) |
| 26 | \(2\cdot13\) | \(e_2+e_{13}\) |
| 27 | \(3^3\) | \(3e_3\) |
| 28 | \(2^2\cdot7\) | \(2e_2+e_7\) |
| 29 | \(29\) | \(e_{29}\) |

The recovery map \(\rho\) returns the original integer in every row.

## 3. Prime-valuation addition fiber

For \(1\le a\le29\), write

\[
P_a=(\nu(a),\nu(30-a)).
\]

Then

\[
\mathcal G_{30}=\{P_1,\dots,P_{29}\}.
\]

The complete ordered list is determined by the following integer pairs:

\[
\begin{aligned}
&(1,29),(2,28),(3,27),(4,26),(5,25),(6,24),(7,23),\\
&(8,22),(9,21),(10,20),(11,19),(12,18),(13,17),(14,16),\\
&(15,15),(16,14),(17,13),(18,12),(19,11),(20,10),(21,9),\\
&(22,8),(23,7),(24,6),(25,5),(26,4),(27,3),(28,2),(29,1).
\end{aligned}
\]

Applying \(\nu\) coordinatewise gives all 29 valuation pairs. Exact recovery proves that no two distinct ordered integer pairs collapse to the same point.

## 4. Reflection structure

Reflection satisfies

\[
\sigma(P_a)=P_{30-a}.
\]

There are fourteen two-point orbits

\[
\{P_a,P_{30-a}\},\qquad 1\le a\le14,
\]

and one fixed point

\[
P_{15}=(\nu(15),\nu(15)).
\]

Thus the unordered quotient has \(15\) orbits.

## 5. Counting measure and convolution

The counting measure is

\[
\mu_{30}=\sum_{a=1}^{29}\delta_{P_a}.
\]

For arithmetic functions \(f,g\),

\[
\int_{\mathcal G_{30}}\widehat f(x)\widehat g(y)\,d\mu_{30}(x,y)
=
\sum_{a=1}^{29}f(a)g(30-a).
\]

For \(f=g=1\), both sides equal \(29\).

## 6. Prime and prime-power loci

The unordered prime-prime representations are exactly

\[
30=7+23=11+19=13+17.
\]

Therefore the ordered prime-prime points are

\[
\begin{aligned}
&(e_7,e_{23}),\ (e_{23},e_7),\\
&(e_{11},e_{19}),\ (e_{19},e_{11}),\\
&(e_{13},e_{17}),\ (e_{17},e_{13}).
\end{aligned}
\]

Hence the ordered Goldbach count in this fiber is

\[
G(30)=6.
\]

This verifies only the exact intersection statement

\[
\mathcal G_{30}\cap(\mathcal P_1\times\mathcal P_1)\ne\varnothing.
\]

No general Goldbach claim is inferred.

## 7. Exact difference coordinate

For \(1\le a\le29\),

\[
d_{30}(a)=2a-30.
\]

Thus the difference values are

\[
-28,-26,-24,\dots,-2,0,2,\dots,24,26,28.
\]

Reflection changes the sign:

\[
d_{30}(30-a)=-d_{30}(a).
\]

## 8. Full reconstruction modulo \(r=29\)

Since \(29\) is odd and \(r=N-1\),

\[
\operatorname{rank}D_{30,29}
=
\min(29,29)=29.
\]

The labels are

\[
d_{30,29}(a)=2a-30\equiv2a-1\pmod{29}.
\]

Because multiplication by \(2\) is invertible modulo \(29\), the 29 labels are all distinct. Therefore every weight \(w_a\) is recovered from exactly one channel:

\[
w_a=(D_{30,29}w)_{2a-30\, (\mathrm{mod}\,29)}.
\]

After removing zero rows and reordering the nonzero rows, the matrix is a permutation matrix. Hence all singular values are \(1\) and

\[
\kappa_2(D_{30,29})=1.
\]

## 9. Noninjective comparison modulo \(r=13\)

The rank theorem gives

\[
\operatorname{rank}D_{30,13}
=
\min(29,13)=13,
\]

so

\[
\dim\ker D_{30,13}=29-13=16.
\]

Because

\[
2(a+13)-30\equiv2a-30\pmod{13},
\]

indices separated by 13 lie in the same channel.

The channel classes are

\[
\begin{aligned}
&\{1,14,27\},\ \{2,15,28\},\ \{3,16,29\},\\
&\{4,17\},\ \{5,18\},\ \{6,19\},\ \{7,20\},\ \{8,21\},\\
&\{9,22\},\ \{10,23\},\ \{11,24\},\ \{12,25\},\ \{13,26\}.
\end{aligned}
\]

A concrete basis for the kernel is

\[
\{e_a-e_{a+13}:1\le a\le16\}.
\]

The first three channel classes have three indices and contribute two independent invisible directions each; the remaining ten classes have two indices and contribute one each. Therefore

\[
3\cdot2+10\cdot1=16,
\]

in agreement with the kernel-dimension formula.

## 10. Canonical-theory checklist

- Exact recovery — verified for all integers \(1\le n\le29\).
- No-information-loss theorem — verified through the 29 distinct ordered pairs.
- Reflection theorem — fourteen paired orbits and one fixed point.
- Fiber convolution identity — checked with the constant functions.
- Prime-locus intersection — six ordered prime-prime points.
- Single-modulus rank theorem — checked at \(r=29\) and \(r=13\).
- Full reconstruction — explicit at \(r=29\).
- Kernel dimension and a concrete basis — explicit at \(r=13\).

This completes the four-example suite \(N=10,12,24,30\) required by `THEORY-FREEZE-v1.0`.