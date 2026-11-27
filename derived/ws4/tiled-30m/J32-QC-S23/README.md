# WS4 tiled 30-m dataset — J32|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S23` (parent `J32|QC`)
- Tile / row / col: `J32` / 2 / 3
- Province: `QC`
- Centroid: 51.670092, -57.678872
- Allocated harvest: 34270.864762 m3
- Productive subcell area: 169708.476960 ha
- Committed geometry area: 238924.406310 ha
- Clipped inventory geometry: 238924.406310 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1782914
- Blocks: 711276
- Forest area: 160462.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59978
- Scheduled area: 14056.92 ha
- Eligible blocks (age class >= 40): 599779
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.81 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 23.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
