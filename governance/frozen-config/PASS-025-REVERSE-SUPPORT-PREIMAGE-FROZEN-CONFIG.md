# PASS-025 — Reverse Support-Preimage Frozen Configuration

```text
Configuration ID: PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG-001
Goal ID: GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001
Date frozen: 2026-07-22
Status: FROZEN BEFORE REGISTERED RESULT PROMOTION
```

## 1. Target

```text
target_prime_pair_closure_depth = 12
known_tail_support = {2,167071}
known_tail_support_closure_depth = 10
reverse_support_depth_budget = 1
predecessor_support_class = binary prime faces only
```

A source prime pair of depth 12 is sought through the exact chain:

```text
source prime pair
→ binary support predecessor E
→ {2,167071}
→ registered depth-10 tail
```

This is a targeted class, not an exhaustive search over all multi-axis support predecessors.

## 2. Frozen caps

```text
reverse_seed_integer_cap = 5346272
candidate_support_node_cap = 50000
candidate_integer_cap = 1000000000000
prime_pair_realization_cap = 1000000000000
orbit_verification_depth_cap = 16
registered_top_witness_count = 25
```

The seed cap includes exact-support integers:

```text
2^e * 167071^f <= 5346272, e>=1, f>=1
```

No cap may be raised after the registered result is observed inside PASS-025.

## 3. Frozen generation rules

1. Generate every integer `n` under the seed cap with exact support `{2,167071}`.
2. Enumerate every unordered distinct-prime representation `a+b=n`.
3. Deduplicate the binary predecessor support `E={a,b}`.
4. Stop with a configuration failure if more than `50000` predecessor supports are generated; do not truncate silently.
5. For each `E={a,b}`, generate every exact-support integer:

\[
m=a^i b^j,\qquad i,j\ge1,\qquad m\le10^{12}.
\]

6. Since `a,b` are odd in this registered class, `m` is odd. A distinct-prime realization of `m` must be:

\[
m=2+(m-2).
\]

Test `m-2` by deterministic 64-bit Miller–Rabin.
7. Forward-verify every promoted witness through the canonical successor rule.

## 4. Frozen ranking

Candidate witnesses are ordered by:

```text
1. exposing prime limit = max(p,q), ascending
2. source sum, ascending
3. predecessor support product, ascending
4. predecessor support lexicographically
5. seed integer, ascending
```

The first registered witness is the minimum only within the frozen search class and caps.

## 5. Frozen pruning

```text
binary predecessor supports only
exact support equality required
distinct primes only
duplicate predecessor supports removed
candidate integers exceeding cap removed
candidate source primes exceeding realization cap removed
no adaptive seed or candidate cap extension
no multi-axis predecessor expansion
no PASS-026 continuation inside this pass
```

## 6. Contamination accounting

A small exploratory reconnaissance was executed before this configuration was committed. It showed that:

- the reverse route is computationally feasible;
- a depth-12 candidate may exist above the PASS-024 sum cap.

Therefore the registered PASS-025 run is **not blinded**. It is a confirmatory and exhaustive run only within this frozen binary-predecessor class. No exploratory candidate is promoted until the committed tool, tests, summary regeneration, forward-orbit verification, and CI gates pass.

## 7. Registered outcomes

Exactly one of the following must be recorded:

```text
DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS
FINITE_ABSENCE_WITHIN_FROZEN_CLASS
CONFIGURATION_CAP_EXCEEDED_NO_RESULT_PROMOTION
```

## 8. Claim ceiling

Even a successful witness proves only existence inside the ordinary mathematical system, while its asserted minimality is restricted to the frozen search class. It does not prove that the witness is globally minimal, that depths are unbounded, that every orbit terminates, or that Goldbach, PNT, RH, or GRH advances.

**Classification:** frozen bounded computational configuration with explicit reconnaissance contamination.
