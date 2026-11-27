# WS4 tiled 30-m dataset — L8|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L8|AB|S11` (parent `L8|AB`)
- Tile / row / col: `L8` / 1 / 1
- Province: `AB`
- Centroid: 58.459730, -118.119918
- Allocated harvest: 105518.724816 m3
- Productive subcell area: 196148.635131 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1776649
- Blocks: 646859
- Forest area: 159898.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42800
- Scheduled area: 5886.45 ha
- Eligible blocks (age class >= 40): 427996
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.13 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 21.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
