# WS4 tiled 30-m dataset — R8|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R8|NT|S13` (parent `R8|NT`)
- Tile / row / col: `R8` / 1 / 3
- Province: `NT`
- Centroid: 66.477700, -123.366108
- Allocated harvest: 54.117985 m3
- Productive subcell area: 151558.072555 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 996331
- Blocks: 393938
- Forest area: 89669.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33265
- Scheduled area: 7521.30 ha
- Eligible blocks (age class >= 40): 332647
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.72 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 13.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
