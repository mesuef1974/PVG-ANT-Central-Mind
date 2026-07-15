# Frequency Dominance as a Precedence Constraint — v1.2

## Setup
For each retained paired frequency k, let the channelwise nonnegative gain be

\[
G_k(c)=P_k(c)+|P_k(c)|\ge 0.
\]

The certificate-count objective under retained set S is

\[
F(S)=\#\{c:L_\varnothing(c)+\sum_{k\in S}G_k(c)>C(c)\}.
\]

## Channelwise dominance
Say that frequency i dominates frequency j when

\[
G_i(c)\ge G_j(c)\qquad\text{for every channel }c.
\]

If the inequality is strict for at least one channel, call it strict dominance.

## Replacement theorem
If i dominates j and S contains j but not i, then

\[
F((S\setminus\{j\})\cup\{i\})\ge F(S).
\]

Proof: each channel lower bound changes by \(G_i(c)-G_j(c)\ge0\).

Therefore, under a uniform cardinality budget, there exists an optimal solution satisfying the precedence rule

\[
\boxed{j\in S\Longrightarrow i\in S}
\]

for a chosen dominator i of j.

## Important non-deletion result
Dominance does **not** justify deleting j from the candidate pool. An optimum may contain both i and j.

Counterexample from the governed verifier:

\[
N=15,\quad r=12,\quad q=6,\quad B=2.
\]

Frequency 2 dominates frequency 1 channelwise, but

\[
F(\{1\})=F(\{2\})=0,
\qquad
F(\{1,2\})=2.
\]

Deleting frequency 1 would reduce the exact optimum from 2 to 0.

## Equivalent frequencies
If \(G_i(c)=G_j(c)\) for every c, impose a canonical ordering rule, for example

\[
j\in S\Longrightarrow i\in S\qquad(i<j),
\]

rather than deleting j. Multiple equivalent copies can still be jointly useful under an additive objective.

## Algorithmic use
Dominance is used as a search constraint:

- reject any branch that selects a dominated frequency while excluding its designated dominator;
- branch on dominators before dominated frequencies;
- retain all candidates unless an additional theorem proves true redundancy.

This preserves exact optimality while reducing the canonical search space.

## Classification
- Replacement theorem: proved.
- Precedence-constrained exact search: proved safe.
- Global deletion of dominated frequencies: disproved.
- Asymptotic improvement: not claimed.
- Goldbach/RH/GRH progress: none claimed.
