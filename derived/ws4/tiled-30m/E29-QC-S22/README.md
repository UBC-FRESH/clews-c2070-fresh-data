# WS4 tiled 30-m dataset — E29|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S22` (parent `E29|QC`)
- Tile / row / col: `E29` / 2 / 2
- Province: `QC`
- Centroid: 47.866918, -68.797312
- Allocated harvest: 119827.235233 m3
- Productive subcell area: 206038.231969 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2357201
- Blocks: 797502
- Forest area: 212148.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70121
- Scheduled area: 17604.45 ha
- Eligible blocks (age class >= 40): 701204
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.33 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 29.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
