#!/usr/bin/env python3
"""Export completed-run evidence and totals; never infer completion from a process log."""
import csv,datetime,json,shutil,shlex
from pathlib import Path
root=Path.home()/'eecs553';d=root/'deliverables';records=[]
for directory,kind in [('runs','inference'),('analysis_runs','metric_postprocessing')]:
 for path in sorted((root/directory).glob('*/run.json')):
  raw=json.loads(path.read_text());out=d/'run_records'/path.parent.name;out.mkdir(parents=True,exist_ok=True)
  for filename in ['run.json','stdout.log','gpu_memory.csv','hydra_config.yaml','resolved_config.yaml','visual_review.json']:
   if (path.parent/filename).exists():shutil.copy2(path.parent/filename,out/filename)
  command=raw['command'];command=command if isinstance(command,str) else ' '.join(command)
  records.append(dict(name=raw['name'],kind=kind,command=command,seed=raw.get('seed',''),start=raw['start'],end=raw['end'],wall_minutes=raw['wall_seconds']/60,gpu_hours=raw['gpu_hours'],peak_sampled_vram_mib=raw['peak_sampled_vram_mib'],status=raw.get('status','ok' if raw['exit_code']==0 else 'failed'),output_dir=str(path.parent)))
for name in ['check_cuda','check_metrics']:
 path=root/'setup'/f'{name}_timing.json'
 if path.exists():
  raw=json.loads(path.read_text());records.append(dict(name=name,kind='setup_diagnostic',command=raw['command'],seed='',start=raw['start'],end=raw['end'],wall_minutes=raw['wall_seconds']/60,gpu_hours=raw['wall_gpu_hours_accounting'],peak_sampled_vram_mib=raw['peak_device_vram_mib_sampled'],status='ok' if raw['exit_code']==0 else 'failed',output_dir=str(path.parent)))
with (d/'tables/run_ledger.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
totals={kind:sum(r['gpu_hours'] for r in records if r['kind']==kind) for kind in ['inference','metric_postprocessing','setup_diagnostic']}
totals['total_completed_wall_gpu_hours']=sum(totals.values());totals['as_of']=datetime.datetime.now().astimezone().isoformat();totals['live_jobs_excluded']=True
(d/'tables/gpu_totals.json').write_text(json.dumps(totals,indent=2))
with (d/'tables/run_ledger.md').open('w') as f:
 f.write('| Run | Type | Seed | Wall min | GPU-h | Sampled VRAM MiB | Status |\n|---|---|---|---:|---:|---:|---|\n')
 for r in records:f.write(f"| {r['name']} | {r['kind']} | {r['seed']} | {r['wall_minutes']:.3f} | {r['gpu_hours']:.6f} | {r['peak_sampled_vram_mib']:.0f} | {r['status']} |\n")
print(json.dumps(totals,indent=2))

# Keep the requested full ledger near the top of the continuous run log.
# Commands include the seed/dump environment reconstructed from explicit run fields.
log=d/'run_log.md'
content=log.read_text()
start=content.index('| run name | command | seed | start | end | wall min | GPU-h | peak VRAM | output dir | status | notes |')
end=content.index('\n## Chronological notes',start)
lines=['| run name | command | seed | start | end | wall min | GPU-h | peak VRAM | output dir | status | notes |',
       '|---|---|---|---|---|---|---|---|---|---|---|']
for r in sorted(records,key=lambda r:r['start']):
 command=r['command']
 if r['kind']=='inference':
  command=f"DF_SEED={r['seed']} DF_DUMP_DIR={shlex.quote(r['output_dir'])} WANDB_MODE=offline "+command
 command=command.replace('|','&#124;').replace('\n',' ')
 lines.append(f"| {r['name']} | `{command}` | {r['seed']} | {r['start']} | {r['end']} | {r['wall_minutes']:.3f} | {r['gpu_hours']:.6f} | {r['peak_sampled_vram_mib']:.0f} MiB (sampled) | {r['output_dir']} | {r['status']} | {r['kind']}; live jobs excluded |")
log.write_text(content[:start]+'\n'.join(lines)+'\n'+content[end:])
