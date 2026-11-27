# WS4 tiled 30-m dataset — J25|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J25|QC|S11` (parent `J25|QC`)
- Tile / row / col: `J25` / 1 / 1
- Province: `QC`
- Centroid: 55.933233, -73.957132
- Allocated harvest: 12221.049458 m3
- Productive subcell area: 91192.941008 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1118184
- Blocks: 444764
- Forest area: 100636.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35433
- Scheduled area: 8251.56 ha
- Eligible blocks (age class >= 40): 354323
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.11 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 14.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
