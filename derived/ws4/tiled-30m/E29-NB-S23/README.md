# WS4 tiled 30-m dataset — E29|NB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|NB|S23` (parent `E29|NB`)
- Tile / row / col: `E29` / 2 / 3
- Province: `NB`
- Centroid: 47.679186, -68.124425
- Allocated harvest: 189843.784851 m3
- Productive subcell area: 185183.202459 ha
- Committed geometry area: 198263.494913 ha
- Clipped inventory geometry: 198263.494913 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2058196
- Blocks: 610518
- Forest area: 185237.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46937
- Scheduled area: 11597.40 ha
- Eligible blocks (age class >= 40): 469368
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.13 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 23.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
