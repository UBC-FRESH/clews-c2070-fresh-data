# WS4 tiled 30-m dataset — E6|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E6|BC|S23` (parent `E6|BC`)
- Tile / row / col: `E6` / 2 / 3
- Province: `BC`
- Centroid: 49.258190, -115.799785
- Allocated harvest: 190123.629937 m3
- Productive subcell area: 206338.922113 ha
- Committed geometry area: 248252.852581 ha
- Clipped inventory geometry: 248252.852581 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2532287
- Blocks: 917651
- Forest area: 227905.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80807
- Scheduled area: 15189.93 ha
- Eligible blocks (age class >= 40): 808064
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.81 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 31.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
