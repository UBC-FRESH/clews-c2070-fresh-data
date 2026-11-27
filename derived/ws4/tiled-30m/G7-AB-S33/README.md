# WS4 tiled 30-m dataset — G7|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|AB|S33` (parent `G7|AB`)
- Tile / row / col: `G7` / 3 / 3
- Province: `AB`
- Centroid: 52.692183, -115.357328
- Allocated harvest: 160595.284005 m3
- Productive subcell area: 182003.461634 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2605689
- Blocks: 1137710
- Forest area: 234512.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 102906
- Scheduled area: 18034.74 ha
- Eligible blocks (age class >= 40): 1029052
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 34.69 MB
- Schedules: 1.24 MB
- Runs: 0.00 MB
- Total: 35.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
