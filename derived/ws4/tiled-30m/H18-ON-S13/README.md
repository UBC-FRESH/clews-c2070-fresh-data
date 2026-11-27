# WS4 tiled 30-m dataset — H18|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|ON|S13` (parent `H18|ON`)
- Tile / row / col: `H18` / 1 / 3
- Province: `ON`
- Centroid: 55.004334, -89.991440
- Allocated harvest: 10535.772862 m3
- Productive subcell area: 131722.308145 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1605427
- Blocks: 627869
- Forest area: 144488.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53862
- Scheduled area: 12567.42 ha
- Eligible blocks (age class >= 40): 538617
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.31 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 20.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
