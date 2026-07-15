# Reduced-Modulus Principal-Frequency Split

Status: `PROVED-v1.2`

## 1. Effective modulus

Let

\[
g=\gcd(2,r),\qquad q=r/g.
\]

The realized difference classes satisfy

\[
d\equiv -N\pmod g.
\]

Writing

\[
d=-N+gu\pmod r,
\]

the congruence

\[
2a-N\equiv d\pmod r
\]

is equivalent to

\[
(2/g)a\equiv u\pmod q.
\]

Since \(\gcd(2/g,q)=1\), multiplication by \(2/g\) permutes \(\mathbb Z/q\mathbb Z\). Therefore the nonempty rows of \(D_{N,r}\) are permutation-equivalent to the ordinary residue aggregation operator

\[
Z_{N,q}(c)=\sum_{\substack{1\le a<N\\a\equiv c\, (\mathrm{mod}\,q)}}w_a.
\]

Hence all information carried by modulus \(r\) is already carried by the reduced modulus \(q=r/\gcd(2,r)\).

## 2. Reduced Fourier transform

Define

\[
\widehat Z_{N,q}(k)
=
\sum_{a=1}^{N-1}w_a e_q(ka),
\qquad k\in\mathbb Z/q\mathbb Z.
\]

Then

\[
Z_{N,q}(c)
=
\frac1q\sum_{k\bmod q}\widehat Z_{N,q}(k)e_q(-kc).
\]

The zero frequency is

\[
\widehat Z_{N,q}(0)=\sum_{a=1}^{N-1}w_a.
\]

For the von Mangoldt fiber weight

\[
w_a=\Lambda(a)\Lambda(N-a),
\]

this is exactly \(R_\Lambda(N)\).

## 3. Principal-frequency split

Let \(A\subseteq (\mathbb Z/q\mathbb Z)\setminus\{0\}\) be any selected frequency set. Define

\[
P_A(c)
=
\frac1q\sum_{k\in A}\widehat Z(k)e_q(-kc)
\]

and

\[
T_A(c)
=
\frac1q\sum_{\substack{k\ne0\\k\notin A}}
\widehat Z(k)e_q(-kc).
\]

Then

\[
Z(c)=\frac{R_\Lambda(N)}q+P_A(c)+T_A(c).
\]

The residual tail satisfies the rigorous bound

\[
|T_A(c)|
\le
\frac1q\sum_{\substack{k\ne0\\k\notin A}}|\widehat Z(k)|.
\]

Therefore

\[
Z(c)
\ge
\frac{R_\Lambda(N)}q
+\operatorname{Re}P_A(c)
-\frac1q\sum_{\substack{k\ne0\\k\notin A}}|\widehat Z(k)|.
\]

## 4. Prime-channel certificate

Let

\[
H_{N,q}(c)
=
\sum_{\substack{1\le a<N\\a\equiv c\, (\mathrm{mod}\,q)\\a=p^m,\ m\ge2}}
\log p.
\]

In the residue coordinate \(a\equiv c\pmod q\), the complementary summand satisfies

\[
N-a\equiv N-c\pmod q.
\]

Therefore the correct local higher-prime-power contamination bound is

\[
C_{N,q}(c)
=
\log N\bigl(H_{N,q}(c)+H_{N,q}(N-c)\bigr),
\]

where residues are interpreted modulo \(q\).

If

\[
\frac{R_\Lambda(N)}q
+\operatorname{Re}P_A(c)
-\frac1q\sum_{\substack{k\ne0\\k\notin A}}|\widehat Z(k)|
>
C_{N,q}(c),
\]

then the prime-prime mass in residue class \(c\) is positive.

Equivalently, there exist primes \(p,q'\) such that

\[
p+q'=N,
\qquad
p\equiv c\pmod q.
\]

After converting back through the permutation induced by \(2/g\), this gives a certificate in the original difference channel modulo \(r\).

## 5. Monotonicity in the selected set

If \(A\subseteq B\), the exact principal contribution changes with phase, while the absolute-value tail cannot increase:

\[
\sum_{k\notin B}|\widehat Z(k)|
\le
\sum_{k\notin A}|\widehat Z(k)|.
\]

Thus enlarging the selected set reduces the certified uncertainty budget, though it does not guarantee a monotone lower bound for every channel because the newly exposed principal contribution may be negative.

## 6. Safe frequency selection

Selecting frequencies by largest magnitude is a computational diagnostic and certificate generator because the retained contribution is used exactly and only the omitted tail is bounded.

It is not yet an analytic theorem about which frequencies are structurally principal. A future analytic layer must select principal frequencies from arithmetic structure before observing the data, for example by denominator, major-arc geometry, or character decomposition.

## 7. Classification

- Reduced-modulus equivalence: `PROVED`.
- Reduced Fourier inversion: `PROVED`.
- Principal/tail split: `PROVED`.
- Tail absolute-value bound: `PROVED`.
- Prime-channel sufficient condition: `PROVED`.
- Largest-magnitude frequency selection: `COMPUTATIONAL DIAGNOSTIC`.
- Major/minor frequency theory: `OPEN`.
- Goldbach theorem: `NOT CLAIMED`.
