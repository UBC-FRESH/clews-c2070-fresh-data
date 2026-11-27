# WS4 tiled 30-m dataset — N7|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N7|NT|S23` (parent `N7|NT`)
- Tile / row / col: `N7` / 2 / 3
- Province: `NT`
- Centroid: 61.274835, -121.408752
- Allocated harvest: 283.888167 m3
- Productive subcell area: 199348.083161 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2270203
- Blocks: 874443
- Forest area: 204318.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81495
- Scheduled area: 17818.92 ha
- Eligible blocks (age class >= 40): 814950
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.55 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 29.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
