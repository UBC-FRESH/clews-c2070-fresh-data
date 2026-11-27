# WS4 tiled 30-m dataset — F23|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F23|ON|S23` (parent `F23|ON`)
- Tile / row / col: `F23` / 2 / 3
- Province: `ON`
- Centroid: 51.452107, -79.547543
- Allocated harvest: 65.592683 m3
- Productive subcell area: 996.938381 ha
- Committed geometry area: 1452.881271 ha
- Clipped inventory geometry: 1452.881271 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 7761
- Blocks: 4025
- Forest area: 698.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3541
- Scheduled area: 636.48 ha
- Eligible blocks (age class >= 40): 3541
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.20 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
