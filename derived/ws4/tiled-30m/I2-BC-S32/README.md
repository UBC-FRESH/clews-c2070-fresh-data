# WS4 tiled 30-m dataset — I2|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S32` (parent `I2|BC`)
- Tile / row / col: `I2` / 3 / 2
- Province: `BC`
- Centroid: 52.217365, -128.033087
- Allocated harvest: 81651.036264 m3
- Productive subcell area: 110973.625901 ha
- Committed geometry area: 163571.973360 ha
- Clipped inventory geometry: 163571.973360 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1700415
- Blocks: 823740
- Forest area: 153037.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81669
- Scheduled area: 14714.46 ha
- Eligible blocks (age class >= 40): 816681
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.39 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 24.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
