# WS4 tiled 30-m dataset — H35|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H35|NL|S22` (parent `H35|NL`)
- Tile / row / col: `H35` / 2 / 2
- Province: `NL`
- Centroid: 47.515050, -55.544338
- Allocated harvest: 3491.344243 m3
- Productive subcell area: 47098.102259 ha
- Committed geometry area: 98334.023107 ha
- Clipped inventory geometry: 98334.023107 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 684369
- Blocks: 360551
- Forest area: 61593.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31134
- Scheduled area: 5546.07 ha
- Eligible blocks (age class >= 40): 311338
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.32 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 10.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
