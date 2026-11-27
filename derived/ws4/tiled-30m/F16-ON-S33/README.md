# WS4 tiled 30-m dataset — F16|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|ON|S33` (parent `F16|ON`)
- Tile / row / col: `F16` / 3 / 3
- Province: `ON`
- Centroid: 53.139712, -94.535876
- Allocated harvest: 3687.936909 m3
- Productive subcell area: 25734.471143 ha
- Committed geometry area: 32857.773168 ha
- Clipped inventory geometry: 32857.773168 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 329932
- Blocks: 114541
- Forest area: 29693.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11349
- Scheduled area: 2906.37 ha
- Eligible blocks (age class >= 40): 113490
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.64 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 4.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
