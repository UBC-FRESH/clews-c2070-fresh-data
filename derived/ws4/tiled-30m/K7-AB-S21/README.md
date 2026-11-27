# WS4 tiled 30-m dataset — K7|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|AB|S21` (parent `K7|AB`)
- Tile / row / col: `K7` / 2 / 1
- Province: `AB`
- Centroid: 57.101268, -119.740206
- Allocated harvest: 87975.259421 m3
- Productive subcell area: 151402.345355 ha
- Committed geometry area: 160889.771863 ha
- Clipped inventory geometry: 160889.771863 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1696841
- Blocks: 614862
- Forest area: 152715.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58563
- Scheduled area: 12774.33 ha
- Eligible blocks (age class >= 40): 585624
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.53 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 21.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
