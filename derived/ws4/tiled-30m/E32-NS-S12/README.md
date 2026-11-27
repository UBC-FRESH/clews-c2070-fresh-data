# WS4 tiled 30-m dataset — E32|NS|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|NS|S12` (parent `E32|NS`)
- Tile / row / col: `E32` / 1 / 2
- Province: `NS`
- Centroid: 45.702733, -63.828484
- Allocated harvest: 88905.016729 m3
- Productive subcell area: 189607.439234 ha
- Committed geometry area: 234339.240672 ha
- Clipped inventory geometry: 234339.240672 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2133811
- Blocks: 634309
- Forest area: 192042.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48468
- Scheduled area: 11448.45 ha
- Eligible blocks (age class >= 40): 484677
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.98 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 24.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
