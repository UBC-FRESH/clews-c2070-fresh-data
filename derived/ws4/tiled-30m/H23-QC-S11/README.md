# WS4 tiled 30-m dataset — H23|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S11` (parent `H23|QC`)
- Tile / row / col: `H23` / 1 / 1
- Province: `QC`
- Centroid: 54.171811, -79.481977
- Allocated harvest: 89.306908 m3
- Productive subcell area: 485.501523 ha
- Committed geometry area: 934.209491 ha
- Clipped inventory geometry: 934.209491 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 446
- Blocks: 411
- Forest area: 40.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 174
- Scheduled area: 16.29 ha
- Eligible blocks (age class >= 40): 174
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
