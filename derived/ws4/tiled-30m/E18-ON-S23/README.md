# WS4 tiled 30-m dataset — E18|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E18|ON|S23` (parent `E18|ON`)
- Tile / row / col: `E18` / 2 / 3
- Province: `ON`
- Centroid: 51.369386, -90.447149
- Allocated harvest: 44053.319318 m3
- Productive subcell area: 196383.006621 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2207454
- Blocks: 776500
- Forest area: 198670.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75401
- Scheduled area: 18885.78 ha
- Eligible blocks (age class >= 40): 754001
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.96 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 27.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
