# WS4 tiled 30-m dataset — A26|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S23` (parent `A26|ON`)
- Tile / row / col: `A26` / 2 / 3
- Province: `ON`
- Centroid: 44.282919, -76.406118
- Allocated harvest: 4645.232057 m3
- Productive subcell area: 18498.349354 ha
- Committed geometry area: 34136.385811 ha
- Clipped inventory geometry: 34136.385811 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 109657
- Blocks: 48488
- Forest area: 9869.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3534
- Scheduled area: 717.75 ha
- Eligible blocks (age class >= 40): 35332
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.89 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
