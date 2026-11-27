# WS4 tiled 30-m dataset — I8|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I8|AB|S13` (parent `I8|AB`)
- Tile / row / col: `I8` / 1 / 3
- Province: `AB`
- Centroid: 54.848677, -114.096838
- Allocated harvest: 138788.880765 m3
- Productive subcell area: 208941.887280 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2422287
- Blocks: 787237
- Forest area: 218005.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66494
- Scheduled area: 14912.28 ha
- Eligible blocks (age class >= 40): 664934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.25 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 29.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
