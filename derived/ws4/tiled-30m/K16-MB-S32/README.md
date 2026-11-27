# WS4 tiled 30-m dataset — K16|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K16|MB|S32` (parent `K16|MB`)
- Tile / row / col: `K16` / 3 / 2
- Province: `MB`
- Centroid: 59.973280, -95.668445
- Allocated harvest: 91.370719 m3
- Productive subcell area: 4940.508694 ha
- Committed geometry area: 29377.767955 ha
- Clipped inventory geometry: 29377.767955 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1683
- Blocks: 1309
- Forest area: 151.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 483
- Scheduled area: 54.81 ha
- Eligible blocks (age class >= 40): 483
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.11 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
