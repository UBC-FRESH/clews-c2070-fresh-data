# WS4 tiled 30-m dataset — H10|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|AB|S21` (parent `H10|AB`)
- Tile / row / col: `H10` / 2 / 1
- Province: `AB`
- Centroid: 54.460882, -110.632074
- Allocated harvest: 87868.773826 m3
- Productive subcell area: 180737.504911 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1487683
- Blocks: 654922
- Forest area: 133891.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56660
- Scheduled area: 11765.25 ha
- Eligible blocks (age class >= 40): 566596
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.08 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 20.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
