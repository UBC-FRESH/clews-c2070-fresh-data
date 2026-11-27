# WS4 tiled 30-m dataset — Q6|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|NT|S23` (parent `Q6|NT`)
- Tile / row / col: `Q6` / 2 / 3
- Province: `NT`
- Centroid: 64.365972, -128.230888
- Allocated harvest: 25.707972 m3
- Productive subcell area: 42534.431928 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 495881
- Blocks: 221923
- Forest area: 44629.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15065
- Scheduled area: 2962.89 ha
- Eligible blocks (age class >= 40): 150642
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.24 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 7.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
