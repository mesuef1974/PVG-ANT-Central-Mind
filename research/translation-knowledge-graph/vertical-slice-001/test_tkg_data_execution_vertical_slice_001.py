from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from benchmark_contamination_audit import CLEAN_RULE_ONLY, audit_case
from tkg_data_execution_vertical_slice_001 import (
    INSUFFICIENT_KNOWLEDGE,
    ExecutionComposer,
    RegistryLoader,
    construct_divisor_box,
    enumerate_divisors,
    factor_integer,
)

REGISTRY = Path(__file__).resolve().parents[1] / "registry" / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"


def load_nodes():
    return RegistryLoader().load(REGISTRY)


def test_registry_loader_exposes_normalized_model():
    nodes = load_nodes()
    tau = next(node for node in nodes if node.node_id == "TKG002-NODE-TAU")
    assert tau.names == ("divisor-counting function tau",)
    assert "tau=1*1" in tau.equivalent_forms
    assert tau.formulas
    assert tau.examples
    assert tau.claim_ceiling == "Finite divisor geometry only."


def test_contamination_audit_accepts_only_clean_new_cases():
    nodes = load_nodes()
    tau = audit_case(
        nodes,
        n=360,
        expected_result=24,
        factorization=factor_integer(360),
        divisors=enumerate_divisors(360),
    )
    sigma = audit_case(
        nodes,
        n=4620,
        expected_result=16128,
        factorization=factor_integer(4620),
        divisors=enumerate_divisors(4620),
    )
    assert tau.classification == CLEAN_RULE_ONLY
    assert sigma.classification == CLEAN_RULE_ONLY


def test_tau_360_is_computed_from_registry_rule_with_provenance():
    answer = ExecutionComposer(load_nodes()).answer("Compute tau(360)")
    assert answer.status == "EXECUTED_FROM_REGISTRY_RULE"
    assert answer.result == 24
    assert answer.matched_node_ids == ("TKG002-NODE-TAU",)
    assert all(bool(step.source_node_id) ^ bool(step.operator_id) for step in answer.steps)
    assert 24 not in [step.value for step in answer.steps[:-1]]


def test_sigma_4620_is_computed_from_registry_rule_with_provenance():
    answer = ExecutionComposer(load_nodes()).answer("Compute sigma(4620)")
    assert answer.status == "EXECUTED_FROM_REGISTRY_RULE"
    assert answer.result == 16128
    assert answer.matched_node_ids == ("TKG002-NODE-SIGMA",)
    assert all(bool(step.source_node_id) ^ bool(step.operator_id) for step in answer.steps)


def test_deleting_examples_does_not_break_new_derivation():
    nodes = [replace(node, examples=()) for node in load_nodes()]
    assert ExecutionComposer(nodes).answer("Compute tau(360)").result == 24
    assert ExecutionComposer(nodes).answer("Compute sigma(4620)").result == 16128


def test_deleting_rule_but_keeping_examples_blocks_new_derivation():
    stripped = []
    for node in load_nodes():
        if node.node_id in {"TKG002-NODE-TAU", "TKG002-NODE-SIGMA"}:
            node = replace(node, formulas=(), equivalent_forms=())
        stripped.append(node)
    assert ExecutionComposer(stripped).answer("Compute tau(360)").status == INSUFFICIENT_KNOWLEDGE
    assert ExecutionComposer(stripped).answer("Compute sigma(4620)").status == INSUFFICIENT_KNOWLEDGE


def test_registry_change_changes_behavior_without_engine_change():
    nodes = load_nodes()
    modified = []
    for node in nodes:
        if node.node_id == "TKG002-NODE-TAU":
            node = replace(node, equivalent_forms=("tau=1*id",))
        modified.append(node)
    answer = ExecutionComposer(modified).answer("Compute tau(360)")
    assert answer.result == sum(enumerate_divisors(360))
    assert answer.result != 24


def test_construct_divisor_box_is_generic_and_consistent():
    box = construct_divisor_box(360)
    assert box["alpha"] == {2: 3, 3: 2, 5: 1}
    assert box["cardinality"] == 24
    assert sorted(point["d"] for point in box["points"]) == enumerate_divisors(360)
    assert all(point["d"] * point["n_over_d"] == 360 for point in box["points"])
