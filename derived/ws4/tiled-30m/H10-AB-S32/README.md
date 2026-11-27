# WS4 tiled 30-m dataset — H10|AB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|AB|S32` (parent `H10|AB`)
- Tile / row / col: `H10` / 3 / 2
- Province: `AB`
- Centroid: 55.007606, -110.225025
- Allocated harvest: 49612.660126 m3
- Productive subcell area: 102048.407104 ha
- Committed geometry area: 141155.549251 ha
- Clipped inventory geometry: 141155.549251 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1413118
- Blocks: 533691
- Forest area: 127180.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49966
- Scheduled area: 11527.83 ha
- Eligible blocks (age class >= 40): 499651
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.71 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 18.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
