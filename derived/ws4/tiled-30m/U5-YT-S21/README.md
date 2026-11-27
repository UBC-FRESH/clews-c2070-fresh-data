# WS4 tiled 30-m dataset — U5|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U5|YT|S21` (parent `U5|YT`)
- Tile / row / col: `U5` / 2 / 1
- Province: `YT`
- Centroid: 67.547442, -140.618398
- Allocated harvest: 104.107522 m3
- Productive subcell area: 60286.373308 ha
- Committed geometry area: 184320.620302 ha
- Clipped inventory geometry: 184320.620302 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 898334
- Blocks: 225729
- Forest area: 80850.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13555
- Scheduled area: 4412.16 ha
- Eligible blocks (age class >= 40): 135543
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.84 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 10.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
