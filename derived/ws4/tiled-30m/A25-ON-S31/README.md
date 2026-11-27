# WS4 tiled 30-m dataset — A25|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A25|ON|S31` (parent `A25|ON`)
- Tile / row / col: `A25` / 3 / 1
- Province: `ON`
- Centroid: 45.111453, -79.036483
- Allocated harvest: 44328.264952 m3
- Productive subcell area: 157512.417503 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2287997
- Blocks: 669809
- Forest area: 205919.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63029
- Scheduled area: 20010.33 ha
- Eligible blocks (age class >= 40): 630289
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.21 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 26.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
