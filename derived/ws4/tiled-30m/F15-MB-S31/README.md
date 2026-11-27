# WS4 tiled 30-m dataset — F15|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F15|MB|S31` (parent `F15|MB`)
- Tile / row / col: `F15` / 3 / 1
- Province: `MB`
- Centroid: 53.229347, -98.585543
- Allocated harvest: 3928.297390 m3
- Productive subcell area: 94387.498312 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 216727
- Blocks: 41209
- Forest area: 19505.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4074
- Scheduled area: 9777.96 ha
- Eligible blocks (age class >= 40): 40736
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.44 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
