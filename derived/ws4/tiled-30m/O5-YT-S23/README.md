# WS4 tiled 30-m dataset — O5|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|YT|S23` (parent `O5|YT`)
- Tile / row / col: `O5` / 2 / 3
- Province: `YT`
- Centroid: 61.267932, -127.852487
- Allocated harvest: 258.460816 m3
- Productive subcell area: 172761.565157 ha
- Committed geometry area: 249925.117811 ha
- Clipped inventory geometry: 249925.117811 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1339179
- Blocks: 613070
- Forest area: 120526.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52542
- Scheduled area: 10375.47 ha
- Eligible blocks (age class >= 40): 525415
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.55 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 19.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
