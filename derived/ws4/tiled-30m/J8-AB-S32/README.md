# WS4 tiled 30-m dataset — J8|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J8|AB|S32` (parent `J8|AB`)
- Tile / row / col: `J8` / 3 / 2
- Province: `AB`
- Centroid: 56.885828, -116.140801
- Allocated harvest: 126368.536618 m3
- Productive subcell area: 212567.530268 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2434463
- Blocks: 795833
- Forest area: 219101.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76908
- Scheduled area: 23039.37 ha
- Eligible blocks (age class >= 40): 769073
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.37 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 29.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
