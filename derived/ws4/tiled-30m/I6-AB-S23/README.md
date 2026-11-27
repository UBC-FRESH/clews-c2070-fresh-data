# WS4 tiled 30-m dataset — I6|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|AB|S23` (parent `I6|AB`)
- Tile / row / col: `I6` / 2 / 3
- Province: `AB`
- Centroid: 54.371579, -118.820168
- Allocated harvest: 173757.009406 m3
- Productive subcell area: 214395.915681 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2594058
- Blocks: 1050980
- Forest area: 233465.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89277
- Scheduled area: 16165.26 ha
- Eligible blocks (age class >= 40): 892764
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.03 MB
- Schedules: 1.07 MB
- Runs: 0.00 MB
- Total: 34.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
