#!/usr/bin/env python3
import argparse
from pathlib import Path
from hydra import compose,initialize_config_dir
from omegaconf import OmegaConf
from run_experiments import plans
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path.home()/'eecs553');a=p.parse_args();out=a.root/'deliverables/config_audit';out.mkdir(exist_ok=True)
with initialize_config_dir(version_base=None,config_dir=str(a.root/'diffusion-forcing/configurations')):
 for name,flags in sum(plans(),[]):
  cfg=compose(config_name='config',overrides=flags+['+name='+name,'experiment.tasks=[validation]','wandb.mode=offline','wandb.entity=offline-local'])
  (out/(name+'.yaml')).write_text(OmegaConf.to_yaml(cfg,resolve=True))
print('Composed 18 intended configurations; these are NOT run outputs.')
