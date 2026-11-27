# WS4 tiled 30-m dataset — J7|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J7|AB|S33` (parent `J7|AB`)
- Tile / row / col: `J7` / 3 / 3
- Province: `AB`
- Centroid: 56.575243, -117.714246
- Allocated harvest: 68788.071280 m3
- Productive subcell area: 127335.026705 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2091545
- Blocks: 857398
- Forest area: 188239.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76678
- Scheduled area: 15737.13 ha
- Eligible blocks (age class >= 40): 766775
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.79 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 27.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
