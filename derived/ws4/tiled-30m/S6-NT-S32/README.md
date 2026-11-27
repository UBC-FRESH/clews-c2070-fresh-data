# WS4 tiled 30-m dataset — S6|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|NT|S32` (parent `S6|NT`)
- Tile / row / col: `S6` / 3 / 2
- Province: `NT`
- Centroid: 66.859823, -133.315987
- Allocated harvest: 134.842717 m3
- Productive subcell area: 132117.922191 ha
- Committed geometry area: 233991.589107 ha
- Clipped inventory geometry: 233991.589107 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1060296
- Blocks: 393018
- Forest area: 95426.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24794
- Scheduled area: 7215.03 ha
- Eligible blocks (age class >= 40): 247936
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.91 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 13.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
