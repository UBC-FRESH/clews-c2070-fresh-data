# WS4 tiled 30-m dataset — T8|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T8|NT|S33` (parent `T8|NT`)
- Tile / row / col: `T8` / 3 / 3
- Province: `NT`
- Centroid: 69.747323, -127.936460
- Allocated harvest: 5.213382 m3
- Productive subcell area: 11533.067302 ha
- Committed geometry area: 244764.478224 ha
- Clipped inventory geometry: 244764.478224 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 250950
- Blocks: 153188
- Forest area: 22585.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3276
- Scheduled area: 365.22 ha
- Eligible blocks (age class >= 40): 32757
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.57 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 4.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
