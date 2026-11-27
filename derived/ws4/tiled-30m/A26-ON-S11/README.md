# WS4 tiled 30-m dataset — A26|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S11` (parent `A26|ON`)
- Tile / row / col: `A26` / 1 / 1
- Province: `ON`
- Centroid: 44.049308, -77.523522
- Allocated harvest: 11653.989933 m3
- Productive subcell area: 46408.785285 ha
- Committed geometry area: 85641.598024 ha
- Clipped inventory geometry: 85641.598024 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 379828
- Blocks: 154046
- Forest area: 34184.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11608
- Scheduled area: 2618.10 ha
- Eligible blocks (age class >= 40): 116073
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.61 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
