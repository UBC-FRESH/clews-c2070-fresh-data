# WS4 tiled 30-m dataset — U7|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S23` (parent `U7|NT`)
- Tile / row / col: `U7` / 2 / 3
- Province: `NT`
- Centroid: 69.579721, -132.854677
- Allocated harvest: 2.134003 m3
- Productive subcell area: 1824.384791 ha
- Committed geometry area: 36413.178841 ha
- Clipped inventory geometry: 36413.178841 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 15844
- Blocks: 11612
- Forest area: 1425.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4264
- Scheduled area: 453.87 ha
- Eligible blocks (age class >= 40): 4264
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.40 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
