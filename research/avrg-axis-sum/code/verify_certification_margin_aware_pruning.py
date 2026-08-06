"""Verify ACTIVE-003-Q certification-margin-aware pruning.

Benchmark: 4 <= N <= 120, 3 <= r <= 30, exact budgets B <= 4.
"""
from __future__ import annotations
import cmath,itertools,json,math
from pathlib import Path
from dataclasses import dataclass
EPS=1e-10; STRICT_EPS=1e-8

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def vm(n):
    if n<2:return 0.0
    for p in range(2,math.isqrt(n)+1):
        if n%p==0:
            x=n
            while x%p==0:x//=p
            return math.log(p) if x==1 else 0.0
    return math.log(n)

def build(N,r):
    g=math.gcd(2,r); q=r//g; u=2//g
    z=[0.0]*q; h=[0.0]*q; pp=[0.0]*q
    for a in range(1,N):
        la=vm(a); lb=vm(N-a); c=(u*a)%q
        z[c]+=la*lb
        if is_prime(a) and is_prime(N-a): pp[c]+=la*lb
        if la>0 and not is_prime(a): h[c]+=la
    C=[math.log(N)*(h[c]+h[(u*N-c)%q]) for c in range(q)]
    hat=[sum(z[c]*cmath.exp(2j*math.pi*k*c/q) for c in range(q)) for k in range(q)]
    freqs=list(range(1,(q-1)//2+1))
    base=[sum(z)/q]*q
    if q%2==0:
        ny=hat[q//2].real/q
        base=[base[c]+ny*((-1)**c) for c in range(q)]
    P={k:[(2/q)*(hat[k]*cmath.exp(-2j*math.pi*k*c/q)).real for c in range(q)] for k in freqs}
    G={k:[x+abs(x) for x in P[k]] for k in freqs}
    L0=[base[c]-sum(abs(P[k][c]) for k in freqs) for c in range(q)]
    return q,freqs,C,L0,G,pp

def objective(S,L0,G,C):
    return sum(L0[c]+sum(G[k][c] for k in S)>C[c]+EPS for c in range(len(C)))

def cert_channels(S,L0,G,C):
    return [c for c in range(len(C)) if L0[c]+sum(G[k][c] for k in S)>C[c]+EPS]

def closure(freqs,G,q):
    desc={k:set() for k in freqs}
    for i,j in itertools.permutations(freqs,2):
        ge=all(G[i][c]>=G[j][c]-EPS for c in range(q))
        strict=any(G[i][c]>G[j][c]+STRICT_EPS for c in range(q))
        equal=all(abs(G[i][c]-G[j][c])<=EPS for c in range(q))
        if ge and (strict or (equal and i<j)): desc[i].add(j)
    changed=True
    while changed:
        changed=False
        for i in freqs:
            u=set().union(*(desc[j] for j in list(desc[i]))) if desc[i] else set()
            n=len(desc[i]); desc[i]|=u; changed|=(len(desc[i])!=n)
    anc={k:set() for k in freqs}
    for i in freqs:
        for j in desc[i]: anc[j].add(i)
    return anc,desc,sum(map(len,desc.values()))

def old_bound(included,undecided,slots,L0,G,C):
    if slots<0:return -1
    cnt=0
    for c in range(len(C)):
        v=L0[c]+sum(G[k][c] for k in included)
        v+=sum(sorted((G[k][c] for k in undecided),reverse=True)[:slots])
        cnt+=v>C[c]+EPS
    return cnt

def greedy_color_upper(adj, vertices):
    colors={}
    un=set(vertices)
    while un:
        v=max(un,key=lambda x:(len({colors[n] for n in adj[x] if n in colors}),len(adj[x]),-x))
        used={colors[n] for n in adj[v] if n in colors}
        color=0
        while color in used: color+=1
        colors[v]=color; un.remove(v)
    return (max(colors.values())+1) if colors else 0

def margin_bound(included,excluded,undecided,slots,L0,G,C,anc,stats):
    stats.margin_calls+=1
    current=[L0[c]+sum(G[k][c] for k in included) for c in range(len(C))]
    potentials=[]; mand={}
    for c in range(len(C)):
        vals=sorted(((G[k][c],k) for k in undecided),reverse=True)
        if current[c]+sum(v for v,k in vals[:slots])<=C[c]+EPS:
            continue
        mandatory=set()
        for k in undecided:
            vals_without=sorted((G[j][c] for j in undecided if j!=k),reverse=True)
            if current[c]+sum(vals_without[:slots])<=C[c]+EPS:
                mandatory.add(k)
        mcl=set()
        for k in mandatory:mcl|=(anc[k]|{k})
        mcl-=included
        if mcl & excluded or len(mcl)>slots:
            stats.channels_removed_by_mandatory+=1
            continue
        potentials.append(c); mand[c]=mcl
    adj={c:set() for c in potentials}
    for i,c in enumerate(potentials):
        for d in potentials[i+1:]:
            if len(mand[c]|mand[d])<=slots:
                adj[c].add(d);adj[d].add(c)
            else:
                stats.incompatible_channel_pairs+=1
    ub=greedy_color_upper(adj,potentials)
    stats.margin_stricter += ub < len(potentials)
    return ub

@dataclass
class Stats:
    visited:int=0; leaves:int=0; ub_prunes:int=0; prec_prunes:int=0; forced:int=0
    margin_calls:int=0; margin_stricter:int=0; channels_removed_by_mandatory:int=0; incompatible_channel_pairs:int=0

def solve(freqs,B,L0,G,C,anc,desc,use_margin):
    best=-1; bestS=(); st=Stats()
    def prop(S,X):
        S=set(S);X=set(X)
        nS=set(S);nX=set(X)
        for j in S:nS|=anc[j]
        for i in X:nX|=desc[i]
        st.forced+=(len(nS)-len(S)+len(nX)-len(X))
        if nS&nX:return None,None,True
        return nS,nX,False
    def score(k,S):
        cost=len((anc[k]|{k})-S)
        return (sum(G[k])/cost,len(anc[k])+len(desc[k]),-cost,-k)
    def rec(S,X):
        nonlocal best,bestS
        st.visited+=1
        S,X,bad=prop(S,X)
        if bad: st.prec_prunes+=1; return
        U=[k for k in freqs if k not in S and k not in X]
        slots=B-len(S)
        if slots<0 or len(U)<slots: st.prec_prunes+=1; return
        ub=margin_bound(S,X,U,slots,L0,G,C,anc,st) if use_margin else old_bound(S,U,slots,L0,G,C)
        if ub<=best: st.ub_prunes+=1; return
        if slots==0 or not U:
            st.leaves+=1; v=objective(S,L0,G,C)
            if v>best:best=v;bestS=tuple(sorted(S))
            return
        k=max(U,key=lambda x:score(x,S))
        rec(S|{k},X); rec(S,X|{k})
    rec(set(),set())
    return best,bestS,st

def exhaustive(freqs,B,L0,G,C):
    best=-1;bs=()
    for S in itertools.combinations(freqs,B):
        v=objective(S,L0,G,C)
        if v>best:best=v;bs=S
    return best,bs

def main():
    s={k:0 for k in ['cases','precedence_cases','old_mismatch','margin_mismatch','false_certificates','old_nodes','margin_nodes','old_leaves','margin_leaves','old_prunes','margin_prunes','margin_stricter_calls','margin_calls','channels_removed_by_mandatory','incompatible_channel_pairs','improved','equal','worse']}
    ex=None; bestred=-10**9
    for N in range(4,121):
      for r in range(3,31):
        q,f,C,L0,G,pp=build(N,r)
        if len(f)<2:continue
        anc,desc,ec=closure(f,G,q)
        for B in range(0,min(4,len(f))+1):
            s['cases']+=1;s['precedence_cases']+=ec>0
            ev,_=exhaustive(f,B,L0,G,C)
            ov,oS,os=solve(f,B,L0,G,C,anc,desc,False)
            mv,mS,ms=solve(f,B,L0,G,C,anc,desc,True)
            s['old_mismatch']+=ov!=ev;s['margin_mismatch']+=mv!=ev
            for S in (oS,mS):
                for c in cert_channels(S,L0,G,C):s['false_certificates']+=pp[c]<=EPS
            s['old_nodes']+=os.visited;s['margin_nodes']+=ms.visited
            s['old_leaves']+=os.leaves;s['margin_leaves']+=ms.leaves
            s['old_prunes']+=os.ub_prunes;s['margin_prunes']+=ms.ub_prunes
            s['margin_stricter_calls']+=ms.margin_stricter;s['margin_calls']+=ms.margin_calls
            s['channels_removed_by_mandatory']+=ms.channels_removed_by_mandatory
            s['incompatible_channel_pairs']+=ms.incompatible_channel_pairs
            if ms.visited<os.visited:s['improved']+=1
            elif ms.visited==os.visited:s['equal']+=1
            else:s['worse']+=1
            red=os.visited-ms.visited
            if red>bestred and ec>0:
                bestred=red;ex={'N':N,'r':r,'q':q,'B':B,'optimum':ev,'old':{'nodes':os.visited,'leaves':os.leaves,'prunes':os.ub_prunes,'S':oS},'margin':{'nodes':ms.visited,'leaves':ms.leaves,'prunes':ms.ub_prunes,'S':mS},'node_reduction':red}
    s['aggregate_node_reduction_percent']=100.0*(s['old_nodes']-s['margin_nodes'])/s['old_nodes']
    out={'schema':'pvg.certification-margin-aware-pruning.v1','status':'PASS' if s['old_mismatch']==s['margin_mismatch']==s['false_certificates']==0 else 'FAIL','benchmark':{'N':[4,120],'r':[3,30],'max_exact_budget':4},'summary':s,'explicit_tree_improvement_example':ex,'claims':{'exact_optimum_preserved':s['margin_mismatch']==0,'false_certificates':s['false_certificates'],'uniform_speedup_claim':False,'polynomial_time_claim':False,'goldbach_proof_claim':False,'rh_or_grh_progress_claim':False}}
    output=Path(__file__).resolve().parents[1]/'results'/'certification_margin_aware_pruning_verification_v1.0.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
