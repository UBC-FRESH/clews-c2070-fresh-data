# WS4 tiled 30-m dataset — B27|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|ON|S11` (parent `B27|ON`)
- Tile / row / col: `B27` / 1 / 1
- Province: `ON`
- Centroid: 44.894012, -75.392820
- Allocated harvest: 5782.572662 m3
- Productive subcell area: 17422.318732 ha
- Committed geometry area: 102171.618151 ha
- Clipped inventory geometry: 102171.618151 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 521070
- Blocks: 167738
- Forest area: 46896.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12431
- Scheduled area: 3663.72 ha
- Eligible blocks (age class >= 40): 124310
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.69 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
