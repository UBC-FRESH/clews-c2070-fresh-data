# WS4 tiled 30-m dataset — I34|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S33` (parent `I34|NL`)
- Tile / row / col: `I34` / 3 / 3
- Province: `NL`
- Centroid: 49.260474, -54.771286
- Allocated harvest: 7839.166977 m3
- Productive subcell area: 101787.093208 ha
- Committed geometry area: 142372.258555 ha
- Clipped inventory geometry: 142372.258555 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1338913
- Blocks: 629243
- Forest area: 120502.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57650
- Scheduled area: 10300.05 ha
- Eligible blocks (age class >= 40): 576493
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.73 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 19.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
