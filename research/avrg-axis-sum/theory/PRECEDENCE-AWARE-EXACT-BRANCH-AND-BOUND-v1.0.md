# ACTIVE-003-N — Precedence-Aware Exact Branch-and-Bound

**Version:** v1.0  
**Status:** exact optimization theory / computationally testable  
**Scope:** frequency-subset optimization for certified reduced difference channels  
**Non-claims:** no polynomial-time claim; no Goldbach proof; no RH/GRH progress.

## 1. Optimization problem

For a reduced modulus `q`, let `K` be the set of paired nonzero Fourier frequencies retained as selectable candidates. For each `k in K` and channel `c`, define the nonnegative gain

\[
G_k(c)=P_k(c)+|P_k(c)|\ge 0.
\]

Let

\[
L_\varnothing(c)=\frac{R_\Lambda(N)}q+P_{\mathrm{Nyq}}(c)-\sum_{k\in K}|P_k(c)|
\]

and let `C(c)` denote the certified local higher-prime-power contamination bound. Then

\[
L_S(c)=L_\varnothing(c)+\sum_{k\in S}G_k(c),
\qquad
F(S)=\#\{c:L_S(c)>C(c)\}.
\]

For a budget `B`, the exact problem is

\[
\max\{F(S):S\subseteq K,\ |S|=B\}.
\]

Because every `G_k(c)` is nonnegative, the at-most-`B` and exact-`B` formulations have the same optimum whenever `B\le |K|`: a smaller feasible set can be padded without decreasing `F`.

## 2. Dominance and precedence

A frequency `i` dominates `j` when

\[
G_i(c)\ge G_j(c)
\]

for every channel `c`. The replacement theorem from ACTIVE-003-M implies that some optimum satisfies

\[
j\in S\Longrightarrow i\in S.
\]

Thus dominance is encoded as a prerequisite edge

\[
i\to j,
\]

meaning that selecting `j` requires selecting `i`.

### 2.1 Equal-gain cycles

The raw non-strict relation can contain cycles when `G_i=G_j` channelwise. Such cycles do not represent strict informational dependence; they represent interchangeable candidates. Before search, equal-gain classes are canonically oriented by frequency index: within one equality class, the smaller index is made prerequisite for the larger index. Strict dominance edges are retained in full.

This produces an acyclic canonical precedence relation while preserving at least one optimum from every equality class.

## 3. Transitive closure

Let `Anc(j)` be the transitive set of prerequisites of `j`, and let `Desc(i)` be the transitive set of candidates requiring `i`. They are computed once before the search.

The closure laws are

\[
j\in S\Longrightarrow Anc(j)\subseteq S,
\]

and, contrapositively,

\[
i\notin S\Longrightarrow Desc(i)\cap S=\varnothing.
\]

The second rule is the exact formalization of: if a prerequisite is excluded, every dependent candidate must also be excluded.

## 4. Search state and propagation

A node is represented by two disjoint sets

\[
(I,E),
\]

where `I` is included and `E` is excluded. The undecided set is

\[
U=K\setminus(I\cup E).
\]

Closure propagation replaces the state by

\[
I^+=I\cup\bigcup_{j\in I}Anc(j),
\]

\[
E^+=E\cup\bigcup_{i\in E}Desc(i),
\]

repeated until stable.

A node is infeasible if

\[
I^+\cap E^+\ne\varnothing,
\]

or

\[
|I^+|>B,
\]

or

\[
|I^+|+|U^+|<B.
\]

These tests are exact, not heuristic.

## 5. Optimistic channelwise upper bound

Let

\[
t=B-|I|
\]

be the number of remaining slots. For each channel `c`, let `U_t(c;U)` be the sum of the largest `t` values among

\[
\{G_k(c):k\in U\}.
\]

Define

\[
UB(I,U,t)=\#\left\{c:
L_I(c)+U_t(c;U)>C(c)
\right\}.
\]

The bound deliberately ignores precedence compatibility among the chosen optimistic gains. Therefore it can overestimate what is jointly attainable, but it cannot underestimate it.

### Lemma 5.1 — Validity of the upper bound

For every feasible completion `T subseteq U` with `|T|=t`,

\[
F(I\cup T)\le UB(I,U,t).
\]

**Proof.** For each channel `c`, the sum contributed by any `t` candidates is at most the sum of the `t` largest channelwise gains. Hence

\[
L_{I\cup T}(c)\le L_I(c)+U_t(c;U).
\]

Every channel certified by `I union T` is therefore counted by `UB`. Counting channels proves the claim. ∎

## 6. Exact precedence-aware branch-and-bound

At each stable node:

1. apply transitive closure propagation;
2. prune infeasible nodes;
3. compute `UB(I,U,B-|I|)`;
4. prune if the upper bound is no larger than the incumbent value;
5. if `|I|=B`, evaluate `F(I)` exactly;
6. otherwise branch on an undecided candidate `k`:
   - include branch: `(I union {k}, E)`;
   - exclude branch: `(I, E union {k})`.

The implementation may prefer a candidate with many descendants, because excluding it can force several exclusions. This is a branching heuristic only; exactness does not depend on it.

### Theorem 6.1 — Soundness

Every set returned by the algorithm satisfies the budget and all precedence constraints.

**Proof.** Every evaluated leaf is closure-stable. Closure stability gives `Anc(j) subseteq I` for each selected `j`; feasibility gives `|I|=B`. ∎

### Theorem 6.2 — Optimality

The algorithm returns the same optimal value as exhaustive enumeration over all budget-`B` subsets.

**Proof.** A branch is removed only in one of two ways.

- A propagation/feasibility prune removes a state with no precedence-feasible budget-`B` completion.
- An upper-bound prune removes a state whose every completion has value at most the incumbent, by Lemma 5.1.

Thus no branch containing a strictly better feasible solution is removed. Since every unpruned binary decision path reaches a feasible leaf, the best evaluated leaf is globally optimal. ∎

## 7. False-certificate audit

The optimization layer only chooses which rigorously reconstructed Fourier contributions are retained. A reported channel must still satisfy

\[
L_S(c)>C_{\mathrm{hpp}}(c).
\]

The verifier independently reconstructs prime-prime channel mass and checks that every certified channel has positive prime-prime mass. This is a finite computational audit of the local sufficient certificate, not a proof for all even integers.

## 8. Complexity boundary

The method remains an exact exponential search in the worst case. Transitive closure and propagation can reduce the explored tree, sometimes substantially, but no polynomial-time complexity claim is made. In instances with weak or absent dominance relations, the precedence-aware tree may be close to the ordinary branch-and-bound tree, and branching-order effects can even offset some savings.

## 9. Scientific classification

- `G_i >= G_j` replacement rule: proved exact optimization theorem.
- precedence closure and propagation: exact combinatorial consequence.
- channelwise `UB`: rigorous optimistic upper bound.
- branch-and-bound optimality: exact finite-search theorem.
- numerical reductions: empirical properties of the tested domain only.
- relation to Goldbach: local sufficient certificates for tested `N`; no general Goldbach result.
- RH/GRH: no claim and no dependency.