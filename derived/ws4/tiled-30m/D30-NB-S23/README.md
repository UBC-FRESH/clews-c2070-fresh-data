# WS4 tiled 30-m dataset — D30|NB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D30|NB|S23` (parent `D30|NB`)
- Tile / row / col: `D30` / 2 / 3
- Province: `NB`
- Centroid: 45.913587, -67.229637
- Allocated harvest: 211115.818464 m3
- Productive subcell area: 218747.429711 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2428517
- Blocks: 895051
- Forest area: 218566.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74807
- Scheduled area: 14406.03 ha
- Eligible blocks (age class >= 40): 748069
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.68 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 30.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
