# WS4 tiled 30-m dataset — A25|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A25|ON|S13` (parent `A25|ON`)
- Tile / row / col: `A25` / 1 / 3
- Province: `ON`
- Centroid: 44.097871, -78.168235
- Allocated harvest: 30933.243922 m3
- Productive subcell area: 109915.649452 ha
- Committed geometry area: 174455.530546 ha
- Clipped inventory geometry: 174455.530546 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 807083
- Blocks: 358909
- Forest area: 72637.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27233
- Scheduled area: 5790.42 ha
- Eligible blocks (age class >= 40): 272330
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.14 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 11.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
