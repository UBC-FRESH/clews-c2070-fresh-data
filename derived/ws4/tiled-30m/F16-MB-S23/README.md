# WS4 tiled 30-m dataset — F16|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S23` (parent `F16|MB`)
- Tile / row / col: `F16` / 2 / 3
- Province: `MB`
- Centroid: 52.971864, -95.047284
- Allocated harvest: 983.774919 m3
- Productive subcell area: 26597.977250 ha
- Committed geometry area: 32577.775344 ha
- Clipped inventory geometry: 32577.775344 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 248350
- Blocks: 89035
- Forest area: 22351.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8188
- Scheduled area: 1797.75 ha
- Eligible blocks (age class >= 40): 81875
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.63 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 3.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
