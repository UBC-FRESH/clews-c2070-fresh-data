# WS4 tiled 30-m dataset — G33|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G33|NL|S32` (parent `G33|NL`)
- Tile / row / col: `G33` / 3 / 2
- Province: `NL`
- Centroid: 47.919753, -59.357637
- Allocated harvest: 116.515309 m3
- Productive subcell area: 1971.534105 ha
- Committed geometry area: 3200.502638 ha
- Clipped inventory geometry: 3200.502638 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 30543
- Blocks: 10440
- Forest area: 2748.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 914
- Scheduled area: 190.44 ha
- Eligible blocks (age class >= 40): 9135
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.52 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
