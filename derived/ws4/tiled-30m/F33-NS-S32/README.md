# WS4 tiled 30-m dataset — F33|NS|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F33|NS|S32` (parent `F33|NS`)
- Tile / row / col: `F33` / 3 / 2
- Province: `NS`
- Centroid: 46.862714, -60.544784
- Allocated harvest: 21790.917929 m3
- Productive subcell area: 65306.290968 ha
- Committed geometry area: 76221.095419 ha
- Clipped inventory geometry: 76221.095419 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 688217
- Blocks: 240885
- Forest area: 61939.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20879
- Scheduled area: 5048.19 ha
- Eligible blocks (age class >= 40): 208785
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.74 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 8.98 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
