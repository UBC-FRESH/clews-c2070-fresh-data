# WS4 tiled 30-m dataset — I10|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|AB|S32` (parent `I10|AB`)
- Tile / row / col: `I10` / 3 / 2
- Province: `AB`
- Centroid: 56.350132, -110.634751
- Allocated harvest: 82707.233931 m3
- Productive subcell area: 222888.722426 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2262269
- Blocks: 744153
- Forest area: 203604.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53459
- Scheduled area: 11684.16 ha
- Eligible blocks (age class >= 40): 534587
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.35 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 26.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
