# Marginal Two-Modulus Spectrum and Conditioning — v1.1

Status: `PROVED THEOREM UNIT`

Scientific scope: exact finite-dimensional linear algebra for the marginal stacked operator. No Goldbach, sieve, circle-method, RH, GRH, novelty, or priority claim is made.

## 1. Setup

Fix \(N\ge2\) and two moduli \(r,s\ge1\). Let

\[
M_{N;(r,s)}=
\begin{pmatrix}
D_{N,r}\\
D_{N,s}
\end{pmatrix}.
\]

Let \(G_{N;r,s}\) be the bipartite residue-coupling multigraph used in the rank and kernel units:

- left vertices are the realized \(r\)-channels;
- right vertices are the realized \(s\)-channels;
- every index \(a\in\{1,\dots,N-1\}\) contributes one edge joining its two residue channels.

Parallel edges are retained. With rows indexed by vertices and columns by edges, \(M_{N;(r,s)}\) is the unsigned vertex-edge incidence matrix \(B_G\).

## 2. Signless-Laplacian identity

### Theorem 2.1

Let \(A_G\) be the adjacency matrix of the bipartite multigraph, counting edge multiplicity, and let \(D_G\) be its diagonal degree matrix. Then

\[
M_{N;(r,s)}M_{N;(r,s)}^{*}
=B_GB_G^{*}
=D_G+A_G
=:Q_G.
\]

Thus the row-side Gram matrix is the signless Laplacian of the residue-coupling multigraph.

### Proof

The diagonal entry at a vertex counts incident edges, hence equals its degree. For two distinct vertices, the corresponding Gram entry counts columns having a \(1\) in both rows, hence counts edges joining those vertices. Vertices on the same bipartition side share no edge. Therefore the Gram matrix is \(D_G+A_G\).

## 3. Reduction to the ordinary graph Laplacian

Let \(S\) be diagonal with value \(+1\) on the left bipartition and \(-1\) on the right. Since \(G\) is bipartite,

\[
S A_G S=-A_G,
\qquad
S D_G S=D_G.
\]

### Corollary 3.1

\[
S Q_G S=D_G-A_G=:L_G.
\]

Hence \(Q_G\) and the ordinary combinatorial Laplacian \(L_G\) are unitarily similar and have the same spectrum.

## 4. Singular values

Write the connected components of \(G\) as \(G_1,\dots,G_c\). For a component with at least one edge, let

\[
0=\lambda_1(G_j)<\lambda_2(G_j)\le\cdots\le\lambda_{|V(G_j)|}(G_j)
\]

be its Laplacian eigenvalues.

### Theorem 4.1

The nonzero singular values of \(M_{N;(r,s)}\) are exactly

\[
\left\{\sqrt{\lambda_k(G_j)}:
1\le j\le c,\ 2\le k\le |V(G_j)|\right\},
\]

with multiplicity.

Equivalently,

\[
\sigma_{\max}(M)^2
=
\max_j\lambda_{\max}(G_j),
\]

and

\[
(\sigma_{\min}^{+}(M))^2
=
\min_j\lambda_2(G_j),
\]

where \(\sigma_{\min}^{+}\) denotes the smallest positive singular value.

### Proof

The squared singular values are the nonzero eigenvalues of \(MM^{*}=Q_G\). By Corollary 3.1 these are the nonzero Laplacian eigenvalues component by component.

### Corollary 4.2 (positive-spectrum condition number)

Define

\[
\kappa^{+}_2(M)
=
\frac{\sigma_{\max}(M)}{\sigma_{\min}^{+}(M)}.
\]

Then

\[
\boxed{
\kappa^{+}_2(M_{N;(r,s)})
=
\sqrt{
\frac{\max_j\lambda_{\max}(G_j)}
{\min_j\lambda_2(G_j)}
}
}.
\]

When \(M\) is injective on its column space — equivalently, when \(G\) is a forest — this is the ordinary spectral condition number of the reconstruction operator.

## 5. Exact full-period decomposition

Define the effective channel periods

\[
q_r=\frac r{\gcd(2,r)},
\qquad
q_s=\frac s{\gcd(2,s)},
\]

and

\[
g=\gcd(q_r,q_s),
\qquad
m=\frac{q_r}{g},
\qquad
n=\frac{q_s}{g},
\qquad
\ell=\operatorname{lcm}(q_r,q_s)=gmn.
\]

Assume that the index interval consists of exactly \(t\ge1\) complete periods:

\[
N-1=t\ell.
\]

Every compatible residue pair occurs exactly \(t\) times.

### Theorem 5.1 (full-period graph structure)

The residue-coupling multigraph is the disjoint union of \(g\) copies of \(K_{m,n}\), with every edge repeated \(t\) times.

### Proof

A left residue and a right residue are compatible exactly when they agree modulo \(g\). Thus the vertices split into \(g\) compatibility classes. Inside each class every one of the \(m\) left residues is compatible with every one of the \(n\) right residues. One full period realizes every compatible pair once; \(t\) periods realize it \(t\) times.

## 6. Exact full-period singular spectrum

The Laplacian spectrum of \(K_{m,n}\) is

\[
0^{(1)},
\quad
(m+n)^{(1)},
\quad
n^{(m-1)},
\quad
m^{(n-1)}.
\]

Repeating each edge \(t\) times multiplies the Laplacian by \(t\).

### Theorem 6.1

For \(N-1=t\ell\), the positive singular values of \(M_{N;(r,s)}\) are

\[
\sqrt{t(m+n)}
\quad\text{with multiplicity }g,
\]

\[
\sqrt{tn}
\quad\text{with multiplicity }g(m-1),
\]

and

\[
\sqrt{tm}
\quad\text{with multiplicity }g(n-1).
\]

Terms with zero multiplicity are omitted.

The column-nullity is

\[
\dim\ker M
=tgmn-g(m+n-1).
\]

### Corollary 6.2 (full-period conditioning)

The scaling factor \(t\) cancels from the condition number.

- If \(m,n\ge2\),
  \[
  \boxed{
  \kappa_2^{+}(M)
  =\sqrt{\frac{m+n}{\min(m,n)}}
  }.
  \]

- If \(m=1<n\),
  \[
  \kappa_2^{+}(M)=\sqrt{n+1}.
  \]

- If \(n=1<m\),
  \[
  \kappa_2^{+}(M)=\sqrt{m+1}.
  \]

- If \(m=n=1\),
  \[
  \kappa_2^{+}(M)=1.
  \]

## 7. Interpretation

The marginal operator loses information through graph cycles, while its noise amplification is governed by graph connectivity:

- the kernel is the alternating cycle space;
- the smallest positive singular value is controlled by the weakest component algebraic connectivity;
- the largest singular value is controlled by the largest component Laplacian eigenvalue;
- in the exact full-period regime, both quantities are explicit.

This creates a precise graph-spectral bridge for marginal residue reconstruction.

## 8. Classification

- incidence representation: proved;
- signless-Laplacian identity: proved;
- Laplacian similarity: proved;
- singular-spectrum formula: proved;
- full-period decomposition: proved;
- full-period exact singular values and conditioning: proved;
- finite computational verification: separate companion unit;
- literature priority: not claimed.
