# RMG-001-D — Registry Integration, Query API, and Public Reasoning Benchmark

Status: completed / finite reasoning regression PASS 21/21

Classification: Knowledge Architecture / Computational Reasoning / Governance Diagnostic

Validation state: query_api_and_public_reasoning_benchmark_verified

Branch: `agent/pvg-axis-sum-continuation-002`

Parent unit: `RMG-001-C`

## 1. Delivered artifacts

```text
research/research-memory-graph/code/rmg_query.py
research/research-memory-graph/code/verify_rmg_001_d.py
research/research-memory-graph/benchmarks/rmg_001_d_public_reasoning_cases.jsonl
research/research-memory-graph/registry/integration-links.jsonl
research/research-memory-graph/results/rmg_001_d_verification.json
```

## 2. Query API

The stdlib-only API loads the existing RMG node and edge registries and provides:

- exact node lookup;
- text and typed-field search;
- incoming/outgoing neighborhood queries;
- bounded directed shortest-path traversal;
- translation reports exposing preservation, loss, inverse status, certificates, assimilation level, and scientific ceiling.

It is deliberately read-only. It does not silently mutate assimilation levels or certificates.

Example commands:

```text
python research/research-memory-graph/code/rmg_query.py get ANT-RH-001
python research/research-memory-graph/code/rmg_query.py search prime
python research/research-memory-graph/code/rmg_query.py neighbors ANT-VON-MANGOLDT-001 --direction out
python research/research-memory-graph/code/rmg_query.py path ANT-VON-MANGOLDT-001 ANT-PSI-001
python research/research-memory-graph/code/rmg_query.py translation-report ANT-ZETA-001
```

## 3. Central integration contract

Eight integration links connect RMG to existing project components without merging or duplicating their authoritative registries:

1. `registries/skills.jsonl` — reuse stable skill/tool identifiers;
2. `registries/program-goals.jsonl` — preserve authoritative research goals;
3. `registries/maturation-events.jsonl` — future governed assimilation changes;
4. `maps/pvg-ant-language-kernel-v1.md` — instantiate the existing translation kernel;
5. `research/avrg-axis-sum/` — ingest certified addition-fiber results;
6. `formal/lean/` — attach genuine formal certificates;
7. `research/certificate-optimization-framework/` — reuse certificate discipline;
8. `research/meta-reasoning/` — supply evidence to confidence and strategy layers.

`linked_not_merged` is intentional: the RMG must not become a competing source of truth for skills, goals, formal proofs, or governance decisions.

## 4. Public reasoning benchmark

The benchmark contains 12 public regression cases:

```text
6 positive path cases
6 negative claim-rejection cases
```

Positive routes test:

- prime → valuation vector;
- prime power → valuation vector;
- Dirichlet convolution → divisor-box geometry;
- von Mangoldt → prime-power support;
- von Mangoldt → psi;
- zeta → Dirichlet-series representation in its stated domain.

Negative routes require rejection of:

- obtaining analytic continuation from PVG reindexing;
- recovering every nontrivial zero from current PVG geometry;
- claiming RH progress;
- claiming PNT implies RH;
- upgrading finite Euler-product expansion to global analytic equality;
- calling an L2 node fully assimilated.

The public benchmark is a regression suite, not a hidden capability evaluation. No hidden answer keys or custody material are included.

## 5. Verification result

```text
QUERY API CHECKS             PASS 6/6
PUBLIC REASONING CASES       PASS 12/12
INTEGRATION REGISTRY CHECKS  PASS 3/3
TOTAL                        PASS 21/21
```

The verifier checks registry size, search/filter behavior, neighborhood and path traversal, RH ceiling preservation, every public reasoning case, integration schema and identifier uniqueness, and positive/negative case balance.

Reproduction:

```text
python research/research-memory-graph/code/verify_rmg_001_d.py --write-result
```

The process exits nonzero on failure.

## 6. Assimilation decision

This unit raises the RMG infrastructure itself to a computational regression-tested state, but it does not automatically raise all mathematical nodes.

```text
RMG QUERY/TRAVERSAL INFRASTRUCTURE = L5_COMPUTATIONALLY_REGRESSION_TESTED
PUBLIC REASONING ROUTES            = regression tested, not locked L7 benchmark
MATHEMATICAL NODE LEVELS           = unchanged from RMG-001-C
```

No node is promoted to L6 without a linked Lean theorem. No node is promoted to L7 because this unit intentionally uses public cases and contains no governed hidden benchmark.

## 7. Scientific ceiling

```text
FINITE QUERY AND REASONING REGRESSION ONLY
NOT A NEW ANALYTIC NUMBER THEORY THEOREM
NOT A GOLDBACH SOLUTION
NO PROVED RH OR GRH PROGRESS
NO TRAINING CORPUS AUTHORIZATION
NO NEURAL NETWORK TRAINED
```

## 8. Acceptance decision

```text
READ_ONLY_QUERY_API = PASS
DIRECTED_TRAVERSAL = PASS
TRANSLATION_REPORT = PASS
CENTRAL_INTEGRATION_LINKS = PASS
PUBLIC_POSITIVE_CASES = PASS 6/6
PUBLIC_NEGATIVE_CASES = PASS 6/6
CLAIM_INFLATION_REJECTION = PASS
TRAINING_SEPARATION = PASS
RMG-001-D = COMPLETED
```

## 9. Next governed step

Recommended next unit:

```text
RMG-002-A — Arithmetic-Function Family Expansion and Lean-Certificate Linkage
```

Proposed scope:

- add constant-one, Mobius, divisor-counting, Euler phi, Liouville, and prime-indicator nodes;
- add exact Dirichlet-convolution identities and counterexamples;
- connect existing Lean valuation theorems to exact RMG nodes;
- add explicit numerical examples and regression checks;
- keep L-functions, zeros, and asymptotic claims at their current honest ceilings.
