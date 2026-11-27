# WS4 tiled 30-m dataset — E7|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|AB|S12` (parent `E7|AB`)
- Tile / row / col: `E7` / 1 / 2
- Province: `AB`
- Centroid: 49.207960, -114.133274
- Allocated harvest: 41121.992170 m3
- Productive subcell area: 39846.201811 ha
- Committed geometry area: 87360.491529 ha
- Clipped inventory geometry: 87360.491529 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 735980
- Blocks: 338070
- Forest area: 66238.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30402
- Scheduled area: 6094.35 ha
- Eligible blocks (age class >= 40): 304011
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.26 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 10.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
