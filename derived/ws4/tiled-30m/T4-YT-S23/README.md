# WS4 tiled 30-m dataset — T4|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S23` (parent `T4|YT`)
- Tile / row / col: `T4` / 2 / 3
- Province: `YT`
- Centroid: 66.194798, -139.373668
- Allocated harvest: 168.824215 m3
- Productive subcell area: 133298.605185 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1507883
- Blocks: 571651
- Forest area: 135709.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42777
- Scheduled area: 9501.21 ha
- Eligible blocks (age class >= 40): 427770
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.06 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 19.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
