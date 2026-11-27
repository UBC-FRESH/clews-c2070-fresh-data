# WS4 tiled 30-m dataset — I15|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I15|MB|S23` (parent `I15|MB`)
- Tile / row / col: `I15` / 2 / 3
- Province: `MB`
- Centroid: 56.930501, -97.285666
- Allocated harvest: 5439.614180 m3
- Productive subcell area: 170601.009204 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1919489
- Blocks: 460722
- Forest area: 172754.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26270
- Scheduled area: 5715.54 ha
- Eligible blocks (age class >= 40): 262692
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.41 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 19.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
