# WS4 tiled 30-m dataset — Q6|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|NT|S31` (parent `Q6|NT`)
- Tile / row / col: `Q6` / 3 / 1
- Province: `NT`
- Centroid: 64.291683, -130.546114
- Allocated harvest: 22.661681 m3
- Productive subcell area: 37494.272406 ha
- Committed geometry area: 220376.003079 ha
- Clipped inventory geometry: 220376.003079 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 127058
- Blocks: 74607
- Forest area: 11435.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2550
- Scheduled area: 315.36 ha
- Eligible blocks (age class >= 40): 25499
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.50 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
