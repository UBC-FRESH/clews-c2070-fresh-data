# WS4 tiled 30-m dataset — H36|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H36|NL|S22` (parent `H36|NL`)
- Tile / row / col: `H36` / 2 / 2
- Province: `NL`
- Centroid: 46.657773, -53.580490
- Allocated harvest: 559.911712 m3
- Productive subcell area: 7002.910873 ha
- Committed geometry area: 13044.344972 ha
- Clipped inventory geometry: 13044.344972 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 64284
- Blocks: 32499
- Forest area: 5785.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2255
- Scheduled area: 381.51 ha
- Eligible blocks (age class >= 40): 22546
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.21 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
