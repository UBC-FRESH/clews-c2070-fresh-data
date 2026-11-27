# WS4 tiled 30-m dataset — H17|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H17|MB|S13` (parent `H17|MB`)
- Tile / row / col: `H17` / 1 / 3
- Province: `MB`
- Centroid: 55.088188, -92.381934
- Allocated harvest: 3645.868581 m3
- Productive subcell area: 164893.583956 ha
- Committed geometry area: 248267.048285 ha
- Clipped inventory geometry: 248267.048285 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2339423
- Blocks: 868380
- Forest area: 210548.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77114
- Scheduled area: 17655.21 ha
- Eligible blocks (age class >= 40): 771132
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.87 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 29.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
