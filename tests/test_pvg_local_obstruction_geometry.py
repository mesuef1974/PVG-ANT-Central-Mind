from __future__ import annotations

from tools.pvg_local_obstruction_geometry import (
    boundary_exception_record,
    even_coordinate_owner_certificate,
    local_obstruction_record,
    local_obstruction_signature,
    odd_coordinate_owner_certificate,
    primes_up_to,
)


def test_primes_up_to() -> None:
    assert primes_up_to(11) == (2, 3, 5, 7, 11)


def test_exact_residue_obstruction() -> None:
    record = local_obstruction_record(12, 3, 3)
    assert record["minus_residue_hit"]
    assert record["plus_residue_hit"]
    assert record["left_obstruction"]
    assert record["right_obstruction"]
    assert record["obstructed"]


def test_boundary_exception_is_not_obstruction() -> None:
    record = local_obstruction_record(8, 5, 3)
    assert record["left_boundary_exception"]
    assert not record["left_obstruction"]
    boundary = boundary_exception_record(8, 5, 3)
    assert boundary["is_boundary_exception"]


def test_even_owner_certificate() -> None:
    cert = even_coordinate_owner_certificate(24, 7, 11)
    assert cert["left"] == 5
    assert cert["right"] == 19
    assert cert["owner_by_primality"]
    assert cert["owner_by_registered_fiber"]
    assert cert["owner_equivalence"]
    assert cert["square_difference_identity"]
    assert cert["gcd_midpoint_radius"] == 1


def test_even_nonowner_certificate() -> None:
    cert = even_coordinate_owner_certificate(24, 3, 11)
    assert not cert["owner_by_primality"]
    assert not cert["owner_by_registered_fiber"]
    assert cert["owner_equivalence"]
    assert 3 in cert["local_signature"]["obstructing_primes"]


def test_local_survival_is_not_sufficient() -> None:
    # 77 and 83 are composite/prime; primes <= 5 do not detect the factor 7.
    cert = even_coordinate_owner_certificate(160, 3, 5)
    assert cert["left"] == 77
    assert cert["right"] == 83
    assert cert["local_signature"]["locally_survives"]
    assert not cert["owner_by_primality"]


def test_odd_route_owner_and_nonowner() -> None:
    represented = odd_coordinate_owner_certificate(21)
    assert represented["radius"] == 17
    assert represented["owner_by_primality"]
    assert represented["owner_equivalence"]

    empty = odd_coordinate_owner_certificate(27)
    assert empty["radius"] == 23
    assert not empty["owner_by_primality"]
    assert empty["owner_equivalence"]


def test_signature_separates_boundaries() -> None:
    signature = local_obstruction_signature(8, 5, 11)
    assert 3 in signature["boundary_exception_primes"]
    assert 3 not in signature["obstructing_primes"]
