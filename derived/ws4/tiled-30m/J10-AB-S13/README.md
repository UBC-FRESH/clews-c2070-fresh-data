# WS4 tiled 30-m dataset — J10|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|AB|S13` (parent `J10|AB`)
- Tile / row / col: `J10` / 1 / 3
- Province: `AB`
- Centroid: 56.897819, -110.220032
- Allocated harvest: 33644.095318 m3
- Productive subcell area: 114635.137708 ha
- Committed geometry area: 132444.584031 ha
- Clipped inventory geometry: 132444.584031 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1317582
- Blocks: 250678
- Forest area: 118582.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13915
- Scheduled area: 19684.35 ha
- Eligible blocks (age class >= 40): 139150
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.32 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 12.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
