# WS4 tiled 30-m dataset — H6|AB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|AB|S23` (parent `H6|AB`)
- Tile / row / col: `H6` / 2 / 3
- Province: `AB`
- Centroid: 53.094082, -117.989570
- Allocated harvest: 115627.463861 m3
- Productive subcell area: 144160.847832 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1832902
- Blocks: 754158
- Forest area: 164961.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69695
- Scheduled area: 13499.55 ha
- Eligible blocks (age class >= 40): 696944
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.93 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 24.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
