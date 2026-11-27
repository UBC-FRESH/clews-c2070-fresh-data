# WS4 tiled 30-m dataset — H8|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H8|AB|S12` (parent `H8|AB`)
- Tile / row / col: `H8` / 1 / 2
- Province: `AB`
- Centroid: 53.404371, -114.148748
- Allocated harvest: 68172.895881 m3
- Productive subcell area: 119882.668469 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 892909
- Blocks: 386597
- Forest area: 80361.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29012
- Scheduled area: 6783.84 ha
- Eligible blocks (age class >= 40): 290116
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.05 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 12.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
