# WS4 tiled 30-m dataset — I1|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I1|BC|S13` (parent `I1|BC`)
- Tile / row / col: `I1` / 1 / 3
- Province: `BC`
- Centroid: 50.801050, -128.606826
- Allocated harvest: 2024.707505 m3
- Productive subcell area: 1720.918529 ha
- Committed geometry area: 1946.749283 ha
- Clipped inventory geometry: 1946.749283 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 20726
- Blocks: 13427
- Forest area: 1865.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1335
- Scheduled area: 180.00 ha
- Eligible blocks (age class >= 40): 13349
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.48 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
