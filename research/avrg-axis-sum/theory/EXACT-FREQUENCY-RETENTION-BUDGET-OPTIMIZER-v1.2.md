# Exact Frequency-Retention Budget Optimizer v1.2

## Scope
Fix an additive fiber, an effective period q, and the paired-frequency singleton tail certificate. Let K_q be the available paired frequencies and let B be a retention budget.

For a retained set S subset K_q define the certified-channel objective

F(S) = #{c mod q : L_S(c) > C_hpp(c)},

where

L_S(c) = R_Lambda(N)/q + P_Nyquist(c) + sum_{k in S} P_k(c) - sum_{k notin S} |P_k(c)|.

Here P_k(c) is the exact signed contribution of the pair k,-k and C_hpp(c) is the local higher-prime-power contamination bound.

## Exact finite optimizer
For a budget B, define

OPT_B = max_{S subset K_q, |S| <= B} F(S).

Because K_q is finite, OPT_B is attained. Exhaustive enumeration gives an exact optimizer inside the declared finite frequency pool.

## Monotonicity under retention
For every S and k notin S,

L_{S union {k}}(c) - L_S(c) = P_k(c) + |P_k(c)| >= 0.

Therefore F is monotone:

S subset T implies F(S) <= F(T).

## No submodularity claim
The certified-channel objective contains threshold crossings and need not be submodular. Consequently greedy selection has no certified approximation ratio here.

Explicit finite counterexample from the verifier:

N = 13, r = 17, q = 17, B = 2.

A greedy certificate-count selection chooses {7,8} and certifies 0 channels, while the exact choice {1,3} certifies 2 channels.

## Baselines
Three strategies are compared:

1. Energy: retain the B pairs with largest |Zhat(k)|^2.
2. Greedy: add the pair with largest current marginal certificate count.
3. Exact: enumerate all subsets of size at most B and maximize F.

The exact result is conditional on the declared q-range, certificate formula, and budget. It is not a global analytic theorem about Goldbach.

## Honest classification
- Exact finite combinatorial optimization theorem: proved.
- Monotonicity of the certificate objective: proved.
- Submodularity: not claimed.
- Goldbach/RH/GRH progress: none.
