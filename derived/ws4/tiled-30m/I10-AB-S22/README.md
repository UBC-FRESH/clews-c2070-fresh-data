# WS4 tiled 30-m dataset — I10|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|AB|S22` (parent `I10|AB`)
- Tile / row / col: `I10` / 2 / 2
- Province: `AB`
- Centroid: 55.906155, -110.440860
- Allocated harvest: 81843.839310 m3
- Productive subcell area: 220561.949845 ha
- Committed geometry area: 247390.208267 ha
- Clipped inventory geometry: 247390.208267 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2528033
- Blocks: 771830
- Forest area: 227522.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69311
- Scheduled area: 17413.02 ha
- Eligible blocks (age class >= 40): 693108
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.94 MB
- Schedules: 0.82 MB
- Runs: 0.00 MB
- Total: 29.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
