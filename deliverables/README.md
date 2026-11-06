# EECS 553 draft reproducibility handoff

**Status: Minecraft 1x, 2x and 8x runs completed, measured and visually reviewed; 4x is next. R3 corrected derivation is complete. The remaining ablation and maze experiments are queued.** GPU access works (RTX 4090 Laptop, 16 GB). Completed inference: 2.170549 GPU-hours; metrics: 0.002542; setup diagnostics: 0.001145. Live queue status: `../setup/queue_status.json`. No training, email, account action, Overleaf access, submission or paper-branch checkout occurred.

## Contents and paste locations

- `sections/00_summary.tex`: summary with six required paragraphs (paste into the matching summary subsections if the template already provides headings).
- `01_intro`, `02_scope`, `03_methodology`, `04_results`, `05_beyond`, `06_discussion`: bodies for the template's corresponding sections. `04_results` includes `sections/r3_proof.tex`.
- `r3_proof.tex`: corrected intended Appendix A proof with explicit support/Jensen/cancellation/Gaussian steps. It identifies discrepancies in the printed v4 statement. It is longer than the main results text; move detailed proof to an appendix if the template budget requires it, retaining the audit summary in Results.
- `refs.bib`: seven references. DF key/year retained from README (2025), despite NeurIPS 2024 conference context. MDF author name follows arXiv v2; venue requires human confirmation.
- `code_changes.diff`: instrumentation against upstream main commit 475e0bcab87545e48b24b39fb46a81fe59d80594. Local repo ../diffusion-forcing, branch eecs553-draft. It additionally preserves video validity masks to exclude padded reference frames.
- `figures/original_*`: original paper assets, not experimental outputs. No fake comparison plots or synthetic experimental CSVs are supplied.
- `tables/paper_maze.csv`: original numbers only. `scripts/` produces empirical CSVs after real inference.
- `pip_freeze.txt`: actual verified inference environment, with local-wheel origins. `requirements-lock.txt`: portable equivalent version pins. `environment.yml`: generated equivalent Conda specification, explicitly NOT a conda export. `host_pip_freeze.txt` and `environment_audit.txt` preserve the initial host audit. `analysis_pip_freeze.txt` describes the document-analysis environment.
- `config_audit/`: composed and resolved intended configs, not configs from executed jobs.
- `preview/`: local article compile check only. Never substitute this wrapper for the course template.

Package assumptions: graphicx, amsmath, amssymb, booktabs, hyperref. No custom style, subcaption, spacing overrides, or document preamble occurs in section files. The preview wrapper alone uses article and geometry. Confirm one-page summary in the actual course template.

## Re-run or resume experiments

A verified Python 3.10.22 virtual environment is installed at ~/eecs553/.venv using uv because Conda is absent. Activate it with `source ~/eecs553/.venv/bin/activate`. The host Python 3.14 is unsuitable for the pinned torch stack. Run `python scripts/check_runtime.py` to verify imports, CUDA and checkpoint/data presence. Do not train. Avoid the paper branch. The authorized quickstart archive is already extracted at the repository root. The runner refuses absent video metadata to avoid triggering a full dataset download.

The queue is already running; do not start duplicate jobs. For a later restart, inspect queue_status.json and the actual process first. From deliverables/, with the inference environment active:

```bash
python scripts/run_experiments.py --kind video                    # print commands only
python scripts/run_experiments.py --kind video --execute --skip-completed --override 'algorithm.metrics=[]'          # seed 0
python scripts/measure_all.py  # GPU metrics plus timing records
python scripts/make_figures.py
# If seed-0 runs used less than ~1.5 GPU-h:
python scripts/run_experiments.py --kind video --seeds 1 2 --execute --skip-completed --override 'algorithm.metrics=[]'
# Recompute metrics/figures after repeats.
```

The runner is sequential, logs full commands and timestamps, saves resolved configs, samples VRAM, and stops on error. It refuses to overwrite a run directory. Console output is saved rather than streamed with tee; inspect `runs/<name>/stdout.log` during execution. Runtime includes model loading and logging; supplementary FVD is disabled by the recorded configuration override; wall time/video is end-to-end validation time, not isolated denoising time. Use only a single GPU. Each record's gpu_hours is wall time / 3600. Sum `run.json` GPU-hours, including failures, into the report and update the status block. Resolved configs are also appended to the log. Review checkpoint load and data-count output before trusting a successful exit code.

On 8x OOM, retain the failed run and rerun under a new name with batch size 4; edit generated flags explicitly and document the deviation. For fairness keep the same batch size for matched schedule comparisons or state the difference. Videos across different multipliers can correspond to different dataset clips; seeds do not fix that confound. Repeats at the same multiplier reuse deterministic dataset order.

Metrics use actual T,B,C,H,W tensors, clamp [0,1] and record raw ranges. Predictions are measured through the requested horizon even after reference data ends; reference masks exclude padded transitions. Frame index is after frame skipping. Initial summaries omit context-only transitions. First-window transitions end at t<10; last-window transitions end at t>=T-10. At 1x both use generated transitions from t=context onward. Per-frame std and one-seed error bars are sample std across videos; with repeats, plot error bars are sample std of seed means. Do not interpret either as a confidence interval. The GT summary band uses only the longest autoregressive run at seed zero and describes variation in video means; duplicated references across seeds and schedules are excluded. Per-run GT curves preserve the actual per-frame band. LPIPS may download its public AlexNet weights when first instantiated.

Maze dependencies and datasets have passed checks. For a later restart:

```bash
python scripts/run_experiments.py --kind maze --execute
python scripts/maze_table.py ../runs --out tables
python scripts/make_figures.py
```

The maze runner includes the five-scale sweep for each environment with defaults first per environment. Inspect default runs before proceeding. Seeds 1/2 are optional only if time permits. Environment seeds remain upstream's hard-coded zero. Episode std must not be described as seed std; non-reaching first_reach values are censored and success_fraction is exported. Confirm paper normalization and single-goal versus random-goal setting before numerical comparisons.

## Findings to preserve

- Diffuser* means its PD-controller variant ignoring generated actions.
- Appendix A Claim 3's expected log ratio has the wrong printed KL sign. A.13 counts indicators. General distribution weights are cumulative probabilities. R3 explicitly derives corrected forms instead of endorsing the printed errors.
- Main uses temporal attention/sliding windows, not the original recurrent latent. Planning is non-causal and lacks MCG/MCTG.
- A dummy nonempty wandb entity is needed even offline. No account login is necessary.
- The code uses /256 pixel scaling, so original data maxima are below 1 before interpolation. Do not infer normalization from an old log_video docstring.
- Author email status is unverified: the draft intentionally does not claim an email was sent.

CUDA computation, repository imports, local video encoding and synthetic LPIPS/padding checks pass. Scripts and instrumentation remain unverified with real checkpoints. Syntax/configuration and proof algebra checks are recorded separately from experimental validation. See human_checklist.md for the submission path and remaining blockers.

- Config composition revealed upstream dataset.metadata references absent dataset.name. Video commands explicitly override dataset.metadata=data/minecraft/metadata.json; no model or sampler change. The first audit failed on this interpolation; audit rerun after correction.

## Local verification and original-asset regeneration

The summary compiles to one page (352 whitespace-delimited words including TeX markup) at 10pt and one-inch margins. The full eight-page local preview includes a separate original-asset rendering check. No final overflow or unresolved-reference warnings remain. These page counts are not guarantees for the course template.

Fetch the arXiv source into ../df_src.tar.gz and extract to ../df_src/ to regenerate original figures; use the source URL in figures/PROVENANCE.md. No checkpoints or datasets are bundled. To repeat the preview, run scripts/preview.py, copy its two wrappers from preview/ temporarily into deliverables/, then run `tectonic summary_check.tex --outdir preview --keep-logs` and similarly for draft_check.tex. Remove the two temporary root wrappers afterward. PDF exports are preview artifacts, not the course-template submission.

## Verified inference setup

Activate `source ~/eecs553/.venv/bin/activate`. Runtime check logs and synthetic smoke-test scripts are in runtime_checks/. No synthetic results were placed in tables/ or runs/. `uv pip check` passes. Install-compatible pins are recorded in requirements-inference.txt; the complete portable package list is requirements-lock.txt. The environment.yml file is an equivalent specification assembled from package metadata because Conda was unavailable.

The runner falls back to ~/eecs553/tools/bin/time if /usr/bin/time is absent. GNU Time 1.9 was built there locally. On another host, install GNU Time or provide that path. Diagnostic VRAM samples missed the brief allocation peaks and must not be used to size experimental batches. Actual GPU is a 16 GB laptop 4090; use measured OOM behavior to decide whether batches must be reduced.

## Legacy Maze2D runtime
Source `scripts/maze_env.sh` before maze commands. MuJoCo 2.1.0, mujoco-py 2.1.2.14 and D4RL 1.1 pass medium/large reset and step checks through SB3 DummyVecEnv. Local GLEW headers and GCC compatibility flags are required on this host; see `runtime_checks/check_maze.log`. Flow/CARLA are optional and absent. No planner checkpoint has been evaluated.

Maze analysis writes `maze_results.csv` (episode SD for every run), `guidance_sweep.csv` (same per-run records) and `maze_seed_summary.csv` (mean of seed means, SD across seed means if repeated; otherwise episode SD). Guidance plots use the latter, displaying all three metrics. These SDs are descriptive, not confidence intervals; the upstream fixed environment seed means repeated model seeds reuse environment initializations.

Both Maze2D sparse-v1 HDF5 datasets are now cached in `../diffusion-forcing/data/maze2d/`, fetched from the original Berkeley host using HTTPS. Repository loading and sample shapes pass; SHA256 values are in `runtime_checks/maze_data.json`. Datasets are excluded from the handoff archive.

Run `python scripts/collect_run_records.py` to export completed-run commands, logs, raw/resolved configs and memory samples into `run_records/`, and produce `tables/run_ledger.csv`, `run_ledger.md` and `gpu_totals.json`. Totals include failed inference attempts and separately identify metric postprocessing and setup diagnostics. Live jobs are excluded until their completion records exist.

The queue pauses after each completed run until the agent has inspected its filmstrip or maze plans and written `runs/<name>/visual_review.json`. This is an agent review step, not a request for human permission. The coordinator may be waiting normally at that gate; inspect its live process and queue status before restarting anything.

For the standalone measured 8x temporal-change and pixel-statistics figure, run `python scripts/r1_plot.py` after metric extraction. This is independent of the pending full ablation.
