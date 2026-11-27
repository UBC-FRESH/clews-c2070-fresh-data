# WS4 tiled 30-m dataset — B25|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|ON|S22` (parent `B25|ON`)
- Tile / row / col: `B25` / 2 / 2
- Province: `ON`
- Centroid: 45.855218, -78.105518
- Allocated harvest: 95678.107504 m3
- Productive subcell area: 331720.889573 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2459478
- Blocks: 960579
- Forest area: 221353.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 91916
- Scheduled area: 21665.70 ha
- Eligible blocks (age class >= 40): 919160
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.42 MB
- Schedules: 1.09 MB
- Runs: 0.00 MB
- Total: 32.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
