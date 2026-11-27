# WS4 tiled 30-m dataset — D7|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D7|AB|S33` (parent `D7|AB`)
- Tile / row / col: `D7` / 3 / 3
- Province: `AB`
- Centroid: 49.028463, -113.341353
- Allocated harvest: 2116.944007 m3
- Productive subcell area: 3987.313957 ha
- Committed geometry area: 18233.825309 ha
- Clipped inventory geometry: 18233.825309 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 27096
- Blocks: 13577
- Forest area: 2438.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 920
- Scheduled area: 168.84 ha
- Eligible blocks (age class >= 40): 9193
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.54 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
