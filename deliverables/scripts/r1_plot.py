#!/usr/bin/env python3
"""Plot the completed 8x R1 rollout independently of the pending ablation."""
from pathlib import Path
import csv
import numpy as np
from make_figures import plt,save
root=Path(__file__).resolve().parents[1]
def read(name):
 with (root/'tables'/name).open() as f:return {k:np.array([float(r[k]) for r in rows]) for rows in [list(csv.DictReader(f))] for k in rows[0]}
p=read('divergence_mc_ar_8x_s0.csv');g=read('ground_truth_mc_ar_8x_s0.csv')
fig,axs=plt.subplots(2,2,figsize=(6.8,4.4),layout='constrained')
for ax,key,label in zip(axs.flat,['lpips_mean','mse_mean','intensity_mean','pixel_std_mean'],['Frame-to-frame LPIPS','Frame-to-frame MSE','Mean pixel intensity','Within-frame pixel SD']):
 for data,color,style,name in [(p,'#0072B2','-','Prediction'),(g,'#D55E00','--','Ground truth')]:
  mask=data['t']>=2
  ax.plot(data['t'][mask],data[key][mask],color=color,ls=style,label=name,lw=1)
  sd=key.replace('_mean','_std')
  if sd in data:ax.fill_between(data['t'][mask],np.maximum(0,data[key][mask]-data[sd][mask]),data[key][mask]+data[sd][mask],color=color,alpha=.12)
 for t in range(10,81,10):ax.axvline(t,color='.6',ls='--',lw=.5)
 ax.set(xlabel='Frame index (frames)',ylabel=label,xlim=(2,80))
axs[0,0].legend(loc='upper left',ncol=2,bbox_to_anchor=(0,1.27),frameon=False)
save(fig,root/'figures/r1_temporal_metrics')
