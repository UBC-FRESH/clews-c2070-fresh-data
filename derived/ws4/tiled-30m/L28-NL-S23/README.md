# WS4 tiled 30-m dataset — L28|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|NL|S23` (parent `L28|NL`)
- Tile / row / col: `L28` / 2 / 3
- Province: `NL`
- Centroid: 56.842560, -63.276200
- Allocated harvest: 1359.386126 m3
- Productive subcell area: 26934.572360 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 103622
- Blocks: 49308
- Forest area: 9325.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3205
- Scheduled area: 641.52 ha
- Eligible blocks (age class >= 40): 32050
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.87 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
