# WS4 tiled 30-m dataset — J34|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J34|NL|S11` (parent `J34|NL`)
- Tile / row / col: `J34` / 1 / 1
- Province: `NL`
- Centroid: 50.211484, -55.742825
- Allocated harvest: 147.091780 m3
- Productive subcell area: 2528.720168 ha
- Committed geometry area: 3174.605637 ha
- Clipped inventory geometry: 3174.605637 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 28871
- Blocks: 17962
- Forest area: 2598.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1674
- Scheduled area: 242.46 ha
- Eligible blocks (age class >= 40): 16739
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.64 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
