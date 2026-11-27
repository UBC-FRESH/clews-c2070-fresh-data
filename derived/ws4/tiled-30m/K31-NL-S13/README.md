# WS4 tiled 30-m dataset — K31|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K31|NL|S13` (parent `K31|NL`)
- Tile / row / col: `K31` / 1 / 3
- Province: `NL`
- Centroid: 53.165988, -58.730040
- Allocated harvest: 11705.187008 m3
- Productive subcell area: 186825.114590 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2157512
- Blocks: 645446
- Forest area: 194176.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58138
- Scheduled area: 17927.37 ha
- Eligible blocks (age class >= 40): 581375
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.56 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 25.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
