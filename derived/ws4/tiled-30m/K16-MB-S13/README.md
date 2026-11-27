# WS4 tiled 30-m dataset — K16|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K16|MB|S13` (parent `K16|MB`)
- Tile / row / col: `K16` / 1 / 3
- Province: `MB`
- Centroid: 59.261967, -94.985179
- Allocated harvest: 361.913409 m3
- Productive subcell area: 19569.030073 ha
- Committed geometry area: 116363.407125 ha
- Clipped inventory geometry: 116363.407125 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 132923
- Blocks: 81499
- Forest area: 11963.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6291
- Scheduled area: 979.65 ha
- Eligible blocks (age class >= 40): 62907
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.75 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 2.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
