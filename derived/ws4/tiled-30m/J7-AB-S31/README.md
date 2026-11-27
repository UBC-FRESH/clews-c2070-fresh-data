# WS4 tiled 30-m dataset — J7|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J7|AB|S31` (parent `J7|AB`)
- Tile / row / col: `J7` / 3 / 1
- Province: `AB`
- Centroid: 56.243757, -119.259179
- Allocated harvest: 68788.071280 m3
- Productive subcell area: 127335.026705 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1401791
- Blocks: 527771
- Forest area: 126161.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45427
- Scheduled area: 10474.92 ha
- Eligible blocks (age class >= 40): 454264
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.82 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 18.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
