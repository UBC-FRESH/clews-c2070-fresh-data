# WS4 tiled 30-m dataset — K8|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K8|AB|S21` (parent `K8|AB`)
- Tile / row / col: `K8` / 2 / 1
- Province: `AB`
- Centroid: 57.597324, -117.510441
- Allocated harvest: 121093.191000 m3
- Productive subcell area: 204039.481003 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2294719
- Blocks: 988212
- Forest area: 206524.71 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92568
- Scheduled area: 17449.29 ha
- Eligible blocks (age class >= 40): 925680
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.31 MB
- Schedules: 1.10 MB
- Runs: 0.00 MB
- Total: 31.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
