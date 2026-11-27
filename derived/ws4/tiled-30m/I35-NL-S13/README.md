# WS4 tiled 30-m dataset — I35|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S13` (parent `I35|NL`)
- Tile / row / col: `I35` / 1 / 3
- Province: `NL`
- Centroid: 47.884436, -54.181407
- Allocated harvest: 9611.456827 m3
- Productive subcell area: 125997.054345 ha
- Committed geometry area: 193530.569589 ha
- Clipped inventory geometry: 193530.569589 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1202299
- Blocks: 665224
- Forest area: 108206.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57595
- Scheduled area: 9558.90 ha
- Eligible blocks (age class >= 40): 575950
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.05 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 18.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
