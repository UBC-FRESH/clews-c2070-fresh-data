# WS4 tiled 30-m dataset — N6|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S22` (parent `N6|NT`)
- Tile / row / col: `N6` / 2 / 2
- Province: `NT`
- Centroid: 60.584286, -124.452075
- Allocated harvest: 11.629546 m3
- Productive subcell area: 7903.895786 ha
- Committed geometry area: 10005.372461 ha
- Clipped inventory geometry: 10005.372461 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 59627
- Blocks: 28895
- Forest area: 5366.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2499
- Scheduled area: 489.51 ha
- Eligible blocks (age class >= 40): 24984
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.11 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
