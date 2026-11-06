# Diffusion Forcing reproducibility study

This study evaluates the released Diffusion Forcing checkpoints and works through
Appendix A's ELBO derivation. The report source is in `sections/`; figures and
measured tables are in `figures/` and `tables/`.

The checked-in results cover eight videos each at 1x, 2x and 8x the Minecraft
training horizon. The remaining schedule comparisons and Maze2D evaluations are
unfinished. Completed inference used 2.170549 GPU-hours; metric computation used
0.002542 GPU-hours. These totals exclude unfinished runs. See
`completion_audit.md` for the experiment checklist and `run_log.md` for the
historical run log.

## Report files

- `sections/00_summary.tex`: reproducibility summary.
- `sections/01_intro.tex` through `06_discussion.tex`: report sections.
- `sections/r3_proof.tex`: expanded proof, included by the results section.
- `refs.bib`: bibliography. The MDF venue still needs verification.
- `figures/original_*` and `tables/paper_maze.csv`: material from the paper;
  sources are listed in `figures/PROVENANCE.md`.
- `config_audit/`: planned configurations. Executed configurations are in the
  run records.
- `code_changes.diff`: instrumentation changes against upstream commit
  `475e0bcab87545e48b24b39fb46a81fe59d80594`.
- `preview/`: local PDF previews. Use the course template for submission.

The section files need `graphicx`, `amsmath`, `amssymb`, `booktabs` and `hyperref`.
They contain no document preamble or formatting overrides. Check the summary's
page count after moving it into the course template.

## Environment

The experiments used Python 3.10.22, PyTorch 2.4.1 with CUDA 12.1,
Torchvision 0.19.1, Lightning 2.1.4, and an RTX 4090 Laptop GPU with 16 GB VRAM.
`requirements-inference.txt` contains compatible pins; `requirements-lock.txt`
contains the full package list. `environment.yml` was assembled from package
metadata. `pip_freeze.txt` records the installed environment, including local
wheel paths. Runtime checks and their outputs are in `runtime_checks/`.

On the original workstation:

```bash
source ~/eecs553/.venv/bin/activate
cd ~/eecs553/deliverables
python scripts/check_runtime.py
```

Install GNU Time for wall-time and memory records. The runner uses
`~/eecs553/tools/bin/time` if `/usr/bin/time` is absent. Some setup helpers use
workstation-specific paths; adjust them on another machine.

Download the released checkpoints and Minecraft mini dataset as described in the
upstream README. Their recorded hashes are in `checkpoints.json`. The runner
requires local video metadata so that a missing mini dataset does not trigger a
full dataset download.

Maze2D uses MuJoCo 2.1.0, mujoco-py 2.1.2.14 and D4RL 1.1. Source
`scripts/maze_env.sh` before running the planner. Local GLEW headers and compiler
compatibility flags were needed on this host. Both medium and large environments
passed reset/step and dataset-loading checks. Dataset hashes are in
`runtime_checks/maze_data.json`.

## Run experiments

Check `../setup/queue_status.json` and running processes before restarting the
queue. From this directory, with the inference environment active:

```bash
# Show video commands.
python scripts/run_experiments.py --kind video

# Run seed zero, then compute metrics and figures.
python scripts/run_experiments.py --kind video --execute --skip-completed --override 'algorithm.metrics=[]'
python scripts/measure_all.py
python scripts/make_figures.py

# Run maze evaluations.
source scripts/maze_env.sh
python scripts/run_experiments.py --kind maze --execute
python scripts/maze_table.py ../runs --out tables
python scripts/make_figures.py
```

The runner uses one GPU, saves commands and resolved configurations, samples
VRAM, and stops on failure. It refuses to overwrite existing run directories.
Console output is in `../runs/<name>/stdout.log`. Wall time includes model loading
and logging. Sampled device-wide VRAM can miss brief allocation peaks.
Supplementary FVD is disabled with `algorithm.metrics=[]`.

If a video run runs out of memory, keep its record and rerun with batch size four
under a new name. Use matching batch sizes for schedule comparisons, or report
the difference. Optional video seeds 1 and 2 were budgeted only if the eight
seed-zero runs took less than 1.5 GPU-hours; completed runs already exceed that
threshold.

The queue waits for `runs/<name>/visual_review.json` after each run. Inspect the
filmstrips or maze plans for clipping, padding, freezing and intensity collapse
before recording approval. A queue waiting at this step does not need restarting.

To export completed run records and resource totals:

```bash
python scripts/collect_run_records.py
```

This writes `run_records/`, `tables/run_ledger.csv`, `tables/run_ledger.md` and
`tables/gpu_totals.json`. Totals include failed attempts; setup diagnostics and
metric computation are listed separately. Unfinished jobs are excluded.

## Metrics and comparisons

Video metrics use T,B,C,H,W tensors clamped to [0,1]; raw ranges are recorded
separately. Predictions cover the requested horizon, while ground-truth validity
masks exclude padded transitions. Frame indices follow frame skipping.
Context-only transitions are excluded. The early window ends before frame ten;
the late window contains transitions ending in the last ten frames. At 1x these
windows both cover the generated transitions.

A single seed's standard deviations describe variation across videos. With
repeats, error bars describe variation of seed means. Neither is a confidence
interval. The ground-truth summary band uses the longest autoregressive run at
seed zero to avoid counting duplicate references. Horizon multipliers change
clip enumeration, so batches at different horizons are not paired. LPIPS may
download AlexNet weights on first use.

Maze tables record episode reward, reward-if-stay, first-reach steps and success
fraction. Failed episodes have censored first-reach times. Repeated model seeds
reuse the upstream environment seed of zero. `maze_results.csv` and
`guidance_sweep.csv` contain per-run episode statistics; `maze_seed_summary.csv`
aggregates run means when repeats exist. Verify normalization and goal selection
before comparing these metrics with the paper's Table 1.

The released video model uses temporal attention and sliding windows; the paper
uses a recurrent latent state. The planner is non-causal and omits MCG/MCTG.
Diffuser* refers to the PD-controller variant that ignores generated actions.
The data loader scales pixels by 256. Offline W&B logging still requires a
nonempty entity; the commands use `offline-local`. They also set
`dataset.metadata=data/minecraft/metadata.json` to resolve an upstream reference
to the missing `dataset.name` field.

The proof in `sections/r3_proof.tex` corrects the expected-log-ratio KL sign and
noise-level weights in Appendix A. It distinguishes the printed statements from
the derived result.

## Build the report

Run `python scripts/preview.py` to generate the preview wrappers. Copy the two
wrappers from `preview/` into this directory temporarily, then compile each:

```bash
tectonic summary_check.tex --outdir preview --keep-logs
tectonic draft_check.tex --outdir preview --keep-logs
```

Remove the temporary wrappers afterward. The local summary was checked at 10 pt
with one-inch margins; the course template may paginate differently.

To regenerate original-paper figures, download the arXiv source URL listed in
`figures/PROVENANCE.md` to `../df_src.tar.gz` and extract it into `../df_src/`.
For the standalone 8x temporal-change figure, run `python scripts/r1_plot.py`
after metric extraction. Submission tasks are listed in `human_checklist.md`.
