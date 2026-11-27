# WS4 tiled 30-m dataset — F7|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|AB|S22` (parent `F7|AB`)
- Tile / row / col: `F7` / 2 / 2
- Province: `AB`
- Centroid: 50.840412, -115.119316
- Allocated harvest: 115418.995529 m3
- Productive subcell area: 131949.603620 ha
- Committed geometry area: 231840.187856 ha
- Clipped inventory geometry: 231840.187856 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1587506
- Blocks: 804968
- Forest area: 142875.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76168
- Scheduled area: 13065.30 ha
- Eligible blocks (age class >= 40): 761679
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.88 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 23.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
