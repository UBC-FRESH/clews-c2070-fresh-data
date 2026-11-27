# WS4 tiled 30-m dataset — K11|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|AB|S11` (parent `K11|AB`)
- Tile / row / col: `K11` / 1 / 1
- Province: `AB`
- Centroid: 58.352151, -110.114924
- Allocated harvest: 7292.191721 m3
- Productive subcell area: 33142.536602 ha
- Committed geometry area: 62705.360365 ha
- Clipped inventory geometry: 62705.360365 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 535093
- Blocks: 102594
- Forest area: 48158.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7705
- Scheduled area: 4280.58 ha
- Eligible blocks (age class >= 40): 77041
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.26 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 5.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
