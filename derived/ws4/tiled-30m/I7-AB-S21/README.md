# WS4 tiled 30-m dataset — I7|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I7|AB|S21` (parent `I7|AB`)
- Tile / row / col: `I7` / 2 / 1
- Province: `AB`
- Centroid: 54.536380, -118.088237
- Allocated harvest: 154024.596877 m3
- Productive subcell area: 211149.245409 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2662148
- Blocks: 1085953
- Forest area: 239593.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96912
- Scheduled area: 19252.53 ha
- Eligible blocks (age class >= 40): 969111
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 34.17 MB
- Schedules: 1.16 MB
- Runs: 0.00 MB
- Total: 35.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
