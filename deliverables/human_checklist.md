# Report checklist

## Experiments

- [x] Download checkpoints and record SHA256 hashes in `checkpoints.json`.
- [x] Verify Python 3.10, CUDA, repository imports, LPIPS, padding and video encoding.
- [x] Verify both Maze2D environments and datasets; record dataset hashes.
- [x] Review the completed Minecraft 1x, 2x and 8x outputs.
- [x] Finish inference and sampled review of all horizon/schedule conditions and maze runs.
- [x] Update figures, tables and resource totals from completed run records.
- [x] Inspect sampled frames of every video and every saved maze plot; document artifacts and coverage limits in `visual_review.md`.
- [ ] Review the Appendix A corrections, especially the KL sign, cumulative weights
  and assumptions for subsequences.

The experiments use a 16 GB RTX 4090 Laptop GPU. Record this distinction from a
24 GB desktop 4090 in the report.

## Report and submission

- [x] Publish code and instrumentation at
  https://github.com/BobyWoby/ECE-553-Project.
- [ ] Contact Boyuan Chen (boyuanc@mit.edu) about robot data/code, the
  teacher-forcing baseline, Table 1 normalization and MCG. Include the Appendix A
  questions if useful. Record the date and any reply; correspondence is currently
  unconfirmed.
- [ ] Copy the course Overleaf template, share with the team and give
  Prof. Fessler view access.
- [ ] Add `eecs553` and the team number to the project name; fill in the report
  title and author names.
- [ ] Move section bodies, figures and `refs.bib` into the template and check
  package requirements in `README.md`.
- [ ] Check the draft against the assignment, reviewer guidelines and F22 example.
- [ ] Check that the six-part reproducibility summary fits one page in the course template (local preview checked separately).
- [x] Integrate measured results and original/ours captions; remove experimental placeholders.
- [ ] Verify the MDF bibliography: arXiv v2 lists Huaidian Hou; confirm the
  preferred name and ICRA proceedings metadata.
- [ ] Compile and review the final PDF in the course template.
- [ ] Submit by the end of 2026-11-07.
