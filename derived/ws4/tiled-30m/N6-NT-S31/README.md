# WS4 tiled 30-m dataset — N6|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S31` (parent `N6|NT`)
- Tile / row / col: `N6` / 3 / 1
- Province: `NT`
- Centroid: 60.855663, -126.188482
- Allocated harvest: 60.316039 m3
- Productive subcell area: 40993.144882 ha
- Committed geometry area: 51892.344483 ha
- Clipped inventory geometry: 51892.344483 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 517641
- Blocks: 188439
- Forest area: 46587.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17293
- Scheduled area: 3660.93 ha
- Eligible blocks (age class >= 40): 172925
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.92 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 7.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
