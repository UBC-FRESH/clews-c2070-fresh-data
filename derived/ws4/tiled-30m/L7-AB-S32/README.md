# WS4 tiled 30-m dataset — L7|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|AB|S32` (parent `L7|AB`)
- Tile / row / col: `L7` / 3 / 2
- Province: `AB`
- Centroid: 58.902709, -119.947212
- Allocated harvest: 5321.971754 m3
- Productive subcell area: 9425.848435 ha
- Committed geometry area: 11157.634289 ha
- Clipped inventory geometry: 11157.634289 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 106909
- Blocks: 55823
- Forest area: 9621.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5458
- Scheduled area: 903.24 ha
- Eligible blocks (age class >= 40): 54578
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.04 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
