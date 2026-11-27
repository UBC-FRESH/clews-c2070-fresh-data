# WS4 tiled 30-m dataset — M7|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|AB|S13` (parent `M7|AB`)
- Tile / row / col: `M7` / 1 / 3
- Province: `AB`
- Centroid: 59.585339, -119.749677
- Allocated harvest: 36252.227365 m3
- Productive subcell area: 73255.392488 ha
- Committed geometry area: 142612.982501 ha
- Clipped inventory geometry: 142612.982501 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 886102
- Blocks: 328195
- Forest area: 79749.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26708
- Scheduled area: 5944.68 ha
- Eligible blocks (age class >= 40): 267073
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.22 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 11.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
