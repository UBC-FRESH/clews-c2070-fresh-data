# WS4 tiled 30-m dataset — J28|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S32` (parent `J28|NL`)
- Tile / row / col: `J28` / 3 / 2
- Province: `NL`
- Centroid: 54.880174, -66.066246
- Allocated harvest: 1172.821413 m3
- Productive subcell area: 28651.507503 ha
- Committed geometry area: 56924.698969 ha
- Clipped inventory geometry: 56924.698969 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 414129
- Blocks: 258406
- Forest area: 37271.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25017
- Scheduled area: 3594.87 ha
- Eligible blocks (age class >= 40): 250166
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.03 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 7.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
