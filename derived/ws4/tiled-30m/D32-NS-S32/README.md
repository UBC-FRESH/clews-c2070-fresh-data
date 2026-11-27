# WS4 tiled 30-m dataset — D32|NS|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S32` (parent `D32|NS`)
- Tile / row / col: `D32` / 3 / 2
- Province: `NS`
- Centroid: 45.455856, -64.220533
- Allocated harvest: 68579.566702 m3
- Productive subcell area: 118593.462061 ha
- Committed geometry area: 145632.223782 ha
- Clipped inventory geometry: 145632.223782 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1368612
- Blocks: 393526
- Forest area: 123175.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30545
- Scheduled area: 7406.73 ha
- Eligible blocks (age class >= 40): 305443
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.82 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 16.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
