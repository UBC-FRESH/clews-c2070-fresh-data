# WS4 tiled 30-m dataset — N6|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S23` (parent `N6|NT`)
- Tile / row / col: `N6` / 2 / 3
- Province: `NT`
- Centroid: 60.689692, -123.979947
- Allocated harvest: 280.864160 m3
- Productive subcell area: 190886.296034 ha
- Committed geometry area: 241638.875458 ha
- Clipped inventory geometry: 241638.875458 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2296570
- Blocks: 1048862
- Forest area: 206691.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 97838
- Scheduled area: 17754.75 ha
- Eligible blocks (age class >= 40): 978373
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.95 MB
- Schedules: 1.17 MB
- Runs: 0.00 MB
- Total: 32.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
