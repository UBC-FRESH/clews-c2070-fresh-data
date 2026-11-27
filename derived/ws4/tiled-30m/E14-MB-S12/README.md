# WS4 tiled 30-m dataset — E14|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E14|MB|S12` (parent `E14|MB`)
- Tile / row / col: `E14` / 1 / 2
- Province: `MB`
- Centroid: 50.903137, -99.813236
- Allocated harvest: 5739.840368 m3
- Productive subcell area: 103522.083624 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1539035
- Blocks: 494841
- Forest area: 138513.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47072
- Scheduled area: 20373.39 ha
- Eligible blocks (age class >= 40): 470714
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.24 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 18.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
