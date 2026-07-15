# Multi-Modulus Marginal versus Joint Factorization — v1.1

Status: `PROVED THEOREM UNIT`

## 1. Setup

Fix \(N\ge2\) and a modulus family

\[
\mathbf r=(r_1,\dots,r_k),\qquad k\ge2.
\]

Let

\[
d_{N,r_j}(a)=2a-N\pmod{r_j}
\]

for \(1\le a\le N-1\). Define the realized joint-signature set

\[
\Sigma_{N;\mathbf r}
=
\left\{
(d_{N,r_1}(a),\dots,d_{N,r_k}(a)):
1\le a\le N-1
\right\}.
\]

For each coordinate \(j\), let

\[
U_j
=
\{d_{N,r_j}(a):1\le a\le N-1\}
\subseteq \mathbb Z/r_j\mathbb Z.
\]

Let \(V_N=\mathbb C^{N-1}\).

## 2. Coupled and marginal operators

### Definition 2.1 (joint-signature operator)

Define

\[
J_{N;\mathbf r}:V_N\to\mathbb C^{\Sigma_{N;\mathbf r}}
\]

by

\[
(J_{N;\mathbf r}w)_\eta
=
\sum_{\substack{1\le a\le N-1\\
(d_{N,r_1}(a),\dots,d_{N,r_k}(a))=\eta}}
w_a.
\]

Thus \(J\) records the total weight in every realized full residue cell.

### Definition 2.2 (stacked marginal operator)

Define

\[
M_{N;\mathbf r}
=
\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_k}
\end{pmatrix}.
\]

After deleting unused rows, its codomain is

\[
\bigoplus_{j=1}^k\mathbb C^{U_j}.
\]

### Definition 2.3 (cell-to-marginal incidence operator)

Define

\[
B_{N;\mathbf r}:\mathbb C^{\Sigma_{N;\mathbf r}}
\longrightarrow
\bigoplus_{j=1}^k\mathbb C^{U_j}
\]

by

\[
(B_{N;\mathbf r}x)_{j,u}
=
\sum_{\substack{\eta\in\Sigma_{N;\mathbf r}\\
\eta_j=u}}
x_\eta.
\]

Each column of \(B\) contains exactly one \(1\) in each of the \(k\) coordinate blocks. Equivalently, \(B\) is the vertex-hyperedge incidence matrix of the realized \(k\)-partite \(k\)-uniform signature hypergraph.

## 3. Exact factorization

### Theorem 3.1 (multi-modulus factorization)

\[
\boxed{
M_{N;\mathbf r}
=
B_{N;\mathbf r}J_{N;\mathbf r}
}
\]

#### Proof

For a coordinate block \(j\) and a used residue \(u\in U_j\),

\[
(BJw)_{j,u}
=
\sum_{\substack{\eta\in\Sigma_{N;\mathbf r}\\\eta_j=u}}
(Jw)_\eta.
\]

Expanding \(J\) groups exactly those indices \(a\) satisfying

\[
d_{N,r_j}(a)=u.
\]

Hence

\[
(BJw)_{j,u}
=
\sum_{d_{N,r_j}(a)=u}w_a
=(D_{N,r_j}w)_u.
\]

This holds in every coordinate block.

## 4. Kernel inclusion and exact information quotient

### Proposition 4.1 (joint data dominate marginals)

\[
\boxed{
\ker J_{N;\mathbf r}
\subseteq
\ker M_{N;\mathbf r}
}
\]

#### Proof

Immediate from \(M=BJ\).

### Proposition 4.2 (surjectivity of the joint cell aggregator)

The map

\[
J_{N;\mathbf r}:V_N\to\mathbb C^{\Sigma_{N;\mathbf r}}
\]

is surjective.

#### Proof

For each realized signature cell \(\eta\), choose one index \(a_\eta\) realizing it. Assigning \(w_{a_\eta}=x_\eta\) and all other coordinates zero gives \(Jw=x\).

### Theorem 4.3 (exact information-loss quotient)

There is a canonical vector-space isomorphism

\[
\boxed{
\ker M_{N;\mathbf r}/\ker J_{N;\mathbf r}
\cong
\ker B_{N;\mathbf r}
}
\]

and therefore

\[
\boxed{
\operatorname{rank}J_{N;\mathbf r}
-
\operatorname{rank}M_{N;\mathbf r}
=
\dim\ker B_{N;\mathbf r}
}
\]

or equivalently

\[
\boxed{
\operatorname{rank}M_{N;\mathbf r}
=
\operatorname{rank}B_{N;\mathbf r}.
}
\]

#### Proof

Because \(J\) is surjective and \(M=BJ\), the first isomorphism theorem applied to the induced map from \(\ker M\) through \(J\) identifies

\[
\ker M/\ker J
\]

with

\[
\ker B.
\]

Also \(\operatorname{rank}J=|\Sigma_{N;\mathbf r}|\), so rank-nullity gives the rank-gap identity.

## 5. Equality criterion

### Corollary 5.1 (when marginals contain all joint information)

The following are equivalent:

1. \(\ker M_{N;\mathbf r}=\ker J_{N;\mathbf r}\);
2. \(\operatorname{rank}M_{N;\mathbf r}=\operatorname{rank}J_{N;\mathbf r}\);
3. \(B_{N;\mathbf r}\) is injective;
4. the only cell array \(x=(x_\eta)\) whose every one-coordinate marginal vanishes is \(x=0\).

Thus the exact obstruction is a nonzero realized cell array satisfying

\[
\sum_{\eta:\eta_j=u}x_\eta=0
\]

for every coordinate \(j\) and every used residue \(u\in U_j\).

## 6. Relation to the two-modulus graph theorem

When \(k=2\), the signature hypergraph is an ordinary bipartite graph and \(B\) is its unsigned incidence matrix. Then

\[
\ker B
\]

is the alternating cycle space, recovering the earlier theorem.

When \(k\ge3\), \(B\) is a hypergraph-incidence matrix. Ordinary graph cycles no longer provide a complete description in general. The correct proved object at this stage is the space of zero-one-coordinate-marginal cell arrays.

## 7. Scientific classification

- Factorization \(M=BJ\): **proved theorem**.
- Joint-to-marginal kernel inclusion: **proved proposition**.
- Exact quotient and rank gap: **proved theorem**.
- Hypergraph-cycle closed form for \(k\ge3\): **not claimed**.
- Goldbach, sieve, major/minor-arc, RH, or GRH progress: **none**.
