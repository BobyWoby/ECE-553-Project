# Experiment status

- Complete: GPU access, Python environment, checkpoint download and hashes, mini dataset, both Maze2D environments and datasets, instrumentation, corrected R3 derivation.
- Complete initial experiment: Minecraft 1x, 2x and 8x, seed 0, eight videos each. Finite tensors, first two filmstrips visually inspected, MSE/LPIPS CSVs computed.
- Running: Minecraft 4x.
- Queued: remaining video schedule/horizon runs; conditional repeats; both default mazes and guidance sweeps; conditional maze baseline repeats; metrics and figures.
- Still required: inspect remaining outputs, integrate all measured results, final captions/tables and report consistency review, final report export.
- Submission tasks are listed in `human_checklist.md`.

R1 now supplies limited long-horizon evidence with original-versus-ours figures; the beyond-paper requirement remains unfinished. Queue status is ../setup/queue_status.json and logs are ../setup/experiment-queue.log.

## Remaining checks

Check the files below after the remaining runs finish.

| Requirement | Evidence to inspect | Current state |
|---|---|---|
| Main-only, inference-only code and exact upstream revision | Repo branch/commit, code_changes.diff, executed commands in run_records | Main-derived code published on the diffusion-forcing branch; no training |
| Actual environment and checkpoint identity | environment_audit.txt, pip_freeze.txt, requirements-lock.txt, environment.yml, checkpoints.json | Recorded; virtualenv/16 GB Laptop GPU deviations explicit |
| R1 autoregressive 1/2/4/8x, eight videos | run_records/mc_ar_*; corresponding saved tensors in ../runs | 1x, 2x, 8x complete; 4x live |
| Full-sequence chunk-two 1/2/4/8x | run_records/mc_fs2_*; corresponding saved tensors | Queued |
| Conditional video seeds 1–2 | Sum of first eight inference times vs 1.5 GPU-hour threshold | Already exceeds threshold from completed AR runs; repeats not required |
| MSE/LPIPS, GT valid masks, pixel statistics, early/late windows, slopes | divergence.py; tables/divergence_*, ground_truth_*, range_* and per-video CSV | Present for completed video runs; remaining runs pending |
| Filmstrips and MP4s, original-versus-ours R1 figure | figures/frames, r1_minecraft_compare.pdf, original assets and provenance | Present/reviewed for completed runs; remaining runs pending |
| Beyond-paper curves, late-horizon summary, time/video table | make_figures.py; ablation_curves, ablation_summary, sanity_curves and table | Final complete-condition figures pending |
| Maze medium g3 / large g2, exact released metrics | run_records/maze_*, maze_metrics.json arrays, resolved configs | Dependencies/data checked; actual inference pending |
| Maze guidance 1–5 and conditional baseline repeats | All ten seed-zero conditions; default run times vs 20-minute threshold | Queued |
| Original Table 1 next to measured maze results; original/ours plans | paper_maze.csv, maze_results.csv/.tex, plan images and captions | Paper values verified; measured side pending |
| Changed architecture/protocol/metric and missing baseline caveats | Sections 03–06 plus actual resolved configs and source | Drafted; retain in final result text |
| R3 notation, support, Jensen, cancellation, Gaussian weights, A.13, subsequences | r3_proof.tex, audit_algebra.py, source_sha256.txt, actual Appendix A source | Corrected intended derivation complete; printed-paper discrepancies explicit |
| Summary six subsections and one-page local check | 00_summary.tex; preview/summary_check.pdf and render | One-page check passed before latest small metric update; final recheck required |
| All seven section bodies, bibliography, no template formatting changes | sections/*.tex, refs.bib, README package assumptions | Drafts exist; pending results must be integrated |
| Runtime, full commands/seeds/configs/VRAM and total GPU-hours | Main run_log table, run_records, tables/run_ledger.csv, gpu_totals.json | Complete for terminal runs; live jobs excluded |
| Reproducible figure scripts, local compile and visual QA | scripts/, preview logs/renders, per-run visual_review.json | Completed results reviewed; remaining outputs and final compile pending |
| Submission details | human_checklist.md; scan section text for TBD/TEAM/AUTHOR | Team details, author correspondence and course-template review pending |
| Final archive without datasets/checkpoints | ../deliverables_<date>.tar.gz listing and extracted-file consistency | Interim archive exists; final refresh and audit pending |

The report still needs the schedule ablation and, if the released workflow succeeds, the maze evaluations. Update the status from completed runs and reviewed outputs.
