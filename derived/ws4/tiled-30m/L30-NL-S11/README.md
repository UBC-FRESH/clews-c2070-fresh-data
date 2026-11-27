# WS4 tiled 30-m dataset — L30|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L30|NL|S11` (parent `L30|NL`)
- Tile / row / col: `L30` / 1 / 1
- Province: `NL`
- Centroid: 55.526082, -60.843139
- Allocated harvest: 7736.583433 m3
- Productive subcell area: 113184.167805 ha
- Committed geometry area: 233205.808549 ha
- Clipped inventory geometry: 233205.808549 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1608569
- Blocks: 476948
- Forest area: 144771.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34888
- Scheduled area: 13077.99 ha
- Eligible blocks (age class >= 40): 348871
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.03 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 18.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
