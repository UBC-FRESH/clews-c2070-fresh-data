# WS4 tiled 30-m dataset — J8|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J8|AB|S11` (parent `J8|AB`)
- Tile / row / col: `J8` / 1 / 1
- Province: `AB`
- Centroid: 55.867703, -116.379569
- Allocated harvest: 126368.536618 m3
- Productive subcell area: 212567.530268 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2097131
- Blocks: 735597
- Forest area: 188741.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60086
- Scheduled area: 13340.16 ha
- Eligible blocks (age class >= 40): 600856
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.02 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 25.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
