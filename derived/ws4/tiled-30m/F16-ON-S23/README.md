# WS4 tiled 30-m dataset — F16|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|ON|S23` (parent `F16|ON`)
- Tile / row / col: `F16` / 2 / 3
- Province: `ON`
- Centroid: 52.813534, -94.749499
- Allocated harvest: 24403.341120 m3
- Productive subcell area: 170286.827950 ha
- Committed geometry area: 217422.224656 ha
- Clipped inventory geometry: 217422.224656 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1777962
- Blocks: 456544
- Forest area: 160016.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34237
- Scheduled area: 11623.59 ha
- Eligible blocks (age class >= 40): 342363
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.53 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 18.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
