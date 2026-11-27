# WS4 tiled 30-m dataset — K2|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K2|BC|S32` (parent `K2|BC`)
- Tile / row / col: `K2` / 3 / 2
- Province: `BC`
- Centroid: 54.567410, -130.298450
- Allocated harvest: 63515.203514 m3
- Productive subcell area: 89077.630029 ha
- Committed geometry area: 126599.983685 ha
- Clipped inventory geometry: 126599.983685 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1250024
- Blocks: 671203
- Forest area: 112502.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65987
- Scheduled area: 10734.12 ha
- Eligible blocks (age class >= 40): 659864
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.29 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 19.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
