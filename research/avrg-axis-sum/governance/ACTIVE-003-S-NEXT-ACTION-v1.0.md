# ACTIVE-003-S next action

`CURRENT ACTION = OPTIMIZE_MINIMAL_HYPEREDGE_ENUMERATION`

Required implementation pass:

1. encode every mandatory channel closure as an integer bit mask;
2. generate minimal forbidden families directly in increasing size;
3. prune a candidate as soon as it contains a known minimal forbidden edge;
4. memoize by `(channel-position, union-mask, chosen-size)`;
5. compare the exact maximum feasible channel count against ACTIVE-003-R without materializing the full upward closure;
6. rerun `4 <= N <= 120`, `3 <= r <= 30`, `B <= 4`;
7. close ACTIVE-003-S only if optimum mismatches, false certificates, bound mismatches, minimality failures, and coverage failures are all zero.

The present status remains `validated_partial`.
