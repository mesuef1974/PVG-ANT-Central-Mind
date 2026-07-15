# ACTIVE-003-Q — Certification-Margin-Aware Pruning Status

## Decision

`PASS / CLOSED`

## Scope

This unit adds an exact branch-and-bound upper bound based on channel certification margins, mandatory frequencies, precedence closure, and pairwise channel compatibility.

## Artifacts

- theory: `theory/CERTIFICATION-MARGIN-AWARE-PRUNING-v1.0.md`
- verifier: `code/verify_certification_margin_aware_pruning.py`
- results: `results/certification_margin_aware_pruning_verification_v1.0.json`

## Verification domain

```text
4 <= N <= 120
3 <= r <= 30
exact budgets B <= 4
optimization cases = 12,987
cases with precedence = 1,077
```

## Exactness checks

```text
old-bound optimum mismatches = 0
margin-aware optimum mismatches = 0
false certificates = 0
status = PASS
```

## Search comparison

```text
old-bound visited nodes = 65,971
margin-aware visited nodes = 65,209
aggregate node reduction = 1.1550529778%

improved cases = 223
equal cases = 12,764
worse cases = 0

old leaves = 13,746
margin-aware leaves = 13,746
margin-bound calls = 61,703
strictly tighter calls = 1,126
incompatible channel pairs detected = 5,998
```

The lower count of recorded upper-bound prunes in the new solver does not indicate a weaker tree. Earlier margin-aware cuts prevent descendant nodes from being generated, so fewer later prune events are reached.

## Explicit improvement example

```text
N = 74
r = 25
q = 25
B = 3
optimum = 7
selected frequencies = {2,9,10}

old bound: 19 nodes, 2 leaves
margin-aware bound: 11 nodes, 2 leaves
node reduction: 8
```

## Scientific interpretation

The useful information is not only whether each channel is individually reachable. Channels may require incompatible mandatory frequency closures. The compatibility graph records this joint obstruction, and any proper coloring upper-bounds the number of channels that can be certified simultaneously.

The improvement is finite and modest. It is not a proof of uniform acceleration or improved asymptotic complexity.

## Claim controls

```text
polynomial-time claim = false
uniform-speedup theorem = false
Goldbach proof claim = false
RH progress claim = false
GRH progress claim = false
```

## Next research target

`ACTIVE-003-R — Higher-Order Channel Compatibility Cuts`

Pairwise compatibility is only a necessary projection of joint feasibility. The next unit should test triple and small-hyperedge mandatory-closure conflicts, while controlling the additional computational cost.
