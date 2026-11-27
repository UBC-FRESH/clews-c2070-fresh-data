# WS4 tiled 30-m dataset — E23|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E23|ON|S11` (parent `E23|ON`)
- Tile / row / col: `E23` / 1 / 1
- Province: `ON`
- Centroid: 50.080862, -81.371659
- Allocated harvest: 24738.224058 m3
- Productive subcell area: 207196.269649 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2632774
- Blocks: 873312
- Forest area: 236949.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81027
- Scheduled area: 21077.28 ha
- Eligible blocks (age class >= 40): 810269
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.10 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 32.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
