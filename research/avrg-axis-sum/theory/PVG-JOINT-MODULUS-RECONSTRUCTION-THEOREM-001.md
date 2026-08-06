# Joint Small-Modulus Reconstruction on Addition Fibers

## Status

Proved finite-dimensional theorem.

## 1. Setup

Fix \(N\ge2\) and let

\[
V_N=\mathbb C^{N-1}
\]

with coordinates \(w_a\), \(1\le a\le N-1\).

For moduli \(r_1,\ldots,r_s\ge1\), define

\[
L=\operatorname{lcm}(r_1,\ldots,r_s).
\]

The difference coordinate is

\[
d_N(a)=2a-N.
\]

## 2. Separate marginals versus joint channels

The separate channel operators are

\[
D_{N,r_j}:V_N\to\mathbb C^{r_j}.
\]

Stacking these operators records the marginal histograms modulo each \(r_j\). It does **not** record the joint residue tuple as a separate cell, and therefore should not be confused with a joint histogram.

Define the joint channel operator

\[
J_{N;\mathbf r}:V_N\to
\mathbb C^{\prod_{j=1}^s\mathbb Z/r_j\mathbb Z}
\]

by

\[
(J_{N;\mathbf r}w)_{d_1,\ldots,d_s}
=
\sum_{\substack{1\le a\le N-1\\
2a-N\equiv d_j\pmod{r_j}\ \forall j}}
w_a.
\]

Only compatible tuples occur.

## 3. CRT factorization

### Theorem 3.1 (joint channels equal one lcm channel up to relabeling)

Let \(L=\operatorname{lcm}(r_1,\ldots,r_s)\). The joint channel operator \(J_{N;\mathbf r}\) is equal, after deletion of identically zero incompatible rows and permutation of the remaining rows, to the single-modulus operator

\[
D_{N,L}.
\]

#### Proof

Two integers have the same residue modulo every \(r_j\) if and only if they have the same residue modulo \(L\). Therefore the equivalence relation on fiber indices induced by the tuple

\[
(2a-N\bmod r_1,\ldots,2a-N\bmod r_s)
\]

is exactly the equivalence relation induced by

\[
2a-N\bmod L.
\]

The nonempty tuple cells and the nonempty \(L\)-residue cells are therefore in bijection, with identical accumulated weights.

### Corollary 3.2 (exact joint rank)

\[
\boxed{
\operatorname{rank}J_{N;\mathbf r}
=
\min\!\left(N-1,\frac{L}{\gcd(2,L)}\right).
}
\]

#### Proof

Apply Theorem 3.1 and the single-modulus rank theorem.

### Corollary 3.3 (joint reconstruction criterion)

The joint small-modulus channels recover every \(w\in V_N\) if and only if

\[
\frac{L}{\gcd(2,L)}\ge N-1.
\]

In particular, if all \(r_j\) are odd, complete reconstruction holds exactly when

\[
L\ge N-1.
\]

## 4. Consequence for measurement design

A collection of individually small odd moduli can achieve exact reconstruction through their **joint** residue signatures once their least common multiple reaches \(N-1\).

For example, pairwise coprime odd moduli \(r_1,\ldots,r_s\) have

\[
L=\prod_{j=1}^s r_j.
\]

Thus a logarithmic number of bounded-size or slowly growing moduli may create at least \(N-1\) joint cells. This does not contradict the scalar measurement lower bound: the full joint histogram is vector-valued and can contain at least \(N-1\) scalar coordinates.

## 5. Important distinction

The theorem does **not** state that the stacked marginals

\[
(D_{N,r_1}w,\ldots,D_{N,r_s}w)
\]

have the same rank as the joint operator. Marginals may lose interaction information between residue coordinates.

This produces two separate research problems:

1. **Joint-channel design:** solved at the rank level by the lcm criterion.
2. **Marginal-channel design:** determine the rank and kernel of the vertically stacked matrix
   \[
   \begin{pmatrix}
   D_{N,r_1}\\
   \vdots\\
   D_{N,r_s}
   \end{pmatrix}.
   \]

The second problem is structurally nontrivial and is the next target.

## 6. Conditioning

After removing zero rows and ordering occupied cells, an injective joint channel matrix is a column-permuted identity matrix. Therefore all nonzero singular values equal \(1\), and

\[
\kappa_2(J_{N;\mathbf r})=1
\]

whenever the joint operator is injective.

Thus exact joint-cell observation is perfectly conditioned. Instability can arise when:

- only marginals are observed;
- frequencies are truncated;
- channels are aggregated;
- weights are measured with nonuniform normalization;
- or the allowed observables are restricted to characters or low frequencies.

## 7. Classification

- The CRT/lcm equivalence is an exact finite identity.
- The rank and injectivity criteria are proved consequences.
- No claim of literature priority is made.
- No conclusion about Goldbach follows from the theorem alone.
