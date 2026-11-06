# Experiment and report status

- Complete: all eight seed-zero Minecraft conditions, eight videos each, at 10/20/40/80 frames under AR and FS2 schedules. Video repeats were omitted because the predefined 1.5 GPU-hour threshold was exceeded.
- Complete: 14 Maze2D runs, 128 episodes each. Guidance 1--5 at seed zero in both environments, plus seeds 1 and 2 at medium g3 and large g2. Environment seed remains zero.
- Complete: finite-output checks, raw ranges, masked ground-truth references, temporal MSE/LPIPS, schedule and guidance plots, original/ours comparisons and exported run ledger. Recomputed late-window MSE and maze means match saved tables.
- Complete: sampled visual review of every video and all 448 saved maze images. Findings and review limits are in `visual_review.md`; per-run records are copied into `run_records/`.
- Complete: results integrated into all seven report sections; README and validation status refreshed. Resource accounting includes the interrupted attempt.
- Complete: corrected R3 derivation retained without changing its claims. It is an algebraic audit, not an independent proof of rollout stability.
- Complete: local summary (one page) and report preview (16 pages) rebuilt and all pages visually inspected. No TeX overflow or undefined-reference warnings. This is a local article wrapper, not the course template.

## Remaining team tasks

Course-template transfer and final formatting, team/title details, bibliography verification, author correspondence, assignment review, and submission remain in `human_checklist.md`. No author message has been sent. The historical November 5 archive predates these results and should not be used as the current report. Exact paper replication remains limited by released architecture/protocol changes and absent baselines; empirical completion does not remove those limitations.
