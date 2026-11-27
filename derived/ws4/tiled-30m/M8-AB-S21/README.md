# WS4 tiled 30-m dataset — M8|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|AB|S21` (parent `M8|AB`)
- Tile / row / col: `M8` / 2 / 1
- Province: `AB`
- Centroid: 59.959330, -119.523023
- Allocated harvest: 4696.863362 m3
- Productive subcell area: 12412.592206 ha
- Committed geometry area: 25680.343770 ha
- Clipped inventory geometry: 25680.343770 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 96149
- Blocks: 29910
- Forest area: 8653.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1403
- Scheduled area: 217.35 ha
- Eligible blocks (age class >= 40): 14022
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.41 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
