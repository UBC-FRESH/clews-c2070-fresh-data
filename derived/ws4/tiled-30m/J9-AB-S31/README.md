# WS4 tiled 30-m dataset — J9|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J9|AB|S31` (parent `J9|AB`)
- Tile / row / col: `J9` / 3 / 1
- Province: `AB`
- Centroid: 57.174897, -114.540024
- Allocated harvest: 105766.628084 m3
- Productive subcell area: 224033.462209 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2176454
- Blocks: 709341
- Forest area: 195880.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 64095
- Scheduled area: 14291.28 ha
- Eligible blocks (age class >= 40): 640944
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.16 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 25.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
