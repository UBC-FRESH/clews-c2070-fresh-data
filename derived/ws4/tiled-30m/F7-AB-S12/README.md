# WS4 tiled 30-m dataset — F7|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|AB|S12` (parent `F7|AB`)
- Tile / row / col: `F7` / 1 / 2
- Province: `AB`
- Centroid: 50.453647, -114.746247
- Allocated harvest: 54960.562089 m3
- Productive subcell area: 62832.156433 ha
- Committed geometry area: 110398.353243 ha
- Clipped inventory geometry: 110398.353243 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 904135
- Blocks: 425751
- Forest area: 81372.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40803
- Scheduled area: 7587.90 ha
- Eligible blocks (age class >= 40): 408025
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.78 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 13.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
