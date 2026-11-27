# WS4 tiled 30-m dataset — G8|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G8|AB|S23` (parent `G8|AB`)
- Tile / row / col: `G8` / 2 / 3
- Province: `AB`
- Centroid: 52.662959, -112.990074
- Allocated harvest: 45222.142318 m3
- Productive subcell area: 65214.268399 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 446431
- Blocks: 205146
- Forest area: 40178.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12315
- Scheduled area: 2850.84 ha
- Eligible blocks (age class >= 40): 123146
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.56 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 6.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
