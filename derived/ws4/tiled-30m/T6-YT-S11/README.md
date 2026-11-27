# WS4 tiled 30-m dataset — T6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T6|YT|S11` (parent `T6|YT`)
- Tile / row / col: `T6` / 1 / 1
- Province: `YT`
- Centroid: 66.877432, -134.978022
- Allocated harvest: 115.561854 m3
- Productive subcell area: 60752.698611 ha
- Committed geometry area: 146156.936462 ha
- Clipped inventory geometry: 146156.936462 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1210755
- Blocks: 376957
- Forest area: 108967.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30869
- Scheduled area: 7150.68 ha
- Eligible blocks (age class >= 40): 308685
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.08 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 14.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
