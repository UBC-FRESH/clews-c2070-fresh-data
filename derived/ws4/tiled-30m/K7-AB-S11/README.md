# WS4 tiled 30-m dataset — K7|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|AB|S11` (parent `K7|AB`)
- Tile / row / col: `K7` / 1 / 1
- Province: `AB`
- Centroid: 56.667265, -119.556884
- Allocated harvest: 133034.727410 m3
- Productive subcell area: 228948.114231 ha
- Committed geometry area: 243294.843160 ha
- Clipped inventory geometry: 243294.843160 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2512407
- Blocks: 913400
- Forest area: 226116.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83249
- Scheduled area: 17317.17 ha
- Eligible blocks (age class >= 40): 832481
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.18 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 31.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
