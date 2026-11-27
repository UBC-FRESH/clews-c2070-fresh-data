# WS4 tiled 30-m dataset — L29|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S32` (parent `L29|NL`)
- Tile / row / col: `L29` / 3 / 2
- Province: `NL`
- Centroid: 56.810701, -61.526666
- Allocated harvest: 3365.362936 m3
- Productive subcell area: 44356.859697 ha
- Committed geometry area: 116680.313815 ha
- Clipped inventory geometry: 116680.313815 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 272047
- Blocks: 134612
- Forest area: 24484.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9375
- Scheduled area: 1793.25 ha
- Eligible blocks (age class >= 40): 93750
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.63 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
