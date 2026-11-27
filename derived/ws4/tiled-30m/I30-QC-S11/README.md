# WS4 tiled 30-m dataset — I30|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|QC|S11` (parent `I30|QC`)
- Tile / row / col: `I30` / 1 / 1
- Province: `QC`
- Centroid: 51.924244, -64.086031
- Allocated harvest: 25759.136513 m3
- Productive subcell area: 114103.015341 ha
- Committed geometry area: 149057.850642 ha
- Clipped inventory geometry: 149057.850642 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1019607
- Blocks: 420712
- Forest area: 91764.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36937
- Scheduled area: 7761.96 ha
- Eligible blocks (age class >= 40): 369362
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.09 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 13.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
