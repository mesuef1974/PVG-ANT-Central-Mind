# ACTIVE-003-O — Precedence-Closure-Ratio Branch Ordering

## Status

Exact algorithmic refinement of `ACTIVE-003-N`. This unit changes only the
branching order inside precedence-aware exact branch-and-bound. It does not
change the objective, the local prime-power contamination certificate, or the
optimistic upper bound.

## 1. Setting

For paired reduced Fourier frequencies `k` define the nonnegative gain vector

\[
G_k(c)=P_k(c)+|P_k(c)|.
\]

For a selected set `S`,

\[
L_S(c)=L_\varnothing(c)+\sum_{k\in S}G_k(c),
\qquad
F(S)=\#\{c:L_S(c)>C_{\mathrm{hpp}}(c)\}.
\]

A precedence relation `i \succcurlyeq j` means

\[
G_i(c)\ge G_j(c)\quad\text{for every channel }c.
\]

After canonical orientation of exact equal-gain classes and transitive closure,
let

\[
A(k)=\{i:i\text{ is an ancestor of }k\},
\qquad
D(k)=\{j:k\text{ is an ancestor of }j\}.
\]

At a search node `(S,E)` the selected frequencies are `S`, the excluded
frequencies are `E`, and all other frequencies are undecided.

## 2. Closure propagation

The exact logical closure is

\[
\operatorname{Incl}(S)=S\cup\bigcup_{k\in S}A(k),
\]

\[
\operatorname{Excl}(E)=E\cup\bigcup_{k\in E}D(k).
\]

A node is infeasible when the two closures intersect or when the inclusion
closure exceeds the remaining budget.

These rules are identical to `ACTIVE-003-N`; therefore the correctness theorem
proved there remains applicable.

## 3. Why the previous branch order can lose time

The `ACTIVE-003-N` prototype prioritized a candidate by the tuple

\[
(|D(k)|,|A(k)|,\sum_cG_k(c),-k).
\]

This favors a large descendant set even when selecting `k` forces many
ancestors and consumes several budget slots at once. The propagation is valid,
but the branch can be explored in a poor order, delaying a strong incumbent
and weakening subsequent upper-bound pruning.

The measured result of `ACTIVE-003-N` was therefore scientifically mixed:
exactness was preserved, but aggregate visited nodes rose by about `0.709%`.

## 4. Inclusion-closure cost

At a node with selected set `S`, define the newly forced inclusion cost

\[
\kappa_S(k)
=
\left|\bigl(A(k)\cup\{k\}\bigr)\setminus S\right|.
\]

Since `k` itself is undecided, `\kappa_S(k)\ge1`.

Define total Fourier gain

\[
W(k)=\sum_cG_k(c).
\]

The closure-ratio branch score is

\[
\rho_S(k)=\frac{W(k)}{\kappa_S(k)}.
\]

The next candidate is chosen lexicographically by

\[
\boxed{
\left(
\rho_S(k),
|A(k)|+|D(k)|,
-\kappa_S(k),
-k
\right).
}
\]

Thus the search first tests the largest aggregate gain per budget slot forced
by precedence. Precedence reach and deterministic frequency order are only
tie-breakers.

## 5. Exactness theorem

### Theorem

Replacing the branch-selection rule of `ACTIVE-003-N` by the closure-ratio
score preserves the exact optimum.

### Proof

At every feasible node, the algorithm still creates the same two logical
children:

1. include `k`, followed by inclusion closure;
2. exclude `k`, followed by exclusion closure.

The choice of `k` changes only the order in which the finite canonical search
space is partitioned. No feasible canonical completion is removed except by:

- a contradiction in the precedence closure;
- a budget infeasibility;
- the previously proved optimistic upper bound
  `UB(S,R,t) <= F_best`.

All three cuts are independent of the branching order and were already proved
safe in `ACTIVE-003-N`. Hence the maximum objective value is unchanged. ∎

## 6. What this score does not prove

The ratio is a branching heuristic inside an exact exponential search. It does
not imply:

- polynomial-time complexity;
- uniform improvement on every instance;
- a better mathematical lower bound for any channel;
- a proof of Goldbach;
- progress on RH or GRH.

Its value is empirical and algorithmic: it attempts to make precedence
propagation cooperate with incumbent discovery and upper-bound pruning.

## 7. Verification protocol

The executable verifier compares, for

- `4 <= N <= 120`,
- `3 <= r <= 30`,
- exact budgets `0 <= B <= min(4,m)`,

three solvers:

1. ordinary exact branch-and-bound;
2. the baseline precedence-aware solver from `ACTIVE-003-N`;
3. the closure-ratio precedence-aware solver.

It checks:

- equality of exact optimum values;
- independent absence of false local prime-prime certificates;
- visited nodes;
- leaves;
- optimistic-upper-bound cuts;
- precedence cuts;
- improved, equal, and worse cases relative to the baseline precedence order.

## 8. Honest classification

- dominance replacement theorem: exact;
- precedence closure: exact;
- preservation of the optimum under reordering: exact;
- closure-ratio score: heuristic branch ordering;
- benchmark conclusions: finite computational evidence only;
- Goldbach/RH/GRH claim: none.
