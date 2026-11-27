# WS4 tiled 30-m dataset — M7|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S32` (parent `M7|BC`)
- Tile / row / col: `M7` / 3 / 2
- Province: `BC`
- Centroid: 59.979494, -121.669764
- Allocated harvest: 1761.664989 m3
- Productive subcell area: 4340.655399 ha
- Committed geometry area: 6081.267736 ha
- Clipped inventory geometry: 6081.267736 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 49157
- Blocks: 5591
- Forest area: 4424.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3589
- Scheduled area: 601.65 ha
- Eligible blocks (age class >= 40): 3589
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.51 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
