from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

try:
    from tools.pvg_local_additive_cell_atlas import factorint, primes_up_to
except ModuleNotFoundError:
    from pvg_local_additive_cell_atlas import factorint, primes_up_to

Face = tuple[int, ...]
REGISTERED_LIMITS = (100, 150, 200, 250, 300, 350, 400, 450, 500)
REGISTERED_MIN_DEPTH = 0
REGISTERED_MAX_DEPTH = 8


def face_key(face: Face | list[int]) -> str:
    return "{" + ",".join(str(x) for x in face) + "}"


def parse_limits(text: str) -> tuple[int, ...]:
    try:
        limits = tuple(int(part.strip()) for part in text.split(",") if part.strip())
    except ValueError as exc:
        raise ValueError("limits must be comma-separated integers") from exc
    if not limits:
        raise ValueError("at least one prime limit is required")
    if tuple(sorted(set(limits))) != limits:
        raise ValueError("limits must be strictly increasing with no duplicates")
    if any(limit < 3 for limit in limits):
        raise ValueError("every prime limit must be at least 3")
    return limits


def support(n: int) -> Face:
    return tuple(sorted(int(p) for p in factorint(n))) if n > 1 else tuple()


def successors(face: Face) -> tuple[Face, ...]:
    if len(face) < 2:
        return tuple()
    return tuple(sorted({support(a + b) for a, b in combinations(face, 2)}))


def analyze_start_profile(start: Face, max_depth: int) -> dict[str, object]:
    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    if len(start) < 2 or tuple(sorted(set(start))) != start:
        raise ValueError("start must be a strictly increasing face of size at least two")

    levels: list[set[Face]] = [{start}]
    expanded_composite_faces: set[Face] = set()
    terminal_axes: set[int] = set()
    signatures_by_depth: list[Face] = []
    unresolved_by_depth: list[list[Face]] = []
    closure_depth: int | None = None

    for depth in range(max_depth + 1):
        level = levels[depth]
        terminal_axes.update(face[0] for face in level if len(face) == 1)
        signatures_by_depth.append(tuple(sorted(terminal_axes)))
        unresolved = sorted(
            face
            for face in level
            if len(face) >= 2 and face not in expanded_composite_faces
        )
        unresolved_by_depth.append(unresolved)
        if closure_depth is None and not unresolved:
            closure_depth = depth
        if depth == max_depth:
            break
        next_level: set[Face] = set()
        for face in level:
            if len(face) >= 2:
                expanded_composite_faces.add(face)
            next_level.update(successors(face))
        levels.append(next_level)

    final_signature = signatures_by_depth[-1]
    stabilization_depth = next(
        depth
        for depth in range(max_depth + 1)
        if all(signature == final_signature for signature in signatures_by_depth[depth:])
    )
    first_terminal_depth = next(
        (depth for depth, signature in enumerate(signatures_by_depth) if signature),
        None,
    )

    return {
        "start_face": list(start),
        "start_key": face_key(start),
        "start_sum": sum(start),
        "max_depth": max_depth,
        "first_bounded_closure_depth": closure_depth,
        "observed_signature_stabilization_depth": stabilization_depth,
        "first_terminal_depth": first_terminal_depth,
        "final_terminal_axes": list(final_signature),
        "final_terminal_key": face_key(final_signature),
        "closure_minus_stabilization_gap": (
            None if closure_depth is None else closure_depth - stabilization_depth
        ),
        "endpoint_signatures_by_depth": [
            {
                "depth": depth,
                "terminal_axes": list(signature),
                "terminal_key": face_key(signature),
            }
            for depth, signature in enumerate(signatures_by_depth)
        ],
        "unresolved_frontier_by_depth": [
            {
                "depth": depth,
                "faces": [list(face) for face in frontier],
                "keys": [face_key(face) for face in frontier],
            }
            for depth, frontier in enumerate(unresolved_by_depth)
        ],
        "layer_faces": [
            [list(face) for face in sorted(level)]
            for level in levels
        ],
    }


def _depth_distribution(
    profiles: list[dict[str, object]], field: str, max_depth: int
) -> dict[str, int]:
    counts = Counter(
        int(profile[field])
        for profile in profiles
        if profile[field] is not None
    )
    return {str(depth): counts[depth] for depth in range(max_depth + 1)}


def _orbit_tail_key(profile: dict[str, object]) -> tuple[tuple[Face, ...], ...]:
    closure_depth = int(profile["first_bounded_closure_depth"])
    return tuple(
        tuple(tuple(int(x) for x in face) for face in layer)
        for layer in profile["layer_faces"][1 : closure_depth + 1]
    )


def _orbit_groups(profiles: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[tuple[Face, ...], ...], list[dict[str, object]]] = defaultdict(list)
    for profile in profiles:
        grouped[_orbit_tail_key(profile)].append(profile)
    out: list[dict[str, object]] = []
    for tail, members in grouped.items():
        sums = sorted({int(member["start_sum"]) for member in members})
        out.append(
            {
                "start_face_count": len(members),
                "start_faces": [member["start_face"] for member in members],
                "start_keys": [member["start_key"] for member in members],
                "start_sums": sums,
                "all_start_sums_equal": len(sums) == 1,
                "orbit_tail_from_depth_1": [
                    [list(face) for face in layer] for layer in tail
                ],
                "final_terminal_axes": members[0]["final_terminal_axes"],
                "final_terminal_key": members[0]["final_terminal_key"],
            }
        )
    return sorted(out, key=lambda row: (-int(row["start_face_count"]), row["start_keys"]))


def _snapshot(
    limit: int,
    profiles: list[dict[str, object]],
    max_depth: int,
) -> dict[str, object]:
    selected = [profile for profile in profiles if int(profile["start_face"][1]) <= limit]
    prime_count = len(primes_up_to(limit))
    unresolved = [
        profile for profile in selected
        if profile["first_bounded_closure_depth"] is None
    ]
    resolved = [
        profile for profile in selected
        if profile["first_bounded_closure_depth"] is not None
    ]
    minimum_closure_depth = (
        max(int(profile["first_bounded_closure_depth"]) for profile in resolved)
        if resolved and not unresolved
        else None
    )
    maximum_observed_closure_depth = max(
        (int(profile["first_bounded_closure_depth"]) for profile in resolved),
        default=None,
    )
    maximum_depth_profiles = [
        profile for profile in resolved
        if int(profile["first_bounded_closure_depth"]) == maximum_observed_closure_depth
    ]
    gaps = Counter(
        int(profile["closure_minus_stabilization_gap"])
        for profile in resolved
    )
    maximum_gap = max(gaps, default=0)
    maximum_gap_profiles = [
        profile for profile in resolved
        if int(profile["closure_minus_stabilization_gap"]) == maximum_gap
    ]
    max_signature_distribution = Counter(
        tuple(int(x) for x in profile["final_terminal_axes"])
        for profile in maximum_depth_profiles
    )

    return {
        "prime_limit": limit,
        "prime_count": prime_count,
        "start_face_count": len(selected),
        "expected_start_face_count": comb(prime_count, 2),
        "all_starts_closed_through_max_depth": not unresolved,
        "unresolved_through_max_depth_count": len(unresolved),
        "unresolved_start_faces": [profile["start_face"] for profile in unresolved],
        "minimum_closure_depth": minimum_closure_depth,
        "maximum_observed_closure_depth": maximum_observed_closure_depth,
        "closure_depth_distribution": _depth_distribution(
            selected, "first_bounded_closure_depth", max_depth
        ),
        "signature_stabilization_depth_distribution": _depth_distribution(
            selected, "observed_signature_stabilization_depth", max_depth
        ),
        "closure_minus_stabilization_gap_distribution": {
            str(gap): gaps[gap] for gap in sorted(gaps)
        },
        "maximum_closure_minus_stabilization_gap": maximum_gap,
        "maximum_gap_start_faces": [
            profile["start_face"] for profile in maximum_gap_profiles
        ],
        "maximum_gap_final_signatures": sorted(
            {profile["final_terminal_key"] for profile in maximum_gap_profiles}
        ),
        "maximum_depth_start_count": len(maximum_depth_profiles),
        "maximum_depth_start_faces": [
            profile["start_face"] for profile in maximum_depth_profiles
        ],
        "maximum_depth_start_sums": sorted(
            {int(profile["start_sum"]) for profile in maximum_depth_profiles}
        ),
        "maximum_depth_terminal_signature_distribution": {
            face_key(signature): count
            for signature, count in sorted(max_signature_distribution.items())
        },
        "maximum_depth_orbit_groups": _orbit_groups(maximum_depth_profiles),
    }


def _threshold_ladder(
    profiles: list[dict[str, object]], max_limit: int
) -> list[dict[str, object]]:
    by_upper_axis: dict[int, list[dict[str, object]]] = defaultdict(list)
    for profile in profiles:
        by_upper_axis[int(profile["start_face"][1])].append(profile)
    current_depth = 0
    out: list[dict[str, object]] = []
    for threshold in sorted(axis for axis in by_upper_axis if axis <= max_limit):
        profiles_here = by_upper_axis[threshold]
        new_depth = max(
            int(profile["first_bounded_closure_depth"])
            for profile in profiles_here
            if profile["first_bounded_closure_depth"] is not None
        )
        if new_depth <= current_depth:
            continue
        witnesses = [
            profile for profile in profiles_here
            if int(profile["first_bounded_closure_depth"]) == new_depth
        ]
        out.append(
            {
                "prime_limit_threshold": threshold,
                "previous_minimum_closure_depth": current_depth,
                "new_minimum_closure_depth": new_depth,
                "witness_start_faces": [profile["start_face"] for profile in witnesses],
                "witness_start_keys": [profile["start_key"] for profile in witnesses],
                "witness_final_terminal_keys": sorted(
                    {profile["final_terminal_key"] for profile in witnesses}
                ),
            }
        )
        current_depth = new_depth
    return out


def analyze(
    limits: tuple[int, ...] = REGISTERED_LIMITS,
    min_depth: int = REGISTERED_MIN_DEPTH,
    max_depth: int = REGISTERED_MAX_DEPTH,
    include_profiles: bool = True,
) -> dict[str, object]:
    if tuple(sorted(set(limits))) != limits or not limits:
        raise ValueError("limits must be a nonempty strictly increasing tuple")
    if any(limit < 3 for limit in limits):
        raise ValueError("every prime limit must be at least 3")
    if min_depth != 0:
        raise ValueError("min_depth must be zero for minimum-depth measurement")
    if max_depth < min_depth:
        raise ValueError("max_depth must be at least min_depth")

    maximum_limit = limits[-1]
    primes = primes_up_to(maximum_limit)
    profiles = [
        analyze_start_profile((p, q), max_depth)
        for p, q in combinations(primes, 2)
    ]
    snapshots = [_snapshot(limit, profiles, max_depth) for limit in limits]
    threshold_ladder = _threshold_ladder(profiles, maximum_limit)
    minimum_depth_series = [snapshot["minimum_closure_depth"] for snapshot in snapshots]

    depth_six_threshold = next(
        (
            row["prime_limit_threshold"]
            for row in threshold_ladder
            if row["new_minimum_closure_depth"] >= 6
        ),
        None,
    )
    depth_seven_threshold = next(
        (
            row["prime_limit_threshold"]
            for row in threshold_ladder
            if row["new_minimum_closure_depth"] >= 7
        ),
        None,
    )

    verification = {
        "start_counts_match_prime_pair_counts": all(
            snapshot["start_face_count"] == snapshot["expected_start_face_count"]
            for snapshot in snapshots
        ),
        "all_registered_starts_close_through_max_depth": all(
            snapshot["all_starts_closed_through_max_depth"] for snapshot in snapshots
        ),
        "minimum_closure_depth_is_nondecreasing": all(
            minimum_depth_series[index] <= minimum_depth_series[index + 1]
            for index in range(len(minimum_depth_series) - 1)
        ),
        "closure_is_never_before_signature_stabilization": all(
            profile["first_bounded_closure_depth"] is None
            or int(profile["first_bounded_closure_depth"])
            >= int(profile["observed_signature_stabilization_depth"])
            for profile in profiles
        ),
        "profile_partitions_close": all(
            sum(snapshot["closure_depth_distribution"].values())
            + snapshot["unresolved_through_max_depth_count"]
            == snapshot["start_face_count"]
            for snapshot in snapshots
        ),
        "threshold_ladder_depths_are_strictly_increasing": all(
            threshold_ladder[index]["new_minimum_closure_depth"]
            < threshold_ladder[index + 1]["new_minimum_closure_depth"]
            for index in range(len(threshold_ladder) - 1)
        ),
        "all_depth_layers_match_successor_union": all(
            {tuple(int(x) for x in face) for face in target_layer}
            == {
                target
                for source_list in source_layer
                for source in [tuple(int(x) for x in source_list)]
                for target in successors(source)
            }
            for profile in profiles
            for source_layer, target_layer in zip(
                profile["layer_faces"][:-1], profile["layer_faces"][1:]
            )
        ),
    }

    result: dict[str, object] = {
        "schema": "PVG-MINIMUM-CLOSURE-DEPTH-GROWTH-001",
        "classification": (
            "finite verified minimum-closure-depth growth over a registered prime-bound ladder; "
            "no general termination, asymptotic, or universal depth-growth claim"
        ),
        "scope": {
            "registered_limits": list(limits),
            "min_depth": min_depth,
            "max_depth": max_depth,
            "depth_values": list(range(min_depth, max_depth + 1)),
            "start_family": "all unordered prime-pair faces {p,q} with p<q<=L",
        },
        "limit_snapshots": snapshots,
        "exact_threshold_ladder_through_maximum_limit": threshold_ladder,
        "first_depth_six_threshold": depth_six_threshold,
        "first_depth_seven_threshold": depth_seven_threshold,
        "no_depth_seven_required_through_maximum_limit": depth_seven_threshold is None,
        "minimum_closure_depth_series": minimum_depth_series,
        "verification": verification,
        "caution": (
            "The exact threshold ladder is exhaustive only through the registered maximum prime limit. "
            "Absence of depth 7 through that limit is not a global depth-6 bound or a termination theorem."
        ),
    }
    if include_profiles:
        result["start_profiles"] = profiles
    return result


def registered_summary(data: dict[str, object]) -> dict[str, object]:
    snapshots = data["limit_snapshots"]
    maximum_registered_limit = snapshots[-1]["prime_limit"]
    limit_table: list[dict[str, object]] = []
    for snapshot in snapshots:
        row: dict[str, object] = {
            "prime_limit": snapshot["prime_limit"],
            "prime_count": snapshot["prime_count"],
            "start_face_count": snapshot["start_face_count"],
            "minimum_closure_depth": snapshot["minimum_closure_depth"],
            "closure_depth_distribution": snapshot["closure_depth_distribution"],
            "signature_stabilization_depth_distribution": snapshot[
                "signature_stabilization_depth_distribution"
            ],
            "maximum_closure_minus_stabilization_gap": snapshot[
                "maximum_closure_minus_stabilization_gap"
            ],
            "maximum_gap_start_count": len(snapshot["maximum_gap_start_faces"]),
            "maximum_depth_start_count": snapshot["maximum_depth_start_count"],
            "maximum_depth_start_faces": (
                snapshot["maximum_depth_start_faces"]
                if int(snapshot["minimum_closure_depth"]) >= 6
                else []
            ),
            "maximum_depth_start_sums": snapshot["maximum_depth_start_sums"],
            "maximum_depth_terminal_signature_distribution": snapshot[
                "maximum_depth_terminal_signature_distribution"
            ],
        }
        if snapshot["prime_limit"] == maximum_registered_limit:
            row["maximum_gap_start_faces"] = snapshot["maximum_gap_start_faces"]
            row["maximum_gap_final_signatures"] = snapshot[
                "maximum_gap_final_signatures"
            ]
            row["maximum_depth_orbit_groups"] = snapshot[
                "maximum_depth_orbit_groups"
            ]
        limit_table.append(row)
    return {
        "schema": data["schema"],
        "classification": data["classification"],
        "scope": data["scope"],
        "limit_table": limit_table,
        "exact_threshold_ladder_through_maximum_limit": data[
            "exact_threshold_ladder_through_maximum_limit"
        ],
        "first_depth_six_threshold": data["first_depth_six_threshold"],
        "first_depth_seven_threshold": data["first_depth_seven_threshold"],
        "no_depth_seven_required_through_maximum_limit": data[
            "no_depth_seven_required_through_maximum_limit"
        ],
        "minimum_closure_depth_series": data["minimum_closure_depth_series"],
        "verification": data["verification"],
        "caution": data["caution"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Measure finite minimum additive-face closure depth across expanding prime bounds."
    )
    parser.add_argument(
        "--limits",
        default=",".join(str(limit) for limit in REGISTERED_LIMITS),
        help="strictly increasing comma-separated prime limits",
    )
    parser.add_argument("--min-depth", type=int, default=REGISTERED_MIN_DEPTH)
    parser.add_argument("--max-depth", type=int, default=REGISTERED_MAX_DEPTH)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        limits = parse_limits(args.limits)
        data = analyze(
            limits,
            args.min_depth,
            args.max_depth,
            include_profiles=not args.summary_only,
        )
    except ValueError as exc:
        parser.error(str(exc))
    if args.registered_summary:
        data = registered_summary(data)
    print(
        json.dumps(
            data,
            ensure_ascii=False,
            sort_keys=True,
            indent=None if args.compact else 2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
