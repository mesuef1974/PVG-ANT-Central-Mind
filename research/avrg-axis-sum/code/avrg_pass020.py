#!/usr/bin/env python3
"""PASS020: rank-one factorization into amplitude and cancellation defect."""
import argparse,json,numpy as np

def leading(A):
    u,s,vh=np.linalg.svd(A,full_matrices=False); v=vh[0].copy(); amp=s[0]*u[:,0]
    eps=float(v.sum())
    if eps<0:v=-v;amp=-amp;eps=-eps
    pred=amp*eps
    return dict(v=v,amp=amp,eps=eps,pred=pred,s=float(s[0]),
        rel_error=float(np.linalg.norm(A-np.outer(amp,v))/np.linalg.norm(A)))

def run(paths):
    datasets=[]
    for path in paths:
        z=json.load(open(path)); blocks=[]
        for r in sorted({x['r'] for x in z['blocks']}):
            q=[x for x in z['blocks'] if x['r']==r]; modes=[x['k'] for x in q]
            Aon=np.array([x['on_vector'] for x in q]); Aoff=np.array([x['off_centered_canonical_vector'] for x in q])
            on=leading(Aon);off=leading(Aoff); exact_on=Aon.sum(1);exact_off=Aoff.sum(1)
            ar=on['amp']/off['amp']; er=on['eps']/off['eps']; prod=ar*er; exact=exact_on/exact_off
            cosine=float(abs(on['v']@off['v']))
            blocks.append(dict(r=r,modes=modes,profile_cosine=cosine,
                on_defect=on['eps'],off_defect=off['eps'],defect_ratio=er,
                on_rank1_relative_error=on['rel_error'],off_rank1_relative_error=off['rel_error'],
                amplitude_ratio=ar.tolist(),rank1_product_ratio=prod.tolist(),exact_energy_ratio=exact.tolist(),
                product_relative_error=(prod/exact-1).tolist(),
                on_amplitude=on['amp'].tolist(),off_amplitude=off['amp'].tolist(),
                on_profile=on['v'].tolist(),off_profile=off['v'].tolist()))
        datasets.append(dict(source=path,exp=z['exp'],window=z['window'],blocks=blocks))
    return dict(identity='rank1 energy = amplitude * profile defect',datasets=datasets)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs='+');p.add_argument('--out');a=p.parse_args();z=run(a.inputs);s=json.dumps(z,indent=2)
 if a.out:open(a.out,'w').write(s+'\n')
 else:print(s)
