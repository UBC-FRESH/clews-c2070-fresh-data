# WS4 tiled 30-m dataset — C32|NS|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S12` (parent `C32|NS`)
- Tile / row / col: `C32` / 1 / 2
- Province: `NS`
- Centroid: 43.560905, -65.657111
- Allocated harvest: 17429.344080 m3
- Productive subcell area: 29022.501347 ha
- Committed geometry area: 34828.539438 ha
- Clipped inventory geometry: 34828.539438 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 285403
- Blocks: 66944
- Forest area: 25686.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5882
- Scheduled area: 2271.78 ha
- Eligible blocks (age class >= 40): 58816
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.40 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
