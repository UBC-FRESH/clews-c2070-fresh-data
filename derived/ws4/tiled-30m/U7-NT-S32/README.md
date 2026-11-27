# WS4 tiled 30-m dataset — U7|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S32` (parent `U7|NT`)
- Tile / row / col: `U7` / 3 / 2
- Province: `NT`
- Centroid: 69.710225, -134.435899
- Allocated harvest: 0.147031 m3
- Productive subcell area: 125.698410 ha
- Committed geometry area: 2508.834051 ha
- Clipped inventory geometry: 2508.834051 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 286
- Blocks: 261
- Forest area: 25.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58
- Scheduled area: 5.58 ha
- Eligible blocks (age class >= 40): 58
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
