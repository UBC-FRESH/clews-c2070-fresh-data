# WS4 tiled 30-m dataset — I18|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|MB|S12` (parent `I18|MB`)
- Tile / row / col: `I18` / 1 / 2
- Province: `MB`
- Centroid: 56.409970, -90.621706
- Allocated harvest: 1740.777450 m3
- Productive subcell area: 134512.346602 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1499094
- Blocks: 520116
- Forest area: 134918.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39200
- Scheduled area: 9873.45 ha
- Eligible blocks (age class >= 40): 391999
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.81 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 18.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
