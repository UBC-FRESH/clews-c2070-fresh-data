# WS4 tiled 30-m dataset — J27|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|NL|S23` (parent `J27|NL`)
- Tile / row / col: `J27` / 2 / 3
- Province: `NL`
- Centroid: 55.009472, -67.338314
- Allocated harvest: 352.592578 m3
- Productive subcell area: 9998.985440 ha
- Committed geometry area: 19403.263339 ha
- Clipped inventory geometry: 19403.263339 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 103091
- Blocks: 64762
- Forest area: 9278.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5552
- Scheduled area: 736.83 ha
- Eligible blocks (age class >= 40): 55515
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.13 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
