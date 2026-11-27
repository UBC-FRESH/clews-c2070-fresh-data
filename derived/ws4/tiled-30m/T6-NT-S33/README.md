# WS4 tiled 30-m dataset — T6|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T6|NT|S33` (parent `T6|NT`)
- Tile / row / col: `T6` / 3 / 3
- Province: `NT`
- Centroid: 68.257856, -134.448025
- Allocated harvest: 164.402728 m3
- Productive subcell area: 143396.174523 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1381004
- Blocks: 683217
- Forest area: 124290.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62416
- Scheduled area: 11798.28 ha
- Eligible blocks (age class >= 40): 624154
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.65 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 20.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
