# COF-FOUNDATION-002 — Exact Branch-and-Bound and Precedence Propagation

Status: `validated_foundation`

Version: `v0.1`

## 1. Scope

This note extracts the exact-search layer of the Certificate Optimization Framework (COF) from the Fourier/PVG realization. It separates three logically distinct ingredients:

1. a finite optimization problem and an admissible upper bound;
2. an additive certificate structure that supplies computable bounds;
3. a dominance preorder that supplies canonical precedence propagation.

The correctness of branch-and-bound depends only on admissibility of the bound and exhaustive branching. The additive formula, nonnegative gains, cardinality budget, and precedence relation are sufficient structures used to construct stronger bounds and reduce the canonical search space; they are not required by the abstract pruning theorem itself.

No polynomial-time claim is made.

---

## 2. Finite certificate optimization problem

Let

\[
\mathfrak C=(I,T,\beta,\Gamma,\Theta)
\]

be a finite additive certificate structure, where

- \(I\) is a finite set of decision objects;
- \(T\) is a finite set of targets;
- \(\beta:T\to\mathbb R\) is the baseline;
- \(\Gamma:I\times T\to\mathbb R\) is the contribution map;
- \(\Theta:T\to\mathbb R\) is the certification threshold.

For \(S\subseteq I\), define

\[
L_S(t)=\beta(t)+\sum_{i\in S}\Gamma(i,t),
\]

and

\[
F(S)=\#\{t\in T:L_S(t)>\Theta(t)\}.
\]

Fix an exact cardinality budget \(B\), with \(0\le B\le |I|\). The optimization problem is

\[
\operatorname{OPT}_B
=
\max\{F(S):S\subseteq I,\ |S|=B\}.
\]

The same search formalism works for \(|S|\le B\), but exact cardinality is used here because it matches the verified Fourier-frequency optimization benchmark. If all contributions are nonnegative, then the optimum for \(|S|\le B\) is attained at cardinality \(B\) whenever \(|I|\ge B\).

---

## 3. Search nodes and completions

A search node is a triple

\[
\nu=(S,X,R),
\]

where

- \(S\subseteq I\) is the included set;
- \(X\subseteq I\) is the excluded set;
- \(R=I\setminus(S\cup X)\) is the undecided set;
- \(S\cap X=\varnothing\).

Write

\[
b(\nu)=B-|S|
\]

for the remaining number of selections.

The completion family of \(\nu\) is

\[
\mathcal K_B(\nu)
=
\{S\cup U:U\subseteq R,\ |U|=b(\nu)\}.
\]

The node is cardinality-infeasible if

\[
b(\nu)<0
\quad\text{or}\quad
|R|<b(\nu).
\]

---

## 4. Admissible upper bounds

### Definition 4.1 (Admissibility)

A function \(U\) on search nodes is an admissible upper bound if

\[
F(Q)\le U(\nu)
\]

for every node \(\nu\) and every \(Q\in\mathcal K_B(\nu)\).

Equivalently,

\[
\max_{Q\in\mathcal K_B(\nu)}F(Q)\le U(\nu).
\]

This definition is independent of additivity, nonnegativity, Fourier structure, or precedence.

### Theorem 4.2 (Safe pruning)

Let \(F_{\mathrm{inc}}\) be the value of a currently known feasible incumbent. If

\[
U(\nu)\le F_{\mathrm{inc}},
\]

then deleting the entire subtree rooted at \(\nu\) cannot delete a solution with value larger than the incumbent.

#### Proof

For every completion \(Q\in\mathcal K_B(\nu)\), admissibility gives

\[
F(Q)\le U(\nu)\le F_{\mathrm{inc}}.
\]

Hence no completion below \(\nu\) improves the incumbent. \(\square\)

---

## 5. Exact branch-and-bound theorem

Assume that every nonterminal feasible node chooses some \(k\in R\) and creates the two children

\[
(S\cup\{k\},X,R\setminus\{k\})
\]

and

\[
(S,X\cup\{k\},R\setminus\{k\}).
\]

A terminal node with \(b(\nu)=0\) evaluates \(F(S)\). Cardinality-infeasible nodes are discarded. Nodes satisfying the safe-pruning condition are discarded.

### Theorem 5.1 (Exactness)

For any admissible upper bound \(U\), the branch-and-bound procedure above returns \(\operatorname{OPT}_B\).

#### Proof

Without pruning, repeated include/exclude branching partitions all subsets of \(I\), and every set of cardinality \(B\) appears at exactly one terminal feasible leaf. By Theorem 4.2, every pruned node contains no completion whose value exceeds the incumbent at the time of pruning. Therefore pruning cannot remove every optimal completion before an equally good incumbent exists. The final incumbent consequently has value \(\operatorname{OPT}_B\). \(\square\)

### Dependency statement

Theorem 5.1 requires only:

- finiteness of the feasible search space;
- exhaustive include/exclude branching;
- exact evaluation at terminal feasible leaves;
- admissibility of \(U\).

It does **not** require:

- \(\Gamma(i,t)\ge0\);
- additivity of \(L_S\);
- dominance or precedence;
- a Fourier or PVG realization.

---

## 6. A computable cardinality upper bound

Now assume the additive structure and nonnegative contributions:

\[
\Gamma(i,t)\ge0
\qquad(i\in I,\ t\in T).
\]

For a node \(\nu=(S,X,R)\), let \(b=b(\nu)\). For each target \(t\), let

\[
M_b(t;R)
\]

be the sum of the \(b\) largest values in

\[
\{\Gamma(i,t):i\in R\},
\]

with \(M_b=-\infty\) for a cardinality-infeasible node.

Define

\[
U_{\mathrm{coord}}(\nu)
=
\#\left\{
 t\in T:
 L_S(t)+M_b(t;R)>\Theta(t)
\right\}.
\]

### Proposition 6.1 (Coordinatewise optimistic admissibility)

\(U_{\mathrm{coord}}\) is admissible.

#### Proof

Let \(Q=S\cup V\in\mathcal K_B(\nu)\), so \(V\subseteq R\) and \(|V|=b\). For each target \(t\),

\[
L_Q(t)
=
L_S(t)+\sum_{i\in V}\Gamma(i,t)
\le
L_S(t)+M_b(t;R).
\]

Therefore a target certified by \(Q\) is counted by \(U_{\mathrm{coord}}(\nu)\). Counting such targets proves

\[
F(Q)\le U_{\mathrm{coord}}(\nu).
\]

\(\square\)

### Remark 6.2

This upper bound is optimistic because a different size-\(b\) subset may maximize each target separately. The independently optimized target gains need not be simultaneously realizable. That looseness motivates compatibility graphs, hypergraphs, and minimal forbidden hyperedges.

---

## 7. Dominance and canonical precedence

Define coordinatewise dominance by

\[
i\succeq j
\quad\Longleftrightarrow\quad
\Gamma(i,t)\ge\Gamma(j,t)
\quad\text{for every }t\in T.
\]

Exact equality classes must be canonically oriented to avoid directed cycles. After quotienting equal contribution vectors, or after imposing a deterministic acyclic orientation inside each equality class, write

\[
i\succcurlyeq_c j
\]

for the resulting acyclic precedence relation.

The exchange theorem from COF-FOUNDATION-001 implies that an optimal cardinality-\(B\) configuration exists that is downward closed with respect to the convention

\[
j\in S,\ i\succcurlyeq_c j
\Longrightarrow i\in S.
\]

In words: selecting a dominated object requires selecting every canonical dominator.

Let

\[
A(j)=\{i\in I:i\succcurlyeq_c j\}
\]

be the transitive ancestor set, and

\[
D(i)=\{j\in I:i\succcurlyeq_c j\}
\]

be the transitive descendant set.

---

## 8. Precedence propagation

For a node \((S,X,R)\), define the propagated sets

\[
S^+
=
S\cup\bigcup_{j\in S}A(j),
\]

and

\[
X^+
=
X\cup\bigcup_{i\in X}D(i).
\]

The second rule is the contrapositive of canonical precedence: if a required dominator is excluded, every object requiring it must also be excluded.

### Proposition 8.1 (Propagation soundness)

Every canonical feasible completion of \((S,X,R)\) includes \(S^+\) and excludes \(X^+\).

#### Proof

If a canonical completion contains \(j\in S\), it contains every \(i\in A(j)\), proving inclusion of \(S^+\). If it excluded \(i\in X\) but contained some \(j\in D(i)\), canonical precedence would require inclusion of \(i\), a contradiction. Hence every descendant in \(D(i)\) is excluded. \(\square\)

### Corollary 8.2 (Contradiction pruning)

If

\[
S^+\cap X^+\ne\varnothing,
\]

then the node has no canonical feasible completion and may be pruned.

### Corollary 8.3 (Budget pruning after propagation)

If

\[
|S^+|>B
\]

or

\[
|I\setminus(S^+\cup X^+)|<B-|S^+|,
\]

then the node has no canonical cardinality-\(B\) completion.

---

## 9. Exactness of precedence-aware search

### Theorem 9.1

Suppose the canonical exchange property holds: for every feasible configuration of cardinality \(B\), there exists a canonical configuration of cardinality \(B\) with at least as large objective value. Then branch-and-bound restricted by the propagation rules of Section 8 still returns \(\operatorname{OPT}_B\).

#### Proof

The exchange property guarantees that at least one optimal configuration belongs to the canonical feasible family. Proposition 8.1 and its corollaries prune only nodes with no canonical completion. The remaining include/exclude branching enumerates every canonical cardinality-\(B\) configuration unless safely removed by an admissible upper bound. Theorem 5.1 applied to this restricted family therefore returns the canonical optimum, which equals the unrestricted optimum. \(\square\)

### Important limit

Precedence-aware exactness does not justify deleting dominated objects from the ground set. A dominated object may coexist with its dominator in an optimal solution. Precedence restricts the shape of a canonical optimum; it is not a global elimination rule.

---

## 10. Dependency matrix

| Result | Finite search | Admissible UB | Additive \(L\) | Nonnegative \(\Gamma\) | Exact budget | Dominance/exchange |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Safe pruning | yes | yes | no | no | no | no |
| Abstract BnB exactness | yes | yes | no | no | cardinality only for this tree | no |
| Coordinatewise optimistic UB | yes | constructed | yes | used for monotone gain interpretation | yes | no |
| Canonical precedence existence | yes | no | yes | no | exchange preserves size | yes |
| Inclusion propagation | yes | no | no | no | no | yes |
| Exclusion propagation | yes | no | no | no | no | yes |
| Precedence-aware BnB exactness | yes | yes | only through exchange realization | no | yes | yes |

---

## 11. Realization in Fourier certificate selection

For the reduced Fourier-frequency problem,

\[
I=\{\text{retained paired frequencies}\},
\qquad
T=\{\text{reduced residue channels}\},
\]

\[
\Gamma(k,c)=G_k(c)=P_k(c)+|P_k(c)|\ge0,
\]

and

\[
\beta(c)
=
\frac{R_\Lambda(N)}q
+P_{\mathrm{Nyq}}(c)
-\sum_k|P_k(c)|.
\]

Thus

\[
L_S(c)=\beta(c)+\sum_{k\in S}G_k(c).
\]

The exact frequency budget is \(|S|=B\), the coordinatewise optimistic bound is the original exact-search upper bound, and coordinatewise frequency dominance realizes the canonical precedence relation.

Consequently, the previously verified Fourier/PVG branch-and-bound is an exact realization of the abstract COF results in this note.

---

## 12. Classification and limits

Classification:

- additive certificate structure: definition;
- admissible-bound pruning: proved abstractly;
- branch-and-bound exactness: proved abstractly;
- coordinatewise optimistic bound: proved for additive cardinality-budget structures;
- precedence propagation: proved under canonical exchange;
- Fourier/PVG mapping: exact realization.

Not claimed:

- polynomial-time complexity;
- universal speedup from precedence;
- validity under arbitrary nonlinear constraints without new hypotheses;
- completion of a general COF theory;
- a proof of Goldbach;
- progress on RH or GRH.

## 13. Next foundation unit

`COF-FOUNDATION-003` should abstract certification margins, mandatory object closures, compatibility hypergraphs, and minimal forbidden hyperedges, while explicitly separating exact combinatorial statements from implementation heuristics.