# WS4 tiled 30-m dataset — N5|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|YT|S22` (parent `N5|YT`)
- Tile / row / col: `N5` / 2 / 2
- Province: `YT`
- Centroid: 60.049384, -127.233996
- Allocated harvest: 61.760311 m3
- Productive subcell area: 26147.418996 ha
- Committed geometry area: 29907.138530 ha
- Clipped inventory geometry: 29907.138530 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 221743
- Blocks: 51751
- Forest area: 19956.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2275
- Scheduled area: 344.16 ha
- Eligible blocks (age class >= 40): 22748
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.55 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 2.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
