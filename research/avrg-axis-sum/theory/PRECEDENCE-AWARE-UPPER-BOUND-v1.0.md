# ACTIVE-003-P — Precedence-Aware Upper Bound

## 1. Scope

This unit strengthens the optimistic upper bound used inside exact branch-and-bound by requiring every hypothetical gain set to respect the transitive precedence closure induced by frequency dominance.

The unit is algorithmic and finite-dimensional. It does not prove Goldbach, does not establish polynomial-time complexity, and makes no RH/GRH claim.

## 2. Search state

At a node let

- `S` be the already selected frequencies;
- `X` be the excluded frequencies;
- `R` be the undecided frequencies;
- `t=B-|S|` be the remaining exact-budget slots.

For every frequency `k`, let `A(k)` denote its full transitive ancestor set. Selecting `k` forces

\[
\operatorname{cl}(k)=A(k)\cup\{k\}.
\]

For a set `T`, define

\[
\operatorname{cl}(T)=\bigcup_{k\in T}\operatorname{cl}(k).
\]

A hypothetical completion is feasible at the node only if

\[
\operatorname{cl}(T)\cap X=\varnothing,
\qquad
\left|\operatorname{cl}(T)\setminus S\right|\le t.
\]

## 3. Old channelwise optimistic bound

For channel `c`, the previous bound independently selected the largest `t` gains among undecided frequencies:

\[
U^{\mathrm{old}}_t(c;R)
=
\sum_{\ell=1}^{t}G_{(\ell)}(c),
\]

where the terms are sorted channelwise in decreasing order.

This is valid but may combine frequencies whose precedence closures cannot fit simultaneously inside the remaining budget.

## 4. Precedence-aware channel bound

Define

\[
U^{\mathrm{prec}}_t(c;S,X,R)
=
\max_{T\subseteq R}
\left\{
\sum_{k\in \operatorname{cl}(T)\setminus S}G_k(c):
\operatorname{cl}(T)\cap X=\varnothing,
\left|\operatorname{cl}(T)\setminus S\right|\le t
\right\}.
\]

The corresponding node bound is

\[
UB_{\mathrm{prec}}(S,X,R,t)
=
\#\left\{
c:
L_S(c)+U^{\mathrm{prec}}_t(c;S,X,R)>C(c)
\right\}.
\]

## 5. Validity theorem

### Theorem

For every feasible completion `Q` of the node and every channel `c`,

\[
L_Q(c)
\le
L_S(c)+U^{\mathrm{prec}}_t(c;S,X,R).
\]

Consequently,

\[
F(Q)\le UB_{\mathrm{prec}}(S,X,R,t).
\]

### Proof

Because `Q` is feasible, `Q\setminus S` is closed under all required ancestors relative to `S`, avoids `X`, and uses at most `t` new frequencies. Therefore `T=Q\setminus S` is one of the admissible sets in the maximum defining `U^{prec}`. Its channel gain cannot exceed that maximum. Counting channels whose optimistic value exceeds contamination gives the stated objective upper bound. ∎

## 6. Dominance over the old bound

Every precedence-feasible completion uses at most `t` new frequencies. The old bound maximizes over all channelwise choices of at most `t` undecided gains without enforcing closure. Hence

\[
U^{\mathrm{prec}}_t(c;S,X,R)
\le
U^{\mathrm{old}}_t(c;R)
\]

for every channel, and therefore

\[
UB_{\mathrm{prec}}
\le
UB_{\mathrm{old}}.
\]

The inequality need not be strict at any particular node.

## 7. Exact finite implementation

In the present benchmark, the reduced frequency count is small and the exact budget satisfies `B<=4`. The verifier enumerates candidate subsets of `R`, forms their transitive closure, rejects candidates conflicting with `X` or exceeding the remaining budget, deduplicates equal closures, and maximizes channel gain over the surviving closures.

This is an exact exponential subroutine. No polynomial-time claim is made.

## 8. Verified benchmark outcome

The benchmark covered

- `4 <= N <= 120`;
- `3 <= r <= 30`;
- exact budgets `B <= 4`;
- `12,987` optimization cases;
- `1,077` cases with nonempty precedence constraints.

Results:

- ordinary precedence-aware solver mismatches: `0`;
- new-bound solver mismatches: `0`;
- false certificates: `0`;
- old-bound visited nodes: `65,971`;
- new-bound visited nodes: `65,971`;
- old-bound leaves: `13,746`;
- new-bound leaves: `13,746`;
- improved cases: `0`;
- equal cases: `12,987`;
- worse cases: `0`.

Thus the bound is mathematically valid and never weaker, but on this benchmark it produced no observable tree reduction.

## 9. Interpretation

The negative result is informative. Dominance precedence is sparse, budgets are small, and the existing channelwise top-gain bound was already sufficient to make exactly the same pruning decisions at every reached node. A stronger symbolic upper bound does not automatically imply fewer visited nodes.

## 10. Classification

- precedence-aware bound: exact theorem;
- comparison `UB_prec <= UB_old`: exact theorem;
- benchmark equality of search trees: finite computational result;
- uniform speedup: not established;
- polynomial-time complexity: not claimed;
- Goldbach proof: not claimed;
- RH/GRH progress: not claimed.
