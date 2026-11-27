# WS4 tiled 30-m dataset — H8|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H8|AB|S32` (parent `H8|AB`)
- Tile / row / col: `H8` / 3 / 2
- Province: `AB`
- Centroid: 54.275329, -114.611868
- Allocated harvest: 68172.895881 m3
- Productive subcell area: 119882.668469 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1250745
- Blocks: 553551
- Forest area: 112567.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47376
- Scheduled area: 9536.49 ha
- Eligible blocks (age class >= 40): 473757
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.23 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 17.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
