# WS4 tiled 30-m dataset — G18|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G18|ON|S23` (parent `G18|ON`)
- Tile / row / col: `G18` / 2 / 3
- Province: `ON`
- Centroid: 54.092472, -90.113694
- Allocated harvest: 23436.922849 m3
- Productive subcell area: 196799.569942 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2197985
- Blocks: 609164
- Forest area: 197818.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55458
- Scheduled area: 16361.46 ha
- Eligible blocks (age class >= 40): 554575
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.27 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 24.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
