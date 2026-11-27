# WS4 tiled 30-m dataset — G24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G24|QC|S33` (parent `G24|QC`)
- Tile / row / col: `G24` / 3 / 3
- Province: `QC`
- Centroid: 53.026721, -76.390187
- Allocated harvest: 29918.867829 m3
- Productive subcell area: 144998.215027 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1598896
- Blocks: 410035
- Forest area: 143900.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25289
- Scheduled area: 3947.94 ha
- Eligible blocks (age class >= 40): 252883
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.41 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 16.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
