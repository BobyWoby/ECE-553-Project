from pathlib import Path
import numpy as np
import wandb
import moviepy.editor
out=Path('/home/bobywoby/eecs553/setup/logging-smoke');out.mkdir(exist_ok=True)
# Construct media locally; no login or online run.
video=wandb.Video(np.zeros((3,3,64,64),dtype=np.uint8),fps=4,format='mp4')
assert Path(video._path).exists()
print('PASS: moviepy.editor import and local wandb.Video encoding',video._path)
