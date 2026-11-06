#!/usr/bin/env python3
"""Summarize measured maze episodes; never replace missing runs with paper values."""
import argparse, csv, json, re
from pathlib import Path
import numpy as np
METRICS=['episode_reward','episode_reward_if_stay','first_reach']
def write(path, rows):
 if not rows: return
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
 p=argparse.ArgumentParser();p.add_argument('runs',type=Path);p.add_argument('--out',type=Path,default=Path('tables'));a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 rows=[];groups={};seen=set()
 for f in sorted(a.runs.glob('maze_*/maze_metrics.json')):
  record=f.parent/'run.json'
  if not record.exists() or json.loads(record.read_text()).get('status')!='ok': continue
  match=re.fullmatch(r'maze_(medium|large)_g([1-5])_s(\d+)',f.parent.name)
  if not match: raise ValueError(f'Unrecognized condition: {f.parent.name}')
  env,g,seed=match.groups();g=int(g);seed=int(seed);d=json.loads(f.read_text())
  if int(d['seed'])!=seed: raise ValueError('Seed metadata mismatch')
  identity=(env,g,seed)
  if identity in seen: raise ValueError('Duplicate condition')
  seen.add(identity);n=len(d['first_reach'])
  if n<2 or any(len(d[k])!=n for k in METRICS+['reached']): raise ValueError('Invalid episode arrays')
  r=dict(run=f.parent.name,environment=env,guidance=g,seed=seed,n=n,success_fraction=float(np.mean(d['reached'])))
  for k in METRICS:r.update({k+'_mean':float(np.mean(d[k])),k+'_std':float(np.std(d[k],ddof=1))})
  rows.append(r);groups.setdefault((env,g),[]).append(r)
 if not rows: raise SystemExit('No maze metrics found; no empirical table generated.')
 write(a.out/'maze_results.csv',rows);write(a.out/'guidance_sweep.csv',rows)
 summary=[]
 for (env,g),items in sorted(groups.items()):
  r=dict(environment=env,guidance=g,seeds=len(items),episodes=sum(v['n'] for v in items),error_bar_unit='seed_mean_SD' if len(items)>1 else 'episode_SD')
  for k in METRICS:
   values=[v[k+'_mean'] for v in items]
   r[k+'_mean']=float(np.mean(values));r[k+'_std']=float(np.std(values,ddof=1)) if len(items)>1 else items[0][k+'_std']
  summary.append(r)
 write(a.out/'maze_seed_summary.csv',summary)
 with (a.out/'maze_results.tex').open('w') as f:
  f.write('\\begin{tabular}{lrrr}\n\\toprule\nRun & Reward & Stay & First reach\\\\\n\\midrule\n')
  for r in rows:
   vals=[f"{r[k+'_mean']:.2f} $\\pm$ {r[k+'_std']:.2f}" for k in METRICS]
   f.write(r['run'].replace('_',r'\_')+' & '+' & '.join(vals)+r'\\'+'\n')
  f.write('\\bottomrule\n\\end{tabular}\n')
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 plt.rcParams.update({'font.size':8,'axes.labelsize':8,'legend.fontsize':8,'pdf.fonttype':42})
 fig,axs=plt.subplots(1,3,figsize=(6.8,2.9),layout='constrained')
 labels=['Episode reward (raw sum)','Reward if stay (raw sum)','First reach (steps; censored)']
 for env,style,color in [('medium','o-','#0072B2'),('large','s--','#D55E00')]:
  selected=[r for r in summary if r['environment']==env]
  if not selected:continue
  for ax,k,label in zip(axs,METRICS,labels):
   ax.errorbar([r['guidance'] for r in selected],[r[k+'_mean'] for r in selected],yerr=[r[k+'_std'] for r in selected],fmt=style,color=color,label=env,capsize=3)
   ax.set_xlabel('Guidance scale');ax.set_ylabel(label);ax.set_xticks(range(1,6))
 axs[0].legend(loc='best');target=a.out.parent/'figures';target.mkdir(exist_ok=True)
 fig.savefig(target/'guidance_sweep.pdf');fig.savefig(target/'guidance_sweep.png',dpi=300);plt.close(fig)
if __name__=='__main__':main()
