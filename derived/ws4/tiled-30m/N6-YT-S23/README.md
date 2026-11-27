# WS4 tiled 30-m dataset — N6|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S23` (parent `N6|YT`)
- Tile / row / col: `N6` / 2 / 3
- Province: `YT`
- Centroid: 60.773336, -124.527369
- Allocated harvest: 17.189618 m3
- Productive subcell area: 7238.509275 ha
- Committed geometry area: 8361.124542 ha
- Clipped inventory geometry: 8361.124542 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 42354
- Blocks: 21946
- Forest area: 3811.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1905
- Scheduled area: 319.77 ha
- Eligible blocks (age class >= 40): 19044
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.84 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
