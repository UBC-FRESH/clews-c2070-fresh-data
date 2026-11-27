# WS4 tiled 30-m dataset — E7|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|AB|S32` (parent `E7|AB`)
- Tile / row / col: `E7` / 3 / 2
- Province: `AB`
- Centroid: 49.987606, -114.519165
- Allocated harvest: 55145.155485 m3
- Productive subcell area: 53434.303117 ha
- Committed geometry area: 117151.617284 ha
- Clipped inventory geometry: 117151.617284 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1116480
- Blocks: 537227
- Forest area: 100483.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49552
- Scheduled area: 8187.39 ha
- Eligible blocks (age class >= 40): 495519
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.78 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 16.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
