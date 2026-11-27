# WS4 tiled 30-m dataset — J6|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|AB|S22` (parent `J6|AB`)
- Tile / row / col: `J6` / 2 / 2
- Province: `AB`
- Centroid: 55.374295, -119.976736
- Allocated harvest: 1149.532764 m3
- Productive subcell area: 1606.182101 ha
- Committed geometry area: 2726.521654 ha
- Clipped inventory geometry: 2726.521654 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 29363
- Blocks: 12495
- Forest area: 2642.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1232
- Scheduled area: 251.55 ha
- Eligible blocks (age class >= 40): 12311
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.55 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
