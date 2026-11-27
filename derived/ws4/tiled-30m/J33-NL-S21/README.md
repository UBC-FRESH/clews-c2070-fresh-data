# WS4 tiled 30-m dataset — J33|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S21` (parent `J33|NL`)
- Tile / row / col: `J33` / 2 / 1
- Province: `NL`
- Centroid: 51.539518, -56.983493
- Allocated harvest: 1339.499530 m3
- Productive subcell area: 28297.777162 ha
- Committed geometry area: 42644.267885 ha
- Clipped inventory geometry: 42644.267885 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 268993
- Blocks: 163570
- Forest area: 24209.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13703
- Scheduled area: 2057.49 ha
- Eligible blocks (age class >= 40): 137028
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.02 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 5.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
