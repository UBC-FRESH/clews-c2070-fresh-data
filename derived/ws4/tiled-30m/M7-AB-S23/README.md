# WS4 tiled 30-m dataset — M7|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|AB|S23` (parent `M7|AB`)
- Tile / row / col: `M7` / 2 / 3
- Province: `AB`
- Centroid: 59.915874, -119.876057
- Allocated harvest: 6227.631724 m3
- Productive subcell area: 12584.264178 ha
- Committed geometry area: 24498.939752 ha
- Clipped inventory geometry: 24498.939752 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 85517
- Blocks: 34000
- Forest area: 7696.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1695
- Scheduled area: 259.38 ha
- Eligible blocks (age class >= 40): 16950
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.41 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
