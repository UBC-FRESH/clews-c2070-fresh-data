# WS4 tiled 30-m dataset — N5|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|YT|S23` (parent `N5|YT`)
- Tile / row / col: `N5` / 2 / 3
- Province: `YT`
- Centroid: 60.137348, -126.498487
- Allocated harvest: 327.919820 m3
- Productive subcell area: 138831.181881 ha
- Committed geometry area: 158793.622784 ha
- Clipped inventory geometry: 158793.622784 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1559006
- Blocks: 550466
- Forest area: 140310.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49194
- Scheduled area: 11061.45 ha
- Eligible blocks (age class >= 40): 491934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.31 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 18.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
