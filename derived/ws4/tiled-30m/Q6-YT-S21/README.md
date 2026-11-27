# WS4 tiled 30-m dataset — Q6|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|YT|S21` (parent `Q6|YT`)
- Tile / row / col: `Q6` / 2 / 1
- Province: `YT`
- Centroid: 63.782557, -130.358420
- Allocated harvest: 12.618588 m3
- Productive subcell area: 11293.997075 ha
- Committed geometry area: 44738.553388 ha
- Clipped inventory geometry: 44738.553388 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 46656
- Blocks: 26497
- Forest area: 4199.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 607
- Scheduled area: 83.79 ha
- Eligible blocks (age class >= 40): 6066
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.93 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
