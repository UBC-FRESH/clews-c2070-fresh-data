# WS4 tiled 30-m dataset — L30|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L30|NL|S12` (parent `L30|NL`)
- Tile / row / col: `L30` / 1 / 2
- Province: `NL`
- Centroid: 55.239028, -60.183098
- Allocated harvest: 4166.661133 m3
- Productive subcell area: 60957.149490 ha
- Committed geometry area: 125596.729731 ha
- Clipped inventory geometry: 125596.729731 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 541318
- Blocks: 273443
- Forest area: 48718.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18173
- Scheduled area: 3353.85 ha
- Eligible blocks (age class >= 40): 181723
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.02 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 8.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
