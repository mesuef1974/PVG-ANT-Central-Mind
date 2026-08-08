# ACTIVE-003-S — Minimal Forbidden Channel Hyperedges

## Status

`validated_partial`

The theorem, executable verifier, and an exact reduced-domain benchmark are complete. The full ACTIVE-003-R domain is not yet closed because naive materialization of every forbidden channel family is computationally excessive.

## Artifacts

- theory: `theory/MINIMAL-FORBIDDEN-CHANNEL-HYPEREDGES-v1.0.md`
- verifier: `code/verify_minimal_forbidden_channel_hyperedges.py`
- preliminary results: `results/minimal_forbidden_channel_hyperedges_preliminary_v1.0.json`

## Exact mathematical result

Every forbidden channel family contains an inclusion-minimal forbidden subfamily. Therefore the antichain of minimal forbidden hyperedges preserves the exact higher-order compatibility bound:

\[
UB_{\min}=UB_{\mathrm{hyp}}.
\]

This is an exact finite-combinatorial compression, not a heuristic.

## Executed benchmark

```text
4 <= N <= 80
3 <= r <= 20
exact budgets B <= 4
optimization cases = 4,697
```

Results:

```text
optimum mismatches = 0
false certificates = 0
hypergraph-bound mismatches = 0
forbidden-family coverage failures = 0
minimality failures = 0
status = PASS
```

Representation counts:

```text
all forbidden families = 49,815
minimal forbidden families = 986
representation reduction = 98.0206765%
```

Minimal-hyperedge size distribution:

```text
size 2 = 954
size 3 = 32
```

The 32 minimal triples prove that the obstruction antichain is not purely graph-theoretic on the executed benchmark.

## Explicit example

```text
N = 16
r = 15
q = 15
B = 2
all forbidden families = 9
minimal forbidden families = 4
minimal edges = {6,7}, {6,10}, {7,11}, {10,11}
full hypergraph bound = 2
minimal-cut bound = 2
```

## Why the unit is not closed

The first full-domain run attempted:

```text
4 <= N <= 120
3 <= r <= 30
B <= 4
```

but naive enumeration and storage of all forbidden channel families exceeded the available execution window. No full-domain result is claimed.

## Required correction before closure

Replace `all_forbidden_families` materialization with direct antichain generation and verify coverage without enumerating every forbidden superset. Candidate methods:

1. incremental union-cost search with antichain pruning;
2. memoization by mandatory-frequency union mask;
3. minimal-transversal style generation;
4. bit-mask representation of channel closures;
5. exact bound comparison without storing the complete forbidden upward closure.

Then rerun the full ACTIVE-003-R benchmark.

## Claims explicitly not made

- no full-domain closure yet;
- no runtime speedup theorem;
- no polynomial-time algorithm;
- no Goldbach proof;
- no RH or GRH progress.
