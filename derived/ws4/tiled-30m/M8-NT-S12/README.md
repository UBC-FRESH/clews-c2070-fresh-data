# WS4 tiled 30-m dataset — M8|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|NT|S12` (parent `M8|NT`)
- Tile / row / col: `M8` / 1 / 2
- Province: `NT`
- Centroid: 60.075219, -118.259108
- Allocated harvest: 47.226143 m3
- Productive subcell area: 33956.923223 ha
- Committed geometry area: 76539.572687 ha
- Clipped inventory geometry: 76539.572687 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 249739
- Blocks: 96384
- Forest area: 22476.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6315
- Scheduled area: 1343.07 ha
- Eligible blocks (age class >= 40): 63145
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.78 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
