from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from itertools import product
from pathlib import Path
from typing import Any, Callable, Iterable


INSUFFICIENT_KNOWLEDGE = "INSUFFICIENT_KNOWLEDGE"


@dataclass(frozen=True)
class KnowledgeNode:
    node_id: str
    record_type: str
    names: tuple[str, ...] = ()
    aliases: tuple[str, ...] = ()
    equivalent_forms: tuple[str, ...] = ()
    formulas: tuple[str, ...] = ()
    hypotheses: tuple[str, ...] = ()
    relations: tuple[str, ...] = ()
    examples: tuple[dict[str, Any], ...] = ()
    counterexamples: tuple[dict[str, Any], ...] = ()
    claim_ceiling: str = ""
    raw: dict[str, Any] = field(default_factory=dict, compare=False, repr=False)


@dataclass(frozen=True)
class MatchEvidence:
    node_id: str
    field: str
    value: str
    matched_term: str


@dataclass(frozen=True)
class RetrievalResult:
    matched_nodes: tuple[KnowledgeNode, ...]
    match_evidence: tuple[MatchEvidence, ...]
    unresolved_terms: tuple[str, ...]


@dataclass(frozen=True)
class ExecutionStep:
    description: str
    value: Any
    source_node_id: str | None = None
    operator_id: str | None = None

    def __post_init__(self) -> None:
        if (self.source_node_id is None) == (self.operator_id is None):
            raise ValueError("Each step must have exactly one provenance source")


@dataclass(frozen=True)
class ExecutionAnswer:
    status: str
    query: str
    matched_node_ids: tuple[str, ...]
    steps: tuple[ExecutionStep, ...]
    result: Any = None
    claim_ceiling: str = ""


class RegistryLoader:
    """Load authored JSONL records without mirroring their mathematical content in code."""

    def load(self, path: str | Path) -> list[KnowledgeNode]:
        nodes: list[KnowledgeNode] = []
        with Path(path).open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    raw = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSONL at line {line_number}: {exc}") from exc
                nodes.append(self._normalize(raw))
        return nodes

    @staticmethod
    def _strings(value: Any) -> tuple[str, ...]:
        if value is None:
            return ()
        if isinstance(value, str):
            return (value,)
        if isinstance(value, list):
            return tuple(str(item) for item in value if item is not None)
        return (str(value),)

    def _normalize(self, raw: dict[str, Any]) -> KnowledgeNode:
        definition = raw.get("ant_standard_definition") or {}
        names = self._strings(raw.get("name"))
        aliases = self._strings(raw.get("aliases"))
        formulas = self._strings(definition.get("formula")) + self._strings(raw.get("statement"))
        hypotheses = (
            self._strings(definition.get("domain"))
            + self._strings(raw.get("conditions"))
            + self._strings(raw.get("hypotheses"))
        )
        relations = self._strings(raw.get("relations"))
        if raw.get("source"):
            relations += (str(raw["source"]),)
        if raw.get("target"):
            relations += (str(raw["target"]),)
        if raw.get("relation"):
            relations += (str(raw["relation"]),)
        return KnowledgeNode(
            node_id=str(raw["record_id"]),
            record_type=str(raw.get("record_type", "UNKNOWN")),
            names=names,
            aliases=aliases,
            equivalent_forms=self._strings(raw.get("equivalent_forms")),
            formulas=formulas,
            hypotheses=hypotheses,
            relations=relations,
            examples=tuple(raw.get("examples") or ()),
            counterexamples=tuple(raw.get("counterexamples") or ()),
            claim_ceiling=str(raw.get("claim_ceiling", "")),
            raw=raw,
        )


class DataDrivenRetriever:
    TOKEN_RE = re.compile(r"[A-Za-zΑ-Ωα-ω_]+|\d+|[*=]+")

    def __init__(self, nodes: Iterable[KnowledgeNode]):
        self.nodes = tuple(nodes)
        self.index: dict[str, list[MatchEvidence]] = {}
        for node in self.nodes:
            for field_name, values in self._searchable_fields(node):
                for value in values:
                    for term in self._terms(value):
                        self.index.setdefault(term, []).append(
                            MatchEvidence(node.node_id, field_name, value, term)
                        )

    @staticmethod
    def _searchable_fields(node: KnowledgeNode) -> tuple[tuple[str, tuple[str, ...]], ...]:
        return (
            ("names", node.names),
            ("aliases", node.aliases),
            ("equivalent_forms", node.equivalent_forms),
            ("formulas", node.formulas),
            ("relations", node.relations),
        )

    @classmethod
    def _terms(cls, text: str) -> set[str]:
        normalized = text.lower().replace("mobius", "mu").replace("möbius", "mu")
        terms = {token.lower() for token in cls.TOKEN_RE.findall(normalized)}
        terms.add(normalized.strip())
        return {term for term in terms if term}

    def retrieve(self, question: str) -> RetrievalResult:
        query_terms = self._terms(question)
        evidence: list[MatchEvidence] = []
        resolved: set[str] = set()
        for term in query_terms:
            hits = self.index.get(term, ())
            if hits:
                evidence.extend(hits)
                resolved.add(term)
        node_by_id = {node.node_id: node for node in self.nodes}
        matched_ids = []
        seen = set()
        for item in evidence:
            if item.node_id not in seen:
                seen.add(item.node_id)
                matched_ids.append(item.node_id)
        unresolved = tuple(sorted(term for term in query_terms - resolved if not term.isdigit()))
        return RetrievalResult(
            matched_nodes=tuple(node_by_id[node_id] for node_id in matched_ids),
            match_evidence=tuple(evidence),
            unresolved_terms=unresolved,
        )


def factor_integer(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be a positive integer")
    factors: dict[int, int] = {}
    remaining = n
    p = 2
    while p * p <= remaining:
        while remaining % p == 0:
            factors[p] = factors.get(p, 0) + 1
            remaining //= p
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def enumerate_divisors(n: int) -> list[int]:
    factors = factor_integer(n)
    divisors = [1]
    for prime, exponent in factors.items():
        divisors = [d * (prime ** e) for d in divisors for e in range(exponent + 1)]
    return sorted(divisors)


def arithmetic_function(name: str) -> Callable[[int], float | int]:
    key = name.strip().lower()
    functions: dict[str, Callable[[int], float | int]] = {
        "1": lambda _: 1,
        "one": lambda _: 1,
        "constant-one": lambda _: 1,
        "id": lambda n: n,
        "identity": lambda n: n,
        "epsilon": lambda n: 1 if n == 1 else 0,
        "mu": mobius,
        "log": lambda n: math.log(n),
    }
    if key not in functions:
        raise KeyError(f"Unsupported arithmetic function: {name}")
    return functions[key]


def mobius(n: int) -> int:
    factors = factor_integer(n)
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def apply_dirichlet_convolution(f: str, g: str, n: int) -> float | int:
    left = arithmetic_function(f)
    right = arithmetic_function(g)
    return sum(left(d) * right(n // d) for d in enumerate_divisors(n))


def evaluate_divisor_sum(rule: str, n: int) -> float | int:
    match = re.fullmatch(r"\s*sum\s*:\s*([A-Za-z0-9_-]+)\s*", rule)
    if not match:
        raise ValueError(f"Unsupported divisor-sum rule syntax: {rule}")
    function = arithmetic_function(match.group(1))
    return sum(function(d) for d in enumerate_divisors(n))


def construct_divisor_box(n: int) -> dict[str, Any]:
    factors = factor_integer(n)
    primes = tuple(factors)
    exponent_ranges = [range(factors[p] + 1) for p in primes]
    points = []
    for exponents in product(*exponent_ranges):
        beta = dict(zip(primes, exponents))
        decoded = math.prod(p ** e for p, e in beta.items())
        complement = n // decoded
        points.append({"beta": beta, "d": decoded, "n_over_d": complement})
    points.sort(key=lambda item: item["d"])
    return {"n": n, "alpha": factors, "points": points, "cardinality": len(points)}


class ExecutionComposer:
    """Compose finite calculations only when the required rule is present in registry data."""

    def __init__(self, nodes: Iterable[KnowledgeNode]):
        self.nodes = tuple(nodes)
        self.by_id = {node.node_id: node for node in self.nodes}
        self.retriever = DataDrivenRetriever(self.nodes)

    def answer(self, question: str) -> ExecutionAnswer:
        retrieval = self.retriever.retrieve(question)
        n = self._extract_integer(question)
        target = self._select_target(retrieval.matched_nodes, question)
        if n is None or target is None:
            return ExecutionAnswer(INSUFFICIENT_KNOWLEDGE, question, (), ())

        rule = self._derive_rule(target)
        if rule is None:
            return ExecutionAnswer(
                INSUFFICIENT_KNOWLEDGE,
                question,
                (target.node_id,),
                (),
                claim_ceiling=target.claim_ceiling,
            )

        steps: list[ExecutionStep] = [
            ExecutionStep(
                description=f"Selected registry rule: {rule}",
                value=rule,
                source_node_id=target.node_id,
            )
        ]
        factors = factor_integer(n)
        steps.append(ExecutionStep("Factor integer", factors, operator_id="OP-FACTOR-INTEGER-001"))
        divisors = enumerate_divisors(n)
        steps.append(ExecutionStep("Enumerate divisors", divisors, operator_id="OP-ENUMERATE-DIVISORS-001"))

        operation, operands = rule
        if operation == "convolution":
            result = apply_dirichlet_convolution(operands[0], operands[1], n)
            steps.append(
                ExecutionStep(
                    f"Apply Dirichlet convolution {operands[0]}*{operands[1]}",
                    result,
                    operator_id="OP-DIRICHLET-CONVOLUTION-001",
                )
            )
        elif operation == "divisor_sum":
            result = evaluate_divisor_sum(f"sum:{operands[0]}", n)
            steps.append(
                ExecutionStep(
                    f"Evaluate divisor sum of {operands[0]}",
                    result,
                    operator_id="OP-EVALUATE-DIVISOR-SUM-001",
                )
            )
        elif operation == "divisor_box":
            result = construct_divisor_box(n)
            steps.append(
                ExecutionStep(
                    "Construct labelled valuation divisor box",
                    result,
                    operator_id="OP-CONSTRUCT-DIVISOR-BOX-001",
                )
            )
        else:
            return ExecutionAnswer(INSUFFICIENT_KNOWLEDGE, question, (target.node_id,), ())

        return ExecutionAnswer(
            status="EXECUTED_FROM_REGISTRY_RULE",
            query=question,
            matched_node_ids=(target.node_id,),
            steps=tuple(steps),
            result=result,
            claim_ceiling=target.claim_ceiling,
        )

    @staticmethod
    def _extract_integer(question: str) -> int | None:
        values = [int(value) for value in re.findall(r"\d+", question)]
        return values[-1] if values else None

    @staticmethod
    def _declared_symbols(node: KnowledgeNode) -> set[str]:
        symbols: set[str] = set()
        for text in node.names + node.aliases:
            symbols.update(re.findall(r"[A-Za-z_]+", text.lower()))
        for expression in node.formulas + node.equivalent_forms:
            lhs = expression.split("=", 1)[0].strip().lower()
            symbols.update(re.findall(r"[A-Za-z_]+", lhs))
        return symbols

    @classmethod
    def _select_target(cls, nodes: Iterable[KnowledgeNode], question: str) -> KnowledgeNode | None:
        query_terms = set(re.findall(r"[A-Za-z_]+", question.lower()))
        ranked = []
        for node in nodes:
            declared = cls._declared_symbols(node)
            overlap = query_terms.intersection(declared)
            phrase_hits = sum(1 for text in node.names + node.aliases if text.lower() in question.lower())
            score = 20 * phrase_hits + 5 * len(overlap)
            if score:
                ranked.append((score, node.node_id, node))
        return max(ranked, default=(0, "", None))[2]

    @staticmethod
    def _derive_rule(node: KnowledgeNode) -> tuple[str, tuple[str, ...]] | None:
        declared = ExecutionComposer._declared_symbols(node)
        for form in node.equivalent_forms:
            compact = form.replace(" ", "")
            match = re.fullmatch(r"([A-Za-z_]+)=([A-Za-z0-9_-]+)\*([A-Za-z0-9_-]+)", compact)
            if match and match.group(1).lower() in declared:
                return "convolution", (match.group(2), match.group(3))
        for formula in node.formulas:
            compact = formula.replace(" ", "")
            match = re.fullmatch(r"([A-Za-z_]+)\(n\)=sum_\{d\|n\}(.+)", compact)
            if match and match.group(1).lower() in declared:
                summand = match.group(2)
                if summand == "1":
                    return "divisor_sum", ("1",)
                if summand == "d":
                    return "divisor_sum", ("id",)
            if "correspondsto" in compact.lower() and "0<=beta" in compact.lower():
                return "divisor_box", ()
        return None
