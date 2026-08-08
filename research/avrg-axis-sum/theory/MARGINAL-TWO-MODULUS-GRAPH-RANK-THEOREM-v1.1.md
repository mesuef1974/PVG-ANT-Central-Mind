# Marginal Two-Modulus Graph Rank Theorem — v1.1

Status: `PROVED THEOREM`

Research phase: `ACTIVE-RESEARCH-v1.1`

## 1. Setup

Fix \(N\ge2\), write \(n=N-1\), and let \(r,s\ge1\). Define

\[
q_r=\frac r{\gcd(2,r)},
\qquad
q_s=\frac s{\gcd(2,s)}.
\]

Let

\[
M_{N;(r,s)}
=
\begin{pmatrix}
D_{N,r}\\
D_{N,s}
\end{pmatrix}
:\mathbb C^n\longrightarrow\mathbb C^{r+s}.
\]

Deleting zero rows and merging the harmless affine relabeling induced by \(2a-N\), the two channel blocks are equivalent to grouping the indices \(a=1,\dots,n\) by their residue classes modulo \(q_r\) and \(q_s\).

## 2. Associated bipartite multigraph

Define a bipartite multigraph

\[
G_{N;r,s}=(U\sqcup V,E)
\]

as follows.

- \(U\) is the set of residue classes modulo \(q_r\) met by \(1,\dots,n\).
- \(V\) is the set of residue classes modulo \(q_s\) met by \(1,\dots,n\).
- For each index \(a\in\{1,\dots,n\}\), introduce an edge \(e_a\) joining
  \[
  a\pmod{q_r}
  \quad\text{to}\quad
  a\pmod{q_s}.
  \]

Parallel edges are allowed.

Let

\[
v(G)=|U|+|V|
\]

and let \(c(G)\) denote the number of connected components containing at least one edge.

## 3. Theorem

### Theorem 3.1 (exact two-modulus marginal rank)

Over \(\mathbb C\),

\[
\boxed{
\operatorname{rank}M_{N;(r,s)}
=
|U|+|V|-c(G_{N;r,s}).
}
\]

Equivalently,

\[
\dim\ker M_{N;(r,s)}
=
(N-1)-|U|-|V|+c(G_{N;r,s}).
\]

## 4. Proof

After deleting zero rows and reordering the remaining rows, every column indexed by \(a\) contains exactly two entries equal to \(1\): one in the row \(a\bmod q_r\) and one in the row \(a\bmod q_s\). Therefore the resulting matrix is the unsigned vertex-edge incidence matrix \(B(G_{N;r,s})\) of the bipartite multigraph.

It remains to compute the rank of an unsigned incidence matrix of a bipartite graph over a field of characteristic different from \(2\).

Orient every edge from \(U\) to \(V\), and let \(C(G)\) be the resulting signed incidence matrix: each column has \(+1\) at its \(U\)-endpoint and \(-1\) at its \(V\)-endpoint. Multiplying every row indexed by \(V\) by \(-1\) transforms \(C(G)\) into \(B(G)\). Hence

\[
\operatorname{rank}B(G)=\operatorname{rank}C(G).
\]

For a graph with \(v(G)\) vertices and \(c(G)\) edge-containing connected components, the signed incidence matrix has rank

\[
v(G)-c(G).
\]

Indeed, on each connected component the sum of all signed vertex rows is zero, giving one row dependence; choosing a spanning tree in that component gives \(v_i-1\) independent incidence columns, so there are no further dependencies. Summing over components yields

\[
\operatorname{rank}C(G)=\sum_i(v_i-1)=v(G)-c(G).
\]

Therefore

\[
\operatorname{rank}M_{N;(r,s)}=|U|+|V|-c(G_{N;r,s}).
\]

The kernel formula follows from rank-nullity. ∎

## 5. Full-period corollary

Let

\[
L=\operatorname{lcm}(q_r,q_s),
\qquad
g=\gcd(q_r,q_s).
\]

### Corollary 5.1 (rank after one complete residue period)

If

\[
N-1\ge L,
\]

then every residue class modulo \(q_r\) and \(q_s\) is used, and the graph has exactly \(g\) connected components. Consequently,

\[
\boxed{
\operatorname{rank}M_{N;(r,s)}
=q_r+q_s-g.
}
\]

#### Proof

During any \(L\) consecutive indices, the Chinese remainder theorem realizes every compatible pair

\[
(u,v)\in\mathbb Z/q_r\mathbb Z\times\mathbb Z/q_s\mathbb Z,
\qquad
u\equiv v\pmod g,
\]

exactly once. For each residue \(t\pmod g\), the vertices congruent to \(t\) form a complete bipartite connected component. Different \(t\)'s cannot be connected. Thus there are exactly \(g\) components, and Theorem 3.1 gives the formula. ∎

## 6. Consequences

1. Separate marginal channels are generally weaker than the coupled joint-signature operator.
2. The loss of information is controlled by graph cycles and parallel edges.
3. A vector in the kernel is an edge weighting whose signed sum at every graph vertex is zero.
4. For two moduli, the marginal rank problem is reduced exactly to finite graph connectivity.

## 7. Example

Take

\[
N=10,\qquad (r,s)=(3,5).
\]

Then

\[
q_r=3,\qquad q_s=5,\qquad L=15.
\]

Since \(N-1=9<L\), the full-period corollary does not apply. The graph has \(3+5=8\) used vertices and is connected, so

\[
\operatorname{rank}M_{10;(3,5)}=8-1=7.
\]

By contrast, the coupled joint-signature operator satisfies

\[
\operatorname{rank}J_{10;(3,5)}=9.
\]

Thus this example exhibits the precise distinction

\[
\text{separate marginals}\neq\text{coupled signatures}.
\]

## 8. Scientific classification

- The graph construction is an exact representation of the defined matrix.
- The rank formula is proved.
- No claim is made about Goldbach, prime production, RH, or GRH.
- Literature priority is not claimed; a targeted incidence-matrix literature check remains required.
