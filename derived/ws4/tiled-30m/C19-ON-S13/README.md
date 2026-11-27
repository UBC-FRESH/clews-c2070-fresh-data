# WS4 tiled 30-m dataset — C19|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C19|ON|S13` (parent `C19|ON`)
- Tile / row / col: `C19` / 1 / 3
- Province: `ON`
- Centroid: 48.243052, -89.067094
- Allocated harvest: 767.019013 m3
- Productive subcell area: 3142.994879 ha
- Committed geometry area: 3764.108003 ha
- Clipped inventory geometry: 3764.108003 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 39615
- Blocks: 13371
- Forest area: 3565.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1303
- Scheduled area: 278.46 ha
- Eligible blocks (age class >= 40): 13024
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.65 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
