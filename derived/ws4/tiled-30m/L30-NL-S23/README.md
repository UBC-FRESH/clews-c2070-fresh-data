# WS4 tiled 30-m dataset — L30|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L30|NL|S23` (parent `L30|NL`)
- Tile / row / col: `L30` / 2 / 3
- Province: `NL`
- Centroid: 55.299428, -59.339415
- Allocated harvest: 46.827765 m3
- Productive subcell area: 685.077812 ha
- Committed geometry area: 1411.541280 ha
- Clipped inventory geometry: 1411.541280 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1529
- Blocks: 1012
- Forest area: 137.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 336
- Scheduled area: 39.06 ha
- Eligible blocks (age class >= 40): 336
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.10 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
