# WS4 tiled 30-m dataset — M28|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S21` (parent `M28|NL`)
- Tile / row / col: `M28` / 2 / 1
- Province: `NL`
- Centroid: 58.487235, -63.530527
- Allocated harvest: 732.336870 m3
- Productive subcell area: 8542.562952 ha
- Committed geometry area: 206709.997744 ha
- Clipped inventory geometry: 206709.997744 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 38237
- Blocks: 23628
- Forest area: 3441.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1356
- Scheduled area: 209.07 ha
- Eligible blocks (age class >= 40): 13551
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.81 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
