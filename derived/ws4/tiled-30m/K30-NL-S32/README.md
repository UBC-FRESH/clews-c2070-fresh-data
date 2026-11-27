# WS4 tiled 30-m dataset — K30|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K30|NL|S32` (parent `K30|NL`)
- Tile / row / col: `K30` / 3 / 2
- Province: `NL`
- Centroid: 54.902224, -60.548115
- Allocated harvest: 9825.941237 m3
- Productive subcell area: 160907.510440 ha
- Committed geometry area: 244294.537746 ha
- Clipped inventory geometry: 244294.537746 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1840436
- Blocks: 561995
- Forest area: 165639.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47345
- Scheduled area: 13393.62 ha
- Eligible blocks (age class >= 40): 473450
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.80 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 21.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
