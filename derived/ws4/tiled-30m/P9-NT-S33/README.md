# WS4 tiled 30-m dataset — P9|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P9|NT|S33` (parent `P9|NT`)
- Tile / row / col: `P9` / 3 / 3
- Province: `NT`
- Centroid: 65.328373, -118.456532
- Allocated harvest: 93.454439 m3
- Productive subcell area: 122113.542037 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1596042
- Blocks: 751363
- Forest area: 143643.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66308
- Scheduled area: 11873.52 ha
- Eligible blocks (age class >= 40): 663074
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.79 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 22.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
