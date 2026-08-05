from __future__ import annotations

import argparse
import bisect
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import prod

Face = tuple[int, ...]
REGISTERED_SUM_CAP = 400_000
REGISTERED_MAX_DEPTH = 12
REGISTERED_DEEP_DEPTH_FLOOR = 7


def face_key(face):
    return "{" + ",".join(str(x) for x in face) + "}"


def sieve_tables(limit):
    if limit < 2:
        raise ValueError("limit must be at least 2")
    spf = list(range(limit + 1))
    spf[0], spf[1] = 0, 1
    for p in range(2, int(limit**0.5) + 1):
        if spf[p] != p:
            continue
        for n in range(p * p, limit + 1, p):
            if spf[n] == n:
                spf[n] = p
    is_prime = [False] * (limit + 1)
    primes = []
    for n in range(2, limit + 1):
        if spf[n] == n:
            is_prime[n] = True
            primes.append(n)
    return spf, is_prime, primes


def support_from_spf(n, spf):
    if n < 1 or n >= len(spf):
        raise ValueError("n must lie inside the SPF table")
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return tuple(out)


def factor_support(n):
    if n < 1:
        raise ValueError("factor_support expects a positive integer")
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return tuple(out)


def successors(face):
    if len(face) < 2:
        return tuple()
    return tuple(sorted({factor_support(a + b) for a, b in combinations(face, 2)}))


def analyze_support_orbit(start, max_depth):
    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    if not start or tuple(sorted(set(start))) != start:
        raise ValueError("start must be a nonempty strictly increasing face")
    levels, expanded, terminals, closure = [{start}], set(), set(), None
    for depth in range(max_depth + 1):
        level = levels[depth]
        terminals.update(face[0] for face in level if len(face) == 1)
        unresolved = [face for face in level if len(face) >= 2 and face not in expanded]
        if closure is None and not unresolved:
            closure = depth
        if depth == max_depth:
            break
        nxt = set()
        for face in level:
            if len(face) >= 2:
                expanded.add(face)
                nxt.update(successors(face))
        levels.append(nxt)
    return {
        "initial_support": list(start),
        "initial_support_key": face_key(start),
        "initial_radical": prod(start),
        "support_closure_depth": closure,
        "prime_pair_closure_depth": None if closure is None else closure + 1,
        "final_terminal_axes": sorted(terminals),
        "final_terminal_key": face_key(tuple(sorted(terminals))),
        "orbit_layers_from_support": [
            [list(face) for face in sorted(level)] for level in levels
        ],
    }


def closest_distinct_prime_pair(n, is_prime, primes):
    if n < 5 or n >= len(is_prime):
        return None
    if n % 2:
        q = n - 2
        return (2, q) if q > 2 and is_prime[q] else None
    i = bisect.bisect_left(primes, n / 2) - 1
    while i >= 0:
        p, q = primes[i], n - primes[i]
        if p < q and is_prime[q]:
            return p, q
        i -= 1
    return None


def distinct_prime_pair_count(n, is_prime, primes):
    if n % 2:
        return int(n >= 5 and is_prime[n - 2])
    count = 0
    for p in primes:
        if p >= n - p:
            break
        count += int(is_prime[n - p])
    return count


def make_record(n, pair, support, orbit):
    return {
        "sum": n,
        "prime_limit_threshold": pair[1],
        "closest_prime_pair": list(pair),
        "initial_support": list(support),
        "initial_support_key": face_key(support),
        "initial_radical": prod(support),
        "prime_pair_closure_depth": orbit["prime_pair_closure_depth"],
        "final_terminal_key": orbit["final_terminal_key"],
    }


def build_threshold_ladder(by_threshold, orbit_cache, is_prime, primes):
    current, out = 0, []
    for threshold in sorted(by_threshold):
        rows = by_threshold[threshold]
        new_depth = max(int(row["prime_pair_closure_depth"]) for row in rows)
        if new_depth <= current:
            continue
        witnesses = []
        for row in rows:
            if int(row["prime_pair_closure_depth"]) != new_depth:
                continue
            support = tuple(row["initial_support"])
            orbit = orbit_cache[support]
            witnesses.append({
                **row,
                "distinct_prime_pair_representation_count":
                    distinct_prime_pair_count(row["sum"], is_prime, primes),
                "orbit_layers_from_prime_pair_depth_1":
                    orbit["orbit_layers_from_support"][: orbit["support_closure_depth"] + 1],
                "final_terminal_axes": orbit["final_terminal_axes"],
            })
        out.append({
            "prime_limit_threshold": threshold,
            "previous_minimum_closure_depth": current,
            "new_minimum_closure_depth": new_depth,
            "witnesses": witnesses,
        })
        current = new_depth
    return out


def build_support_family(support, members, orbit, is_prime, primes):
    rows = []
    for member in sorted(members, key=lambda row: row["sum"]):
        rows.append({
            "sum": member["sum"],
            "closest_prime_pair": member["closest_prime_pair"],
            "prime_limit_threshold": member["prime_limit_threshold"],
            "distinct_prime_pair_representation_count":
                distinct_prime_pair_count(member["sum"], is_prime, primes),
        })
    return {
        "initial_support": list(support),
        "initial_support_key": face_key(support),
        "radical": prod(support),
        "prime_pair_closure_depth": orbit["prime_pair_closure_depth"],
        "final_terminal_axes": orbit["final_terminal_axes"],
        "final_terminal_key": orbit["final_terminal_key"],
        "orbit_layers_from_prime_pair_depth_1":
            orbit["orbit_layers_from_support"][: orbit["support_closure_depth"] + 1],
        "represented_sum_count_under_cap": len(rows),
        "represented_sums_under_cap": rows,
        "total_distinct_prime_pair_representations_under_cap":
            sum(row["distinct_prime_pair_representation_count"] for row in rows),
        "all_sums_have_same_support": all(
            tuple(member["initial_support"]) == support for member in members
        ),
    }


def analyze(sum_cap=REGISTERED_SUM_CAP, max_depth=REGISTERED_MAX_DEPTH,
            deep_depth_floor=REGISTERED_DEEP_DEPTH_FLOOR):
    if sum_cap < 10:
        raise ValueError("sum_cap must be at least 10")
    if max_depth < 1:
        raise ValueError("max_depth must be at least 1")
    if deep_depth_floor < 2:
        raise ValueError("deep_depth_floor must be at least 2")

    spf, is_prime, primes = sieve_tables(sum_cap)
    orbit_cache, by_threshold, by_support = {}, defaultdict(list), defaultdict(list)
    depth_distribution, represented_count, unresolved = Counter(), 0, set()

    for n in range(5, sum_cap + 1):
        pair = closest_distinct_prime_pair(n, is_prime, primes)
        if pair is None:
            continue
        represented_count += 1
        support = support_from_spf(n, spf)
        orbit = orbit_cache.get(support)
        if orbit is None:
            orbit = analyze_support_orbit(support, max_depth)
            orbit_cache[support] = orbit
        if orbit["prime_pair_closure_depth"] is None:
            unresolved.add(support)
            continue
        row = make_record(n, pair, support, orbit)
        by_threshold[pair[1]].append(row)
        by_support[support].append(row)
        depth_distribution[row["prime_pair_closure_depth"]] += 1

    ladder = build_threshold_ladder(by_threshold, orbit_cache, is_prime, primes)
    deep_ladder = [
        row for row in ladder if row["new_minimum_closure_depth"] >= deep_depth_floor
    ]
    deep_supports = {
        tuple(witness["initial_support"])
        for row in deep_ladder for witness in row["witnesses"]
    }
    families = [
        build_support_family(
            support, by_support[support], orbit_cache[support], is_prime, primes
        )
        for support in sorted(
            deep_supports, key=lambda f: orbit_cache[f]["prime_pair_closure_depth"]
        )
    ]
    threshold_pairs = [
        (row["prime_limit_threshold"], row["new_minimum_closure_depth"])
        for row in ladder
    ]
    prefix = [(3, 1), (7, 2), (19, 3), (31, 4), (73, 5), (359, 6)]
    maximum_depth = max(depth_distribution, default=0)

    verification = {
        "all_represented_sums_close_through_max_depth": not unresolved,
        "threshold_depths_are_strictly_increasing": all(
            a[1] < b[1] for a, b in zip(threshold_pairs, threshold_pairs[1:])
        ),
        "thresholds_are_strictly_increasing": all(
            a[0] < b[0] for a, b in zip(threshold_pairs, threshold_pairs[1:])
        ),
        "pass023_threshold_prefix_is_reproduced": threshold_pairs[:6] == prefix,
        "support_families_are_orbit_invariant": all(
            family["all_sums_have_same_support"] for family in families
        ),
        "closest_pairs_are_distinct_primes_and_reconstruct_sums": all(
            p < q and is_prime[p] and is_prime[q] and p + q == row["sum"]
            for rows in by_threshold.values() for row in rows
            for p, q in [tuple(row["closest_prime_pair"])]
        ),
        "record_depths_match_support_orbits": all(
            row["prime_pair_closure_depth"]
            == orbit_cache[tuple(row["initial_support"])]["prime_pair_closure_depth"]
            for rows in by_threshold.values() for row in rows
        ),
    }

    def first(depth):
        return next(
            (row["prime_limit_threshold"] for row in ladder
             if row["new_minimum_closure_depth"] >= depth),
            None,
        )

    return {
        "schema": "PVG-DEEP-ORBIT-PREIMAGE-FAMILIES-001",
        "classification": (
            "exact sum/support-fiber identities plus a finite verified prime-limit "
            "threshold search through the registered sum cap; no global termination "
            "or asymptotic depth-growth claim"
        ),
        "scope": {
            "sum_cap": sum_cap,
            "max_depth": max_depth,
            "deep_depth_floor": deep_depth_floor,
            "represented_sum_count": represented_count,
            "distinct_initial_support_count": len(orbit_cache),
        },
        "exact_identities": {
            "pair_successor_identity":
                "T({p,q})={supp(p+q)} for every two-axis start {p,q}",
            "sum_fiber_invariance":
                "equal sums imply identical dynamics from depth 1 onward",
            "support_fiber_invariance":
                "supp(p+q)=supp(r+s) implies identical dynamics from depth 1 onward",
            "support_preimage_characterization":
                "supp(n)=F iff n=product(p^e_p for p in F) with every e_p>=1",
        },
        "represented_sum_depth_distribution": {
            str(d): depth_distribution[d] for d in range(1, maximum_depth + 1)
        },
        "maximum_observed_prime_pair_closure_depth": maximum_depth,
        "no_depth_above_maximum_observed_through_sum_cap": True,
        "exact_prime_limit_threshold_ladder_through_sum_cap": ladder,
        "deep_prime_limit_threshold_ladder": deep_ladder,
        "deep_threshold_support_families": families,
        "first_depth_seven_threshold": first(7),
        "first_depth_eight_threshold": first(8),
        "first_depth_nine_threshold": first(9),
        "first_depth_ten_threshold": first(10),
        "first_depth_eleven_threshold": first(11),
        "first_depth_twelve_threshold": first(12),
        "verification": verification,
        "caution": (
            "The support-fiber identities are exact consequences of the transition "
            "definition. The threshold ladder is exhaustive only for represented sums "
            "n<=sum_cap, so absence of depth 12 is finite and cap-dependent."
        ),
    }


def registered_summary(data):
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Classify prime-pair sum/support fibers and deep PVG thresholds."
    )
    parser.add_argument("--sum-cap", type=int, default=REGISTERED_SUM_CAP)
    parser.add_argument("--max-depth", type=int, default=REGISTERED_MAX_DEPTH)
    parser.add_argument("--deep-depth-floor", type=int,
                        default=REGISTERED_DEEP_DEPTH_FLOOR)
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        data = analyze(args.sum_cap, args.max_depth, args.deep_depth_floor)
    except ValueError as exc:
        parser.error(str(exc))
    if args.registered_summary:
        data = registered_summary(data)
    print(json.dumps(
        data, ensure_ascii=False, sort_keys=True,
        indent=None if args.compact else 2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
