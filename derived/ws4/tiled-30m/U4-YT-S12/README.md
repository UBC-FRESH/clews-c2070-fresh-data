# WS4 tiled 30-m dataset — U4|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U4|YT|S12` (parent `U4|YT`)
- Tile / row / col: `U4` / 1 / 2
- Province: `YT`
- Centroid: 66.572195, -140.982370
- Allocated harvest: 1.018243 m3
- Productive subcell area: 570.644264 ha
- Committed geometry area: 852.446664 ha
- Clipped inventory geometry: 852.446664 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8667
- Blocks: 2673
- Forest area: 780.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2464
- Scheduled area: 741.60 ha
- Eligible blocks (age class >= 40): 2464
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.18 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
