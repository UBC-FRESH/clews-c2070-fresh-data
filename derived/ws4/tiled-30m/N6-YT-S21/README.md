# WS4 tiled 30-m dataset — N6|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S21` (parent `N6|YT`)
- Tile / row / col: `N6` / 2 / 1
- Province: `YT`
- Centroid: 60.274782, -125.664515
- Allocated harvest: 509.372332 m3
- Productive subcell area: 214495.540715 ha
- Committed geometry area: 247761.501912 ha
- Clipped inventory geometry: 247761.501912 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2632574
- Blocks: 1327746
- Forest area: 236931.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 128085
- Scheduled area: 21067.11 ha
- Eligible blocks (age class >= 40): 1280843
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 37.28 MB
- Schedules: 1.56 MB
- Runs: 0.00 MB
- Total: 38.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
