#!/usr/bin/env python3
"""Inference only. Explicit --execute required; never downloads data or checkpoints."""
import argparse, datetime, hashlib, json, os, shlex, subprocess, sys, time
from pathlib import Path

def plans():
    video=[]; maze=[]
    for schedule in ['ar','fs2']:
        for m in [1,2,4,8]:
            flags=['load=outputs/minecraft.ckpt','dataset.metadata=data/minecraft/metadata.json',f'dataset.validation_multiplier={m}']
            if schedule=='fs2': flags+=['algorithm.scheduling_matrix=full_sequence','algorithm.chunk_size=2']
            video.append((f'mc_{schedule}_{m}x',flags))
    for env,g0 in [('medium',3),('large',2)]:
        mean,std=('[3.5092521,3.4765592]','[1.3371079,1.52102]') if env=='medium' else ('[3.7296331,5.3047247]','[1.8070312,2.5687592]')
        for g in [g0]+[i for i in range(1,6) if i!=g0]:
            maze.append((f'maze_{env}_g{g}',['experiment=exp_planning','algorithm=df_planning',f'dataset=maze2d_{env}',f'dataset.observation_mean={mean}',f'dataset.observation_std={std}','dataset.action_mean=[]','dataset.action_std=[]',f'load=outputs/maze2d_{env}_x.ckpt',f'algorithm.guidance_scale={g}']))
    maze.sort(key=lambda job: 0 if job[0] in ("maze_medium_g3", "maze_large_g2") else 1)
    return video,maze

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',type=Path,default=Path.home()/'eecs553'); p.add_argument('--kind',choices=['video','maze'],default='video'); p.add_argument('--seeds',type=int,nargs='+',default=[0]); p.add_argument('--execute',action='store_true'); p.add_argument('--only',nargs='+'); p.add_argument('--override',nargs='*',default=[]); p.add_argument('--batch-size',type=int); p.add_argument('--skip-completed',action='store_true'); a=p.parse_args(); repo=a.root/'diffusion-forcing'; log=a.root/'deliverables/run_log.md'
    jobs=plans()[a.kind=='maze']
    if a.only:
        unknown=set(a.only)-{name for name,_ in jobs}
        if unknown: raise SystemExit(f'Unknown runs: {unknown}')
        jobs=[job for job in jobs if job[0] in a.only]
    if a.execute:
        import torch
        if not torch.cuda.is_available(): raise SystemExit('CUDA unavailable; no runs started.')
        if a.kind=='video' and not (repo/'data/minecraft/metadata.json').exists(): raise SystemExit('Mini dataset absent; refusing automatic full dataset download.')
        for _,flags in jobs:
            ck=repo/next(v.split('=',1)[1] for v in flags if v.startswith('load='))
            if not ck.exists(): raise SystemExit(f'Missing {ck}; transfer manually.')
        with log.open('a') as f:
            for ck in sorted((repo/'outputs').glob('*.ckpt')):
                digest=hashlib.sha256()
                with ck.open('rb') as stream:
                    for block in iter(lambda: stream.read(8*1024*1024), b''): digest.update(block)
                h=digest.hexdigest(); f.write(f'\n- Checkpoint SHA256: `{h}  {ck.name}`\n')
    for seed in a.seeds:
        for base,flags in jobs:
            name=f'{base}'+(f'_b{a.batch_size}' if a.batch_size else '')+f'_s{seed}'; out=a.root/'runs'/name
            if a.skip_completed and (out/'run.json').exists() and json.loads((out/'run.json').read_text())['status']=='ok': continue
            extra=a.override+([f'experiment.validation.batch_size={a.batch_size}'] if a.batch_size else [])
            cmd=[sys.executable,'-m','main',f'+name={name}','experiment.tasks=[validation]','wandb.mode=offline','wandb.entity=offline-local',f'hydra.run.dir={out}/hydra']+flags+extra
            env=os.environ.copy(); env.update(DF_DUMP_DIR=str(out),DF_SEED=str(seed),WANDB_MODE='offline')
            print('DF_SEED='+str(seed)+' DF_DUMP_DIR='+shlex.quote(str(out))+' '+shlex.join(cmd),flush=True)
            if not a.execute: continue
            out.mkdir(parents=True,exist_ok=False); started=datetime.datetime.now().astimezone().isoformat(); tic=time.monotonic(); peak=0
            with (out/'stdout.log').open('w') as f, (out/'gpu_memory.csv').open('w') as gpu:
                proc=subprocess.Popen([str(Path('/usr/bin/time') if Path('/usr/bin/time').exists() else Path.home()/'eecs553/tools/bin/time'),'-v']+cmd,cwd=repo,env=env,stdout=f,stderr=subprocess.STDOUT)
                while proc.poll() is None:
                    q=subprocess.run(['nvidia-smi','--query-gpu=timestamp,memory.used','--format=csv,noheader,nounits'],capture_output=True,text=True)
                    gpu.write(q.stdout); gpu.flush()
                    for line in q.stdout.splitlines():
                        try: peak=max(peak,float(line.rsplit(',',1)[1]))
                        except ValueError: pass
                    time.sleep(2)
            seconds=time.monotonic()-tic; end=datetime.datetime.now().astimezone().isoformat(); cfg=out/'hydra/.hydra/config.yaml'
            if cfg.exists():
                from omegaconf import OmegaConf
                raw=cfg.read_text(); (out/'hydra_config.yaml').write_text(raw)
                resolved=OmegaConf.to_yaml(OmegaConf.load(cfg),resolve=True); (out/'resolved_config.yaml').write_text(resolved)
                with log.open('a') as f: f.write(f'\n### Resolved config: {name}\n```yaml\n{resolved}\n```\n')
            expected = out / ('validation_samples.pt' if a.kind == 'video' else 'maze_metrics.json')
            if proc.returncode == 0 and not expected.exists():
                proc.returncode = 99  # e.g. upstream silently skipped missing d4rl
            record=dict(name=name,command=shlex.join(cmd),seed=seed,start=started,end=end,wall_seconds=seconds,gpu_hours=seconds/3600,peak_sampled_vram_mib=peak,status='ok' if proc.returncode==0 else 'failed',exit_code=proc.returncode)
            (out/'run.json').write_text(json.dumps(record,indent=2))
            with log.open('a') as f: f.write(f'\n| {name} | `{shlex.join(cmd)}` | {seed} | {started} | {end} | {seconds/60:.3f} | {seconds/3600:.6f} | {peak} MiB (sampled) | {out} | {record["status"]} | env seed fixed 0 for maze |\n')
            records=[json.loads(path.read_text()) for path in (a.root/'runs').glob('*/run.json')]
            total=sum(r['gpu_hours'] for r in records)
            (a.root/'deliverables/tables/run_totals.json').write_text(json.dumps(dict(attempts=len(records),successful=sum(r['status']=='ok' for r in records),inference_wall_gpu_hours=total,setup_diagnostic_wall_gpu_hours=0.0011451148780558165),indent=2))
            with log.open('a') as f: f.write(f'\n- Cumulative inference-attempt wall-GPU-hours: {total:.6f}; includes failed attempts.\n')
            if proc.returncode: raise SystemExit(f'{name} failed. Inspect stdout before resuming.')
if __name__=='__main__': main()
