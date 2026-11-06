#!/usr/bin/env python3
"""Run the requested GPU temporal metrics and account for postprocessing time."""
import datetime,json,subprocess,sys,time
from pathlib import Path
root=Path.home()/'eecs553';d=root/'deliverables';name='metrics_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S');out=root/'analysis_runs'/name;out.mkdir(parents=True)
cmd=[sys.executable,str(d/'scripts/divergence.py'),str(root/'runs'),'--out',str(d/'tables')]
start=datetime.datetime.now().astimezone().isoformat();tic=time.monotonic();peak=0
with (out/'stdout.log').open('w') as f:
 p=subprocess.Popen([str(root/'tools/bin/time'),'-v']+cmd,stdout=f,stderr=subprocess.STDOUT)
 while p.poll() is None:
  q=subprocess.run(['nvidia-smi','--query-gpu=memory.used','--format=csv,noheader,nounits'],capture_output=True,text=True)
  for line in q.stdout.splitlines():
   try:peak=max(peak,float(line))
   except ValueError:pass
  time.sleep(1)
seconds=time.monotonic()-tic
record=dict(name=name,type='GPU metric postprocessing',command=cmd,start=start,end=datetime.datetime.now().astimezone().isoformat(),wall_seconds=seconds,gpu_hours=seconds/3600,peak_sampled_vram_mib=peak,exit_code=p.returncode)
(out/'run.json').write_text(json.dumps(record,indent=2))
with (d/'run_log.md').open('a') as f:f.write('\n- GPU metric postprocessing: '+json.dumps(record)+'\n')
print(json.dumps(record));sys.exit(p.returncode)
