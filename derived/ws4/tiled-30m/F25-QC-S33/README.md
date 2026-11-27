# WS4 tiled 30-m dataset — F25|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F25|QC|S33` (parent `F25|QC`)
- Tile / row / col: `F25` / 3 / 3
- Province: `QC`
- Centroid: 51.317946, -74.938390
- Allocated harvest: 29746.222024 m3
- Productive subcell area: 159257.145725 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1402301
- Blocks: 434818
- Forest area: 126207.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26996
- Scheduled area: 6143.94 ha
- Eligible blocks (age class >= 40): 269955
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.89 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 16.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
