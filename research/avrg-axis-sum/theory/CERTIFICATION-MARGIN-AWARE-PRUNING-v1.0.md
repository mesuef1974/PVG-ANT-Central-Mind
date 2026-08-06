# ACTIVE-003-Q — Certification-Margin-Aware Pruning

## Status

Exact finite-search result. No polynomial-time claim. No Goldbach, RH, or GRH claim.

## 1. Node state and certification margins

At a branch-and-bound node let

- `S` be the included frequencies;
- `X` be the excluded frequencies;
- `R` be the undecided frequencies;
- `t = B - |S|` be the remaining exact-budget slots.

For channel `c`, write

\[
L_S(c)=L_\varnothing(c)+\sum_{k\in S}G_k(c)
\]

and define its certification deficit

\[
\delta_S(c)=C(c)-L_S(c).
\]

The channel is already certified exactly when `delta_S(c) < 0`.

The old optimistic bound counts `c` whenever the sum of the `t` largest gains among `R` exceeds `delta_S(c)`. This treats channels independently.

## 2. Mandatory frequencies for one channel

For `k in R`, remove `k` from the optimistic pool. If

\[
L_S(c)+\sum_{\ell\in\operatorname{Top}_t(R\setminus\{k\};c)}G_\ell(c)
\le C(c),
\]

then every exact-budget completion certifying channel `c` must include `k`.

Define the mandatory-frequency set

\[
M_c(S,R,t)
=
\left\{
 k\in R:
 L_S(c)+\sum_{\ell\in\operatorname{Top}_t(R\setminus\{k\};c)}G_\ell(c)
 \le C(c)
\right\}.
\]

This is a necessary, not sufficient, set.

## 3. Precedence closure of mandatory frequencies

Let `A(k)` denote all transitive precedence ancestors of `k`. Any feasible solution containing `k` must contain `A(k)`.

Define

\[
\overline M_c
=
\left(\bigcup_{k\in M_c}(A(k)\cup\{k\})\right)\setminus S.
\]

Channel `c` is impossible at the node if either

\[
\overline M_c\cap X\ne\varnothing
\]

or

\[
|\overline M_c|>t.
\]

## 4. Pairwise channel compatibility

Two individually possible channels `c,d` can be certified together only if

\[
|\overline M_c\cup\overline M_d|\le t
\]

and the union does not meet `X`.

Construct the channel compatibility graph `Gamma`:

- vertices: channels passing the old individual optimistic test and the mandatory-closure feasibility test;
- edge `c--d`: the two mandatory closures fit jointly in the remaining budget.

Every set of simultaneously certifiable channels is a clique in `Gamma`.

Therefore

\[
\#\{\text{simultaneously certifiable channels}\}
\le \omega(\Gamma)
\le \chi(\Gamma).
\]

Any proper coloring gives a safe upper bound. The verifier uses a deterministic DSATUR-style greedy coloring, whose number of colors is at least the clique number.

## 5. Margin-aware upper bound

Let `color(Gamma)` be the number of colors produced by the proper coloring. Define

\[
UB_{\mathrm{margin}}(S,X,R,t)
=
\operatorname{color}(\Gamma).
\]

Since every jointly certifiable channel family is a clique,

\[
F(T)\le UB_{\mathrm{margin}}
\]

for every feasible completion `T` of the node.

Also, because `Gamma` only uses channels counted by the old individual bound,

\[
UB_{\mathrm{margin}}\le UB_{\mathrm{old}}.
\]

Thus pruning when

\[
UB_{\mathrm{margin}}\le F_{\mathrm{best}}
\]

is exact.

## 6. Exactness theorem

**Theorem.** Branch-and-bound with precedence propagation, closure-ratio branch ordering, and the margin-aware compatibility coloring bound returns the same optimum as exhaustive enumeration.

**Reason.**

1. precedence propagation preserves a canonical optimum;
2. each mandatory-frequency test is necessary;
3. every jointly certifiable channel family is a clique in the compatibility graph;
4. every proper coloring count upper-bounds the clique number;
5. hence the new pruning bound never lies below the value of a feasible completion.

## 7. Finite verification result

Benchmark:

- `4 <= N <= 120`;
- `3 <= r <= 30`;
- exact budgets through `4`;
- `12,987` optimization cases.

Observed:

- optimum mismatches: `0`;
- false certificates: `0`;
- old-bound nodes: `65,971`;
- margin-aware nodes: `65,209`;
- improved/equal/worse cases: `223 / 12,764 / 0`;
- stricter margin-bound calls: `1,126`;
- incompatible channel pairs detected: `5,998`.

Aggregate node reduction:

\[
\frac{65971-65209}{65971}\times100\%
\approx 1.1551\%.
\]

The improvement is real but modest. No uniform asymptotic speedup is claimed.

## 8. Explicit example

For

\[
N=74,\qquad r=25,\qquad q=25,\qquad B=3,
\]

both solvers return optimum `7` with selected frequencies

\[
\{2,9,10\}.
\]

The old bound visits `19` nodes, while the margin-aware bound visits `11` nodes, a reduction of `8` nodes.

## 9. Scientific classification

- mandatory-frequency lemma: exact;
- mandatory precedence closure: exact;
- compatibility-graph upper bound: exact;
- DSATUR coloring value: safe upper bound, not necessarily the chromatic number;
- finite benchmark: computational verification;
- polynomial-time claim: none;
- Goldbach proof claim: none;
- RH/GRH progress claim: none.
