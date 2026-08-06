#!/usr/bin/env python3
"""RMG query and bounded traversal API (stdlib only)."""
from __future__ import annotations
import argparse, json
from collections import deque
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
NODES = ROOT / "registry" / "nodes.jsonl"
EDGES = ROOT / "registry" / "edges.jsonl"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class RMG:
    def __init__(self, nodes: Iterable[dict], edges: Iterable[dict]):
        self.nodes = {n["node_id"]: n for n in nodes}
        self.edges = list(edges)
        self.outgoing: dict[str, list[dict]] = {node_id: [] for node_id in self.nodes}
        self.incoming: dict[str, list[dict]] = {node_id: [] for node_id in self.nodes}
        for edge in self.edges:
            self.outgoing.setdefault(edge["source_id"], []).append(edge)
            self.incoming.setdefault(edge["target_id"], []).append(edge)

    @classmethod
    def from_repo(cls) -> "RMG":
        return cls(load_jsonl(NODES), load_jsonl(EDGES))

    def get(self, node_id: str) -> dict:
        if node_id not in self.nodes:
            raise KeyError(f"unknown node_id: {node_id}")
        return self.nodes[node_id]

    def search(self, text: str = "", node_type: str | None = None,
               assimilation_level: str | None = None,
               translation_type: str | None = None) -> list[dict]:
        q = text.casefold().strip()
        out = []
        for node in self.nodes.values():
            haystack = " ".join(str(node.get(k, "")) for k in
                                ("node_id", "canonical_name", "short_definition", "ant_view", "pvg_view")).casefold()
            if q and q not in haystack:
                continue
            if node_type and node.get("node_type") != node_type:
                continue
            if assimilation_level and node.get("assimilation_level") != assimilation_level:
                continue
            if translation_type and node.get("translation_type") != translation_type:
                continue
            out.append(node)
        return sorted(out, key=lambda n: n["node_id"])

    def neighbors(self, node_id: str, direction: str = "both",
                  edge_types: set[str] | None = None) -> list[dict]:
        self.get(node_id)
        selected = []
        if direction in ("out", "both"):
            selected.extend(self.outgoing.get(node_id, []))
        if direction in ("in", "both"):
            selected.extend(self.incoming.get(node_id, []))
        if edge_types:
            selected = [e for e in selected if e["edge_type"] in edge_types]
        return sorted(selected, key=lambda e: e["edge_id"])

    def shortest_path(self, source_id: str, target_id: str,
                      allowed_edge_types: set[str] | None = None,
                      max_depth: int = 8) -> dict | None:
        self.get(source_id); self.get(target_id)
        queue = deque([(source_id, [], [source_id])])
        seen = {source_id}
        while queue:
            current, edge_path, node_path = queue.popleft()
            if current == target_id:
                return {"node_path": node_path, "edge_path": edge_path}
            if len(edge_path) >= max_depth:
                continue
            for edge in self.outgoing.get(current, []):
                if allowed_edge_types and edge["edge_type"] not in allowed_edge_types:
                    continue
                nxt = edge["target_id"]
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, edge_path + [edge["edge_id"]], node_path + [nxt]))
        return None

    def translation_report(self, node_id: str) -> dict:
        node = self.get(node_id)
        return {
            "node_id": node_id,
            "canonical_name": node["canonical_name"],
            "translation_type": node["translation_type"],
            "inverse_status": node.get("inverse_status"),
            "preserved_information": node.get("preserved_information", []),
            "lost_information": node.get("lost_information", []),
            "certificate_present": node.get("certificate_present", []),
            "certificate_missing": node.get("certificate_missing", []),
            "scientific_ceiling": node.get("scientific_ceiling"),
            "assimilation_level": node.get("assimilation_level"),
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    p_get = sub.add_parser("get"); p_get.add_argument("node_id")
    p_search = sub.add_parser("search"); p_search.add_argument("text", nargs="?", default="")
    p_search.add_argument("--node-type"); p_search.add_argument("--assimilation-level"); p_search.add_argument("--translation-type")
    p_neigh = sub.add_parser("neighbors"); p_neigh.add_argument("node_id"); p_neigh.add_argument("--direction", choices=["in","out","both"], default="both")
    p_path = sub.add_parser("path"); p_path.add_argument("source_id"); p_path.add_argument("target_id"); p_path.add_argument("--max-depth", type=int, default=8)
    p_report = sub.add_parser("translation-report"); p_report.add_argument("node_id")
    args = parser.parse_args(); graph = RMG.from_repo()
    if args.command == "get": result = graph.get(args.node_id)
    elif args.command == "search": result = graph.search(args.text, args.node_type, args.assimilation_level, args.translation_type)
    elif args.command == "neighbors": result = graph.neighbors(args.node_id, args.direction)
    elif args.command == "path": result = graph.shortest_path(args.source_id, args.target_id, max_depth=args.max_depth)
    else: result = graph.translation_report(args.node_id)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
