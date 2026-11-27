# WS4 tiled 30-m dataset — I34|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I34|NL|S32` (parent `I34|NL`)
- Tile / row / col: `I34` / 3 / 2
- Province: `NL`
- Centroid: 49.595005, -55.685907
- Allocated harvest: 3332.166793 m3
- Productive subcell area: 43266.277262 ha
- Committed geometry area: 60517.668979 ha
- Clipped inventory geometry: 60517.668979 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 591040
- Blocks: 309977
- Forest area: 53193.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29419
- Scheduled area: 5022.45 ha
- Eligible blocks (age class >= 40): 294181
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.10 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 9.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
