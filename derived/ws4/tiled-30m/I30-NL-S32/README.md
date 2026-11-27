# WS4 tiled 30-m dataset — I30|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|NL|S32` (parent `I30|NL`)
- Tile / row / col: `I30` / 3 / 2
- Province: `NL`
- Centroid: 52.534466, -62.855304
- Allocated harvest: 12082.103414 m3
- Productive subcell area: 184287.684846 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1985794
- Blocks: 732116
- Forest area: 178721.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69278
- Scheduled area: 17513.82 ha
- Eligible blocks (age class >= 40): 692772
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.96 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 24.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
