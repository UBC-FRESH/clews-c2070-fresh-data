# WS4 tiled 30-m dataset — O9|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O9|NT|S23` (parent `O9|NT`)
- Tile / row / col: `O9` / 2 / 3
- Province: `NT`
- Centroid: 63.594501, -116.958357
- Allocated harvest: 90.559773 m3
- Productive subcell area: 115433.428079 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1165382
- Blocks: 569677
- Forest area: 104884.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34136
- Scheduled area: 5453.19 ha
- Eligible blocks (age class >= 40): 341356
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.10 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 16.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
