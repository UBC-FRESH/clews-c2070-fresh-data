# WS4 tiled 30-m dataset — C29|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C29|QC|S21` (parent `C29|QC`)
- Tile / row / col: `C29` / 2 / 1
- Province: `QC`
- Centroid: 45.586265, -70.928209
- Allocated harvest: 125256.658753 m3
- Productive subcell area: 218205.020366 ha
- Committed geometry area: 215843.072780 ha
- Clipped inventory geometry: 215843.072780 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2102269
- Blocks: 645556
- Forest area: 189204.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57445
- Scheduled area: 16140.06 ha
- Eligible blocks (age class >= 40): 574449
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.00 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 24.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
