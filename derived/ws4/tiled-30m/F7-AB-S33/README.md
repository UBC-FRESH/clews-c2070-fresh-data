# WS4 tiled 30-m dataset — F7|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|AB|S33` (parent `F7|AB`)
- Tile / row / col: `F7` / 3 / 3
- Province: `AB`
- Centroid: 51.396444, -114.673360
- Allocated harvest: 124459.651060 m3
- Productive subcell area: 142285.085300 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1732252
- Blocks: 763151
- Forest area: 155902.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66212
- Scheduled area: 12453.21 ha
- Eligible blocks (age class >= 40): 662120
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.10 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 23.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
