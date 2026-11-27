# WS4 tiled 30-m dataset — E33|NS|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|NS|S31` (parent `E33|NS`)
- Tile / row / col: `E33` / 3 / 1
- Province: `NS`
- Centroid: 45.825211, -61.978568
- Allocated harvest: 3645.670166 m3
- Productive subcell area: 7585.273290 ha
- Committed geometry area: 9149.397585 ha
- Clipped inventory geometry: 9149.397585 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 92231
- Blocks: 31878
- Forest area: 8300.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2536
- Scheduled area: 499.32 ha
- Eligible blocks (age class >= 40): 25354
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.44 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
