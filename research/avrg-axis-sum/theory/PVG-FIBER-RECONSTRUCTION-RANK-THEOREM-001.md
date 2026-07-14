# PVG Fiber Reconstruction Rank Theorem 001

## Status

- Classification: exact finite-dimensional theorem.
- Scope: ordered positive addition fiber for fixed `N` and modulus `r`.
- No Goldbach proof, no asymptotic claim, and no RH/GRH progress.

## 1. Fiber-weight space

Fix an integer `N >= 2` and write

\[
m=N-1.
\]

For the ordered positive addition fiber

\[
\mathcal F_N^+=\{(a,N-a):1\le a\le N-1\},
\]

let

\[
V_N=\mathbb C^m.
\]

An element `w in V_N` is written

\[
w=(w_1,\ldots,w_m),
\]

where `w_a` is the weight attached to the PVG fiber point

\[
(\nu(a),\nu(N-a)).
\]

## 2. Difference-channel operator

For a modulus `r >= 1`, define

\[
d_r(a)\equiv a-(N-a)=2a-N\pmod r.
\]

The difference-channel operator is

\[
D_{N,r}:V_N\longrightarrow \mathbb C^r,
\]

with coordinates

\[
(D_{N,r}w)_d
=
\sum_{\substack{1\le a\le N-1\\2a-N\equiv d\pmod r}}w_a.
\]

Its matrix has one `1` in each column, in row `d_r(a)`, and zeros elsewhere.

## 3. Exact rank theorem

Let

\[
g=\gcd(2,r),\qquad q=\frac r g.
\]

Then

\[
\boxed{\operatorname{rank}D_{N,r}=\min(N-1,q).}
\]

Consequently,

\[
\boxed{\dim\ker D_{N,r}=(N-1)-\min(N-1,q).}
\]

### Proof

Two columns `a` and `b` of the matrix coincide exactly when

\[
2a-N\equiv2b-N\pmod r,
\]

or equivalently

\[
2(a-b)\equiv0\pmod r.
\]

Writing `r=gq` with `g=gcd(2,r)`, this is equivalent to

\[
a\equiv b\pmod q.
\]

Hence distinct columns are indexed by the residue classes modulo `q` met by the consecutive integers

\[
1,2,\ldots,N-1.
\]

The number of such classes is

\[
\min(N-1,q).
\]

Columns belonging to different classes are distinct standard basis vectors, hence linearly independent. Therefore the rank equals the number of distinct classes, proving the formula. The nullity follows from rank-nullity.

## 4. Odd-modulus corollary

If `r` is odd, then `g=1` and `q=r`. Thus

\[
\boxed{\operatorname{rank}D_{N,r}=\min(N-1,r).}
\]

In particular, if

\[
r\ge N-1,
\]

then

\[
\operatorname{rank}D_{N,r}=N-1,
\]

so `D_{N,r}` is injective.

Therefore all fiber weights are recovered exactly from the difference channels alone.

For each `a`, the unique occupied channel is

\[
d\equiv2a-N\pmod r.
\]

When `r` is odd, let `2^{-1}` denote the inverse of `2 mod r`. Then

\[
a\equiv2^{-1}(d+N)\pmod r.
\]

If `r>=N-1`, this residue identifies the unique `a in {1,...,N-1}` and

\[
\boxed{w_a=(D_{N,r}w)_{2a-N\bmod r}.}
\]

## 5. Fourier-channel corollary

Let `F_r` be the `r x r` discrete Fourier matrix and define

\[
\widehat D_{N,r}=F_rD_{N,r}.
\]

Because `F_r` is invertible,

\[
\boxed{\operatorname{rank}\widehat D_{N,r}=\operatorname{rank}D_{N,r}.}
\]

Thus the complete family of difference Fourier modes has exactly the same information as the channel vector.

For odd `r>=N-1`, the Fourier modes recover the entire fiber weight vector after inverse DFT followed by the explicit channel-to-index map.

## 6. Redundancy of the zero mode

The unweighted additive observable is

\[
L_0(w)=\sum_{a=1}^{N-1}w_a.
\]

But

\[
L_0(w)=\sum_{d\bmod r}(D_{N,r}w)_d=\widehat D_{N,r}(0).
\]

Hence the ordinary convolution row is already the zero Fourier mode of the difference-channel system. It adds no rank when all difference channels or all Fourier modes are present.

## 7. Character rows for odd `r`

For a Dirichlet character `chi mod r`, define

\[
L_\chi(w)=\sum_{a=1}^{N-1}\chi(a)w_a.
\]

If `r` is odd, the map

\[
a\mapsto d_r(a)=2a-N\pmod r
\]

is a bijection of residue classes. Therefore there is a function `c_chi` on difference residues satisfying

\[
\chi(a)=c_\chi(d_r(a)).
\]

Consequently,

\[
L_\chi(w)
=
\sum_{d\bmod r}c_\chi(d)(D_{N,r}w)_d.
\]

Thus every character row lies in the row span of the full difference-channel operator. For odd modulus, adding all Dirichlet-character observables does not increase rank beyond the complete difference-channel system.

This does not make character observables useless: they are structured harmonic combinations adapted to multiplicative residue geometry. It only establishes information-theoretic redundancy when every difference channel is already known.

## 8. Interpretation

The first reconstruction problem has a complete answer:

- information loss is caused exactly by collisions of `a` modulo `r/gcd(2,r)`;
- the kernel consists of redistributions whose sum inside every collision class is zero;
- large odd moduli separate all ordered fiber points;
- the finite Fourier transform changes coordinates but not information;
- the ordinary convolution and character rows are structured projections of the complete channel data.

The genuinely nontrivial research problem is therefore not finite injectivity with unrestricted large modulus. It is reconstruction under constrained observables, such as:

- fixed small moduli;
- only selected characters;
- only low frequencies;
- symmetry-quotiented or unordered fibers;
- prime-supported weights;
- stability and conditioning under noise;
- uniform or asymptotic reconstruction as `N` grows.
