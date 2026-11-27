# WS4 tiled 30-m dataset — E29|NB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|NB|S33` (parent `E29|NB`)
- Tile / row / col: `E29` / 3 / 3
- Province: `NB`
- Centroid: 47.925348, -67.870622
- Allocated harvest: 54748.820071 m3
- Productive subcell area: 53404.760338 ha
- Committed geometry area: 57176.970097 ha
- Clipped inventory geometry: 57176.970097 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 601711
- Blocks: 196748
- Forest area: 54153.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13926
- Scheduled area: 3169.08 ha
- Eligible blocks (age class >= 40): 139254
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.60 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 7.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
