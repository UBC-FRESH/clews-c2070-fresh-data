# WS4 tiled 30-m dataset — C24|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|ON|S22` (parent `C24|ON`)
- Tile / row / col: `C24` / 2 / 2
- Province: `ON`
- Centroid: 47.490453, -79.671508
- Allocated harvest: 26193.229187 m3
- Productive subcell area: 92740.084046 ha
- Committed geometry area: 113134.286135 ha
- Clipped inventory geometry: 113134.286135 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 712297
- Blocks: 266746
- Forest area: 64106.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23302
- Scheduled area: 5372.64 ha
- Eligible blocks (age class >= 40): 233018
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.42 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 9.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
