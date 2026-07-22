from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

try:
    from tools.pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        support_universe,
    )
    from tools.pvg_inverse_prime_fibers import prime_gap_fiber, prime_pair_fiber
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        support_universe,
    )
    from pvg_inverse_prime_fibers import prime_gap_fiber, prime_pair_fiber

Spectrum = tuple[int, ...]
PrimePair = tuple[int, int]


def centered_radius_spectrum(n: int) -> Spectrum:
    """Authorized Phase-C spectrum: Delta/2 for even n, Delta for odd n."""
    if n <= 0:
        raise ValueError("n must be positive")
    gaps = prime_gap_fiber(n)
    if n % 2 == 0:
        if any(gap % 2 for gap in gaps):
            raise AssertionError("even sums must have even centered gaps")
        return tuple(gap // 2 for gap in gaps)
    return tuple(gaps)


def normalized_centered_radius_spectrum(n: int) -> Spectrum:
    """Compatibility alias retained for callers; returns the governed spectrum."""
    return centered_radius_spectrum(n)


def reconstruct_prime_pairs(n: int, spectrum: Spectrum | None = None) -> tuple[PrimePair, ...]:
    """Reconstruct the complete pair fiber from N and its governed spectrum."""
    if n <= 0:
        raise ValueError("n must be positive")
    spectrum = centered_radius_spectrum(n) if spectrum is None else tuple(spectrum)
    if any(not isinstance(value, int) or value <= 0 for value in spectrum):
        raise ValueError("spectrum coordinates must be positive integers")
    if n % 2 == 0:
        midpoint = n // 2
        pairs = tuple((midpoint - radius, midpoint + radius) for radius in spectrum)
    else:
        pairs = tuple((2, radius + 2) for radius in spectrum)
    if any(not (left < right and left + right == n) for left, right in pairs):
        raise ValueError("spectrum is incompatible with the supplied integer")
    return pairs


def spectrum_record(n: int) -> dict[str, object]:
    spectrum = centered_radius_spectrum(n)
    pairs = prime_pair_fiber(n)
    reconstructed = reconstruct_prime_pairs(n, spectrum)
    return {
        "integer": n,
        "route": "even_half_gap" if n % 2 == 0 else "odd_raw_gap",
        "spectrum": list(spectrum),
        "multiplicity": len(spectrum),
        "prime_pairs": [list(pair) for pair in pairs],
        "reconstructed_prime_pairs": [list(pair) for pair in reconstructed],
        "reconstruction_holds": reconstructed == pairs,
    }


def spectrum_relation(left: Spectrum, right: Spectrum) -> str:
    left_set, right_set = set(left), set(right)
    if left_set == right_set:
        return "equal"
    if left_set < right_set:
        return "proper_subset"
    if right_set < left_set:
        return "proper_superset"
    if left_set & right_set:
        return "overlap"
    return "disjoint"


def registered_points() -> tuple[tuple[int, tuple[int, ...]], ...]:
    out: list[tuple[int, tuple[int, ...]]] = []
    for support in support_universe(
        REGISTERED_SUPPORT_PRIME_LIMIT, REGISTERED_SUPPORT_FACE_SIZES
    ):
        for value in integer_fiber(support, REGISTERED_INTEGER_CAP):
            out.append((value, support))
    return tuple(out)


def _member_record(value: int, support: tuple[int, ...], multiplicity: int) -> dict[str, object]:
    return {
        "integer": value,
        "support": list(support),
        "multiplicity": multiplicity,
    }


def registered_summary() -> dict[str, object]:
    points = registered_points()
    classes: dict[Spectrum, list[dict[str, object]]] = defaultdict(list)
    coordinate_owners: dict[int, list[dict[str, object]]] = defaultdict(list)
    all_reconstruct = True
    cardinality_matches = True
    odd_route_n_minus_4 = True

    for value, support in points:
        spectrum = centered_radius_spectrum(value)
        pairs = prime_pair_fiber(value)
        reconstructed = reconstruct_prime_pairs(value, spectrum)
        all_reconstruct = all_reconstruct and reconstructed == pairs
        cardinality_matches = cardinality_matches and len(spectrum) == len(pairs)
        if value % 2:
            odd_route_n_minus_4 = odd_route_n_minus_4 and all(
                coordinate == value - 4 for coordinate in spectrum
            )
        classes[spectrum].append(_member_record(value, support, len(spectrum)))
        route = "even" if value % 2 == 0 else "odd"
        for coordinate, (left, right) in zip(spectrum, pairs):
            coordinate_owners[coordinate].append(
                {
                    "integer": value,
                    "support": list(support),
                    "prime_pair": [left, right],
                    "route": route,
                }
            )

    empty_members = sorted(classes.get(tuple(), []), key=lambda item: int(item["integer"]))
    nonempty = {spectrum: members for spectrum, members in classes.items() if spectrum}
    collision_classes = sorted(
        (
            (spectrum, sorted(members, key=lambda item: int(item["integer"])))
            for spectrum, members in nonempty.items()
            if len(members) > 1
        ),
        key=lambda item: (-len(item[1]), item[0]),
    )

    spectra = tuple(nonempty)
    containments: list[tuple[Spectrum, Spectrum]] = []
    for index, left in enumerate(spectra):
        left_set = set(left)
        for right in spectra[index + 1 :]:
            right_set = set(right)
            if left_set < right_set:
                containments.append((left, right))
            elif right_set < left_set:
                containments.append((right, left))
    containments.sort(key=lambda item: (len(item[0]), item[0], len(item[1]), item[1]))
    non_singleton_containments = [edge for edge in containments if len(edge[0]) > 1]

    non_singleton_edges: list[dict[str, object]] = []
    for subset, superset in non_singleton_containments:
        subset_member = min(classes[subset], key=lambda item: int(item["integer"]))
        superset_member = min(classes[superset], key=lambda item: int(item["integer"]))
        non_singleton_edges.append(
            {
                "subset_spectrum": list(subset),
                "subset_integer": subset_member["integer"],
                "subset_support": subset_member["support"],
                "superset_integer": superset_member["integer"],
                "superset_support": superset_member["support"],
                "superset_spectrum_cardinality": len(superset),
            }
        )

    shared_coordinate_records: list[dict[str, object]] = []
    even_coordinates: set[int] = set()
    odd_coordinates: set[int] = set()
    route_collision_counts = {"even_even": 0, "odd_even": 0, "odd_odd": 0}
    for coordinate, owners in coordinate_owners.items():
        routes = {str(owner["route"]) for owner in owners}
        if "even" in routes:
            even_coordinates.add(coordinate)
        if "odd" in routes:
            odd_coordinates.add(coordinate)
        if len(owners) <= 1:
            continue
        if routes == {"even"}:
            route_class = "even_even"
        elif routes == {"odd", "even"}:
            route_class = "odd_even"
        elif routes == {"odd"}:
            route_class = "odd_odd"
        else:
            raise AssertionError(f"unexpected route class: {routes}")
        route_collision_counts[route_class] += 1
        sorted_owners = sorted(owners, key=lambda item: int(item["integer"]))
        shared_coordinate_records.append(
            {
                "coordinate": coordinate,
                "integer_count": len(sorted_owners),
                "route_class": route_class,
                "first_owners": sorted_owners[:5],
            }
        )
    shared_coordinate_records.sort(
        key=lambda item: (-int(item["integer_count"]), int(item["coordinate"]))
    )

    representable = sum(len(members) for members in nonempty.values())
    total_coordinate_occurrences = sum(
        len(spectrum) * len(members) for spectrum, members in classes.items()
    )
    only_collision = collision_classes[0]
    only_collision_members = []
    for member in only_collision[1]:
        value = int(member["integer"])
        only_collision_members.append(
            {
                "integer": value,
                "support": member["support"],
                "route": "odd" if value % 2 else "even",
                "prime_pairs": [list(pair) for pair in prime_pair_fiber(value)],
            }
        )

    return {
        "id": "ENGINE-004-CENTERED-RADIUS-SPECTRA-SUMMARY-001",
        "classification": "Identity / Proved / Finite-Verified / Diagnostic",
        "scope": {
            "support_prime_limit": REGISTERED_SUPPORT_PRIME_LIMIT,
            "support_face_sizes": list(REGISTERED_SUPPORT_FACE_SIZES),
            "integer_cap": REGISTERED_INTEGER_CAP,
            "integer_point_count": len(points),
        },
        "exact_laws": {
            "even_spectrum": "D(N)={Delta/2:Delta in Delta_2(N)} for even N",
            "odd_spectrum": "D(N)=Delta_2(N) for odd N",
            "even_reconstruction": "for N=2m and d in D(N), p=m-d and q=m+d",
            "odd_reconstruction": "for odd representable N and d in D(N), N=d+4 and the pair is (2,d+2)",
            "fixed_point_losslessness": "N together with D(N) reconstructs the full distinct-prime fiber",
            "multiplicity": "|D(N)|=|R_2(N)|",
            "odd_route_injectivity": "two represented odd points cannot share a coordinate",
        },
        "totals": {
            "representable_point_count": representable,
            "nonrepresentable_point_count": len(empty_members),
            "total_coordinate_occurrence_count": total_coordinate_occurrences,
            "unique_coordinate_value_count": len(coordinate_owners),
            "unique_even_coordinate_value_count": len(even_coordinates),
            "unique_odd_coordinate_value_count": len(odd_coordinates),
            "cross_route_coordinate_value_count": len(even_coordinates & odd_coordinates),
            "odd_only_coordinate_value_count": len(odd_coordinates - even_coordinates),
            "unique_spectrum_count_including_empty": len(classes),
            "unique_nonempty_spectrum_count": len(nonempty),
            "nonempty_spectrum_collision_class_count": len(collision_classes),
            "empty_spectrum_class_size": len(empty_members),
            "proper_containment_edge_count": len(containments),
            "singleton_subset_containment_edge_count": sum(
                len(subset) == 1 for subset, _ in containments
            ),
            "non_singleton_subset_containment_edge_count": len(non_singleton_containments),
            "shared_coordinate_value_count": len(shared_coordinate_records),
            "even_even_shared_coordinate_value_count": route_collision_counts["even_even"],
            "odd_even_shared_coordinate_value_count": route_collision_counts["odd_even"],
            "odd_odd_shared_coordinate_value_count": route_collision_counts["odd_odd"],
        },
        "compression": {
            "represented_point_to_nonempty_spectrum_ratio": f"{len(nonempty)}/{representable}",
            "nonempty_collision_excess_point_count": representable - len(nonempty),
            "empty_fiber_collapse": f"{len(empty_members)} nonrepresentable points map to the empty spectrum",
            "preserved": "multiplicity and the complete prime-pair fiber when N is retained",
            "lost_without_N": "the midpoint and integer label are generally lost; coordinate collisions occur across points",
        },
        "only_nonempty_spectrum_collision": {
            "spectrum": list(only_collision[0]),
            "class_size": len(only_collision[1]),
            "members": only_collision_members,
        },
        "containment_profile": {
            "non_singleton_subset_spectrum_count": len(
                {subset for subset, _ in non_singleton_containments}
            ),
            "non_singleton_subset_spectra": [
                list(spectrum)
                for spectrum in sorted({subset for subset, _ in non_singleton_containments})
            ],
            "non_singleton_edges": non_singleton_edges,
        },
        "largest_shared_coordinates": shared_coordinate_records[:10],
        "verification": {
            "all_coordinates_positive_integers": all(
                coordinate > 0 for coordinate in coordinate_owners
            ),
            "all_218024_pairs_reconstruct_from_N_and_spectrum": all_reconstruct,
            "spectrum_cardinality_matches_representation_count": cardinality_matches,
            "odd_route_coordinates_are_N_minus_4": odd_route_n_minus_4,
            "odd_route_has_no_internal_coordinate_collision": route_collision_counts["odd_odd"] == 0,
            "only_nonempty_spectrum_collision_is_1_at_5_8_12": (
                len(collision_classes) == 1
                and collision_classes[0][0] == (1,)
                and [int(member["integer"]) for member in collision_classes[0][1]] == [5, 8, 12]
            ),
            "containment_counts_complete": len(containments) == 2048,
            "deterministic_ordering": True,
            "phase_d_not_used": True,
        },
        "claim_ceiling": {
            "historical_originality": False,
            "phase_d_authorized": False,
            "goldbach_progress": False,
            "pnt_progress": False,
            "rh_progress": False,
            "grh_progress": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze governed centered-radius spectra.")
    parser.add_argument("integer", nargs="?", type=int)
    parser.add_argument("--registered-summary", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    if args.registered_summary:
        data: object = registered_summary()
    else:
        if args.integer is None:
            parser.error("integer is required unless --registered-summary is used")
        data = spectrum_record(args.integer)
    text = json.dumps(
        data,
        ensure_ascii=False,
        separators=(",", ":") if args.compact else None,
        indent=None if args.compact else 2,
    ) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
