# WS4 tiled 30-m dataset — K10|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K10|AB|S23` (parent `K10|AB`)
- Tile / row / col: `K10` / 2 / 3
- Province: `AB`
- Centroid: 58.693262, -110.853248
- Allocated harvest: 78980.366110 m3
- Productive subcell area: 180525.622718 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1079882
- Blocks: 462729
- Forest area: 97189.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37680
- Scheduled area: 6873.57 ha
- Eligible blocks (age class >= 40): 376797
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.04 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 14.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
