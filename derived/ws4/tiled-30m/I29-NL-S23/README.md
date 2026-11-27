# WS4 tiled 30-m dataset — I29|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|NL|S23` (parent `I29|NL`)
- Tile / row / col: `I29` / 2 / 3
- Province: `NL`
- Centroid: 52.561141, -64.543184
- Allocated harvest: 7091.451150 m3
- Productive subcell area: 134053.864382 ha
- Committed geometry area: 238216.725400 ha
- Clipped inventory geometry: 238216.725400 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1164885
- Blocks: 382443
- Forest area: 104839.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33853
- Scheduled area: 9928.44 ha
- Eligible blocks (age class >= 40): 338530
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.79 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 14.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
