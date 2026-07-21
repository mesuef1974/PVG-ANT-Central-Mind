#!/usr/bin/env python3
"""Topology and graph geometry of the global Pareto frontier on a PVG level."""
from __future__ import annotations
import argparse, json
from collections import deque

try:
    from .pvg_multiobjective_geometry import analyze as mo_analyze, adjacent
    from .pvg_level_terrain import parse_primes
    from .pvg_inverse_geometry import GeometryInputError
except ImportError:
    from pvg_multiobjective_geometry import analyze as mo_analyze, adjacent  # type: ignore
    from pvg_level_terrain import parse_primes  # type: ignore
    from pvg_inverse_geometry import GeometryInputError  # type: ignore


def _components(nodes, graph):
    seen=set(); out=[]
    for node in sorted(nodes):
        if node in seen: continue
        comp=[]; stack=[node]; seen.add(node)
        while stack:
            x=stack.pop(); comp.append(x)
            for y in graph[x]:
                if y not in seen: seen.add(y); stack.append(y)
        out.append(sorted(comp))
    return out


def _component_count(nodes, graph, excluded_node=None, excluded_edge=None):
    keep=[n for n in nodes if n != excluded_node]
    seen=set(); count=0
    for node in keep:
        if node in seen: continue
        count += 1; stack=[node]; seen.add(node)
        while stack:
            x=stack.pop()
            for y in graph[x]:
                if y == excluded_node: continue
                if excluded_edge and frozenset((x,y)) == frozenset(excluded_edge): continue
                if y not in seen: seen.add(y); stack.append(y)
    return count


def _shortest_path(graph, source, target):
    if source == target: return [source]
    q=deque([source]); parent={source:None}
    while q:
        x=q.popleft()
        for y in graph[x]:
            if y in parent: continue
            parent[y]=x
            if y == target:
                path=[y]
                while path[-1] is not None: path.append(parent[path[-1]])
                return list(reversed(path[:-1]))
            q.append(y)
    return None


def analyze(primes, level):
    mo=mo_analyze(primes, level)
    frontier=[tuple(x['exponents']) for x in mo['global_pareto_frontier']]
    frontier_set=set(frontier)
    edges=[(a,b) for i,a in enumerate(frontier) for b in frontier[i+1:] if adjacent(a,b)]
    graph={n:[] for n in frontier}
    for a,b in edges: graph[a].append(b); graph[b].append(a)
    for n in graph: graph[n].sort()
    comps=_components(frontier,graph)
    base=len(comps)
    articulations=[n for n in frontier if _component_count(frontier,graph,excluded_node=n)>base]
    bridges=[(a,b) for a,b in edges if _component_count(frontier,graph,excluded_edge=(a,b))>base]
    degrees={n:len(graph[n]) for n in frontier}
    terrain={tuple(x['exponents']):x for x in __import__('pvg_level_terrain').analyze(primes,level)['points']}
    peaks={
      'n': max(frontier,key=lambda x: terrain[x]['n']),
      'tau': max(frontier,key=lambda x: terrain[x]['tau']),
      'sigma_over_n': max(frontier,key=lambda x:(terrain[x]['sigma_over_n']['numerator']/terrain[x]['sigma_over_n']['denominator'])),
      'phi_over_n': max(frontier,key=lambda x:(terrain[x]['phi_over_n']['numerator']/terrain[x]['phi_over_n']['denominator'])),
    }
    peak_paths={}
    names=sorted(peaks)
    for i,a in enumerate(names):
        for b in names[i+1:]:
            path=_shortest_path(graph,peaks[a],peaks[b])
            peak_paths[f'{a}__{b}']=None if path is None else [list(x) for x in path]
    component_sizes=sorted((len(c) for c in comps),reverse=True)
    cycle_rank=len(edges)-len(frontier)+len(comps)
    return {
      'schema':'PVG-PARETO-FRONTIER-GEOMETRY-001','axes':primes,'level':level,
      'frontier_size':len(frontier),'frontier_edge_count':len(edges),
      'component_count':len(comps),'component_sizes':component_sizes,
      'components':[[list(x) for x in c] for c in comps],
      'degree_distribution':{str(d):sum(v==d for v in degrees.values()) for d in sorted(set(degrees.values()))},
      'isolated_points':[list(n) for n,d in degrees.items() if d==0],
      'leaf_points':[list(n) for n,d in degrees.items() if d==1],
      'branch_points':[list(n) for n,d in degrees.items() if d>=3],
      'articulation_points':[list(n) for n in sorted(articulations)],
      'bridges':[[list(a),list(b)] for a,b in bridges],
      'cycle_rank':cycle_rank,
      'objective_peaks':{k:list(v) for k,v in peaks.items()},
      'shortest_paths_between_objective_peaks':peak_paths,
      'verification':{
        'frontier_matches_pass_011':len(frontier)==mo['global_pareto_frontier_size'],
        'edge_count_closes':sum(degrees.values())==2*len(edges),
        'components_partition_frontier':sum(component_sizes)==len(frontier),
        'cycle_rank_nonnegative':cycle_rank>=0,
      },
      'classification':'exact finite induced-subgraph geometry of one registered Pareto frontier; no asymptotic or novelty claim'
    }


def main():
    p=argparse.ArgumentParser(); p.add_argument('axes'); p.add_argument('level',type=int); p.add_argument('--compact',action='store_true'); a=p.parse_args()
    try: r=analyze(parse_primes(a.axes),a.level)
    except (GeometryInputError,ValueError) as e:
        print(json.dumps({'status':'invalid_pareto_frontier_input','reason':str(e)},indent=2)); return 2
    print(json.dumps(r,ensure_ascii=False,sort_keys=True,indent=None if a.compact else 2)); return 0
if __name__=='__main__': raise SystemExit(main())
