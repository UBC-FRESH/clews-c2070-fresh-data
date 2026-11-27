# WS4 tiled 30-m dataset — E7|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|AB|S23` (parent `E7|AB`)
- Tile / row / col: `E7` / 2 / 3
- Province: `AB`
- Centroid: 49.670480, -113.827814
- Allocated harvest: 117679.031591 m3
- Productive subcell area: 114028.095291 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 278326
- Blocks: 158658
- Forest area: 25049.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11416
- Scheduled area: 1899.27 ha
- Eligible blocks (age class >= 40): 114154
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.01 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
