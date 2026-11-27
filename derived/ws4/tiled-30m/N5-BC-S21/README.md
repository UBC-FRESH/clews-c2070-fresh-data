# WS4 tiled 30-m dataset — N5|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N5|BC|S21` (parent `N5|BC`)
- Tile / row / col: `N5` / 2 / 1
- Province: `BC`
- Centroid: 59.606667, -128.086988
- Allocated harvest: 71478.149458 m3
- Productive subcell area: 221524.303503 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2345108
- Blocks: 796325
- Forest area: 211059.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66768
- Scheduled area: 15530.31 ha
- Eligible blocks (age class >= 40): 667675
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.02 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 27.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
