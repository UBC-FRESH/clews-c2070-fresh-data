# WS4 tiled 30-m dataset — E23|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E23|ON|S33` (parent `E23|ON`)
- Tile / row / col: `E23` / 3 / 3
- Province: `ON`
- Centroid: 50.759214, -79.771897
- Allocated harvest: 17947.624344 m3
- Productive subcell area: 150321.252015 ha
- Committed geometry area: 181375.432422 ha
- Clipped inventory geometry: 181375.432422 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1577884
- Blocks: 517803
- Forest area: 142009.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45644
- Scheduled area: 11552.13 ha
- Eligible blocks (age class >= 40): 456439
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.68 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 19.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
