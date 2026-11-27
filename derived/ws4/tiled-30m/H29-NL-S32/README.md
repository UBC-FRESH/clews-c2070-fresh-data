# WS4 tiled 30-m dataset — H29|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|NL|S32` (parent `H29|NL`)
- Tile / row / col: `H29` / 3 / 2
- Province: `NL`
- Centroid: 52.126880, -65.791926
- Allocated harvest: 2380.258945 m3
- Productive subcell area: 32304.581427 ha
- Committed geometry area: 53163.866902 ha
- Clipped inventory geometry: 53163.866902 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 457502
- Blocks: 237417
- Forest area: 41175.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22628
- Scheduled area: 3832.47 ha
- Eligible blocks (age class >= 40): 226279
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.13 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 7.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
