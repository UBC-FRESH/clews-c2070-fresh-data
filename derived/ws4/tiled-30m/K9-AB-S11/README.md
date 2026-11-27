# WS4 tiled 30-m dataset — K9|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K9|AB|S11` (parent `K9|AB`)
- Tile / row / col: `K9` / 1 / 1
- Province: `AB`
- Centroid: 57.613104, -114.799331
- Allocated harvest: 136547.554935 m3
- Productive subcell area: 212379.340034 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2450541
- Blocks: 763837
- Forest area: 220548.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62997
- Scheduled area: 14087.52 ha
- Eligible blocks (age class >= 40): 629968
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.49 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 28.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
