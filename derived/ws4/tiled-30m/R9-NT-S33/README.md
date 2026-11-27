# WS4 tiled 30-m dataset — R9|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R9|NT|S33` (parent `R9|NT`)
- Tile / row / col: `R9` / 3 / 3
- Province: `NT`
- Centroid: 67.897168, -121.163252
- Allocated harvest: 2.277543 m3
- Productive subcell area: 6125.131406 ha
- Committed geometry area: 228438.751974 ha
- Clipped inventory geometry: 228438.751974 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 40937
- Blocks: 29762
- Forest area: 3684.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3079
- Scheduled area: 319.86 ha
- Eligible blocks (age class >= 40): 3079
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.92 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
