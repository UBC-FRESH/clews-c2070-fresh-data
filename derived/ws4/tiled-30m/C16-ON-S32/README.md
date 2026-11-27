# WS4 tiled 30-m dataset — C16|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C16|ON|S32` (parent `C16|ON`)
- Tile / row / col: `C16` / 3 / 2
- Province: `ON`
- Centroid: 49.410765, -95.151980
- Allocated harvest: 18.139441 m3
- Productive subcell area: 86.483764 ha
- Committed geometry area: 109.935516 ha
- Clipped inventory geometry: 109.935516 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 897
- Blocks: 501
- Forest area: 80.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 445
- Scheduled area: 73.62 ha
- Eligible blocks (age class >= 40): 445
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
