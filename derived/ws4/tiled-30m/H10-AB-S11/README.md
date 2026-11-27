# WS4 tiled 30-m dataset — H10|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|AB|S11` (parent `H10|AB`)
- Tile / row / col: `H10` / 1 / 1
- Province: `AB`
- Centroid: 54.017979, -110.444955
- Allocated harvest: 87563.262521 m3
- Productive subcell area: 180109.097928 ha
- Committed geometry area: 249130.773960 ha
- Clipped inventory geometry: 249130.773960 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1772559
- Blocks: 566457
- Forest area: 159530.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48634
- Scheduled area: 13639.05 ha
- Eligible blocks (age class >= 40): 486339
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.80 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 21.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
