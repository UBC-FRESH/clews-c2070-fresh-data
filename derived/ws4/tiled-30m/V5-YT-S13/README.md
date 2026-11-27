# WS4 tiled 30-m dataset — V5|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V5|YT|S13` (parent `V5|YT`)
- Tile / row / col: `V5` / 1 / 3
- Province: `YT`
- Centroid: 68.848248, -140.460785
- Allocated harvest: 29.740269 m3
- Productive subcell area: 30328.493946 ha
- Committed geometry area: 221996.075565 ha
- Clipped inventory geometry: 221996.075565 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 339277
- Blocks: 114345
- Forest area: 30534.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4833
- Scheduled area: 1418.58 ha
- Eligible blocks (age class >= 40): 48321
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.53 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 4.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
