# WS4 tiled 30-m staged national build

This directory holds real per-50-km-node WS4 datasets built from 30-m
SCANFI pixels. Staged national coverage is in progress. It is a
`model_estimate` / `sensitivity_only` artifact, not official OSeCAN,
not a chain v5.1 change, and not a completed national run.

## Stage table

| Stage | Provinces | Candidates | Built | Validated | Remaining | Complete |
|---|---|---:|---:|---:|---:|---|
| stage1 | NB, NS, PE, NL, YT, NT, NU | 1,254 | 1,042 | 1,042 | 0 | yes |
| stage2 | BC, AB | 713 | 709 | 709 | 0 | yes |
| stage3 | SK, MB | 494 | 2 | 2 | 492 | no |
| stage4 | ON, QC | 1,101 | 2 | 2 | 1,099 | no |

- Candidates: 3,562
- Completed stages: stage1, stage2
- Remaining stages: stage3, stage4
- Completed/validated tiles: 1,755
- Remaining tiles: 1,591
- Explicitly skipped zero-harvest tiles: 203
- Explicitly skipped no-forest sliver tiles: 13

## Storage

- Filesystem: `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/ws4/tiled-30m`
- `df -h`: `Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        15T  9.8T  4.7T  68% /srv/shared-data`
- Free: 5,157.849 GB
- Required minimum: 120.000 GB
- Projected full national: 96.9 GB
- Used by built tiles: 30.740 GB
- Projected remaining: 71.7 GB

## Sample simulation

- Status: pass
- Tiles simulated: 10
- Harvested volume: 37,697,066.921 m3
- Treated/managed area: 150,234.210 ha

## Commands

```bash
# One stage, resumable, datasets + validation only:
.venv/bin/python -m workflows.ws4_instances.build_scanfi_tiled_30m \
  --stage stage1 --resume --datasets-only --simulate-sample 5 \
  --workers 32

# Eventual full national run (all 3,562 candidates):
.venv/bin/python -m workflows.ws4_instances.build_scanfi_tiled_30m --all --include-zero-harvest --workers 32 --years 20 --sample-fraction 0.1
```

See `docs/ws4-tiled-30m-staged-national.md` for the stage plan,
storage basis, and remaining work.
