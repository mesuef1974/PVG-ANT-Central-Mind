# Modulus Selection as a Submodular Rank-Design Problem — v1.1

Status: `PROVED THEOREM UNIT`

Branch state: `ACTIVE-RESEARCH-v1.1`

## 1. Purpose

The exact multi-modulus rank theorem reduces measurement design to a finite frequency-cover problem. This unit formalizes that reduction and proves the structural properties needed for principled modulus selection under a measurement budget.

No claim about Goldbach, prime production, RH/GRH, or literature priority is made here.

## 2. Effective moduli and frequency sets

For a physical modulus `r`, define its effective modulus

\[
q(r)=\frac{r}{\gcd(2,r)}.
\]

Fix a finite candidate family `\mathcal Q` of effective moduli and let

\[
L=\operatorname{lcm}(q:q\in\mathcal Q).
\]

For each `q\in\mathcal Q`, define the frequency subgroup

\[
H_q
=
\left\{
 m\in\mathbb Z/L\mathbb Z:
 m\equiv0\pmod{L/q}
\right\}.
\]

Then `|H_q|=q`, and for every nonempty finite set `T\subseteq\mathcal Q`,

\[
\left|\bigcap_{q\in T}H_q\right|
=
\gcd(T).
\]

For a selected family `S\subseteq\mathcal Q`, define the unsaturated frequency coverage

\[
F(S)=\left|\bigcup_{q\in S}H_q\right|,
\]

and the fiber-rank objective

\[
R_N(S)=\min(N-1,F(S)).
\]

By the exact multi-modulus rank theorem,

\[
R_N(S)=\operatorname{rank}M_{N;S}.
\]

## 3. Theorem: monotonicity and diminishing returns

### Theorem 3.1

The functions `F` and `R_N` are normalized, monotone, and submodular on the candidate family `\mathcal Q`.

Equivalently, whenever `A\subseteq B\subseteq\mathcal Q` and `q\notin B`,

\[
F(A\cup\{q\})-F(A)
\ge
F(B\cup\{q\})-F(B),
\]

and

\[
R_N(A\cup\{q\})-R_N(A)
\ge
R_N(B\cup\{q\})-R_N(B).
\]

### Proof

Normalization is immediate: `F(\varnothing)=R_N(\varnothing)=0`.

Monotonicity follows because adding a subgroup cannot shrink a union.

For submodularity of `F`, the marginal gain of adding `q` to `S` is

\[
\Delta_F(q\mid S)
=
\left|H_q\setminus\bigcup_{p\in S}H_p\right|.
\]

If `A\subseteq B`, then

\[
\bigcup_{p\in A}H_p
\subseteq
\bigcup_{p\in B}H_p,
\]

so the uncovered part of `H_q` can only decrease. Hence

\[
\Delta_F(q\mid A)\ge\Delta_F(q\mid B).
\]

For `R_N(S)=\min(N-1,F(S))`, write `c=N-1`. Its marginal gain is

\[
\Delta_R(q\mid S)
=
\min\bigl(c-F(S),\Delta_F(q\mid S)\bigr)
\]

when `F(S)<c`, and is zero after saturation. Both arguments of the minimum are nonincreasing as `S` grows, so diminishing returns is preserved. Therefore `R_N` is submodular.

## 4. Exact marginal-gain formula

### Proposition 4.1

Before rank saturation, the gain from adding `q` to `S` is

\[
\Delta_F(q\mid S)
=
\sum_{T\subseteq S}
(-1)^{|T|}
\gcd\bigl(\{q\}\cup T\bigr),
\]

where the empty-set term is interpreted as `q`.

Consequently,

\[
\Delta_R(q\mid S)
=
\min\left(
N-1-R_N(S),
\sum_{T\subseteq S}
(-1)^{|T|}
\gcd\bigl(\{q\}\cup T\bigr)
\right).
\]

### Proof

Apply inclusion-exclusion to

\[
H_q\setminus\bigcup_{p\in S}H_p
\]

and use

\[
\left|H_q\cap\bigcap_{p\in T}H_p\right|
=
\gcd\bigl(\{q\}\cup T\bigr).
\]

The truncated rank formula follows by saturation at `N-1`.

## 5. Exact redundancy criterion

### Proposition 5.1

If `q_1\mid q_2`, then

\[
H_{q_1}\subseteq H_{q_2}.
\]

Therefore, for every selected family `S` containing both,

\[
F(S)=F(S\setminus\{q_1\}),
\qquad
R_N(S)=R_N(S\setminus\{q_1\}).
\]

Thus a smaller effective modulus dividing another selected effective modulus is rank-redundant.

### Corollary 5.2

Every rank-optimal family admits an equivalent divisibility antichain obtained by deleting all selected moduli dominated by divisibility.

This pruning preserves rank and weakly reduces every nonnegative additive cost.

## 6. Budgeted design problem

Let `c(q)>0` be any declared measurement cost. Examples include:

- effective channel cost: `c(q)=q`;
- physical residue-channel cost: `c(r)=r`;
- unit hardware cost: `c(q)=1`;
- an experimentally measured implementation cost.

For budget `B`, the exact design problem is

\[
\max_{S\subseteq\mathcal Q}
R_N(S)
\quad\text{subject to}\quad
\sum_{q\in S}c(q)\le B.
\]

### Theorem 6.1

This is a monotone submodular maximization problem under an additive budget constraint.

The theorem is a classification of the optimization structure. It does not assert that a simple greedy rule is always exactly optimal.

## 7. Safe optimization workflow

An exact search may use the following certified reductions:

1. replace each physical modulus by its effective modulus `q=r/\gcd(2,r)`;
2. merge duplicate effective moduli;
3. delete divisibility-dominated candidates when their costs are no smaller than the dominating candidate;
4. stop any branch once rank reaches `N-1`;
5. upper-bound a branch by the current rank plus the sum of remaining uncovered-frequency gains;
6. retain all ties, since equal rank may have different conditioning.

A greedy diagnostic may select the candidate maximizing

\[
\frac{\Delta_R(q\mid S)}{c(q)},
\]

but this unit classifies that rule as a heuristic unless an independent optimality proof is supplied for the chosen constraint class.

## 8. Rank is not conditioning

Two families may have the same rank but very different smallest positive singular value. Therefore the design objective should eventually be bi-criteria:

\[
\text{maximize rank coverage}
\quad\text{and then improve}\quad
\sigma_{\min}^{+}(M_{N;S}).
\]

The current theorem solves only the rank-coverage layer. Spectral design remains a separate active problem.

## 9. Classification

- effective-frequency reduction: **proved**;
- monotonicity: **proved**;
- submodularity: **proved**;
- exact marginal-gain formula: **proved**;
- divisibility-antichain pruning: **proved**;
- budgeted-design classification: **proved**;
- universal greedy optimality: **not claimed**;
- optimal conditioning under budget: **open**.
