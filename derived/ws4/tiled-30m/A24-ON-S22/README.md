# WS4 tiled 30-m dataset — A24|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S22` (parent `A24|ON`)
- Tile / row / col: `A24` / 2 / 2
- Province: `ON`
- Centroid: 44.828076, -80.225042
- Allocated harvest: 905.061428 m3
- Productive subcell area: 3477.030371 ha
- Committed geometry area: 7246.846013 ha
- Clipped inventory geometry: 7246.846013 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 70679
- Blocks: 14279
- Forest area: 6361.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1327
- Scheduled area: 447.75 ha
- Eligible blocks (age class >= 40): 13267
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.90 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
