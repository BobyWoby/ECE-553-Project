"""Time setup checks and keep their accounting separate from research inference."""
import datetime,json,subprocess,sys,time
from pathlib import Path
root=Path('/home/bobywoby/eecs553');script=Path(sys.argv[1]);name=script.stem
out=root/'setup'/f'{name}.log';start=datetime.datetime.now().astimezone().isoformat();t=time.monotonic()
with out.open('w') as f:
 proc=subprocess.Popen([str(Path('/usr/bin/time') if Path('/usr/bin/time').exists() else Path.home()/'eecs553/tools/bin/time'),'-v',sys.executable,str(script)],cwd=root/'diffusion-forcing',stdout=f,stderr=subprocess.STDOUT)
 peak=0
 while proc.poll() is None:
  q=subprocess.run(['nvidia-smi','--query-gpu=memory.used','--format=csv,noheader,nounits'],capture_output=True,text=True)
  for v in q.stdout.splitlines():
   try:peak=max(peak,float(v))
   except ValueError:pass
  time.sleep(1)
secs=time.monotonic()-t
r={'name':name,'type':'setup diagnostic, not research result','command':f'{sys.executable} {script}','start':start,'end':datetime.datetime.now().astimezone().isoformat(),'wall_seconds':secs,'wall_gpu_hours_accounting':secs/3600,'peak_device_vram_mib_sampled':peak,'exit_code':proc.returncode}
(root/'setup'/f'{name}_timing.json').write_text(json.dumps(r,indent=2));print(json.dumps(r));print(out.read_text()[-5000:]);sys.exit(proc.returncode)
