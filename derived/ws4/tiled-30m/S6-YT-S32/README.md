# WS4 tiled 30-m dataset — S6|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|YT|S32` (parent `S6|YT`)
- Tile / row / col: `S6` / 3 / 2
- Province: `YT`
- Centroid: 66.844370, -133.941590
- Allocated harvest: 20.195098 m3
- Productive subcell area: 11086.204923 ha
- Committed geometry area: 16008.410893 ha
- Clipped inventory geometry: 16008.410893 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 27391
- Blocks: 12900
- Forest area: 2465.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 612
- Scheduled area: 121.68 ha
- Eligible blocks (age class >= 40): 6119
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.53 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
