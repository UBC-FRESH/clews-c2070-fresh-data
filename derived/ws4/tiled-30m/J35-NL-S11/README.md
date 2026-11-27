# WS4 tiled 30-m dataset — J35|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J35|NL|S11` (parent `J35|NL`)
- Tile / row / col: `J35` / 1 / 1
- Province: `NL`
- Centroid: 49.386469, -54.067384
- Allocated harvest: 6349.238463 m3
- Productive subcell area: 91182.362430 ha
- Committed geometry area: 116650.433951 ha
- Clipped inventory geometry: 116650.433951 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 830954
- Blocks: 436259
- Forest area: 74785.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40412
- Scheduled area: 6835.23 ha
- Eligible blocks (age class >= 40): 404120
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.19 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 12.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
