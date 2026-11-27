# WS4 tiled 30-m dataset — T4|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S11` (parent `T4|YT`)
- Tile / row / col: `T4` / 1 / 1
- Province: `YT`
- Centroid: 65.242923, -140.346511
- Allocated harvest: 166.577051 m3
- Productive subcell area: 131524.310888 ha
- Committed geometry area: 246672.331465 ha
- Clipped inventory geometry: 246672.331465 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1174395
- Blocks: 552216
- Forest area: 105695.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39145
- Scheduled area: 7443.45 ha
- Eligible blocks (age class >= 40): 391444
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.36 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 16.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
