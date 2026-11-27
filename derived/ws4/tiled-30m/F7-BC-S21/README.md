# WS4 tiled 30-m dataset — F7|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|BC|S21` (parent `F7|BC`)
- Tile / row / col: `F7` / 2 / 1
- Province: `BC`
- Centroid: 50.677010, -115.820940
- Allocated harvest: 109941.007801 m3
- Productive subcell area: 165877.105066 ha
- Committed geometry area: 241954.237214 ha
- Clipped inventory geometry: 241954.237214 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1840551
- Blocks: 910896
- Forest area: 165649.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 82601
- Scheduled area: 13345.92 ha
- Eligible blocks (age class >= 40): 826002
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.80 MB
- Schedules: 0.98 MB
- Runs: 0.00 MB
- Total: 26.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
