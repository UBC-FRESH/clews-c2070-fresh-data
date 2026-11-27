# WS4 tiled 30-m dataset — F6|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F6|BC|S13` (parent `F6|BC`)
- Tile / row / col: `F6` / 1 / 3
- Province: `BC`
- Centroid: 50.108941, -116.251960
- Allocated harvest: 138342.879396 m3
- Productive subcell area: 175902.532281 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1828194
- Blocks: 947356
- Forest area: 164537.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86352
- Scheduled area: 13719.96 ha
- Eligible blocks (age class >= 40): 863511
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.00 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 27.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
