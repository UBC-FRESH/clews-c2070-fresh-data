# WS4 tiled 30-m dataset — F33|NS|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F33|NS|S22` (parent `F33|NS`)
- Tile / row / col: `F33` / 2 / 2
- Province: `NS`
- Centroid: 46.575867, -60.797241
- Allocated harvest: 47202.618768 m3
- Productive subcell area: 141463.887193 ha
- Committed geometry area: 165107.102000 ha
- Clipped inventory geometry: 165107.102000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1498896
- Blocks: 476110
- Forest area: 134900.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41025
- Scheduled area: 13069.62 ha
- Eligible blocks (age class >= 40): 410242
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.46 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 17.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
