# WS4 tiled 30-m dataset — S6|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|NT|S21` (parent `S6|NT`)
- Tile / row / col: `S6` / 2 / 1
- Province: `NT`
- Centroid: 66.237581, -133.388486
- Allocated harvest: 73.196111 m3
- Productive subcell area: 71717.022026 ha
- Committed geometry area: 127016.680793 ha
- Clipped inventory geometry: 127016.680793 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 799426
- Blocks: 219024
- Forest area: 71948.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13936
- Scheduled area: 3531.51 ha
- Eligible blocks (age class >= 40): 139359
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.87 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 9.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
