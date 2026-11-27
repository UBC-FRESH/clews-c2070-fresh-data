# WS4 tiled 30-m dataset — F7|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|AB|S21` (parent `F7|AB`)
- Tile / row / col: `F7` / 2 / 1
- Province: `AB`
- Centroid: 50.862659, -115.570125
- Allocated harvest: 4005.491315 m3
- Productive subcell area: 4579.168177 ha
- Committed geometry area: 8045.762786 ha
- Clipped inventory geometry: 8045.762786 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 29333
- Blocks: 17358
- Forest area: 2639.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1571
- Scheduled area: 226.89 ha
- Eligible blocks (age class >= 40): 15706
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.63 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
