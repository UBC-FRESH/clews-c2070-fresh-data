# WS4 tiled 30-m dataset — I9|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I9|AB|S23` (parent `I9|AB`)
- Tile / row / col: `I9` / 2 / 3
- Province: `AB`
- Centroid: 55.673382, -112.011310
- Allocated harvest: 116090.047215 m3
- Productive subcell area: 214402.660003 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2548630
- Blocks: 656647
- Forest area: 229376.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50105
- Scheduled area: 10640.61 ha
- Eligible blocks (age class >= 40): 501045
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.45 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 27.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
