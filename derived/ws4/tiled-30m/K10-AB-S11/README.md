# WS4 tiled 30-m dataset — K10|AB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K10|AB|S11` (parent `K10|AB`)
- Tile / row / col: `K10` / 1 / 1
- Province: `AB`
- Centroid: 58.010473, -112.320965
- Allocated harvest: 78980.366110 m3
- Productive subcell area: 180525.622718 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2544302
- Blocks: 553336
- Forest area: 228987.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48093
- Scheduled area: 13146.48 ha
- Eligible blocks (age class >= 40): 480930
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.70 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 25.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
