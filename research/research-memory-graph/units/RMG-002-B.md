# RMG-002-B — Dirichlet Convolution Algebra and Formalization Candidate Pack

Status: completed / finite computational certificate PASS 14/14

Classification: Knowledge Architecture / Algebraic Verification / Formalization Planning

Branch: `agent/pvg-axis-sum-continuation-002`

## Mission

Turn Dirichlet convolution from an isolated definition into a governed algebraic component of the Number Theory Research Mind, with exact ANT↔PVG transport, positive and negative reasoning rules, executable regression checks, and a truthful Lean candidate pack.

## Delivered artifacts

```text
research/research-memory-graph/registry/dirichlet-convolution-algebra.jsonl
research/research-memory-graph/formalization/RMG-002-B-LEAN-CANDIDATE-PACK.md
research/research-memory-graph/code/verify_rmg_002_b.py
research/research-memory-graph/results/rmg_002_b_verification.json
```

## Algebra registered

The registry records:

- convolution identity `epsilon`;
- commutativity;
- associativity;
- distributivity;
- `mu * 1 = epsilon`;
- `1 * 1 = tau`;
- `phi * 1 = id`;
- `Lambda * 1 = log`;
- preservation of multiplicativity;
- failure to preserve complete multiplicativity;
- the classical Dirichlet-inverse criterion `f(1) != 0`.

## Exact PVG transport

For `v=nu(n)`, the divisor correspondence gives

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d)
\]

as the box convolution

\[
(F\star_{\mathrm{box}}G)(v)
=
\sum_{0\le u\le v}F(u)G(v-u).
\]

This is an exact identity rewrite once the integer↔valuation-vector bijection and divisor↔subvector correspondence are supplied. It does not by itself produce analytic continuation, asymptotics, positivity, or prime-distribution theorems.

## Reasoning rules

Accepted rule:

```text
f multiplicative
g multiplicative
-----------------------------
f * g multiplicative
```

Rejected inflation:

```text
f completely multiplicative
g completely multiplicative
--------------------------------
f * g completely multiplicative
```

Counterexample:

\[
1*1=\tau,
\qquad
\tau(4)=3\ne4=\tau(2)^2.
\]

Thus convolution preserves multiplicativity but not complete multiplicativity in general.

## Numerical verification

The stdlib-only harness checks the finite range `1<=n<=300` and 2203 coprime pairs in `[1,60]^2`.

Observed result:

```text
PASS 14/14
```

Verified families:

- identity, commutativity, associativity, and distributivity;
- Möbius inversion identity;
- divisor-counting identity;
- totient identity;
- von Mangoldt logarithmic identity;
- multiplicativity closure on a concrete nontrivial convolution `mu*tau`;
- negative complete-multiplicativity counterexample;
- registry schema, unique IDs, negative-rule presence, and L6 ceiling.

## Lean state

A 12-item formalization candidate pack was created. It includes divisor-box equivalence, convolution algebra laws, named arithmetic-function identities, multiplicativity closure, and the formal counterexample for complete multiplicativity.

Current truthful state:

```text
LEAN_CANDIDATES = 12
PROJECT_OWNED_PROOFS_ADDED = 0
L6_PROMOTION = NOT AUTHORIZED
```

The existing Lean valuation layer is a dependency, not a certificate for these new statements.

## Assimilation state

```text
DIRICHLET_CONVOLUTION_ALGEBRA = L5_COMPUTATIONALLY_REGRESSION_TESTED
BOX_CONVOLUTION_TRANSLATION = L3_BIDIRECTIONALLY_ANALYZED
LEAN_CANDIDATE_PACK = planning artifact, not an assimilation level
```

No blanket L6 or L7 promotion is made.

## Scientific ceiling

```text
CLASSICAL IDENTITIES + FINITE REGRESSION
NO NEW ANT THEOREM
NO ASYMPTOTIC IMPROVEMENT
NO GOLDBACH CLAIM
NO RH OR GRH PROGRESS
NO FORMAL-PROOF CERTIFICATE YET
```

## Acceptance decision

```text
ALGEBRA_REGISTRY = PASS
PVG_BOX_TRANSLATION = PASS
POSITIVE_REASONING_RULE = PASS
NEGATIVE_REASONING_RULE = PASS
NUMERICAL_HARNESS = PASS 14/14
LEAN_CANDIDATE_PACK = PASS AS CANDIDATE ONLY
RMG-002-B = COMPLETED
```

## Next governed step

```text
RMG-002-C — Dirichlet Series / Euler Product Dependency Graph and Convergence-Certificate Discipline
```

It should connect arithmetic functions and convolution identities to Dirichlet-series multiplication, Euler products, abscissae of convergence, analytic continuation boundaries, and explicit anti-collapse tests separating formal coefficient identities from analytic equalities.
