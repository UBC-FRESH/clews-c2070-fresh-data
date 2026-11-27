# WS4 tiled 30-m dataset — J33|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S13` (parent `J33|NL`)
- Tile / row / col: `J33` / 1 / 3
- Province: `NL`
- Centroid: 50.577179, -56.442236
- Allocated harvest: 4025.082888 m3
- Productive subcell area: 85032.428964 ha
- Committed geometry area: 128142.421183 ha
- Clipped inventory geometry: 128142.421183 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1129202
- Blocks: 587937
- Forest area: 101628.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57020
- Scheduled area: 9870.57 ha
- Eligible blocks (age class >= 40): 570200
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.44 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 17.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
