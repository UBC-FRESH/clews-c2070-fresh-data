# WS4 tiled 30-m dataset — I19|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I19|ON|S12` (parent `I19|ON`)
- Tile / row / col: `I19` / 1 / 2
- Province: `ON`
- Centroid: 56.270397, -88.192363
- Allocated harvest: 4727.371439 m3
- Productive subcell area: 90153.637091 ha
- Committed geometry area: 220171.485107 ha
- Clipped inventory geometry: 220171.485107 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 723461
- Blocks: 277539
- Forest area: 65111.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21745
- Scheduled area: 5554.26 ha
- Eligible blocks (age class >= 40): 217441
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.45 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 9.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
