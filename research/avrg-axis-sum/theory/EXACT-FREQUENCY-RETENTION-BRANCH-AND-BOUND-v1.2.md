# Exact Frequency-Retention Branch-and-Bound — v1.2

Status: proved finite optimization theorem / no Goldbach claim.

## Setup
For a fixed effective period q, let K be the finite set of paired nonzero frequencies. For each channel c define a baseline lower bound L_empty(c), a contamination threshold C(c), and nonnegative retention gains

G_k(c)=P_k(c)+|P_k(c)| >= 0.

For S subset K,

L_S(c)=L_empty(c)+sum_{k in S} G_k(c),

and

F(S)=#{c mod q : L_S(c)>C(c)}.

For budget B, monotonicity implies an optimum may be searched among sets of size min(B,|K|).

## Node upper bound
At a search node with selected set S, remaining candidates R, and t slots left, define channelwise optimistic gain

U_t(c;R)=sum of the t largest values among {G_k(c):k in R}.

Then every completion T subset R with |T|=t satisfies

L_{S union T}(c) <= L_S(c)+U_t(c;R).

Therefore

UB(S,R,t)=#{c : L_S(c)+U_t(c;R)>C(c)}

is an admissible upper bound for every descendant objective value.

## Pruning theorem
If UB(S,R,t) <= F_best, where F_best is the best incumbent certificate count, the entire node may be pruned without losing an optimum.

Proof: every feasible descendant has certificate count at most UB(S,R,t), hence cannot improve the incumbent.

## Exactness
Depth-first include/exclude search with:
- exact-size budget search,
- admissible UB pruning,
- deterministic tie-breaking,
- any feasible incumbent initialization,

returns exactly OPT_B.

## Honest scope
The method is exponential in the worst case. The result is an exact finite optimizer, not a polynomial-time theorem and not progress on binary Goldbach. Its value is computational: it can avoid most subset evaluations when the channelwise upper bound is informative.