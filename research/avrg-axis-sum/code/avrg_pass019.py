#!/usr/bin/env python3
"""PASS019: does the tiny second singular component control the signed row sum?"""
import argparse,json,numpy as np

def block_analysis(block):
    A=np.array(block['matrix'],float); r=block['r']
    if not A.size:return None
    u,s,vh=np.linalg.svd(A,full_matrices=False); one=np.ones(r)
    comps=[]
    for j in range(len(s)):
        C=s[j]*np.outer(u[:,j],vh[j]); rs=C@one
        comps.append(dict(index=j+1,singular_value=float(s[j]),
            frobenius_energy_fraction=float(s[j]**2/np.sum(s**2)),
            right_alignment_with_ones=float(abs(vh[j]@one)/np.sqrt(r)),
            signed_row_sums=rs.tolist()))
    total=A@one; A1=s[0]*np.outer(u[:,0],vh[0]); residual=A-A1; rs1=A1@one; rsr=residual@one
    return dict(r=r,state=block['state'],even_modes=block['even_modes'],total_row_sums=total.tolist(),
        rank1_row_sums=rs1.tolist(),residual_row_sums=rsr.tolist(),
        residual_over_total=[float(rsr[i]/total[i]) if total[i] else None for i in range(len(total))],
        residual_frobenius_fraction=float(np.linalg.norm(residual)**2/np.linalg.norm(A)**2),
        components=comps,closure=float(np.max(np.abs(total-rs1-rsr))))

def run(paths):
    out=[]
    for path in paths:
        z=json.load(open(path)); out.append(dict(source=path,exp=z['exp'],window=z['window'],
            blocks=[x for b in z['blocks'] if (x:=block_analysis(b)) is not None]))
    return dict(question='whether small singular residual controls signed energy projection',datasets=out)

def run_geometry(paths):
    out=[]
    for path in paths:
        z=json.load(open(path)); blocks=[]
        for r in sorted({x['r'] for x in z['blocks']}):
            q=[x for x in z['blocks'] if x['r']==r]
            for state,key in [('on','on_vector'),('off_centered_canonical','off_centered_canonical_vector')]:
                A=np.array([x[key] for x in q]); u,s,vh=np.linalg.svd(A,full_matrices=False); one=np.ones(r)
                energy=s*s/(s@s); sums=A@one; comps=[]
                for j in range(len(s)):
                    C=s[j]*np.outer(u[:,j],vh[j]); comps.append(dict(index=j+1,
                        energy_fraction=float(energy[j]),alignment_with_ones=float(abs(vh[j]@one)/np.sqrt(r)),
                        signed_row_sums=(C@one).tolist()))
                blocks.append(dict(r=r,state=state,modes=[x['k'] for x in q],total_row_sums=sums.tolist(),components=comps))
        out.append(dict(source=path,exp=z['exp'],window=z['window'],blocks=blocks))
    return dict(question='same test after canonical off centering',datasets=out)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs='+');p.add_argument('--geometry',action='store_true');p.add_argument('--out');a=p.parse_args();z=run_geometry(a.inputs) if a.geometry else run(a.inputs);s=json.dumps(z,indent=2)
 if a.out:open(a.out,'w').write(s+'\n')
 else:print(s)
