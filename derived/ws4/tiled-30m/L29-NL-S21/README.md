# WS4 tiled 30-m dataset — L29|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S21` (parent `L29|NL`)
- Tile / row / col: `L29` / 2 / 1
- Province: `NL`
- Centroid: 56.618373, -62.555450
- Allocated harvest: 6971.209754 m3
- Productive subcell area: 91883.395308 ha
- Committed geometry area: 241698.431133 ha
- Clipped inventory geometry: 241698.431133 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 685085
- Blocks: 274549
- Forest area: 61657.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19425
- Scheduled area: 5080.86 ha
- Eligible blocks (age class >= 40): 194245
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.11 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 9.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
