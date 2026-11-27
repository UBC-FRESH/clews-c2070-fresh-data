# WS4 tiled 30-m dataset — C21|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C21|ON|S21` (parent `C21|ON`)
- Tile / row / col: `C21` / 2 / 1
- Province: `ON`
- Centroid: 48.359520, -85.945787
- Allocated harvest: 46319.843287 m3
- Productive subcell area: 161783.313405 ha
- Committed geometry area: 179915.547346 ha
- Clipped inventory geometry: 179915.547346 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1909403
- Blocks: 685798
- Forest area: 171846.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66474
- Scheduled area: 17385.93 ha
- Eligible blocks (age class >= 40): 664731
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.44 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 24.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
