# WS4 tiled 30-m dataset — B22|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B22|ON|S22` (parent `B22|ON`)
- Tile / row / col: `B22` / 2 / 2
- Province: `ON`
- Centroid: 46.734726, -83.741151
- Allocated harvest: 65919.612759 m3
- Productive subcell area: 225032.950533 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2587231
- Blocks: 606981
- Forest area: 232850.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59175
- Scheduled area: 21607.47 ha
- Eligible blocks (age class >= 40): 591744
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.44 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 28.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
