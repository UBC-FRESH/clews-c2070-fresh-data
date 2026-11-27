# WS4 tiled 30-m dataset — R5|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R5|NT|S23` (parent `R5|NT`)
- Tile / row / col: `R5` / 2 / 3
- Province: `NT`
- Centroid: 64.848766, -132.287379
- Allocated harvest: 5.293230 m3
- Productive subcell area: 7965.937431 ha
- Committed geometry area: 49922.585464 ha
- Clipped inventory geometry: 49922.585464 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 35606
- Blocks: 20760
- Forest area: 3204.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1137
- Scheduled area: 166.23 ha
- Eligible blocks (age class >= 40): 11370
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.74 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
