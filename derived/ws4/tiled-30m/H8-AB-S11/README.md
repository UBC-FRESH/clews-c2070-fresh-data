# WS4 tiled 30-m dataset — H8|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H8|AB|S11` (parent `H8|AB`)
- Tile / row / col: `H8` / 1 / 1
- Province: `AB`
- Centroid: 53.266701, -114.874849
- Allocated harvest: 68172.895881 m3
- Productive subcell area: 119882.668469 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1591757
- Blocks: 692922
- Forest area: 143258.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60775
- Scheduled area: 12509.37 ha
- Eligible blocks (age class >= 40): 607747
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.44 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 22.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
