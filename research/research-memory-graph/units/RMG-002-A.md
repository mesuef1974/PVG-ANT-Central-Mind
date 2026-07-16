# RMG-002-A — Arithmetic-Function Family Expansion and Lean-Certificate Linkage

Status: completed / finite computational certificate PASS 14/14

Classification: Knowledge Architecture / Computational Verification / Diagnostic

Validation state: arithmetic_function_family_registered_and_regression_tested

Branch: `agent/pvg-axis-sum-continuation-002`

Parent units:

- `RMG-001-C` — machine-readable node and edge registry;
- `RMG-001-D` — query API, integration links, and public reasoning benchmark.

## 1. Delivered artifacts

```text
research/research-memory-graph/registry/arithmetic-functions.jsonl
research/research-memory-graph/registry/arithmetic-function-edges.jsonl
research/research-memory-graph/code/verify_rmg_002_a.py
research/research-memory-graph/results/rmg_002_a_verification.json
```

## 2. Registered function family

The unit adds six governed arithmetic-function nodes:

1. constant-one function `1`;
2. Mobius function `mu`;
3. divisor-counting function `tau`;
4. Euler totient `phi`;
5. Liouville function `lambda`;
6. prime indicator `1_P`.

Each node records the standard ANT definition, PVG realization, translation class, inverse status, preserved and lost information, provenance, certificates, assimilation level, and scientific ceiling.

## 3. ANT ↔ PVG translations

### Constant one

```text
ANT: 1(n)=1
PVG: constant observable on valuation space
translation: exact
```

### Mobius

```text
ANT: mu(n)=0 off squarefree integers; otherwise (-1)^omega(n)
PVG: zero off the squarefree locus; support-parity sign on that locus
translation: exact as an observable
```

The scalar value is not an injective encoding of the valuation vector.

### Divisor count

```text
tau(n)=product_p (v_p(n)+1)
```

This is exactly the divisor-box cardinality. It is lossy as an inverse map: for example,

```text
tau(6)=tau(8)=4
```

although `nu(6)` and `nu(8)` are different.

### Euler totient

```text
phi(n)=n product_{p|n}(1-1/p)
```

The PVG representation is axis-local and support-dependent, but the output is noninjective:

```text
phi(15)=phi(16)=8.
```

### Liouville

```text
lambda(n)=(-1)^Omega(n)=(-1)^{sum_p v_p(n)}.
```

This is an exact parity character of valuation mass and a severe lossy projection. For example,

```text
lambda(6)=lambda(10)=1
```

while their supports differ.

### Prime indicator

```text
1_P(n)=1
```

exactly on unit points of one prime axis. Finite primality classification does not imply the Prime Number Theorem.

## 4. Verified identities

The stdlib-only harness verifies:

```text
mu * 1 = epsilon                 for 1 <= n <= 500
tau = 1 * 1                     for 1 <= n <= 500
phi * 1 = id                    for 1 <= n <= 500
```

It also verifies:

- Mobius multiplicativity on 6400 ordered pairs;
- tau multiplicativity on coprime pairs in the same grid;
- phi multiplicativity on coprime pairs;
- Liouville complete multiplicativity on all 6400 pairs;
- prime-indicator equivalence with unit-axis valuation points;
- explicit noninjectivity counterexamples;
- registry schema and edge referential integrity.

Observed result:

```text
PASS 14/14
```

## 5. Lean linkage decision

The repository contains a mature Lean valuation layer covering valuation laws, support, cardinality, and mass geometry. Those results are relevant dependencies for the PVG readings in this unit.

However, this inspection did not establish a function-specific project file and successful build certificate proving the Mobius, tau, phi, Liouville, or prime-indicator identities added here.

Therefore:

```text
LEAN_FOUNDATIONAL_DEPENDENCY = PRESENT
FUNCTION_SPECIFIC_LEAN_CERTIFICATE = ABSENT
L6_PROMOTION = REJECTED
```

No node is assigned `L6_FORMALLY_VERIFIED` merely because adjacent valuation infrastructure exists.

## 6. Assimilation state

```text
L5_COMPUTATIONALLY_REGRESSION_TESTED:
- Mobius function
- tau
- phi
- Liouville function

L4_NUMERICALLY_VERIFIED:
- constant-one function
- prime indicator
```

The noninjective examples are part of the assimilation evidence because they state precisely what the PVG observable loses.

## 7. Scientific ceiling

```text
CLASSICAL IDENTITIES + FINITE REGRESSION
NOT A NEW ARITHMETIC-FUNCTION THEOREM
NOT AN ASYMPTOTIC RESULT
NOT A PNT IMPROVEMENT
NO RH OR GRH PROGRESS
NO FUNCTION-SPECIFIC LEAN L6 CERTIFICATE
NO TRAINING CORPUS AUTHORIZATION
```

## 8. Acceptance decision

```text
ARITHMETIC_FUNCTION_NODES = PASS 6/6
TYPED_EDGES = PASS 8/8
NUMERICAL_AND_REGRESSION_CHECKS = PASS 14/14
COUNTEREXAMPLES_AND_LOSS_PROFILES = PASS
LEAN_CEILING_DISCIPLINE = PASS
RMG-002-A = COMPLETED
```

## 9. Next governed step

Recommended next unit:

```text
RMG-002-B — Dirichlet Convolution Algebra and Formalization Candidate Pack
```

It should add:

- identity, associativity, commutativity, and distributivity records;
- explicit convolution tables and divisor-box visual examples;
- inverse criteria and failure cases;
- a small Lean candidate pack, separated into proposed statements and actually compiled certificates;
- reasoning cases that distinguish pointwise multiplication from Dirichlet convolution.
