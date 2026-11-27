# WS4 tiled 30-m dataset — F26|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F26|QC|S11` (parent `F26|QC`)
- Tile / row / col: `F26` / 1 / 1
- Province: `QC`
- Centroid: 50.317033, -74.705392
- Allocated harvest: 44490.015211 m3
- Productive subcell area: 161030.532555 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1473339
- Blocks: 575621
- Forest area: 132600.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44117
- Scheduled area: 9885.87 ha
- Eligible blocks (age class >= 40): 441165
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.04 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 19.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
