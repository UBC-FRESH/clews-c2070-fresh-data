# WS4 tiled 30-m dataset — J6|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|AB|S23` (parent `J6|AB`)
- Tile / row / col: `J6` / 2 / 3
- Province: `AB`
- Centroid: 55.641344, -119.658248
- Allocated harvest: 92504.910288 m3
- Productive subcell area: 129252.280496 ha
- Committed geometry area: 219407.962134 ha
- Clipped inventory geometry: 219407.962134 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1984297
- Blocks: 857467
- Forest area: 178586.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78417
- Scheduled area: 15102.45 ha
- Eligible blocks (age class >= 40): 784168
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.09 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 27.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
