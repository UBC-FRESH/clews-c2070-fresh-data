# WS4 tiled 30-m dataset — J28|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S12` (parent `J28|NL`)
- Tile / row / col: `J28` / 1 / 2
- Province: `NL`
- Centroid: 54.194264, -66.570999
- Allocated harvest: 5150.758083 m3
- Productive subcell area: 125830.737896 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1261261
- Blocks: 565211
- Forest area: 113513.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45434
- Scheduled area: 9458.01 ha
- Eligible blocks (age class >= 40): 454337
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.98 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 17.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
