# WS4 tiled 30-m dataset — U6|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|YT|S22` (parent `U6|YT`)
- Tile / row / col: `U6` / 2 / 2
- Province: `YT`
- Centroid: 68.696563, -137.051399
- Allocated harvest: 31.727903 m3
- Productive subcell area: 17113.754846 ha
- Committed geometry area: 199246.222320 ha
- Clipped inventory geometry: 199246.222320 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 71935
- Blocks: 50857
- Forest area: 6474.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2376
- Scheduled area: 276.48 ha
- Eligible blocks (age class >= 40): 23751
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.60 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
