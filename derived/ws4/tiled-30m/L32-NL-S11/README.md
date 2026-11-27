# WS4 tiled 30-m dataset — L32|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L32|NL|S11` (parent `L32|NL`)
- Tile / row / col: `L32` / 1 / 1
- Province: `NL`
- Centroid: 54.000690, -57.302062
- Allocated harvest: 179.711904 m3
- Productive subcell area: 3206.463382 ha
- Committed geometry area: 6153.384172 ha
- Clipped inventory geometry: 6153.384172 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 44463
- Blocks: 19840
- Forest area: 4001.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1653
- Scheduled area: 330.66 ha
- Eligible blocks (age class >= 40): 16524
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.82 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
