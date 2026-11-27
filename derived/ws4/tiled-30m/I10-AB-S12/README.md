# WS4 tiled 30-m dataset — I10|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|AB|S12` (parent `I10|AB`)
- Tile / row / col: `I10` / 1 / 2
- Province: `AB`
- Centroid: 55.460566, -110.319651
- Allocated harvest: 66870.848761 m3
- Productive subcell area: 180211.056995 ha
- Committed geometry area: 202131.196941 ha
- Clipped inventory geometry: 202131.196941 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1831539
- Blocks: 449195
- Forest area: 164838.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41684
- Scheduled area: 18971.82 ha
- Eligible blocks (age class >= 40): 416837
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.84 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 19.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
