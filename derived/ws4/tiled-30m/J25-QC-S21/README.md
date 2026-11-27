# WS4 tiled 30-m dataset — J25|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J25|QC|S21` (parent `J25|QC`)
- Tile / row / col: `J25` / 2 / 1
- Province: `QC`
- Centroid: 56.366983, -73.688407
- Allocated harvest: 12221.049458 m3
- Productive subcell area: 91192.941008 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1144483
- Blocks: 520386
- Forest area: 103003.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38602
- Scheduled area: 7769.61 ha
- Eligible blocks (age class >= 40): 386015
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.27 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 15.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
