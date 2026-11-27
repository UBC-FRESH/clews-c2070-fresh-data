# WS4 tiled 30-m dataset — B23|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B23|ON|S12` (parent `B23|ON`)
- Tile / row / col: `B23` / 1 / 2
- Province: `ON`
- Centroid: 46.149585, -81.959078
- Allocated harvest: 40778.858110 m3
- Productive subcell area: 134918.934911 ha
- Committed geometry area: 159724.782398 ha
- Clipped inventory geometry: 159724.782398 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1356491
- Blocks: 550702
- Forest area: 122084.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50881
- Scheduled area: 11525.85 ha
- Eligible blocks (age class >= 40): 508804
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.09 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 18.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
