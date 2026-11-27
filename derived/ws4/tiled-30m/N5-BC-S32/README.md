# WS4 tiled 30-m dataset — N5|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S32` (parent `N5|BC`)
- Tile / row / col: `N5` / 3 / 2
- Province: `BC`
- Centroid: 59.974010, -127.854386
- Allocated harvest: 2417.919987 m3
- Productive subcell area: 7493.591329 ha
- Committed geometry area: 8456.850118 ha
- Clipped inventory geometry: 8456.850118 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 81795
- Blocks: 35800
- Forest area: 7361.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3505
- Scheduled area: 525.60 ha
- Eligible blocks (age class >= 40): 35046
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.38 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
