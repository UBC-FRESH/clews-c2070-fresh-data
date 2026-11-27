# WS4 tiled 30-m dataset — G24|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G24|QC|S12` (parent `G24|QC`)
- Tile / row / col: `G24` / 1 / 2
- Province: `QC`
- Centroid: 52.280337, -77.527327
- Allocated harvest: 29918.867829 m3
- Productive subcell area: 144998.215027 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 936457
- Blocks: 314287
- Forest area: 84281.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16418
- Scheduled area: 3129.03 ha
- Eligible blocks (age class >= 40): 164171
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.95 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 11.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
