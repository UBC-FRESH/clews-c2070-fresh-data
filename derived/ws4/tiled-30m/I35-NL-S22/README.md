# WS4 tiled 30-m dataset — I35|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S22` (parent `I35|NL`)
- Tile / row / col: `I35` / 2 / 2
- Province: `NL`
- Centroid: 48.473774, -54.307978
- Allocated harvest: 12033.986981 m3
- Productive subcell area: 157754.119791 ha
- Committed geometry area: 242309.193791 ha
- Clipped inventory geometry: 242309.193791 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1833400
- Blocks: 892328
- Forest area: 165006.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80712
- Scheduled area: 14422.86 ha
- Eligible blocks (age class >= 40): 807120
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.53 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 26.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
