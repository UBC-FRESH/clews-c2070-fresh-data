# WS4 tiled 30-m dataset — R6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R6|YT|S11` (parent `R6|YT`)
- Tile / row / col: `R6` / 1 / 1
- Province: `YT`
- Centroid: 64.407762, -131.317003
- Allocated harvest: 3.520274 m3
- Productive subcell area: 3033.940935 ha
- Committed geometry area: 6727.398985 ha
- Clipped inventory geometry: 6727.398985 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1209
- Blocks: 674
- Forest area: 108.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16
- Scheduled area: 1.71 ha
- Eligible blocks (age class >= 40): 16
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
