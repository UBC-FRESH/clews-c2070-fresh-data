# WS4 tiled 30-m dataset — E14|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E14|MB|S31` (parent `E14|MB`)
- Tile / row / col: `E14` / 3 / 1
- Province: `MB`
- Centroid: 51.769286, -100.653263
- Allocated harvest: 5739.840368 m3
- Productive subcell area: 103522.083624 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2080221
- Blocks: 772236
- Forest area: 187219.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71285
- Scheduled area: 16070.58 ha
- Eligible blocks (age class >= 40): 712846
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.57 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 26.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
