# WS4 tiled 30-m dataset — P8|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P8|NT|S12` (parent `P8|NT`)
- Tile / row / col: `P8` / 1 / 2
- Province: `NT`
- Centroid: 63.763891, -121.603940
- Allocated harvest: 81.527466 m3
- Productive subcell area: 142920.379368 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1485687
- Blocks: 528401
- Forest area: 133711.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33421
- Scheduled area: 6382.35 ha
- Eligible blocks (age class >= 40): 334202
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.00 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 18.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
