# WS4 tiled 30-m dataset — R2|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S21` (parent `R2|YT`)
- Tile / row / col: `R2` / 2 / 1
- Province: `YT`
- Centroid: 61.657436, -140.967063
- Allocated harvest: 2.727536 m3
- Productive subcell area: 1293.985180 ha
- Committed geometry area: 2510.845581 ha
- Clipped inventory geometry: 2510.845581 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 13061
- Blocks: 7299
- Forest area: 1175.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4486
- Scheduled area: 652.23 ha
- Eligible blocks (age class >= 40): 4486
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.31 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
