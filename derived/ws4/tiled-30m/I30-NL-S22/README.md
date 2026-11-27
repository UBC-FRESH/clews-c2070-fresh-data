# WS4 tiled 30-m dataset — I30|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|NL|S22` (parent `I30|NL`)
- Tile / row / col: `I30` / 2 / 2
- Province: `NL`
- Centroid: 52.175398, -63.216636
- Allocated harvest: 10033.824445 m3
- Productive subcell area: 153045.393984 ha
- Committed geometry area: 207617.500474 ha
- Clipped inventory geometry: 207617.500474 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1621499
- Blocks: 707095
- Forest area: 145934.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68763
- Scheduled area: 14196.69 ha
- Eligible blocks (age class >= 40): 687628
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.12 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 21.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
