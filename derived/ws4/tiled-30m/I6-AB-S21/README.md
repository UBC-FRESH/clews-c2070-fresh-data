# WS4 tiled 30-m dataset — I6|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|AB|S21` (parent `I6|AB`)
- Tile / row / col: `I6` / 2 / 1
- Province: `AB`
- Centroid: 53.999535, -119.919193
- Allocated harvest: 24016.996677 m3
- Productive subcell area: 29634.177131 ha
- Committed geometry area: 34555.435719 ha
- Clipped inventory geometry: 34555.435719 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 271521
- Blocks: 131571
- Forest area: 24436.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12246
- Scheduled area: 2253.33 ha
- Eligible blocks (age class >= 40): 122459
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.60 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 4.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
