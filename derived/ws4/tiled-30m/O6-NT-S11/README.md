# WS4 tiled 30-m dataset — O6|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O6|NT|S11` (parent `O6|NT`)
- Tile / row / col: `O6` / 1 / 1
- Province: `NT`
- Centroid: 61.087141, -126.514356
- Allocated harvest: 94.353327 m3
- Productive subcell area: 113854.810047 ha
- Committed geometry area: 231717.215462 ha
- Clipped inventory geometry: 231717.215462 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1956078
- Blocks: 744978
- Forest area: 176047.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67620
- Scheduled area: 16392.96 ha
- Eligible blocks (age class >= 40): 676195
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.12 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 24.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
