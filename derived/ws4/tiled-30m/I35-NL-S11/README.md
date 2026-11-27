# WS4 tiled 30-m dataset — I35|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S11` (parent `I35|NL`)
- Tile / row / col: `I35` / 1 / 1
- Province: `NL`
- Centroid: 48.375766, -55.241536
- Allocated harvest: 12415.941377 m3
- Productive subcell area: 162761.178521 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1602108
- Blocks: 838680
- Forest area: 144189.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74168
- Scheduled area: 12143.34 ha
- Eligible blocks (age class >= 40): 741674
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.06 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 23.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
