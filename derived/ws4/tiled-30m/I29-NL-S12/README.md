# WS4 tiled 30-m dataset — I29|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|NL|S12` (parent `I29|NL`)
- Tile / row / col: `I29` / 1 / 2
- Province: `NL`
- Centroid: 52.364878, -65.524769
- Allocated harvest: 7441.046487 m3
- Productive subcell area: 140662.470273 ha
- Committed geometry area: 249960.366377 ha
- Clipped inventory geometry: 249960.366377 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1899520
- Blocks: 837273
- Forest area: 170956.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78521
- Scheduled area: 16123.23 ha
- Eligible blocks (age class >= 40): 785205
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.85 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 25.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
