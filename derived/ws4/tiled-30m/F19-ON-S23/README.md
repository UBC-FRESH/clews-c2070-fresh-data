# WS4 tiled 30-m dataset — F19|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F19|ON|S23` (parent `F19|ON`)
- Tile / row / col: `F19` / 2 / 3
- Province: `ON`
- Centroid: 52.603413, -88.050186
- Allocated harvest: 29832.315511 m3
- Productive subcell area: 204802.351765 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2105024
- Blocks: 606172
- Forest area: 189452.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51041
- Scheduled area: 12427.47 ha
- Eligible blocks (age class >= 40): 510408
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.19 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 23.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
