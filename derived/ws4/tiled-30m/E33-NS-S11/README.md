# WS4 tiled 30-m dataset — E33|NS|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|NS|S11` (parent `E33|NS`)
- Tile / row / col: `E33` / 1 / 1
- Province: `NS`
- Centroid: 45.291529, -62.715951
- Allocated harvest: 99601.830411 m3
- Productive subcell area: 207234.080299 ha
- Committed geometry area: 249966.866215 ha
- Clipped inventory geometry: 249966.866215 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2390587
- Blocks: 693265
- Forest area: 215152.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49355
- Scheduled area: 9393.12 ha
- Eligible blocks (age class >= 40): 493545
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.37 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 26.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
