#!/usr/bin/env python3
"""CPU-only contact sheet for inspecting every video in a saved batch."""
import argparse
from pathlib import Path
import torch
from make_figures import plt,save,draw_frame
p=argparse.ArgumentParser();p.add_argument('run',type=Path);a=p.parse_args()
d=torch.load(a.run/'validation_samples.pt',map_location='cpu',weights_only=True)
x=d['pred'].clamp(0,1);ts=sorted(set([0,int(d['context_frames']),len(x)//2,len(x)-2,len(x)-1]))
fig,axs=plt.subplots(x.shape[1],len(ts),figsize=(6.8,x.shape[1]*1.2),squeeze=False,layout='constrained')
for b in range(x.shape[1]):
 for j,t in enumerate(ts):
  draw_frame(axs[b,j],x[t,b],title=f'Video {b+1}, t={t}',context=t<int(d['context_frames']))
save(fig,Path(__file__).resolve().parents[1]/'figures/frames'/(a.run.name+'_all_videos'))
