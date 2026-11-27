# WS4 tiled 30-m dataset — J8|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J8|AB|S12` (parent `J8|AB`)
- Tile / row / col: `J8` / 1 / 2
- Province: `AB`
- Centroid: 56.016382, -115.606248
- Allocated harvest: 126368.536618 m3
- Productive subcell area: 212567.530268 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2148501
- Blocks: 777009
- Forest area: 193365.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68327
- Scheduled area: 15672.15 ha
- Eligible blocks (age class >= 40): 683262
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.20 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 27.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
