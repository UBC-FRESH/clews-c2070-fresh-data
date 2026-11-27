# WS4 tiled 30-m dataset — F6|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F6|BC|S33` (parent `F6|BC`)
- Tile / row / col: `F6` / 3 / 3
- Province: `BC`
- Centroid: 50.961928, -116.722100
- Allocated harvest: 138342.879396 m3
- Productive subcell area: 175902.532281 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1788963
- Blocks: 844313
- Forest area: 161006.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75064
- Scheduled area: 12037.68 ha
- Eligible blocks (age class >= 40): 750638
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.56 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 25.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
