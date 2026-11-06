#!/usr/bin/env python3
"""Read-only dependency/CUDA preflight; does not build a model or fetch data."""
import importlib, json, sys
from pathlib import Path
repo=Path.home()/'eecs553/diffusion-forcing';sys.path.insert(0,str(repo))
mods=['torch','torchvision','lightning','torchmetrics','wandb','hydra','moviepy.editor','main','experiments']
versions={}
for name in mods:
 m=importlib.import_module(name);versions[name]=getattr(m,'__version__','import OK')
import torch
versions['cuda_available']=torch.cuda.is_available()
if versions['cuda_available']:
 versions['gpu']=torch.cuda.get_device_name(0);versions['vram_bytes']=torch.cuda.get_device_properties(0).total_memory
versions['checkpoint_present']=(repo/'outputs/minecraft.ckpt').exists()
versions['dataset_metadata_present']=(repo/'data/minecraft/metadata.json').exists()
print(json.dumps(versions,indent=2))
