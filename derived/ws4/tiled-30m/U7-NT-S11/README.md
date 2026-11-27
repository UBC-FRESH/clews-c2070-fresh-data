# WS4 tiled 30-m dataset — U7|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S11` (parent `U7|NT`)
- Tile / row / col: `U7` / 1 / 1
- Province: `NT`
- Centroid: 68.901506, -134.162089
- Allocated harvest: 14.425659 m3
- Productive subcell area: 12332.669462 ha
- Committed geometry area: 246149.661436 ha
- Clipped inventory geometry: 246149.661436 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 391220
- Blocks: 230828
- Forest area: 35209.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17053
- Scheduled area: 2488.23 ha
- Eligible blocks (age class >= 40): 170529
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.63 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 6.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
