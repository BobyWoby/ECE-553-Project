# Original asset provenance

Source: https://arxiv.org/e-print/2407.01392 (v4), fetched 2026-11-05. Archive/PDF hashes: ../source_sha256.txt.

| Export stem | Source path inside archive | Paper location |
|---|---|---|
| original_minecraft_fig8_9 | figures/appendix_vis/df_minecraft_long_1.png | Figures 8 and 9 both reference this same asset |
| original_maze_fig14 | figures/appendix_vis/df_medium_close_mpc.png | Figure 14 |
| original_maze_fig15_medium | figures/appendix_vis/df_medium_close.png | Figure 15 upper |
| original_maze_fig15_large | figures/appendix_vis/df_large_close.png | Figure 15 lower |

`make_figures.py --originals-only` wraps these raster originals into PDFs and 300-dpi preview PNGs. They are not new measurements or vector reconstructions. Empirical plots, when generated from real CSVs, use vector PDF output. No source image is labeled as ours.
