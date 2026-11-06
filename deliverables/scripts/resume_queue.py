#!/usr/bin/env python3
"""Resume saved inference queue; skip successful runs and leave visual review deferred."""
from pathlib import Path
import subprocess
root=Path.home()/'eecs553'
script=root/'deliverables/scripts/finish_experiments.py'
for entry in Path('/proc').iterdir():
 if not entry.name.isdigit():continue
 try:argv=(entry/'cmdline').read_bytes().split(b'\0')
 except (FileNotFoundError,PermissionError,ProcessLookupError):continue
 if str(script).encode() in argv:
  raise SystemExit('Queue already running; no duplicate started.')
 if b'-m' in argv and b'main' in argv and any(b'+name=mc_' in v or b'+name=maze_' in v for v in argv):
  raise SystemExit('Research inference already running; no duplicate started.')
with (root/'setup/experiment-queue.log').open('a') as log:
 proc=subprocess.Popen([str(root/'.venv/bin/python'),str(script),'--wait-pid','0','--wait-run','mc_ar_8x_s0','--unattended'],cwd=root/'diffusion-forcing',stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
print('Queue resumed in background; PID',proc.pid)
print('Status:',root/'setup/queue_status.json')
