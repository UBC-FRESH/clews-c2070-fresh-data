# WS4 tiled 30-m dataset — F32|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F32|QC|S23` (parent `F32|QC`)
- Tile / row / col: `F32` / 2 / 3
- Province: `QC`
- Centroid: 47.239287, -61.940875
- Allocated harvest: 787.511203 m3
- Productive subcell area: 2281.503980 ha
- Committed geometry area: 5380.408260 ha
- Clipped inventory geometry: 5380.408260 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 35210
- Blocks: 16459
- Forest area: 3168.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1322
- Scheduled area: 314.46 ha
- Eligible blocks (age class >= 40): 13212
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.67 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
