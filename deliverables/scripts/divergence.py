#!/usr/bin/env python3
"""Measure temporal change, not prediction accuracy. Run in inference environment."""
import argparse, csv, json
from pathlib import Path
import numpy as np
import torch
from torchmetrics.image.lpip import LearnedPerceptualImagePatchSimilarity


def write_csv(path, rows):
    if rows:
        with path.open('w', newline='') as f:
            w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def measure(x, valid, model, device):
    x=x.float().clamp(0,1); t,b=x.shape[:2]
    mse=(x[1:]-x[:-1]).square().mean((2,3,4)).numpy()
    # torchmetrics 0.11.4 only offers mean/sum reductions. Its own net
    # produces per-image scores; use that exact network for batched video SDs.
    lp=np.full((t-1,b),np.nan)
    for i in range(t-1):
        for j in range(0,b,8):
            with torch.no_grad():
                lp[i,j:j+8]=model.net(x[i,j:j+8].to(device),x[i+1,j:j+8].to(device),normalize=True).cpu().numpy().reshape(-1)
            model.reset()
    mask=(valid[1:] & valid[:-1]).numpy()
    mse[~mask]=np.nan; lp[~mask]=np.nan
    intensity=x[1:].mean((2,3,4)).numpy(); spread=x[1:].flatten(2).std(2,unbiased=False).numpy()
    intensity[~valid[1:].numpy()]=np.nan; spread[~valid[1:].numpy()]=np.nan
    rows=[]
    for i in range(t-1):
        def avg(a): return float(np.nanmean(a)) if np.isfinite(a).any() else float('nan')
        def sd(a): return float(np.nanstd(a,ddof=1)) if np.isfinite(a).sum()>1 else float('nan')
        rows.append(dict(t=i+1,mse_mean=avg(mse[i]),mse_std=sd(mse[i]),lpips_mean=avg(lp[i]),lpips_std=sd(lp[i]),intensity_mean=avg(intensity[i]),pixel_std_mean=avg(spread[i]),n_valid=int(mask[i].sum())))
    return rows,mse,lp


def main():
    p=argparse.ArgumentParser(); p.add_argument('runs',type=Path); p.add_argument('--out',type=Path,default=Path('tables')); p.add_argument('--horizon',type=int,default=10); p.add_argument('--device',default='cuda'); a=p.parse_args(); a.out.mkdir(parents=True,exist_ok=True)
    files=sorted(a.runs.glob('*/validation_samples.pt'))
    if not files: raise SystemExit('No samples found; no metrics generated.')
    model=LearnedPerceptualImagePatchSimilarity(net_type='alex',normalize=True).to(a.device).eval()
    summaries=[]; pervideo=[]
    for f in files:
        record=f.parent/'run.json'
        if not record.exists() or json.loads(record.read_text())['status']!='ok': continue
        data=torch.load(f,map_location='cpu',weights_only=True); name=f.parent.name; x=data['pred']; gt=data['gt']; context=int(data['context_frames'])
        if x.ndim!=5 or gt.ndim!=5: raise ValueError('Expected T,B,C,H,W')
        if 'valid' not in data: raise ValueError('Missing validity mask; padding must not be guessed from pixel values.')
        valid=data['valid'].bool()
        (a.out/f'range_{name}.json').write_text(json.dumps({k:{'min':float(data[k].min()),'max':float(data[k].max()),'shape':list(data[k].shape)} for k in ['pred','gt']},indent=2))
        rows,mse,lp=measure(x,torch.ones(x.shape[:2],dtype=torch.bool),model,a.device)
        write_csv(a.out/f'divergence_{name}.csv',rows)
        grows,gm,gl=measure(gt,valid[:len(gt)],model,a.device); write_csv(a.out/f'ground_truth_{name}.csv',grows)
        ts=np.arange(1,len(x)); first=(ts>=context)&(ts<a.horizon); last=(ts>=max(context,len(x)-a.horizon)); generated=ts>=context
        summary={'run':name,'videos':x.shape[1],'frames':len(x),'context_frames':context}
        for metric,arr in [('mse',mse),('lpips',lp)]:
            for period,mask in [('first',first),('last',last)]:
                per=arr[mask].mean(0); summary[f'{metric}_{period}_mean']=float(per.mean()); summary[f'{metric}_{period}_video_std']=float(per.std(ddof=1)) if len(per)>1 else float('nan')
            summary[f'{metric}_slope']=float(np.polyfit(ts[generated],arr[generated].mean(1),1)[0])
        summaries.append(summary)
        for b in range(x.shape[1]):
            pervideo.append(dict(run=name,video=b,late_mse=float(mse[last,b].mean()),late_lpips=float(lp[last,b].mean()),gt_mse=float(np.nanmean(gm[:,b])),gt_lpips=float(np.nanmean(gl[:,b]))))
    write_csv(a.out/'divergence_summary.csv',summaries); write_csv(a.out/'divergence_per_video.csv',pervideo)
if __name__=='__main__': main()
