# WS4 tiled 30-m dataset — H18|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|MB|S21` (parent `H18|MB`)
- Tile / row / col: `H18` / 2 / 1
- Province: `MB`
- Centroid: 55.538331, -91.567003
- Allocated harvest: 2819.213448 m3
- Productive subcell area: 139808.414090 ha
- Committed geometry area: 227925.333210 ha
- Clipped inventory geometry: 227925.333210 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1835145
- Blocks: 714496
- Forest area: 165163.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63071
- Scheduled area: 13410.81 ha
- Eligible blocks (age class >= 40): 630701
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.02 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 23.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
