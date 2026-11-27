# WS4 tiled 30-m dataset — S6|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|YT|S12` (parent `S6|YT`)
- Tile / row / col: `S6` / 1 / 2
- Province: `YT`
- Centroid: 65.972629, -132.481063
- Allocated harvest: 6.053958 m3
- Productive subcell area: 3323.352218 ha
- Committed geometry area: 4798.899913 ha
- Clipped inventory geometry: 4798.899913 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 43076
- Blocks: 12244
- Forest area: 3876.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1059
- Scheduled area: 263.97 ha
- Eligible blocks (age class >= 40): 10583
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.65 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
