# WS4 tiled 30-m national sample

This directory holds per-50-km-node WS4 datasets built from 30-m SCANFI
pixels. It is a `model_estimate` / `sensitivity_only` sample, not a
national 30-m run, not official OSeCAN, and not a chain v5.1 change.

## Scope

- Candidate tile datasets: 3,562
- Unique 50-km rectangles: 3,164
- Multi-province rectangles: 398
- Selected/built tiles: 24
- Province-top tiles: 12
- PEI nodes: 13 across 6 parent tiles
- Zero-harvest provinces skipped: NU

## Selected totals

- Fragments: 27,164,931
- Blocks: 10,075,337
- Forest area: 2,444,843.79 ha
- Storage: 0.576 GB

## Full national scale

- Area-scaled fragments: 4,569,451,448
- Area-scaled blocks: 1,694,786,681
- Area-scaled storage: 96.9 GB
- Scale factor: 168.2x

The full 3,562-dataset build is a distributed/storage-scale
operation. It was **not** run here.

## Contents

- `national_tiled_manifest.json` — candidates, selection, per-tile
  counts, validation/simulation status, totals, extrapolation,
  provenance hashes, and the full-run command.
- `<tile_slug>/dataset/` — 12 canonical WS4 tables + `manifest.json`.
- `<tile_slug>/schedules/` — 10% CC schedule.
- `<tile_slug>/runs/` — 20-year simulation outputs.
- `<tile_slug>/inventory_summary.json` — full tile evidence.

## Full-run command

```bash
.venv/bin/python -m workflows.ws4_instances.build_scanfi_tiled_30m --all --workers 32 --years 20 --sample-fraction 0.1
```

See `docs/ws4-tiled-30m-national.md` for architecture and limitations.
