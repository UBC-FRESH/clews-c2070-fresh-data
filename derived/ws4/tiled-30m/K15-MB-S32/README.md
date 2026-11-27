# WS4 tiled 30-m dataset — K15|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K15|MB|S32` (parent `K15|MB`)
- Tile / row / col: `K15` / 3 / 2
- Province: `MB`
- Centroid: 59.951020, -98.443176
- Allocated harvest: 384.390375 m3
- Productive subcell area: 22356.254817 ha
- Committed geometry area: 53718.069681 ha
- Clipped inventory geometry: 53718.069681 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 50993
- Blocks: 32482
- Forest area: 4589.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1367
- Scheduled area: 198.45 ha
- Eligible blocks (age class >= 40): 13667
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.09 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
