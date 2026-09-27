"""EXP26-2: declared synthetic-only viability study. Not a scientific pipeline change."""
from __future__ import annotations
import hashlib
import json
import resource
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.special import expit
def threadpool_info():
    line=next(l for l in Path('/proc/self/status').read_text().splitlines() if l.startswith('Threads:'))
    return [{'backend':'process_status_NLWP','num_threads':int(line.split()[1])}]
from .controls import generate_gue_central_levels

KS = (2, 6, 12, 30)
TAU = np.linspace(.05, 2., 128)

def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    c = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime + c.ru_utime + c.ru_stime

def transform(x, w, center):
    out = np.empty(len(TAU), complex)
    for j in range(0, len(TAU), 16):
        out[j:j+16] = np.exp(-2j*np.pi*TAU[j:j+16,None]*(x-center)) @ w
    return out

def mask_for(x, k, mechanism, rng):
    candidates = np.arange(1, len(x)-2)
    if mechanism == 1:
        gaps = np.diff(x)[candidates]
        candidates = candidates[gaps <= np.quantile(gaps, .1)]
    chosen, used = [], set()
    for j in rng.permutation(candidates):
        if int(j) not in used and int(j+1) not in used:
            chosen.extend([int(j), int(j+1)])
            used.update([int(j), int(j+1)])
            if len(chosen) == k:
                break
    if len(chosen) != k:
        raise ValueError('Insufficient disjoint pairs; no replacement rule allowed')
    return np.asarray(chosen, dtype=int)

def features(y, amp, q):
    s = np.diff(y)
    local = [s.mean(), s.var(), s.max(), *np.quantile(s,[.1,.5,.9,.99]),
             np.mean(s<.3),np.mean(s>2),np.mean(s>3),np.mean(s>4)]
    spec = np.abs(amp)**2/q
    return np.r_[local, spec.reshape(8,16).mean(1),
                 (amp.real/np.sqrt(q)).reshape(8,16).mean(1),
                 (amp.imag/np.sqrt(q)).reshape(8,16).mean(1)]

def fit_logistic(x, y):
    mean, scale = x.mean(0), x.std(0)
    scale = np.where(scale>1e-12,scale,1.)
    z = np.c_[np.ones(len(x)), (x-mean)/scale]
    def objective(b):
        t = z @ b
        return (np.mean(np.logaddexp(0,t)-y*t)+.005*np.dot(b[1:],b[1:]),
                z.T@(expit(t)-y)/len(y)+np.r_[0.,.01*b[1:]])
    r = minimize(objective,np.zeros(z.shape[1]),jac=True,method='L-BFGS-B',
                 options={'maxiter':500})
    return r, mean, scale

def interval(a, indices):
    b = a[indices].mean(1)
    return {'estimate':float(a.mean()),'ci95_pointwise':np.quantile(b,[.025,.975]).tolist()}

def analyze(f, g):
    rng = np.random.default_rng(26092699)
    boot = rng.integers(0,40,size=(2000,40))
    summary = {'severities':{},'inference':'exploratory, fixed trained model; parent bootstrap; not Bayes bound'}
    ytrain = np.broadcast_to(np.array([0,1])[None,:,None],(40,2,8)).reshape(-1)
    for ki,k in enumerate(KS):
        entry, preds = {}, {}
        for label, nfeat in [('B0',11),('B1',35)]:
            tr=f[:40,ki,:,:,:nfeat].reshape(-1,nfeat)
            result, mean, scale=fit_logistic(tr,ytrain)
            entry[label]={'converged':bool(result.success),'iterations':int(result.nit),'message':str(result.message),
                          'coefficients':result.x.tolist(),'mean':mean.tolist(),'scale':scale.tolist()}
            if not result.success:
                continue
            def score(z): return result.x[0]+((z-mean)/scale)@result.x[1:]
            cal=score(f[40:80,ki,:,:,:nfeat])
            threshold=float(np.quantile(cal[:,0,:],.95,method='higher'))
            pred=score(f[80:120,ki,:,:,:nfeat])>threshold
            preds[label]=pred
            entry[label].update(threshold=threshold, fpr=interval(pred[:,0,:].mean(1),boot),
                                tpr=interval(pred[:,1,:].mean(1),boot))
        if len(preds)==2:
            diff=(preds['B1'][:,1,:]-preds['B0'][:,1,:].astype(int)).mean(1)
            gain=interval(diff,boot)
            entry['gain']=gain
            lo,hi=gain['ci95_pointwise']
            fhi=entry['B1']['fpr']['ci95_pointwise'][1]
            entry['decision']=('parar_B1_GUE_nesta_severidade' if hi<.05 else
                'seguir_para_piloto_nesta_severidade' if lo>.05 and fhi<=.05 else 'inconclusivo')
        else: entry['decision']='inconclusivo_falha_otimizacao'
        summary['severities'][str(k)]=entry
    edges=np.r_[np.arange(0,8.000001,.2),np.inf]
    counts=np.array([np.histogram(g[:40,m,:].ravel(),edges)[0]+.5 for m in (0,1)])
    lr=np.log(counts[1]/counts[1].sum())-np.log(counts[0]/counts[0].sum())
    def scores(z):return lr[np.minimum(np.searchsorted(edges,z,side='right')-1,len(lr)-1)]
    threshold=float(np.quantile(scores(g[40:80,0,:]),.95,method='higher'))
    pred=scores(g[80:120])>threshold
    equal=scores(g[80:120])>0
    accuracy=(np.mean(~equal[:,0,:],axis=1)+np.mean(equal[:,1,:],axis=1))/2
    summary['local_gap_oracle']={'label':'histogram likelihood discriminator, not optimality bound',
        'threshold':threshold,'bin_edges':edges[:-1].tolist()+['infinity'],
        'log_likelihood_ratio':lr.tolist(),'equal_prior_accuracy':interval(accuracy,boot),
        'fpr':interval(pred[:,0,:].mean(1),boot),'tpr':interval(pred[:,1,:].mean(1),boot)}
    return summary

def run(output):
    output=Path(output)
    start_wall=time.monotonic()
    pools=threadpool_info()
    if any(p['num_threads']!=1 for p in pools):raise RuntimeError('Expected single-thread libraries')
    f=np.full((120,4,2,8,35),np.nan)
    g=np.full((120,2,8),np.nan)
    masks=np.full((120,4,2,8,30),-1,dtype=np.int32)
    base=np.full((120,128),np.nan)
    delta=np.full((120,4,2,128),np.nan)
    # Effect metrics: mean delta, mean delta squared, interference squared, quadratic mean, quadratic squared.
    effects=np.full((120,4,2,5),np.nan)
    meta=[];checks=[];completed=0
    def save():
        np.savez_compressed(output/'sinteticos_resumos.npz',features=f[:completed],oracle_gap=g[:completed],
            masks=masks[:completed],baseline_k=base[:completed],mean_delta=delta[:completed],
            effects=effects[:completed],tau=TAU)
        (output/'pais.json').write_text(json.dumps(meta,indent=2)+'\n')
        (output/'checkpoint.json').write_text(json.dumps({'completed_parents':completed,'cpu_seconds':cpu(),
            'wall_seconds':time.monotonic()-start_wall,'checks':checks},indent=2)+'\n')
    for i in range(120):
        if cpu()>560:break
        assert threadpool_info()[0]['num_threads']==1
        seed=2026092600+i
        x, gm=generate_gue_central_levels(3000,.6,np.random.default_rng(seed))
        assert len(x)==3000 and np.all(np.diff(x)>0)
        a,b=x[0],x[-1];length=b-a;center=(a+b)/2
        w=.5*(1-np.cos(2*np.pi*(x-a)/length));q=.375*length
        v=TAU*length
        mu=length*(.5*np.sinc(v)+.25*(np.sinc(v-1)+np.sinc(v+1)))
        amp=transform(x,w,center)-mu
        base[i]=np.abs(amp)**2/q
        for ki,k in enumerate(KS):
            for m in (0,1):
                dv=[];ev=[]
                for rep in range(8):
                    mask=mask_for(x,k,m,np.random.default_rng(np.random.SeedSequence([20260926,i,k,m,rep])))
                    assert len(np.unique(mask))==k and min(mask)>0 and max(mask)<len(x)-1
                    masks[i,ki,m,rep,:k]=mask
                    keep=np.ones(len(x),bool);keep[mask]=False
                    d=transform(x[mask],w[mask],center)
                    aa=amp-d
                    yy=x[keep]
                    assert len(yy)==3000-k and yy[0]==a and yy[-1]==b
                    inter=-2*np.real(amp*np.conjugate(d))/q
                    quad=np.abs(d)**2/q
                    change=np.abs(aa)**2/q-base[i]
                    err=float(np.max(np.abs(change-inter-quad)))
                    assert err<=1e-9
                    if i==0 and rep==0:
                        direct=transform(yy,w[keep],center)-mu
                        ed=float(np.max(np.abs(np.abs(direct)**2/q-np.abs(aa)**2/q)))
                        assert ed<=1e-9
                        checks.append({'k':k,'mechanism':m,'identity_error':err,'direct_error':ed})
                    f[i,ki,m,rep]=features(yy,aa,q)
                    if k==2:
                        j=min(mask);g[i,m,rep]=x[j+2]-x[j-1]
                    dv.append(change)
                    ev.append([change.mean(),np.mean(change**2),np.mean(inter**2),quad.mean(),np.mean(quad**2)])
                delta[i,ki,m]=np.mean(dv,axis=0)
                effects[i,ki,m]=np.mean(ev,axis=0)
        meta.append({'parent':i,'seed':seed,'sha256_levels':hashlib.sha256(x.tobytes()).hexdigest(),
            'split':'development' if i<40 else 'calibration' if i<80 else 'evaluation',**gm})
        completed=i+1
        save()
        if completed%10==0:print(f'parents={completed}/120 cpu={cpu():.2f}s wall={time.monotonic()-start_wall:.2f}s',flush=True)
    result={'completed_parents':completed,'status':'complete' if completed==120 else 'inconclusivo_orcamento',
        'threads':pools,'versions':{'numpy':np.__version__,'scipy':scipy.__version__},'checks':checks}
    if completed==120 and cpu()<560:
        result['analysis']=analyze(f,g)
        effect_summary={}
        # Evaluation parents only; baseline variation is across independent parents.
        baseline_sd=np.std(base[80:],axis=0,ddof=1)
        result['baseline']=dict(mean_k=float(base[80:].mean()),median_sd_per_bin=float(np.median(baseline_sd)),
                               sd_frequency_average=float(base[80:].mean(1).std(ddof=1)))
        corr=np.corrcoef(base[80:],rowvar=False)
        result['baseline']['effective_rank_covariance']=float(np.trace(np.cov(base[80:],rowvar=False))**2/
            np.sum(np.cov(base[80:],rowvar=False)**2))
        np.save(output/'correlacao_bins_avaliacao.npy',corr)
        for ki,k in enumerate(KS):
            effect_summary[str(k)]={}
            for m,label in [(0,'MA'),(1,'MP')]:
                e=effects[80:,ki,m]
                effect_summary[str(k)][label]={'mean_delta_k':float(e[:,0].mean()),
                    'rms_delta_k':float(np.sqrt(e[:,1].mean())),
                    'rms_interference':float(np.sqrt(e[:,2].mean())),
                    'mean_quadratic':float(e[:,3].mean()),
                    'rms_mean_shift_over_bin_sd':float(np.sqrt(np.mean((delta[80:,ki,m].mean(0)/baseline_sd)**2)))}
        result['effects']=effect_summary
    elif completed==120:result['status']='inconclusivo_orcamento_analise'
    result['cpu_seconds']=cpu();result['wall_seconds']=time.monotonic()-start_wall
    result['nlwp_end']=next((l.strip() for l in Path('/proc/self/status').read_text().splitlines() if l.startswith('Threads:')),None)
    (output/'resumo.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ['status','completed_parents','cpu_seconds','wall_seconds']}),flush=True)
