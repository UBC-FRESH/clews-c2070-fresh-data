# WS4 tiled 30-m dataset — B23|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B23|ON|S11` (parent `B23|ON`)
- Tile / row / col: `B23` / 1 / 1
- Province: `ON`
- Centroid: 46.202964, -82.565624
- Allocated harvest: 32203.183195 m3
- Productive subcell area: 106545.876439 ha
- Committed geometry area: 126135.126555 ha
- Clipped inventory geometry: 126135.126555 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1133041
- Blocks: 417133
- Forest area: 101973.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38066
- Scheduled area: 9148.41 ha
- Eligible blocks (age class >= 40): 380659
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.51 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 14.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
