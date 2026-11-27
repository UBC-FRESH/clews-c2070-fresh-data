# WS4 tiled 30-m dataset — U6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|YT|S11` (parent `U6|YT`)
- Tile / row / col: `U6` / 1 / 1
- Province: `YT`
- Centroid: 68.075674, -137.187383
- Allocated harvest: 39.188127 m3
- Productive subcell area: 21137.734691 ha
- Committed geometry area: 246095.250480 ha
- Clipped inventory geometry: 246095.250480 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 83067
- Blocks: 55354
- Forest area: 7476.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1943
- Scheduled area: 252.63 ha
- Eligible blocks (age class >= 40): 19426
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.77 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
