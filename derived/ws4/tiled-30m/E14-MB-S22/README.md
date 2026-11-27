# WS4 tiled 30-m dataset — E14|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E14|MB|S22` (parent `E14|MB`)
- Tile / row / col: `E14` / 2 / 2
- Province: `MB`
- Centroid: 51.354750, -99.867962
- Allocated harvest: 5739.840368 m3
- Productive subcell area: 103522.083624 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 484012
- Blocks: 104603
- Forest area: 43561.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7629
- Scheduled area: 4074.75 ha
- Eligible blocks (age class >= 40): 76288
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.31 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 5.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
