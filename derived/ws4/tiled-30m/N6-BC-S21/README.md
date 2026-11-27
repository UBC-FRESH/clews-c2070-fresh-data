# WS4 tiled 30-m dataset — N6|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|BC|S21` (parent `N6|BC`)
- Tile / row / col: `N6` / 2 / 1
- Province: `BC`
- Centroid: 59.986893, -125.824336
- Allocated harvest: 690.604310 m3
- Productive subcell area: 2103.755637 ha
- Committed geometry area: 2238.498088 ha
- Clipped inventory geometry: 2238.498088 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 24354
- Blocks: 11184
- Forest area: 2191.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1108
- Scheduled area: 198.27 ha
- Eligible blocks (age class >= 40): 11075
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.48 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
