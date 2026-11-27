# WS4 tiled 30-m dataset — J8|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J8|AB|S23` (parent `J8|AB`)
- Tile / row / col: `J8` / 2 / 3
- Province: `AB`
- Centroid: 56.596549, -115.081937
- Allocated harvest: 126368.536618 m3
- Productive subcell area: 212567.530268 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2028857
- Blocks: 699436
- Forest area: 182597.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66332
- Scheduled area: 17450.91 ha
- Eligible blocks (age class >= 40): 663312
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.19 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 24.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
