# EECS 553: Diffusion Forcing

Reports, experiment scripts and results for our Diffusion Forcing reproducibility study.
See [deliverables/README.md](deliverables/README.md) for environment setup,
experiment commands, validation status, and remaining work.

## Clone with the modified model code

```bash
git clone --recurse-submodules https://github.com/BobyWoby/ECE-553-Project.git
cd ECE-553-Project
```

For an existing clone, run `git submodule update --init --recursive`.
The `diffusion-forcing/` submodule pins our instrumented version of
[upstream Diffusion Forcing](https://github.com/buoyancy99/diffusion-forcing).
Its code history is preserved on this repository's `diffusion-forcing` branch.

- `deliverables/`: report source, preview PDFs, figures, tables, and experiment scripts.
- `runs/` and `analysis_runs/`: lightweight run records, configs, logs, and measurements.
- `setup/`: environment checks and dependency download helpers.

Datasets, checkpoints and local build files are excluded from Git. See
`deliverables/README.md` for download and setup instructions.
Some setup helpers contain paths for the original workstation; adjust those
paths for your environment. Recorded results and logs are snapshots and may
include incomplete runs; consult the validation status before using them.
