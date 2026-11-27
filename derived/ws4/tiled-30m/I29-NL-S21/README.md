# WS4 tiled 30-m dataset — I29|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|NL|S21` (parent `I29|NL`)
- Tile / row / col: `I29` / 2 / 1
- Province: `NL`
- Centroid: 52.975992, -65.856196
- Allocated harvest: 7340.245807 m3
- Productive subcell area: 138756.975841 ha
- Committed geometry area: 246574.260009 ha
- Clipped inventory geometry: 246574.260009 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1714591
- Blocks: 604659
- Forest area: 154313.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57863
- Scheduled area: 15482.16 ha
- Eligible blocks (age class >= 40): 578621
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.04 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 21.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
