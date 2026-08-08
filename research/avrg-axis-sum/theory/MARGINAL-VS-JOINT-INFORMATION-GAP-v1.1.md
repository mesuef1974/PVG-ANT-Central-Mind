# Marginal versus Joint Information Gap — v1.1

Status: **proved theorem unit** under `ACTIVE-RESEARCH-v1.1`.

## 1. Setup

Fix `N >= 2` and two moduli `r,s >= 1`. Put

\[
q_r=\frac{r}{\gcd(2,r)},\qquad q_s=\frac{s}{\gcd(2,s)}.
\]

Let

\[
M_{N;(r,s)}=
\begin{pmatrix}
D_{N,r}\\
D_{N,s}
\end{pmatrix}
\]

be the marginal stacked operator, and let

\[
J_{N;(r,s)}:V_N\longrightarrow \mathbb C^{\Sigma_{N;r,s}}
\]

be the coupled joint-signature operator, where

\[
\Sigma_{N;r,s}
=
\left\{
\bigl(2a-N\bmod r,\,2a-N\bmod s\bigr):1\le a\le N-1
\right\}.
\]

The distinction is essential:

- `J` records the total weight in each realized joint residue cell;
- `M` records only the two separate marginal totals.

## 2. Joint-cell graph

Define the simple bipartite graph

\[
H_{N;r,s}=(U\sqcup V,E)
\]

as follows:

- `U` is the set of realized residues modulo `r`;
- `V` is the set of realized residues modulo `s`;
- each distinct joint signature `(u,v) in Sigma_{N;r,s}` gives one edge joining `u` to `v`.

There is one edge per **distinct joint cell**, not one edge per fiber index. Thus repeated indices with the same joint signature are merged at this stage.

Let

\[
B_H:\mathbb C^{E}\longrightarrow\mathbb C^{U\sqcup V}
\]

be the unsigned vertex-edge incidence operator of `H`.

## 3. Factorization theorem

### Theorem 3.1

The marginal operator factors through the joint operator:

\[
\boxed{M_{N;(r,s)}=B_HJ_{N;(r,s)}.}
\]

### Proof

For a joint-cell weight vector `z`, the coordinate of `B_H z` at a left residue `u` is the sum of all joint-cell weights incident to `u`. Applied to

\[
z=J_{N;(r,s)}w,
\]

this is exactly the residue total `(D_{N,r}w)_u`. The right coordinates similarly give `D_{N,s}w`. Hence `B_HJ=M`.

## 4. Kernel inclusion and information order

### Corollary 4.1

\[
\boxed{\ker J_{N;(r,s)}\subseteq\ker M_{N;(r,s)}.}
\]

Therefore the coupled joint data are always at least as informative as the two separate marginals.

### Proof

Immediate from `M=B_HJ`.

The inclusion can be strict. A vector in `ker J` redistributes weight only among fiber indices lying in the same joint cell. A vector in `ker M` may additionally move mass around alternating cycles of distinct joint cells while preserving both marginals.

## 5. Exact quotient theorem

Because every realized joint cell is nonempty, `J` is surjective onto `C^E`: for each edge choose one fiber index in that cell and place the desired edge weight there.

### Theorem 5.1

There is a natural vector-space isomorphism

\[
\boxed{
\ker M_{N;(r,s)}\big/\ker J_{N;(r,s)}
\cong
\ker B_H.
}
\]

Since `H` is bipartite,

\[
\ker B_H
\]

is its alternating cycle space. Consequently,

\[
\boxed{
\dim\ker M-\dim\ker J
=
|E|-|U|-|V|+c(H),
}
\]

where `c(H)` is the number of connected components.

### Proof

Restrict `J` to `ker M`. The factorization gives

\[
J(\ker M)\subseteq\ker B_H.
\]

Conversely, if `z in ker B_H`, surjectivity of `J` gives `w` with `Jw=z`; then

\[
Mw=B_HJw=B_Hz=0,
\]

so `w in ker M`. Thus the induced map

\[
\ker M\to\ker B_H
\]

is surjective and has kernel exactly `ker J`. The first isomorphism theorem yields the quotient statement. The dimension formula is the cycle-rank formula for a bipartite graph.

## 6. Equality criterion

### Corollary 6.1

The two measurement systems carry exactly the same information if and only if the joint-cell graph is a forest:

\[
\boxed{
\ker M_{N;(r,s)}=\ker J_{N;(r,s)}
\iff
H_{N;r,s}\text{ is a forest}.
}
\]

Equivalently,

\[
\boxed{
\operatorname{rank}M_{N;(r,s)}
=
\operatorname{rank}J_{N;(r,s)}
\iff
H_{N;r,s}\text{ is a forest}.
}
\]

Thus the precise information lost by marginalization is not merely “coupling information” in an informal sense: it is the alternating cycle space of the realized joint-cell graph.

## 7. Rank-gap formula

### Corollary 7.1

\[
\boxed{
\operatorname{rank}J_{N;(r,s)}
-
\operatorname{rank}M_{N;(r,s)}
=
|E|-|U|-|V|+c(H_{N;r,s}).
}
\]

The right-hand side is nonnegative and equals the cyclomatic number of the joint-cell graph.

## 8. Full-period classification

Let

\[
g=\gcd(q_r,q_s),\qquad
m=\frac{q_r}{g},\qquad
n=\frac{q_s}{g}.
\]

Assume a complete effective period is realized:

\[
N-1\ge\operatorname{lcm}(q_r,q_s).
\]

Then the joint-cell graph is the disjoint union of `g` copies of the complete bipartite graph `K_{m,n}`. Hence

\[
\operatorname{rank}J
=
\operatorname{lcm}(q_r,q_s)
=gmn,
\]

while

\[
\operatorname{rank}M
=
q_r+q_s-g
=g(m+n-1).
\]

Therefore

\[
\boxed{
\operatorname{rank}J-\operatorname{rank}M
=
g(m-1)(n-1).
}
\]

### Corollary 8.1

In the full-period regime, marginal and joint data are information-equivalent exactly when

\[
\boxed{m=1\quad\text{or}\quad n=1.}
\]

Equivalently,

\[
\boxed{
q_r\mid q_s
\quad\text{or}\quad
q_s\mid q_r.
}
\]

If neither effective modulus divides the other, every complete period contains genuine cycle information that is visible to `J` and invisible to `M`.

## 9. Interpretation

There are two distinct sources of invisibility:

1. **within-cell invisibility** — indices sharing the same joint signature can exchange weight; this is exactly `ker J`;
2. **between-cell cycle invisibility** — distinct joint cells can exchange alternating weight around cycles; this is the quotient `ker M / ker J`.

The coupled operator removes the second loss but not the first. Full recovery of the original fiber weights still requires injectivity of `J`, governed by the effective least-common-multiple criterion from the v1.0 core.

## 10. Scientific classification

- Factorization `M=B_HJ`: **proved identity**.
- Kernel inclusion: **proved**.
- Quotient/cycle-space theorem: **proved**.
- Equality iff forest: **proved**.
- Full-period divisibility criterion: **proved**.
- No Goldbach, sieve, circle-method, RH, GRH, novelty, or priority claim is made.