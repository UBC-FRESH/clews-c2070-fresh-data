# WS4 tiled 30-m dataset — J34|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J34|NL|S12` (parent `J34|NL`)
- Tile / row / col: `J34` / 1 / 2
- Province: `NL`
- Centroid: 49.954077, -55.547095
- Allocated harvest: 326.083569 m3
- Productive subcell area: 5605.847585 ha
- Committed geometry area: 7037.692651 ha
- Clipped inventory geometry: 7037.692651 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 60428
- Blocks: 37808
- Forest area: 5438.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3527
- Scheduled area: 516.15 ha
- Eligible blocks (age class >= 40): 35268
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.29 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
