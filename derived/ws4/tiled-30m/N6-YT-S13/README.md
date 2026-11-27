# WS4 tiled 30-m dataset — N6|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S13` (parent `N6|YT`)
- Tile / row / col: `N6` / 1 / 3
- Province: `YT`
- Centroid: 60.016376, -123.835339
- Allocated harvest: 1.289176 m3
- Productive subcell area: 542.869176 ha
- Committed geometry area: 627.062372 ha
- Clipped inventory geometry: 627.062372 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 6045
- Blocks: 3249
- Forest area: 544.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3189
- Scheduled area: 511.92 ha
- Eligible blocks (age class >= 40): 3189
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.18 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
