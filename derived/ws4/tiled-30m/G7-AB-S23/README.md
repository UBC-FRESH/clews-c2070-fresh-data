# WS4 tiled 30-m dataset — G7|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|AB|S23` (parent `G7|AB`)
- Tile / row / col: `G7` / 2 / 3
- Province: `AB`
- Centroid: 52.260219, -115.124290
- Allocated harvest: 160595.284005 m3
- Productive subcell area: 182003.461634 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2167417
- Blocks: 1041775
- Forest area: 195067.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92925
- Scheduled area: 15209.64 ha
- Eligible blocks (age class >= 40): 929247
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.69 MB
- Schedules: 1.11 MB
- Runs: 0.00 MB
- Total: 30.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
