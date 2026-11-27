# WS4 tiled 30-m dataset — N6|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S32` (parent `N6|YT`)
- Tile / row / col: `N6` / 3 / 2
- Province: `YT`
- Centroid: 60.749436, -125.177629
- Allocated harvest: 167.368615 m3
- Productive subcell area: 70478.546567 ha
- Committed geometry area: 81409.014340 ha
- Clipped inventory geometry: 81409.014340 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 763297
- Blocks: 402964
- Forest area: 68696.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36925
- Scheduled area: 7871.31 ha
- Eligible blocks (age class >= 40): 369246
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.37 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 11.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
