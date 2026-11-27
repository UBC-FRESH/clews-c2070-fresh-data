# WS4 tiled 30-m dataset — H34|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H34|NL|S23` (parent `H34|NL`)
- Tile / row / col: `H34` / 2 / 3
- Province: `NL`
- Centroid: 47.904130, -56.561504
- Allocated harvest: 7561.915737 m3
- Productive subcell area: 124765.284299 ha
- Committed geometry area: 247656.817368 ha
- Clipped inventory geometry: 247656.817368 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 777114
- Blocks: 516660
- Forest area: 69940.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35632
- Scheduled area: 4696.29 ha
- Eligible blocks (age class >= 40): 356316
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.82 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 13.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
