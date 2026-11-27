# WS4 tiled 30-m dataset — E31|NB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S22` (parent `E31|NB`)
- Tile / row / col: `E31` / 2 / 2
- Province: `NB`
- Centroid: 46.722842, -65.247145
- Allocated harvest: 174030.785335 m3
- Productive subcell area: 217334.276898 ha
- Committed geometry area: 239779.381281 ha
- Clipped inventory geometry: 239779.381281 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2463694
- Blocks: 942407
- Forest area: 221732.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78294
- Scheduled area: 15380.91 ha
- Eligible blocks (age class >= 40): 782933
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.62 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 31.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
