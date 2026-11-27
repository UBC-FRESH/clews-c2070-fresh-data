# WS4 tiled 30-m dataset — H36|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H36|NL|S21` (parent `H36|NL`)
- Tile / row / col: `H36` / 2 / 1
- Province: `NL`
- Centroid: 46.894848, -54.101559
- Allocated harvest: 1004.555371 m3
- Productive subcell area: 12564.144639 ha
- Committed geometry area: 23403.273285 ha
- Clipped inventory geometry: 23403.273285 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 100179
- Blocks: 51079
- Forest area: 9016.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3838
- Scheduled area: 659.43 ha
- Eligible blocks (age class >= 40): 38373
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.87 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
