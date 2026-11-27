# WS4 tiled 30-m dataset — K8|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K8|AB|S12` (parent `K8|AB`)
- Tile / row / col: `K8` / 1 / 2
- Province: `AB`
- Centroid: 57.320129, -116.418213
- Allocated harvest: 121093.191000 m3
- Productive subcell area: 204039.481003 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2339917
- Blocks: 919067
- Forest area: 210592.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89525
- Scheduled area: 19147.50 ha
- Eligible blocks (age class >= 40): 895250
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.88 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 30.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
