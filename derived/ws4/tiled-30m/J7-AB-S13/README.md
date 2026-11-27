# WS4 tiled 30-m dataset — J7|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J7|AB|S13` (parent `J7|AB`)
- Tile / row / col: `J7` / 1 / 3
- Province: `AB`
- Centroid: 55.713829, -117.146375
- Allocated harvest: 68788.071280 m3
- Productive subcell area: 127335.026705 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 813560
- Blocks: 263172
- Forest area: 73220.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22778
- Scheduled area: 6599.16 ha
- Eligible blocks (age class >= 40): 227778
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.86 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 10.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
