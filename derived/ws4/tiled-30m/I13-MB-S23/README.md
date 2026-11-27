# WS4 tiled 30-m dataset — I13|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|MB|S23` (parent `I13|MB`)
- Tile / row / col: `I13` / 2 / 3
- Province: `MB`
- Centroid: 56.715537, -101.944112
- Allocated harvest: 843.244655 m3
- Productive subcell area: 27088.508664 ha
- Committed geometry area: 36426.798648 ha
- Clipped inventory geometry: 36426.798648 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 255360
- Blocks: 39705
- Forest area: 22982.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2438
- Scheduled area: 565.38 ha
- Eligible blocks (age class >= 40): 24375
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.51 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
