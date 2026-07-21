#!/usr/bin/env python3
"""Strict ascent/descent flows for arithmetic fields on a fixed PVG level."""
from __future__ import annotations

import argparse, json
from collections import defaultdict, deque
from fractions import Fraction

try:
    from .pvg_level_terrain import analyze as terrain_analyze, parse_primes
    from .pvg_inverse_geometry import GeometryInputError
except ImportError:
    from pvg_level_terrain import analyze as terrain_analyze, parse_primes  # type: ignore
    from pvg_inverse_geometry import GeometryInputError  # type: ignore

FIELDS=("n","tau","sigma_over_n","phi_over_n")


def val(row:dict, field:str):
    x=row[field]
    return Fraction(x["numerator"],x["denominator"]) if isinstance(x,dict) else x


def adjacent(a:tuple[int,...], b:tuple[int,...])->bool:
    return sum(abs(x-y) for x,y in zip(a,b))==2 and sum(a)==sum(b)


def undirected_edges(points:list[dict]):
    exp=[tuple(p["exponents"]) for p in points]
    return [(exp[i],exp[j]) for i in range(len(exp)) for j in range(i+1,len(exp)) if adjacent(exp[i],exp[j])]


def plateau_components(nodes:list[tuple[int,...]], equal_edges:list[tuple[tuple[int,...],tuple[int,...]]]):
    g={n:set() for n in nodes}
    for a,b in equal_edges:g[a].add(b);g[b].add(a)
    seen=set(); comps=[]
    for n in nodes:
        if n in seen:continue
        q=[n];seen.add(n);c=[]
        while q:
            x=q.pop();c.append(x)
            for y in g[x]:
                if y not in seen:seen.add(y);q.append(y)
        comps.append(sorted(c))
    return comps


def acyclic(nodes, directed):
    indeg={n:0 for n in nodes};g={n:[] for n in nodes}
    for a,b in directed:g[a].append(b);indeg[b]+=1
    q=deque([n for n in nodes if indeg[n]==0]);seen=0
    while q:
        x=q.popleft();seen+=1
        for y in g[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    return seen==len(nodes)


def strongest_paths(nodes, directed, values):
    out=defaultdict(list)
    for a,b in directed:out[a].append(b)
    sinks=[n for n in nodes if not out[n]]
    memo={}
    def go(n):
        if n in memo:return memo[n]
        if not out[n]:memo[n]=[n];return memo[n]
        best=max(out[n],key=lambda y:(values[y]-values[n],values[y],tuple(y)))
        memo[n]=[n]+go(best);return memo[n]
    return {str(n):go(n) for n in nodes},sinks


def field_flow(points:list[dict], field:str)->dict:
    rows={tuple(p["exponents"]):p for p in points};nodes=sorted(rows);values={n:val(rows[n],field) for n in nodes}
    edges=undirected_edges(points);up=[];eq=[]
    for a,b in edges:
        if values[a]<values[b]:up.append((a,b))
        elif values[b]<values[a]:up.append((b,a))
        else:eq.append((a,b))
    out=defaultdict(list);inc=defaultdict(list)
    for a,b in up:out[a].append(b);inc[b].append(a)
    maxima=[n for n in nodes if not out[n]];minima=[n for n in nodes if not inc[n]]
    paths,sinks=strongest_paths(nodes,up,values)
    basin=defaultdict(list)
    for n in nodes: basin[tuple(paths[str(n)][-1])].append(n)
    comps=plateau_components(nodes,eq);cid={n:i for i,c in enumerate(comps) for n in c};cond=set()
    for a,b in up:
        if cid[a]!=cid[b]:cond.add((cid[a],cid[b]))
    return {
      "field":field,"strict_edge_count":len(up),"equal_edge_count":len(eq),"strict_acyclic":acyclic(nodes,up),
      "local_maxima":[list(x) for x in maxima],"local_minima":[list(x) for x in minima],
      "global_maxima":[list(n) for n in nodes if values[n]==max(values.values())],
      "global_minima":[list(n) for n in nodes if values[n]==min(values.values())],
      "plateau_components":[[list(x) for x in c] for c in comps],
      "plateau_condensation_acyclic":acyclic(list(range(len(comps))),list(cond)),
      "strongest_ascent_paths":{k:[list(x) for x in v] for k,v in paths.items()},
      "strongest_ascent_basins":{str(k):[list(x) for x in v] for k,v in basin.items()},
      "sink_count":len(sinks)
    }


def analyze(primes:list[int],level:int)->dict:
    terrain=terrain_analyze(primes,level); flows={f:field_flow(terrain["points"],f) for f in FIELDS}
    return {"schema":"PVG-LEVEL-FLOW-001","axes":primes,"level":level,"point_count":terrain["point_count"],"fields":flows,
      "verification":{"all_strict_flows_acyclic":all(x["strict_acyclic"] for x in flows.values()),"all_condensations_acyclic":all(x["plateau_condensation_acyclic"] for x in flows.values())},
      "classification":"exact finite graph dynamics induced by arithmetic scalar fields; no asymptotic or novelty claim"}


def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("axes");ap.add_argument("level",type=int);ap.add_argument("--compact",action="store_true");a=ap.parse_args()
    try:r=analyze(parse_primes(a.axes),a.level)
    except (GeometryInputError,ValueError) as e:print(json.dumps({"status":"invalid_level_flow_input","reason":str(e)},indent=2));return 2
    print(json.dumps(r,sort_keys=True,indent=None if a.compact else 2));return 0
if __name__=="__main__":raise SystemExit(main())
