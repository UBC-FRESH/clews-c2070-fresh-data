# WS4 tiled 30-m dataset — N7|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N7|NT|S21` (parent `N7|NT`)
- Tile / row / col: `N7` / 2 / 1
- Province: `NT`
- Centroid: 60.890452, -123.144533
- Allocated harvest: 283.888167 m3
- Productive subcell area: 199348.083161 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2523171
- Blocks: 1127411
- Forest area: 227085.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 110155
- Scheduled area: 22546.26 ha
- Eligible blocks (age class >= 40): 1101547
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 34.68 MB
- Schedules: 1.32 MB
- Runs: 0.00 MB
- Total: 36.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
