from pathlib import Path
import hashlib,json
from omegaconf import OmegaConf
from datasets.offline_rl.maze2d import Maze2dOfflineRLDataset
records=[]
for name in ['medium','large']:
 cfg=OmegaConf.load(f'configurations/dataset/maze2d_{name}.yaml')
 data=Maze2dOfflineRLDataset(cfg,split='validation'); sample=data[0]
 path=Path(cfg.save_dir)/Path(cfg.dataset_url).name
 sha=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(8*1024*1024),b''):sha.update(block)
 record=dict(environment=name,sha256=sha.hexdigest(),bytes=path.stat().st_size,transitions=data.total_steps,validation_windows=len(data),sample_shapes=[list(x.shape) for x in sample])
 print(json.dumps(record),flush=True);records.append(record)
Path('/home/bobywoby/eecs553/deliverables/runtime_checks/maze_data.json').write_text(json.dumps(records,indent=2))
