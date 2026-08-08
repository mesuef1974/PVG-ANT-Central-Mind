# ACTIVE-003-R — Hypergraph Compatibility Certification

## Status

**PASS / CLOSED**

## Artifacts

- Theory: `theory/HYPERGRAPH-COMPATIBILITY-CERTIFICATION-v1.0.md`
- Verifier: `code/verify_hypergraph_compatibility_certification.py`
- Results: `results/hypergraph_compatibility_certification_v1.0.json`

## Verification scope

- `4 <= N <= 120`
- `3 <= r <= 30`
- exact budgets through `4`
- `12,987` optimization cases

## Findings

The higher-order mandatory-closure union bound preserved every exhaustive optimum and produced zero false prime-pair certificates.

Aggregate comparison against ACTIVE-003-Q pairwise compatibility:

- pairwise visited nodes: `65,209`
- hypergraph visited nodes: `65,191`
- improved cases: `9`
- equal cases: `12,978`
- worse cases: `0`
- aggregate node change: `-0.0276032%`

Explicit strict improvement:

- `N=44`, `r=13`, `q=13`, exact budget `B=2`
- optimum: `4`
- selected frequencies: `{1,3}`
- pairwise tree: `9` nodes / `1` leaf
- hypergraph tree: `7` nodes / `1` leaf

## Interpretation

The unit confirms that pairwise channel compatibility does not capture every joint budget obstruction. Higher-order mandatory-closure unions can tighten the admissible upper bound and prune additional exact-search nodes.

The aggregate gain is real but small. No uniform speedup theorem is claimed.

## Claim controls

- polynomial-time claim: **NO**
- uniform asymptotic speedup claim: **NO**
- Goldbach proof claim: **NO**
- RH/GRH progress claim: **NO**

## Next research direction

`ACTIVE-003-S — Minimal Forbidden Channel Hyperedges`

Extract inclusion-minimal forbidden channel families, study their size distribution and recurrence across `(N,r,B)`, and test whether reusable forbidden-pattern cuts can replace repeated full subset enumeration.
