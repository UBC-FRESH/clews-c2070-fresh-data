# WS4 tiled 30-m dataset — K32|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K32|NL|S21` (parent `K32|NL`)
- Tile / row / col: `K32` / 2 / 1
- Province: `NL`
- Centroid: 53.298202, -57.679199
- Allocated harvest: 10938.847905 m3
- Productive subcell area: 199423.734393 ha
- Committed geometry area: 249625.423832 ha
- Clipped inventory geometry: 249625.423832 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2351371
- Blocks: 728772
- Forest area: 211623.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69057
- Scheduled area: 19405.62 ha
- Eligible blocks (age class >= 40): 690567
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.08 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 27.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
