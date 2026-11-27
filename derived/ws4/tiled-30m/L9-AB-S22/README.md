# WS4 tiled 30-m dataset — L9|AB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|AB|S22` (parent `L9|AB`)
- Tile / row / col: `L9` / 2 / 2
- Province: `AB`
- Centroid: 59.508861, -115.047330
- Allocated harvest: 98025.289357 m3
- Productive subcell area: 196257.628929 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2445136
- Blocks: 557908
- Forest area: 220062.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46895
- Scheduled area: 21588.57 ha
- Eligible blocks (age class >= 40): 468945
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.87 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 25.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
