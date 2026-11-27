# WS4 tiled 30-m dataset — I10|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|AB|S23` (parent `I10|AB`)
- Tile / row / col: `I10` / 2 / 3
- Province: `AB`
- Centroid: 56.083457, -110.044987
- Allocated harvest: 4940.369649 m3
- Productive subcell area: 13313.861762 ha
- Committed geometry area: 14933.305751 ha
- Clipped inventory geometry: 14933.305751 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 148144
- Blocks: 45365
- Forest area: 13332.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3470
- Scheduled area: 943.83 ha
- Eligible blocks (age class >= 40): 34694
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.11 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
