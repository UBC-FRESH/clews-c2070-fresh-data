# WS4 tiled 30-m dataset — G6|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G6|AB|S23` (parent `G6|AB`)
- Tile / row / col: `G6` / 2 / 3
- Province: `AB`
- Centroid: 51.919606, -116.989189
- Allocated harvest: 16725.146386 m3
- Productive subcell area: 18192.966351 ha
- Committed geometry area: 55595.928402 ha
- Clipped inventory geometry: 55595.928402 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 155114
- Blocks: 83802
- Forest area: 13960.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7671
- Scheduled area: 1198.89 ha
- Eligible blocks (age class >= 40): 76709
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.91 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
