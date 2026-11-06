# Draft reproducibility run log

## Status
- **PAUSED at user request for travel (2026-11-06 00:33 EST). No experiment processes or GPU compute jobs remain. Seven video runs complete; FS2 8x interrupted and archived for restart. Maze runs pending. Current total including interrupted inference: 3.886556 GPU-hours; detailed ledger below. Earlier status bullets are historical and await final integration.**
- R3: completed corrected intended-ELBO derivation and source audit; printed theorem discrepancies explicitly documented.
- R1: 1x, 2x and 8x completed with eight videos each; tensors, metrics and filmstrips reviewed. 4x is next, followed by the chunk-two schedule. R2 / 5.1 / 5.2 pending. User authorized public Drive download; all requested checkpoints and mini dataset are now present.
- Draft sections, bibliography, instrumentation commits/diff, 18 intended configs, original figure assets, runnable analysis/launch scripts, and human checklist prepared.
- Local summary: one page, 10-point article with one-inch margins; full preview: eleven pages after adding the R1 figures and measured results. Real course template still needs human verification.
- Completed inference GPU-hours: **2.170549**; metric postprocessing **0.002542**; setup diagnostics **0.001145**. Completed total **2.174237**. Live jobs excluded.
- Course rubric: **NOT SATISFIED** until the beyond-paper ablation is completed; R1 now supplies an experimental result.

## Environment
Initial commands: `pwd`; `rg --files -g AGENTS.md -g '*ckpt' -g '*quickstart*' -g '*2407*' -g '*SKILL*' . /home/bobywoby/eecs553`; `ls -la`; `nvidia-smi`; `command -v conda`; `command -v pdflatex`; `ls -ld /home/bobywoby/eecs553`.
Workspace initially empty except .git and protected configuration directories. Requested working directory absent. No matching local checkpoint found in workspace.
`nvidia-smi`: NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

| run name | command | seed | start | end | wall min | GPU-h | peak VRAM | output dir | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| check_cuda | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/setup/check_cuda.py` |  | 2026-11-05T20:17:27.288834-05:00 | 2026-11-05T20:17:29.365384-05:00 | 0.035 | 0.000577 | 15 MiB (sampled) | /home/bobywoby/eecs553/setup | ok | setup_diagnostic; live jobs excluded |
| check_metrics | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/setup/check_metrics.py` |  | 2026-11-05T20:17:42.759519-05:00 | 2026-11-05T20:17:44.805455-05:00 | 0.034 | 0.000568 | 15 MiB (sampled) | /home/bobywoby/eecs553/setup | ok | setup_diagnostic; live jobs excluded |
| mc_ar_1x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_ar_1x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_1x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_1x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=1 'algorithm.metrics=[]'` | 0 | 2026-11-05T20:38:49.132028-05:00 | 2026-11-05T20:46:09.153792-05:00 | 7.334 | 0.122228 | 15827 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_1x_s0 | ok | inference; live jobs excluded |
| metrics_20261105_204625 | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/deliverables/scripts/divergence.py /home/bobywoby/eecs553/runs --out /home/bobywoby/eecs553/deliverables/tables` |  | 2026-11-05T20:46:25.445711-05:00 | 2026-11-05T20:46:28.492604-05:00 | 0.051 | 0.000846 | 355 MiB (sampled) | /home/bobywoby/eecs553/analysis_runs/metrics_20261105_204625 | ok | metric_postprocessing; live jobs excluded |
| mc_ar_8x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_ar_8x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_8x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_8x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=8 'algorithm.metrics=[]'` | 0 | 2026-11-05T20:46:46.346008-05:00 | 2026-11-05T22:28:57.020630-05:00 | 102.178 | 1.702965 | 14343 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_8x_s0 | ok | inference; live jobs excluded |
| metrics_20261105_222900 | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/deliverables/scripts/divergence.py /home/bobywoby/eecs553/runs --out /home/bobywoby/eecs553/deliverables/tables` |  | 2026-11-05T22:29:00.322675-05:00 | 2026-11-05T22:29:03.373288-05:00 | 0.051 | 0.000847 | 355 MiB (sampled) | /home/bobywoby/eecs553/analysis_runs/metrics_20261105_222900 | ok | metric_postprocessing; live jobs excluded |
| mc_ar_2x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_ar_2x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_2x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_2x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T22:29:17.241217-05:00 | 2026-11-05T22:50:00.522680-05:00 | 20.721 | 0.345356 | 15849 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_2x_s0 | ok | inference; live jobs excluded |
| metrics_20261105_225002 | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/deliverables/scripts/divergence.py /home/bobywoby/eecs553/runs --out /home/bobywoby/eecs553/deliverables/tables` |  | 2026-11-05T22:50:02.145921-05:00 | 2026-11-05T22:50:05.200009-05:00 | 0.051 | 0.000848 | 355 MiB (sampled) | /home/bobywoby/eecs553/analysis_runs/metrics_20261105_225002 | ok | metric_postprocessing; live jobs excluded |
| mc_ar_4x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_ar_4x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_4x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_4x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=4 'algorithm.metrics=[]'` | 0 | 2026-11-05T22:50:12.545008-05:00 | 2026-11-05T23:37:59.918023-05:00 | 47.790 | 0.796492 | 15939 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_4x_s0 | ok | inference; live jobs excluded |
| mc_fs2_1x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_fs2_1x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_1x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_1x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=1 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T23:38:11.249493-05:00 | 2026-11-05T23:42:09.391775-05:00 | 3.969 | 0.066151 | 15049 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_1x_s0 | ok | inference; live jobs excluded |
| mc_fs2_2x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_fs2_2x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_2x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_2x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=2 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T23:42:11.593111-05:00 | 2026-11-05T23:53:01.395524-05:00 | 10.830 | 0.180501 | 15071 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_2x_s0 | ok | inference; live jobs excluded |
| mc_fs2_4x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_fs2_4x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_4x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_4x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=4 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T23:53:03.651676-05:00 | 2026-11-06T00:17:34.545602-05:00 | 24.515 | 0.408582 | 15196 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_4x_s0 | ok | inference; live jobs excluded |
| mc_fs2_8x_s0_interrupted_20261106_0033 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_fs2_8x_s0_interrupted_20261106_0033 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_8x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_8x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=8 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-06T00:17:36.860572-05:00 | 2026-11-06T00:33:14.998672-05:00 | 15.636 | 0.260594 | 15257 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_8x_s0_interrupted_20261106_0033 | interrupted | inference; live jobs excluded |
| mc_fs2_8x_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/mc_fs2_8x_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_8x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_8x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=8 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-06T00:45:27.736754-05:00 | 2026-11-06T01:37:08.010250-05:00 | 51.657 | 0.860947 | 15257 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_8x_s0 | ok | inference; live jobs excluded |
| metrics_20261106_013709 | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/deliverables/scripts/divergence.py /home/bobywoby/eecs553/runs --out /home/bobywoby/eecs553/deliverables/tables` |  | 2026-11-06T01:37:09.187250-05:00 | 2026-11-06T01:37:13.251209-05:00 | 0.068 | 0.001129 | 355 MiB (sampled) | /home/bobywoby/eecs553/analysis_runs/metrics_20261106_013709 | ok | metric_postprocessing; live jobs excluded |
| maze_medium_g3_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g3_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g3_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g3_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=3` | 0 | 2026-11-06T01:37:24.854479-05:00 | 2026-11-06T01:38:01.143426-05:00 | 0.605 | 0.010080 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g3_s0 | ok | inference; live jobs excluded |
| maze_large_g2_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g2_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g2_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g2_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=2` | 0 | 2026-11-06T01:38:02.358802-05:00 | 2026-11-06T01:38:58.819361-05:00 | 0.941 | 0.015683 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g2_s0 | ok | inference; live jobs excluded |
| maze_medium_g1_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g1_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g1_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g1_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=1` | 0 | 2026-11-06T01:39:00.054516-05:00 | 2026-11-06T01:39:36.363192-05:00 | 0.605 | 0.010086 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g1_s0 | ok | inference; live jobs excluded |
| maze_medium_g2_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g2_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g2_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g2_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=2` | 0 | 2026-11-06T01:39:37.567693-05:00 | 2026-11-06T01:40:13.866083-05:00 | 0.605 | 0.010083 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g2_s0 | ok | inference; live jobs excluded |
| maze_medium_g4_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g4_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g4_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g4_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=4` | 0 | 2026-11-06T01:40:15.049399-05:00 | 2026-11-06T01:40:51.345003-05:00 | 0.605 | 0.010082 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g4_s0 | ok | inference; live jobs excluded |
| maze_medium_g5_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g5_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g5_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g5_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=5` | 0 | 2026-11-06T01:40:52.539970-05:00 | 2026-11-06T01:41:28.846794-05:00 | 0.605 | 0.010085 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g5_s0 | ok | inference; live jobs excluded |
| maze_medium_g3_s1 | `DF_SEED=1 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g3_s1 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g3_s1 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g3_s1/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=3` | 1 | 2026-11-06T01:41:30.050490-05:00 | 2026-11-06T01:42:06.334363-05:00 | 0.605 | 0.010079 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g3_s1 | ok | inference; live jobs excluded |
| maze_medium_g3_s2 | `DF_SEED=2 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_medium_g3_s2 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g3_s2 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g3_s2/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=3` | 2 | 2026-11-06T01:42:07.565993-05:00 | 2026-11-06T01:42:43.862833-05:00 | 0.605 | 0.010082 | 1291 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g3_s2 | ok | inference; live jobs excluded |
| maze_large_g1_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g1_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g1_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g1_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=1` | 0 | 2026-11-06T01:42:45.047994-05:00 | 2026-11-06T01:43:39.503939-05:00 | 0.908 | 0.015127 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g1_s0 | ok | inference; live jobs excluded |
| maze_large_g3_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g3_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g3_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g3_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=3` | 0 | 2026-11-06T01:43:40.691439-05:00 | 2026-11-06T01:44:35.144297-05:00 | 0.908 | 0.015126 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g3_s0 | ok | inference; live jobs excluded |
| maze_large_g4_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g4_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g4_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g4_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=4` | 0 | 2026-11-06T01:44:36.315020-05:00 | 2026-11-06T01:45:30.759652-05:00 | 0.907 | 0.015124 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g4_s0 | ok | inference; live jobs excluded |
| maze_large_g5_s0 | `DF_SEED=0 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g5_s0 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g5_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g5_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=5` | 0 | 2026-11-06T01:45:31.911622-05:00 | 2026-11-06T01:46:28.386303-05:00 | 0.941 | 0.015687 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g5_s0 | ok | inference; live jobs excluded |
| maze_large_g2_s1 | `DF_SEED=1 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g2_s1 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g2_s1 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g2_s1/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=2` | 1 | 2026-11-06T01:46:29.629813-05:00 | 2026-11-06T01:47:26.093354-05:00 | 0.941 | 0.015684 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g2_s1 | ok | inference; live jobs excluded |
| maze_large_g2_s2 | `DF_SEED=2 DF_DUMP_DIR=/home/bobywoby/eecs553/runs/maze_large_g2_s2 WANDB_MODE=offline /home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g2_s2 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g2_s2/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=2` | 2 | 2026-11-06T01:47:27.288538-05:00 | 2026-11-06T01:48:21.728575-05:00 | 0.907 | 0.015122 | 1717 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g2_s2 | ok | inference; live jobs excluded |

## Chronological notes
- First commands were read-only environment inspection; this log transcribes their outputs immediately afterward.
- Section 13 explicitly prohibits Google Drive access, superseding the tarball download recipe. No Google Drive request made.

- Upstream main: 475e0bcab87545e48b24b39fb46a81fe59d80594 (matches prompt). Local branch eecs553-draft.
- Instrumented tensor dumps including dataset validity masks (needed for padded ground truth), maze JSON and PIL image dumps, and Lightning seeding. No sampler/model changes.
- Retained upstream envs.seed(0); repeat seeds vary sampling, not environment seeds. Offline commands use wandb.entity=offline-local to satisfy upstream validation, without account access.
- Commit: [eecs553-draft 25f7426] Add inference dumps, validity masks, and seed instrumentation
 3 files changed, 49 insertions(+)


- 2026-11-05: Source and PDF fetched from arXiv v4; only main cloned (--single-branch). No paper branch access. Source hash recorded in provenance file.
- Driver failure and absent local checkpoints prevent all inference. No MuJoCo installation attempted; this is an earlier-blocker fallback, not a demonstrated MuJoCo failure. No GPU run rows exist because no GPU runs started.
- Host Python is 3.14.9, unsuitable for requested pinned inference stack. Created /tmp/df-analysis with managed Python 3.11 for document/figure tooling only; this is not the inference environment. No torch install or training attempted.
- Added corrected R3 derivation. v4 Claim 3 has positive KL where E_q log(p/q) = -KL; Theorem A.1 reverses model transition conditioning; A.13 is indicator counting; general-distribution weights in A.3 require cumulative probabilities. Do not report literal verification of the printed theorem.
- Verified paper 36M Minecraft parameters, eight A100 video training, Figures 8/9 (same source asset), and Figures 14/15 planning. Verified Table 1 numbers and Diffuser* PD-controller meaning.
- Corrected MDF bibliographic author to Huaidian Hou per arXiv v2; ICRA venue awaits human confirmation. DF BibTeX retains README year 2025 despite conference year 2024.
- Email-sent statement withheld because no evidence of human sending was provided. Explicit honesty requirement takes precedence over the requested canned sentence. Human checklist supplies replacement wording.
- Local instrumentation follow-up commit 792e5ad preserves namespace for validation/test wrappers. git diff --check and Python syntax compilation passed; no actual checkpoint test possible.
- Prepared scripts passed syntax compilation. audit_algebra.py passed counts, nonuniform-weight counterexample, posterior variance, v-parameterization MSE, and negative-KL checks. These are analytical checks, not reproduced experiments.
- Command-print smoke test piped to head emitted BrokenPipe after two lines; this was output truncation, not an inference failure. Full dry-run command files are regenerated without a pipe.
- Run wrapper redirects output to stdout.log instead of tee; samples device-wide VRAM every two seconds; validates expected dumps because upstream can silently skip d4rl interaction. It never downloads checkpoints or starts training.

- Config composition revealed upstream dataset.metadata references absent dataset.name. Video commands explicitly override dataset.metadata=data/minecraft/metadata.json; no model or sampler change. The first audit failed on this interpolation; audit rerun after correction.

- Final checks: all 18 intended Hydra configs composed after explicit metadata-path override; upstream missing-_self_ warning retained. Citation keys resolve. Section files contain no preamble/package/margin/spacing commands. Syntax checks and git diff --check passed.
- Summary local compile: one page including its reference entry. Full local article: eight pages including original-asset check page and bibliography. Final compile has no overfull boxes or unresolved references. Rendered summary, original assets, full-page montage, methodology and proof pages visually inspected.
- Preview setup initially failed because wrappers were compiled from preview/ while inputs are relative to deliverables/. Fixed by compiling temporary root wrappers. One hash-line overflow and adjacent-image overflow were corrected using paragraph boundaries. The templates/section formatting was not changed.
- Public arXiv PDF emitted Poppler/MuPDF cross-reference/color-space warnings. Text extraction was corroborated with LaTeX source; original visual assets came directly from source PNGs rather than affected PDF images.
- Downloaded portable Tectonic 0.17.0 for compilation and a separate Python 3.11 analysis environment; package versions recorded in analysis_pip_freeze.txt. Host pip_freeze.txt is not an inference environment. No conda export can be produced because conda is absent.
- Prepared scripts have not been exercised with real checkpoint outputs. No empirical CSVs, generated videos, metrics or side-by-side experimental comparisons exist yet. Conditional report figure blocks activate only when measured figures exist.

- Final audit timestamp: 2026-11-05T19:33:37.354826-05:00

## Resumed setup after permission change
- GPU access now works with unrestricted tool execution. Earlier device invisibility/driver error was environment-specific; a broken host driver was not established. No driver changes made.
- Actual GPU: NVIDIA GeForce RTX 4090 Laptop GPU, 16376 MiB VRAM, driver 615.78.08. This differs from the assumed desktop 24 GB GPU; adjust batches on demonstrated OOM.
- Rechecked workspace, ~/eecs553, and ~/Downloads: no quickstart archive or checkpoints found. Google Drive prohibition remains in effect.
- Conda absent; using uv-managed Python 3.10 venv at ~/eecs553/.venv instead. Installing complete upstream requirements, with stdout/stderr in setup/install.log. No training authorized or started.

- Dependency source audit found torchmetrics 0.11.4 rejects reduction=none. Corrected divergence.py to instantiate the requested default metric and use its exact underlying net with normalize=True for batched per-image scores; will cross-check their mean against the public metric wrapper. No upstream metric code changed.
- W&B 0.17 source imports moviepy.editor for video encoding; latest MoviePy removes this API. Plan to pin moviepy==1.0.3 after upstream dependency installation, then test local encoding without online logging.
- Large-wheel download throughput was slow. Tested official direct endpoints and a checksum-verified segmented downloader, but concurrent segments competed with the ongoing install rather than improving aggregate throughput. Stopped that auxiliary downloader and retained the original uv installation progress. No unverified wheel was installed.
- Also tested the official PyTorch wheel mirror. Aggregate transfer rate remained constrained; stopped the auxiliary mirror transfers to avoid competing with uv. Original installation continues, with completed packages cached. AlexNet weights completed separately and matched SHA256 7be5be791159472b1fbf3c69796f7cb30dca7ad8466c2df70058c37116cdee02.
- Resumed ranged fetches for only the three critical large wheels (torch 2.4.1, cuDNN 9.1.0.70, cuBLAS 12.1.3.1), preserving partial segments. This concentrates transfers on the longest downloads; all complete wheels require PyPI SHA256 verification. Original installer continues caching other packages. Regenerated command files with the actual Python 3.10 interpreter path.

## Verified runtime after resuming
- Installed complete upstream requirements in Python 3.10.22 uv venv; no packages skipped. Compatible pins: setuptools 65.5.0 (pkg_resources for Lightning), wheel 0.40.0, MoviePy 1.0.3 (moviepy.editor for W&B), Diffusers 0.30.3 (current 0.41.0 calls torch.accelerator, unavailable in torch 2.4).
- Download bottleneck resolved using exact PyPI wheels fetched in ranges; all five large wheels verified against PyPI SHA256. Interrupted duplicate uv transfers only after verified local wheels were ready, then installed from those files. Raw freeze retains local-wheel origins; requirements-lock.txt provides portable version pins.
- Verified torch 2.4.1+cu121, torchvision 0.19.1+cu121, Lightning 2.1.4, TorchMetrics 0.11.4, W&B 0.17.9; uv pip check reports all 118 installed packages compatible.
- /usr/bin/time absent. Built GNU Time 1.9 under ~/eecs553/tools using CFLAGS='-O2 -std=gnu11'; default GCC 16 C mode rejected old signal-handler declarations. Run wrapper uses system GNU Time when present, otherwise this local binary. First timing attempt failed before launching a GPU process; no GPU use in that attempt.
- CUDA tensor and matrix multiplication checks passed. Full repository imports and Hydra CLI config resolution passed. Local W&B MP4 encoding passed, without account access. LPIPS per-image mean matches public TorchMetrics mean; identical frames yield zero and invalid ground-truth transitions are excluded. These synthetic checks are not research experiments and generated no report metrics or videos.
- Fixed Python 3.10 incompatibility in prepared runner: replaced hashlib.file_digest (Python 3.11+) with streaming SHA256 updates. Python 3.10 syntax checks pass; missing-data guard blocks automatic full-dataset download and inference launch.
- CUDA diagnostics finish too quickly for the one-second VRAM sampler: recorded 15 MiB is only the observed device baseline, NOT actual diagnostic peak. Peak memory for research inference remains unknown. GNU Time captures CPU maximum RSS separately.

### Setup diagnostics (excluded from research results)
| run name | command | seed | start | end | wall min | GPU-h | peak VRAM | output dir | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| check_cuda | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/setup/check_cuda.py` | synthetic only | 2026-11-05T20:17:27.288834-05:00 | 2026-11-05T20:17:29.365384-05:00 | 0.034608 | 0.00057681 | sampler missed brief peak | runtime_checks/ | PASS | not a reproduced result |
| check_metrics | `/home/bobywoby/eecs553/.venv/bin/python /home/bobywoby/eecs553/setup/check_metrics.py` | synthetic only | 2026-11-05T20:17:42.759519-05:00 | 2026-11-05T20:17:44.805455-05:00 | 0.034098 | 0.00056831 | sampler missed brief peak | runtime_checks/ | PASS | not a reproduced result |

- Runtime update timestamp: 2026-11-05T20:18:36.562141-05:00

- Final refreshed previews: summary remains one page; full article remains eight pages; no overfull or unresolved-reference warnings. Updated summary and methodology/results pages visually reviewed. No checkpoint or dataset appeared during setup. Runtime installation and smoke checks are complete; all download/install subprocesses have exited. Archive refreshed.

## Goal continuation: Maze2D dependency preflight (2026-11-05 20:19 local)
- Previous turn classified as progress: base runtime and CUDA verified, report refreshed. Current goal remains incomplete: no research inference or beyond-paper ablation exists.
- Rechecked local workspace, ~/eecs553 and ~/Downloads: no checkpoints/quickstart archive. Public search for the exact tarball/checkpoint names found the original README and derivative references, but no alternate author-hosted checkpoint source. No Google Drive access attempted.
- Beginning MuJoCo dependency work with a three-hour maximum effort budget, before the Nov 7 noon cutoff. Passwordless sudo is unavailable; no system packages modified. Base host has Mesa/libGL but lacks OSMesa headers and patchelf. Downloading public MuJoCo 2.1.0 binary to ~/.mujoco and installing user-space build/runtime prerequisites. No training or paper branch access.

### 2026-11-05 20:19–20:25 Detroit: Maze setup and plot validation
- Started Maze compatibility setup before checkpoint arrival to remove independent blockers; three-hour effort cap applies. Installed official MuJoCo 2.1.0 under ~/.mujoco, legacy mujoco-py 2.1.2.14, Cython 0.29.37, Gym 0.19.0, D4RL 1.1, SB3 2.3.2, Shimmy 0.2.1, and D4RL optional import dependencies. Gym required pip 23.0.1 legacy setup.py fallback after malformed old wheel metadata. No system driver or model changes.
- No passwordless sudo. Installed GLEW 2.1 headers locally. GCC 16 initially rejected old generated pointer conversions, implicit declarations and integer conversions; retry uses GNU11 with those warnings downgraded. Native import/reset validation still in progress. Logs in setup/maze-reset-check.log.
- Updated plotting script to use fonts >=8 pt, consistent horizon line styles, seed/video SD in both tables and plots, a single highest-horizon seed for the GT summary band (avoids duplicated references), direct frame axes in comparison figures, and independent maze-figure generation. Synthetic plotting fixtures live only in /tmp/df-plot-smoke and are not report results.
- MuJoCo compilation succeeded using documented local headers/flags. Both Maze2D medium and large passed reset and one random-action step with two SB3 DummyVecEnv environments, using Shimmy compatibility. Torch remains 2.4.1+cu121; CUDA available; pip check reports no broken requirements. Flow/CARLA optional imports warn but do not block Maze2D. This is a CPU simulator setup check, not R2 or a learned policy result.
- Plotting fixture completed end-to-end (all eight conditions, CSV aggregation, PDF/PNG figures, filmstrips and MP4s). Curves and comparison layout visually inspected; fixtures remain outside deliverables. Default medium and large runs now precede guidance sweeps in execution order. Environment freeze and portable specifications refreshed.

- Final continuation check: summary remains one page; full preview eight pages; no overfull boxes or undefined references. Summary visually inspected. Repo instrumentation diff check passed; repo clean. No checkpoints found in final local search. Research GPU-hours remain 0; GPU setup diagnostic wall-hours remain 0.001145.

### Next continuation: remaining prerequisites
- Previous goal turn made concrete progress: legacy simulator setup and figure pipeline validation completed. Checkpoints/archive still absent on renewed local search; Google Drive prohibition remains in force.
- Original Berkeley Maze2D dataset host responds over HTTPS. Downloading medium and large sparse-v1 HDF5 files directly, keeping partial downloads under .part names. This avoids the old HTTP URL without changing model/data content.
- Maze table script now emits per-run episode SD and a separate across-seed summary; the guidance plot includes reward, reward-if-stay and censored first reach. Error-bar units are explicit in CSV. Synthetic fixtures outside deliverables verified known two-seed mean/SD values; these are not research results.

- Both Berkeley HTTPS dataset downloads completed. The repository loader read medium (2,000,000 transitions; sample length 601) and large (4,000,000 transitions; sample length 801). Dataset hashes and sizes recorded in runtime_checks/maze_data.json. No model evaluation or GPU computation performed in this check.
- Final independent prerequisite audit: CUDA, base imports, legacy maze reset/step, maze dataset loading, metric fixtures, plotting/aggregation and local report compilation checked. Mandatory experiment outputs remain absent. Missing author checkpoints and Minecraft mini data persist across consecutive goal turns; obtaining them requires manual transfer under the Google Drive prohibition. No further setup-only checks can establish the missing scientific results.

## User-authorized public Drive download
- User explicitly approved downloading the authors' public Google Drive quickstart archive, superseding the earlier restriction for this file. Started gdown for official file id 1xAOQxWcLzcFyD4zc0_rC9jGXe_uaHb7b. No account sign-in or other Drive access authorized or attempted. GPU still available with 16,376 MiB total VRAM; over 600 GB disk space free.
- Public Drive download succeeded in starting without sign-in: approximately 592 MB. Prepared archive path/link validation before extraction. Initial video inference will use default sampling and batch size eight; supplementary upstream FVD is disabled with algorithm.metrics=[] because this study measures consecutive-frame MSE/LPIPS and eight clips do not support a reliable distributional FVD estimate. This avoids an unrelated I3D detector download; no denoiser, sampler, or metric implementation changes.

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`
- Quickstart archive verified and extracted (83 archive members). Seven checkpoint hashes recorded in checkpoints.json. Minecraft metadata lists ten training and ten validation source clips; ten validation MP4s are present.
- Important checkpoint discrepancy: README says 100k video training steps, but minecraft.ckpt contains global_step=110000 (epoch 0). Report both rather than repeating the README as exact checkpoint metadata. Position-only medium/large checkpoints each contain global_step=200000 (epochs 102/51). Checkpoint state_dict entry counts include buffers and are not reported as trainable-parameter counts.
- Started mc_ar_1x_s0 with batch eight, default denoising settings and supplementary FVD disabled. Timing and device-memory samples are being recorded.
- Planning protocol clarification from executed dependency/source inspection: D4RL registers maze2d-medium-v1 and maze2d-large-v1 with reset_target=False. The main planner uses envs.get_attr('goal_locations'), so these are random starts with a fixed maze goal, not independently random start/goal pairs as suggested in the task. envs.seed(0) fixes the starts across model-seed repeats. Preserve actual code behavior and state this in the report.

### Resolved config: mc_ar_1x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 1
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 1
  scheduling_matrix: autoregressive
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_ar_1x_s0

```

| mc_ar_1x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_1x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_1x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=1 'algorithm.metrics=[]'` | 0 | 2026-11-05T20:38:49.132028-05:00 | 2026-11-05T20:46:09.153792-05:00 | 7.334 | 0.122228 | 15827.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_1x_s0 | ok | env seed fixed 0 for maze |

- GPU metric postprocessing: {"name": "metrics_20261105_204625", "type": "GPU metric postprocessing", "command": ["/home/bobywoby/eecs553/.venv/bin/python", "/home/bobywoby/eecs553/deliverables/scripts/divergence.py", "/home/bobywoby/eecs553/runs", "--out", "/home/bobywoby/eecs553/deliverables/tables"], "start": "2026-11-05T20:46:25.445711-05:00", "end": "2026-11-05T20:46:28.492604-05:00", "wall_seconds": 3.0468727329971443, "gpu_hours": 0.0008463535369436512, "peak_sampled_vram_mib": 355.0, "exit_code": 0}

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`
- mc_ar_1x_s0 completed successfully: eight videos, tensor shape (10,8,3,128,128), two context frames, all GT frames valid. Pred raw range [-0.0769663,1.0808158], GT [0,1], all finite. First two prediction/GT filmstrips visually inspected: plausible Minecraft scenes, no gross saturation; prediction paths differ from GT as expected. Saved PDF/PNG and MP4.
- First measured generated-transition means (1x): MSE 0.0131280 with video SD 0.00648438; AlexNet LPIPS 0.143319 with video SD 0.0542898. These establish the short-horizon reference only, not long-rollout stability. Inference wall time 440.022 s (0.122228 GPU-h), peak sampled VRAM 15,827 MiB. Metrics took 3.047 s (0.000846 GPU-h).
- Started mc_ar_8x_s0 next to prioritize the minimum long-horizon result. Retain batch eight because the full attention window completed without OOM in the 1x run.

- Inference queue: waiting for already-running mc_ar_8x_s0
- Continuing while the verified 8x process runs. Expanded R3's subsequence step explicitly: importance-sample omitted terminal-noise variables, apply Jensen, identify the KL gap and parameter-independent noise entropy. State the paper's consistent-joint-measure assumption and distinguish it from an arbitrary collection of conditional networks. Clarified that code timestep index zero is the first positive-noise step, not the theorem's exactly clean endpoint. No equation numbers added or invented.

- Verified wait: {"time": "2026-11-05T20:57:28.734154-05:00", "run": "mc_ar_8x_s0", "launcher_pid": 1240046, "queue_pid": 2432836, "completed_frames": 12, "requested_frames": 80, "status": "verified live; no restart; no errors observed", "observed_window": {"start": 3, "end": 13}}

- Verified wait: active 8x session 40199 advanced from 12 to 16 of 80 frames; GPU utilization 100%, sampled memory 12,967 MiB. Inference and queue PIDs remain live. No retry, restart or configuration change.
- Queue workflow correction: added an agent visual-review gate after each completed run, matching the prompt's instruction to inspect frames/plans before advancing. Recorded the already-completed 1x visual inspection. Replaced only the idle queue coordinator to load this change; the live 8x launcher/session and GPU subprocess were not interrupted or restarted.

- Inference queue: waiting for already-running mc_ar_8x_s0

- Verified wait: the existing 8x session advanced from 20 to 23/80 frames; inference PID 1240046 and review-gated queue PID 2435512 remain live, with no observed error. No restart or configuration change.

- Verified wait: existing 8x session 40199 advanced from 23 to 30/80 frames. Both inference PID 1240046 and queue PID 2435512 are live; no errors or restarts.

- Verified wait: existing 8x session advanced from 30 to 38/80 frames; inference PID 1240046 and queue PID 2435512 remain live. GPU memory steady at 12,967 MiB, no errors observed.

- Verified wait: existing 8x session advanced from 38 to 45/80 frames, with steady 12,967 MiB sampled VRAM and 100% GPU utilization. Both live processes remain active; no restart or configuration change.

- Verified wait: existing 8x session advanced from 45 to 52/80 frames. Both process handles remain live; steady GPU utilization and memory, no error or restart.

- Verified wait: 8x sampling advanced from 52 to 60/80 frames. Inference and queue process handles remain live; no error, restart, or configuration change.

### Resolved config: mc_ar_8x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 8
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 1
  scheduling_matrix: autoregressive
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_ar_8x_s0

```

| mc_ar_8x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_8x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_8x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=8 'algorithm.metrics=[]'` | 0 | 2026-11-05T20:46:46.346008-05:00 | 2026-11-05T22:28:57.020630-05:00 | 102.178 | 1.702965 | 14343.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_8x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 1.825193; includes failed attempts.

- Inference queue: completed mc_ar_1x_s0; automated output checks pass; waiting for agent visual review

- Inference queue: visual review recorded for mc_ar_1x_s0

- Inference queue: completed mc_ar_8x_s0; automated output checks pass; waiting for agent visual review

- GPU metric postprocessing: {"name": "metrics_20261105_222900", "type": "GPU metric postprocessing", "command": ["/home/bobywoby/eecs553/.venv/bin/python", "/home/bobywoby/eecs553/deliverables/scripts/divergence.py", "/home/bobywoby/eecs553/runs", "--out", "/home/bobywoby/eecs553/deliverables/tables"], "start": "2026-11-05T22:29:00.322675-05:00", "end": "2026-11-05T22:29:03.373288-05:00", "wall_seconds": 3.0505838470016897, "gpu_hours": 0.0008473844019449138, "peak_sampled_vram_mib": 355.0, "exit_code": 0}

- Inference queue: visual review recorded for mc_ar_8x_s0

- Inference queue: running mc_ar_2x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

- 2026-11-05 22:29 EST: 8x inference succeeded, 6130.675 seconds / 1.702965 GPU-hours, sampled peak 14343 MiB. Reviewed first two video filmstrips; recognizable changing terrain with no gross saturation. Measured early/late LPIPS 0.133850/0.136594; MSE 0.014498/0.017802. Wrote visual review marker and released queue for AR2x. Generated and visually checked original-versus-ours R1 strip. R1 interpretation is limited to one seed, eight videos, aggregate temporal metrics.

- 2026-11-05 22:32 EST: Integrated completed R1 results into summary/method/results/discussion. Both local LaTeX checks compile; summary remains one page (visually reviewed), full preview eleven pages including bibliography and original-asset QA page. Intermediate horizons and schedule/maze results are still pending.

- Analysis hardening: maze_table.py now excludes missing/unsuccessful run records, matching divergence.py. This prevents a partial metric dump from a failed planner run entering final tables. No inference/model/sampler logic changed. Human checklist updated to distinguish completed R1 from still-running ablation.

- Additional R1 visual QA: inspected frames 0, 2, 40, 78 and 79 of all eight 8x samples using reproducible CPU-only scripts/video_contact_sheet.py. Recognizable terrain/trees/sky persist, late adjacent frames differ; soft textures remain a quality limitation. Individual late LPIPS means range 0.0723--0.2266, so the aggregate does not conceal a completely frozen late window in any of these eight videos. Sparse inspection is not a guarantee of all-frame semantic coherence.

### Resolved config: mc_ar_2x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 2
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 1
  scheduling_matrix: autoregressive
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_ar_2x_s0

```

| mc_ar_2x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_2x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_2x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T22:29:17.241217-05:00 | 2026-11-05T22:50:00.522680-05:00 | 20.721 | 0.345356 | 15849.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_2x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 2.170549; includes failed attempts.

- Inference queue: completed mc_ar_2x_s0; automated output checks pass; waiting for agent visual review

- GPU metric postprocessing: {"name": "metrics_20261105_225002", "type": "GPU metric postprocessing", "command": ["/home/bobywoby/eecs553/.venv/bin/python", "/home/bobywoby/eecs553/deliverables/scripts/divergence.py", "/home/bobywoby/eecs553/runs", "--out", "/home/bobywoby/eecs553/deliverables/tables"], "start": "2026-11-05T22:50:02.145921-05:00", "end": "2026-11-05T22:50:05.200009-05:00", "wall_seconds": 3.0540614080018713, "gpu_hours": 0.0008483503911116309, "peak_sampled_vram_mib": 355.0, "exit_code": 0}

- Inference queue: visual review recorded for mc_ar_2x_s0

- Inference queue: running mc_ar_4x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

- 2026-11-05 22:50 EST: AR2x completed successfully in 1243.281 seconds (0.345356 GPU-hours), sampled peak 15849 MiB. Reviewed first two filmstrips; scenes remain recognizable and change, with differing predicted/GT motion. Early/late LPIPS 0.108470/0.124770, late video SD 0.061420; early/late MSE 0.008642/0.010443. Saved metric CSVs and agent visual-review record, allowing AR4x to start. Completed overall GPU-hours 2.174237, excluding next live run.

- User requested lower token use and unattended completion. Restarted only the coordinator in unattended mode; existing AR4x inference continues untouched. Subsequent jobs retain automated finite-output checks, timing and dumps. Visual reviews are deferred until after the queue, not falsely marked complete. New coordinator PID 645906.

- Inference queue: waiting for already-running mc_ar_4x_s0

### Resolved config: mc_ar_4x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 4
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 1
  scheduling_matrix: autoregressive
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_ar_4x_s0

```

| mc_ar_4x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_ar_4x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_ar_4x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=4 'algorithm.metrics=[]'` | 0 | 2026-11-05T22:50:12.545008-05:00 | 2026-11-05T23:37:59.918023-05:00 | 47.790 | 0.796492 | 15939.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_ar_4x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 2.967042; includes failed attempts.

- Inference queue: completed mc_ar_1x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: completed mc_ar_8x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: completed mc_ar_2x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: completed mc_ar_4x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: running mc_fs2_1x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: mc_fs2_1x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 1
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 2
  scheduling_matrix: full_sequence
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_fs2_1x_s0

```

| mc_fs2_1x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_1x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_1x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=1 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T23:38:11.249493-05:00 | 2026-11-05T23:42:09.391775-05:00 | 3.969 | 0.066151 | 15049.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_1x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 3.033193; includes failed attempts.

- Inference queue: completed mc_fs2_1x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: running mc_fs2_2x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: mc_fs2_2x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 2
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 2
  scheduling_matrix: full_sequence
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_fs2_2x_s0

```

| mc_fs2_2x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_2x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_2x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=2 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T23:42:11.593111-05:00 | 2026-11-05T23:53:01.395524-05:00 | 10.830 | 0.180501 | 15071.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_2x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 3.213693; includes failed attempts.

- Inference queue: completed mc_fs2_2x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: running mc_fs2_4x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: mc_fs2_4x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 4
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 2
  scheduling_matrix: full_sequence
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_fs2_4x_s0

```

| mc_fs2_4x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_4x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_4x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=4 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-05T23:53:03.651676-05:00 | 2026-11-06T00:17:34.545602-05:00 | 24.515 | 0.408582 | 15196.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_4x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 3.622275; includes failed attempts.

- Inference queue: completed mc_fs2_4x_s0; automated output checks pass; visual review deferred per user request for unattended execution

- Inference queue: running mc_fs2_8x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: mc_fs2_8x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 8
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 2
  scheduling_matrix: full_sequence
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_fs2_8x_s0

```

| mc_fs2_8x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_8x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_8x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=8 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-06T00:17:36.860572-05:00 | 2026-11-06T00:33:14.998672-05:00 | 15.636 | 0.260594 | 15257.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_8x_s0 | failed | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 3.882869; includes failed attempts.

- User requested stop now for travel. Stopped coordinator and interrupted FS2 8x via SIGINT; seven successful video conditions preserved. Interrupted attempt archived as mc_fs2_8x_s0_interrupted_20261106_0033; wall 938.138 seconds / 0.260594 GPU-hours, sampled peak 15257 MiB. No resumable mid-run tensor exists; this single condition will restart. Created scripts/resume_queue.py, which skips completed conditions and refuses duplicate queues. Maze inference has not started.

- Inference queue: waiting for already-running mc_ar_8x_s0

- Inference queue: completed mc_ar_1x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: completed mc_ar_8x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: completed mc_ar_2x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: completed mc_ar_4x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: completed mc_fs2_1x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: completed mc_fs2_2x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: completed mc_fs2_4x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running mc_fs2_8x_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: mc_fs2_8x_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 8.0e-05
    batch_size: 8
    max_epochs: -1
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 1.0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 16-mixed
    compile: false
    batch_size: 8
    val_every_n_step: 5000
    val_every_n_epoch: null
    limit_batch: 1
    inference_mode: true
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 8
    limit_batch: 1
    data:
      num_workers: 16
      shuffle: false
  logging:
    metrics:
    - fvd
dataset:
  debug: false
  metadata: data/minecraft/metadata.json
  data_mean: 0.5
  data_std: 0.5
  save_dir: data/minecraft
  n_frames: 10
  context_length: 2
  resolution: 128
  observation_shape:
  - 3
  - 128
  - 128
  external_cond_dim: 0
  validation_multiplier: 8
  frame_skip: 2
algorithm:
  debug: false
  lr: 8.0e-05
  x_shape:
  - 3
  - 128
  - 128
  frame_stack: 1
  frame_skip: 2
  data_mean: 0.5
  data_std: 0.5
  external_cond_dim: 0
  context_frames: 2
  weight_decay: 0.002
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.99
  uncertainty_scale: 1
  guidance_scale: 0.0
  chunk_size: 2
  scheduling_matrix: full_sequence
  noise_level: random_all
  causal: true
  diffusion:
    objective: pred_v
    beta_schedule: sigmoid
    schedule_fn_kwargs: {}
    clip_noise: 6.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: true
    snr_clip: 5.0
    cum_snr_decay: 0.96
    timesteps: 1000
    sampling_timesteps: 100
    ddim_sampling_eta: 0.0
    stabilization_level: 15
    architecture:
      network_size: 64
      attn_heads: 4
      attn_dim_head: 64
      dim_mults:
      - 1
      - 2
      - 4
      - 8
      resolution: 128
      attn_resolutions:
      - 16
      - 32
      - 64
      - 128
      use_init_temporal_attn: true
      use_linear_attn: true
      time_emb_type: rotary
  n_frames: 10
  metadata: data/minecraft/metadata.json
  metrics: []
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/minecraft.ckpt
name: mc_fs2_8x_s0

```

| mc_fs2_8x_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=mc_fs2_8x_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/mc_fs2_8x_s0/hydra load=outputs/minecraft.ckpt dataset.metadata=data/minecraft/metadata.json dataset.validation_multiplier=8 algorithm.scheduling_matrix=full_sequence algorithm.chunk_size=2 'algorithm.metrics=[]'` | 0 | 2026-11-06T00:45:27.736754-05:00 | 2026-11-06T01:37:08.010250-05:00 | 51.657 | 0.860947 | 15257.0 MiB (sampled) | /home/bobywoby/eecs553/runs/mc_fs2_8x_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.743815; includes failed attempts.

- Inference queue: completed mc_fs2_8x_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: Video repeats omitted: initial eight runs exceed the 1.5 GPU-hour repeat threshold

- GPU metric postprocessing: {"name": "metrics_20261106_013709", "type": "GPU metric postprocessing", "command": ["/home/bobywoby/eecs553/.venv/bin/python", "/home/bobywoby/eecs553/deliverables/scripts/divergence.py", "/home/bobywoby/eecs553/runs", "--out", "/home/bobywoby/eecs553/deliverables/tables"], "start": "2026-11-06T01:37:09.187250-05:00", "end": "2026-11-06T01:37:13.251209-05:00", "wall_seconds": 4.063931681994291, "gpu_hours": 0.0011288699116650807, "peak_sampled_vram_mib": 355.0, "exit_code": 0}

- Inference queue: running maze_medium_g3_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g3_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 3
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g3_s0

```

| maze_medium_g3_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g3_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g3_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=3` | 0 | 2026-11-06T01:37:24.854479-05:00 | 2026-11-06T01:38:01.143426-05:00 | 0.605 | 0.010080 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g3_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.753896; includes failed attempts.

- Inference queue: completed maze_medium_g3_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g2_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g2_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 2
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g2_s0

```

| maze_large_g2_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g2_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g2_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=2` | 0 | 2026-11-06T01:38:02.358802-05:00 | 2026-11-06T01:38:58.819361-05:00 | 0.941 | 0.015683 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g2_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.769579; includes failed attempts.

- Inference queue: completed maze_large_g2_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_medium_g1_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g1_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 1
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g1_s0

```

| maze_medium_g1_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g1_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g1_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=1` | 0 | 2026-11-06T01:39:00.054516-05:00 | 2026-11-06T01:39:36.363192-05:00 | 0.605 | 0.010086 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g1_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.779665; includes failed attempts.

- Inference queue: completed maze_medium_g1_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_medium_g2_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g2_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 2
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g2_s0

```

| maze_medium_g2_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g2_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g2_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=2` | 0 | 2026-11-06T01:39:37.567693-05:00 | 2026-11-06T01:40:13.866083-05:00 | 0.605 | 0.010083 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g2_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.789748; includes failed attempts.

- Inference queue: completed maze_medium_g2_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_medium_g4_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g4_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 4
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g4_s0

```

| maze_medium_g4_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g4_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g4_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=4` | 0 | 2026-11-06T01:40:15.049399-05:00 | 2026-11-06T01:40:51.345003-05:00 | 0.605 | 0.010082 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g4_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.799830; includes failed attempts.

- Inference queue: completed maze_medium_g4_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_medium_g5_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g5_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 5
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g5_s0

```

| maze_medium_g5_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g5_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g5_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=5` | 0 | 2026-11-06T01:40:52.539970-05:00 | 2026-11-06T01:41:28.846794-05:00 | 0.605 | 0.010085 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g5_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.809915; includes failed attempts.

- Inference queue: completed maze_medium_g5_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_medium_g3_s1

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g3_s1
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 3
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g3_s1

```

| maze_medium_g3_s1 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g3_s1 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g3_s1/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=3` | 1 | 2026-11-06T01:41:30.050490-05:00 | 2026-11-06T01:42:06.334363-05:00 | 0.605 | 0.010079 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g3_s1 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.819994; includes failed attempts.

- Inference queue: completed maze_medium_g3_s1; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_medium_g3_s2

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_medium_g3_s2
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-medium-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-medium-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 600
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  reward_mean: 0.0236665
  reward_std: 0.15200786
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 3
  chunk_size: 600
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0236665
  reward_std: 0.15200786
  observation_mean:
  - 3.5092521
  - 3.4765592
  observation_std:
  - 1.3371079
  - 1.52102
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 600
  env_id: maze2d-medium-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_medium_x.ckpt
name: maze_medium_g3_s2

```

| maze_medium_g3_s2 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_medium_g3_s2 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_medium_g3_s2/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_medium 'dataset.observation_mean=[3.5092521,3.4765592]' 'dataset.observation_std=[1.3371079,1.52102]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_medium_x.ckpt algorithm.guidance_scale=3` | 2 | 2026-11-06T01:42:07.565993-05:00 | 2026-11-06T01:42:43.862833-05:00 | 0.605 | 0.010082 | 1291.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_medium_g3_s2 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.830076; includes failed attempts.

- Inference queue: completed maze_medium_g3_s2; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g1_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g1_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 1
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g1_s0

```

| maze_large_g1_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g1_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g1_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=1` | 0 | 2026-11-06T01:42:45.047994-05:00 | 2026-11-06T01:43:39.503939-05:00 | 0.908 | 0.015127 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g1_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.845203; includes failed attempts.

- Inference queue: completed maze_large_g1_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g3_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g3_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 3
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g3_s0

```

| maze_large_g3_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g3_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g3_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=3` | 0 | 2026-11-06T01:43:40.691439-05:00 | 2026-11-06T01:44:35.144297-05:00 | 0.908 | 0.015126 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g3_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.860329; includes failed attempts.

- Inference queue: completed maze_large_g3_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g4_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g4_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 4
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g4_s0

```

| maze_large_g4_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g4_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g4_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=4` | 0 | 2026-11-06T01:44:36.315020-05:00 | 2026-11-06T01:45:30.759652-05:00 | 0.907 | 0.015124 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g4_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.875452; includes failed attempts.

- Inference queue: completed maze_large_g4_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g5_s0

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g5_s0
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 5
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g5_s0

```

| maze_large_g5_s0 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g5_s0 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g5_s0/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=5` | 0 | 2026-11-06T01:45:31.911622-05:00 | 2026-11-06T01:46:28.386303-05:00 | 0.941 | 0.015687 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g5_s0 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.891140; includes failed attempts.

- Inference queue: completed maze_large_g5_s0; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g2_s1

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g2_s1
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 2
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g2_s1

```

| maze_large_g2_s1 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g2_s1 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g2_s1/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=2` | 1 | 2026-11-06T01:46:29.629813-05:00 | 2026-11-06T01:47:26.093354-05:00 | 0.941 | 0.015684 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g2_s1 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.906824; includes failed attempts.

- Inference queue: completed maze_large_g2_s1; automated output checks pass; visual review deferred (--unattended)

- Inference queue: running maze_large_g2_s2

- Checkpoint SHA256: `33c1bc65f82ed3e745924680bd236ddcfdb0a39610f3a5e089d4fd9dfef172f6  maze2d_large_x.ckpt`

- Checkpoint SHA256: `a33b1e52ff46b28b49aa64c707eb6c9252db1f4e85d0cffb491ca194eeda518d  maze2d_large_xv.ckpt`

- Checkpoint SHA256: `a4cbd875ba3ad36a2817f98c178d407b3fd8d228273ff1956327b45f782cf600  maze2d_large_xva.ckpt`

- Checkpoint SHA256: `4fc9ee61a4bf5061c39871ef2e9d0a33e78a474a3f28448ced3100779a5f06d2  maze2d_medium_x.ckpt`

- Checkpoint SHA256: `c16a368397ea15eecf1f5dda78362a3ac2aed37c41a01e25a2d527fc0c2d76fc  maze2d_medium_xv.ckpt`

- Checkpoint SHA256: `769d961dac56b98f44bc028463b09469691a2b4fc58f3c7aec1ee049893e6680  maze2d_medium_xva.ckpt`

- Checkpoint SHA256: `d0d0f9d4481d46acd01af0422a660751425f2506a82ee9fd103798280ea7ffcb  minecraft.ckpt`

### Resolved config: maze_large_g2_s2
```yaml
experiment:
  debug: false
  tasks:
  - validation
  num_nodes: 1
  training:
    precision: 16-mixed
    compile: false
    lr: 0.0005
    batch_size: 1024
    max_epochs: 1000
    max_steps: 200005
    max_time: null
    data:
      num_workers: 8
      shuffle: true
    optim:
      accumulate_grad_batches: 1
      gradient_clip_val: 0
    checkpointing:
      every_n_train_steps: 10000
      every_n_epochs: null
      train_time_interval: null
      enable_version_counter: false
  validation:
    precision: 32
    compile: false
    batch_size: 128
    val_every_n_step: null
    val_every_n_epoch: 10
    limit_batch: 1
    inference_mode: false
    data:
      num_workers: 16
      shuffle: false
  test:
    precision: 16-mixed
    compile: false
    batch_size: 16
    limit_batch: null
    data:
      num_workers: 16
      shuffle: false
dataset:
  debug: false
  env_id: maze2d-large-v1
  save_dir: data/maze2d
  dataset_url: http://rail.eecs.berkeley.edu/datasets/offline_rl/maze2d/maze2d-large-sparse-v1.hdf5
  gamma: 1.0
  episode_len: 800
  observation_shape:
  - 4
  action_dim: 2
  goal_dim: 2
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  reward_mean: 0.0089225
  reward_std: 0.09403666
algorithm:
  debug: false
  lr: 0.0005
  x_shape: null
  frame_stack: 10
  frame_skip: 1
  data_mean: null
  data_std: null
  external_cond_dim: 0
  context_frames: 1
  weight_decay: 0.0001
  warmup_steps: 10000
  optimizer_beta:
  - 0.9
  - 0.999
  uncertainty_scale: 1
  guidance_scale: 2
  chunk_size: 800
  scheduling_matrix: pyramid
  noise_level: random_all
  causal: false
  diffusion:
    objective: pred_x0
    beta_schedule: linear
    schedule_fn_kwargs: {}
    clip_noise: 20.0
    use_snr: false
    use_cum_snr: false
    use_fused_snr: false
    snr_clip: 5.0
    cum_snr_decay: 0.98
    timesteps: 1000
    sampling_timesteps: 50
    ddim_sampling_eta: 0.0
    stabilization_level: 10
    architecture:
      network_size: 128
      num_layers: 12
      attn_heads: 4
      dim_feedforward: 512
  reward_mean: 0.0089225
  reward_std: 0.09403666
  observation_mean:
  - 3.7296331
  - 5.3047247
  observation_std:
  - 1.8070312
  - 2.5687592
  action_mean: []
  action_std: []
  gamma: 1.0
  episode_len: 800
  env_id: maze2d-large-v1
  open_loop_horizon: 50
  use_reward: false
  plot_start_goal: true
  padding_mode: same
debug: false
wandb:
  entity: offline-local
  project: diffusion-forcing
  mode: offline
resume: null
load: outputs/maze2d_large_x.ckpt
name: maze_large_g2_s2

```

| maze_large_g2_s2 | `/home/bobywoby/eecs553/.venv/bin/python -m main +name=maze_large_g2_s2 'experiment.tasks=[validation]' wandb.mode=offline wandb.entity=offline-local hydra.run.dir=/home/bobywoby/eecs553/runs/maze_large_g2_s2/hydra experiment=exp_planning algorithm=df_planning dataset=maze2d_large 'dataset.observation_mean=[3.7296331,5.3047247]' 'dataset.observation_std=[1.8070312,2.5687592]' 'dataset.action_mean=[]' 'dataset.action_std=[]' load=outputs/maze2d_large_x.ckpt algorithm.guidance_scale=2` | 2 | 2026-11-06T01:47:27.288538-05:00 | 2026-11-06T01:48:21.728575-05:00 | 0.907 | 0.015122 | 1717.0 MiB (sampled) | /home/bobywoby/eecs553/runs/maze_large_g2_s2 | ok | env seed fixed 0 for maze |

- Cumulative inference-attempt wall-GPU-hours: 4.921946; includes failed attempts.

- Inference queue: completed maze_large_g2_s2; automated output checks pass; visual review deferred (--unattended)

- Inference queue: INFERENCE AND ANALYSIS COMPLETE; report integration and visual review remain

- 2026-11-06: Completed sampled visual review for all 22 successful runs, integrated video/maze/sweep results, corrected maze plan filename discovery and refreshed run records/resource totals. See visual_review.md for artifacts and coverage limits.

- 2026-11-06T12:35:06.812467-05:00: Rebuilt and visually checked the 1-page summary and 16-page local report preview; no final TeX layout/undefined-reference warnings. Course-template export remains a team task.
