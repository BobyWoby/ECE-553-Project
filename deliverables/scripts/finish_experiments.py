#!/usr/bin/env python3
"""Run the remaining inference experiments, stopping on errors."""
import argparse,datetime,json,os,subprocess,sys,time,traceback
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--wait-pid',type=int,required=True);p.add_argument('--wait-run',default='mc_ar_8x_s0');p.add_argument('--unattended',action='store_true');a=p.parse_args()
root=Path.home()/'eecs553';d=root/'deliverables';scripts=d/'scripts';repo=root/'diffusion-forcing';state=root/'setup/queue_status.json'
def note(message):
 print(datetime.datetime.now().astimezone().isoformat(),message,flush=True)
 state.write_text(json.dumps(dict(time=datetime.datetime.now().astimezone().isoformat(),status=message,pid=os.getpid()),indent=2))
 with (d/'run_log.md').open('a') as f:f.write('\n- Inference queue: '+message+'\n')
def call(command,env=None):
 subprocess.run(command,cwd=repo,env=env,check=True)
def run(base,kind='video',seed=0):
 name=f'{base}_s{seed}';record=root/'runs'/name/'run.json'
 if record.exists() and json.loads(record.read_text())['status']=='ok':return json.loads(record.read_text())
 env=os.environ.copy()
 if kind=='maze':
  env['PATH']=str(root/'.venv/bin')+':'+str(root/'tools/bin')+':'+env['PATH']
  env['LD_LIBRARY_PATH']=str(Path.home()/'.mujoco/mujoco210/bin')+':/usr/lib/nvidia:/usr/lib'+(':'+env['LD_LIBRARY_PATH'] if env.get('LD_LIBRARY_PATH') else '')
  env['C_INCLUDE_PATH']=str(root/'tools/include')
  env['CFLAGS']='-O2 -std=gnu11 -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration -Wno-error=int-conversion'
  env['MUJOCO_GL']='egl'
 cmd=[sys.executable,str(scripts/'run_experiments.py'),'--kind',kind,'--only',base,'--seeds',str(seed),'--execute']
 if kind=='video':cmd+=['--override','algorithm.metrics=[]']
 note('running '+name)
 if not record.exists():
  result=subprocess.run(cmd,cwd=repo,env=env)
  if result.returncode==0:return json.loads(record.read_text())
 if kind=='video' and 'out of memory' in (record.parent/'stdout.log').read_text().lower():
  note('OOM fallback: '+base+' batch four; preserve failed attempt')
  fallback=root/'runs'/f'{base}_b4_s{seed}'/'run.json'
  if not fallback.exists():call(cmd+['--batch-size','4'],env)
  r=json.loads(fallback.read_text())
  if r['status']=='ok':return r
 raise RuntimeError('Inference failed: '+name)
def validate_record(r):
 import torch,numpy as np
 folder=root/'runs'/r['name']
 if r['name'].startswith('mc_'):
  data=torch.load(folder/'validation_samples.pt',map_location='cpu',weights_only=True)
  if not all(torch.isfinite(data[k]).all() for k in ['pred','gt']):raise ValueError('Nonfinite video output')
  from make_figures import filmstrips
  filmstrips(root,[dict(run=r['name'])],d/'figures')
 else:
  data=json.loads((folder/'maze_metrics.json').read_text())
  if not all(np.isfinite(data[k]).all() for k in ['episode_reward','episode_reward_if_stay','first_reach']):raise ValueError('Nonfinite maze output')
 if a.unattended:
  note('completed '+r['name']+'; automated output checks pass; visual review deferred (--unattended)')
  return
 note('completed '+r['name']+'; automated output checks pass; waiting for visual review')
 while not (folder/'visual_review.json').exists():time.sleep(5)
 review=json.loads((folder/'visual_review.json').read_text())
 if not review.get('approved_to_continue'):raise RuntimeError('Visual review did not approve continuation')
 note('visual review recorded for '+r['name'])
try:
 note('waiting for already-running '+a.wait_run)
 record=root/'runs'/a.wait_run/'run.json'
 while not record.exists():
  try:os.kill(a.wait_pid,0)
  except ProcessLookupError:raise RuntimeError('Existing 8x launcher exited without a run record; inspect log')
  time.sleep(10)
 videos=[]
 for base in ['mc_ar_1x','mc_ar_8x','mc_ar_2x','mc_ar_4x','mc_fs2_1x','mc_fs2_2x','mc_fs2_4x','mc_fs2_8x']:
  r=run(base);validate_record(r);videos.append(r)
 if sum(r['gpu_hours'] for r in videos)<1.5:
  for seed in [1,2]:
   for base in ['mc_ar_1x','mc_ar_2x','mc_ar_4x','mc_ar_8x','mc_fs2_1x','mc_fs2_2x','mc_fs2_4x','mc_fs2_8x']:
    r=run(base,seed=seed);validate_record(r)
 else:note('Video repeats omitted: initial eight runs exceed the 1.5 GPU-hour repeat threshold')
 call([sys.executable,str(scripts/'measure_all.py')])
 call([sys.executable,str(scripts/'make_figures.py')])
 defaults={}
 for env,g in [('medium',3),('large',2)]:
  r=run(f'maze_{env}_g{g}','maze');validate_record(r);defaults[env]=r
 for env,g0 in [('medium',3),('large',2)]:
  for g in range(1,6):
   if g!=g0:
    r=run(f'maze_{env}_g{g}','maze');validate_record(r)
  if defaults[env]['wall_seconds']<1200:
   for seed in [1,2]:
    r=run(f'maze_{env}_g{g0}','maze',seed);validate_record(r)
  else:note(env+' baseline repeats omitted: baseline takes at least 20 minutes')
 call([sys.executable,str(scripts/'maze_table.py'),str(root/'runs'),'--out',str(d/'tables')])
 call([sys.executable,str(scripts/'make_figures.py')])
 note('INFERENCE AND ANALYSIS COMPLETE; report integration and visual review remain')
except Exception:
 note('STOPPED: '+traceback.format_exc())
 raise
