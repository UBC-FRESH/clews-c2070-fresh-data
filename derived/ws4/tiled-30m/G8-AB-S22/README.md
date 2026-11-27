# WS4 tiled 30-m dataset — G8|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G8|AB|S22` (parent `G8|AB`)
- Tile / row / col: `G8` / 2 / 2
- Province: `AB`
- Centroid: 52.533529, -113.706375
- Allocated harvest: 45222.142318 m3
- Productive subcell area: 65214.268399 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 480087
- Blocks: 241629
- Forest area: 43207.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16762
- Scheduled area: 3326.49 ha
- Eligible blocks (age class >= 40): 167612
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.37 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 7.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
