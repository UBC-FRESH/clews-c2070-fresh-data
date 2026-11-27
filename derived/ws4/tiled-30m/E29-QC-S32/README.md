# WS4 tiled 30-m dataset — E29|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S32` (parent `E29|QC`)
- Tile / row / col: `E29` / 3 / 2
- Province: `QC`
- Centroid: 48.250143, -68.507628
- Allocated harvest: 104666.607792 m3
- Productive subcell area: 179970.127607 ha
- Committed geometry area: 218369.821328 ha
- Clipped inventory geometry: 218369.821328 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1956176
- Blocks: 711287
- Forest area: 176055.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61564
- Scheduled area: 14254.83 ha
- Eligible blocks (age class >= 40): 615633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.96 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 24.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
