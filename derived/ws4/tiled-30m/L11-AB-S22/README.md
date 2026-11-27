# WS4 tiled 30-m dataset — L11|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|AB|S22` (parent `L11|AB`)
- Tile / row / col: `L11` / 2 / 2
- Province: `AB`
- Centroid: 59.992044, -110.048457
- Allocated harvest: 134.272764 m3
- Productive subcell area: 635.873976 ha
- Committed geometry area: 823.338262 ha
- Clipped inventory geometry: 823.338262 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8015
- Blocks: 1273
- Forest area: 721.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1206
- Scheduled area: 713.07 ha
- Eligible blocks (age class >= 40): 1206
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.15 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
