# ACTIVE-003-L — Exact Branch-and-Bound Frequency Retention — v1.2

Status: CLOSED / PASS.

## Completed
- Proved an admissible channelwise upper bound for remaining retention gains.
- Proved safe pruning and exactness of the include/exclude Branch-and-Bound solver.
- Implemented a complete governed verifier.
- Compared against exhaustive exact-size enumeration.
- Verified zero optimal-value mismatches and zero false certificates.

## Benchmark
- 2 <= N <= 120.
- 1 <= r <= 20.
- Budgets B=0..4.
- 11,900 optimization instances.

## Performance result
- Exhaustive complete subsets: 86,751.
- Branch-and-Bound complete subsets: 4,752.
- Reduction: 94.52225334578276%.
- Total Branch-and-Bound nodes visited: 15,152.
- Nodes pruned by admissible bound: 8,734.

## Classification
- Exact finite optimizer: proved and verified.
- Worst-case polynomial time: NOT claimed.
- Goldbach theorem or new analytic lower bound: NOT claimed.
- RH/GRH progress: none.

## Next target
Strengthen the upper bound and candidate ordering for larger effective periods q, including dominance pruning and cached channel masks, while preserving exactness.