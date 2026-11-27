# WS4 tiled 30-m dataset — A24|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S23` (parent `A24|ON`)
- Tile / row / col: `A24` / 2 / 3
- Province: `ON`
- Centroid: 44.781140, -79.738590
- Allocated harvest: 23919.876022 m3
- Productive subcell area: 91894.464666 ha
- Committed geometry area: 191526.953686 ha
- Clipped inventory geometry: 191526.953686 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1421939
- Blocks: 506310
- Forest area: 127974.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43845
- Scheduled area: 11226.33 ha
- Eligible blocks (age class >= 40): 438441
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.58 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 18.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
