# WS4 tiled 30-m dataset — I6|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|BC|S22` (parent `I6|BC`)
- Tile / row / col: `I6` / 2 / 2
- Province: `BC`
- Centroid: 54.305103, -120.018304
- Allocated harvest: 829.043558 m3
- Productive subcell area: 1322.173806 ha
- Committed geometry area: 1744.312183 ha
- Clipped inventory geometry: 1744.312183 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 18713
- Blocks: 7563
- Forest area: 1684.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 743
- Scheduled area: 156.15 ha
- Eligible blocks (age class >= 40): 7427
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.37 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
