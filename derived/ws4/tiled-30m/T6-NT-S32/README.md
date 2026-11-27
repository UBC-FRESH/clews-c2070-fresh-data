# WS4 tiled 30-m dataset — T6|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T6|NT|S32` (parent `T6|NT`)
- Tile / row / col: `T6` / 3 / 2
- Province: `NT`
- Centroid: 67.986798, -135.448834
- Allocated harvest: 164.402728 m3
- Productive subcell area: 143396.174523 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 898612
- Blocks: 475106
- Forest area: 80875.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40982
- Scheduled area: 7088.49 ha
- Eligible blocks (age class >= 40): 409818
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.24 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 13.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
