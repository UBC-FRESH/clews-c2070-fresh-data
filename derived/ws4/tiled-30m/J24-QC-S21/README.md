# WS4 tiled 30-m dataset — J24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J24|QC|S21` (parent `J24|QC`)
- Tile / row / col: `J24` / 2 / 1
- Province: `QC`
- Centroid: 56.796574, -76.058690
- Allocated harvest: 10646.629605 m3
- Productive subcell area: 64110.031827 ha
- Committed geometry area: 248530.125351 ha
- Clipped inventory geometry: 248530.125351 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 495384
- Blocks: 291961
- Forest area: 44584.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14892
- Scheduled area: 2172.78 ha
- Eligible blocks (age class >= 40): 148917
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.94 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 8.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
