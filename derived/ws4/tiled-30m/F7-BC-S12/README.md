# WS4 tiled 30-m dataset — F7|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|BC|S12` (parent `F7|BC`)
- Tile / row / col: `F7` / 1 / 2
- Province: `BC`
- Centroid: 50.350537, -115.050525
- Allocated harvest: 63433.258751 m3
- Productive subcell area: 95707.011760 ha
- Committed geometry area: 139601.646757 ha
- Clipped inventory geometry: 139601.646757 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 879021
- Blocks: 410572
- Forest area: 79111.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36023
- Scheduled area: 5725.35 ha
- Eligible blocks (age class >= 40): 360230
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.21 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 12.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
