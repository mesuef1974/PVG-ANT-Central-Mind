# RMG-001-C — Machine-Readable Node and Edge Registry + Executable Numerical Verification Harness

Status: completed / finite computational certificate PASS 14/14

Classification: Knowledge Architecture / Computational Verification / Diagnostic

Validation state: registry_instantiated_and_harness_verified

Branch: `agent/pvg-axis-sum-continuation-002`

Parent units:

- `RMG-001-A` — ontology and typed edge schema;
- `RMG-001-B` — seed ANT ↔ PVG translation families.

## 1. Delivered artifacts

```text
research/research-memory-graph/registry/nodes.jsonl
research/research-memory-graph/registry/edges.jsonl
research/research-memory-graph/code/verify_rmg_001_c.py
research/research-memory-graph/results/rmg_001_c_verification.json
```

The registry reuses the ontology, translation classes, certificate discipline, and assimilation scale already established by RMG-001-A/B and the ANT–PVG acceptance standard. It does not create a parallel ontology.

## 2. Initial governed node population

The executable registry contains 16 nodes:

1. prime number;
2. prime power;
3. prime valuation vector;
4. arithmetic function;
5. multiplicative function;
6. Dirichlet convolution;
7. Dirichlet series;
8. Euler product;
9. von Mangoldt function;
10. prime-counting function `pi(x)`;
11. Chebyshev `theta(x)`;
12. Chebyshev `psi(x)`;
13. Riemann zeta function;
14. nontrivial zeta zeros;
15. Prime Number Theorem;
16. Riemann Hypothesis.

Each record carries stable identity, ANT view, PVG view, translation type, inverse status, preserved and lost information, provenance, assimilation level, certificate state, and scientific ceiling.

## 3. Translation honesty

Exact translations are limited to structures that genuinely admit exact reindexing or exact valuation encoding:

- positive integers ↔ finitely supported nonnegative valuation vectors;
- primes ↔ unit single-axis points;
- prime powers ↔ positive single-axis points;
- arithmetic functions ↔ observables on valuation vectors;
- multiplicativity ↔ multiplicativity under disjoint-support addition;
- Dirichlet convolution ↔ divisor-box convolution;
- Dirichlet series ↔ log-height weighted PVG transforms;
- von Mangoldt ↔ logarithmically labelled single-axis support;
- finite `pi`, `theta`, and `psi` values ↔ cumulative PVG observables.

The following are explicitly not promoted to exact PVG solutions:

- analytic continuation of zeta;
- the functional equation;
- zero distribution;
- nontrivial zero recovery;
- proof of the Prime Number Theorem from PVG geometry alone;
- proof or progress on RH or GRH.

For zeta zeros and RH, the registry uses `COARSE_DIAGNOSTIC`, records no inverse, and marks missing translation/proof certificates.

## 4. Executable checks

The standard-library-only harness executes 14 checks:

```text
CHK-VALUATION-ROUNDTRIP-001
CHK-MULTIPLICATION-001
CHK-PRIME-001
CHK-PRIME-POWER-001
CHK-MULTIPLICATIVE-001
CHK-DIRICHLET-CONV-001
CHK-MOBIUS-001
CHK-DIRICHLET-SERIES-001
CHK-EULER-PRODUCT-001
CHK-LAMBDA-001
CHK-CHEBYSHEV-001
CHK-REGISTRY-SCHEMA-001
CHK-EDGE-REFERENTIAL-001
CHK-REGISTRY-UNIQUENESS-001
```

Observed result:

```text
PASS 14/14
```

Selected explicit evidence:

- valuation decode/encode round trip for every `1 <= n <= 500`;
- valuation multiplication law over 2500 ordered pairs `1 <= m,n <= 50`;
- Möbius multiplicativity on all coprime pairs in the same grid;
- `mu * 1 = epsilon` for `1 <= n <= 500`;
- finite Dirichlet-series reindexing at `s=2`, cutoff 100:

  ```text
  ANT sum = 1.634983900184893
  PVG sum = 1.634983900184893
  ```

- truncated Euler product over primes `2,3,5,7`, exponents `0..3`, producing 256 unique coefficients;
- `Lambda(2)=log 2`, `Lambda(8)=log 2`, `Lambda(9)=log 3`, `Lambda(12)=0`, `Lambda(25)=log 5`;
- at `x=100`:

  ```text
  pi(100)    = 25
  theta(100) = 83.72839039906393
  psi(100)   = 94.0453112293574
  ```

## 5. Assimilation status

The registry does not assign one blanket level to all nodes.

```text
L5_COMPUTATIONALLY_REGRESSION_TESTED:
- valuation vector
- Dirichlet convolution
- von Mangoldt function
- psi(x)

L4_NUMERICALLY_VERIFIED:
- prime number
- prime power
- multiplicative function
- Dirichlet series
- Euler product (finite/truncated scope only)
- pi(x)
- theta(x)

L3_BIDIRECTIONALLY_ANALYZED:
- arithmetic function
- Riemann zeta function
- Prime Number Theorem

L2_TRANSLATED_TO_PVG:
- nontrivial zeros
- Riemann Hypothesis
```

No concept below L4 is called fully assimilated. No node is assigned L6 because this unit adds no new Lean formalization. No node is assigned L7 because no locked reasoning benchmark for this registry has yet been executed.

## 6. Reproduction

From the repository root:

```text
python research/research-memory-graph/code/verify_rmg_001_c.py --write-result
```

The process exits nonzero if any check fails.

## 7. Scientific ceiling

```text
FINITE REGISTRY + FINITE NUMERICAL VERIFICATION
NOT A NEW ANT THEOREM
NOT A GOLDBACH SOLUTION
NO PROVED RH OR GRH PROGRESS
NO TRAINING CORPUS AUTHORIZATION
NO NEURAL NETWORK TRAINED
```

The result is a governed symbolic memory component suitable for further graph population, formalization, and reasoning benchmarks.

## 8. Acceptance decision

```text
MACHINE_READABLE_NODE_REGISTRY = PASS
MACHINE_READABLE_EDGE_REGISTRY = PASS
PROVENANCE_FIELDS = PASS
ASSIMILATION_LEVEL_FIELDS = PASS
CERTIFICATE_AND_CEILING_FIELDS = PASS
NUMERICAL_HARNESS = PASS 14/14
REFERENTIAL_INTEGRITY = PASS
DUPLICATE_ID_CHECK = PASS
RMG-001-C = COMPLETED
```

## 9. Next governed step

Recommended next unit:

```text
RMG-001-D — Registry Integration, Query API, and Reasoning Benchmark
```

It should:

- connect the RMG registry to existing central registries without duplicating IDs;
- add query and neighborhood traversal;
- test ANT → PVG → ANT reasoning routes;
- add negative reasoning cases that reject equivalence inflation;
- preserve benchmark secrecy and training-corpus separation;
- nominate suitable exact identities for Lean formalization rather than claiming blanket L6.
