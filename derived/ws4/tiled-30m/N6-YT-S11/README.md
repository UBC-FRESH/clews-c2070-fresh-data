# WS4 tiled 30-m dataset — N6|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S11` (parent `N6|YT`)
- Tile / row / col: `N6` / 1 / 1
- Province: `YT`
- Centroid: 60.058042, -125.205484
- Allocated harvest: 88.522068 m3
- Productive subcell area: 37276.443140 ha
- Committed geometry area: 43057.620254 ha
- Clipped inventory geometry: 43057.620254 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 458077
- Blocks: 200995
- Forest area: 41226.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19080
- Scheduled area: 3207.24 ha
- Eligible blocks (age class >= 40): 190791
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.75 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 6.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
