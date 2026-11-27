# WS4 tiled 30-m dataset — H10|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|AB|S22` (parent `H10|AB`)
- Tile / row / col: `H10` / 2 / 2
- Province: `AB`
- Centroid: 54.562012, -110.134331
- Allocated harvest: 28160.667502 m3
- Productive subcell area: 57923.748782 ha
- Committed geometry area: 80121.373827 ha
- Clipped inventory geometry: 80121.373827 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 484491
- Blocks: 199364
- Forest area: 43604.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18381
- Scheduled area: 3767.22 ha
- Eligible blocks (age class >= 40): 183807
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.88 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 7.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
