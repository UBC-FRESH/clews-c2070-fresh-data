# WS4 tiled 30-m dataset — A26|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S12` (parent `A26|ON`)
- Tile / row / col: `A26` / 1 / 2
- Province: `ON`
- Centroid: 43.953622, -77.106158
- Allocated harvest: 5346.411845 m3
- Productive subcell area: 21290.603543 ha
- Committed geometry area: 39289.141036 ha
- Clipped inventory geometry: 39289.141036 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 202904
- Blocks: 75221
- Forest area: 18261.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5589
- Scheduled area: 1323.27 ha
- Eligible blocks (age class >= 40): 55885
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.05 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
