# WS4 tiled 30-m dataset — B25|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|ON|S23` (parent `B25|ON`)
- Tile / row / col: `B25` / 2 / 3
- Province: `ON`
- Centroid: 45.734172, -77.499834
- Allocated harvest: 94055.367983 m3
- Productive subcell area: 326094.768704 ha
- Committed geometry area: 245759.898573 ha
- Clipped inventory geometry: 245759.898573 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2253945
- Blocks: 795858
- Forest area: 202855.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74396
- Scheduled area: 18898.20 ha
- Eligible blocks (age class >= 40): 743952
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.78 MB
- Schedules: 0.88 MB
- Runs: 0.00 MB
- Total: 28.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
