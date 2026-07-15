# ACTIVE-002-A — Submodular Modulus-Design Status v1.1

Status: `COMPLETED / PROVED / VERIFIED`

## Object

For effective moduli `q=r/\gcd(2,r)`, let `H_q` be the corresponding frequency subgroup in a common cyclic ambient period. For a selected family `S`, define

\[
R_N(S)=\min\left(N-1,\left|\bigcup_{q\in S}H_q\right|\right).
\]

By the exact multi-modulus rank theorem,

\[
R_N(S)=\operatorname{rank}M_{N;S}.
\]

## Completed results

1. `R_N` is normalized and monotone.
2. `R_N` is submodular: added moduli have diminishing rank returns.
3. The exact unsaturated marginal gain is
   \[
   \Delta(q\mid S)
   =
   \sum_{T\subseteq S}(-1)^{|T|}\gcd(\{q\}\cup T).
   \]
4. If `q_1\mid q_2`, then `q_1` is rank-redundant once `q_2` is selected.
5. Every rank-optimal design has an equivalent divisibility-antichain representative.
6. Rank maximization under any positive additive cost is a monotone submodular budget problem.
7. Rank and conditioning remain separate objectives.
8. Gain-per-cost greedy selection is not universally exact.

## Verified counterexample to universal greedy optimality

Candidate effective moduli:

\[
\{2,3,4,5,6\}.
\]

With

\[
N=8,
\qquad
B=8,
\qquad
c(q)=q,
\]

gain-per-cost greedy selects `\{6\}` and obtains rank `6`, whereas the feasible family `\{3,5\}` obtains full rank `7`.

Thus:

```text
UNIVERSAL GREEDY OPTIMALITY = FALSE
```

## Finite verification

- candidate universes: `5`;
- diminishing-return checks: `24,570`;
- submodularity mismatches: `0`;
- budgeted optimization instances: `1,440`;
- strict greedy-suboptimal instances: `83`;
- status: `PASS`.

## Controlling files

- `theory/MODULUS-SELECTION-SUBMODULAR-RANK-DESIGN-v1.1.md`;
- `code/verify_modulus_selection_submodular_design.py`;
- `results/modulus_selection_submodular_design_verification_v1.1.json`.

## Next target

`ACTIVE-002-B — Exact budget optimizer and Pareto frontier.`

Build a certified exhaustive/branch-and-bound optimizer that returns:

- maximum achievable rank under budget;
- all minimum-cost full-rank designs;
- the rank-versus-cost Pareto frontier;
- divisibility-pruned equivalent designs;
- later, conditioning as a secondary objective.

## Scientific ceiling

This unit concerns finite measurement design. It does not prove Goldbach, improve analytic prime estimates, establish novelty or priority, or constitute RH/GRH progress.
