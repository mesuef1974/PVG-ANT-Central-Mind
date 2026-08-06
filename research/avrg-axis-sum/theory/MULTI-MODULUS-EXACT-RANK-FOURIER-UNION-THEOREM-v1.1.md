# Multi-Modulus Exact Rank via Fourier-Subgroup Unions — v1.1

## Status

`PROVED THEOREM`

This unit gives an exact closed formula for the rank of the marginal stacked operator for an arbitrary finite family of moduli. It does not make any new claim about Goldbach, prime distribution, or RH/GRH.

## 1. Setup

Fix \(N\ge2\) and a modulus family

\[
\mathbf r=(r_1,\dots,r_k).
\]

Let

\[
M_{N;\mathbf r}
=
\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_k}
\end{pmatrix},
\qquad
(D_{N,r_j}w)_d
=
\sum_{2a-N\equiv d\pmod{r_j}}w_a.
\]

Define the effective periods

\[
q_j=\frac{r_j}{\gcd(2,r_j)}
\]

and

\[
L=\operatorname{lcm}(q_1,\dots,q_k).
\]

The constant shift \(-N\) does not affect rank. Moreover,

\[
2a\equiv2b\pmod{r_j}
\iff
a\equiv b\pmod{q_j}.
\]

Hence the row space contributed by modulus \(r_j\) is the space of functions of the index \(a\) that depend only on \(a\bmod q_j\).

## 2. Fourier subgroups

Let \(\widehat{\mathbb Z/L\mathbb Z}\cong\mathbb Z/L\mathbb Z\). For each \(q_j\mid L\), define

\[
H_j
=
\left\{m\in\mathbb Z/L\mathbb Z:
 m\equiv0\pmod{L/q_j}
\right\}.
\]

Then \(|H_j|=q_j\).

A function on \(\mathbb Z/L\mathbb Z\) depends only on the residue modulo \(q_j\) if and only if its Fourier support is contained in \(H_j\). Therefore the sum of the marginal row spaces over one full period has Fourier support

\[
H=\bigcup_{j=1}^k H_j.
\]

Consequently, over a full period, the marginal row-space dimension is \(|H|\).

## 3. Exact finite-fiber rank theorem

### Theorem 3.1

For every \(N\ge2\) and every finite modulus family \(\mathbf r\),

\[
\boxed{
\operatorname{rank}M_{N;\mathbf r}
=
\min\!\left(N-1,\left|\bigcup_{j=1}^k H_j\right|\right).
}
\]

### Proof

Let \(n=N-1\). By Fourier inversion on \(\mathbb Z/L\mathbb Z\), the full-period marginal row space is spanned by the characters

\[
\chi_m(a)=e^{2\pi i ma/L},
\qquad m\in H.
\]

Restrict these characters to the consecutive indices \(a=1,\dots,n\). The resulting evaluation matrix has entries

\[
\chi_m(a)=z_m^a,
\qquad z_m=e^{2\pi i m/L},
\]

with distinct nodes \(z_m\) for distinct \(m\in H\). Every square submatrix formed from the first \(s\) consecutive powers and any \(s\) distinct nodes is a Vandermonde matrix and is nonsingular. Hence the restricted character family has rank

\[
\min(n,|H|).
\]

This restricted character span is exactly the row space of \(M_{N;\mathbf r}\), so

\[
\operatorname{rank}M_{N;\mathbf r}
=
\min(N-1,|H|).
\]

## 4. Inclusion-exclusion closed form

For every nonempty subset \(S\subseteq\{1,\dots,k\}\),

\[
\left|\bigcap_{j\in S}H_j\right|
=
\gcd(q_j:j\in S).
\]

Indeed, the intersection consists of multiples of

\[
\operatorname{lcm}\left(\frac L{q_j}:j\in S\right)
=
\frac L{\gcd(q_j:j\in S)}.
\]

Therefore inclusion-exclusion gives

\[
\boxed{
\left|\bigcup_{j=1}^k H_j\right|
=
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{|S|+1}
\gcd(q_j:j\in S).
}
\]

Thus

\[
\boxed{
\operatorname{rank}M_{N;\mathbf r}
=
\min\!\left(
N-1,
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{|S|+1}
\gcd(q_j:j\in S)
\right).
}
\]

## 5. Three-modulus specialization

For \(k=3\),

\[
\boxed{
\operatorname{rank}M_{N;(r_1,r_2,r_3)}
=
\min\!\Bigl(
N-1,
q_1+q_2+q_3
-\gcd(q_1,q_2)
-\gcd(q_1,q_3)
-\gcd(q_2,q_3)
+\gcd(q_1,q_2,q_3)
\Bigr).
}
\]

## 6. Recovery criterion

### Corollary 6.1

The marginal operator is injective exactly when

\[
N-1
\le
\left|\bigcup_{j=1}^kH_j\right|.
\]

Equivalently,

\[
\boxed{
M_{N;\mathbf r}\text{ injective}
\iff
N-1
\le
\sum_{\varnothing\ne S\subseteq[k]}
(-1)^{|S|+1}
\gcd(q_j:j\in S).
}
\]

## 7. Comparison with the joint-signature operator

The joint-signature operator satisfies

\[
\operatorname{rank}J_{N;\mathbf r}
=
\min(N-1,L).
\]

Hence the exact rank gap is

\[
\boxed{
\operatorname{rank}J_{N;\mathbf r}
-
\operatorname{rank}M_{N;\mathbf r}
=
\min(N-1,L)
-
\min(N-1,|H|).
}
\]

In the full-period range \(N-1\ge L\),

\[
\boxed{
\operatorname{rank}J_{N;\mathbf r}
-
\operatorname{rank}M_{N;\mathbf r}
=
L-|H|.
}
\]

## 8. Redundant moduli

If \(q_i\mid q_j\), then

\[
H_i\subseteq H_j.
\]

Therefore adding modulus \(r_i\) to a family already containing \(r_j\) does not increase marginal rank.

More generally, a new modulus increases rank exactly by the number of new Fourier frequencies it contributes:

\[
\Delta\operatorname{rank}
=
\min(N-1,|H\cup H_{\mathrm{new}}|)
-
\min(N-1,|H|).
\]

## 9. Classification

- Fourier-subgroup representation: `PROVED`.
- Exact arbitrary-family rank formula: `PROVED`.
- Inclusion-exclusion gcd formula: `PROVED`.
- Exact injectivity criterion: `PROVED`.
- Exact marginal/joint rank gap: `PROVED`.
- Novelty or priority: `NOT AUTHORIZED` pending deeper literature review.
