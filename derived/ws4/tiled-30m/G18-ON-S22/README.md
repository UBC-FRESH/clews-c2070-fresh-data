# WS4 tiled 30-m dataset — G18|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G18|ON|S22` (parent `G18|ON`)
- Tile / row / col: `G18` / 2 / 2
- Province: `ON`
- Centroid: 54.124754, -90.889179
- Allocated harvest: 23436.922849 m3
- Productive subcell area: 196799.569942 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1947209
- Blocks: 483957
- Forest area: 175248.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37258
- Scheduled area: 10338.39 ha
- Eligible blocks (age class >= 40): 372577
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.16 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 20.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
