# WS4 tiled 30-m dataset — L30|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L30|NL|S22` (parent `L30|NL`)
- Tile / row / col: `L30` / 2 / 2
- Province: `NL`
- Centroid: 55.502583, -59.847789
- Allocated harvest: 29.448428 m3
- Productive subcell area: 430.822713 ha
- Committed geometry area: 887.671492 ha
- Clipped inventory geometry: 887.671492 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 557
- Blocks: 402
- Forest area: 50.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87
- Scheduled area: 8.64 ha
- Eligible blocks (age class >= 40): 87
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
