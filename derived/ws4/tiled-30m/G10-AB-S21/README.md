# WS4 tiled 30-m dataset — G10|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|AB|S21` (parent `G10|AB`)
- Tile / row / col: `G10` / 2 / 1
- Province: `AB`
- Centroid: 53.124928, -110.229448
- Allocated harvest: 4007.612628 m3
- Productive subcell area: 8957.209733 ha
- Committed geometry area: 149935.033515 ha
- Clipped inventory geometry: 149935.033515 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 200862
- Blocks: 86320
- Forest area: 18077.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3691
- Scheduled area: 935.28 ha
- Eligible blocks (age class >= 40): 36907
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.21 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 3.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
