# WS4 tiled 30-m dataset — U6|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|YT|S21` (parent `U6|YT`)
- Tile / row / col: `U6` / 2 / 1
- Province: `YT`
- Centroid: 68.436968, -137.946810
- Allocated harvest: 39.809918 m3
- Productive subcell area: 21473.123363 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 44515
- Blocks: 32468
- Forest area: 4006.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 669
- Scheduled area: 71.55 ha
- Eligible blocks (age class >= 40): 6687
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.01 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
