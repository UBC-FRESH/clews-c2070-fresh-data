# WS4 tiled 30-m dataset — E13|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|MB|S13` (parent `E13|MB`)
- Tile / row / col: `E13` / 1 / 3
- Province: `MB`
- Centroid: 50.824699, -101.197848
- Allocated harvest: 6704.808510 m3
- Productive subcell area: 136264.313483 ha
- Committed geometry area: 221897.898178 ha
- Clipped inventory geometry: 221897.898178 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 487658
- Blocks: 143375
- Forest area: 43889.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10200
- Scheduled area: 3080.97 ha
- Eligible blocks (age class >= 40): 101993
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.09 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 6.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
