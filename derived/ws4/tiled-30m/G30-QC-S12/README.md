# WS4 tiled 30-m dataset — G30|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G30|QC|S12` (parent `G30|QC`)
- Tile / row / col: `G30` / 1 / 2
- Province: `QC`
- Centroid: 49.170701, -65.520296
- Allocated harvest: 27249.352174 m3
- Productive subcell area: 61418.482506 ha
- Committed geometry area: 70475.520378 ha
- Clipped inventory geometry: 70475.520378 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 698252
- Blocks: 255433
- Forest area: 62842.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21541
- Scheduled area: 4739.85 ha
- Eligible blocks (age class >= 40): 215402
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.09 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 9.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
