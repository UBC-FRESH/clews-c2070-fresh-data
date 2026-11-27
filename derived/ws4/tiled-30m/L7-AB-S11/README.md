# WS4 tiled 30-m dataset — L7|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|AB|S11` (parent `L7|AB`)
- Tile / row / col: `L7` / 1 / 1
- Province: `AB`
- Centroid: 57.826643, -119.994235
- Allocated harvest: 66.916524 m3
- Productive subcell area: 118.517167 ha
- Committed geometry area: 140.292008 ha
- Clipped inventory geometry: 140.292008 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1593
- Blocks: 321
- Forest area: 143.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 303
- Scheduled area: 137.97 ha
- Eligible blocks (age class >= 40): 303
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
