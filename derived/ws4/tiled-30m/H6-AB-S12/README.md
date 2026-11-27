# WS4 tiled 30-m dataset — H6|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|AB|S12` (parent `H6|AB`)
- Tile / row / col: `H6` / 1 / 2
- Province: `AB`
- Centroid: 52.583023, -118.190331
- Allocated harvest: 27673.715255 m3
- Productive subcell area: 34502.756703 ha
- Committed geometry area: 59833.785008 ha
- Clipped inventory geometry: 59833.785008 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 231030
- Blocks: 141993
- Forest area: 20792.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13233
- Scheduled area: 1893.06 ha
- Eligible blocks (age class >= 40): 132325
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.49 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 4.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
