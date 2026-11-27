# WS4 tiled 30-m dataset — I35|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S23` (parent `I35|NL`)
- Tile / row / col: `I35` / 2 / 3
- Province: `NL`
- Centroid: 48.217899, -53.809333
- Allocated harvest: 9286.181852 m3
- Productive subcell area: 121733.008895 ha
- Committed geometry area: 186981.026435 ha
- Clipped inventory geometry: 186981.026435 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1664456
- Blocks: 777577
- Forest area: 149801.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71786
- Scheduled area: 13373.82 ha
- Eligible blocks (age class >= 40): 717858
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.84 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 23.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
