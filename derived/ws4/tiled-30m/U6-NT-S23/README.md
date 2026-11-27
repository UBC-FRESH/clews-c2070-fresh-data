# WS4 tiled 30-m dataset — U6|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|NT|S23` (parent `U6|NT`)
- Tile / row / col: `U6` / 2 / 3
- Province: `NT`
- Centroid: 69.090058, -135.585306
- Allocated harvest: 37.993952 m3
- Productive subcell area: 32056.419383 ha
- Committed geometry area: 138070.504289 ha
- Clipped inventory geometry: 138070.504289 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 275317
- Blocks: 159931
- Forest area: 24778.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7322
- Scheduled area: 886.59 ha
- Eligible blocks (age class >= 40): 73211
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.93 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 5.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
