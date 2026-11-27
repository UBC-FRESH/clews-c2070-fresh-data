# WS4 tiled 30-m dataset — N11|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N11|NT|S21` (parent `N11|NT`)
- Tile / row / col: `N11` / 2 / 1
- Province: `NT`
- Centroid: 62.830579, -112.118814
- Allocated harvest: 42.605610 m3
- Productive subcell area: 75817.363283 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 740349
- Blocks: 245862
- Forest area: 66631.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5231
- Scheduled area: 1160.46 ha
- Eligible blocks (age class >= 40): 52307
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.57 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 8.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
