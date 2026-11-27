# WS4 tiled 30-m dataset — C29|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C29|QC|S11` (parent `C29|QC`)
- Tile / row / col: `C29` / 1 / 1
- Province: `QC`
- Centroid: 45.311220, -71.189310
- Allocated harvest: 32449.911348 m3
- Productive subcell area: 56529.797593 ha
- Committed geometry area: 55917.894078 ha
- Clipped inventory geometry: 55917.894078 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 560073
- Blocks: 160521
- Forest area: 50406.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14504
- Scheduled area: 4341.51 ha
- Eligible blocks (age class >= 40): 145038
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.89 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 7.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
