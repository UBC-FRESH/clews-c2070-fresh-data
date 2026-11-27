# WS4 tiled 30-m dataset — H7|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H7|AB|S22` (parent `H7|AB`)
- Tile / row / col: `H7` / 2 / 2
- Province: `AB`
- Centroid: 53.406865, -116.561890
- Allocated harvest: 197916.560201 m3
- Productive subcell area: 219705.769105 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2525371
- Blocks: 1125137
- Forest area: 227283.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 95191
- Scheduled area: 15153.21 ha
- Eligible blocks (age class >= 40): 951902
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.50 MB
- Schedules: 1.14 MB
- Runs: 0.00 MB
- Total: 34.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
