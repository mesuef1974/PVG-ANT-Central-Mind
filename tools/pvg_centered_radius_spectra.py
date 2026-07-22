from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
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

Spectrum = tuple[Fraction, ...]


def normalized_centered_radius_spectrum(n: int) -> Spectrum:
    """Return the exact shape spectrum {Delta/N} in increasing order."""
    if n <= 0:
        raise ValueError("n must be positive")
    return tuple(Fraction(gap, n) for gap in prime_gap_fiber(n))


def encode_spectrum(spectrum: Spectrum) -> tuple[str, ...]:
    return tuple(f"{value.numerator}/{value.denominator}" for value in spectrum)


def spectrum_relation(left: Spectrum, right: Spectrum) -> str:
    left_set = set(left)
    right_set = set(right)
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
    spectrum_classes: dict[Spectrum, list[dict[str, object]]] = defaultdict(list)
    radius_owners: dict[Fraction, list[int]] = defaultdict(list)

    for value, support in points:
        spectrum = normalized_centered_radius_spectrum(value)
        record = {
            "integer": value,
            "support": list(support),
            "multiplicity": len(spectrum),
        }
        spectrum_classes[spectrum].append(record)
        for radius in spectrum:
            radius_owners[radius].append(value)

    nonempty_classes = {
        spectrum: members for spectrum, members in spectrum_classes.items() if spectrum
    }
    collision_classes = [
        (spectrum, members)
        for spectrum, members in nonempty_classes.items()
        if len(members) > 1
    ]
    collision_classes.sort(
        key=lambda item: (-len(item[1]), encode_spectrum(item[0]), item[1][0]["integer"])
    )

    nonempty_spectra = tuple(nonempty_classes)
    containment_edges: list[dict[str, object]] = []
    for i, left in enumerate(nonempty_spectra):
        left_set = set(left)
        for right in nonempty_spectra[i + 1 :]:
            right_set = set(right)
            if left_set < right_set:
                containment_edges.append(
                    {"subset": list(encode_spectrum(left)), "superset": list(encode_spectrum(right))}
                )
            elif right_set < left_set:
                containment_edges.append(
                    {"subset": list(encode_spectrum(right)), "superset": list(encode_spectrum(left))}
                )

    shared_radii = [
        {
            "radius": f"{radius.numerator}/{radius.denominator}",
            "integer_count": len(set(owners)),
            "integers": sorted(set(owners))[:25],
        }
        for radius, owners in radius_owners.items()
        if len(set(owners)) > 1
    ]
    shared_radii.sort(key=lambda item: (-int(item["integer_count"]), str(item["radius"])))

    representable_point_count = sum(bool(spectrum) for spectrum in spectrum_classes for _ in spectrum_classes[spectrum])
    unique_nonempty_spectrum_count = len(nonempty_classes)

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
            "normalized_radius": "rho=Delta/N=(q-p)/(p+q)",
            "range": "0<rho<1 for every admitted distinct-prime pair",
            "reconstruction": "p/N=(1-rho)/2 and q/N=(1+rho)/2",
            "shape_meaning": "equal rho gives equal ordered prime proportions, not equal integers",
        },
        "totals": {
            "representable_point_count": representable_point_count,
            "unique_nonempty_spectrum_count": unique_nonempty_spectrum_count,
            "spectrum_collision_class_count": len(collision_classes),
            "proper_containment_edge_count": len(containment_edges),
            "shared_radius_value_count": len(shared_radii),
        },
        "compression": {
            "point_to_unique_spectrum_ratio": (
                None
                if representable_point_count == 0
                else f"{unique_nonempty_spectrum_count}/{representable_point_count}"
            ),
            "information_loss": "normalized spectra forget absolute scale N",
        },
        "largest_collision_classes": [
            {
                "spectrum": list(encode_spectrum(spectrum)),
                "class_size": len(members),
                "members": members[:25],
            }
            for spectrum, members in collision_classes[:25]
        ],
        "containment_edges": containment_edges[:100],
        "most_shared_radii": shared_radii[:25],
        "verification": {
            "all_radii_strictly_between_zero_and_one": all(
                0 < radius < 1 for spectrum in spectrum_classes for radius in spectrum
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
    parser = argparse.ArgumentParser(description="Analyze exact normalized centered-radius spectra.")
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
        spectrum = normalized_centered_radius_spectrum(args.integer)
        data = {
            "integer": args.integer,
            "spectrum": list(encode_spectrum(spectrum)),
            "multiplicity": len(spectrum),
        }

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
