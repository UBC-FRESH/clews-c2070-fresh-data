# WS4 tiled 30-m dataset — K7|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|AB|S31` (parent `K7|AB`)
- Tile / row / col: `K7` / 3 / 1
- Province: `AB`
- Centroid: 57.518027, -119.884852
- Allocated harvest: 31289.461203 m3
- Productive subcell area: 53848.068675 ha
- Committed geometry area: 57222.386246 ha
- Clipped inventory geometry: 57222.386246 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 615676
- Blocks: 272374
- Forest area: 55410.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26276
- Scheduled area: 5879.07 ha
- Eligible blocks (age class >= 40): 262760
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.68 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 8.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
