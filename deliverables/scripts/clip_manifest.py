#!/usr/bin/env python3
"""List the deterministic validation windows selected by the released dataset."""
import csv,sys
from pathlib import Path
from hydra import initialize_config_dir,compose
root=Path.home()/'eecs553';repo=root/'diffusion-forcing';sys.path.insert(0,str(repo))
from datasets.video.minecraft_video_dataset import MinecraftVideoDataset
rows=[]
with initialize_config_dir(config_dir=str(repo/'configurations'),version_base=None):
 for multiplier in [1,2,4,8]:
  cfg=compose(config_name='config',overrides=[f'dataset.validation_multiplier={multiplier}','dataset.metadata=data/minecraft/metadata.json'])
  assert cfg.experiment.validation.data.shuffle is False
  dataset=MinecraftVideoDataset(cfg.dataset,'validation')
  for i in range(8):
   file_idx,frame_idx=dataset.split_idx(dataset.idx_remap[i])
   rows.append(dict(multiplier=multiplier,batch_index=i,source=str(dataset.data_paths[file_idx]),start_raw_frame=int(frame_idx),requested_raw_frames=int(dataset.n_frames),frame_skip=int(dataset.frame_skip)))
with (root/'deliverables/tables/validation_clip_manifest.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('Recorded 8 candidate clips per horizon; actual batch count comes from run config.')
