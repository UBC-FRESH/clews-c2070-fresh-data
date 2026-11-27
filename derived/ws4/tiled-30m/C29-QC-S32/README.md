# WS4 tiled 30-m dataset — C29|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C29|QC|S32` (parent `C29|QC`)
- Tile / row / col: `C29` / 3 / 2
- Province: `QC`
- Centroid: 45.858621, -70.348918
- Allocated harvest: 8384.162091 m3
- Productive subcell area: 14605.740549 ha
- Committed geometry area: 14447.641558 ha
- Clipped inventory geometry: 14447.641558 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 143127
- Blocks: 45937
- Forest area: 12881.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4173
- Scheduled area: 1112.04 ha
- Eligible blocks (age class >= 40): 41730
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.12 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
