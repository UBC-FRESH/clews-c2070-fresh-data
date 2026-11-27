# WS4 tiled 30-m dataset — T6|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T6|YT|S12` (parent `T6|YT`)
- Tile / row / col: `T6` / 1 / 2
- Province: `YT`
- Centroid: 66.973581, -134.143185
- Allocated harvest: 5.669314 m3
- Productive subcell area: 2980.447996 ha
- Committed geometry area: 7170.268290 ha
- Clipped inventory geometry: 7170.268290 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 35865
- Blocks: 13587
- Forest area: 3227.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 636
- Scheduled area: 110.43 ha
- Eligible blocks (age class >= 40): 6360
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.60 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
