# WS4 tiled 30-m dataset — I6|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|AB|S11` (parent `I6|AB`)
- Tile / row / col: `I6` / 1 / 1
- Province: `AB`
- Centroid: 53.648808, -119.732975
- Allocated harvest: 58354.603014 m3
- Productive subcell area: 72002.784752 ha
- Committed geometry area: 83960.070464 ha
- Clipped inventory geometry: 83960.070464 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 538682
- Blocks: 272061
- Forest area: 48481.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25104
- Scheduled area: 3783.96 ha
- Eligible blocks (age class >= 40): 251036
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.06 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 8.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
