# WS4 tiled 30-m dataset — I7|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I7|AB|S33` (parent `I7|AB`)
- Tile / row / col: `I7` / 3 / 3
- Province: `AB`
- Centroid: 55.282674, -116.872538
- Allocated harvest: 154024.596877 m3
- Productive subcell area: 211149.245409 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1486818
- Blocks: 523156
- Forest area: 133813.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46364
- Scheduled area: 12816.18 ha
- Eligible blocks (age class >= 40): 463639
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.34 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 18.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
