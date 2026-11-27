# WS4 tiled 30-m dataset — G20|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G20|ON|S22` (parent `G20|ON`)
- Tile / row / col: `G20` / 2 / 2
- Province: `ON`
- Centroid: 53.848297, -86.262505
- Allocated harvest: 10027.306091 m3
- Productive subcell area: 122222.059994 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 968824
- Blocks: 576789
- Forest area: 87194.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50265
- Scheduled area: 7786.62 ha
- Eligible blocks (age class >= 40): 502641
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.84 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 15.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
