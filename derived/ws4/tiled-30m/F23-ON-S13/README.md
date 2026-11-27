# WS4 tiled 30-m dataset — F23|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|ON|S13` (parent `F23|ON`)
- Tile / row / col: `F23` / 1 / 3
- Province: `ON`
- Centroid: 51.170700, -79.665952
- Allocated harvest: 4089.633621 m3
- Productive subcell area: 62158.041252 ha
- Committed geometry area: 90585.592520 ha
- Clipped inventory geometry: 90585.592520 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 665920
- Blocks: 201650
- Forest area: 59932.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18212
- Scheduled area: 6600.42 ha
- Eligible blocks (age class >= 40): 182112
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.17 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 8.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
