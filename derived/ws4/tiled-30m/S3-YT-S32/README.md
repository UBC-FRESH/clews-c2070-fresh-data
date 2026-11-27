# WS4 tiled 30-m dataset — S3|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S3|YT|S32` (parent `S3|YT`)
- Tile / row / col: `S3` / 3 / 2
- Province: `YT`
- Centroid: 64.282808, -140.842015
- Allocated harvest: 98.842169 m3
- Productive subcell area: 40769.896380 ha
- Committed geometry area: 52274.762758 ha
- Clipped inventory geometry: 52274.762758 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 541079
- Blocks: 127314
- Forest area: 48697.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10631
- Scheduled area: 1958.13 ha
- Eligible blocks (age class >= 40): 106307
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.93 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 6.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
