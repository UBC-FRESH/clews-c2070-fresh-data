# WS4 tiled 30-m dataset — H6|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|AB|S32` (parent `H6|AB`)
- Tile / row / col: `H6` / 3 / 2
- Province: `AB`
- Centroid: 53.380990, -118.960853
- Allocated harvest: 102233.609561 m3
- Productive subcell area: 127461.792719 ha
- Committed geometry area: 221040.932119 ha
- Clipped inventory geometry: 221040.932119 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 925545
- Blocks: 434268
- Forest area: 83299.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38983
- Scheduled area: 7011.18 ha
- Eligible blocks (age class >= 40): 389825
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.92 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 13.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
