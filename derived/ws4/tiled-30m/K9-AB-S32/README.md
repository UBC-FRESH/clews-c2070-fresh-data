# WS4 tiled 30-m dataset — K9|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K9|AB|S32` (parent `K9|AB`)
- Tile / row / col: `K9` / 3 / 2
- Province: `AB`
- Centroid: 58.630675, -114.499367
- Allocated harvest: 136547.554935 m3
- Productive subcell area: 212379.340034 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2172102
- Blocks: 861031
- Forest area: 195489.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69672
- Scheduled area: 12102.57 ha
- Eligible blocks (age class >= 40): 696713
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.87 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 27.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
