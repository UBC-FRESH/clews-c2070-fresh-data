# WS4 tiled 30-m dataset — F17|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F17|ON|S32` (parent `F17|ON`)
- Tile / row / col: `F17` / 3 / 2
- Province: `ON`
- Centroid: 53.275788, -93.264575
- Allocated harvest: 35793.117881 m3
- Productive subcell area: 200847.237281 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2201338
- Blocks: 753128
- Forest area: 198120.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69134
- Scheduled area: 15328.80 ha
- Eligible blocks (age class >= 40): 691333
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.26 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 27.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
