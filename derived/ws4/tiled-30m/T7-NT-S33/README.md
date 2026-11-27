# WS4 tiled 30-m dataset — T7|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T7|NT|S33` (parent `T7|NT`)
- Tile / row / col: `T7` / 3 / 3
- Province: `NT`
- Centroid: 69.031863, -131.308386
- Allocated harvest: 142.374524 m3
- Productive subcell area: 146242.744005 ha
- Committed geometry area: 248112.721198 ha
- Clipped inventory geometry: 248112.721198 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 552882
- Blocks: 290125
- Forest area: 49759.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14141
- Scheduled area: 2049.48 ha
- Eligible blocks (age class >= 40): 141406
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.36 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 8.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
