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
    from tools.pvg_inverse_prime_fibers import prime_gap_fiber
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import (
        REGISTERED_INTEGER_CAP,
        REGISTERED_SUPPORT_FACE_SIZES,
        REGISTERED_SUPPORT_PRIME_LIMIT,
        integer_fiber,
        support_universe,
    )
    from pvg_inverse_prime_fibers import prime_gap_fiber

Spectrum = tuple[int, ...]


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


def registered_summary() -> dict[str, object]:
    points = registered_points()
    classes: dict[Spectrum, list[dict[str, object]]] = defaultdict(list)
    coordinate_owners: dict[int, list[int]] = defaultdict(list)

    for value, support in points:
        spectrum = centered_radius_spectrum(value)
        classes[spectrum].append(
            {"integer": value, "support": list(support), "multiplicity": len(spectrum)}
        )
        for coordinate in spectrum:
            coordinate_owners[coordinate].append(value)

    nonempty = {spectrum: members for spectrum, members in classes.items() if spectrum}
    collisions = sorted(
        ((spectrum, members) for spectrum, members in nonempty.items() if len(members) > 1),
        key=lambda item: (-len(item[1]), item[0], item[1][0]["integer"]),
    )
    spectra = tuple(nonempty)
    containments: list[dict[str, object]] = []
    for index, left in enumerate(spectra):
        for right in spectra[index + 1 :]:
            if set(left) < set(right):
                containments.append({"subset": list(left), "superset": list(right)})
            elif set(right) < set(left):
                containments.append({"subset": list(right), "superset": list(left)})

    shared = sorted(
        (
            {
                "coordinate": coordinate,
                "integer_count": len(set(owners)),
                "integers": sorted(set(owners))[:25],
            }
            for coordinate, owners in coordinate_owners.items()
            if len(set(owners)) > 1
        ),
        key=lambda item: (-int(item["integer_count"]), int(item["coordinate"])),
    )
    representable = sum(len(members) for spectrum, members in classes.items() if spectrum)

    return {
        "id": "ENGINE-004-CENTERED-RADIUS-SPECTRA-SUMMARY-001",
        "classification": "Identity / Finite-Verified / Diagnostic",
        "scope": {
            "support_prime_limit": REGISTERED_SUPPORT_PRIME_LIMIT,
            "support_face_sizes": list(REGISTERED_SUPPORT_FACE_SIZES),
            "integer_cap": REGISTERED_INTEGER_CAP,
            "integer_point_count": len(points),
        },
        "exact_laws": {
            "even_spectrum": "D(N)={Delta/2:Delta in Delta_2(N)} for even N",
            "odd_spectrum": "D(N)=Delta_2(N) for odd N",
            "even_coordinate": "for N=2m and Delta=2d, d=(q-p)/2 and gcd(m,d)=1",
            "separation": "support, integer, pair fiber, gap spectrum, and radius spectrum remain distinct layers",
        },
        "totals": {
            "representable_point_count": representable,
            "unique_nonempty_spectrum_count": len(nonempty),
            "spectrum_collision_class_count": len(collisions),
            "proper_containment_edge_count": len(containments),
            "shared_coordinate_value_count": len(shared),
        },
        "compression": {
            "point_to_unique_spectrum_ratio": None if not representable else f"{len(nonempty)}/{representable}",
            "information_loss": "the spectrum projection forgets the integer and prime-pair labels",
        },
        "largest_collision_classes": [
            {"spectrum": list(spectrum), "class_size": len(members), "members": members[:25]}
            for spectrum, members in collisions[:25]
        ],
        "containment_edges": containments[:100],
        "most_shared_coordinates": shared[:25],
        "verification": {
            "even_coordinates_are_positive_integers": all(
                all(value > 0 for value in spectrum)
                for spectrum, members in classes.items()
                if spectrum and all(int(member["integer"]) % 2 == 0 for member in members)
            ),
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
        spectrum = centered_radius_spectrum(args.integer)
        data = {"integer": args.integer, "spectrum": list(spectrum), "multiplicity": len(spectrum)}
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
