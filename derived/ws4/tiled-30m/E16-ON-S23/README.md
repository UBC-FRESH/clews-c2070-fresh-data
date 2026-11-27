# WS4 tiled 30-m dataset — E16|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E16|ON|S23` (parent `E16|ON`)
- Tile / row / col: `E16` / 2 / 3
- Province: `ON`
- Centroid: 51.471061, -94.792648
- Allocated harvest: 29709.404375 m3
- Productive subcell area: 167974.263949 ha
- Committed geometry area: 248091.426350 ha
- Clipped inventory geometry: 248091.426350 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1458363
- Blocks: 529126
- Forest area: 131252.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30332
- Scheduled area: 5515.38 ha
- Eligible blocks (age class >= 40): 303316
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.78 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 18.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
